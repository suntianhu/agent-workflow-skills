# Agent Workflow Skills

Composable development workflows for coding agents, with explicit project gates and evidence before completion.

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 26](https://img.shields.io/badge/skills-26-2563eb)
![Workflows: 8](https://img.shields.io/badge/workflows-8-0f766e)

**Version 1.4.2** · Agent Skills directories · Python 3.10+ utilities · No runtime dependencies beyond the Python standard library

Version 1.4.2 connects design reference research and project design standards: 26 skills and eight compositions now connect brainstorming, platform guidance, shared rules and page design across Web, mini-programs, native apps, desktop and cross-platform UI. See [the design workflow](docs/design-workflow.md), [sources](docs/provenance.md) and [launch copy](docs/promotion.en.md). Native discovery below belongs to 1.2.0; discovery of the current 26-skill set has not been rerun. A standalone page draft or isolated prototype can be delivered without starting a product project; product integration retains the normal development gates. Verified baselines and completed prerequisites are reused by evidence, with separate conditions for real gaps. See the [26-skill workflow audit](docs/workflow-audit.md).

Build on an existing codebase or start a new project without mixing the two workflows. Select only the skills that fit the task. Keep frontend and backend conventions separate, choose validation before implementation, and report what was actually verified.

## Why this collection

- **Existing skills stay connected:** inventory project skills and agent/plugin rules, then align later skill adoption with the same project standards and prior decisions.
- **Existing projects:** review all project-owned code and write evidence-backed standards inside the project before changing code, configuration, or engineering scripts.
- **New projects:** respect the requested language, research maintained frameworks and known relevant risks, obtain the user's stack choice, then derive conventions from matching public repositories.
- **Proportional validation:** decide scope, TDD order, and artifact retention separately. Small edits do not automatically require TDD; existing user tests are preserved.
- **Grounded estimates:** separate implementation, checks, review, and external waits. Calibrate using comparable measured work rather than a universal multiplier.
- **Design from requirements:** define behavior and acceptance first; derive visual decisions from the actual interface and context.
- **Optional resources:** additional skills, models, and agents need a concrete benefit and the host's actual capabilities and authorization.

This is a collection of instructions and local utilities. Workflow JSON files describe conditions and order; they are not a native workflow engine.

## Quick start

1. Pick a workflow below or browse the [26 skills](docs/skill-map.md) (Chinese reference).
2. Ask your agent to read the relevant `skills/<name>/SKILL.md` and its referenced resources. Load only the capabilities needed for the current task.
3. To prepare a self-contained composition in a new directory outside this repository:

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

Add `--include-optional` to include the agent coordination skill. Exporting does not install skills or change agent settings. Existing targets, redirected paths, stale generated files, in-repository targets, and native installation locations are rejected.

For native discovery, copy complete individual skill directories only when you intend to install them, following your host's current documentation. See [agent compatibility](docs/agent-compatibility.md).

## Eight workflows

| Workflow | Use it for | Key gate |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | Frontend work in an existing project | Full codebase review → internal standards → frontend design and implementation |
| [existing-backend](bundles/existing-backend.json) | Backend work in an existing project | Full codebase review → internal standards → backend implementation |
| [new-frontend](bundles/new-frontend.json) | A genuinely new frontend project | Language/platform → researched options → user choice → reference conventions → standards |
| [new-backend](bundles/new-backend.json) | A genuinely new backend project | Language/deployment needs → user-selected stack → reference conventions → standards |
| [fullstack](bundles/fullstack.json) | Work spanning both ends | Select the existing/new branch; separate end-specific rules and share API contracts |
| [small-change](bundles/small-change.json) | A bounded, low-impact change | Reduce ceremony while preserving the applicable existing/new project gates |
| [debug-and-fix](bundles/debug-and-fix.json) | A reproducible defect or integration symptom | Select validation before executed reproduction; meet codebase gates before a fix |
| [release](bundles/release.json) | Requested integration, packaging, or release | Prepare evidence, compatibility and recovery; hand code fixes back to development |

The `skills` field is the exportable capability closure, not an instruction to run every skill. Conditional stages select the work to perform. If TDD is selected, its loop owns implementation; the standalone implementation stage is skipped. Detailed [composition rules](docs/bundles.md) are currently in Chinese.

## Capability map

| Area | Skills |
| --- | --- |
| Task and resource decisions | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| Codebase and architecture | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference` |
| Requirements and implementation | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| Contracts and safety boundaries | `aw-api-contracts`, `aw-security-boundaries` |
| Validation and diagnosis | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| Delivery and maintenance | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

Each skill includes its own instructions, necessary references/resources, and license. The catalog and source guides are the maintenance source of truth; generated skill copies must stay synchronized.

## Agent compatibility

| Host | Packaging | Evidence |
| --- | --- | --- |
| Codex | Agent Skills directory plus optional `agents/openai.yaml` UI metadata | 1.2.0: Native isolated Windows discovery: 24/24; no model execution |
| Claude Code | Complete skill directories in documented host locations | 1.2.0: Native CLI + official SDK discovery: 24/24; no successful model execution |
| Gemini CLI | Complete skill directories in documented host locations | Documentation mapping only; end-to-end use not tested |
| GitHub Copilot | Complete skill directories in supported clients | Documentation mapping only; individual clients not tested |
| Other agents | Read `SKILL.md` and relative references when supported | No blanket claim of native compatibility |

Portable [role briefs](docs/role-briefs.md) (Chinese) describe optional multi-agent responsibilities. They are not automatically registered agent configurations. Host permissions, tools, trust settings, and model capabilities still apply.

## Validation

```sh
python scripts/build_catalog.py
python scripts/validate.py
```

The validator checks declarations, generated content freshness, exact resource sets, local links, Python syntax, composition order, and selected distribution hygiene rules. It does not prove that an agent will make the right decision or that a framework is vulnerability-free.

Windows/Linux CI checks source, executed offline examples and release packaging. Native isolated discovery passed for all 24 skills in Codex and Claude on Windows. Agents also completed new/existing-project flows and follow-up requirements in two runnable synthetic Web projects, with 42 final browser checks; this does not establish automatic discovery/triggering of the current 26 skills or production coverage. See [executed flows](docs/executed-workflows.md), [validation](docs/validation.md) and [native evidence](docs/agent-loading.md) for exact scope and versions.

## Examples and automated releases

See [worked examples](examples/README.md) for an executed repository case and prompts for small changes, existing backends, and new frontend/backend projects. Run `python scripts/run_examples.py` to reproduce the offline utility checks in TEMP.

Pushing a matching version tag publishes a validated ZIP and SHA-256 checksum; see [release steps](docs/github-publishing.md). [Native discovery replay](docs/agent-loading.md) uses isolated directories without changing default skills. Optional native probes require real clients; Claude also requires Node and the official Agent SDK. Python utilities otherwise use only the standard library.

## Languages

The project overview is available in English, Simplified Chinese, Traditional Chinese, Japanese, Korean, and Russian. GitHub contribution documents and templates use English; contributions in English or Chinese are welcome. Skill bodies, detailed workflow guides, and utility messages remain in Simplified Chinese in this release. These translations cover the README, not the entire skill collection. Ask the agent to respond in your preferred language.

## Contributing and releases

Start with a concrete task that demonstrates a gap. Prefer improving the responsible skill over adding another overlapping rule. See [contributing](CONTRIBUTING.md), [security](SECURITY.md), and the [GitHub publishing guide](docs/github-publishing.md).

The export and validation utilities do not publish repositories or operate remote accounts. No private reporting address or adoption claim is preconfigured.

## License and provenance

Original material is licensed under [MIT](LICENSE). Public upstream references were studied and rewritten; their skill bodies, implementations, assets, and databases are not redistributed. See [third-party notices](THIRD_PARTY_NOTICES.md), [fixed sources](provenance/upstreams.json), and the [provenance notes](docs/provenance.md) (Chinese). The repository's license does not relicense linked third-party material.
