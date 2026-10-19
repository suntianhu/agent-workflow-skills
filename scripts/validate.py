"""Read-only checks of schemas, generated freshness, references and public files."""
from pathlib import Path
import ast
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
from catalog_files import check_skill, expected_files, existing_files, load_bundle, load_catalog, read_json, safe_path

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    try:
        catalog = load_catalog(ROOT)
        rows = catalog["skills"]
        names = {row["name"] for row in rows}
        actual = {p.name for p in safe_path(ROOT, "skills").iterdir()}
        if actual != names:
            errors.append("catalog and skill directory sets differ")
        for row in rows:
            try:
                check_skill(ROOT, row)
                text = safe_path(ROOT, "skills/" + row["name"] + "/SKILL.md").read_text(encoding="utf-8")
                if len(text.splitlines()) > 100:
                    errors.append(row["name"] + ": entrypoint too long")
            except (OSError, ValueError, KeyError, TypeError) as error:
                errors.append(str(error))
        files = existing_files(ROOT, exclude_dirs={".git"})
        user_path = re.compile(r"(?:[A-Z]:[\\/](?:Users|home)[\\/]|/(?:Users|home)/)[a-z0-9._-]+[\\/]", re.I)
        key_material = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
        for relative in sorted(files):
            if relative.startswith(".git/"):
                continue
            path = safe_path(ROOT, relative)
            if "__pycache__" in path.parts or path.suffix == ".pyc":
                errors.append(relative + ": compiled residue")
            if path.name in {".env", "test.env", ".npmrc", ".pypirc"} or path.name.startswith(".env."):
                errors.append(relative + ": runtime/sensitive configuration is not part of this distribution")
            if path.suffix not in {".md", ".json", ".py", ".yaml", ".yml", ".txt"} and path.name not in {"LICENSE", ".gitignore", ".gitattributes"}:
                errors.append(relative + ": unexpected distribution file type")
                continue
            text = path.read_text(encoding="utf-8")
            if user_path.search(text):
                errors.append(relative + ": machine-specific user path")
            if key_material.search(text):
                errors.append(relative + ": private key material")
            if path.suffix == ".py":
                try:
                    ast.parse(text, filename=relative)
                except SyntaxError as error:
                    errors.append(str(error))
            if path.suffix == ".md":
                for target in re.findall(r"\]\(([^)]+)\)", text):
                    target = target.split("#")[0]
                    if not target or re.match(r"https?://|mailto:", target):
                        continue
                    resolved = (path.parent / target).resolve()
                    if not resolved.is_relative_to(ROOT) or not resolved.exists():
                        errors.append(relative + ": missing or escaping local link " + target)
        bundles = sorted(safe_path(ROOT, "bundles").glob("*.json"))
        for path in bundles:
            try:
                load_bundle(ROOT, path.stem, catalog)
            except (OSError, ValueError, KeyError, TypeError) as error:
                errors.append(str(error))
        generated = read_json(safe_path(ROOT, "provenance/generated-files.json"))
        allowed = {"skills/" + row["name"] + "/" + p for row in rows for p in expected_files(row)}
        if not isinstance(generated, dict) or set(generated) != allowed:
            errors.append("generated manifest differs from exact catalog set")
        else:
            for relative, digest in generated.items():
                path = safe_path(ROOT, relative)
                if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                    errors.append(relative + ": generated hash mismatch")
        result = {"skills": len(rows), "bundles": len(bundles), "version": catalog["version"], "errors": errors, "passed": not errors}
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {"errors": [str(error)], "passed": False}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
