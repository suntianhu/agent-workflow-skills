# v1.4.0 — Cross-platform design research and project standards

Agent Workflow Skills now provides 26 skills and eight compositions. Design reference research and shared project design standards connect requirements brainstorming to page/flow design across Web, mini-programs, native apps, desktop and cross-platform interfaces.

## Changes

- Add aw-design-reference for evidence-backed adoption of platform guidance, systems and examples; aw-design-standards for shared content, tokens/components, accessibility and platform mappings.
- Expand proportional brainstorming and keep shared rules separate from page/flow UI. Preserve existing design documents and the same project standards entry.
- Add conditional platform guidance and design stages to five UI-capable compositions; API-only tasks skip UI, local edits reuse existing rules.
- Extend the source ledger to 11 repositories and 54 selected files, including licenses/notices. Record design website access and unavailable bodies separately.

The following project-directory and native validation policies from 1.3.1 remain:

- Reuse existing project standards directories; fall back to docs/engineering only when no convention exists.
- Provide a thin project-level skill template in the project host's actual discovery directory, referencing the same canonical standards with verified relative paths. Do not use global skill directories or duplicate standards per host.
- Select existing native test languages, runtimes, roots and scoped commands. A Python rewrite or source-text check does not demonstrate Java/frontend behavior; real cross-language black-box checks retain their narrower evidence scope.
- Reuse the same TDD carrier across retries. P1 temporary files and assertions do not become persistent additions, while P2 additions need actual regression value and a maintenance location.
- Clean only agreed task-owned temporary artifacts, preserving existing tests and other user changes. See [the detailed policy](project-standards-and-tdd.md).

## Validation and limits

See [the validation record](validation.md) for actual structural, export, source-hash, scenario and archive checks on this revision. Synthetic scenario responses do not demonstrate real browser, database or application execution and are not a cross-model effectiveness benchmark.

Native discovery records for Codex and Claude belong to 1.2.0 and its 24 skills. Discovery of the current 26-skill set was not rerun. No real product screens, native devices or model-driven end-to-end workflows were validated in this update. Check Actions for CI results on the actual commit; local preparation does not establish remote CI success.

Original material remains MIT-licensed. Upstream material retains its own license, including Trail of Bits CC-BY-SA-4.0; no upstream skill bodies, translations, implementations, datasets or assets are bundled.

The SHA-256 sidecar applies only to the named prepared ZIP. Preparing this source does not publish a release, install skills or change default agent settings.
