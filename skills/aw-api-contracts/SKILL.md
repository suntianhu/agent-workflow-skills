---
name: aw-api-contracts
description: "Use when requests, responses, validation, pagination, errors, timestamps, identity, or persistence contracts change across callers and services."
license: MIT
---

# 前后端契约

保持全部直接调用方与数据语义一致。

## 前置条件与边界

不能只改一端或凭类型编译推断实际兼容。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 追踪入口、调用方、旧数据和错误/恢复路径。
2. 核对字段、枚举、分页、时区、身份、幂等和兼容。
3. 将事实落入项目内部规范，报告实际契约验证范围。

## 必须得到的结果

契约差异、受影响调用方、兼容/恢复策略与证据。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [api-contracts.md](references/api-contracts.md)：触发本技能时读取的基础指南。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
