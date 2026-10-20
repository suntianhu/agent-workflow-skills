# Repository maintenance

This repository contains generic Agent Skills, not product code.
Keep one responsibility per skill and preserve existing/new frontend/backend gates.
Edit catalog.json and guides first; run python scripts/build_catalog.py to synchronize generated skills.
Run python scripts/validate.py after changes; do not add persistent test suites for content-only edits.
Use task-owned temporary fixtures within the authorized local project workspace for script behavior checks; keep them separate from distribution sources, do not default to system TEMP, and verify task-scoped cleanup.
Do not install skills, alter user configuration, publish, or operate external accounts without explicit authorization.
Keep private product rules, credentials, user data, and machine-specific paths out of the distribution.
Document actual validation separately from format compatibility and untested agent runtimes.
Use only task-relevant skills and references; reuse valid project decisions instead of reopening completed stages.
Before modifying an existing user Skill, show the exact proposal and obtain explicit confirmation; preserve partial work and project rules.
For routine releases increment the latest published patch; preserve published tags and record substantial version changes explicitly in docs/versioning.md.
