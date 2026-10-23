# Agent Workflow Skills: helping coding agents carry existing projects forward

[English](promotion.en.md) · [简体中文](promotion.zh-CN.md) · [GitHub](https://github.com/suntianhu/agent-workflow-skills)

**v1.3.1 · 29 skills · Nine conditional workflows · MIT**

**Build on existing conventions, keep changes scoped, and back completion claims with evidence.**

Now listed on [skills.sh](https://skills.sh/suntianhu/agent-workflow-skills), where you can browse all 29 skills by category. See the [Skills CLI guide](skills-sh.md) for installation and privacy details.

When a coding agent works on an existing product, I want it to carry the project's decisions forward: where conventions live, which behavior must stay intact, and what evidence is needed to call a change complete.

Consider adding an inventory page to an existing admin app. The page needs its own flow, but it also needs to fit the established fonts, theme, components, and API contracts. A later session should be able to build on the same project knowledge.

**Agent Workflow Skills** organizes those expectations into **29 skills and nine conditional workflows**. They cover frontend and backend development in new and existing projects, full-stack work, small changes, debugging, migration, and release preparation.

Five design choices shape the collection:

1. **Carry project conventions forward.** Before formal implementation in an existing product, establish complete codebase understanding and internal standards. Reuse a verifiable baseline, review subsequent changes and knowledge gaps, and keep later skills connected to the same standards entry point. New pages inherit the product's established design conventions.

2. **Trace changes to requested outcomes.** Keep separate acceptance criteria for multiple small requests. Follow actual dependencies when a shared component or service needs to change. Bug fixes address the responsible module, account for invalidated logic, and check affected normal behavior as well as the reported failure.

3. **Select workflow stages for the task.** Compositions describe conditions and handoffs. Choose validation scope, TDD order, and test retention separately. Reuse valid decisions and checks within their coverage. Additional models and agents require a concrete benefit and appropriate authorization.

4. **Account for the old system during migration.** Map existing evidence, consumers, expected behavior, target ownership, and acceptance. Include API consumers, historical data, scheduled jobs, callbacks, and recovery. Scheduled work needs an explicit handoff of execution responsibility and in-flight work.

5. **Make completion claims inspectable.** Report what was implemented, what was actually checked, and which gaps remain. Local utilities support composition export, source tracking, structural validation, and reproducible release archives.

A documented example extends a fictional maintenance app with an inventory page and a later filtering request. The work keeps its original handbook and theme while checking the existing work-order flow. Together with a separate new-project demo, the historical record contains 42 grouped browser behavior and invariant checks. See the [executed workflows](https://github.com/suntianhu/agent-workflow-skills/blob/main/docs/executed-workflows.md) for scope and limitations.

Original material is MIT-licensed. Thanks to the authors and maintainers of the referenced open-source projects; see [references and acknowledgments](provenance.md) for sources and adoption decisions. The README is available in six languages; skill bodies and detailed guides are currently in Simplified Chinese.

Try one redacted task and report whether the agent carried the existing conventions forward, kept changes within scope, and provided evidence you could inspect.

[Source, quick start, and examples](https://github.com/suntianhu/agent-workflow-skills)

## Start with one actual task

| Your task | A starting point |
| --- | --- |
| A small, clearly scoped change | [small-change](../bundles/small-change.json) |
| A new business page in an existing frontend | [existing-frontend](../bundles/existing-frontend.json) |
| Planning a framework or database migration | [Migration guide](project-migration.md), currently in Chinese |

Choose a composition for the task, or ask your agent to read the required skill directory's SKILL.md and the references it needs. The first formal implementation in an existing product requires a valid codebase understanding and internal standards; later work can reuse that baseline while reviewing changes. See the [quick start](../README.md#quick-start) and [worked examples](../examples/README.md).

## Version and evidence scope

- Workflow JSON files describe stage conditions and order. Execution depends on the coding agent and its host.
- The v1.2.7 Windows Codex discovery check found all 29 skills enabled; v1.2.8 retains those skill files. Discovery does not establish model behavior. See [compatibility](agent-compatibility.md) for the tested and documented scope of other hosts.
- The 42 grouped checks cover two historical, small fictional Web demos. They do not establish current skill effectiveness, production migration outcomes, or general productivity gains. See the [validation record](validation.md).

Feedback from one redacted task is welcome: selected capabilities, preserved conventions, repeated steps, and the evidence actually obtained.
