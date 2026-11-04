# Voyage Maker feature implementation guide

Use this handoff to continue *The Schools of Magic, Arise!* from a new Codex chat. The shared repository is [Vladzenn/voyage-maker](https://github.com/Vladzenn/voyage-maker), with `main` as the integration branch. Git carries the world, decisions, guides and reviewed changes between accounts. For decisions still in a chat, carry forward a short task brief and any needed Studio export or art references.

## Connect Codex Cloud

1. Open [Codex](https://chatgpt.com/codex) while signed in to the second ChatGPT account. A separate browser profile makes it easy to see which ChatGPT and GitHub accounts are active.
2. For GitHub, first try signing in as `Vladzenn` when Codex asks to connect. If you want a separate GitHub identity, sign in to GitHub as `Vladzenn`, open the repository’s **Settings → Collaborators → Add people**, invite the other GitHub username, then accept from that identity. Verify it can open the private repository. [GitHub collaborator setup](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)
3. In Codex choose **Work in → Cloud → Select environment → Create environment**, connect GitHub if prompted and select `Vladzenn/voyage-maker`. If the repository is missing, verify the linked GitHub identity and check that the repo owner’s GitHub App installation includes `voyage-maker`. [OpenAI Cloud setup](https://learn.chatgpt.com/docs/environments/cloud-environments) · [GitHub App access settings](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps)
4. Choose **Get started** and review the setup. Use Python 3.12 and Node.js 22. The repo’s `bash tools/cloud_setup.sh` runs the baseline checks without package downloads or project credentials. Set access to **Only me**, then publish the environment and start a task in it. This makes the environment available to Codex. Voyage Studio import and publication are separate release steps. [OpenAI Cloud setup](https://learn.chatgpt.com/docs/environments/cloud-environments)

Copy this into the first Cloud task to verify that the handoff works:

```text
Continue Voyage Maker in Vladzenn/voyage-maker. This is a read-only setup check.
Read AGENTS.override.md, README.md, docs/CURRENT_STATE.md, docs/DECISIONS.md,
and docs/FEATURE_IMPLEMENTATION.md. Report the branch or detached checkout and
commit SHA, confirm the canonical world file is present, and run
bash tools/cloud_setup.sh. Summarize the active feature and any unresolved
decisions. Leave files and Voyage Studio untouched.
```

## Implement a feature

1. **Confirm scope and base.** Read [AGENTS.override.md](../AGENTS.override.md), [README.md](../README.md), [CURRENT_STATE.md](CURRENT_STATE.md), and [DECISIONS.md](DECISIONS.md). Check the branch, SHA and working tree. On desktop run `python tools/project.py start` before editing. A fresh Studio export supplied by the author takes precedence as the world merge base. Preserve the author's images, coordinates, music, voices and ordering. If current work is marked as planning, deliver a proposal until the author asks for implementation.
2. **Trace the existing feature before adding another mechanism.** Locate the actual records, the player action that starts the flow, and the owner of each completion, reward or state change. Use native quests for undertakings with objectives, arcs for developing stories, and exact triggers for events that require authoritative state. Put mechanical rules in supported fields and behavioral guidance. Keep player-facing descriptions in-world. For uncertain mechanics, check current Voyage documentation, then inspect this world and [the technical guide](../research/Voyage%20Technical%20Guide.md). Treat `sources/` as read-only examples.
3. **Edit the canonical JSON.** Work in [`world-draft/WorldAlpha - World.json`](../world-draft/WorldAlpha%20-%20World.json), then generate the section exports. Reuse existing patterns and keep the diff scoped. Preserve the Spider Realm unless the task explicitly changes it. Use the linked authoring guides in the README and repository instructions for any new NPC, quest, portrait or location. Give a dedicated handoff for any needed desktop-only art or authorized upload.
4. **Test the player's actual paths.** For a progression event, check the intended action, a similar action that should do nothing, repeat attempts, and returning after interruption. Include pre-existing save state or multiplayer only where it can change the result. For example, a trophy-triggered encounter should distinguish carrying the exact trophy in the required place from merely mentioning it or carrying it somewhere else. Keep the fixture results separate from checks still needed in Voyage Studio.
5. **Review and deliver.** For world changes, run the commands below and the relevant feature checks listed in the README. Inspect the diff, including generated section changes, and write concise public notes for meaningful player-facing changes. Update `docs/CURRENT_STATE.md` with the status and remaining live tests. State which JSON to import and which cases still need a live test.

```sh
python tools/project.py sync
python tools/project.py validate
python tools/test_validation.py
node tools/test_item_mechanics.cjs
python tools/project.py sync --check
git diff --check
```

## Hand off between accounts

Assign one account at a time to edit the full world. The other can review, research, draft content separately or test the same revision. For Cloud implementation, publish the changes on a feature branch or PR, review the diff, then merge to `main`. The next desktop session can fast-forward from there. A running Cloud task has its own working state, so check its starting SHA before resuming. Use the desktop publish command only after checking what it will stage, since it collects worktree changes and eligible media. [Desktop and Cloud workflow](DESKTOP_AND_CLOUD.md)

Paste this when assigning a specific feature:

```text
Implement [feature] for The Schools of Magic, Arise!
Base: [main SHA or attached Studio export, with any later Studio edits noted].
Player goal: [what the player can do and what they should see].
Acceptance cases: [normal path, denied path, repeat or interruption if relevant].
Preserve: [systems, content, art or balance that constrain this change].
Decisions from the previous chat: [approved choices and open questions].
Read docs/FEATURE_IMPLEMENTATION.md. Keep changes scoped to this feature.
Deliver a reviewable branch or PR with validation results, the import file,
and the manual Voyage playtest checklist. Stop at the reviewed Git changes.
```
