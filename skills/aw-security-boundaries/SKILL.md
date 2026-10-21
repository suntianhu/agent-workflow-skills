---
name: aw-security-boundaries
description: "Use when a change affects authentication, authorization, ownership, private files, external requests, payment, refund, or other concrete trust boundaries, or when verifying a specific suspected security finding."
license: MIT
---

# 应用安全边界

核对本次实际信任边界与恢复路径。

不是无范围全仓渗透；不操作未知金额/对象的交易或真实业务数据。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 识别入口身份、资源归属、输入和外部依赖；核实疑似漏洞或安全控制变更时读取security-review-evidence.md。
2. 按涉及点核对授权/私图/SSRF/签名/支付退款/日志与幂等；密码变更区分入口、认证/同值/强度顺序和成功写入；涉及PostgreSQL/Supabase角色、策略或租户隔离时读取postgres-data.md。
3. 限定静态检查、局部行为与真实渠道证据，保留未验门槛。

## 交付

有证据的边界发现、修复与真实外部验证缺口。 未核实项如实标注。

## 按需资料

- [security-boundaries.md](references/security-boundaries.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。
- [security-review-evidence.md](references/security-review-evidence.md)：核实具体疑似漏洞或安全控制变更时读取。
- [postgres-data.md](references/postgres-data.md)：涉及实际PostgreSQL/Supabase角色、策略或租户隔离时读取。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
