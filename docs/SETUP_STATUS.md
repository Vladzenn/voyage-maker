# Shared workspace setup

Verified 1 November 2026:

- Private GitHub repository: https://github.com/Vladzenn/voyage-maker
- Desktop checkout: the existing project folder, also accessible through R:\VoyageMaker.
- Default branch: main. Origin uses HTTPS and the existing Git credential helper; no credential is stored in repository files.
- Current world, 23 derived section files, guides, reference JSON, decisions and planning are committed.
- GitHub Actions passed the initial Linux run: 6,267 structural checks, consistent section exports, 1,209 mechanics assertions and compilation of 164 trigger scripts.
- These checks are local/CI fixtures, not a live Voyage playtest.
- 334 existing original media assets are indexed and retained locally. Hosted image and music URLs remain in the shared world. New and changed media is shared by the publish helper.
- No local files or conversations were deleted.

## One-time account connection

The repository is ready. Codex Cloud has not yet been verified: the environment-list tool returned no saved environments. The local browser automation could not start because of a Windows sandbox initialization error. Account-side setup therefore needs the user to select the repository in Codex web.

Open https://chatgpt.com/codex, select Cloud, create an environment, and select Vladzenn/voyage-maker. Connect GitHub if requested, granting access to this private repository. Let Codex inspect the project, review setup, and publish the environment.

Use Python 3.12+ and Node.js 22+. The repo needs no third-party packages, project secrets or API keys. Its optional setup/check script is:

```sh
bash tools/cloud_setup.sh
```

If the environment asks what to prepare, use:

```text
Prepare this Voyage world authoring repository. Read AGENTS.override.md and README.md.
Provide Python 3.12+ and Node.js 22+. No dependency installation or secrets are needed.
Run bash tools/cloud_setup.sh. Preserve sources/ and the original AGENTS.md.
Do not change world content as part of environment setup.
```

Once published, a normal task can begin with:

```text
Continue Voyage Maker from this repository. Read AGENTS.override.md,
docs/CURRENT_STATE.md and docs/DECISIONS.md before editing. Use the canonical
world-draft/WorldAlpha - World.json and validate before publishing changes.
```

Cloud changes must be committed/published and merged into main to arrive through the normal desktop fast-forward. Unpublished cloud edits are not visible in the desktop checkout. Independent chats do not share live conversation memory.

This setup does not change Voyage Studio automatically. Import the resulting full world JSON as before.
