---
name: aw-evidence-verification
description: "Use before claiming a change is fixed, checks passed, acceptance completed, or a release is ready, to align each claim with evidence for the final artifact."
license: MIT
---

# 完成前证据核对

让结论精确对应实际证据。

构建、模拟页、代理总结不等于真实行为/云/生产验收。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 在定向收尾之后逐项核对最终差异对应哪条需求或必要联动，确认保留行为和各项验收范围，不交付无关的本任务增量；新增业务文件有必要，本次失效逻辑已收敛且无无关重构。
2. 核对最终代码/运行版本、命令范围、输出和退出码；缺陷结论须对应关键真实数据、原症状及完整受影响链路。编译/替身通过不能支持已修复；关键未验只报代码已改/局部通过及缺口。
3. 复用仍覆盖最终状态的证据；收尾影响工程输入只补相关检查，无关日志/报告删除不触发全量重跑。
4. 列出缺口和影响，不用“应该通过”作完成结论。

## 交付

证据清单、可支持的结论与未验证项。 未核实项如实标注。

## 按需资料

- [evidence-verification.md](references/evidence-verification.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
