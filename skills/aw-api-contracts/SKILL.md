---
name: aw-api-contracts
description: "Use when requests, responses, validation, pagination, errors, timestamps, identity, persistence or shared configuration contracts change across callers and services."
license: MIT
---

# 前后端契约

保持全部直接调用方与数据语义一致。

不遗漏受影响端和直接调用方；兼容性单端变更可只改该端，说明其他调用方无需修改的依据，不凭类型编译推断兼容。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 追踪入口、调用方、旧数据和错误/恢复路径。
2. 核对字段、枚举、分页、时区、身份、幂等和兼容；可维护参数还要追踪维护入口、消费者、生效方式及私密边界。
3. 将事实落入项目内部规范，报告实际契约验证范围。

## 交付

契约差异、受影响调用方、兼容/恢复策略与证据。 未核实项如实标注。

## 按需资料

- [api-contracts.md](references/api-contracts.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
