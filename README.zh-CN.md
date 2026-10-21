# Agent Workflow Skills

面向编程智能体的可组合开发工作流，明确项目门禁，以真实证据支持完成结论。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Skills: 29](https://img.shields.io/badge/skills-29-2563eb)
![Workflows: 9](https://img.shields.io/badge/workflows-9-0f766e)

**版本 1.3.0** · Agent Skills 目录格式 · Python 3.10+ 工具 · 运行工具仅依赖 Python 标准库

**按任务选技能，沿用项目已有规范。** 29 个技能、9 套条件组合覆盖新旧项目开发、[项目迁移](docs/project-migration.md)、[性能优化与可观测性](docs/adoption-integration.md)。承接有效决定，按需拆分协作，以实际证据说明交付结果。

[项目介绍](docs/promotion.zh-CN.md) · [参考来源与鸣谢](#sources) · [使用示例](examples/README.md) · [版本记录](CHANGELOG.md)

## 为什么使用这套技能

- **精简入口：** 去除重复说明，先选一项主要能力，缺口才补读相关资料；已成立的决定和未变化的已读内容直接复用。
- **精准触发：** 九套组合按条件选择阶段。明确的局部改动不自动启动大范围调研、模型比较或多代理；估时也有独立触发条件。
- **改动有边界：** 多个小任务逐项对应需求与验收，只做有依据的必要联动；保留其他功能的既有行为，无关新问题只记录、不顺手修复。
- **沿用老项目规范：** 核对完整代码基线及后续差异，继续维护原规范目录和规则来源。新页面即使业务全新，也继承项目字体、主题、组件和交互习惯。
- **按风险验证：** 范围、TDD 顺序和产物保留分别决定。小改不自动 TDD，不擅删用户已有测试。
- **按需使用资源：** 额外技能、模型和代理需要具体收益，以及宿主真实能力与相应授权。

本项目提供指令与本地工具。组合 JSON 描述条件和顺序，不是宿主原生工作流引擎。

## 快速开始

1. 在下表选择组合，或查看 [29 个技能的职责边界](docs/skill-map.md)。
2. 让智能体读取所需的 `skills/<name>/SKILL.md` 及其引用资料，只加载本次适用能力。
3. 如需在仓库之外的新目录准备完整组合：

```sh
python scripts/export_bundle.py --bundle existing-frontend --out ../workflow-export
```

添加 `--include-optional` 可携带代理协作技能。导出不安装技能、不改默认设置；拒绝既有目录、重定向路径、过期生成内容、仓库内部目标和原生安装位置。

需要宿主原生发现时，按其当前文档和明确安装意图，复制完整的单个技能目录。详见[代理适配](docs/agent-compatibility.md)（英文）。

### 可选的 Skills CLI

使用 Node.js 22.20+ 时，可通过官方 CLI 列出本仓库技能：

```sh
npx skills@1.7.4 add suntianhu/agent-workflow-skills --list
```

项目范围安装、关闭遥测及 skills.sh 分组见[安装与隐私说明](docs/skills-sh.md#简体中文)。CLI 发现与智能体执行证据分别说明。

## 九套组合

| 组合 | 适用任务 | 核心门禁 |
| --- | --- | --- |
| [existing-frontend](bundles/existing-frontend.json) | 老项目前端开发 | 全仓阅读 → 内部规范 → 前端设计与实现 |
| [existing-backend](bundles/existing-backend.json) | 老项目后端开发 | 全仓阅读 → 内部规范 → 后端实现 |
| [new-frontend](bundles/new-frontend.json) | 真正从零的前端项目 | 语言/平台 → 框架核查 → 用户选择 → 范本 → 规范 |
| [new-backend](bundles/new-backend.json) | 真正从零的后端项目 | 语言/部署需求 → 用户选栈 → 范本 → 规范 |
| [fullstack](bundles/fullstack.json) | 前后端跨端开发 | 选择新旧分支，端内规范独立，API 契约共同核对 |
| [project-migration](bundles/project-migration.json) | 项目换框架、前后台或数据库重构 | 保留台账 → 目标/共存 → 业务分批 → 验证后切换与恢复 |
| [small-change](bundles/small-change.json) | 低影响的局部改动 | 缩减仪式，仍满足对应新旧项目门禁 |
| [debug-and-fix](bundles/debug-and-fix.json) | 可复现缺陷或联调异常 | 执行复现前选策略，修复前满足全仓和规范门禁 |
| [release](bundles/release.json) | 已请求的集成、打包或发布 | 准备兼容/恢复/验收证据，代码修复回到开发流程 |

`skills` 是可导出的能力闭包，不代表全部执行。阶段按条件触发；已选择 TDD 时由其循环统筹实现，跳过独立实现阶段。详见[组合条件和顺序](docs/bundles.md)。

## 能力分布

| 领域 | 技能 |
| --- | --- |
| 任务与资源判断 | `aw-project-triage`、`aw-skill-selection`、`aw-model-routing`、`aw-effort-estimation` |
| 代码理解与规范 | `aw-repository-audit`、`aw-project-standards`、`aw-framework-selection`、`aw-github-reference`、`aw-project-migration` |
| 需求、设计与实现 | `aw-requirements-design`、`aw-design-reference`、`aw-design-standards`、`aw-ui-design`、`aw-frontend-implementation`、`aw-backend-implementation` |
| 性能与可观测性 | `aw-performance-optimization`、`aw-observability` |
| 契约与安全边界 | `aw-api-contracts`、`aw-security-boundaries` |
| 验证与排障 | `aw-test-strategy`、`aw-scoped-tdd`、`aw-evidence-debugging`、`aw-adversarial-review`、`aw-evidence-verification` |
| 交付与维护 | `aw-delivery-cleanup`、`aw-release-readiness`、`aw-agent-coordination`、`aw-skill-authoring`、`aw-open-source-readiness` |

每个技能包含自己的说明、必要资料/脚本/模板与许可。catalog 和源指南是维护入口，生成副本须保持同步。

## 智能体兼容性

| 宿主 | 打包方式 | 实际证据 |
| --- | --- | --- |
| Codex | Agent Skills 目录，可选 `agents/openai.yaml` 界面扩展 | 1.2.7 Windows Codex 原生发现：29/29 本机已安装技能启用，无解析错误；未执行模型任务 |
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

Windows/Linux CI 校验源码、离线工具和可复现打包。1.2.7 的 Windows Codex 原生发现识别并启用全部 29 个本机技能，无解析错误；154 个安装文件与源码一致。早期 Codex/Claude 隔离发现及 42 项浏览器检查保留原有范围，不代表本版自动触发准确率、模型遵循率或生产覆盖。见[验证记录](docs/validation.md)及[原生加载证据](docs/agent-loading.md)。

## 使用示例与自动发布

[完整示例](examples/README.md)包含已执行的本仓库案例，以及小改、老后端和新前后端的提示词。运行 `python scripts/run_examples.py` 可在 TEMP 重现离线工具检查。

推送匹配版本的标签后自动校验并发布 ZIP 与 SHA-256 文件，见[发布步骤](docs/github-publishing.md)。[原生发现复跑](docs/agent-loading.md)使用隔离目录，不改默认技能。可选原生检查需要实际客户端，Claude 还需要 Node 与官方 Agent SDK；其余 Python 工具只依赖标准库。

## 语言

项目主页提供英文、简体中文、繁体中文、日语、韩语和俄语。GitHub 贡献文档和模板采用英文，欢迎英文或中文贡献。本版技能正文、详细指南和工具提示保留简体中文，这些翻译仅覆盖 README，不代表整套技能已完成六语翻译。可要求智能体按你的偏好语言回复。

## 贡献与发布

先用实际任务说明缺口，优先完善负责该能力的技能，避免追加重叠规则。参见[贡献指南](CONTRIBUTING.md)、[安全说明](SECURITY.md)和[GitHub 上传与发布步骤](docs/github-publishing.md)（英文）。

导出和校验工具不会发布仓库或操作远端账号，没有预设私密报告地址或使用规模。

<a id="sources"></a>

## 参考来源与鸣谢

感谢以下 14 个开源项目的作者与维护者。本项目参考了其中的部分设计与工程方法，结合自身需求独立编写技能与指南。记录覆盖固定提交下实际取得的 73 份文件，不代表完整审计这些仓库。下表说明主要借鉴点；具体阅读范围、未采纳规则和许可见[来源与采纳说明](docs/provenance.md)、[固定提交与文件指纹](provenance/upstreams.json)、[第三方说明](THIRD_PARTY_NOTICES.md)。

| 项目 | 主要借鉴内容 |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 精简技能入口、按需展开引用资源 |
| [openai/skills](https://github.com/openai/skills) | 历史技能打包方式、源与生成副本分离、脚本实证 |
| [obra/superpowers](https://github.com/obra/superpowers) | 证据驱动调试、明确假设、限定范围的审查 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 按框架触发、按影响排序性能问题 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 区分技能、指令与代理角色，保持职责集中 |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 沿真实调用链核对安全边界，用反例检验结论 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | PostgreSQL 执行计划、索引、连接预算与事务/锁边界 |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 根据实时定位器操作、隔离浏览器会话、区分动作和断言证据 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 从界面需求推导字体、组件与平台选择 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 继承已有设计规范，区分局部设计与共享标准 |
| [wshobson/agents](https://github.com/wshobson/agents) | 设计令牌、可复用组件、平台差异与适量动效 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 需求就绪度、任务交接、质量门槛、迁移、性能与可观测性 |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills) | 迁移兼容性、数据对账与恢复能力的真实边界 |
| [rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills) | 集成关系梳理、按业务分批迁移、明确执行责任 |

## 许可

原创内容采用 [MIT](LICENSE)，未重新分发上游技能正文、代码、模板、素材或数据库。各来源许可独立适用；其中 Trail of Bits 来源为 CC-BY-SA-4.0，未将其正文改编为 MIT 内容。逐项许可范围见第三方说明。
