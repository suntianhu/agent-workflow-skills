---
name: aw-evidence-debugging
description: "Use when investigating a reproducible defect, unexpected behavior, failed check, or integration symptom before selecting a code fix."
license: MIT
---

# 证据驱动排障

先定位实际根因，不叠猜测补丁。

## 前置条件与边界

产品修复仍须满足老项目全仓理解和内部规范门禁。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 记录已观察的最小复现、预期/实际和相关历史。
2. 沿层追踪，一个可证伪假设一次，选择最便宜允许证据。
3. 修根因及直接调用方，验证原症状并记录外部缺口。

## 必须得到的结果

根因、修复、实际验证和项目既有回归记录。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [evidence-debugging.md](references/evidence-debugging.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
