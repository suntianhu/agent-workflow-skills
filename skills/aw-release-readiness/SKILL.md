---
name: aw-release-readiness
description: "Use when a user explicitly requests integration, a pull request, packaging, deployment, or release and the concrete artifact, rollback, and environment gates must be prepared."
license: MIT
---

# 发布准备与集成

把已授权发布推进到可审查产物和实际门槛。

## 前置条件与边界

不自动push/合并/公开发布；发布不授权未知真实交易或数据删除。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 检查分支/worktree/最终diff，只纳入本次文件。
2. 核对构建、配置、契约/迁移、备份回滚和真实环境验收。
3. 先完成独立可做准备，再说明缺失权限和未达门槛。

## 必须得到的结果

可审查集成/发布产物、验证与回滚、外部阻断。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [release-readiness.md](references/release-readiness.md)：触发本技能时读取的基础指南。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
