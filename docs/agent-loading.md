# Isolated native loading validation

Checked on 2026-10-19 on Windows. All native processes used disposable projects under system TEMP with separate home/config/cache directories. No default skills were installed, replaced, or removed.

| Host | Version | Native evidence | Scope |
| --- | --- | --- | --- |
| Codex CLI | `0.163.0-alpha.10.2` | Real `app-server` initialization followed by `skills/list`: all 24 names enabled, no parser errors, skill paths confined to the isolated project | Discovery and metadata loading; no model turn |
| Claude Code | `2.1.303` | Native `--init-only` reported 24 project skills and zero user skills; official Agent SDK `0.3.303` returned all 24 names from `supportedCommands()` | Discovery and command registration; no successful model turn |

The same checks were rerun through the shipped [probe](../scripts/verify_agent_loading.py). Sanitized machine-readable evidence is in [native discovery](../provenance/native-discovery.json). Snapshot hashes of the three default skill trees were identical before and after. The report includes only relative tree labels and hashes; private logs, executable locations, and user paths stay outside the distribution.

## Reproduce without touching defaults

Python 3.10+, Git, and an existing native Codex executable are required for Codex. The optional Claude adapter additionally requires Node, a native Claude executable, and the official `@anthropic-ai/claude-agent-sdk` package. None are automatically installed by these scripts. The recorded Claude packages came from pinned official npm releases `@anthropic-ai/claude-code@2.1.303` and `@anthropic-ai/claude-agent-sdk@0.3.303`, installed only into TEMP for this check.

```sh
python scripts/verify_agent_loading.py --host codex
python scripts/verify_agent_loading.py --host claude --claude-exe <NATIVE_CLAUDE_EXECUTABLE> --claude-sdk <SDK_DIRECTORY>/sdk.mjs
```

Use `--host both` with the Claude options to check both hosts. Use `--codex-exe <EXECUTABLE>` if Codex is not on PATH. Optionally supply `--out <NEW_TEMP_DIRECTORY>`; an existing directory, source-tree target, agent configuration directory, or non-TEMP target is rejected. Do not point at an active project. The probe copies validated skill directories into its disposable project and never writes a default discovery location. It leaves `result.json` and private diagnostics in that directory for inspection and manual cleanup.

Child processes receive an allowlisted OS environment, isolated `HOME`, `USERPROFILE`, `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, application-data and temporary paths. Provider tokens are not inherited. The probe does not copy credentials or request authentication; native client file reads are not sandbox-enforced. Git templates and global/system Git config are disabled for project initialization.

**The disposable project must be a Git root.** A first exploratory Claude run without this boundary discovered 34 skills by walking real-home ancestors on Windows, even with isolated home variables. That contaminated run was discarded. The shipped probe creates the boundary before either host starts and verifies the expected names. This matters when TEMP itself is under the real user home.

The Claude adapter holds an empty async input stream while asking the official SDK for initialization and supported commands. It never yields a user prompt. The Codex adapter uses the documented app-server JSON-RPC discovery request and does not start a turn. Unexpected collection counts, names, parser errors, timeouts, or changed default-tree snapshots fail the probe.

**Codex's Windows discovery is not an OS sandbox.** This native version also enumerates existing OS-user skill metadata despite home overrides, plus bundled skills in the temporary CODEX_HOME. The probe reports these extra counts separately and requires every collection skill to come from the temporary project. The initial probe checked only the collection; an all-entry follow-up exposed this host behavior. No outside skill was invoked, and default trees stayed unchanged. The result establishes temporary-project collection loading, not an absence of metadata reads outside TEMP. Raw native rows stay in a private TEMP diagnostic file. The installed native schema and official configuration expose no global user-root exclusion; per-skill enablement overrides do not prove that metadata was never scanned.

## What remains unverified

Native discovery does not demonstrate that a model selects a skill, reads its full body, follows its gates, or completes an application task. A separate isolated Claude invocation attempt stopped with “Not logged in” and reported zero API duration, cost, and input/output tokens; it is not a successful workflow run. No user credentials were copied to remove that boundary. The reusable probe makes no model invocation.

Gemini CLI, Copilot, macOS/Linux native loading, and other host versions remain untested. The ordinary Windows/Linux CI runs source validation, offline examples, and packaging; it does not install paid agent clients or claim native host coverage.

## Primary sources

- [Codex app-server skill discovery and explicit invocation](https://learn.chatgpt.com/docs/app-server)
- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Codex skill locations](https://learn.chatgpt.com/docs/build-skills)
- [Claude skill locations](https://code.claude.com/docs/en/skills)
- [Claude CLI initialization flags](https://code.claude.com/docs/en/cli-reference)
- [Claude SDK command discovery](https://code.claude.com/docs/en/agent-sdk/slash-commands)
