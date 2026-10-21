---
name: aw-performance-optimization
description: "Use when a user requests performance investigation or budgets, or concrete latency, throughput, resource-use or regression symptoms require measurement, bottleneck evidence and comparable before/after results across frontend, backend or data paths. Not for speculative cleanup or ordinary feature implementation."
license: MIT
---

# 性能调查与优化

用可比较测量定位实际瓶颈，验证收益与业务正确性后决定保留。

沿用项目基线/规范和验证决定；测量/负载只在允许环境，产品修改保留开发门禁，不默认生产压测、安装工具或固定性能阈值。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 明确具体流程/症状、主要指标、成功口径和本次范围；复用已有版本/配置、测量与失败结论，不为已有决定重做需求访谈。
2. 核对工具与允许环境，固定设备/数据/负载、缓存/预热、样本/窗口及预算，取得可比较基线，报告缺环境和测量限制。
3. 按症状分段定位、提出可区分假设；数据专项按实际引擎读取，缺信号再交观测设计，不先叠缓存/索引或另建观测管道。
4. 优化并入唯一端内实现或已选TDD循环，保持必要业务工作量与正确性；用匹配条件复测，区分改善、噪声和未确定。
5. 只保留有依据的优化，撤回仅限本任务增量；记录失败尝试、实际结果及适用预算/回归观察，交证据核对，不自动扩成发布。

## 交付

性能目标、可比较基线/瓶颈证据、实现与正确性范围、复测/波动和保留决定、未验证项；复用项目现有记录。 未核实项如实标注。

## 按需资料

- [performance-optimization.md](references/performance-optimization.md)：测量设计、瓶颈定位、结果比较或优化保留判断有缺口时读取。
- [implementation-sources.md](references/implementation-sources.md)：测量/实现依赖版本敏感工具/API且尚无有效依据时读取。
- [postgres-data.md](references/postgres-data.md)：实际使用PostgreSQL/Supabase且瓶颈涉及查询、连接、锁或计划证据时只读相关段落。
- [performance-record.md](assets/performance-record.md)：按指南使用；模板按真实项目填写。

本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
