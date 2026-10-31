> Historical snapshot: this document predates Alpha28. For the current import use `world-draft/WorldAlpha - World.json` or `GlowhavenAlpha28 - Milestone Traits and Equipment.json`; consult Alpha28 patch notes before following older configuration instructions.

# Alpha readiness: missing pieces

2026-10-27, after the portals revision. This is an assessment of the actual draft, not a proposal to add every system before playing.

The alpha has 128 NPCs, 91 locations, 345 areas, 58 lore entries, 23 quests, 42 skills, ten techniques and four realm maps. It already has marks and everyday prices, authored local situations, academy personalities, crime/prison scenarios, HP/MP and basic progression. Those should be tested and refined rather than treated as absent.

## Highest priorities

| Gap | What exists | Useful next addition or test |
|---|---|---|
| A proven ordinary-player loop | Four academy starts and Random; many local situations | Play one normal opening through meeting someone, undertaking a task, handling a challenge, receiving the actual reward and returning. Then repeat with a physical/noncasting build. |
| Live import and runtime verification | Local preservation/reference checks and mocked mechanics fixtures | Studio validation plus actual portal round trips, developer setup, difficult zero-MP checks, quest-state transitions and resource timing. Local tests cannot establish AI behavior. |
| Destination populations | Ten new destination locations with functions and situations | A small curated cast: a Drakenspire host/armorer/warrior and an Asterveil host/researcher/habitat keeper. None is authored yet. More Glowhaven students are not the immediate need. |
| Concrete expedition content | One party-level authorized-expedition framework | One actual mission per destination with a specific existing contact, bounded objective, optional approaches, evidence, return and debrief. The framework currently relies on scene generation to define these details. |
| Mid- and late-game progression | Level cap 100, 42 skills, ten mostly introductory magical techniques | Distinct martial, spellblade and caster advancement. The current level-up trait pool is empty despite a trait pick every ten levels; decide what those picks should offer. This was deliberately deferred. |
| An ordinary combat balance baseline | Adult power bands and player stats; developer testing preset | Test a mundane fight, a dangerous fight and a supervised duel with normal players. Check hit rates, damage, resource cost, escape and NPC authority. The developer preset cannot validate fair difficulty. |

## Important content and continuity gaps

1. **New destination art.** Drakenspire and Asterveil have authored locations and coordinates but no map images or location art. The Portal Room and developer preset also have no new image assets. Existing images are retained.
2. **Academy support staff and operational detail.** Each academy's current 17-member roster comprises its Archon, headmaster, three faculty and twelve students. Dedicated infirmary, library, grounds or workshop staff have not been authored as a school roster. Add only the people needed for useful services and scenes.
3. **Routines and availability.** There is no recurring authored NPC schedule system. Starting placements exist, but ordinary class hours, office hours, meals, sleep and absences need a small consistent framework before a full timetable. Conversation, custody and other actual events must override routines.
4. **Noncasting introductions and progression.** Existing starts allow nonstudents and noncasters, and skills support them. There is no bespoke traveler, worker or martial opening, and the ten named techniques do not yet provide a broad purely martial advancement catalogue. Narrative permission alone is not equal mechanical depth.
5. **Transit administration.** The routes have actual endpoints and permission-aware guidance, but no authored transit official, timetable, universal fare, cargo policy or emergency closure procedure. Establish a few practical rules through one playable arrival instead of inventing a large bureaucracy.
6. **Repeatable and individual expedition records.** The quest records one assignment per party, not repeatable mission IDs or individual student transcripts. This is enough for the first test; graduation, retakes and separate-player expeditions need a design if they become relevant.
7. **Tournament structure.** Competition culture and an active-duel flag exist. A complete event still needs a registration path, opponent selection, bracket or bout structure, officials, reward rules and handling of proven cheating. The current flag does not provide these.
8. **Consumables and crafting precision.** Prices and sample items exist, but consumption effects need live confirmation rather than assuming equipment bonuses act on use. Mana medicines have lore but no agreed standard dose, stock item or restoration rule. Crafting needs actual input/output and failure conventions when it becomes a recurring activity.
9. **Foreign trade and jurisdiction.** Marks work in the current economy. Drakenspire/Asterveil exchange practices, local offices and how Glowhaven authorizations are recognized abroad are still loose. Do not invent automatic foreign authority or new currencies just to fill a table.
10. **A longer campaign pressure.** Succession, academy politics and local quest hooks provide material. There is only one authored arc and one narrative event. A chosen campaign needs a few connected developments and consequences; the sandbox does not need an urgent main plot on every visit.
11. **Player-facing orientation.** The world has many places and possible acquaintances. An optional concise explanation of choosing a role, finding a few contacts, taking work and reaching the portals would help. It should not introduce every NPC or recruit a class-sized party.
12. **Publication cleanup.** Before release, remove the developer preset, its two traits and setup trigger or move them into a separate testing export. Recheck retained older reports against the chosen release, confirm content/discovery settings and keep a known-good backup. This alpha intentionally retains the developer option the author requested.

## Recommended next slice

Build a small Drakenspire expedition with three supporting people and a survey/repair problem that permits both a martial traveler and a caster to contribute. Play the outward portal, local stay, agreed task, return and debrief with a normal character. Use the developer preset separately to inspect every location and reproduce state bugs. That would test the new structure more effectively than adding another large batch of characters immediately.
