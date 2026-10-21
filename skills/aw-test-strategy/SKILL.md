---
name: aw-test-strategy
description: "Use before code or behavior checks when validation scope, TDD choice or retention is missing or materially changed; consume an existing valid policy directly."
license: MIT
---

# 测试策略与保留

分开验证范围、TDD顺序与保留政策。

小改不自动TDD；不把其他项目禁测规则推广全局；已有用例不擅删。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 读取当前用户/项目P0/P1/P2政策和真实风险。
2. 确定原生工具链、复用用例与局部命令；临时验证默认放当前已授权本地项目内的独立任务目录，记录产物与清理边界，不默认使用系统TEMP；验证实际目标，不用跨语言替代实现冒充功能证据。 涉及核心依赖时明确真实产物、替身边界、适用输入边界与保存/读取往返契约。
3. 沿用已有选择并交接执行；实质升级成本/保留政策才一次确认，本阶段不实现或清理。

## 交付

本次验证/TDD/保留决定、目标工具链与测试目录、复用/新增边界、临时产物收尾及必要未决项。 未核实项如实标注。

## 按需资料

- [test-strategy.md](references/test-strategy.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
