# Worked examples

These examples show the decisions and evidence behind a workflow. A composition lists available capabilities; exporting 19 skills does not mean loading or executing all 19 for a small task.

## Executed case: release automation in this repository

The request was to add tag-triggered packaging, usable examples, and isolated Codex/Claude loading checks. This is an existing tooling repository. It needs engineering checks and bounded negative cases, but no UI redesign, framework selection, extra model, or persistent TDD suite.

The implementation separates read-only validation/build jobs from the GitHub job with release write permission. Only a stable tag matching `catalog.json` and pointing into `main` can publish. The archive uses committed regular files, fixed member metadata, and a SHA-256 sidecar. Existing releases are not overwritten on a rerun.

Reproduce the offline examples from the source root:

```sh
python scripts/validate.py
python scripts/run_examples.py
```

The second command creates a new system-TEMP directory and leaves `result.json` there. Supply `--out <NEW_TEMP_DIRECTORY>` to select an inspectable location. It executes real repository utilities against a disposable fixture:

| Observed check | Result |
| --- | --- |
| Inventory one source file, then check an empty reading ledger | Gate blocked with missing reading evidence; scanning alone never authorizes development |
| Estimate 10 implementation minutes with explicit prior 0.5, plus 1 check minute and 1 review minute | Likely 7 minutes; heuristic range 6–8.5; zero historical samples; external CI queue remains unknown |
| Export `small-change`, then compare every exported skill resource with source | 1.2.1: 21 available skills, 106 byte-identical files, no installation |

The 0.5 factor is an explicit demonstration input, not a global accuracy guarantee or a real calibration sample. The fixture is synthetic. These are executed utility examples, not transcripts of a model completing a product task. Native host results and exact versions are in [loading validation](../docs/agent-loading.md).

The 1.3.0 export includes conditional specialist references. See [source integration](../docs/provenance.md) for their reading conditions and [launch materials](../docs/promotion.en.md) for accurate public descriptions.

The 1.3.1 export also includes a project-level standards skill template. Follow [project directory and TDD rules](../docs/project-standards-and-tdd.md) when filling it; do not install the unfilled template or treat native test tools as interchangeable with substitute implementations.

The unpublished 1.4.0 source checkpoint added conditional design reference research, project design standards and a design template; these remain in current 1.2.3. See [the design workflow](../docs/design-workflow.md). Exported availability does not require running every stage or recreating an existing design system.

The unpublished 1.4.1 source checkpoint distinguished standalone page/prototype delivery from product integration. Pages belonging to an existing product still inherit its design and global typography/theme even when the business flow is new or the prototype is outside the repository.

## Scenario: a small documentation correction

Codex prompt (Claude uses `/aw-test-strategy` instead of `$aw-test-strategy`):

```text
Use $aw-test-strategy to classify this task, then correct the misspelled heading
in the existing README. Preserve its meaning and links. This is a documentation
change only. Do not add tests or start the application. Report the exact diff.
```

Expected decision: use the current agent, inspect applicable instructions and the affected document, make the correction, then review the diff and links. Skip repository implementation gates that do not apply to pure documentation, UI design, extra agents, and TDD. Do not invent a task duration or ask again for permission to omit tests. This is a prompt recipe, not a claimed native model execution.

## Scenario: change an existing backend

```text
Use aw-project-triage, aw-repository-audit and aw-project-standards first.
In this existing backend, add an optional status filter to the list endpoint.
Read all owned code, configuration and scripts; document exclusions and blocked
files. Produce PROJECT_STANDARDS.md inside this project before implementation.
Preserve its response contract and authorization rules. Choose a bounded test
strategy before changing code; follow the project's test-retention policy.
```

Expected sequence: classify backend scope → complete genuine repository reading → produce a current internal standard → define filter semantics, invalid input and authorization behavior → choose validation → implement under that standard → review and verify affected paths. A complete ledger is self-reported reading evidence, not proof of understanding. Blocked files or stale reading evidence keep the implementation gate closed. Frontend work is needed only if a caller actually changes. This scenario has not been executed against an external backend.

## Scenario: start a new frontend and backend

```text
Use aw-project-triage and aw-framework-selection. I want a new TypeScript web
frontend and a new Python API. First clarify user flows, deployment constraints
and data boundaries. Research currently maintained mainstream frameworks using
official release and security sources. Explain tradeoffs and wait for my stack
choice before initializing either project. Then use aw-github-reference to derive
conventions from mature, pinned public repositories and write project standards.
```

Expected sequence: separate frontend/backend requirements → present current, sourced options → obtain the user's choice → review reference conventions and licenses → write project standards → design relevant interaction/API states → choose validation → implement each affected side. No fixed framework is recommended here because maintenance and security status change. A skill or reference project does not authorize account creation, paid services, deployment, or copying proprietary code. This is a recipe; no external application has been initialized.

The unpublished 1.4.2 source checkpoint separated missing reading coverage from missing project rules and new-project prerequisites, reusing completed outputs. Cleanup precedes final evidence verification; see the [workflow audit](../docs/workflow-audit.md).

Current v1.2.3 retains precise conditional loading and independent resource decisions, while refining configuration contracts, project structure, validation evidence and scoped cleanup. Earlier 1.3/1.4 labels above are [unpublished development checkpoints](../docs/versioning.md), not additional public tags.
