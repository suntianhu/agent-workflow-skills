---
name: aw-observability
description: "Use when designing, adding or verifying logs, metrics, traces, correlation or alerts to answer concrete operational questions or close an observability gap. Not for routine feature changes, diagnosis using sufficient existing telemetry, or performance optimization itself."
license: MIT
---

# 可观测性设计与验证

把运行问题映射为最小必要信号，并用实际输出证明可查询和可诊断。

复用现有观测栈、项目规范及验证决定；具体数据采集、外传、通知和故障演练受实际授权约束，不默认全站埋点、供应商或真实告警。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 明确运行问题、业务入口/成功语义与当前信号缺口；已有信号足够就复用，不新建重复管道/仪表盘。
2. 按问题选择日志/指标/链路或更轻证据，设计字段/单位/关联和查询；区分请求、调度、回调、队列与手工入口。
3. 明确脱敏、维度基数、采样/容量/保留、导出范围与失败/背压处置，按项目版本核查工具能力。
4. 埋点/配置并入唯一端内实现，按项目口径设计告警条件、去重/恢复和处置入口，不重复实施或选择验证策略。
5. 在允许环境核对实际信号、查询、关联、敏感字段与适用告警演练；配置存在、模拟通知和真实渠道送达分开陈述，缺口交证据核对。

## 交付

运行问题到信号/查询映射、数据/成本边界、实际信号与告警证据和未验证范围；复用现有记录及运维入口。 未核实项如实标注。

## 按需资料

- [observability.md](references/observability.md)：需要信号设计、数据/成本边界、查询/关联或告警验证细节时读取。
- [implementation-sources.md](references/implementation-sources.md)：采集/导出/关联依赖版本敏感API且尚无有效依据时读取。
- [observability-record.md](assets/observability-record.md)：按指南使用；模板按真实项目填写。

本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
