# Glowhaven Alpha 7 — NPC Levels, One-Time Anomaly and Teaching Subjects

2026-10-28. Complete export: **GlowhavenAlpha7 - World.json**, identical to **WorldAlpha - World.json** after packaging. Baseline: the current Alpha 6 working world. The repeated transcript supplied after the usage interruption is byte-identical to the earlier transcript. Work continued in the same staging folder; the new chat/curriculum requests were added to that revision.

## NPC level generation

The level-87/1110-HP report matches the existing 12-per-level + 66 health settings. Four regions lacked NPC generation ranges. Added fallback ranges to all five regions:

| Region | Generated level band |
|---|---:|
| Glowhaven | 1–30 |
| Drakenspire Highlands | 8–45 |
| Asterveil Skies | 5–40 |
| Silken Chasm | 18–26 |
| Wraith Island Custody District | 10–55 |

Locations can narrow or override those bands. Villages use 1–20; many shops/public interiors use 1–25; the three main transit hubs use 8–30. Academy generation permits trained staff up to 55; security and genuinely dangerous sites have higher bands. The early Silken route rises from 18–22 at entry/upper galleries toward 22–26 at the boss chamber. These bands constrain unpinned generated levels, not the explicit authored roster. The Great Sage remains 100, Archons 85, headmasters 70, professors 50 and named students 15. Global HP scaling is unchanged.

New-NPC guidance also distinguishes ordinary work from veteran training, uses sensible tiers and avoids inflated explicit health. It cannot retroactively repair characters already generated in an old save. The documented band behavior and the local calculation tests require a fresh-game generation check in Voyage.

## Surprise crossing and the discovered room

The first actual ordinary Evertree crossing to Drakenspire or Asterveil is interrupted if at least one active **player** is level 20 or above. Standing in the room, inspecting an arch, possessing a key or traveling with a high-level NPC does not count. Genuine route-key possession and the chosen actual crossing still matter. This works for a solo character, a mixed-level player party and the level-100 developer; academy enrollment, examination acceptance and a briefing are not gates.

Both normal travel handlers and the immediate explicit-command handler set the same persistent incident flag during the actual displacement. Later normal travel remains available and cannot trigger it again. The first-arrival onboarding and key-grant triggers are explicitly **non-recurring**. Ordinary travel routers remain reusable because players still need to cross those routes again.

The old Stranded Threshold location is now **Silken Portal Room**, an enclosed ruined chamber with an arrival floor, visible Return Arch and a descent stair. All relevant IDs, paths, quests, scripts and prose references are updated together; its map coordinates and connections are retained. Travelers arrive together with their possessions. The room offers an immediately usable route to Glowhaven, with no boss, key, briefing or descent requirement.

## Key and investigation timing

The **Silver Web Portal Key now manifests on first arrival**, rather than first return. Its one-time typed item grant targets players missing a copy. The first discovery also makes **Silver Threads Below** available in the new room. The player can accept the investigation or leave immediately. The discovered route can subsequently be selected from the existing Evertree Portal Room with the reusable key.

Returning grants no second silver key. Losing it does not remove the free home arch. Existing legitimate replacement handling remains separate from crossing. Discovery does not count as defeating the matron or reporting findings. Portal command handling also recognizes the two supplied physical-action wordings with quoted speech, including the clear Dragonspire typo, while quoted movement alone, inspection, negation and conditional plans remain noncrossings in the local tests.

## Field test and expedition separation

The routine level-twenty field-test notice and briefing encourage ordinary travel. They do not arm a gate, predict a displacement or tell a traveler a historical copy of this incident happened before. Removed the developer arming command and the old compulsory examination-report step.

On actual return, any already offered or accepted field-test sitting is archived as **cancelled and postponed**. No field test is passed, no XP or graduation is awarded and no replacement date is invented. A player who never had the notice is not assigned a new field-test quest merely to cancel it.

The documented quest states/effects have no distinct cancellation effect. For a live offered/accepted record, this implementation uses a completed administrative-closure entry whose objective and outcome explicitly say cancellation/postponement. An offered record passes through accepted only to archive it; that bookkeeping does not represent consent to undertake a new exercise. Hidden, rejected, abandoned and previously completed records keep their existing status. The closure flag prevents reopening the old sitting.

**Beyond Glowhaven: An Authorized Expedition** and all four of its trigger definitions are unchanged. An actual authorized expedition can remain in progress through the anomaly, return home, resume normal travel, complete its real distant fieldwork and debrief. The Silken realm itself grants no expedition credit. A dedicated local fixture exercises that whole continuation.

## Named boss and removed stalker

Renamed the matron to **Vhalessra Veyrath**, a non-Japanese arachne identity. She remains the actual authored person in Widow's Crucible, with the existing appearance, temperament, motives and five combat descriptions. Added the reusable **Arachne** type; no universal armor immunity or new affinity is introduced.

Her encounter is now **level 24, boss tier, healthMultiplier 1.0, initialRelationship -85**. The former level 38 and 1.5 health scalar were excessive for an early level-20 route. Under neutral difficulty, the current documented health formula gives about **602 HP** before UI rounding. This is a fixed early-arc boss, not a boss rescaled to a level-100 developer. She has no extra damage reduction or damage bonus. Actual defeat and achieved surrender remain valid, while a friendly remark does not resolve hostile control. This is a calibration proposal implemented in data, not a claim of live combat balance.

Removed **Silverthread Stalker** from the roster. Its portrait slot was empty. The gallery now uses terrain/web hazards and optional type-backed creature encounters; its route trigger no longer requires an invented stalker or a kill. Existing bypasses and cleared states remain valid.

## Faculty subjects

| Academy | Magic Theory | Other subject | Other subject |
|---|---|---|---|
| Phoenix Wing | Haruki Saitō | Magical Combat — Ritsu Kurogane | Potions & Alchemy — Ranka Kagari |
| Gryffin Tail | Kei Aoki | Magical Engineering — Sōichirō Takamine | Magical Arts — Ririka Kujō |
| Dragon Hoard | Noriaki Takatsuki | Spellcraft — Madoka Narukami | Magical Creatures — Genzō Iwakura |
| Hydra Head | Kana Fujimoto | Enchantment — Reon Fujisaki | Herbology — Kaoruko Hanazono |

There are exactly three appointed core professors per academy, including one Magic Theory teacher. Assignments use teaching strengths, method and institutional opportunities, not automatic affinity-to-department conversion. Their existing affinities, numerical combat values, equipment, portraits and abilities are preserved.

Updated public role text, the faculty profiles, academy service descriptions, relevant classroom notices, core-subject lore and enrollment guidance. The courses supply actual lesson contexts using existing learning/skill systems; no new unsupported course fields, automatic mastery, extra professors or timetable system are added. In particular, a Nature-affinity professor can teach general theory, and an Arcane-affinity professor need not run an Arcane-only class.

## Chat and prompt-scope cleanup

Removed the five fixed named voice examples from direct NPC chat. Also removed personal examples/private facts from eight other general procedure blocks, replacing them with speaker/actor-specific rules. Canonical names remain in the dedicated roster lookup and in actual world records where identification requires them. The current general-procedure scan permits that lookup while rejecting unrelated authored-person examples elsewhere.

Repaired the confirmed `Gen'ichirō Mizuhara’ichirō` corruption in Ririka Kujō, Kei Aoki and Sōichirō Takamine's private records. The full explanation, evidence, distinctions and future checklist are in **Alpha7 - Prompt Scope and Curriculum Audit.md**. These prompt changes reduce avoidable context leakage; they do not guarantee that a runtime model never invents a fact.

## Preservation, checks and live limits

The result has **130 NPCs, 48 students, 62 NPC types, 13 starts, 28 quests, 79 general triggers, 21 party quest triggers, 17 factions, 5 realms, 5 regions, 97 locations and 364 areas**. The roster retains its order apart from the requested stalker removal and the matron's exact identity rename. The stable overview, narrator style, remaining starts, attributes, skills, progression, HP/MP, character creation, premades, game modes, music and name filters are unchanged. Faculty changes are confined to curriculum/work prose and verified reference repairs; their mechanics and appearance are intact.

All **261 nonempty image URLs** are preserved. The only removed media field was the stalker's empty portrait slot. Location identity changes preserve the existing map geometry, paths and media values. Standalone sections and readable copies are synchronized when packaged; previous current files are backed up under `backups/2026-10-28-before-alpha7/`.

Local structural/reference/size/preservation checks and **92 fixtures passed**. These include actual configured scripts in a Node VM, parser cases from the transcript, threshold levels, both outbound routes, no-briefing/developer/multiplayer cases, one-shot discovery, free retreat, cancellation, boss outcomes, expedition continuation and curriculum/chat guards. Typed effects are mocked and semantic decisions are supplied; documented level/HP tests model the reference behavior. This is not a live Studio validation, generated-NPC observation, combat balance test or saved-game migration.

Fresh-game priorities: meet an incidental worker with the developer, cross an ordinary route without a briefing, check the changed realm/location and first-entry key/quest, return and cross normally, verify the cancelled test gives no expedition credit, and attend one broad Magic Theory lesson with a professor whose affinity differs from the course's scope.

## Research basis

Current community references: [NPCs](https://wiki.unofficial.voyage/world/npcs), [Regions](https://wiki.unofficial.voyage/world/regions), [Locations](https://wiki.unofficial.voyage/world/locations), [Other Settings](https://wiki.unofficial.voyage/other/otherSettings), [Quests](https://wiki.unofficial.voyage/world/quests), [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions). These are unofficial schema/behavior documentation, not independent proof of the live engine. Observed local examples: Luxcellia uses regional bands and a different HP curve, while ChikaraOld uses the same 12/66 settings without a regional band. The reference worlds demonstrate choices, not a single automatically correct balance.
