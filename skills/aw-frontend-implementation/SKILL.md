---
name: aw-frontend-implementation
description: "Use when implementing frontend pages, admin UI, components, routing, state, or platform interactions after the relevant existing/new project gates are satisfied."
license: MIT
---

# 前端实现

按项目规范实现正确交互与状态。

## 前置条件与边界

已有项目先全仓梳理和内部规范；新项目先用户选栈和范本规范。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 读取前端规范与实际后端契约，识别路由/状态/样式/平台边界。
2. 实现正常、加载、错误、重试、取消、重复操作和账号切换。
3. 执行项目规定工程检查，按测试政策验证直接影响并更新规范；需要且允许浏览器交互验证时读取browser-validation.md。

## 必须得到的结果

前端改动、规范同步、工程/行为证据与外部缺口。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [frontend.md](references/frontend.md)：触发本技能时读取的基础指南。
- [project-mode.md](references/project-mode.md)：触发本技能时读取的基础指南。
- [browser-validation.md](references/browser-validation.md)：本次需要且允许浏览器实际交互验证时读取；不自动安装工具或新增持久测试。
- [design-platforms.md](references/design-platforms.md)：涉及平台原生交互、设备/窗口适配或跨端迁移时，只读目标平台相关部分。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
