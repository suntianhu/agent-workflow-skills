---
name: aw-adversarial-review
description: "Use for a scoped read-only review of a nontrivial change where requirements, contracts, ownership, recovery, privacy, or compatibility need counterexample analysis."
license: MIT
---

# 只读反例审查

找可观察反例，避免为实现背书。

## 前置条件与边界

轻微改动只核对需求/diff；代理审查需已有授权且不能变成测试/写入。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 读取原需求、最终差异、规则与检查证据。
2. 检查适用边界，逐项给位置、触发、后果和验证办法；仅疑似漏洞或安全相关差异另读security-review-evidence.md。
3. 将核实发现交给实现者处理；由实现者修复后，审查者只读定向复核。

## 必须得到的结果

有证据的发现或限定范围未见阻断问题。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [adversarial-review.md](references/adversarial-review.md)：触发本技能时读取的基础指南。
- [security-review-evidence.md](references/security-review-evidence.md)：本次涉及疑似漏洞或安全相关差异时读取；通用审查不加载。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
