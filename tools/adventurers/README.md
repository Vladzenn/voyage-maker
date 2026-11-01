# Adventurers of Glowhaven authoring pass

The canonical full world remains `world-draft/WorldAlpha - World.json`. These tables and scripts document the implementation of Update 4, not a second live world or a reason to recreate NPC notes.

- `cast.py`: sixteen original character designs and deterministic recorded affinity/pose draws.
- `content.py`: three native arc records, sixteen finite native quests and six creature types.
- `housing.py`: six quoted room/property arrangements and natural key/deed identities.
- JavaScript files: actual portable trigger-script sources. They use documented `check`, `storage` and typed effects only.
- `polish.py`: targeted combat, generation, item and quest guidance, cast anchors and reciprocal relationships.
- `portrait-briefs.json`: final prompts, prominence and recorded choices. Each portrait received one built-in image-generation pass.
- `manifest.json`: released changes and preservation fingerprints.

`prepare.py`/`build.py` are release-authoring helpers. The build reads `tmp/adventurers/baseline.json`, a cached copy of the user-current Studio export with nineteen new item images. This cache is deliberately excluded from Git. They are not daily synchronization commands and should not be run against the already-updated world. The initial text baseline is preserved in Git commit `d780acf`; the user's subsequent image changes are retained in the canonical world and preservation manifest.

For ordinary later editing, use the portable commands in the root README. `node tools/test_adventurers.cjs` exercises schedules, current offers, public-lead pacing, equipment policies and the repair command. `python tools/adventurers/validate.py` is this release's preservation audit, not a blanket ban on future intentional changes to images, quests or maps. Update its baseline intentionally when a later approved release changes those records.

Fixtures supply semantic answers and state reads explicitly. They do not reproduce Voyage's runtime ordering or language-model judgment. Test the live scenarios listed in the development notes after importing the world.

`python tools/adventurers/export.py` packages the **current canonical** world, the sixteen supplied portraits, new cards and a separate native Solo Ironman variant. It works in a fresh checkout and does not need the excluded baseline/candidate cache. `--candidate PATH` is an explicit one-time installation option for a separately validated candidate; it is not used by normal synchronization. Large duplicate release packages remain local outputs; the canonical JSON, source data, tools and sixteen new PNGs are shared through Git.
