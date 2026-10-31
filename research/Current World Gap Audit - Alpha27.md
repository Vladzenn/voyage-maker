# Current World Gap Audit — Alpha27

Audited: 2026-10-29. Images and missing artwork are excluded.

## Scope and evidence

Source: `world-draft/WorldAlpha - World.json`, SHA-256 `3b6b47591093e10cd2c92b4358c695eea4f44a34f05f69b669d21d29dd5b3c33`.

The current world contains 5 realms, 9 regions, 173 locations, 710 areas, 205 NPCs, 26 factions, 159 lore entries, 96 NPC types, 116 quests, 300 world triggers, 480 abilities, 45 skills, 222 traits, 14 creation categories and 14 story starts. It already has currencies/prices, martial techniques, distinct academy subjects, destination populations, native quest conditions, staged adventures and authored academic pacing. These are not missing systems.

This audit inspected the current export, selected system definitions and scripts, current community schema explanations, and existing local test notes. A fresh check found no unresolved direct location-region, region-realm, NPC location/area/faction/type or ability-prerequisite references. All 116 quest completionCondition fields pass the shared typed-condition guard. Those limited checks are not full Studio validation or gameplay certification. Previous user playtests exist; a complete recorded pass for the latest merged release does not.

## Priority 1: equipment, rewards and consumable reliability

**Confirmed configuration gap.** Item Settings defines five Armor slots and no Weapon or Tool slot. The catalogue has no Armor item templates, only two Weapon templates (Practice Blade and Training Shield), and no item has a configured slot. Weapons and tools can still be used narratively, but there is little authored equipment progression or supported equipping of their passive bonuses.

Of 59 item templates, 27 are Documents, 21 Tools, 4 Keys, 4 Consumables, 2 Weapons and 1 Currency. The world is much richer in techniques than in desirable purchases and finds. Its existing shops and craftspeople provide a strong foundation, so this needs a focused catalogue rather than more establishments: ordinary combat gear, a few useful enchanted items, field supplies, materials, commissions and distinctive finite rewards. AI-generated items can appear; the absence of templates does not mean nothing can ever be bought.

**Confirmed semantic mismatch.** Clean Bandages and Standard Healing Draught carry Health resource bonuses of 8 and 25. The current community reference defines item resource bonuses as maximum-resource increases while equipped, not one-time restoration. Their descriptions and Health instructions request healing on actual use, but those text rules are separate from native equipped bonuses. Correct the misleading bonus configuration and test consumption, inventory removal and a single actual Health restoration. This does not require converting every ordinary purchase into a trigger.

References: [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings), [Items](https://wiki.unofficial.voyage/world/itemTypes).

## Priority 2: useful advancement and an ordinary-player balance baseline

**Confirmed incomplete progression choice.** A trait pick is configured every ten levels, but levelUpTraitPool is empty. There is no eligible advancement selection to offer. Either author a small pool of useful, compatible specializations or deliberately leave trait advancement disabled/unadvertised. Creation traits are not automatically good level-up traits.

There is already a large ability catalogue: 430 of 480 entries have a highest skill prerequisite below 80. More bulk spells are not the immediate shortage. The missing evidence is how builds perform with the current skill checks, costs, recovery and encounter opposition.

Ability descriptions specify resource costs, but the native ability schema has no dedicated cost or status-effect fields. Bonus and cooldown are structured; the narrator interprets most other effects. Therefore Mana/Stamina spending, multi-target effects, summons, control, defensive techniques and mixtures need representative live tests rather than an assertion that every described mechanic is deterministic.

Use ordinary characters at early, incident and midgame stages: a caster, a martial character and a spellblade. Test one duel, one enemy group, escape, healing and the level-45 queen with appropriate support. All 48 authored students currently have level 15 despite spanning four academic years. That is a calibration question, not a recommendation to weaken adult faculty. Preserve the user's intended powerful professionals.

References: [Level Progression](https://wiki.unofficial.voyage/mechanics/progressionSettings), [Abilities](https://wiki.unofficial.voyage/mechanics/abilities).

## Priority 3: a defined starting livelihood

**Confirmed omission in authored grants.** Ordinary starts, ordinary creation traits and global starting items grant no Marks. The developer kit grants 100,000. Ordinary native trigger item-add effects do not supply starting cash either. Runtime generation could still establish money, but the export does not provide a consistent baseline.

Decide what a new student, new employee, adventurer applicant and merchant actually begin with: pocket money, accommodation, meals already covered, first pay date, and any optional debt. A penniless start can be intentional; every origin silently depending on the model to invent its finances is less reliable. This need not become a salary simulator.

Everyday prices already exist. The improvement is connecting those prices to earnings and worthwhile spending: supplies, repairs, transport, commissions, living arrangements and optional luxuries. Most fixed quest item rewards are presently Marks rather than authored equipment. Rewards delivered by triggers or generated in play also exist and were not treated as absent.

## Priority 4: routines and academy support

**Partially implemented.** The mandatory morning block and free afternoons are established, timetables exist, academic milestones have pacing, and first-day placements are authored. Ordinary recurring daily routines for most people are not configured. Orivelle's circuit is an existing exception.

Add a compact availability plan: morning workplace/class, afternoon personal activity or consultation, evening meal/home. Some NPCs should share spaces and change company. Conversations, combat, custody and commitments must override routines. A schedule should help find people without dragging them out of active scenes or moving the whole cast every turn.

Each academy's 17 authored members are its Archon, headmaster, three professors and twelve students. Support roles such as registrar, librarian, infirmary staff and workshop supervision remain largely unnamed. Select a few recurring service characters where the player will actually return; not every desk needs a full major card.

The latest first-day openings are substantial. The remaining proof is the transition from welcome to actual lesson to afternoon choices, then a different second morning. Faculty starts establish tomorrow's teaching and a preparation quest, but recurring classroom play still depends heavily on generation.

## Priority 5: stronger recurring activities and personal follow-through

**Content opportunity, not a broken system.** The academic sequence, festival, thesis, guild jobs and regional quest chains already provide activities. A repeatable thesis is not needed; it is correctly treated as a capstone.

The Eternal Crucible has tournament lore and active-match flags, plus related quests. It lacks a fully authored public tournament loop with registration, opponents/bouts, adjudication, actual result and prize. One memorable tournament would make better use of the cast and arena than another large batch of unrelated jobs.

Relationship personalities, knowledge boundaries and consequences already exist. The useful next layer is callbacks: what someone does differently after a shared experience, an invitation they initiate, a dispute that changes ordinary meetings, or a personal goal the player can choose to support. Most of these can be scenes and persistent factual outcomes; not every relationship needs a journal quest or a new numerical meter.

The central Glowhaven power structure has major characters and succession lore, but no comparable authored succession/political sequence in the current quest list. That is an optional longer-campaign direction, not a prerequisite for open-ended beta play. Drakenspire already has clan and household quest chains; those should not be counted as absent.

## Priority 6: prison depth

**Confirmed thin coverage relative to its footprint.** Wraith Island Prison has 14 locations but one initially placed authored NPC, Akira Oritsu, and two directly prison-sourced quests. Intake, work authorization, discharge, escape and access triggers exist. They are not a complete prison-life cast or a proven serving-time loop.

If imprisonment is a meaningful consequence in beta, give the player people and choices there: a few officers and inmates, legal review, work, visiting, tensions and a viable release path. Do not merely add extra rooms. Actual sentence accounting and individual multiplayer custody require a separate design; they are not already implemented by a custody flag.

## Priority 7: consistency and remaining internal language

**Confirmed stale text.** The developer premade advertises 42 skills; the kit actually grants 44 public skills out of 45 configured, excluding Time. Its description and trait narrative also describe arranging an examination briefing to test the anomaly. The outbound portal scripts actually check level >=20 and the incident flag independently of briefing. Update those explanations to describe the current mechanic.

**Confirmed mixed-purpose lore.** Asterveil Ecology and Progression and Dungeon Enemy Groups still contain terms such as NPC type, automatic spawn, authored boss, generated record and native actor. These are authoring instructions, not natural setting knowledge. Their presence does not prove an NPC will recite them, but it leaves a leakage route. Move generation mechanics into the appropriate under-the-hood instructions and keep lore focused on the world itself. Public NPC descriptions and location/area descriptions did not yield comparable engine-language hits in the targeted scan; ordinary references to physical storage were excluded as false positives.

Some older guides still describe the very early world and even retired academy terminology. They should be marked historical or updated before they are used to guide the next change. Use the current export and release notes as the source of truth.

AI instructions total approximately 288,000 characters across 18 separate tasks, not one single prompt. The next quality pass should check contradictory rules and ownership of instructions, not add length for its own sake. Several task sections have little remaining room for future additions.

## Priority 8: verify critical paths and multiplayer scope

**Unverified runtime behaviour.** The latest full release needs a recorded normal-character pass through creation, the academy opening, actual lesson participation, a paid job, purchasing/consuming an item, an ordinary fight, portal travel and return, the once-only anomaly, dungeon progression, trophy delivery and the bazaar rivalry. Test failure, refusal, retreat, reload and repeat attempts, not just success. A local reference check cannot establish semantic recognition or timing.

**Confirmed shared-state design requiring a decision.** The academic clock stores one party phase and computes guild rank from the highest badge carried by any party member. Prison role and custody flags are also party-level. These are understandable for a shared campaign, but they cannot stand in for separate qualifications or separate imprisonment of individual players. Decide which systems are deliberately shared before advertising broad multiplayer support.

The previous allegation that eleven guild offer flags have no writers is not repeated here: the guild board writes them dynamically, and earlier executable fixtures covered those paths. A simple literal-name search is insufficient evidence of unreachable progression.

## Later expansion, not beta blockers

- Custom music and specific boss/event overrides: currently 21 stock families and no music effects in world triggers. This is an approved future direction, awaiting the user's tracks and scene choices.
- High-level adventure content: much of the exploration range ends around the level-60 frontier, while the character cap is 100. Powerful named adults are not automatically endgame adventures. State the beta's intended content range before expanding it.
- Finer ancestry appearance choices: Fae and Beastfolk allow user-written individual anatomy, but there is no separate pickable suite of fae body features or beastfolk variants yet. The general appearance builder already exists.

## Things this audit does not treat as defects

Asterveil is intentionally wilderness-heavy and has twelve NPCs. The dragon Rovakthuun and yeti Orrum deliberately begin offstage. Not every location needs an authored resident. Empty worldVoices can use available/default voices. Empty dedicated arcs, narrativeEvents and questTriggers collections do not erase the 116 quests or 300 world triggers. Random travel encounters are deliberately disabled; existing on-site threat descriptions and dungeon pack systems remain distinct.

Recommended work order: resolve equipment/consumable semantics and starting livelihood; settle level-up choices; run ordinary-player tests; then add a small set of daily routines and one flagship tournament. Develop prison depth according to the user's forthcoming plans. Keep new content responsive to playtest findings rather than filling every possible system before beta.

No world, image, source or export file was changed by this audit.
