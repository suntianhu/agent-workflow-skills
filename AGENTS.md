# Repository maintenance

This repository contains generic Agent Skills, not product code.
Keep one responsibility per skill and preserve existing/new frontend/backend gates.
Edit catalog.json and guides first; run python scripts/build_catalog.py to synchronize generated skills.
Run python scripts/validate.py after changes; do not add persistent test suites for content-only edits.
Use temporary fixtures outside this repository for script behavior checks.
Do not install skills, alter user configuration, publish, or operate external accounts without explicit authorization.
Keep private product rules, credentials, user data, and machine-specific paths out of the distribution.
Document actual validation separately from format compatibility and untested agent runtimes.
