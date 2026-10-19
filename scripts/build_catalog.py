"""Synchronize declared skills after checking every source and destination."""
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
from catalog_files import existing_files, expected_contents, expected_files, load_catalog, no_links, safe_path

ROOT = Path(__file__).resolve().parents[1]


def main():
    try:
        catalog = load_catalog(ROOT)
        expected_names = {row["name"] for row in catalog["skills"]}
        skills_root = safe_path(ROOT, "skills")
        if skills_root.exists():
            for path in skills_root.iterdir():
                no_links(path)
                if not path.is_dir() or path.name not in expected_names:
                    raise ValueError("undeclared skill directory: " + path.name)
        plan = []
        for row in catalog["skills"]:
            folder = safe_path(ROOT, "skills/" + row["name"])
            extras = existing_files(folder) - expected_files(row)
            if extras:
                raise ValueError(row["name"] + ": review obsolete files before rebuilding: " + str(sorted(extras)))
            for relative, data in expected_contents(ROOT, row).items():
                target = safe_path(folder, relative)
                if target.exists() and not target.is_file():
                    raise ValueError("generated file target is not a regular file: " + str(target))
                plan.append((target, data))
        manifest_path = safe_path(ROOT, "provenance/generated-files.json")
        if manifest_path.exists() and not manifest_path.is_file():
            raise ValueError("manifest target is not a regular file")
        # No mutations before all declarations, sources and output paths pass.
        for target, data in plan:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(data).hexdigest() for p, data in plan}
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"skills_generated": len(catalog["skills"]), "version": catalog["version"], "installed": False}))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("build error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
