# Third-party notices

This collection contains newly written workflow instructions and utility code.
Upstream skill bodies, implementation scripts, assets, and databases are not redistributed.
References are pinned in provenance/upstreams.json; individual upstream license scope remains separate.

- obra/superpowers: retrieved MIT license, copyright Jesse Vincent. Principles of evidence-led debugging, bounded review and requirements brainstorming were studied and rewritten.
- github/awesome-copilot: retrieved MIT license, copyright GitHub. Skill granularity and contribution boundaries were studied.
- anthropics/skills: mixed license repository; the exact license of every studied skill was not established. No implementation is copied.
- openai/skills: deprecated snapshot, per-skill license scope; historical structure only. Current examples point to openai/plugins.
- vercel-labs/agent-skills: the studied React skill declares MIT; other files have separate or unconfirmed scope. Framework-specific rules are not copied into a universal rule database.
- trailofbits/skills: retrieved root CC-BY-SA-4.0 license at the pinned commit. Abstract ideas about evidence and security analysis were studied. No upstream prose, translations, report templates, code, agents or assets are included. The original wording and organization here do not purport to relicense Trail of Bits material; any future reuse of its protected expression must retain the applicable attribution and share-alike terms.
- supabase/agent-skills: retrieved MIT license, copyright (c) 2026 Supabase. Selected PostgreSQL rules were studied; SQL examples, rule bodies and implementation are not redistributed. Generalizations about indexes, pooling and performance were checked against official documentation before writing independent guidance.
- microsoft/playwright-cli: retrieved Apache License 2.0. Selected interaction, session and evidence capabilities were studied; no CLI implementation, generated tests or reference manual is included. This collection does not install Playwright.
- nextlevelbuilder/ui-ux-pro-max-skill: retrieved MIT license, copyright (c) 2024 Next Level Builder. Selected design guidance was studied; datasets, templates, scripts, fonts, icons and assets are not redistributed.
- pbakaus/impeccable: retrieved Apache License 2.0, copyright 2025 Paul Bakaus, and root NOTICE.md. Selected existing-design extraction and adaptation principles were studied; no command infrastructure, formats, skill prose, code or assets are included. Its notice attributes the unselected iOS/Android reference bodies to ehmo/platform-design-skills under MIT; those bodies are not redistributed here.
- wshobson/agents: retrieved MIT license, copyright (c) 2024 Seth Hobson. Selected design-system, iOS, Android and interaction skill methods were studied; no examples, component implementations or skill bodies are redistributed.

Public platform and design-system websites are research references, not bundled content or assets. Actual text access and gaps are listed in provenance/design-references.json. A reference link does not establish asset licensing or application accessibility.

Unreleased migration research (2026-10-21), pinned in provenance/upstreams.json and scoped in provenance/migration-references.json:

- addyosmani/agent-skills: selected deprecation-and-migration skill and root MIT license retrieved, copyright (c) 2025 Addy Osmani. Consumer compatibility and retirement concepts were studied; its prose, code and templates are not redistributed.
- magnus919/agent-skills: selected migration-engineering skill declares MIT in frontmatter; root LICENSE returned HTTP 404, so repository-wide license scope is not established. Cross-system reconciliation and recovery limitations were studied as abstract methods; no upstream expression or assets are redistributed.
- rmyndharis/antigravity-skills: selected framework-migration-legacy-modernize skill and root MIT license retrieved, copyright (c) 2026 Yudhi Armyndharis. Dependency mapping and role separation were studied; full collection lineage was not audited. No upstream skill prose, translations, templates, code or agent configuration is included.

Microsoft Azure, AWS, Kubernetes, PostgreSQL and Prisma official text sections were used to check specific technical assumptions, not bundled as content or treated as permission to copy implementations. No commands from those external materials were executed and no service deployment was performed during that research.

The MIT license at this repository root applies to this repository's original material, not external repositories or linked services. Do not copy third-party code or assets based solely on this notices file.

Further unreleased workflow adoption from the same pinned addyosmani/agent-skills commit studies the README, ten selected lifecycle skills and three evaluation files, with per-file reading scope in provenance/upstreams.json. Original requirements/task/quality/evidence guidance and the new performance/observability workflows were independently written; upstream prose, translations, templates, scripts, fixtures and default configurations are not redistributed. Official OpenTelemetry, Prometheus and web.dev text sections were checked for narrow technical assumptions, recorded in provenance/workflow-adoption.json; no SDK, benchmark, telemetry service or alert was executed. Its subjective interview confidence, lexical routing floor and reported model results are separate and are not evidence for this collection.
