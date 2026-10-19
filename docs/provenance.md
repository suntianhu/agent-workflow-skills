# GitHub蒸馏来源与取舍

1.4.0 共记录 **11 个公开仓库、54 个选定文件**。本版新增 Impeccable、wshobson/agents 两仓的 10 个文件，并在原固定的 obra/superpowers 快照补取头脑风暴文件；许可和 NOTICE 计入文件数。具体日期、固定提交、原始字节散列、大小与部分阅读范围见 [upstreams.json](../provenance/upstreams.json)。官方设计网站另记[实际取证与访问缺口](../provenance/design-references.json)，不计作已审阅的上游技能仓库。

## 既有研究与许可边界

1.3.0 共记录九个公开仓库、43 个选定文件：前五仓的 15 个文件取得于 2026-10-18，新增四仓的 28 个文件取得于 2026-10-19。固定提交、原始字节散列、大小及本次阅读范围见 [upstreams.json](../provenance/upstreams.json)。完整文件已取得不等于全文审阅；部分文件只读相关章节或数据行。这是选定材料研究，不是整仓审计。

基于抽象思想与本集合需求独立撰写规则，不分发上游技能正文、翻译、脚本、资产、数据库、SQL 示例或报告模板。各上游许可分别记录；“蒸馏”不是把外部作品重新授权为 MIT 的方法。

| 来源 | 实际采纳的原则 | 明确不采纳 |
| --- | --- | --- |
| anthropics/skills | 短入口与按需资源、任务边界评估、简报驱动视觉 | 虚构客户背景、激进全任务触发、Claude专属评测链条 |
| openai/skills | 单一信息源、粒度与风险适配、验证脚本实际运行 | 该快照README已标弃用，仅作历史结构参考；不强依赖其初始化脚本 |
| obra/superpowers | 复现/数据流/单一假设、确认真实失败、分离审查职责 | 一切先TDD、全量套件、删除用户实现重做、强制worktree与代理 |
| vercel-labs/agent-skills | 栈限定触发、按影响排序、具体规则渐进加载、可定位审查 | 把React/Next/Vercel规则推广所有栈；每次自动取远端指令并扩大授权 |
| github/awesome-copilot | 明确技能/指令/代理区别、单职责、固定来源、补足真实能力缺口 | Copilot工具名和.agent.md作为通用前提；外部插件自动继承许可/授权 |
| trailofbits/skills | 从实际调用链建立证据、变更前后控制比较、主动查反证、保留未决结论 | 强制代理、固定阶段/数量、二元判定、审查切换工作区、复制其表达或报告格式 |
| supabase/agent-skills | 基于查询计划选索引、连接预算、事务与锁、实际角色下的 RLS | 性能倍数、游标恒定耗时、顺序扫描必缺索引、固定池参数/端口、事务池能力一概而论 |
| microsoft/playwright-cli | 当前页面定位、会话隔离、操作与断言分开、mock/trace 证据边界 | 强制安装 CLI、录制即验收、默认持久测试、全局关浏览器、导出私人会话 |
| nextlevelbuilder/ui-ux-pro-max-skill | 需求驱动设计规则、全局约定与局部差异、密度/状态/资源核对 | 复制搜索库/模板/素材、固定风格与数值、覆盖既有设计规范、自动安装与全主题检查 |
| pbakaus/impeccable | 先提取并继承既有设计、局部扩展与整体体系分开、按目标平台重构体验 | 强制随机概念/固定候选数、强制审批/代理、专用工具与格式、根目录并行规范、复制平台参考正文 |
| wshobson/agents | 适量语义 token、组件职责、移动平台分别适配、目的明确的状态反馈 | 强制 React/Figma/主题工具链、固定动画数值、把代码示例当当前官方 API、把移动规则推广所有端 |

obra/superpowers 的补充头脑风暴阅读用于具体使用场景、目标/非目标、区分假设和已有选择、按复杂度表达方案；不继承固定文档路径、强制审批、伴随工具或全任务问答仪式。

新旧项目门禁、全仓阅读后内部规范、语言→候选→用户选择→范本→规范的流程来自本集合明确需求。PostgreSQL 专项补充不代表所有后端技术栈都完成了上游专项验证。多代理只研究相关职责与分离原则，没有声称审阅全部实现。

老仓库既有 Skills、代理/插件配置的清点，以及后续启用技能必须接回同一项目规范的规则，来自本次用户明确要求。其落点包括项目判断、全仓阅读、技能采纳、规范模板和交接；不冒称来自新增上游或已在真实项目全流程验证。

## 1.3.0 四套新增资料的去重落点（历史）

保留 24 个技能、八套组合及原有阶段关系。新增四份按条件读取的指南；共同主题只在对应指南维护，生成副本用于技能独立分发，不要求重复加载。

| 唯一维护源 | 使用技能 | 职责边界 |
| --- | --- | --- |
| [安全证据](../guides/security-review-evidence.md) | aw-security-boundaries / aw-adversarial-review | 前者核对控制，后者只读评估；不重复实施修复 |
| [PostgreSQL](../guides/postgres-data.md) | aw-backend-implementation / aw-security-boundaries | 前者负责数据实现，后者按角色/策略核对；其他数据库不加载 |
| [浏览器验收](../guides/browser-validation.md) | aw-frontend-implementation | 按已选测试政策执行；aw-evidence-verification 只核对结论与证据 |
| [设计体系](../guides/ui-system.md) | aw-ui-design | 消费已有需求与规范，必要时补设计细则，不重做需求和选栈 |

原测试策略继续决定范围、TDD 与保留，不从上游继承强制测试。安全、数据库或浏览器能力也不扩大外部写入授权。

## 1.4.0 设计资料去重

新增 aw-design-reference 拥有设计参考证据与采纳，aw-design-standards 拥有项目共用规则；头脑风暴归原需求设计，UI 归原页面/流程设计。共用规则、平台问题和单页应用不重复拥有。

| 唯一维护源 | 条件使用者 | 边界 |
| --- | --- | --- |
| brainstorming.md | aw-requirements-design | 方向开放/用户要求时探索；已定方案不重复审批 |
| design-reference.md | aw-design-reference | 来源层级、实际访问证据、采纳/许可，不代替产品验收 |
| design-standards.md / 规范模板 | aw-design-standards | 同一项目规范入口、共用规则与实际源映射，不另起目录 |
| design-platforms.md | 参考、规范、UI、前端实现 | 按实际平台取相关行，生成副本不要求重复读取 |
| ui-system.md | aw-design-standards / aw-ui-design | 共用具体核对细则；规范定共用规则，UI 只应用与报告局部差异 |

Apple HIG、微信设计入口与 Material 页面本次存在正文访问限制，不能宣称已逐页核对；可读取的 Android、Fluent、Carbon、GOV.UK 和 WeUI README 也只记录实际文本范围，没有实际视觉或设备验收。资料链接是候选入口，不代表所有资源可复制或所有平台已经验证。

## 对具体规则的官方补核

2026-10-19 补查 PostgreSQL、PgBouncer、Supabase 与 Playwright 官方文档，核对 EXPLAIN 的执行副作用、组合索引和版本差异、池能力、请求身份与 RLS、定位与等待。它们是技术核对资料，不计为额外已蒸馏仓库；具体项目运行时仍按目标版本复核。

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- [PostgreSQL 组合索引](https://www.postgresql.org/docs/current/indexes-multicolumn.html)
- [PgBouncer 能力](https://www.pgbouncer.org/features.html)
- [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Playwright 定位](https://playwright.dev/docs/locators)与[可操作性](https://playwright.dev/docs/actionability)

## 当前官方示例入口

2026-10-18 的 openai/skills 快照 README 指向 [openai/plugins](https://github.com/openai/plugins)，当时补看了其 README。该补充只作为入口记录，不计入九仓固定文件审阅，也不代表每次已复核其当前状态；没有复制其插件或把 skill-only 目录冒充原生插件包。

## 许可范围

obra/superpowers与github/awesome-copilot已取得根MIT许可；Vercel React技能frontmatter标注MIT，但其他技能不能据此推断统一许可。Anthropic与OpenAI所读部分指向逐技能许可，未取得全部对应许可文件；未知许可的实现不复制。第三方贡献、链接的插件、文档、字体与素材始终各按自身许可。

新增四仓均取得固定提交的根许可：Trail of Bits 为 CC-BY-SA-4.0，Supabase 与 Next Level Builder 为 MIT，Microsoft Playwright CLI 为 Apache-2.0。只学习抽象方法，独立组织本集合规则；没有把 Trail of Bits 正文翻译或适配后挂 MIT，也没有随包携带其他三仓实现或数据。将来若复制或改编第三方表达，应先按具体文件许可处理归属、声明和分发条件，不能仅凭本次来源表推断授权。

本集合原创重写内容和工具用MIT分发，见[LICENSE](../LICENSE)。[第三方说明](../THIRD_PARTY_NOTICES.md)保留来源与边界，不声称MIT覆盖外部作品。

## 发行资料最小化

发行包只保留可公开的上游URL、固定提交、选定文件散列及取舍。个人安装清单、本地能力指纹、私有项目资料、回归日志与本机路径不属于公开来源记录，已移除。来源日期是取得快照的日期，不代表每次运行都已重查“最新”；具体选型仍须当次核查。

1.4.1 仅修订单页稿/独立原型/正式实施的范围与条件，来源仍为 11 仓、54 文件；没有新增来源阅读或把先前散列检查当成本轮新增证据。

1.4.2 为集合触发/衔接修正，来源仍 11 仓、54 文件，未新增外部研究。审计记录与少量隔离场景不等于上游重审或跨模型效果基准。
