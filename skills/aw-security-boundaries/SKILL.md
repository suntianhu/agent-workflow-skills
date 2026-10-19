---
name: aw-security-boundaries
description: "Use when a change affects authentication, authorization, ownership, private files, external requests, payment, refund, or other concrete trust boundaries."
license: MIT
---

# 应用安全边界

核对本次实际信任边界与恢复路径。

## 前置条件与边界

不是无范围全仓渗透；不操作未知金额/对象的交易或真实业务数据。 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

## 执行

1. 识别入口身份、资源归属、输入和外部依赖。
2. 按涉及点核对授权/私图/SSRF/签名/支付退款/日志与幂等。
3. 限定静态检查、局部行为与真实渠道证据，保留未验门槛。

## 必须得到的结果

有证据的边界发现、修复与真实外部验证缺口。 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

- [security-boundaries.md](references/security-boundaries.md)：本次触发该能力时读取。


本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
