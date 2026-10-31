# Alpha 14 — Portal Hub and Dungeon Enemy Groups

External return portals now consistently end at **Evertree Base - Portal Room**, the sole portal hub in Glowhaven. The Spider Realm has six finite enemy groups, two unique boss retainers and a fixed level-45 queen. Its map, passage challenges, free retreat and proof-item follow-up remain intact.

## Return portal repair

The playtest shows a narrated homecoming on turn 24 without the corresponding Travel Update. Subsequent narration treated the player as already in Glowhaven, while a later ordinary journey finally moved the location to Evertree Base. This is consistent with the old exact-area gate missing the crossing: the Silken router required Return Arch, although normal arrival at the parent Portal Room can select Arrival Floor. The transcript alone does not expose the saved area or trigger logs, so this is the identified code defect rather than a proven snapshot of the failed condition.

The return routers now accept an actual portal crossing from local staging areas. Explicitly entering the portal does not require the exact sub-area label. Bare “I enter” works in the unambiguous portal room, including the Silken arrival floor; it does not silently turn a market doorway into a portal trip. Entering a stair, future discussion or negation is not a crossing.

Drakenspire, Asterveil and the Silken return arch all apply the same fixed endpoint. Naming a desired alternative does not retarget that arch. The hub's outward routes still require their genuine destination keys and a selected route. The existing first-crossing anomaly remains one-time and affects only the actual outward crossing.

A state-phase backstop checks the same-turn return ledger and restores the exact hub location/area if a later native update contradicts the completed crossing. It expires with that turn, so it cannot recall a later chosen walk away from the hub. Returning needs no key, victory or debrief; it preserves the actual party and possessions.

## Dungeon population

| Encounter | Area | Opponents | Levels |
|---|---|---:|---|
| Entry watchers | Threadfall Upper Walk | 2 spiders | 18–19 |
| Bridge hunters | Tension Crossing | 3 spiders | 20–22 |
| Molting nest | Molting Alcoves | 2 lurkers | 19–20 |
| Brood span guard | Guarded Span | 3 arachne defenders | 22–25 |
| Winch nest | Lower Winch | 3 spiders | 23–25 |
| Gate guard | Matron Gate | 2 gatekeepers | 26–27 |

These are **fifteen separate native NPCs**, each with a fixed level, type, hostile initial relationship, area, health pool and actual persistent outcome. Once-only discovery hooks identify the existing groups; they do not create aggregate enemies, refill health or respawn a cleared pack. Roles, positions and warning signs differ. The entrance refuge and dry observation spaces remain useful, and a real bypass can avoid combat. The entire dungeon does not aggro as one encounter.

The queen's two unique retainers are:

- **Khessik Threadwarden, level 30, strong Arachne:** hooked spear bodyguard who interrupts a rush and protects the queen's flank.
- **Orruk Cindershell, level 28, average Cinder Carapace Spider:** vent-guard with short heat bursts, fire resistance and an ice vulnerability. The vent grants no free healing.

The existing boss-introduction trigger places and identifies both alongside Vhalessra Veyrath, using exactly ten effects. A dead retainer cannot be moved or revived. A real queen surrender need not require killing every surviving minion. Her native-health proof grant still works once and remains independent of the minions' deaths.

For future combat dungeons, the lore, encounter palette and encounter guidance now specify bounded packs, complementary roles, readable threats, persistent identities and useful retreat. This is scoped to authored dungeon exploration, not every cave, prison or ordinary city scene. Global random encounters remain disabled.

## Boss level and calibration

Vhalessra Veyrath is now **level 45, boss tier**, with healthMultiplier 1 and no added damage/reduction tuning. Her existing portrait, abilities, hostility and victory item are retained. Ordinary generated minions use the lower local bands; her explicit authored level remains 45.

I found no published universal rule saying a player at level X should face a boss at level Y. The [community NPC reference](https://wiki.unofficial.voyage/world/npcs) documents separate level, tier and difficulty effects: boss tier multiplies derived health by 1.7, damage by 1.35, and supports 2–3 tactical intents. Our local HP settings are 12 per level plus 66. Without an authored hpMax or extra multipliers, that gives:

| Queen level | Medium baseline HP | Hard encounter HP |
|---|---:|---:|
| 45 | about 1,030 | about 1,288 |
| 54 | about 1,214 | about 1,517 |

These calculations are a comparison of configured inputs, not a live balance test. Level 54 has roughly 18% more derived HP than 45, alongside a higher level-derived damage component. Adding retainers also changes action pressure substantially. The level-100 developer body with maximum skills and enormous resources is not evidence of fairness for an ordinary level-20 character.

Level 45 therefore implements the requested **dangerous optional party boss**. Finding the realm at level twenty is access to the investigation, not a promise of a safe solo fight. Warnings before the chamber, cover, retreat, preparation and willing companions are intentional. Exact party-size/build recommendations still require normal-stat playtests; no invulnerability, forced loss or fake level cap was added.

## Supported mechanics and limits

The [trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents item grants, named NPC placement, persistent state and movement effects. It does not document a general spawn-from-type effect. Consequently, this finite dungeon uses authored native enemy records and actual placement/discovery effects. The [encounter palette](https://wiki.unofficial.voyage/other/encounterElements) supplies generation ingredients; it is not a mechanical population command. These are community-maintained details. The official [Expanded Beta release](https://voyage.io/releases/expanded-beta) describes map and discovery improvements without providing a boss-level recommendation.

The duplicate matron-objective lines visible in the playtest were also cleaned up: native defeat/surrender records resolution, while the single proof watcher owns the objective update and trophy grant. The native boss death countdown may continue after zero health; no repeated finishing blow is required for the proof.

## Delivery

Use **GlowhavenAlpha14 - Portal Hub and Dungeon Packs.json**. It is identical to the canonical WorldAlpha - World.json; the standalone sections and readable AI are synchronized. There are now **147 NPCs, 173 locations and 134 general triggers**. All existing image URLs, map coordinates, unrelated NPCs, quests, progression and resources are preserved. The Alpha 13 map needs no replacement.

Local checks and simulations are recorded in the companion validation report. They do not certify a live Studio import, model behavior or combat balance. Import the complete world and start a fresh game; an existing run is not migrated. See the live checklist for portal staging-area returns, normal-stat group encounters and boss-party testing.
