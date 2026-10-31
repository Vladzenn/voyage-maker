# Alpha18 — Complete Ability Catalogue

## Delivered sections

- **WorldAlpha - Abilities.json:** a complete plain-map replacement containing 480 abilities; no outer abilities wrapper.
- **WorldAlpha - Traits.json:** a complete plain-map replacement containing all 45 traits, including updated starter grants; no outer traits wrapper.
- **GlowhavenAlpha18 - Complete Ability Catalogue.json:** the synchronized full world, identical to WorldAlpha - World.json.

For the requested section-only workflow, import Abilities first and Traits second. This leaves the other sections in your Studio world alone. New trait grants should be checked on fresh characters; no running-save migration was implemented.

## Repertoire

Added **445** records and retained all existing **35** exactly, including their original order. The complete catalogue has **360 spells** across **20 public disciplines**, **64 martial/tactical techniques** split equally between Force Combat, Finesse Combat, Guarded Combat and Tactics, **40 mixed techniques** (two per public discipline), and **16 Magitech techniques**.

Each discipline has eighteen spells: five introductory, six trained, three advanced, two expert and two master. Fourteen are eligible by skill 59; this is a skill threshold, not a character-level prescription. New names describe distinct actions rather than numbered spell evolutions. Reaching a skill threshold makes a technique eligible; it does not grant the entire library automatically. Spellcraft remains mandatory for invention and substantial redesign, rather than every casting of a known spell. Ordinary attacks, guard and movement remain free.

Fire, Water, Earth, Wind, Lightning, Ice, Light, Metal, Nature, Sound, Gravity, Space, Void, Healing, Enchantment, Summoning, Illusion, Divination and Soul join the existing full Arcane repertoire. Each includes practical utility and tactical options as well as attacks. Physical methods offer strength, precision, defence and teamwork without requiring magic. Hybrid techniques use one actual physical delivery resolution and explicitly spend both Mana and Stamina. Magitech uses actual tools, materials, known systems and project work rather than producing finished devices for free.

New restorative spells use maximum-Health percentages so they continue to matter at higher character levels. Group triage has one shared budget rather than a full restoration for every recipient. Existing Gentle Closure and Quiet Meridian are unchanged. Recovery must be applied once; actual injuries, viable tissue and treatment conditions remain meaningful.

Space requires Gravity Magic 25 alongside each Space threshold. Short moves need real safe landings; long-range journeys need genuinely learned existing destinations, stable anchors and actual native location updates. Private spatial work does not grant authorization to the public court portal network. Time gets no public abilities or creation grants. Soul entries specify whether they animate unconscious remains, address a conscious willing spirit or contest an intrusion; necromancy is not silently treated as resurrection.

## Starting studies

All **19 current starting study traits** now grant two suitable rank-1/rank-3 spells with their existing discipline skill 3. Force Training and Finesse Training receive two basics too; Arcane Studies and Guarded Training retain their already approved pairs. In total, 22 starting study/training traits have two eligible techniques each. The Developer Playtest Kit contains all 480 entries once. See Starting Studies and Training.md for the exact pairings.

No new Space starting choice, Time affinity, character-creation selection count, spontaneous-learning setting or teacher/book requirement was added. The user deferred skill acquisition. Scholarly Practice remains theory training rather than another free casting discipline.

## Preservation and verification

Passed **8,648 local structural/reference/preservation checks** and **1,872 script/eligibility fixtures**. Every native prerequisite was tested at its threshold and with each individual prerequisite one point short; starter grants were checked against the actual starting skill bonuses. Existing portal, dungeon, guild and court cases still pass. All configured JavaScript compiles in the local test harness.

Only abilities and the specific trait repertoire/text fields changed in the world. NPCs, uploaded images, map positions, lore, skills, resources, AI instructions, quests, triggers and acquisition settings are unchanged. Fifteen standalone sections match the complete export. SHA-256: `747812294ac6d60a54969b20f8914646c7f2d168bb10d72d4393fb4c91ac687c`.

This is **not a live Studio import or balance playtest**. The documented ability record supplies name, description, prerequisites, bonus and cooldown; it does not supply native per-ability cost, damage, summon or teleport effect fields. Those actions remain interpreted from the authored descriptions and the existing AI/resource guidance. Requirements, bonus and cooldown are actual native data. No unsupported effect fields, artificial spawn functions or redundant per-spell triggers were invented.

## Voyage checks to perform

1. Replace Abilities and Traits, then create a few fresh characters from different studies. Check the two named grants and their actual costs; inspect physical Force/Finesse/Guarded starts too.
2. Try introductory, trained and advanced choices. Confirm that eligibility does not automatically award unlearned spells and that the 480-entry catalogue remains usable in the interface.
3. Compare forceful, precise and defensive delivery; confirm mixed techniques do not double-hit or add two complete skill totals. Ordinary physical actions must remain possible at zero Stamina.
4. Test single-target and group Healing, one-time percentage restoration, interruption, cooldowns and the preserved Quiet Meridian action.
5. Call a familiar, command it and dismiss it. Check action economy, persistent actual entities and no automatic duplicate attacks or permanent conjured resources.
6. Test safe short Space movement and a prepared journey to a learned existing destination. Confirm native realm/location/area changes; descriptions alone cannot prove travel succeeded. Public portal key checks and authored dungeon navigation must still hold.
7. Test Magitech inspection and real repair with actual tools/materials, and a small Spellcraft invention experiment. Neither grants an artifact, new discipline or rare Time knowledge automatically.

References: [community ability documentation](https://wiki.unofficial.voyage/mechanics/abilities), [community trait documentation](https://wiki.unofficial.voyage/mechanics/traits). These document the schema; they are not a guarantee of every live AI interpretation.
