---
name: aw-release-readiness
description: "Use when a user explicitly requests integration, a pull request, packaging, deployment, or release and the concrete artifact, rollback, and environment gates must be prepared."
license: MIT
---

# 发布准备与集成

把已授权发布推进到可审查产物和实际门槛。

不自动push/合并/公开发布；发布不授权未知真实交易或数据删除。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 检查分支/worktree/最终diff，只纳入本次文件。
2. 核对构建、配置、契约/迁移、备份回滚和真实环境验收。
3. 先完成独立可做准备，再说明缺失权限和未达门槛。

## 交付

可审查集成/发布产物、验证与回滚、外部阻断。 未核实项如实标注。

## 按需资料

- [release-readiness.md](references/release-readiness.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
