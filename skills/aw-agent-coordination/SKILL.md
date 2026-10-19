---
name: aw-agent-coordination
description: "Use when an authorized workflow has independent subtasks suitable for additional agents or needs a bounded handoff across agents or context windows."
license: MIT
---

# 智能体协作与交接

按真实工具、授权和文件所有权协调。

## 前置条件与边界

没有代理工具顺序完成；不把支持多个宿主等同自动启动多个代理。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 比较独立性、收益与协调成本。
2. 分派最小原始材料、读写边界、文件所有权和产物标准。
3. 主执行者核对真实文件与证据，传递状态和未完成项。

## 必须得到的结果

职责分工、边界、产物核对和交接状态。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [agent-coordination.md](references/agent-coordination.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
