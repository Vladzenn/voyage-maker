# Desktop and cloud workflow

The GitHub repository is the shared source of truth for project files and history. Independent desktop and web chats do not inherit this entire conversation automatically; read CURRENT_STATE.md and DECISIONS.md.

## Desktop

Before a new task, `python tools/project.py start` fetches and fast-forwards a clean checkout. If there is local work or diverging history, it stops rather than overwriting anything. Finish a completed edit with:

```sh
python tools/project.py publish -m "Describe the completed change"
```

This synchronizes derived section files, validates the current world, runs mechanics checks, adds project changes and eligible new media, commits, and pushes the current branch. It reports failure instead of force-pushing. It does not run a background watcher or commit unfinished edits on every keystroke.

## Codex web / Cloud

Connect the private repository in Codex Cloud, create/publish an environment using Python and Node, and open tasks against that repository. `tools/cloud_setup.sh` contains the checks and requires no downloads. Start a task by reading AGENTS.override.md and the two state documents.

Cloud task workspaces are separate checkouts. Review and publish their changes through the platform's branch/PR controls. If normal authenticated Git pushing is available, the publish command also works there. Merge the cloud branch before the next desktop task pulls. Editing the canonical world from two tasks simultaneously can require a real JSON merge; never resolve it by blindly selecting the older full file.

## Media

The current world retains hosted portraits, location images, maps and music URLs. Existing original media and old ZIP exports stay on the desktop, with relative paths and hashes in asset-index.json. They are not silently deleted or uploaded in bulk. A cloud task can use the hosted URLs where accessible or request a particular original when needed.

The publish command compares present image/audio/PDF assets with that initial index. New and changed assets under the established media folders are explicitly added and then included in Git. Unchanged legacy originals remain local; their absence in a cloud checkout is not treated as deletion. Files above 95 MiB require a deliberate external-storage plan instead of an accidental large push.

## What is not synchronized

Authentication files, Codex session databases and chats, unrelated projects, temporary caches, old backup exports and redundant ZIP files remain local. GitHub changes reach Voyage only when the resulting world JSON is imported there; Git is not a live Voyage Studio connection.
