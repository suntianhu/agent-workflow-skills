---
name: aw-project-migration
description: "Use when migrating an existing product to a different frontend/backend framework, language, architecture, ORM or database while preserving business behavior, APIs, scheduled jobs and data; plan phased replacement, coexistence, cutover, recovery and optional multi-agent work. Not for ordinary local refactors, simple dependency upgrades or greenfield projects."
license: MIT
---

# 项目迁移与框架重构

从真实迁移目标和业务保留项出发，按可独立验收的业务批次替换技术实现。

迁移到新目录仍按老产品理解行为；正式实施先满足有效全仓基线、同一项目规范、目标决定及验证策略。分析不自动授权实施/生产切换，多智能体按实际授权、独立性和工具判断。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 核实动机、范围、旧/新栈、停写窗口及成功条件；已有选择直接沿用，缺选择只推进无依赖调查，明确委托时自主核查决定。
2. 从源码、消费者和获授权的运行证据建立保留映射，覆盖前端/管理端、服务、入站/出站接口、回调、定时/异步任务、历史数据与文件；未知不等于可删除。
3. 比较原位演进、业务分批替换和窗口切换；明确契约/身份、数据权威写入方、任务执行权、兼容窗口、恢复边界与退役条件，不默认微服务或换库。
4. 在已授权实施及门禁满足后，先做代表性贯通样本，再按业务能力拆批；每任务给保留项ID、依赖、独占写入范围、输入契约、完成判据和停止/恢复条件。
5. 可独立任务才考虑并行；先稳定共享契约与模型，实际委派前读协作资料，明确唯一写入者和集成负责人；无工具或收益时顺序完成。
6. 按批实施与核验兼容矩阵、数据回填/增量对账、任务交接及受影响正常业务；数据与外部副作用的恢复不能仅靠撤回代码。
7. 切换前备齐可审阅步骤和演练证据，在具体授权范围内执行；逐项报告实现、演练、部署、切换、观察和退役状态，交代尚未验证项。

## 交付

同一项目内的迁移简报、保留/改变台账、目标与过渡方案、依赖任务图、文件/数据所有权、分批验收及切换/恢复/退役记录；复用已有等效文档。 未核实项如实标注。

## 按需资料

- [project-migration.md](references/project-migration.md)：目标、迁移路径、现状证据、分批方式或与既有能力衔接有缺口时读取。
- [migration-preservation.md](references/migration-preservation.md)：盘点或核验接口、定时/异步任务、身份、前后端与数据保留项时读取相关段落。
- [migration-execution.md](references/migration-execution.md)：需要共存、数据搬迁、对账、任务/写入切换、恢复或退役方案时读取。
- [migration-agents.md](references/migration-agents.md)：需要设计任务依赖/并行方案，或已授权且适合实际委派时读取；不强制启动代理。
- [task-planning.md](references/task-planning.md)：业务批次缺通用任务依赖、验收/所有权或恢复交接结构时读取；迁移字段仍在迁移记录维护。
- [project-migration-plan.md](assets/project-migration-plan.md)：按指南使用；模板按真实项目填写。
- [task-record.md](assets/task-record.md)：按指南使用；模板按真实项目填写。

本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
