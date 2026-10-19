---
name: aw-adversarial-review
description: "Use for a scoped read-only review of a nontrivial change where requirements, contracts, ownership, recovery, privacy, or compatibility need counterexample analysis."
license: MIT
---

# 只读反例审查

找可观察反例，避免为实现背书。

轻微改动只核对需求/diff；代理审查需已有授权且不能变成测试/写入。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 读取原需求、最终差异、规则与检查证据。
2. 检查适用边界，逐项给位置、触发、后果和验证办法；仅疑似漏洞或安全相关差异另读security-review-evidence.md。
3. 将核实发现交给实现者处理；由实现者修复后，审查者只读定向复核。

## 交付

有证据的发现或限定范围未见阻断问题。 未核实项如实标注。

## 按需资料

- [adversarial-review.md](references/adversarial-review.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [security-review-evidence.md](references/security-review-evidence.md)：本次涉及疑似漏洞或安全相关差异时读取；通用审查不加载。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
