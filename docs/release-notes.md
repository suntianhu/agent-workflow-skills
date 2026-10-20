# v1.2.4 — Precise bug fixes and affected behavior regression checks

Patch release for 26 skills and eight conditional compositions. Existing published tags are preserved.

## Changes

- Fix defects in the existing business module with the smallest sufficient change. Reuse the same responsibility across retries and explain necessary new business files instead of accumulating repair copies.
- Remove or merge branches, duplicate logic, temporary fallbacks and references invalidated by the fix. Check dynamic callers and compatibility uses before removal, and keep unrelated historical cleanup outside the repair.
- Check the original defect, affected normal consumers and applicable failure/recovery paths under the existing test policy. Shared changes require attention to their real consumers.
- Review the final diff for unrelated formatting, renames, file moves, dependency upgrades and architectural rewrites. Necessary migrations and compatible legacy paths remain supported.
- Apply these rules to five existing skills and their guides; preserve the skill/composition counts, project gates, test policy and authorization boundaries.

## Evidence and limits

Source validation, offline utility examples and reproducible tracked-source packaging are the release checks. The current five-skill update was synchronized to the local installation: all 126 skill files matched source, and native Windows Codex discovery found 26 enabled skills without parser errors. Historical isolated Codex/Claude discovery and Web demo checks retain their original scope. Discovery and content review do not prove model execution, automatic trigger accuracy, product regression coverage or productivity gains.

See [CHANGELOG](../CHANGELOG.md), [version history](versioning.md) and [validation](validation.md). No community posts are sent by this release.
