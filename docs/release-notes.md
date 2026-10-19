# v1.1.2 — Multilingual project overview

Agent Workflow Skills provides 24 focused skills and eight documented development compositions. This release adds complete README translations in Traditional Chinese, Japanese, Korean, and Russian alongside English and Simplified Chinese.

## Changes

- Add four full README translations with the same workflow gates, skill list, commands, compatibility status, validation limits, and license boundaries.
- Connect all six READMEs through a shared language selector; keep English as the default overview.
- Update contribution guidance, release instructions, and version metadata for the six-language overview.
- Fix Windows/Linux checkout validation by enforcing LF text, rebuilding generated hashes, and allowing the repository attributes file.

## Validation and limits

Local validation checks all README links and generated source consistency. Translation checks cover version numbers, skill identifiers, workflow references, commands, language navigation, and the scope of translated material. These are documentation checks, not native-agent or product tests.

Skill bodies, detailed guides, and utility messages remain in Simplified Chinese. The 24 skill responsibilities and eight compositions are preserved. The validator additionally recognizes `.gitattributes`; generated content and hashes now use stable LF text. Native discovery and end-to-end agent usage remain untested; remote CI status must be checked on the hosting repository. No human native-speaker review has been performed for the new translations.

The attached SHA-256 file applies only to the named prepared ZIP, not GitHub's automatically generated source archives. Nothing is installed automatically and no default agent settings are changed.
