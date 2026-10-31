# Glowhaven Alpha Playability Audit

**Date:** 2026-10-26 (Asia/Shanghai)  
**Status:** Historical audit of the earlier Alpha playable copy; superseded by the three current WorldAlpha files. The findings below do not establish validation or playability of the new files.  
**Current files:** [WorldAlpha - World.json](../world-draft/WorldAlpha%20-%20World.json), [WorldAlpha - Locations.json](../world-draft/WorldAlpha%20-%20Locations.json), [WorldAlpha - NPCs.json](../world-draft/WorldAlpha%20-%20NPCs.json).  
**Input:** `C:\Users\VladCodes\Downloads\GlowhavenAlpha.json` (left unchanged)  
**Reference sources:** read-only files under `../sources/` (left unchanged)

## What the supplied Alpha contains

The supplied V37-labeled export has 45 NPCs, one realm, one region, 68 locations, 256 areas, one `Random` story start, seven skills, and nine social triggers. The user's refreshed area-map paste removes the redundant Dragon Hoard quiet lounge, leaving 255 supplied area records; the academy update adds 20 areas. The current expansion and Alpha working copies now contain 275 areas. The refreshed user paste is the source of truth for this academy revision; the original export remains unchanged.

The map is substantial, but the play wiring was mostly blank: all 45 NPCs lacked locations and areas; faction and world-lore catalogs were empty; the only start selected no fixed location; there were no quests, traits, abilities, or items; and 44 NPCs had level `0` and tier `average`. The separate character-card file has the same 45 names and its authored profile fields match the Alpha roster. Those cards were used as the writing source and retained in the output.

The supplied Alpha and all six reference exports use the older root-level `triggers`, `quests`, `narrativeEvents`, `arcs`, and `questTriggers` layout. The current community V37 reference uses `triggerDefinitions` at the root and puts `quests`, `narrativeEvents`, `arcs`, and `questTriggers` under `parties[""]`. The Studio error text says those party fields were `undefined` (missing); an empty JSON object `{}` is a defined map, not null or undefined. The edited copy currently mirrors authored arc/quest/event/quest-trigger maps at root and under the default party to cover the two observed layouts. That compatibility approach still needs a fresh Studio import/save to confirm.

A concrete missing object was also found: the supplied Alpha omitted `imagePromptConfiguration`, while all six reference exports and the current V37 seed contain it. The current seed additionally supplies `characterCreationMusic` and `compatibilityRevision`, which the older exports omit. The playable copy now includes those exact seed defaults; `imagePromptConfiguration` has the five default keys (`npcs`, `locations`, `areas`, `regions`, `items`). This is a plausible cause of the generic object-conversion error, not a confirmed diagnosis.

## Borrowing from Luxcellia and ChikaraOld

The supplied examples vary greatly in size. ChikaraOld has 137 NPCs, 277 locations, 24 story starts, 655 quests, and 672 triggers. Luxcellia has 372 NPCs, 279 locations, 100 story starts, 380 quests, and 847 triggers. Glowhaven's 45-character cast and 68-location map have enough authored material for a focused first scenario; it does not need the examples' content volume.

This pass borrows reusable design techniques only:

- **From Luxcellia:** behavioral personality cues, clear character motives, and a concrete opening hook tied to an authored start.
- **From ChikaraOld:** grounded school and city routines that leave room for conversation and everyday choices.
- **Guardrail from both:** keep the initial system surface small and follow current field names; neither old export is treated as a current schema template.

No unique names, lore, or plot content from either reference world was copied.

## Implemented in the playable copy

### NPC roles, levels, tiers, and placements

Role bands use the world's 100-level cap. Every member of a role shares one initial test level so parity is easy to review. The band leaves room for later differentiation. Combat `tier` is assigned separately from level and role.

| Role | Cast size | Working band | Initial level | Combat tiers in the copy |
|---|---:|---:|---:|---|
| Archons | 4 | 80–89 | 85 | 4 elite |
| Headmasters | 4 | 65–74 | 70 | 1 strong, 3 average |
| Teachers | 12 | 40–59 | 50 | 3 strong, 9 average |
| Students | 24 | 10–20 | 15 | 6 strong, 10 average, 8 weak |
| Great Sage | 1 | Fixed | 100 | 1 mythic |

### Level calibration from the reference worlds

The source worlds do not share one universal level scale. ChikaraOld commonly assigns level `0` to academy students, which makes them party-scaled rather than a reliable absolute benchmark. Luxcellia's named academy students provide a clearer comparison: examples run from level 15 (Hikari, average tier) through the high teens and twenties (including strong or elite students). Across other references, weak-tier NPCs range from level 1–2 training constructs in Larion to levels 3–10 in Konosuba and 9–10 in Luxcellia; those examples are different roles and should not be used as student-level rules.

I lowered the student design band from 15–34 to **10–20**, with all named students currently set to level **15**. This places ordinary students near Luxcellia's lower student range while keeping a common baseline for peers. Combat tier remains independent: all eight weak-tier students are still level 15, not pushed lower because of the word `weak`. These levels remain untested balance starting points. Voyage's community reference describes tier as affecting combat HP, damage, and intent complexity, while explicit NPC level is a separate field.

The 44 academy characters now belong to their canon academy and have a valid location and area there. Ilyra Stillglass is placed in the Administrative Wing of the Grand Sage's Court. Hinae Komori is at Phoenix Wing's Arrival Court for the opening; she is the only authored NPC assigned to that starting area. All 68 locations and 275 areas are present in the current working copy. Each academy location has an NPC level range of 1–60 for party-scaled generated NPCs; the named cast uses explicit levels.

The original export's `known` flags are preserved entry by entry, with matching values mirrored to `initialKnown`: 63 of 68 locations are known; only **Wraith Island**, **Hermit's hut**, **Shadowspire**, **Wraith Island Prison**, and **Evertree Base** remain unknown. NPC flags also match the original (37 known, 8 unknown).

### Factions, lore, and story

Seven faction records are now present: the four canon academies, the Conclave of Archons, the Council, and the Elite Strikeforce. The last two remain descriptive working labels where their formal names or membership are not established. Each faction's public summary is mirrored verbatim in its World Lore entry to avoid conflicting descriptions.

The Alpha copy now has a concise world overview and lore for academy ideals, the Archon/headmaster distinction, magic affinity, the Evertree, Great Sage succession, and the Elvish language rule. The current notes' academy names and ideals are used: Phoenix Wing/strength, Hydra Head/harmony, Gryffin Tail/study, Dragon Hoard/wonder. The earlier small draft contained a stale Pegasus Academy entry and different ideals, so its faction and lore text was not copied. References to the city's landmark now use its canon name, **the Evertree**.

`Phoenix Wing: Arrival Court` is the default start at the exact Arrival Court area. It leaves the player's reason for being there and academy affiliation open; Hinae offers directions or an answer to a question. The optional `First Words` quest is available from this start and asks for one brief conversation, without assuming the player is a student. After the player accepts and voluntarily greets, introduces themselves to, or asks someone nearby a question, a quest trigger starts the one-turn `A Friendly Reply` narrative event; event completion completes the quest. The original Random start remains available as a non-default option. The nine existing social triggers remain under the current `triggerDefinitions` key.

### What the source worlds show about empty sections

All six source exports use root-level `triggers`; the supplied current Studio seed and community schema instead use root-level `triggerDefinitions`. The Alpha’s nine social rules were retained under `triggerDefinitions`. ChikaraOld has two authored arcs, while Luxcellia and the other four supplied examples have none, so arcs are optional. For this import/playability check, I added one compact `first_connection` arc using Chikara’s demonstrated arc fields; it is concluded by the single `First Words` quest. The social loop does not copy either source world’s unique plot or lore.

### Minimum mechanics and AI guidance

The seven existing social/adventure skills remain. One `spellcraft` skill is added to the catalog for general magic checks, and AI guidance says all schools remain learnable and that affinity does not grant a spell automatically. This does **not** guarantee a new character starts with Spellcraft: there is no character-creation trait that grants it in this pass. The current skill settings allow an unowned skill to be learned probabilistically when attempted (base 10% plus the linked attribute modifier), so its availability and first-use behavior need to be checked in a fresh game.

The opening can be played through conversation and exploration. Traits, guaranteed starting skills, learned spells/abilities, items, and a mechanical affinity bonus are not built in this first pass. The first playtest should confirm how character creation handles the skill list, then try Spellcraft and record whether the character can use or learn it. This is not a complete combat or magic-progression system.

## Checks performed and still open

**Static checks performed on the new copy:** JSON parses; all 45 NPC location/area/faction references resolve; all location faction references resolve; every area path points to a defined area and links back symmetrically; the Phoenix start’s location/area and `First Words` quest resolve; each faction has a matching World Lore mirror; root and party-level quest, narrative-event, quest-trigger, and arc maps are present and match; `First Words` points to the defined reply event and the trigger points back to the quest/event; the arc requires one quest and `First Words` is marked conclusive; all original trigger records have matching keys/names and condition/effect arrays; the current V37 seed defaults are present; source `known` flags are preserved on all NPCs and locations; the two intentionally open success-score bounds remain `null` as in the supplied Alpha; and the Evertree/academy-name scan found no stale aliases.

**Studio import correction:** the screenshot of `Content → World → Advanced → Quests` showed `{}` and an error naming missing (`undefined`) party fields `questTriggers` and `arcs`. The working JSON now has a non-empty `First Words` quest, `A Friendly Reply` event, `first_words_reply` quest trigger, and `first_connection` arc. These maps are mirrored at root and under `parties[""]`. The two open success-score bounds are restored to `null` from the supplied Alpha. The original `known` values are also mirrored to `initialKnown`. This compatibility layout still needs a fresh Studio import/save; no successful save is claimed.

**Not performed:** import into Voyage Studio, Studio's native validation, or a live game playtest. The source file is marked V37 but has an older field layout; the target release channel must confirm the migration on import. Do not describe this copy as Studio-validated or playtested yet.

**One focused dry-run check:** the default Phoenix start resolves to its location and Arrival Court area; Hinae is placed in that scene; the start references `First Words`; the quest location resolves; the quest completion condition names the defined reply event; the quest trigger gates on an accepted quest and a voluntary conversation at Phoenix Wing; the event and trigger references resolve; and the one-quest arc and root/party maps match. This checks the authored wiring only; it does not execute Voyage’s narrator, confirm event timing, or prove runtime quest completion.

## Next playtest pass

1. Import the working copy as a separate private world in the intended Voyage Studio channel.
2. Confirm the default start opens at Phoenix Wing's Arrival Court and Hinae appears without being forced into the party.
3. Create a character with an arbitrary background and try accepting and declining Hinae's invitation.
4. Accept `First Words`, greet or ask someone nearby a simple question, confirm `A Friendly Reply` starts, and check that the quest completes after the reply without assuming school enrollment.
5. Check the character's starting skills. Attempt Spellcraft and record whether it resolves as a check, whether the character learns it, and how the learning chance behaves; do not treat the skill description as proof of spell learning or combat balance. The community schema documents skill learning on use, but Studio/runtime behavior still needs confirmation.
6. Record Studio warnings and observed behavior before adding more quest, trait, or ability content.
