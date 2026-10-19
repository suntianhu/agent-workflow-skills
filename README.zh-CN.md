# Agent Workflow Skills

面向编程智能体的可组合开发工作流，明确项目门禁，以真实证据支持完成结论。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 24](https://img.shields.io/badge/skills-24-2563eb)
![Workflows: 8](https://img.shields.io/badge/workflows-8-0f766e)

**版本 1.3.1** · Agent Skills 目录格式 · Python 3.10+ 工具 · 运行工具仅依赖 Python 标准库

1.3.1 将安全证据、PostgreSQL、浏览器验收和设计体系细则整合为按条件读取的参考资料，仍保留 24 个技能、8 套组合。见[来源与去重落点](docs/provenance.md)、[中文宣传文案](docs/promotion.zh-CN.md)和[英文宣传文案](docs/promotion.en.md)。下方原生发现证据来自 1.2.0，1.3.1 未重跑宿主发现。

区分已有项目和新项目，按任务选择适用技能，分别维护前后端规范，在实现前选定验证策略，并如实报告实际验证范围。

## 为什么使用这套技能

- **承接已有技能：** 梳理项目已配 Skills 和代理/插件规则，后续启用技能先对齐同一份项目规范与既有决定。
- **老项目：** 修改代码、配置或工程脚本前，阅读全部自有代码，并在项目内部形成有证据的工程规范。
- **新项目：** 尊重指定语言，核查框架维护状态和已知相关风险，由用户选栈，再从匹配的公开项目提炼规范。
- **按风险验证：** 范围、TDD 顺序和产物保留分别决定。小改不自动 TDD，不擅删用户已有测试。
- **基于实耗估时：** 分开实现、检查、审查和外部等待，用同类真实记录校准，不统一乘除固定倍数。
- **根据需求设计：** 先明确行为和验收，再根据界面与场景推导视觉方案。
- **按需使用资源：** 额外技能、模型和代理需要具体收益，以及宿主真实能力与相应授权。

本项目提供指令与本地工具。组合 JSON 描述条件和顺序，不是宿主原生工作流引擎。

## 快速开始

1. 在下表选择组合，或查看 [24 个技能的职责边界](docs/skill-map.md)。
2. 让智能体读取所需的 `skills/<name>/SKILL.md` 及其引用资料，只加载本次适用能力。
3. 如需在仓库之外的新目录准备完整组合：

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

添加 `--include-optional` 可携带代理协作技能。导出不安装技能、不改默认设置；拒绝既有目录、重定向路径、过期生成内容、仓库内部目标和原生安装位置。

需要宿主原生发现时，按其当前文档和明确安装意图，复制完整的单个技能目录。详见[代理适配](docs/agent-compatibility.md)（英文）。

## 八套组合

| 组合 | 适用任务 | 核心门禁 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 老项目前端开发 | 全仓阅读 → 内部规范 → 前端设计与实现 |
| [existing-backend](bundles/existing-backend.json) | 老项目后端开发 | 全仓阅读 → 内部规范 → 后端实现 |
| [new-frontend](bundles/new-frontend.json) | 真正从零的前端项目 | 语言/平台 → 框架核查 → 用户选择 → 范本 → 规范 |
| [new-backend](bundles/new-backend.json) | 真正从零的后端项目 | 语言/部署需求 → 用户选栈 → 范本 → 规范 |
| [fullstack](bundles/fullstack.json) | 前后端跨端开发 | 选择新旧分支，端内规范独立，API 契约共同核对 |
| [small-change](bundles/small-change.json) | 低影响的局部改动 | 缩减仪式，仍满足对应新旧项目门禁 |
| [debug-and-fix](bundles/debug-and-fix.json) | 可复现缺陷或联调异常 | 执行复现前选策略，修复前满足全仓和规范门禁 |
| [release](bundles/release.json) | 已请求的集成、打包或发布 | 准备兼容/恢复/验收证据，代码修复回到开发流程 |

`skills` 是可导出的能力闭包，不代表全部执行。阶段按条件触发；已选择 TDD 时由其循环统筹实现，跳过独立实现阶段。详见[组合条件和顺序](docs/bundles.md)。

## 能力分布

| 领域 | 技能 |
| --- | --- |
| 任务与资源判断 | `aw-project-triage`、`aw-skill-selection`、`aw-model-routing`、`aw-effort-estimation` |
| 代码理解与规范 | `aw-repository-audit`、`aw-project-standards`、`aw-framework-selection`、`aw-github-reference` |
| 需求、设计与实现 | `aw-requirements-design`、`aw-ui-design`、`aw-frontend-implementation`、`aw-backend-implementation` |
| 契约与安全边界 | `aw-api-contracts`、`aw-security-boundaries` |
| 验证与排障 | `aw-test-strategy`、`aw-scoped-tdd`、`aw-evidence-debugging`、`aw-adversarial-review`、`aw-evidence-verification` |
| 交付与维护 | `aw-delivery-cleanup`、`aw-release-readiness`、`aw-agent-coordination`、`aw-skill-authoring`、`aw-open-source-readiness` |

每个技能包含自己的说明、必要资料/脚本/模板与许可。catalog 和源指南是维护入口，生成副本须保持同步。

## 智能体兼容性

| 宿主 | 打包方式 | 实际证据 |
| --- | --- | --- |
| Codex | Agent Skills 目录，可选 `agents/openai.yaml` 界面扩展 | 1.2.0: Windows 隔离原生发现 24/24；未执行模型任务 |
| Claude Code | 按官方目录放完整技能 | 1.2.0: 原生 CLI 与官方 SDK 发现 24/24；未成功执行模型任务 |
| Gemini CLI | 按官方目录放完整技能 | 文档适配，未端到端实测 |
| GitHub Copilot | 按支持客户端的目录放完整技能 | 文档适配，各客户端未实测 |
| 其他代理 | 支持时读取 `SKILL.md` 及相对引用 | 不承诺未经核对的原生兼容 |

[协作角色说明](docs/role-briefs.md)是可选的文字职责，不是自动注册配置。实际权限、工具、信任和模型能力以宿主为准。

## 维护与验证

```sh
python scripts/build_catalog.py
python scripts/validate.py
```

校验覆盖源声明、生成内容新鲜度、精确资源集合、相对引用、Python 语法、组合顺序和部分分发卫生规则；不证明智能体决策正确，也不证明框架没有漏洞。

Windows/Linux CI 校验源码、执行离线示例并预演打包。Codex 与 Claude 已在 Windows 隔离项目中原生发现全部 24 个技能；模型驱动的工作流执行仍未验证。具体版本和范围见[验证记录](docs/validation.md)与[原生加载证据](docs/agent-loading.md)。

## 使用示例与自动发布

[完整示例](examples/README.md)包含已执行的本仓库案例，以及小改、老后端和新前后端的提示词。运行 `python scripts/run_examples.py` 可在 TEMP 重现离线工具检查。

推送匹配版本的标签后自动校验并发布 ZIP 与 SHA-256 文件，见[发布步骤](docs/github-publishing.md)。[原生发现复跑](docs/agent-loading.md)使用隔离目录，不改默认技能。可选原生检查需要实际客户端，Claude 还需要 Node 与官方 Agent SDK；其余 Python 工具只依赖标准库。

## 语言

项目主页提供英文、简体中文、繁体中文、日语、韩语和俄语。GitHub 贡献文档和模板采用英文，欢迎英文或中文贡献。本版技能正文、详细指南和工具提示保留简体中文，这些翻译仅覆盖 README，不代表整套技能已完成六语翻译。可要求智能体按你的偏好语言回复。

## 贡献与发布

先用实际任务说明缺口，优先完善负责该能力的技能，避免追加重叠规则。参见[贡献指南](CONTRIBUTING.md)、[安全说明](SECURITY.md)和[GitHub 上传与发布步骤](docs/github-publishing.md)（英文）。

导出和校验工具不会发布仓库或操作远端账号，没有预设私密报告地址或使用规模。

## 许可与来源

原创内容采用 [MIT](LICENSE)。公开上游仅用于研究并重新撰写原则，不分发其技能正文、实现、素材或数据库。参见[第三方说明](THIRD_PARTY_NOTICES.md)、[固定来源](provenance/upstreams.json)和[来源取舍](docs/provenance.md)。本仓库许可不替第三方内容重新授权。
