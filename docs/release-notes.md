# v1.3.3 — Clearer READMEs and explicit conditional branches

29 skills and nine conditional compositions.

## Changes

- Remove the actual-evidence column and historical validation-result paragraphs from all six READMEs. Keep installation guidance, validation commands and separate historical records.
- Use explicit branches instead of ternary operators for new or modified frontend and backend conditional logic. Split long conditions into meaningful variables or helpers, then use if/else, early returns or equivalent clear branches.
- Preserve short-circuit evaluation, null guards and side-effect timing. Apply the rule to the requested changes without refactoring unrelated historical code.

## Scope

The catalog and source guides generate the two implementation skills and their portable references. No new skill, composition, persistent test suite or utility behavior is introduced. Existing project gates and test policies remain in force.

See [CHANGELOG](../CHANGELOG.md), [version history](versioning.md) and [GitHub publishing](github-publishing.md).
