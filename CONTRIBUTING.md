# Contributing

English and Simplified Chinese contributions are welcome. Start with a concrete request that exposes a gap, then improve the responsible skill or propose a narrowly scoped new one. Avoid adding a universal gate for a single past failure.

## Source of truth

- Edit `catalog.json`, `guides/`, `templates/`, and the relevant standard-library utilities.
- Do not edit generated skill copies in isolation. Run `python scripts/build_catalog.py` after changing their sources.
- Keep existing/new project gates, frontend/backend boundaries, explicit stack choice, and proportional validation intact.
- Do not add private product rules, automatic installations, paid-service defaults, session uploads, or unauthorized external actions.

## Validate the change

```sh
python scripts/build_catalog.py
python scripts/validate.py
python scripts/run_examples.py
```

For changed utility behavior, use temporary synthetic fixtures outside the repository and cover the affected success, error, and boundary paths. Content-only edits do not require a new test framework or persistent test suite. For complex workflows, use scoped scenario review when authorized and useful. Report actual commands and results; format checks are not end-to-end agent validation.

The builder rejects undeclared leftover resources. When withdrawing a reference or template, inspect its callers and the generated manifest, then remove only the identified files. Do not reclassify obsolete resources as expected just to make validation pass.

Composition files use this project's schema 2. Maintain conditions, stage order, and the complete exportable capability set together. Validation selection must precede implementation. When TDD owns implementation, the separate implementation stage must not run again.

## Language and documentation

`README.md` is the English source overview. Translations are `README.zh-CN.md`, `README.zh-TW.md`, `README.ja.md`, `README.ko.md`, and `README.ru.md`. Update all six for changes to versions, counts, commands, workflow semantics, compatibility, or limitations. Keep the same meaning and disclose untranslated material. Skill instructions and detailed guides remain Chinese in this release; translating those is a separate change.

Contribution templates and release-facing documentation use English. A report or pull request may be written in either language. Do not invent maintainer affiliations, adoption numbers, support claims, test results, or repository-specific URLs.

## Pull requests

Describe the concrete trigger, final behavior, affected files, evidence, and remaining gaps. Include current primary sources when adding host compatibility or time-sensitive framework guidance. Pin borrowed references and check their exact license scope. Follow [SECURITY.md](SECURITY.md) for sensitive reports.

CI runs source checks, offline examples, and packaging dry runs on Windows and Linux. Check actual results for each pull request and release commit. Keep text in LF form as specified by `.gitattributes`; do not disable byte freshness or hash checks. New adapters must distinguish documentation mapping, discovery and end-to-end execution. Optional native probes require real clients and do not run in ordinary CI. See [loading validation](docs/agent-loading.md) and [tag release guidance](docs/github-publishing.md).
