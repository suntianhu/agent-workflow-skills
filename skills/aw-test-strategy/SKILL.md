---
name: aw-test-strategy
description: "Use before code implementation or behavioral validation to decide test scope, whether TDD is selected, existing project policy, and disposable versus retained artifacts."
license: MIT
---

# 测试策略与保留

分开验证范围、TDD顺序与保留政策。

## 前置条件与边界

小改不自动TDD；不把其他项目禁测规则推广全局；已有用例不擅删。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 读取当前用户/项目P0/P1/P2政策和真实风险。
2. 确定目标语言/运行时、现有测试工具/目录/局部命令、复用用例与临时路径；验证实际目标，不用跨语言替代实现冒充功能证据。
3. 沿用已有选择并交接执行；实质升级成本/保留政策才一次确认，本阶段不实现或清理。

## 必须得到的结果

本次验证/TDD/保留决定、目标工具链与测试目录、复用/新增边界、临时产物收尾及必要未决项。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [test-strategy.md](references/test-strategy.md)：触发本技能时读取的基础指南。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
