---
name: aw-backend-implementation
description: "Use when implementing API services, business logic, persistence, migrations, tasks, or integrations after existing/new project prerequisites are satisfied."
license: MIT
---

# 后端实现

按实际栈的内部规范实现业务与数据边界。

## 前置条件与边界

不固定ORM/数据库/分层库；老项目先全仓与规范，新项目先用户选栈。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 读取真实入口、业务、事务、数据与部署规范。
2. 落实输入、归属、错误、并发/幂等、迁移和外部调用边界。
3. 执行规定工程检查及允许的局部验证，同步契约与规范。

## 必须得到的结果

后端改动、契约/迁移/规范同步及实际证据。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [backend.md](references/backend.md)：本次触发该能力时读取。
- [project-mode.md](references/project-mode.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
