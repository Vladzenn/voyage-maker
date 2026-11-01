# Voyage Maker — The Schools of Magic, Arise!

Private shared workspace for authoring a Voyage world from Codex desktop and Codex web/cloud.

Repository: [Vladzenn/voyage-maker](https://github.com/Vladzenn/voyage-maker) (private).

## Current project

- **Canonical world:** [world-draft/WorldAlpha - World.json](world-draft/WorldAlpha%20-%20World.json)
- **Current state and next work:** [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)
- **Latest minor patch:** [public notes](world-draft/Phantom%20Patch%20-%20Patch%20Notes.md), [creation review guide](world-draft/Phantom%20Patch%20-%20Creation%20Guide.md) and [development notes](world-draft/Phantom%20Patch%20-%20Development%20Notes.md)
- **Approved decisions:** [docs/DECISIONS.md](docs/DECISIONS.md)
- **Adventurers update:** [release notes](world-draft/Adventurers%20of%20Glowhaven%20-%20Patch%20Notes.md) and [implementation/playtest guide](world-draft/Adventurers%20of%20Glowhaven%20-%20Development%20Notes.md)
- **Shared workflow:** [docs/DESKTOP_AND_CLOUD.md](docs/DESKTOP_AND_CLOUD.md)

Read AGENTS.override.md before editing. The original AGENTS.md and sources/ are preserved references.

## Commands

Python 3.10+ and Node.js 20+ are sufficient. No package install or API key is needed.

```sh
python tools/project.py start
python tools/project.py sync
python tools/project.py validate
node tools/test_item_mechanics.cjs
node tools/test_adventurers.cjs
node tools/test_creation.cjs
python tools/project.py publish -m "Describe the completed change"
```

Use `python3` on a system where `python` is unavailable. `start` fetches and fast-forwards only a clean checkout. `publish` validates and pushes completed changes; it does not watch half-written files or silently resolve conflicts. A cloud task without push credentials can still commit its work and use Codex's native review/PR workflow.

GitHub Actions repeats the portable checks on pushes and pull requests. Local checks verify structure and selected mechanics; important outcomes still need a Voyage playtest.

Setup status and the one-time Cloud connection: [docs/SETUP_STATUS.md](docs/SETUP_STATUS.md).

## Working from either surface

The private GitHub repository is the common project history. Desktop work pushes when complete; cloud work uses the latest repository revision and publishes its branch or pull request. Merge cloud work before continuing the same files locally. Chat context is carried through the state and decision documents, not an assumed shared memory between independent chats.

This repo contains the active world, current section exports, writing guides, plans, reference JSON and portable tools. Roughly a gigabyte of existing original media and large duplicate archives remain on the desktop; their hosted URLs and asset index preserve discoverability. New or changed generated media is shared selectively by the publish command. No local file was deleted during setup.

To import the world into Voyage, use the canonical full JSON. Section files are supplied for deliberate section replacement and are synchronized from the full world.
