# Launch copy: Agent Workflow Skills 1.3.0

Repository: [suntianhu/agent-workflow-skills](https://github.com/suntianhu/agent-workflow-skills)

Use the version announcement after that version is available. While it is local or under review, say “Preparing 1.3.0” and link the accessible source or PR.

## Short description

Composable skills for coding agents: understand the project, follow its conventions, choose proportionate validation, and deliver evidence.

## Community post

### Title

I organized my AI coding workflow into 24 composable skills

### Body

When a coding agent works on an existing project, I want it to understand the code and conventions before making changes. When it reports success, I want to know what it actually verified.

I built **Agent Workflow Skills** around those requirements. Version **1.3.0** keeps **24 skills and eight compositions** for project review, requirements, frontend/backend work, debugging, contracts, review and delivery.

The collection distinguishes existing projects from new ones. Existing project skills and agent/plugin rules are inventoried; later skill adoption reconnects to the same project standards, stack and validation decisions. Validation scope, TDD order and test retention are separate decisions. Small changes keep a bounded workflow, and each completion claim should match its evidence.

This update adds conditional references for security finding verification, PostgreSQL data access and isolation, browser interaction checks, and design systems. They are integrated into the existing responsibilities rather than added as another mandatory workflow. The source ledger covers selected material from nine upstream repositories, with pinned commits, file hashes, reading scope and adoption decisions. It is not a full-repository audit or an endorsement by those maintainers.

The project includes export and validation utilities, offline examples, and native discovery probes. Windows discovery checks for all 24 skills in Codex and Claude were recorded for 1.2.0; discovery does not demonstrate successful model-driven application work. Scenario checks are not a cross-model effectiveness benchmark. The project makes no fixed productivity or universal compatibility claim.

READMEs are available in six languages. Skill bodies and detailed guides are currently Chinese. Original material is MIT-licensed; upstream licenses remain separate, and no upstream skill bodies, implementations, design datasets or assets are bundled.

If you try it, feedback on one concrete task is especially useful: what triggered, what helped, which rules conflicted, and what evidence was missing.

Source: https://github.com/suntianhu/agent-workflow-skills

## Social post

Agent Workflow Skills: 24 composable skills and eight workflows for coding agents. Version 1.3.0 integrates conditional security, PostgreSQL, browser validation and design references. Includes pinned sources and validation tools. Feedback from real tasks welcome.

https://github.com/suntianhu/agent-workflow-skills

## DEV preparation

Use the community post with a real worked example and a descriptive image only when available. Distinguish executed results from prompt recipes, disclose agent-assisted drafting, and follow the community's current posting rules. This file is a local draft; it does not create or publish an article.
