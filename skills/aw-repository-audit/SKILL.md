---
name: aw-repository-audit
description: "Use before implementing in an existing project when complete code understanding is missing or changes since a verifiable baseline need review; reuse valid unchanged coverage instead of restarting for each request."
license: MIT
---

# 老项目全仓梳理

形成或补齐覆盖当前项目的可核对完整代码理解。

## 前置条件与边界

不得用目录扫描、抽样、已有README或局部检索冒充全仓阅读；未完成不开始产品实现。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 先核对现行规范、完整阅读记录与版本/指纹；已有基线承接未变覆盖并补查全部差异，没有可核对基线才全仓清点。
2. 逐项阅读缺失/变化及直接影响，无基线时读全部自有代码；记录用途、关系、约束和证据，排除项给实际依据。
3. 汇总完整阅读证据与真实阻断，交给内部规范阶段；规范完成前不开始产品实现。

## 必须得到的结果

全仓清单、逐项阅读台账、模块/数据流地图、真实未读/排除/阻断。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [repository-audit.md](references/repository-audit.md)：触发本技能时读取的基础指南。
- [audit-tool.md](references/audit-tool.md)：触发本技能时读取的基础指南。
- [repo_audit.py](scripts/repo_audit.py)：按指南使用；模板按真实项目填写。
- [reading-ledger.json](assets/reading-ledger.json)：按指南使用；模板按真实项目填写。

本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
