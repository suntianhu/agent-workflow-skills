---
name: aw-security-boundaries
description: "Use when a change affects authentication, authorization, ownership, private files, external requests, payment, refund, or other concrete trust boundaries, or when verifying a specific suspected security finding."
license: MIT
---

# 应用安全边界

核对本次实际信任边界与恢复路径。

## 前置条件与边界

不是无范围全仓渗透；不操作未知金额/对象的交易或真实业务数据。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

1. 识别入口身份、资源归属、输入和外部依赖；核实疑似漏洞或安全控制变更时读取security-review-evidence.md。
2. 按涉及点核对授权/私图/SSRF/签名/支付退款/日志与幂等；涉及PostgreSQL/Supabase角色、策略或租户隔离时读取postgres-data.md。
3. 限定静态检查、局部行为与真实渠道证据，保留未验门槛。

## 必须得到的结果

有证据的边界发现、修复与真实外部验证缺口。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [security-boundaries.md](references/security-boundaries.md)：触发本技能时读取的基础指南。
- [security-review-evidence.md](references/security-review-evidence.md)：核实具体疑似漏洞或安全控制变更时读取。
- [postgres-data.md](references/postgres-data.md)：涉及实际PostgreSQL/Supabase角色、策略或租户隔离时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
