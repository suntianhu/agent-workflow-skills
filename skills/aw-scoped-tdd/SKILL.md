---
name: aw-scoped-tdd
description: "Use only after TDD has been selected for a bounded feature or reproducible defect and its execution and artifact retention are authorized."
license: MIT
---

# 已授权局部TDD

用真实失败驱动最小修复，避免测试堆积。

本次已选择并授权TDD及保留政策；老项目先全仓与内部规范，新项目先用户选栈与规范，不删除用户实现制造红灯。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 按项目原生工具和已定目录复用最小用例，观察针对真实目标行为的失败，排除环境/语法错误及替代实现伪验证。
2. 最小实现转绿，必要重构后对最终代码局部复核。
3. 同轮重试复用载体，限制新增范围；保存真实红绿证据和精确产物清单，按约定交接保留/清理，不滚动堆测试文件。

## 交付

实际红/绿证据、最终版本复核、保留/清理清单。 未核实项如实标注。

## 按需资料

- [scoped-tdd.md](references/scoped-tdd.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
