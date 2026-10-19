---
name: aw-delivery-cleanup
description: "Use when preparing a task handoff and removing only confirmed task-owned disposable artifacts while preserving user changes, runtime files, and production outputs."
license: MIT
---

# 交付与定向清理

按精确清单交付与清理。

## 前置条件与边界

不批量删用户已有测试/整个构建目录；策略拒绝后停止绕行。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 核对本次文件、实际用途、入口/引用/依赖和约定保留方式。
2. 核实绝对路径、授权范围与重定向后定向清理。
3. 把清理后最终文件与受影响证据交给完成前核对，再交付实际结果与缺口；仅工程输入变化需定向补验。

## 必须得到的结果

最终改动、清理结果和真实保留/阻断项。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [delivery-cleanup.md](references/delivery-cleanup.md)：触发本技能时读取的基础指南。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
