---
name: aw-design-standards
description: "Use when explicitly requested to establish shared project design standards, or when product implementation needs shared tokens, components, content or platform rules; a standalone page draft does not require a project design system."
license: MIT
---

# 跨平台项目设计规范

形成接回项目唯一规范入口的共用设计规则。

## 前置条件与边界

只设计单页/独立原型不强制建体系；需要共用规范时复用原有设计文档/token/组件与项目规范入口。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 读取同一项目基线、技能采纳表、需求与参考；提取既有设计事实，区分新决定、例外与未知。
2. 明确共用语义、内容、token/组件与状态；按实际发布平台映射导航、输入、单位和可访问性。
3. 维护现有规范入口及可读相对引用，核对真实消费者与验证边界，后续技能沿用同一决定。

## 必须得到的结果

项目内设计规则/子文档、真实 token/组件映射、平台边界、采纳依据及入口/验证证据。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [design-standards.md](references/design-standards.md)：触发本技能时读取的基础指南。
- [ui-system.md](references/ui-system.md)：需要具体排版、密度、状态与资源细则时读取。
- [design-platforms.md](references/design-platforms.md)：设计包含平台交互、设备/窗口或跨端映射时，只读实际目标部分。
- [design-standards.md](assets/design-standards.md)：按指南使用；模板按真实项目填写。

本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
