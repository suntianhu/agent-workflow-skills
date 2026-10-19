# Publish this collection on GitHub

Publish the contents of the `agent-workflow-skills` source directory as the repository root. Keep the release ZIP and its SHA-256 file outside Git history and attach them to a release. This guide does not execute any remote action.

## 1. Create an empty repository

On GitHub, create a repository named `agent-workflow-skills`. Select Public if you intend to open-source it. Do not initialize another README, license, or gitignore; the source directory already contains them.

Suggested About text:

> Composable workflows for coding agents: project review, design, implementation, and evidence-based delivery.

Suggested topics: `agent-skills`, `coding-agents`, `developer-tools`, `ai-workflows`, `codex`, `claude-code`, `gemini-cli`, `github-copilot`. Topics describe integration targets; the README must retain the actual validation limits.

## 2. Commit and push the source

Open a terminal in the source directory, not its parent. Run commands in order and stop if a command fails:

```sh
python scripts/validate.py
git init -b main
git add .
git status --short
git commit -m "Release v1.1.2"
git remote add origin https://github.com/YOUR_USERNAME/agent-workflow-skills.git
git remote -v
git push -u origin main
```

Replace `YOUR_USERNAME` with the owner of the empty repository. If Git asks for an author identity, configure the intended name and email for this repository; use your GitHub-provided privacy email if desired. Authenticate through the supported Git credential flow. Existing Git repositories should inspect their branch and remotes rather than blindly repeat initialization or `remote add`.

The first upload should have `README.md`, all five `README.*.md` translations, `.github/`, `skills/`, `bundles/`, and the remaining source files at the repository root. Do not upload the parent folder or only a ZIP. Committing with Git preserves hidden files such as the workflow directory.

## 3. Inspect the repository

Check that English is the default README, all six language links open correctly, and both issue templates and the pull-request template are available from the default branch. Inspect the Actions run; the local distribution does not claim that remote CI has passed. GitHub settings may require you to enable or approve workflow execution.

## 4. Create release v1.1.2

Open Releases → Draft a new release. Create tag `v1.1.2` targeting the uploaded `main` commit. Use `v1.1.2 — Multilingual project overview` as the title, copy [the release notes](release-notes.md), and attach:

```text
agent-workflow-skills-1.1.2.zip
agent-workflow-skills-1.1.2.zip.sha256
```

Attach both assets before publishing, particularly if immutable releases are enabled. Check that the uploaded ZIP corresponds to the tagged source. If you change source files after packaging, regenerate the archive and its checksum before attaching them; do not use the earlier checksum with a modified ZIP.

GitHub's automatically generated source archive has different bytes from this prepared release ZIP, so the supplied checksum applies only to the named attached ZIP. Review the draft and publish when ready.

## Primary documentation

- [Add locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Manage releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [Issue and pull-request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
