# 组合条件与执行顺序

八份JSON清单是本集合的文档格式（schema 2），不是Agent Skills标准或执行引擎。宿主不会仅因这些文件存在自动执行。skills是可导出的条件能力闭包，不表示所有技能无条件运行；stages逐项给when和说明，conditions解释触发，optional仅包含有收益且获授权的代理协作。

## 共用阶段

1. 识别项目与范围；资源判断/估时按实际需要进行。
2. 老项目缺本轮有效基线时，全仓阅读→项目内规范。真正新项目则需求/语言→框架核查→用户选择→GitHub范本→规范。fullstack只执行对应新/旧分支。
3. 按需求触发行为方案、UI、契约与信任边界核对。纯API也有需求与失败验收，不要求界面原型。
4. **实现前**选择测试范围、TDD和保留。选TDD时以其统筹红绿循环，implementation_constraints给出需在循环内使用的端内约束，跳过独立实现阶段；未选TDD才执行implementation-without-tdd。P0不擅自恢复。
5. 常规/关键改动做只读反例审查，由实现者处理确认问题，再定向复核、证据核对和交付清理。小改只核对需求/diff，不因清单存在启动全套仪式。

## 八种组合

| 组合 | 条件重点 |
| --- | --- |
| [existing-frontend](../bundles/existing-frontend.json) | 全仓/规范先行；只实现前端，契约/安全按涉及触发 |
| [existing-backend](../bundles/existing-backend.json) | 全仓/规范先行；需求、契约、权限/数据边界与后端实现 |
| [new-frontend](../bundles/new-frontend.json) | 用户选框架后制定规范；UI适用，契约/安全按涉及触发 |
| [new-backend](../bundles/new-backend.json) | 行为需求先明确；用户选栈与范本规范后开发服务 |
| [fullstack](../bundles/fullstack.json) | 明确新/旧分支，前后端独立规范与共同契约 |
| [small-change](../bundles/small-change.json) | 文档/文案无需全量设计；老代码缺基线时仍先全仓/规范；新代码项目先走选栈/范本/规范条件分支；只选受影响端 |
| [debug-and-fix](../bundles/debug-and-fix.json) | 复现前先选策略；静态调查可先行，实际修复仍受全仓与规范门禁约束 |
| [release](../bundles/release.json) | 只有请求发布才做准备；仅公开分发触发开源检查。发现代码修复需交接到相应开发组合再返回 |

内部部署不自动执行开源检查；纯发布准备不自动执行TDD或启动产品实现。导出闭包保留所有可能需要的条件技能，--include-optional只额外带代理协作；导出不会安装，既有目录和集合内部路径均拒绝。
