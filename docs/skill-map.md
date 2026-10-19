# 技能职责与重复边界

24个技能按能力拆分，可选择其中一个或按组合使用。必要前置条件摘要出现在多个独立技能中是为保证单独使用不绕门禁；正文决策的拥有者如下。guides是维护源，skills中的参考/脚本/模板是便携发行副本，不是另一个需同时加载的流程。

## 项目与能力判断

| 技能 | 主产物/职责 | 与相邻能力的边界 |
| --- | --- | --- |
| [aw-project-triage](../skills/aw-project-triage/SKILL.md) | 项目类型、影响端、门禁 | 不负责写规范或实现 |
| [aw-skill-selection](../skills/aw-skill-selection/SKILL.md) | 技能采纳与冲突收敛 | 不强制加载全部技能 |
| [aw-model-routing](../skills/aw-model-routing/SKILL.md) | 现有模型/工具是否足够 | 不自行切换聊天模型 |
| [aw-effort-estimation](../skills/aw-effort-estimation/SKILL.md) | 剩余时间与实耗校准 | 不承诺未知外部完成时刻 |

## 理解与方案

| 技能 | 主产物/职责 | 与相邻能力的边界 |
| --- | --- | --- |
| [aw-repository-audit](../skills/aw-repository-audit/SKILL.md) | 全仓阅读证据与真实阻断 | 不把扫描当阅读，不重复拥有规范文档 |
| [aw-project-standards](../skills/aw-project-standards/SKILL.md) | 项目内规范唯一入口 | 消费审计/选栈证据，不编造现状 |
| [aw-framework-selection](../skills/aw-framework-selection/SKILL.md) | 语言约束下的框架候选与用户选择 | 用户未选定不初始化 |
| [aw-github-reference](../skills/aw-github-reference/SKILL.md) | 固定范本引用和采纳表 | 不复制无关业务/许可不明实现 |
| [aw-requirements-design](../skills/aw-requirements-design/SKILL.md) | 行为、数据、失败恢复与验收 | 不规定配色/字体，支持API/任务/迁移 |
| [aw-ui-design](../skills/aw-ui-design/SKILL.md) | 层级、布局、视觉token和反馈 | 消费需求简报，不重做需求审批 |

## 实现与验证

| 技能 | 主产物/职责 | 与相邻能力的边界 |
| --- | --- | --- |
| [aw-frontend-implementation](../skills/aw-frontend-implementation/SKILL.md) | 前端/后台UI与状态实现 | 遵从新旧门禁和内部规范 |
| [aw-backend-implementation](../skills/aw-backend-implementation/SKILL.md) | 服务、业务、数据与异步实现 | 不固定数据库/ORM/分层库 |
| [aw-api-contracts](../skills/aw-api-contracts/SKILL.md) | 调用方/服务之间的协议一致 | 不代替完整安全边界审查 |
| [aw-security-boundaries](../skills/aw-security-boundaries/SKILL.md) | 认证、授权、隔离与输入边界 | 支付/文件仅条件适用 |
| [aw-test-strategy](../skills/aw-test-strategy/SKILL.md) | 范围、TDD与保留决定 | 实现前完成，不执行红绿循环 |
| [aw-scoped-tdd](../skills/aw-scoped-tdd/SKILL.md) | 已授权红绿重构与最终证据 | 不再次选策略，不绕过项目门禁 |
| [aw-evidence-debugging](../skills/aw-evidence-debugging/SKILL.md) | 复现/假设/根因调查 | 代码修复仍需满足项目门禁 |
| [aw-adversarial-review](../skills/aw-adversarial-review/SKILL.md) | 只读反例与定位证据 | 实现者修复，审查者只读复核 |
| [aw-evidence-verification](../skills/aw-evidence-verification/SKILL.md) | 核对最终产物与完成声明 | 不重复跑无变化的全量检查 |

## 交付与维护

| 技能 | 主产物/职责 | 与相邻能力的边界 |
| --- | --- | --- |
| [aw-delivery-cleanup](../skills/aw-delivery-cleanup/SKILL.md) | 最终交付与任务内定向清理 | 不替代验收，不删未知用户文件 |
| [aw-release-readiness](../skills/aw-release-readiness/SKILL.md) | 已授权集成/发布准备与恢复 | 不自动授权远端发布/真实交易 |
| [aw-agent-coordination](../skills/aw-agent-coordination/SKILL.md) | 有界委派、所有权与交接 | 没有代理工具可顺序完成 |
| [aw-skill-authoring](../skills/aw-skill-authoring/SKILL.md) | 单职责技能与维护来源 | 不引入特定宿主隐藏依赖 |
| [aw-open-source-readiness](../skills/aw-open-source-readiness/SKILL.md) | 公开分发的许可/隐私/结构核对 | 本地就绪不等于已公开发布 |

需求→UI、审计→规范、策略→TDD、实现→只读审查→证据交付是交接关系，不要求重复产出同一份文档。TDD被选中时统筹实现，前/后端技能在循环内作为约束，不执行第二轮独立实现。复杂度不足以需要多个技能时，可在同一执行者内完成必要判断。

## 1.3.0 专项资料整合

新增来源不新增技能或组合。数据库实施细则由 aw-backend-implementation 的 postgres-data.md 维护；安全技能携带同源副本以支持独立角色/隔离核对。浏览器验证由前端实现按已选策略执行，证据技能只核对声明。设计体系细则归 UI，安全候选的调用链与反证资料由安全/只读审查按任务共用。具体[来源和去重表](provenance.md)记录取舍，专项资料仅匹配场景时读取。
