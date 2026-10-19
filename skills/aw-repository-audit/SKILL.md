---
name: aw-repository-audit
description: "Use before developing code, configuration, or engineering scripts in an existing project when a current complete codebase review and project standards baseline are required."
license: MIT
---

# 老项目全仓梳理

读完当前项目全部自有代码，形成可追溯全仓理解。

## 前置条件与边界

不得用目录扫描、抽样、已有README或局部检索冒充全仓阅读；未完成不开始产品实现。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 清点隐藏/未跟踪、前后端、共享库、迁移、生成器、CI和部署。
2. 逐项阅读，记录每项用途、调用关系、约束、证据和指纹；排除项给实际依据。
3. 汇总完整阅读证据与真实阻断，交给内部规范阶段；规范完成前不开始产品实现。

## 必须得到的结果

全仓清单、逐项阅读台账、模块/数据流地图、真实未读/排除/阻断。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [repository-audit.md](references/repository-audit.md)：本次触发该能力时读取。
- [audit-tool.md](references/audit-tool.md)：本次触发该能力时读取。
- [repo_audit.py](scripts/repo_audit.py)：按指南使用；模板按真实项目填写。
- [reading-ledger.json](assets/reading-ledger.json)：按指南使用；模板按真实项目填写。

本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
