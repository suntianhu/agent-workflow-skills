---
name: aw-evidence-debugging
description: "Use when investigating a reproducible defect, unexpected behavior, failed check, or integration symptom before selecting a code fix."
license: MIT
---

# 证据驱动排障

先定位实际根因，不叠猜测补丁。

产品修复仍须满足老项目全仓理解和内部规范门禁。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 记录已观察的最小复现、预期/实际和相关历史。
2. 沿层追踪，一个可证伪假设一次，选择最便宜允许证据。
3. 修根因及直接调用方，验证原症状并记录外部缺口。

## 交付

根因、修复、实际验证和项目既有回归记录。 未核实项如实标注。

## 按需资料

- [evidence-debugging.md](references/evidence-debugging.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
