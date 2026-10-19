"""Build a reproducible release from clean, validated, tracked HEAD bytes."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

sys.dont_write_bytecode = True
from catalog_files import load_catalog, no_links, relative_name

ROOT = Path(__file__).resolve().parents[1]


def new_output(path):
    path = path.absolute()
    no_links(path)
    resolved = path.resolve()
    if path.exists() or resolved.is_relative_to(ROOT) or ROOT.is_relative_to(resolved):
        raise ValueError("output must be a new directory outside the source tree")
    for parent in (resolved, *resolved.parents):
        if parent.name.lower() in {".agents", ".claude", ".codex", ".gemini", ".copilot", ".github"}:
            raise ValueError("output cannot be inside an agent configuration directory")
    return path


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True).stdout


def tracked_source():
    if git("status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError("commit or remove all working-tree changes before packaging")
    records = []
    names = set()
    for record in git("ls-tree", "-rz", "--full-tree", "HEAD").split(b"\0"):
        if not record:
            continue
        metadata, raw_name = record.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        name = relative_name(raw_name.decode("utf-8"))
        if mode not in {b"100644", b"100755"} or kind != b"blob":
            raise ValueError("release accepts regular files only: " + name)
        if name.casefold() in names:
            raise ValueError("case-colliding archive path: " + name)
        names.add(name.casefold())
        no_links(ROOT / name)
        records.append((name, oid))
    # Batch reads avoid one subprocess per file and use committed bytes on every OS.
    response = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "--batch"],
        input=b"".join(oid + b"\n" for _, oid in records),
        check=True, capture_output=True,
    ).stdout
    stream = io.BytesIO(response)
    result = {}
    for name, oid in records:
        actual_oid, kind, size = stream.readline().split()
        if actual_oid != oid or kind != b"blob":
            raise ValueError("unexpected Git object response")
        data = stream.read(int(size))
        if stream.read(1) != b"\n" or (ROOT / name).read_bytes() != data:
            raise ValueError("checkout bytes differ from HEAD: " + name)
        result[name] = data
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True, help="exact stable tag, for example v1.2.0")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        target = new_output(args.out)
        version = load_catalog(ROOT)["version"]
        if not re.fullmatch(r"v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", args.tag) or args.tag != "v" + version:
            raise ValueError("tag must exactly match catalog version v" + version)
        files = tracked_source()
        check = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate.py")], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if check.returncode:
            raise ValueError("source validation failed: " + check.stdout.strip())
        notes = files["docs/release-notes.md"]
        if not notes.decode("utf-8").startswith("# " + args.tag + " — "):
            raise ValueError("release notes heading must match the tag")
        buffer = io.BytesIO()
        # Stored entries avoid zlib-version differences between platforms.
        with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, data in sorted(files.items()):
                info = zipfile.ZipInfo("agent-workflow-skills/" + name, (1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        packed = buffer.getvalue()
        with zipfile.ZipFile(io.BytesIO(packed)) as archive:
            if archive.testzip() is not None or len(archive.namelist()) != len(files):
                raise ValueError("archive integrity check failed")
            for name, data in files.items():
                if archive.read("agent-workflow-skills/" + name) != data:
                    raise ValueError("archive content mismatch")
        filename = "agent-workflow-skills-" + version + ".zip"
        digest = hashlib.sha256(packed).hexdigest()
        # All validation above happens before creating any output.
        target.mkdir(parents=True, exist_ok=False)
        (target / filename).write_bytes(packed)
        (target / (filename + ".sha256")).write_text(digest + "  " + filename + "\n", encoding="ascii", newline="\n")
        (target / "RELEASE_NOTES.md").write_bytes(notes)
        print(json.dumps({"tag": args.tag, "commit": git("rev-parse", "HEAD").decode().strip(), "files": len(files), "archive": filename, "sha256": digest, "bytes": len(packed)}))
        return 0
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print("release error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
