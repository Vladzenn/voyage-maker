# Voyage Maker: shared desktop and cloud instructions

This is the active authoring repository for **The Schools of Magic, Arise!** The world is already developed and playable. The research-only objective in the original synced AGENTS.md is historical. Preserve that original file and every file under sources/ unchanged; this override supplies the current workflow.

## Start here

1. Read README.md, docs/CURRENT_STATE.md and docs/DECISIONS.md.
2. On the desktop run `python tools/project.py start` before a new editing task. It only fast-forwards a clean checkout; never reset or discard work to pull. In a cloud task, inspect the checked-out branch and latest commit instead.
3. `world-draft/WorldAlpha - World.json` is the canonical editable full world. WorldAlpha section JSON files are derived from it. A newly supplied Studio export becomes the merge base; preserve its images, coordinates, music, voices, order and user edits. Never rebuild from an old Alpha export or an ignored local candidate snapshot.
4. Treat sources/ as read-only reference material. Reference worlds are examples, not authority over our lore or current Studio validation.

## Research and authoring

- Use current official Voyage documentation/release notes and the community wiki for uncertain mechanics. Separate documented behavior, observed configuration and untested hypotheses. Never invent schema fields or platform capabilities.
- Consult research/Character Creation Format.md for NPC cards, research/Portrait Creation Format.md for portraits, and research/Location and Area Image Creation Guide.md for location art. Also consult the Population Creation Guide and Narrative Writing and Quest Craft Guide when relevant.
- NPC cards are native JSON by default. Do not recreate the retired NPC notes folder. Follow the existing card structure; no phantom sections. Public text must not contain save, trigger or generation instructions.
- Keep ordinary native quests, developing narrative arcs and exact event triggers distinct. One completion and reward owner per undertaking. Do not create a state machine for every conversation.
- Preserve the Spider Realm exactly unless the user explicitly requests a change to it. Ordinary difficulty safeguards must not override its surprise event, encounters or boss.
- Names, lore, spells, equipment and portraits must follow the approved setting and guides. Creativity belongs in specific people, conflicts, useful items and playable choices.
- Do not start planned expansions just because they are documented. Current planning scope is in docs/CURRENT_STATE.md.

## Validation and delivery

- Run `python tools/project.py sync`, `python tools/project.py validate`, and `node tools/test_item_mechanics.cjs` after relevant world changes. These work on Windows and Linux without third-party dependencies.
- Fix introduced size/reference errors. Checks include the 5,000-character quest-generation field; do not rely on old reports that omitted this field. Never claim live Studio validation or playtesting from local fixtures.
- Update docs/CURRENT_STATE.md and concise public Markdown patch notes for meaningful changes. If a change is only a snippet requested by the user, record whether it was actually applied to the canonical file.
- Hosted artwork URLs remain in the world. Existing large original media is represented in docs/asset-index.json and stays on the desktop. New or modified media is picked up by the publish command and shared; never bulk force-add all old media or archives.

## GitHub synchronization requested by the user

The user authorizes keeping completed project work synchronized with the private GitHub repository. At the end of a completed editing task on the desktop run `python tools/project.py publish -m "Concise description"`. This validates, synchronizes section files, checks new media and commits/pushes the completed work. Report a failed push honestly; do not say it is synced until it succeeds.

Cloud tasks work from the repository and return committed changes through the platform's branch/PR workflow, or use publish when authenticated Git pushing is available. Never force-push or overwrite remote work. When cloud work is merged, the next desktop task pulls it before editing. Avoid simultaneous edits to the full world from desktop and web; merge carefully when necessary.

The GitHub repository stores project files, decisions and history, not the full private Codex conversation or credentials. Do not export chat databases, authentication files or unrelated projects. Remain candid about whether Codex Cloud itself has been configured and verified.
