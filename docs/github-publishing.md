# GitHub publishing and maintenance

Publish source at the repository root. Keep generated ZIPs and checksums outside Git history. A pull request (PR) proposes a change for review and merging. `main` is the validated baseline; a tag identifies a fixed version, and a release adds notes and assets.

## Change and merge

From a clean, synchronized clone:

```sh
git switch main
git pull --ff-only
git switch -c codex/describe-the-change
```

Make the change. For a release update `catalog.json`, all six READMEs, `CHANGELOG.md`, and [release notes](release-notes.md). Regenerate when catalog, guides, or bundled resources change:

```sh
python scripts/build_catalog.py
python scripts/validate.py
python scripts/run_examples.py
git add .
git diff --cached
git commit -m "Describe the resulting behavior"
git push -u origin codex/describe-the-change
```

Open a PR into `main`, inspect the diff, and wait for both `validate (ubuntu-latest)` and `validate (windows-latest)`. CI also executes offline examples and a packaging dry run. Resolve conversations and update the branch if required. Squash-merge, then delete the merged feature branch; this preserves merged source and tags.

External contributors normally fork the repository and open a PR from a branch in their fork. Write-access collaborators can branch here. Another permanent `develop` branch is unnecessary.

## Protect main

In Settings → Branches or Rules → Rulesets, target `main` and require:

- A PR before merging, with conversations resolved.
- Both exact CI checks above, with the branch up to date.
- Enforcement for administrators; no force pushes or deletion.

A solo maintainer can require PRs with **zero required approvals**; authors cannot approve their own PRs. Increase this to one when another active maintainer can review. Fork PR workflows retain read-only permissions and receive no release token. Review workflow changes before merging.

## Publish by tag

After the version PR merges and CI passes, synchronize `main` and create a new annotated tag:

```sh
git switch main
git pull --ff-only
python scripts/validate.py
git tag -a v1.3.1 -m "Release v1.3.1"
git push origin v1.3.1
```

Do not repeat these tag commands if the tag already exists. For future releases, change the source version and notes through a PR, then use the new tag. Never move a published tag to fix an asset.

The [release workflow](../.github/workflows/release.yml) performs:

1. Source validation and offline examples on Windows and Linux.
2. Verification that the tag commit is reachable from `origin/main` and the stable `vX.Y.Z` tag exactly matches the catalog and release-notes heading.
3. Reproducible packaging of clean tracked source, excluding Git metadata, untracked files and redirected entries.
4. Archive integrity and SHA-256 checks, then publication with notes, ZIP and checksum.

Build jobs have `contents: read`. Only the separate publication job has `contents: write`; it verifies the transferred checksum and executes no repository scripts. Actions are pinned to full commits. Enable repository Actions and permission to create releases using `GITHUB_TOKEN`; no personal access token secret is required.

Watch Actions → Release, then inspect Releases. Failed validation never publishes. Reruns do not overwrite existing releases. If no release was created, inspect the failure and rerun failed jobs after resolving it. If a published asset is wrong, issue a new patch version.

## Local packaging and checksum

From a clean committed tree, select a new output directory outside source and agent configuration trees:

```sh
python scripts/build_release.py --tag v1.3.1 --out ../release-v1.3.1
```

This prepares the ZIP, `.zip.sha256`, and release notes. It does not publish, create a tag, or install skills. It checks the proposed version; tag existence and ancestry are enforced by the workflow. Identical tracked bytes produce identical ZIP bytes. Fixed stored ZIP entries trade compression size for reproducibility.

The sidecar applies only to the named prepared ZIP, not GitHub's source archives. On Windows compare `(Get-FileHash <ZIP> -Algorithm SHA256).Hash` with its first field. Where available, run `sha256sum --check <ZIP>.sha256`.

## Initial upload only

For a new independent repository, create an empty GitHub repository and upload this source as its root, including `.github`, `.gitattributes`, and all READMEs. Inspect existing Git state before initialization or `remote add`. Suggested topics: `agent-skills`, `coding-agents`, `developer-tools`, `codex`, `claude-code`. These are integration targets, not adoption claims.

## Primary documentation

- [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [Workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub CLI release creation](https://cli.github.com/manual/gh_release_create)
