---
name: aw-test-strategy
description: "Use before code implementation or behavioral validation to decide test scope, whether TDD is selected, existing project policy, and disposable versus retained artifacts."
license: MIT
---

# 测试策略与保留

分开验证范围、TDD顺序与保留政策。

## 前置条件与边界

小改不自动TDD；不把其他项目禁测规则推广全局；已有用例不擅删。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 读取当前用户/项目P0/P1/P2政策和真实风险。
2. 选择必要工程检查与直接行为路径，不间接运行禁用套件。
3. 沿用已有选择并交接执行；实质升级成本/保留政策才一次确认，本阶段不实现或清理。

## 必须得到的结果

本次验证与保留决定、实际命令范围和必要未决选择。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [test-strategy.md](references/test-strategy.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
