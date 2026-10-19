"""Execute offline utility examples in a new temporary directory, never a product."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import uuid

sys.dont_write_bytecode = True
from build_release import ROOT, new_output


def run(script, *args, expected=0):
    result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / script), *map(str, args)], capture_output=True, text=True, encoding="utf-8")
    if result.returncode != expected:
        raise ValueError(script + " returned " + str(result.returncode) + ": " + result.stderr)
    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, help="new directory under the system temporary directory")
    args = parser.parse_args()
    try:
        target = new_output(args.out or Path(tempfile.gettempdir()) / ("aw-examples-" + uuid.uuid4().hex))
        if not target.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise ValueError("examples require a system temporary directory")
        target.mkdir(parents=True)
        project = target / "fixture"
        project.mkdir()
        source = project / "service.py"
        source.write_text("def status():\n    return {'ready': True}\n", encoding="utf-8")
        inventory, ledger = target / "inventory.json", target / "ledger.json"
        scan = run("repo_audit.py", "scan", "--root", project, "--out", inventory, "--ledger", ledger)
        # An empty ledger must not authorize implementation in an existing project.
        ledger.write_text(json.dumps({"schema": 1, "files": []}), encoding="utf-8")
        blocked = run("repo_audit.py", "check", "--inventory", inventory, "--ledger", ledger, expected=2)
        forecast = run("estimate.py", "forecast", "--kind", "docs-example", "--work", 10, "--checks", 1, "--review", 1, "--prior", 0.5, "--unknown", "external CI queue")
        exported = run("export_bundle.py", "--bundle", "small-change", "--out", target / "composition")
        bundle = json.loads((target / "composition/BUNDLE.json").read_text(encoding="utf-8"))
        copied = 0
        for name in bundle["exported_skills"]:
            for original in (ROOT / "skills" / name).rglob("*"):
                if original.is_file():
                    copy = target / "composition/skills" / name / original.relative_to(ROOT / "skills" / name)
                    if hashlib.sha256(original.read_bytes()).digest() != hashlib.sha256(copy.read_bytes()).digest():
                        raise ValueError("exported resource differs from source")
                    copied += 1
        if scan["reading_complete"] or blocked["gate_passed"] or forecast["comparable_samples"] != 0 or forecast["local_minutes"]["likely"] != 7 or exported["installed"]:
            raise ValueError("example did not preserve its documented gate")
        report = {
            "schema": 1,
            "version": json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))["version"],
            "passed": True,
            "examples": {
                "existing_project_empty_ledger": "blocked",
                "estimate_explicit_prior": {"samples": 0, "local_minutes": forecast["local_minutes"], "unknown": "external CI queue"},
                "small_change_export": {"skills": exported["exported_skills"], "byte_identical_files": copied, "installed": False},
            },
            "model_execution": "not_run",
            "fixtures": "synthetic; not real calibration samples or product acceptance",
        }
        (target / "result.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print("example error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
