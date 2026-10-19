# v1.2.0 — Reproducible releases and native discovery

Agent Workflow Skills provides 24 focused skills and eight documented development compositions, with six README languages.

## Changes

- Publish version tags through Windows/Linux validation, reproducible tracked-source packaging, and a separate release job with minimal permissions.
- Attach a prepared ZIP and SHA-256 checksum; reject stale versions, dirty trees, unsafe output paths, and nonregular Git entries.
- Add worked usage scenarios and executable offline examples for repository-reading gates, explicit time calibration, and byte-verified composition export.
- Add isolated native Codex/Claude discovery probes and sanitized evidence with before/after default-skill snapshots.
- Document PR maintenance, solo-maintainer branch protection, future releases, and exact compatibility limits across all six READMEs.

## Validation and limits

Codex CLI `0.163.0-alpha.10.2` and Claude Code `2.1.303` discovered all 24 skills in disposable Windows projects. Claude named discovery used the official Agent SDK `0.3.303`. Default skill trees were unchanged. This verifies discovery and metadata/command loading, not model decisions or full workflow execution. No credentials were copied; authenticated agent scenarios remain unverified.

CI validates source, executes offline synthetic examples, and dry-runs packaging on Windows and Linux. Native host probes are separate local checks. See the validation record and Actions result for the tagged commit. Skill bodies and guides remain Chinese; Gemini, Copilot, and other host versions remain untested.

The attached SHA-256 file applies only to the named prepared ZIP. Nothing is installed automatically and no default agent settings are changed.
