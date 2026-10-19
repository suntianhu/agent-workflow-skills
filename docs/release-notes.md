# v1.3.1 — Project skill directories and bounded native validation

Agent Workflow Skills retains 24 skills, eight compositions and the specialist references from 1.3.0. This patch clarifies project standards placement and prevents temporary TDD checks from accumulating or validating substitute implementations.

## Changes

- Reuse existing project standards directories; fall back to docs/engineering only when no convention exists.
- Provide a thin project-level skill template in the project host's actual discovery directory, referencing the same canonical standards with verified relative paths. Do not use global skill directories or duplicate standards per host.
- Select existing native test languages, runtimes, roots and scoped commands. A Python rewrite or source-text check does not demonstrate Java/frontend behavior; real cross-language black-box checks retain their narrower evidence scope.
- Reuse the same TDD carrier across retries. P1 temporary files and assertions do not become persistent additions, while P2 additions need actual regression value and a maintenance location.
- Clean only agreed task-owned temporary artifacts, preserving existing tests and other user changes. See [the detailed policy](project-standards-and-tdd.md).

## Validation and limits

See [the validation record](validation.md) for actual structural, export, source-hash, scenario and archive checks on this revision. Synthetic scenario responses do not demonstrate real browser, database or application execution and are not a cross-model effectiveness benchmark.

Native discovery records for Codex and Claude belong to 1.2.0. Native discovery was not rerun for 1.3.0. Gemini, Copilot, other platforms and end-to-end agent workflows remain outside that evidence. Check Actions for CI results on the actual release commit; local preparation does not establish remote CI success.

Original material remains MIT-licensed. Upstream material retains its own license, including Trail of Bits CC-BY-SA-4.0; no upstream skill bodies, translations, implementations, datasets or assets are bundled.

The SHA-256 sidecar applies only to the named prepared ZIP. Preparing this source does not publish a release, install skills or change default agent settings.
