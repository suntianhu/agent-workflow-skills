"""Probe native discovery in TEMP. No authentication, installation or model turns."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid

sys.dont_write_bytecode = True
from build_release import ROOT, new_output
from catalog_files import check_skill, load_catalog


def defaults_snapshot():
    result = {}
    for owner in (".codex", ".agents", ".claude"):
        root = Path.home() / owner / "skills"
        rows = []
        if root.exists():
            for directory, dirs, files in os.walk(root, followlinks=False):
                for name in sorted(dirs + files):
                    path = Path(directory) / name
                    relative = path.relative_to(root).as_posix()
                    redirected = path.is_symlink() or bool(getattr(path.lstat(), "st_file_attributes", 0) & 0x400)
                    if redirected:
                        rows.append((relative, "link", os.readlink(path)))
                        if name in dirs:
                            dirs.remove(name)
                    elif path.is_file():
                        rows.append((relative, "file", hashlib.sha256(path.read_bytes()).hexdigest()))
        digest = hashlib.sha256(json.dumps(sorted(rows), ensure_ascii=True).encode()).hexdigest()
        result[owner] = {"exists": root.exists(), "entries": len(rows), "sha256": digest}
    return result


def isolated_env(target):
    # Allow OS/runtime basics only. No inherited tokens, provider config or CLI overrides.
    allowed = {"PATH", "PATHEXT", "SYSTEMROOT", "WINDIR", "COMSPEC", "SYSTEMDRIVE", "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "LANG", "LC_ALL"}
    env = {k: v for k, v in os.environ.items() if k.upper() in allowed}
    for variable, folder in {
        "HOME": "home", "USERPROFILE": "home", "CODEX_HOME": "codex", "CLAUDE_CONFIG_DIR": "claude",
        "APPDATA": "appdata", "LOCALAPPDATA": "localappdata", "XDG_CONFIG_HOME": "xdg-config",
        "XDG_DATA_HOME": "xdg-data", "TMP": "tmp", "TEMP": "tmp", "TMPDIR": "tmp",
    }.items():
        path = target / folder
        path.mkdir(exist_ok=True)
        env[variable] = str(path)
    env.update(PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1", DISABLE_AUTOUPDATER="1", DISABLE_TELEMETRY="1", DISABLE_ERROR_REPORTING="1", CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
    return env


def codex_probe(executable, project, env, target):
    messages = queue.Queue()
    with (target / "codex-private.log").open("w", encoding="utf-8") as log:
        process = subprocess.Popen([executable, "app-server", "--listen", "stdio://"], cwd=project, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=log, text=True, encoding="utf-8")
        def read():
            for line in process.stdout:
                try:
                    messages.put(json.loads(line))
                except json.JSONDecodeError:
                    continue
        threading.Thread(target=read, daemon=True).start()
        def request(identity, method, params):
            process.stdin.write(json.dumps({"id": identity, "method": method, "params": params}) + "\n")
            process.stdin.flush()
            until = time.monotonic() + 25
            while time.monotonic() < until:
                try:
                    reply = messages.get(timeout=max(0.1, until - time.monotonic()))
                except queue.Empty:
                    break
                if reply.get("id") == identity:
                    if "error" in reply:
                        raise ValueError("native Codex request failed; inspect private log")
                    return reply["result"]
            raise ValueError("native Codex initialization timed out")
        try:
            request(1, "initialize", {"clientInfo": {"name": "aw-isolated-probe", "version": "1.2.0"}, "capabilities": {"experimentalApi": True}})
            process.stdin.write('{"method":"initialized","params":{}}\n')
            process.stdin.flush()
            data = request(2, "skills/list", {"cwds": [str(project)], "forceReload": True})["data"]
            if len(data) != 1 or data[0].get("errors"):
                raise ValueError("native Codex skill parser returned errors")
            skills = data[0]["skills"]
            if not all(s.get("enabled", True) and Path(s["path"]).resolve().is_relative_to(project) for s in skills):
                raise ValueError("disabled skill or a skill loaded outside isolation")
            return sorted(s["name"] for s in skills)
        finally:
            process.stdin.close()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait(timeout=5)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["codex", "claude", "both"], required=True)
    parser.add_argument("--out", type=Path, help="new directory below system TEMP")
    parser.add_argument("--codex-exe", default=shutil.which("codex"))
    parser.add_argument("--claude-exe", help="absolute native Claude executable, not an npm shell shim")
    parser.add_argument("--claude-sdk", type=Path, help="existing official SDK sdk.mjs; no auto-install")
    args = parser.parse_args()
    report = {"schema": 1, "model_execution": "not_run", "authentication_used": False, "hosts": {}}
    before = defaults_snapshot()
    target = None
    code = 2
    try:
        target = new_output(args.out or Path(tempfile.gettempdir()) / ("aw-loading-" + uuid.uuid4().hex))
        if not target.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise ValueError("probe requires a system temporary directory")
        hosts = ["codex", "claude"] if args.host == "both" else [args.host]
        if "codex" in hosts and not args.codex_exe:
            raise ValueError("Codex executable is required")
        if "claude" in hosts and (not args.claude_exe or not args.claude_sdk or not args.claude_sdk.is_file() or not shutil.which("node")):
            raise ValueError("Claude native executable, official SDK sdk.mjs and Node are required")
        catalog = load_catalog(ROOT)
        expected = sorted(row["name"] for row in catalog["skills"])
        for row in catalog["skills"]:
            check_skill(ROOT, row)
        target.mkdir(parents=True)
        env = isolated_env(target)
        for host in hosts:
            project = target / (host + "-project")
            project.mkdir()
            subprocess.run(["git", "-c", "init.templateDir=", "init", "--quiet", str(project)], env=env, check=True, capture_output=True)
            destination = project / (".agents" if host == "codex" else ".claude") / "skills"
            shutil.copytree(ROOT / "skills", destination)
            if host == "codex":
                executable = str(Path(args.codex_exe).resolve())
                names = codex_probe(executable, project, env, target)
            else:
                executable = str(Path(args.claude_exe).resolve())
                debug = target / "claude-private.log"
                subprocess.run([executable, "--init-only", "--debug-file", str(debug)], cwd=project, env=env, check=True, capture_output=True, timeout=40)
                if not re.search(r"Loaded " + str(len(expected)) + r" unique skills .*user: 0, project: " + str(len(expected)) + r",", debug.read_text(encoding="utf-8")):
                    raise ValueError("Claude native loader count/scope did not match")
                config = target / "sdk-input-private.json"
                config.write_text(json.dumps({"sdk": str(args.claude_sdk.resolve()), "project": str(project), "executable": executable}), encoding="utf-8")
                result = subprocess.run(["node", str(ROOT / "scripts/claude_discovery.mjs"), str(config)], cwd=project, env=env, capture_output=True, text=True, encoding="utf-8", timeout=40)
                if result.returncode:
                    (target / "sdk-private.log").write_text(result.stderr, encoding="utf-8")
                    raise ValueError("Claude SDK discovery failed; inspect private log")
                names = json.loads(result.stdout)["names"]
            if names != expected:
                raise ValueError(host + " returned a different skill set")
            version = subprocess.run([executable, "--version"], env=env, capture_output=True, text=True, encoding="utf-8", check=True, timeout=20).stdout.strip()
            report["hosts"][host] = {"version": version, "native_discovery": "passed", "count": len(names), "names": names}
        report["version"] = catalog["version"]
        report["passed"] = True
        code = 0
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        report.update(passed=False, error=str(error))
    finally:
        after = defaults_snapshot()
        report["default_skills"] = {"unchanged": before == after, "before": before, "after": after}
        if before != after:
            report["passed"] = False
            code = 2
        if target and target.is_dir():
            (target / "result.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
