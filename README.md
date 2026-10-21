# Agent Workflow Skills

Composable development workflows for coding agents, with explicit project gates and evidence before completion.

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 29](https://img.shields.io/badge/skills-29-2563eb)
![Workflows: 9](https://img.shields.io/badge/workflows-9-0f766e)

**Version 1.2.8** · Agent Skills directories · Python 3.10+ utilities · No runtime dependencies beyond the Python standard library

**Select skills for the task. Build on the project's existing rules.** 29 skills and nine conditional compositions cover existing and new projects, [project migration](docs/project-migration.md), and [performance and observability](docs/adoption-integration.md). Reuse valid decisions, delegate when useful, and report evidence for the delivered result.

[Sources and adoption](#sources) · [Usage examples](examples/README.md) · [Release history](CHANGELOG.md)

## Why this collection

- **Leaner entries:** remove repeated instructions, choose one main capability, and read additional reference sections only when needed. Reuse valid decisions and unchanged material already read.
- **Task-scoped activation:** nine compositions describe conditions rather than a mandatory sequence. A clear local edit does not automatically start broad research, model comparison or multiple agents; estimates have their own trigger.
- **Bounded changes:** map each edit to a requested item or a necessary dependency, preserve unrelated behavior, and record newly found issues without silently fixing them.
- **Continuity in existing projects:** verify the complete code baseline and subsequent changes, then use the same standards directory and rule sources. New pages inherit fonts, themes, components and interaction patterns even when their business purpose is new.
- **Proportional validation:** decide scope, TDD order, and artifact retention separately. Small edits do not automatically require TDD; existing user tests are preserved.
- **Optional resources:** additional skills, models, and agents need a concrete benefit and the host's actual capabilities and authorization.

This is a collection of instructions and local utilities. Workflow JSON files describe conditions and order; they are not a native workflow engine.

## Quick start

1. Pick a workflow below or browse the [29 skills](docs/skill-map.md) (Chinese reference).
2. Ask your agent to read the relevant `skills/<name>/SKILL.md` and its referenced resources. Load only the capabilities needed for the current task.
3. To prepare a self-contained composition in a new directory outside this repository:

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

Add `--include-optional` to include the agent coordination skill. Exporting does not install skills or change agent settings. Existing targets, redirected paths, stale generated files, in-repository targets, and native installation locations are rejected.

For native discovery, copy complete individual skill directories only when you intend to install them, following your host's current documentation. See [agent compatibility](docs/agent-compatibility.md).

## Nine workflows

| Workflow | Use it for | Key gate |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | Frontend work in an existing project | Full codebase review → internal standards → frontend design and implementation |
| [existing-backend](bundles/existing-backend.json) | Backend work in an existing project | Full codebase review → internal standards → backend implementation |
| [new-frontend](bundles/new-frontend.json) | A genuinely new frontend project | Language/platform → researched options → user choice → reference conventions → standards |
| [new-backend](bundles/new-backend.json) | A genuinely new backend project | Language/deployment needs → user-selected stack → reference conventions → standards |
| [fullstack](bundles/fullstack.json) | Work spanning both ends | Select the existing/new branch; separate end-specific rules and share API contracts |
| [project-migration](bundles/project-migration.json) | Framework, backend/frontend or database migration | Preservation inventory → target/coexistence → business batches → verified cutover/recovery |
| [small-change](bundles/small-change.json) | A bounded, low-impact change | Reduce ceremony while preserving the applicable existing/new project gates |
| [debug-and-fix](bundles/debug-and-fix.json) | A reproducible defect or integration symptom | Select validation before executed reproduction; meet codebase gates before a fix |
| [release](bundles/release.json) | Requested integration, packaging, or release | Prepare evidence, compatibility and recovery; hand code fixes back to development |

The `skills` field is the exportable capability closure, not an instruction to run every skill. Conditional stages select the work to perform. If TDD is selected, its loop owns implementation; the standalone implementation stage is skipped. Detailed [composition rules](docs/bundles.md) are currently in Chinese.

## Capability map

| Area | Skills |
| --- | --- |
| Task and resource decisions | `aw-project-triage`, `aw-skill-selection`, `aw-model-routing`, `aw-effort-estimation` |
| Codebase and architecture | `aw-repository-audit`, `aw-project-standards`, `aw-framework-selection`, `aw-github-reference`, `aw-project-migration` |
| Requirements and implementation | `aw-requirements-design`, `aw-design-reference`, `aw-design-standards`, `aw-ui-design`, `aw-frontend-implementation`, `aw-backend-implementation` |
| Performance and observability | `aw-performance-optimization`, `aw-observability` |
| Contracts and safety boundaries | `aw-api-contracts`, `aw-security-boundaries` |
| Validation and diagnosis | `aw-test-strategy`, `aw-scoped-tdd`, `aw-evidence-debugging`, `aw-adversarial-review`, `aw-evidence-verification` |
| Delivery and maintenance | `aw-delivery-cleanup`, `aw-release-readiness`, `aw-agent-coordination`, `aw-skill-authoring`, `aw-open-source-readiness` |

Each skill includes its own instructions, necessary references/resources, and license. The catalog and source guides are the maintenance source of truth; generated skill copies must stay synchronized.

## Agent compatibility

| Host | Packaging | Evidence |
| --- | --- | --- |
| Codex | Agent Skills directory plus optional `agents/openai.yaml` UI metadata | 1.2.7 Windows Codex discovery: 29/29 installed skills enabled, no parser errors; no model turn |
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

Windows/Linux CI checks source, offline utilities and reproducible packaging. In 1.2.7, local Windows Codex discovery loaded all 29 installed skills with no parser errors; all 154 installed skill files matched source. Earlier isolated Codex/Claude discovery and 42 browser checks keep their historical scope. This does not establish automatic trigger accuracy, model adherence or production coverage. See [validation](docs/validation.md) and [native evidence](docs/agent-loading.md).

## Examples and automated releases

See [worked examples](examples/README.md) for an executed repository case and prompts for small changes, existing backends, and new frontend/backend projects. Run `python scripts/run_examples.py` to reproduce the offline utility checks in TEMP.

Pushing a matching version tag publishes a validated ZIP and SHA-256 checksum; see [release steps](docs/github-publishing.md). [Native discovery replay](docs/agent-loading.md) uses isolated directories without changing default skills. Optional native probes require real clients; Claude also requires Node and the official Agent SDK. Python utilities otherwise use only the standard library.

## Languages

The project overview is available in English, Simplified Chinese, Traditional Chinese, Japanese, Korean, and Russian. GitHub contribution documents and templates use English; contributions in English or Chinese are welcome. Skill bodies, detailed workflow guides, and utility messages remain in Simplified Chinese in this release. These translations cover the README, not the entire skill collection. Ask the agent to respond in your preferred language.

## Contributing and releases

Start with a concrete task that demonstrates a gap. Prefer improving the responsible skill over adding another overlapping rule. See [contributing](CONTRIBUTING.md), [security](SECURITY.md), and the [GitHub publishing guide](docs/github-publishing.md).

The export and validation utilities do not publish repositories or operate remote accounts. No private reporting address or adoption claim is preconfigured.

<a id="sources"></a>

## GitHub research and acknowledgments

This collection distills selected ideas from the 14 GitHub projects below into independently written guidance. The research covers 73 retrieved files at pinned commits, not complete repository audits. The table summarizes what was adopted; [provenance notes](docs/provenance.md), [fixed sources](provenance/upstreams.json), and [third-party notices](THIRD_PARTY_NOTICES.md) record scope, rejected assumptions and license details.

| Project | Ideas adopted |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | Short skill entries and progressive disclosure of resources |
| [openai/skills](https://github.com/openai/skills) | Historical skill packaging, source-of-truth separation and script verification |
| [obra/superpowers](https://github.com/obra/superpowers) | Evidence-led debugging, explicit hypotheses and bounded review |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Framework-scoped activation and impact-based performance priorities |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Separate skills, instructions and agent roles; keep responsibilities focused |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Trace real call chains and test security claims with counterexamples |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | PostgreSQL query plans, indexes, connection budgets and transaction/locking boundaries |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Inspect live locators, isolate browser sessions and distinguish actions from assertion evidence |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Derive typography, components and platform choices from interface requirements |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Inherit existing design conventions; distinguish local changes from shared standards |
| [wshobson/agents](https://github.com/wshobson/agents) | Design tokens, reusable components and platform-specific interaction/motion |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Requirements readiness, task handoffs, quality gates, migration, performance and observability |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills) | Migration compatibility, data reconciliation and realistic recovery limits |
| [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) | Map integrations, migrate by business batch and assign clear responsibilities |

## License

Original material is licensed under [MIT](LICENSE). Upstream skill bodies, code, templates, assets and databases are not redistributed. Upstream licenses remain separate; the Trail of Bits source is CC-BY-SA-4.0 and its text was not adapted into MIT material. See the notices for per-source limits.
