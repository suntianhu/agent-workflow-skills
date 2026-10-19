---
name: aw-repository-audit
description: "Use before implementing in an existing project when complete code understanding is missing or changes since a verifiable baseline need review; reuse valid unchanged coverage instead of restarting for each request."
license: MIT
---

# 老项目全仓梳理

形成或补齐覆盖当前项目的可核对完整代码理解。

不得用目录扫描、抽样、已有README或局部检索冒充全仓阅读；未完成不开始产品实现。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 先核对现行规范、完整阅读记录与版本/指纹；已有基线承接未变覆盖并补查全部差异，没有可核对基线才全仓清点。
2. 逐项阅读缺失/变化及直接影响，无基线时读全部自有代码；记录用途、关系、约束和证据，排除项给实际依据。
3. 汇总完整阅读证据与真实阻断，交给内部规范阶段；规范完成前不开始产品实现。

## 交付

全仓清单、逐项阅读台账、模块/数据流地图、真实未读/排除/阻断。 未核实项如实标注。

## 按需资料

- [repository-audit.md](references/repository-audit.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [audit-tool.md](references/audit-tool.md)：需要清点/校验台账工具时读取；手工有效记录不额外跑工具。
- [repo_audit.py](scripts/repo_audit.py)：按指南使用；模板按真实项目填写。
- [reading-ledger.json](assets/reading-ledger.json)：按指南使用；模板按真实项目填写。

本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
