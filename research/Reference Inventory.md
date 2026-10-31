# Reference Inventory

**Checked:** 2026-10-25 (Asia/Shanghai)  
**Scope:** read-only inventory of every JSON under `sources/`, plus the attached frozen map reference.  
**Result:** six JSON files inspected. None was edited, moved, renamed, or deleted.

See [Reference Atlas](Reference%20Atlas.md) for comparative analysis and [Voyage Technical Guide](Voyage%20Technical%20Guide.md) for documented platform behavior and schema notes.

## JSON files

All six files parse as JSON with a case-sensitive JSON parser and report `heroesVersion: 37`. The record counts below are the number of keyed entries, except `premadeCharacters`, which is an array count. Sizes are the local mirror's file sizes; the project sync time is not evidence of the original export date.

| File | Size | Realms / regions / locations | NPCs | Story starts | Traits / categories | Abilities / skills | Quests / narrative events | Triggers | First-pass profile |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [ChikaraOld.json](../sources/ChikaraOld.json) | 5,276,567 B | 1 / 1 / 277 | 137 | 24 | 345 / 15 | 411 / 44 | 655 / 19 | 672 + 1 `questTriggers` entry | Dense one-region urban world; 18 resources, 102 world voices, 29 trigger scripts. |
| [DnD.json](../sources/DnD.json) | 3,419,108 B | 21 / 140 / 463 | 0 | 68 | 313 / 9 | 1,449 / 37 | 0 / 0 | 52 | Broad map and character-option catalog; no authored NPC or quest catalog. |
| [Konosuba.json](../sources/Konosuba.json) | 4,324,821 B | 1 / 16 / 51 | 276 | 51 | 546 / 21 | 896 / 66 | 89 / 12 | 191 + 37 `questTriggers` entries | Many character starts and authored quests; two resources; 30 premade characters. |
| [Larion.json](../sources/Larion.json) | 10,101,757 B | 3 / 49 / 274 | 314 | 35 | 1,056 / 8 | 471 / 62 | 167 / 209 | 2,321 | Event- and trigger-heavy world; 759 trigger scripts and 7 attributes. |
| [Luxcellia.json](../sources/Luxcellia.json) | 12,758,457 B | 2 / 28 / 279 | 372 | 100 | 2,041 / 15 | 1,500 / 102 | 380 / 6 | 847 + 380 `questTriggers` entries | Largest content catalog; at or near several current community-documented limits. |
| [Overlord.json](../sources/Overlord.json) | 1,715,457 B | 1 / 54 / 53 | 71 | 4 | 58 / 4 | 234 / 18 | 66 / 6 | 229 | Small geography and cast, with extensive NPC-intent and trigger-script guidance. |

Every file also contains world lore, AI task instructions, items, factions, NPC types, resources, progression settings, game modes, and other settings. File sizes are not a quality score.

## Attached visual reference

`C:\Users\VladCodes\Downloads\VoyageWorldWIP\Map\Final2_upscaled.png` is the frozen visual reference for city map Version 1. The supplied image shows a walled circular city with concentric/radial districts, a luminous central tree, a waterfront, surrounding farmland, and distant mountains. This is a visual description of the supplied image, not new setting canon. Preserve the asset and its composition unless the user explicitly asks for a redesign. The map is separate from `sources/` and is not a Voyage JSON export.

## Gaps and interpretation limits

- The six files have no source-world URLs, creator changelogs, original export timestamps, or matching playtest reports. `ChikaraOld` is named “Old,” but its original export date and the exact changes from any newer version are unknown.
- `heroesVersion: 37` appears in every export, but all six use root-level `triggers`, `questTriggers`, and `quests` (and root-level `narrativeEvents`). Current community V37 runtime-state guidance documents `triggerDefinitions` at world root, while `arcs`, `narrativeEvents`, `quests`, and `questTriggers` belong under `parties[""]`; the community validator flags the root-level sections. However, the user's Studio import of a party-nested file showed an empty Advanced → Quests editor and missing party fields. Treat this as a mismatch between the community runtime-state schema and the Studio import/editor format until a fresh Studio round-trip resolves it. [Trigger schema](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [Quest schema](https://wiki.unofficial.voyage/world/quests), [API and validator](https://wiki.unofficial.voyage/tools/api).
- `ChikaraOld.json` contains case-distinct names such as `investigation` and `Investigation`. PowerShell's default object conversion treats keys case-insensitively and reported a collision; a case-sensitive JSON parser parsed the file successfully. This is a PowerShell reader limitation, not evidence of malformed JSON.
- A static scan can identify dangling keys and likely size-limit problems, but it cannot prove how a current Voyage build migrates or interprets these exports. No current Studio validator or playtest was run on them.
- The source set does not contain a current Studio-generated blank world, a schema export from the user's target release channel, or the official platform's full private schema. A separate local draft now exists in `../world-draft/`; it was seeded from the community API and checked with its public V37 validator, not imported into Voyage Studio.

## Read-only handling

All reference JSON remains under `sources/` unchanged. Research notes live in `research/`, and the active draft remains separate under `world-draft/`.
