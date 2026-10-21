---
name: aw-backend-implementation
description: "Use when implementing API services, business logic, persistence, migrations, tasks, or integrations after existing/new project prerequisites are satisfied, including scoped PostgreSQL query, connection and locking work."
license: MIT
---

# 后端实现

按实际栈的内部规范实现业务与数据边界。

消费有效基线/选栈/范本/规范，缺口只交回对应阶段；不固定ORM/数据库/分层库，不在TDD后再实现。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 读取真实入口、业务、事务、数据与部署规范。
2. 只落实本次涉及的输入、归属、错误、并发/幂等、迁移与外部调用边界；实际涉及PostgreSQL/Supabase时再读postgres-data.md对应部分。
3. 缺陷优先在原职责位置最小充分修复；新增业务文件说明必要性，同步清理本次失效逻辑，不叠修复副本或夹带无关重构。
4. 执行规定工程检查及允许的局部验证，同步契约与规范；缺陷修复覆盖原症状、受影响正常业务及适用反例。

## 交付

后端改动、契约/迁移/规范同步及实际证据。 未核实项如实标注。

## 按需资料

- [backend.md](references/backend.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [project-mode.md](references/project-mode.md)：交付类型、新旧判断或开发门禁尚有缺口时读取；已有有效判断直接复用。
- [postgres-data.md](references/postgres-data.md)：实际使用PostgreSQL/Supabase且涉及查询、连接、锁、迁移或权限时读取。
- [implementation-sources.md](references/implementation-sources.md)：版本敏感行为、陌生接口或弃用/兼容冲突缺少有效依据时读取；已有适配来源直接复用，不重做选型。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
