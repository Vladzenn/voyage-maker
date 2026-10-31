# Schools of Magic patch notes

2026-10-27. Built from the user's latest full-world attachment, preserving its newer map changes. The supplied lore sheet provides accepted magic rules; the user's latest instruction establishes Dragon Hoard's exploration-and-relics direction.

## Academy identities

The old Strength/Harmony/Study/Wonder descriptions are replaced with institutional work, traditions and room for disagreement:

| Academy | Current direction |
|---|---|
| Phoenix Wing | Defense, readiness, threat assessment and supervised protective work; demanding drills and a fierce dueling culture. |
| Hydra Head | Diplomacy, trade, logistics, mediation and civic coordination, alongside broad magical and combat education. |
| Gryffin Tail | Research, investigation and dungeon surveys, with the academies' most advanced facilities and sole formal magitech research specialization. |
| Dragon Hoard | Exploration, relic assessment, careful handling and responsible field recovery, with strict traditions inherited from its founder. |

Faction descriptions, matching World Lore entries, world background, generation guidance and relevant locations agree. Mandates do not dictate every student's personality or affinity. All schools retain comparable broad education and combat training. Existing civilian, judicial and security responsibilities remain distinct.

## Lore and consistency

World Lore grows from **42 to 54 entries**, adding focused accounts of mana and souls, capacity and recovery, exhaustion and the vital remainder, hypothetical extraction, body casting, catalysts, external reserves, spell blueprints, Freeform, bodily Enchantment, magitech, medicine, expeditions and relic work.

- Ordinary animals may contain inert mana but lack the soul needed for intentional circulation. Mana beasts and summoned constructs are distinct.
- The Evertree thickens local mana; it is not declared the universal origin of magic.
- Body casting is trainable. Catalysts assist learned control and generally contain no spare reserve.
- Speech, gestures and materials are optional casting aids; personalized blueprints guide familiar spells. True Freeform is rare and demanding.
- Intentional bodily enhancement belongs to Enchantment and can be very strong. Affinity still does not restrict what someone can learn.
- Zero usable MP leaves a caster conscious. Ordinary casting cannot consume the soul-sustaining remainder. A rare last spell requires an exceptionally difficult authoritative check.
- Forced soul extraction remains unobserved for humanoids, including Void mages. It does not become a new player or enemy power.
- Mana medicines are expensive and regulated. Excess ordinary doses cause illness and poor returns rather than fatal overdose; restoring MP does not instantly cure soul shock.

Five NPC entries receive narrow clarifications: **Akane Todo**, **Ritsu Kurogane**, and **Takeru Akabane** use learned Enchantment for bodily acceleration; **Tōru Shizunami** is exceptional for control and scale rather than merely casting barehanded; **Gen'ichirō Mizuhara** demands precise incantations as his own doctrine rather than a universal law of magic. Their identities, affinities, levels, portraits and relationships are retained.

Existing skill and study descriptions, three ordinary catalyst descriptions, and associated kit text are aligned. No new ability, trait, item catalogue entry, affinity or resource is added.

## Gameplay changes

**Variable passive MP recovery:** A once-per-tick script restores **1–3 MP**, averaging the previous +2. Native MP recharge is set to zero to avoid double recovery. Base MP, maximum-MP level gains and completed-rest restoration are retained. These numbers are game calibration, not a newly established biological formula. A fresh-zero reminder reinforces the consciousness and last-cast rules without causing damage or awarding success.

**Authorized expeditions:** A new hidden quest records a chosen student assignment through acceptance, actual Great Sage/court authorization, completed out-of-city fieldwork and a received debrief. All students have the educational requirement, but the player is not forced into enrollment or a particular assignment. The existing Genzō Iwakura fieldwork scenario now respects actual authorization when used for academy credit. A party record does not automatically graduate everyone or give visitors credit.

**Tournament state:** Official duels involving a player competitor record active/stopped state. External stored mana and mana potions are prohibited during the live duel; ordinary non-battery catalysts remain permitted. An official stop permits emergency treatment. Evidence and rulings govern cheating; no automatic detector, confiscation or punishment is invented.

There are **eight new general triggers**: variable uptake, fresh-zero notice, tournament start/stop, and four expedition stages. The total is **39 general triggers**, **22 existing party quest triggers**, and **23 quests**.

## Preservation

- **128 NPCs**, original roster order and all **268 media URL fields** preserved.
- **81 locations**, **313 areas**, latest coordinates, region/realm membership, images and path connections preserved. Five location summaries and four area descriptions gain relevant context.
- Wraith Island remains a Glowhaven location; Wraith Island Prison remains a separate realm with **14 facilities**.
- Six attributes, 42 skills, 41 traits, 10 abilities and 23 item types retained. Skill, check-contribution and character caps remain 100.
- HP settings, progression rates, existing starts and unrelated quest outcomes retained.
- Input attachment, lore sheet and all six `sources/` reference files left unchanged. Previous canonical files and the exact user input are backed up locally.

## Verification and limits

Local structural, reference, size and preservation checks passed, along with **15 script and lifecycle fixtures**. Those fixtures run the actual scripts with mocked documented state. They do not prove the live AI will classify authorization, competition or medical situations correctly.

**No live Studio import, full platform-validator run or gameplay playtest was performed.** The zero-MP check, evidence-based tournament rulings and interpretation of personal spell knowledge remain AI-dependent. The expedition ledger tracks one party assignment; individual transcripts and repeatable expeditions are not implemented. Numerical capacity growth per cast, medical thresholds and unspecified medicine doses remain open.

See [research and implementation decisions](../research/Schools%20of%20Magic%20-%20Lore%20and%20Mechanical%20Implementation.md) for official/community sources, examples, and focused live checks. Use the full **GlowhavenAlpha3 - Schools of Magic.json** export; **WorldAlpha - World.json** is its identical canonical copy.
