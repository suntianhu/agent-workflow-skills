---
name: aw-adversarial-review
description: "Use for a scoped read-only counterexample review of a nontrivial change or a high-impact unresolved decision involving requirements, contracts, ownership, recovery, privacy, compatibility or quality-gate changes; not for routine local edits."
license: MIT
---

# 只读反例审查

找可观察反例，避免为实现背书。

轻微改动只核对需求/diff；代理审查需已有授权且不能变成测试/写入。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 读取原需求、当前产物/差异、适用契约和实际证据，保留必要背景而不传作者预设结论；高影响未决方案可先审，已有有效结果直接复用。
2. 核对适用反例及本次质量门槛变化，给位置、可达触发、后果和依据；区分背景不足、有效问题、已接受取舍与误读，疑似漏洞才补安全证据资料。
3. 核实后交实现者处理，修复后只读定向复核；无新增实质证据即停止，不固定多轮或反复询问跨模型。

## 交付

有证据的发现或限定范围未见阻断问题。 未核实项如实标注。

## 按需资料

- [adversarial-review.md](references/adversarial-review.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [security-review-evidence.md](references/security-review-evidence.md)：本次涉及疑似漏洞或安全相关差异时读取；通用审查不加载。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
