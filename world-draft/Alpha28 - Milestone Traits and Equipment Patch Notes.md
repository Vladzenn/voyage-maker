# Alpha28 — Milestone Traits and Equipment

Use **GlowhavenAlpha28 - Milestone Traits and Equipment.json**, identical to WorldAlpha - World.json. This is a complete world export.

- Added 53 simple advancement traits to the native pool, one pick every ten levels. Forty-four known public skills have a +3 option requiring existing skill level 1; six attributes have +1 options; Health/Mana/Stamina capacity options grant +20/+15/+10. All require character level 10 and remain outside creation categories. Time is excluded. Each trait is an individual pick, not a recurring grant or an automatic increase to every skill.
- Retained and polished the existing custom equipment generator. It can create appropriate new goods when templates do not fit, with contextual stock, agreed prices, real ownership, bounded bonuses and crafting outcomes. Added two weapon slots and one tool slot alongside five existing armor slots. Existing practice blade/shield and three casting foci receive matching slots. No equipment catalogue expansion.
- Removed misleading equipped Health bonuses from bandages and healing draughts. Their existing 8/25 one-use restoration remains in item/resource instructions and still needs consumption testing. Consumable restoration is not a native equipment bonus.
- Rewrote Asterveil Ecology and Progression and Dungeon Enemy Groups as natural lore. Finite-pack actor/persistence directions remain under NPC-intent guidance and the existing dungeon triggers.
- Removed Developer Playtester, its story start, both developer traits, setup trigger, obsolete exam exclusion and test-only wording throughout current world data. Ordinary anomaly behaviour remains: the first qualifying outbound crossing at level 20 or above, once; no briefing requirement added. Court key permission remains separate.
- Marked four stale general guides as historical. Synced all 21 standalone section files and current release pointers.

## Schedules — unchanged

Orivelle alone has a programmed recurring schedule: day 1 Mythwing Meadows / Return Hide; day 2 Rimeglass Crown / Summit Saddle; day 3 Mirrorwater Basin / Rim Watch; day 4 Prismbloom Basin / Mineral Shore; then repeat. The route pauses during encounters, combat, party membership, death or actual confinement.

The other 204 authored NPCs do not have programmed recurring daily schedules. Initial positions, first-day placements, portal companion travel, boss placement, Ryūka's event movement and rare encounter appearances are event responses, not daily schedules. Academy morning attendance and academic-event pacing exist separately. No routine system was added in this update.

## Validation

Local JSON parsing; typed quest-condition guard for all 116 quests; milestone arrays, prerequisite targets and pool references; equipment slot/category matching; removal of current-world developer references; retained NPCs, abilities, images/coordinates and quest conditions/objectives/rewards; all 21 section exports synced. No live Studio import, level-up selection or gameplay test performed. This update is for fresh ordinary-character testing; existing saves containing removed developer traits were not migrated.

Counts: 205 NPCs, 173 locations, 710 areas, 480 abilities, 273 traits, 116 quests, 299 world triggers, 13 starts, 45 skills.
