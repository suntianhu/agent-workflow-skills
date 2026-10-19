---
name: aw-effort-estimation
description: "Use when the user asks for time or a substantial task needs an initial or revised remaining-time estimate; trivial edits do not need clock or logging overhead."
license: MIT
---

# 基于实耗的估时

给可校准的本地剩余时间，外部未知单列。

开始给有依据的初估并单列未知；辨明历史偏差方向，只校准同类未校准部分，不统一乘二或减半。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 用已知范围、项目检查命令与可信同类实耗给初始剩余区间；必要调查后修订，不先展开估时专项调研。
2. 同类实际/预计比值校准实现，少于三条标弱证据；验证/外部等待分别估，并行按关键路径计时。
3. 范围改变或接近上界及时更新；结束比较真实用时与偏差，持久记录只写约定位置。

## 交付

时间范围、证据/样本数、未知阶段与偏差。 未核实项如实标注。

## 按需资料

- [effort-estimation.md](references/effort-estimation.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [estimate.py](scripts/estimate.py)：按指南使用；模板按真实项目填写。

本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
