# Agent compatibility

Documentation mapping checked on 2026-10-18. Shared entrypoints use Agent Skills `name`, `description`, `license`, and relative resources. `agents/openai.yaml` is an optional Codex UI extension, not a cross-host requirement. Skill bodies and detailed guides are currently in Simplified Chinese; the repository overview is available in six languages.

| Host | Documented integration | Actual evidence |
| --- | --- | --- |
| Codex | Complete skills in supported project/user locations, or explicitly read a `SKILL.md`; UI prompts use `$skill-name` | Files and scripts used in the current Codex environment; native installation/discovery not tested |
| Claude Code | Complete skills in `.claude/skills/<name>/`; invoke according to host discovery and permission settings | Official documentation mapping; client not launched |
| Gemini CLI | Complete skills in `.gemini/skills/<name>/` or the documented `.agents` alias | Official documentation mapping; installation, activation, and execution not tested |
| GitHub Copilot | Complete skills in client-supported locations such as `.github/skills/<name>/` | Official documentation mapping; individual IDE/CLI clients not tested |
| Other agents | Read `SKILL.md` and relative references if the host supports doing so | Generic reading path; no unverified native-support claim |

These locations are guidance, not executed installation steps. Copying the collection's top-level `skills` directory does not prove host discovery. Current host version, trust, sandbox, network, tools, and model capabilities remain authoritative. Recheck the host documentation when integrating.

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
