---
name: aw-scoped-tdd
description: "Use only after TDD has been selected for a bounded feature or reproducible defect and its execution and artifact retention are authorized."
license: MIT
---

# 已授权局部TDD

用真实失败驱动最小修复，避免测试堆积。

## 前置条件与边界

本次已选择并授权TDD及保留政策；老项目先全仓与内部规范，新项目先用户选栈与规范，不删除用户实现制造红灯。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 观察针对真实行为的失败并排除环境/语法错误。
2. 最小实现转绿，必要重构后对最终代码局部复核。
3. 保存脱敏红绿证据与本任务产物清单，按约定交给交付清理阶段处理保留或删除。

## 必须得到的结果

实际红/绿证据、最终版本复核、保留/清理清单。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [scoped-tdd.md](references/scoped-tdd.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
