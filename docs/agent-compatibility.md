# Agent compatibility

Version 1.2.5 contains 29 skills and nine conditional compositions. Authorized Windows Codex synchronization verified 154 installed files against source; fresh native discovery found all 29 enabled with no parser errors. This does not establish automatic trigger accuracy, model execution, other hosts or isolated discovery of the current collection. Historical 1.2.0 Codex/Claude probes retain their 24-skill scope. See [validation](validation.md), [native evidence](agent-loading.md) and [version history](versioning.md).

Documentation mapping and isolated native probes checked on 2026-10-19. Shared entrypoints use Agent Skills `name`, `description`, `license`, and relative resources. `agents/openai.yaml` is an optional Codex UI extension, not a cross-host requirement. Skill bodies and detailed guides are currently in Simplified Chinese; the repository overview is available in six languages.

| Host | Documented integration | Actual evidence |
| --- | --- | --- |
| Codex | Complete skills in supported project/user locations, or explicitly read a `SKILL.md`; UI prompts use `$skill-name` | 1.2.5: native CLI `0.163.0-alpha.10.2` discovered all 29 enabled local-user skills with no parser errors; no model turn. Historical isolated probe: 24 |
| Claude Code | Complete skills in `.claude/skills/<name>/`; invoke according to host discovery and permission settings | Native CLI `2.1.303` and official SDK `0.3.303` discovered all 24 in isolation; no successful model turn |
| Gemini CLI | Complete skills in `.gemini/skills/<name>/` or the documented `.agents` alias | Official documentation mapping; installation, activation, and execution not tested |
| GitHub Copilot | Complete skills in client-supported locations such as `.github/skills/<name>/` | Official documentation mapping; individual IDE/CLI clients not tested |
| Other agents | Read `SKILL.md` and relative references if the host supports doing so | Generic reading path; no unverified native-support claim |

The historical isolated probes did not modify default user locations; the 1.2.5 check separately performed the explicitly authorized user installation. The probes copied complete skills only to disposable projects and compared default-tree snapshots before/after. See [native loading evidence and replay](agent-loading.md). Copying a directory by itself does not prove discovery or execution. Current host version, trust, sandbox, network, tools, and model capabilities remain authoritative. Recheck host documentation when integrating.

If reading, shell, or network capabilities are unavailable, disclose the resulting gaps. If delegation is unavailable, the primary agent may work sequentially; existing-project review and new-project selection gates still apply. A model recommendation is not evidence that the current model has been switched.

## Multi-agent coordination

[Role briefs](role-briefs.md) are portable descriptions in Chinese, not auto-registered host agent files. Delegate only with authorization and a concrete benefit, using actual host APIs. A read-only reviewer does not modify implementation, run unauthorized tests, or operate external data.

## Primary references

- [Agent Skills specification](https://agentskills.io/specification)
- [Integrating skills support](https://agentskills.io/client-implementation/adding-skills-support)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Gemini CLI skills](https://geminicli.com/docs/cli/creating-skills/)
- [Copilot agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
