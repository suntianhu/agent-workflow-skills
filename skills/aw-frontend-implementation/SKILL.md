---
name: aw-frontend-implementation
description: "Use when implementing frontend pages, admin UI, components, routing, state, or platform interactions after the relevant existing/new project gates are satisfied."
license: MIT
---

# 前端实现

按项目规范实现正确交互与状态。

消费已有有效完整基线、已选栈及同一规范；前置缺口先补齐，TDD循环内提供约束，不重复审计/选栈或另做实现。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 读取前端规范与实际后端契约，识别路由/状态/样式/平台边界。
2. 仅实现本次涉及的页面/状态与约束；加载、失败、重试、取消、重复或账号切换按真实行为选择，不补无关流程。
3. 执行项目规定工程检查，按测试政策验证直接影响并更新规范；需要且允许浏览器交互验证时读取browser-validation.md。

## 交付

前端改动、规范同步、工程/行为证据与外部缺口。 未核实项如实标注。

## 按需资料

- [frontend.md](references/frontend.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [project-mode.md](references/project-mode.md)：交付类型、新旧判断或开发门禁尚有缺口时读取；已有有效判断直接复用。
- [browser-validation.md](references/browser-validation.md)：本次需要且允许浏览器实际交互验证时读取；不自动安装工具或新增持久测试。
- [design-platforms.md](references/design-platforms.md)：涉及平台原生交互、设备/窗口适配或跨端迁移时，只读目标平台相关部分。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
