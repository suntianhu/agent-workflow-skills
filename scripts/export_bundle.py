"""Export a validated composition outside this collection; never install or overwrite."""
import argparse
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True
from catalog_files import check_skill, expected_contents, load_bundle, load_catalog, no_links, safe_path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--include-optional", action="store_true")
    args = parser.parse_args()
    try:
        catalog = load_catalog(ROOT)
        bundle = load_bundle(ROOT, args.bundle, catalog)
        target = args.out.absolute()
        no_links(target)
        resolved = target.resolve()
        if target.exists() or resolved.is_relative_to(ROOT.resolve()) or ROOT.resolve().is_relative_to(resolved):
            raise ValueError("export requires a new directory outside the collection")
        for location in (target, resolved):
            parts = [part.lower() for part in location.parts]
            if any(parts[i] in {".agents", ".claude", ".gemini", ".github", ".copilot", ".codex"} and parts[i + 1] == "skills" for i in range(len(parts) - 1)):
                raise ValueError("export cannot target native skill discovery/install locations")
        names = bundle["skills"] + (bundle["optional"] if args.include_optional else [])
        rows = {row["name"]: row for row in catalog["skills"]}
        plan = []
        for name in names:
            check_skill(ROOT, rows[name])
            for relative, data in expected_contents(ROOT, rows[name]).items():
                plan.append(("skills/" + name + "/" + relative, data))
        for relative in ("LICENSE", "THIRD_PARTY_NOTICES.md", "provenance/upstreams.json"):
            plan.append((relative, safe_path(ROOT, relative).read_bytes()))
        exported = dict(bundle, collection_version=catalog["version"], exported_skills=names)
        plan.append(("BUNDLE.json", (json.dumps(exported, ensure_ascii=False, indent=2) + "\n").encode("utf-8")))
        readme = "# Exported composition\n\nRead BUNDLE.json for stage conditions. This is not an installed or executable workflow.\n\n" + "\n".join("- [" + name + "](skills/" + name + "/SKILL.md)" for name in names) + "\n"
        plan.append(("README.md", readme.encode("utf-8")))
        target.mkdir(parents=True, exist_ok=False)
        for relative, data in plan:
            path = safe_path(target, relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        print(json.dumps({"exported_skills": len(names), "directory": str(target), "version": catalog["version"], "installed": False}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("export error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
