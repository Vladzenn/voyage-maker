# Voyage Maker — The Schools of Magic, Arise!

Private shared workspace for authoring a Voyage world from Codex desktop and Codex web/cloud.

Repository: [Vladzenn/voyage-maker](https://github.com/Vladzenn/voyage-maker) (private).

## Current project

- **Ardelis capital:** [public notes](world-draft/Ardelis%20-%20Patch%20Notes.md), [mechanics and live checklist](world-draft/Ardelis%20-%20Development%20Notes.md), [map placement handoff](world-draft/Ardelis%20-%20Map%20and%20Landmark%20Handoff.md). Delivery status is recorded in CURRENT_STATE.
- **Glowhaven fresh map brief:** [standalone PDF](world-draft/authoring/plans/Glowhaven%20-%20Fresh%20Map%20Brief.pdf), [editable text](world-draft/authoring/plans/Glowhaven%20-%20Fresh%20Map%20Brief.md), [exact position index](world-draft/authoring/plans/Glowhaven%20-%20Fresh%20Map%20Positions.csv); no old map artwork is supplied.
- **Schools of magic, Rebirth!:** [public notes](world-draft/Schools%20of%20magic%2C%20Rebirth!%20-%20Patch%20Notes.md), [implementation, limits and live tests](world-draft/Schools%20of%20magic%2C%20Rebirth!%20-%20Development%20Notes.md)
- **Fishing patch:** [public notes](world-draft/Fishing%20-%20Patch%20Notes.md), [mechanics, limits and live tests](world-draft/Fishing%20-%20Mechanics%20and%20Playtest.md)
- **Canonical world:** [world-draft/WorldAlpha - World.json](world-draft/WorldAlpha%20-%20World.json)
- **Glowhaven Expanded:** [public notes](world-draft/Glowhaven%20Expanded%20-%20Patch%20Notes.md), [mechanics, map migration and live tests](world-draft/Glowhaven%20Expanded%20-%20Development%20Notes.md)
- **Current state and next work:** [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)
- **Champions of the Crucible:** [public notes](world-draft/Champions%20of%20the%20Crucible%20-%20Patch%20Notes.md), [current bracket mechanics](world-draft/Crucible%20Bracket%20-%20Mechanics.md)
- **Beginner contracts and fieldwork:** [scope, references and playtest checklist](research/Beginner%20Contracts%20and%20Fieldwork%20-%202026-11-02.md), bundled with the unreleased Crucible announcement
- **Wider Earth lore:** [implemented scope and review](research/Wider%20Earth%20Lore%20-%20Implementation%202026-11-02.md), merged with the latest Studio export
- **Steel and Spirits — Akitsuhara implemented:** [public notes](world-draft/Steel%20and%20Spirits%20-%20Patch%20Notes.md), [scope, mechanics and live tests](world-draft/Portal%20to%20Akitsuhara%20-%20Development%20Notes.md), [placed-map and complete-portrait follow-up](world-draft/Akitsuhara%20-%20Placement%20and%20Portrait%20Follow-up.md); the earlier [4×3 map plan](world-draft/authoring/plans/Portal%20to%20the%20Oni%20Nation%20-%20Research%20and%20Map%20Plan.md) is historical planning.
- **Official portrait uploads:** [safe batch workflow](docs/PORTRAIT_UPLOADS.md)
- **Academy and guild area artwork:** [public notes](world-draft/Academy%20and%20Guild%20Artwork%20-%20Patch%20Notes.md), [exact upload receipts](tools/location-art/academy-area-upload-receipts-2026-11-02.json)
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
python tools/test_validation.py
python tools/test_voyage_portraits.py
node tools/test_item_mechanics.cjs
node tools/test_fieldwork.cjs
node tools/test_adventurers.cjs
node tools/test_creation.cjs
node tools/test_crucible.cjs
node tools/test_oni.cjs
node tools/test_glowhaven_expansion.cjs
node tools/test_fishing.cjs
node tools/test_rebirth.cjs
node tools/test_ardelis.cjs
node tools/test_ardelis_followup.cjs
python tools/project.py publish -m "Describe the completed change"
```

Use `python3` on a system where `python` is unavailable. `start` fetches and fast-forwards only a clean checkout. `publish` validates and pushes completed changes; it does not watch half-written files or silently resolve conflicts. A cloud task without push credentials can still commit its work and use Codex's native review/PR workflow.

GitHub Actions repeats the portable checks on pushes and pull requests. Local checks verify structure and selected mechanics; important outcomes still need a Voyage playtest.

Setup status and the one-time Cloud connection: [docs/SETUP_STATUS.md](docs/SETUP_STATUS.md).

## Working from either surface

The private GitHub repository is the common project history. Desktop work pushes when complete; cloud work uses the latest repository revision and publishes its branch or pull request. Merge cloud work before continuing the same files locally. Chat context is carried through the state and decision documents, not an assumed shared memory between independent chats.

This repo contains the active world, current section exports, writing guides, plans, reference JSON and portable tools. Roughly a gigabyte of existing original media and large duplicate archives remain on the desktop; their hosted URLs and asset index preserve discoverability. New or changed generated media is shared selectively by the publish command. No local file was deleted during setup.

To import the world into Voyage, use the canonical full JSON. Section files are supplied for deliberate section replacement and are synchronized from the full world.
