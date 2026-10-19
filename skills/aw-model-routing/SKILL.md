---
name: aw-model-routing
description: "Use when deciding whether the current model and tools can complete a task or whether additional reasoning, vision, or delegation has a concrete benefit."
license: MIT
---

# 模型与能力判断

根据能力缺口选择资源。

## 前置条件与边界

不能自行切换当前聊天模型或虚构允许列表；普通小改不追加模型。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 识别歧义、上下文、视觉输入、推理与执行需求。
2. 优先当前能力，只有具体瓶颈才核对可用选项与当前官方事实。
3. 委派另核对授权、独立性和开销；无代理可顺序完成。

## 必须得到的结果

能力判断、依据及必要的调整建议。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [model-routing.md](references/model-routing.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
