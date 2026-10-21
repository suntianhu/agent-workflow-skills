# 组合条件与执行顺序

九份JSON清单是本集合的文档格式（schema 2），不是Agent Skills标准或执行引擎。宿主不会仅因这些文件存在自动执行。skills是可导出的条件能力闭包，不表示所有技能无条件运行；stages逐项给when和说明，conditions解释触发，optional仅包含有收益且获授权的代理协作。

## 最短适用路径

先按描述选主要能力，只有缺口才加载另一项正文；参考按问题读相关段落。同一判断与验证决定不重复做，不按技能数量开代理。

| 实际任务 | 足够的路径 |
| --- | --- |
| 已明确的文案/普通文档 | 项目规则 → 修改 → 核对差异；无需单独需求、设计、估时或代理 |
| 有效基线内的明确代码改动 | 相关端实现 → 既定局部验证 → 必要的一次反例核对；前置产物直接消费 |
| 单独页面稿 | UI设计 → 可查看产物；老产品仍继承旧字体/主题/组件，正式接入另满足门禁 |
| 故障定位 | 调试 → 允许范围的区分证据；授权修复后只接影响端，不重开全流程 |
| 已验证代码的提交/发布 | 发布准备 → 目标产物与必要环境核对；不因提交再实现一次 |

技能选择、模型路由和估时现在分别使用独立条件；加载其中一项不带上另两项。小任务可内联判断，复杂任务需要时再扩展。修改用户已有 Skill 的具体方案先确认，普通业务改动不因此多一轮审批。

先判断交付物：只写需求、单页视觉稿或独立展示原型，直接选对应能力并在产物处停止。正式实施才判断阅读/规范/选栈/范本缺口，不能只按新旧身份选择全部阶段；缺项目规范不强迫单页稿建设体系。可运行原型在 UI 阶段制作，编写可运行代码/执行自动交互前承接同一次局部验证决定，不能混入产品代码或真实业务；正式接入后再满足完整门禁。

## 共用阶段

1. 识别项目与范围；资源判断/估时按实际需要进行。
2. 老项目用 existing-audit-needed 与 existing-standards-needed 分开判断：缺阅读覆盖才补审计，阅读已完成而规则缺失就只补同一规范；可核对基线承接全部差异，不按轮次全读。新产品用 new-stack-needed、new-reference-needed、new-standards-needed 分别判断选择/依据/规范缺口；已完成且仍有效的阶段直接消费产物，不重选、重搜或重填。fullstack只执行对应新/旧分支。
3. 需求设计按需头脑风暴；有界面时依缺口做设计参考→项目共用设计规范→页面 UI，再衔接契约与信任边界。已有规则直接复用；纯 API 跳过设计参考、设计体系与 UI 阶段。
4. **实现前**选择测试范围、TDD和保留。有具体性能目标/症状或观测缺口时，专项前置只补方案/基线，改变并入唯一端内实现；选TDD时以其统筹红绿循环，implementation_constraints给出需在循环内使用的端内约束，跳过独立实现阶段；未选TDD才执行implementation-without-tdd。专项后置仅补最终比较/信号证据，已有效则复用。P0不擅自恢复。
5. 常规/关键改动需要只读反例审查时，先复用覆盖最终产物的有效结果，修复后只复核相关差异。最后先定向清理，再核对最终证据并交付；收尾改变工程输入才补受影响检查，删无关日志不重测。小改只核对需求/diff，不因清单存在启动全套仪式。

## 九种组合

| 组合 | 条件重点 |
| --- | --- |
| [existing-frontend](../bundles/existing-frontend.json) | 全仓/规范先行；只实现前端，契约/安全按涉及触发 |
| [existing-backend](../bundles/existing-backend.json) | 全仓/规范先行；需求、契约、权限/数据边界与后端实现 |
| [new-frontend](../bundles/new-frontend.json) | 用户选框架后制定规范；UI适用，契约/安全按涉及触发 |
| [new-backend](../bundles/new-backend.json) | 行为需求先明确；用户选栈与范本规范后开发服务 |
| [fullstack](../bundles/fullstack.json) | 明确新/旧分支，前后端独立规范与共同契约 |
| [project-migration](../bundles/project-migration.json) | 老产品保留台账、目标/共存、业务分批、数据与任务交接、恢复与退役；代理仅可选 |
| [small-change](../bundles/small-change.json) | 文档/文案无需全量设计；老代码缺基线时仍先全仓/规范；新代码项目先走选栈/范本/规范条件分支；只选受影响端 |
| [debug-and-fix](../bundles/debug-and-fix.json) | 复现前先选策略；静态调查可先行，实际修复仍受全仓与规范门禁约束 |
| [release](../bundles/release.json) | 只有请求发布才做准备；仅公开分发触发开源检查。发现代码修复需交接到相应开发组合再返回 |

内部部署不自动执行开源检查；纯发布准备不自动执行TDD或启动产品实现。导出闭包保留所有可能需要的条件技能，--include-optional只额外带代理协作；导出不会安装，既有目录和集合内部路径均拒绝。

六个可涉及 UI 的组合（existing-frontend、new-frontend、fullstack、small-change、debug-and-fix、project-migration）包含条件设计阶段。design-reference-needed 只在要求借鉴或仍需依据时触发；design-standards-needed 只在共用规则新增/变化或缺少所需规范时触发；ui-change 要求实际界面范围。条件闭包导出不表示全部运行。后端与发布组合不增加 UI 流程。

## 项目迁移增量（1.2.5）

[project-migration](../bundles/project-migration.json) 使用老项目门禁，以迁移技能统筹保留映射、目标/过渡方案、贯通样本、业务分批和切换/恢复。目标目录新建不等于新产品；只写方案不授权实现或生产操作。目标选型由迁移方案处理，不调用限定真正新产品的选型阶段。UI、契约、安全、TDD和代理均按范围触发，批次内依据任务图迭代，前置已有效时不复跑。详见[迁移用法与边界](project-migration.md)。

## 性能与可观测性条件（1.2.5）

九组合不增加。八个开发/排障/迁移组合携带 aw-performance-optimization 与 aw-observability 的条件闭包；performance-scope-needed / observability-scope-needed 只补对应方案和现有证据缺口，performance-result-needed / observability-result-needed 只补最终结果，均不额外拥有一次实现。无对应目标或变化就跳过。release 组合消费现成结果，缺口交回实施，不增加自动压测、埋点或通知阶段。规则归属和避免重复的交接见[采纳与专项职责](adoption-integration.md)。
