---
name: aw-delivery-cleanup
description: "Use when preparing a task handoff and removing only confirmed task-owned disposable artifacts while preserving user changes, runtime files, and production outputs."
license: MIT
---

# 交付与定向清理

按精确清单交付与清理。

不批量删用户已有测试/整个构建目录；策略拒绝后停止绕行。

沿用当前项目规范、有效基线及验证决定，缺口才补。改写、合并或替换用户已有 Skill，先展示具体差异并获明确确认；已确认范围直接沿用。只使用本次获授权的工具与操作。

## 执行

1. 核对本次文件、实际用途、入口/引用/依赖和约定保留方式；确认实现已清理本次失效业务逻辑，保留仍有兼容用途或未证实无用的代码。
2. 核实绝对路径、授权范围与重定向，按清单清理项目内任务自有临时文件和空任务目录，并确认实际结果；路径在项目内不等于自动获得工具删除权限。
3. 把清理后最终文件与受影响证据交给完成前核对，再交付实际结果与缺口；仅工程输入变化需定向补验。

## 交付

最终改动、清理结果和真实保留/阻断项。 未核实项如实标注。

## 按需资料

- [delivery-cleanup.md](references/delivery-cleanup.md)：入口不足以处理本次细节时，仅读相关段落；已读且未变则复用。


本目录可独立使用；只补真实缺口，不自动串联其他技能。组合是条件说明，不是必跑清单。
