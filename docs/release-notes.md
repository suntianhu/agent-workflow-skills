# v1.3.1 — Verify real data and complete business paths

29 skills and nine conditional compositions. This patch strengthens the existing debugging, API-contract, test-strategy and evidence-verification responsibilities after a missed data-identity assumption.

## Changes

- Verify actual schema, unique constraints, relevant existing data and match counts before selecting a fix. An id/key name or single-row fixture does not establish uniqueness.
- Follow the complete affected business path: entry identity, lookup, validation, writes, rereads/authentication and the resulting response. Check that every stage addresses the same object and that the deployed build contains the change.
- Select relevant duplicate-identifier, multi-account/tenant and historical-data counterexamples. Confirm that unselected objects and their metadata remain unchanged.
- Keep a defect pending when critical real-data or business-path evidence is missing. Compilation and test doubles do not establish a fix; adding an integration disclaimer does not make an unconditional completion claim valid.
- Regenerate portable skills and align all six README languages. Existing authorization, test/retention policies, utility behavior, skill identities and composition counts remain in force.

## Evidence and limits

Source validation, generated freshness, offline utility examples, static scenario review and reproducible tracked-source packaging each support their stated scope. Actual source results are recorded in [validation](validation.md); Windows/Linux CI, main/tag alignment, release assets and the authorized local Codex update are checked separately after execution.

No persistent test suite, skill or composition is added. Static scenario review and native skill discovery do not establish model adherence, automatic triggering or product acceptance. Historical evidence keeps its original version and scope. Real-data investigation remains subject to existing authorization and does not permit changing real credentials or business data to obtain a passing result.

See [CHANGELOG](../CHANGELOG.md), [version history](versioning.md), [validation](validation.md) and [GitHub publishing](github-publishing.md).
