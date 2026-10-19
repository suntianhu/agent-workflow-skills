# 全仓清单与阅读记录工具

从本技能目录通过Python 3.10+运行；不联网、不执行产品、不安装。显式输出路径是唯一写入位置，内容不含源码或凭据。不要发布运行后生成的真实项目清单或阅读台账，它们是项目内部资料。

```text
python scripts/repo_audit.py scan --root /path/to/project --out /path/to/project/docs/engineering/inventory-001.json --ledger /path/to/project/docs/engineering/reading-ledger.json
python scripts/repo_audit.py check --inventory /path/to/project/docs/engineering/inventory-001.json --ledger /path/to/project/docs/engineering/reading-ledger.json
```

Windows使用实际绝对路径。scan不覆盖已有快照，新一轮用新文件名。隐藏与未跟踪文件会清点；默认仅排除版本库元数据、常见依赖与缓存。构建产物要用 `--exclude relative/directory=已核对的生成命令或依据` 明确排除，不能靠目录名猜测。

项目的 Skills、AGENTS/CLAUDE 等规则与插件配置同属清点材料；不要把隐藏技能目录作为缓存排除。清单不会自动解析配置中的外部技能引用，也不能判断宿主是否启用，须从实际配置人工追踪并在项目规范登记。新技能或规则文件加入会使旧快照失效；核对变化并更新清单/阅读记录与同一规范。

逐项阅读后在台账的files数组添加对应记录：path、status、summary、evidence、fingerprint。普通文件status为reviewed，fingerprint为清单sha256；敏感配置仅核对必要键/加载方式，fingerprint取mtime_ns的字符串，不读取/输出值。排除目录status为excluded，fingerprint为字符串excluded，summary/evidence需说明核对依据。

summary写实际职责、关键约束和关系，evidence给文件/章节/符号或明确排除依据；不能批量复制通用句子把所有文件标已读。图片等资产核对用途与引用，不要求像源码一样逐字读二进制。检查器能检出缺项、过期指纹、增加/删除/修改和阻断项，不能证明真正理解。

规范文档写入后也属于当前项目，必要时重新扫描并阅读它以形成最终基线；清单与台账自身被排除以避免自引用。预存其他快照应按生成资料明确排除或核对，不静默扩大排除范围。链接、联接、不可访问文件保持阻断；确认的外部子模块需另行在授权范围读取并汇总证据。

这里的工具阻断指清单覆盖范围内的不可读/重定向条目，不能把未解决项填成已读通过。配置提到但不属于自有代码范围的外部第三方技能，另在规范中登记可访问性与适用范围；有证据证明与本次任务无关时，不因其正文未加载就全局停工，影响当前门禁的关键未知仍须补证。
