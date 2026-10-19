# 项目规范级 Skill 入口模板

这是供填写的入口结构，不是可直接安装的成品。先确定目标项目现有的规范目录和宿主项目级技能目录；正文只维护在现行规范入口，技能引用它。不要把本模板安装到全局，或在多个宿主目录复制规范正文。

复制下列结构到已确定的项目技能目录，按真实项目替换全部尖括号字段；description 要覆盖该项目真实触发范围，不吸引其他项目。规范路径从最终 SKILL.md 所在目录解析，交付前核对存在性、作用域和读取权限。

```yaml
---
name: project-<project-id>-standards
description: Apply the engineering conventions of <project-scope> when changing its code, configuration or scripts, or adopting a skill within that project.
---
```

```text
# <项目名称>工程规范入口

适用范围：<目标项目及实际子目录/工作区包>。
规范正文：<相对于本 SKILL.md 的真实项目规范路径>。
相关端规范：<现行规范中的章节或实际文件路径；不适用则删除>。

先读取适用目录的项目规则和上述现行规范，承接已有梳理、技能采纳、技术栈、冻结区、测试和保留决定，再开展本次任务。
新增或更新技能时，核对与当前规范的重复/冲突，将采纳决定和实际变化写回相同规范入口，不生成独立的竞争规则。
行为或工具链改变后核对规范的证据、命令和维护记录。未知事项先补证；此入口不授权迁栈、全局安装、生产操作或扩大测试范围。
交付如实区分文档/入口建立、宿主发现和行为验证，入口存在不等于已经生效。
```

相对路径核对示例：若项目实际使用 .agents/skills/project-demo-standards/SKILL.md，规范在 docs/engineering/PROJECT_STANDARDS.md，则从该技能目录到规范的路径为 ../../../docs/engineering/PROJECT_STANDARDS.md。这是特定目录深度的示例，实际目录不同须重新计算；已有 docs/team 规范时引用原位置，不照抄默认路径。
