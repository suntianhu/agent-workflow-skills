---
name: aw-delivery-cleanup
description: "Use when preparing a task handoff and removing only confirmed task-owned disposable artifacts while preserving user changes, runtime files, and production outputs."
license: MIT
---

# 交付与定向清理

按精确清单交付与清理。

## 前置条件与边界

不批量删用户已有测试/整个构建目录；策略拒绝后停止绕行。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 核对本次文件、实际用途、入口/引用/依赖和约定保留方式。
2. 核实绝对路径、授权范围与重定向后定向清理。
3. 交付结果、实际证据、回归记录和未完成事项。

## 必须得到的结果

最终改动、清理结果和真实保留/阻断项。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [delivery-cleanup.md](references/delivery-cleanup.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
