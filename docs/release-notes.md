# v1.4.1 — Standalone page design without a product workflow

This patch separates requirements, page drafts and isolated display prototypes from formal product implementation. A single page can be designed without creating a project, choosing a production stack, completing an unrelated codebase audit or establishing a whole design system. Existing rules and relevant page constraints are still read; product integration retains all existing/new project gates.

- Add conditional standalone-page guidance to aw-ui-design and route by deliverable in triage, requirements, skill selection and composition conditions.
- Require a viewable artifact when the user asks to see the page; prototype simulation is not real business functionality.
- Existing-product pages first inspect incumbent UI and style/component sources, including global typography and theme. Unrelated business flows, missing design documents or an isolated prototype do not authorize a new visual identity.
- Preserve the requested page/prototype deliverable separately from temporary P1 validation artifacts.
- Retain 26 skills, eight compositions and the same 11-repository/54-file provenance ledger. No upstream tools, new runtime dependencies or default skill installations are added.

## Design capabilities retained from 1.4.0

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

See [the validation record](validation.md) for revision-specific structural, export and scenario checks. Source-hash and other historical checks retain their recorded version scope. Synthetic responses do not demonstrate real application execution or establish a cross-model effectiveness benchmark.

Native discovery records for Codex and Claude belong to 1.2.0 and its 24 skills. Discovery of the current 26-skill set was not rerun. No real product screens, native devices or model-driven end-to-end workflows were validated in this update. Check Actions for CI results on the actual commit; local preparation does not establish remote CI success.

Original material remains MIT-licensed. Upstream material retains its own license, including Trail of Bits CC-BY-SA-4.0; no upstream skill bodies, translations, implementations, datasets or assets are bundled.

The SHA-256 sidecar applies only to the named prepared ZIP. Preparing this source does not publish a release, install skills or change default agent settings.
