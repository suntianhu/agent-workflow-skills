---
name: aw-effort-estimation
description: "Use when estimating remaining work, revising a time range after new evidence, or calibrating repeated overestimation from comparable measured tasks."
license: MIT
---

# 基于实耗的估时

给可校准的本地剩余时间，外部未知单列。

## 前置条件与边界

先调查再估；已测步骤不重复校准，已完成调查不计入剩余。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 读取真实时钟和用户时区，分解未完成实现/检查/审查/清理。
2. 用同类实耗比例校准未校准实现部分，缺样本时明确先验。
3. 范围/假设改变就更新；完成后只记录真实匿名分钟。

## 必须得到的结果

时间范围、证据/样本数、未知阶段与偏差。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [effort-estimation.md](references/effort-estimation.md)：本次触发该能力时读取。
- [estimate.py](scripts/estimate.py)：按指南使用；模板按真实项目填写。

本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
