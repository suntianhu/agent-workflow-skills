# Skills CLI and skills.sh

[English](#english) · [简体中文](#简体中文)

## English

The official Skills CLI can discover this repository's standard skill directories. The checked CLI version is 1.7.4, requiring Node.js 22.20 or later. Python-only export and validation remain available without Node.js.

List the available skills without installing them:

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --list
```

Install one selected skill into your current project for Codex:

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --skill aw-evidence-verification --agent codex --copy
```

Review the destination before confirming. Without the global flag, installation is project-scoped. Choose only the skills needed for your task; directory discovery and copied resources do not establish agent behavior. See [host compatibility](agent-compatibility.md).

### Privacy options

The CLI's enabled installation event includes public source and skill identifiers, agent labels, CLI version, and repository-relative SKILL.md paths. Optional caller metadata is unnecessary. The CLI also requests security-audit information for confirmed-public GitHub repositories. These CLI payload fields are separate from ordinary HTTP connection metadata; consult the platform's [privacy policy](https://skills.sh/privacy) for server-side handling.

Disable both CLI telemetry and security-audit requests when you prefer:

```sh
DISABLE_TELEMETRY=1 npx skills@1.7.4 add suntianhu/agent-workflow-skills --skill aw-evidence-verification --agent codex --copy
```

In PowerShell, use a process-local environment setting:

```powershell
$env:DISABLE_TELEMETRY = '1'
npx skills@1.7.4 add suntianhu/agent-workflow-skills --skill aw-evidence-verification --agent codex --copy
```

Disabling telemetry still allows installation; that installation does not contribute to directory discovery statistics. Do not pass credentials, personal details, local paths, private project content, or session transcripts through the optional metadata flag.

### Discovery and grouping

skills.sh documents automatic discovery through real CLI installation events with telemetry enabled. There is no separate listing application described in its FAQ. A successful CLI install or event submission does not guarantee immediate visibility, ranking, or an endorsement.

The root [skills.sh.json](../skills.sh.json) groups all 29 skills into seven sections. It contains only group descriptions and skill names. The platform reads it from the default branch after an enabled installation event and may cache the result. This display configuration does not change skill instructions or installation behavior.

Sources checked on 2026-10-21: [listing FAQ](https://skills.sh/docs/faq), [CLI source and commands](https://github.com/vercel-labs/skills), [telemetry controls](https://github.com/vercel-labs/skills/blob/a80e4c9d12d607631249d4d7d059f835d4b2f13a/docs/troubleshooting.md), and [repository page configuration](https://skills.sh/docs/customize).

## 简体中文

官方 Skills CLI 可以发现本仓库的标准技能目录。已核对 CLI 1.7.4，需要 Node.js 22.20 或以上；原有 Python 导出与校验方式继续可用。

上面的第一条命令只列出技能，第二条将单个技能复制到当前项目的 Codex 技能位置。确认前检查目标路径；不加全局选项即采用项目范围。按当前任务选择能力，CLI 能发现或复制文件不等于模型执行效果已通过验证。

开启遥测时，安装事件包含公开仓库标识、技能名、代理标签、CLI 版本和仓库相对入口路径，并可请求公开仓库的安全审计信息。不需要附加个人资料或自定义 metadata。示例提供关闭遥测的 sh 与 PowerShell 写法；关闭后仍能安装，但该次安装不会贡献目录发现统计。HTTP 连接信息的服务端处理另见平台隐私政策。

skills.sh 依据真实安装事件自动发现技能，公开 FAQ 没有单独申请收录的表单。提交安装事件不等于立即显示或获得排名。根目录 skills.sh.json 将 29 项能力分为七组，只包含分组说明和技能名称；平台在默认分支读取配置，刷新可能有缓存延迟。
