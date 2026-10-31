# Current release — Crime and Creation, 31 October 2026

Import [Schools of Magic - Crime and Creation - Start Fix.json](Schools%20of%20Magic%20-%20Crime%20and%20Creation%20-%20Start%20Fix.json), identical to the legacy-named WorldAlpha - World.json. Based on the author's newest export, preserving supplied images, geometry, soundtrack, level-150 progression, resources and equipment settings.

See [copyable public patch notes](Crime%20and%20Creation%20-%20Patch%20Notes.md), [development notes and live tests](Crime%20and%20Creation%20-%20Development%20Notes.md), and [five supporting character cards](Crime%20and%20Creation%20-%20Character%20Cards.md).

Adds the narrow solo Crime/Prison loop, optional ancestry/portrait choices, four summoned openings and a first-spell quest. Local checks passed: 15,653 structural/reference/preservation checks, 385 mechanics fixtures and 164 script compilations. No live Studio import or gameplay test. All 23 section replacements match the release. Studio-reported start key/name mismatches are repaired; the shared validation guard now requires exact agreement, and eight references were migrated. Historical instructions below remain as release history.

# Historical release: Alpha28

Import **GlowhavenAlpha28 - Milestone Traits and Equipment.json**, identical to **WorldAlpha - World.json**. See [Alpha28 patch notes](Alpha28%20-%20Milestone%20Traits%20and%20Equipment%20Patch%20Notes.md). Earlier release instructions below are historical; keep their exports as rollback snapshots.

# Current canonical export: Alpha27 — Quest Condition Schema Fix

Use `GlowhavenAlpha27 - Quest Condition Schema Fix.json`, identical to `WorldAlpha - World.json`. Repairs eight invalid completionCondition shapes from Alpha25/26. Preserves every image/coordinate and all Alpha26 features. All116 quests checked against the typed condition union; all21 section maps match. See `Alpha27 - Quest Condition Schema Fix Patch Notes.md`. Live Studio import remains to verify.

# Historical export: Alpha26 — Site Danger and AuthorSeeds

Use `GlowhavenAlpha26 - Site Danger and Author Seeds.json`, identical to `WorldAlpha - World.json`. Preserves the latest supplied twelve NPC portraits, 59 location image objects and six coordinate values while keeping Alpha25’s first-day and appearance update. Adds sixteen focused AuthorSeeds, fifteen place archetypes and concrete on-site risk at 37 existing locations. Travel encounters remain disabled. See `Alpha26 - Site Danger and Author Seeds Patch Notes.md`, `On-Site Danger Catalogue - Alpha26.md` and `../research/NPC Author Seeds - Research and Revamp.md`. Live generation testing remains.

# Historical export: Alpha25 — First Days and Appearance

Use `GlowhavenAlpha25 - First Days and Appearance.json`, identical to `WorldAlpha - World.json`. Adds optional appearance traits, removes Space from creation, rewrites four student welcomes and four instructor inductions, and aligns first-day quests and morning timetables. See `Alpha25 - First Days and Appearance Patch Notes.md`, `Opening Scenes - Alpha25.md`, and `Character Creation Guide - Alpha25.md`. Existing images, maps, combat and unrelated event systems are preserved. Fresh-game testing remains.

# Historical export: Alpha24 — Character Creation and Relationships

Use `GlowhavenAlpha24 - Character Creation and Relationships.json`. Includes the Alpha22 text cleanup and Alpha23 quest revamp. See `Character Creation Guide - Alpha24.md`, `Alpha24 - Character Creation and Relationships Patch Notes.md`, and `Guild Offer Writer Verification - Alpha24.md`. Fresh-character and live relationship testing remain.

# Historical export: Alpha23 — Quest Resolution Revamp

Use `GlowhavenAlpha23 - Quest Resolution Revamp.json`. Includes Alpha22 text cleanup. See `Alpha23 - Quest Resolution Patch Notes.md`, `Quest Resolution Catalogue - Alpha23.md`, `Runtime Text Audit - Alpha22.md` and `Quest Systems Review - 2026-10-29.md`.

# Historical export: Alpha22 — Runtime Text Cleanup

Use `GlowhavenAlpha22 - Runtime Text Cleanup.json`. See `Runtime Text Audit - Alpha22.md` and `Quest Systems Review - 2026-10-29.md`. Quest and trigger behavior was preserved pending discussion.

# Historical export: Alpha21 — Asterveil Population

Use `GlowhavenAlpha21 - Asterveil Population.json` (identical to `WorldAlpha - World.json`). Twelve NPCs and twelve portraits added; 205 NPCs total. See `Asterveil - Character Cards.md`, `Asterveil - Population and Placements.md`, `Asterveil - Portraits.md`, and `Alpha21 - Asterveil Population Patch Notes.md`.

# World Draft

Storage maintenance: historical text is losslessly compressed and two redundant download ZIPs were removed after verifying every member remains available. Current world data and unique artwork are unchanged. See [storage report and working rules](../maintenance/Storage%20Maintenance.md) for the audit and bundle-recovery instructions.

## Current export — Alpha20 Questlines and Academy Life

Use [GlowhavenAlpha20 - Questlines and Academy Life.json](GlowhavenAlpha20%20-%20Questlines%20and%20Academy%20Life.json), identical to WorldAlpha - World.json. Merged against the user's newest world with all 193 NPCs, uploaded portraits, maps and placements preserved.

Added 70 quests, for 112 total: paced academy milestones and ordinary school life, guild adventures and four recurring contract patterns, Drakenspire clan/mountain stories and Asterveil field adventures. The thesis is one practical capstone per playthrough. Existing portal/anomaly/dungeon/ability systems remain. See the [catalogue](Quest%20Catalogue%20-%20Alpha20.md), [authored briefs](Questlines%20-%20Authored%20Briefs.md), [patch notes](Alpha20%20-%20Questlines%20and%20Academy%20Life%20Patch%20Notes.md) and [live playtest notes](Alpha20%20-%20Live%20Playtest%20Notes.md).

Passed 7,598 local structural checks and 2,438 script/eligibility fixtures; no live Studio import or playtest. Eighteen standalone sections match. Full world import applies all matching quest, trigger, AI and local-hook changes.

## Historical export — Alpha19 Drakenspire Population

Use [GlowhavenAlpha19 - Drakenspire Cast.json](GlowhavenAlpha19%20-%20Drakenspire%20Cast.json), identical to WorldAlpha - World.json, for the complete population update. Full [NPC](WorldAlpha%20-%20NPCs.json) and [Faction](WorldAlpha%20-%20Factions.json) section replacements are also supplied. The full import applies local scene/lore changes, the Yeti type retirement and rare encounter hooks too.

Added 52 authored characters, 18 major and 34 minor, with complete [cards](Drakenspire%20-%20Character%20Cards.md), [placements](Drakenspire%20-%20Population%20and%20Placements.md), [relationships/situations](Drakenspire%20-%20Relationships%20and%20Situations.md), [rare-contact notes](Drakenspire%20-%20Rare%20Encounter%20Notes.md) and [patch notes](Alpha19%20-%20Drakenspire%20Population%20Patch%20Notes.md). The roster now has 193 NPCs. [Portrait status and outputs](Drakenspire%20-%20Portraits.md) are tracked separately; new PNGs need hosted upload. All previously supplied images and map coordinates are preserved, including the latest two retainer portraits.

Passed 5,478 local structural checks and 1,906 script/eligibility fixtures; no live import or playtest. All 480 abilities, traits, resources and unrelated gameplay are unchanged. The reusable [Population Creation Guide](../research/Population%20Creation%20Guide.md) supplements the existing character and portrait templates.

## Historical export — Alpha18: Complete Ability Catalogue

The requested section replacements are [WorldAlpha - Abilities.json](WorldAlpha%20-%20Abilities.json) and [WorldAlpha - Traits.json](WorldAlpha%20-%20Traits.json). Import Abilities first, then Traits. They are plain section maps matching the Studio section format. The synchronized full world is [GlowhavenAlpha18 - Complete Ability Catalogue.json](GlowhavenAlpha18%20-%20Complete%20Ability%20Catalogue.json), identical to WorldAlpha - World.json.

Completed 480 abilities: 360 spells (18 per public discipline), 64 martial/tactical techniques, 40 mixed and 16 Magitech. All original 35 records are unchanged. The nineteen existing magical studies and three combat-training choices each grant two eligible basic techniques; the developer kit includes the complete catalogue. Space remains advanced, Time has no public abilities, and skill-acquisition/affinity-creation settings are unchanged.

[Complete index](Ability%20Catalogue%20-%20Complete%20Index.md), [full cards](Abilities%20-%20Readable.md), [starter pairs](Starting%20Studies%20and%20Training.md) and [patch notes](Alpha18%20-%20Complete%20Ability%20Catalogue%20Patch%20Notes.md) accompany the export. Passed **8,648 local structural checks and 1,872 script/eligibility fixtures**. No live Studio import or balance playtest was performed. Only abilities and specific trait repertoire/text fields changed; images, NPCs, maps, AI, resources, quests and triggers are preserved. Existing saves are not migrated.

## Historical export — Alpha17: Arcane and Guarded Abilities

Use [GlowhavenAlpha17 - Arcane and Guarded Abilities.json](GlowhavenAlpha17%20-%20Arcane%20and%20Guarded%20Abilities.json), identical to WorldAlpha - World.json. Batch one implements 18 Arcane spells and eight purely physical guarded techniques; Arcane Stitch is preserved, so 25 new entries bring the total to 35. Arcane Studies and Guarded Training each grant two basic moves. Existing NPCs, uploaded artwork, maps, positions, quests, triggers and acquisition settings are preserved.

[Batch cards](Ability%20Batch%2001%20-%20Arcane%20and%20Guarded%20Combat.md), [patch notes](Alpha17%20-%20Arcane%20and%20Guarded%20Abilities%20Patch%20Notes.md), [current 480-ability plan](Ability%20Catalogue%20-%20Implementation%20Plan.md) and [skill-learning research](Skill%20Learning%20and%20Affinity%20Creation%20-%20Research.md) accompany the export. Fourteen of eighteen Arcane spells are eligible by skill 59; further batches prioritize early/middle options too. The later one-to-three affinity menu and instruction-based skill acquisition are researched, not activated here.

Passed **1,023 local structural/reference/preservation checks and 224 script checks/fixtures**. This is not a live Studio import or balance playtest. Native requirements, bonuses and cooldowns are authored; costs, restoration, targets and tactical effects are AI-interpreted. Test a fresh game, especially starter grants, ward timing, construct action use and Quiet Meridian’s modest recovery. Existing saves are not migrated. Next planned batch: Fire and Force Combat.

## Historical export — Alpha16: Magic Foundation and Cast Fixes, 2026-10-28

Use [GlowhavenAlpha16 - Magic Foundation and Cast Fixes.json](GlowhavenAlpha16%20-%20Magic%20Foundation%20and%20Cast%20Fixes.json), identical to WorldAlpha - World.json. This merges the latest supplied export and preserves all 16 uploaded-image/map-position changes. It defines 20 public disciplines plus reserved Time, merges Magitech, clarifies mandatory Spellcraft invention and adds Stamina with natural Health/Mana names. No new spell batch is imported: the existing ten abilities remain.

Vhalessra, Kharvess and the revised male arachne staff-caster Orrhask share the boss room. The retainers are explicitly hostile and have new local portraits awaiting upload. The lawyer is now Ryōichi Naruse, with his exact uploaded portrait retained. Dusklamp Quarter and its four areas are removed; other map images and positions remain unchanged.

[Discipline guide](Magic%20Disciplines%20and%20Combat%20Foundation.md), [360-ability proposal](Ability%20Catalogue%20-%20360%20Proposal.md), [research decisions](Magic%20and%20Combat%20-%20Research%20Decisions.md), [patch notes](Alpha16%20-%20Magic%20Foundation%20and%20Cast%20Fixes%20Patch%20Notes.md) and [retainer portraits](Silken%20Retainers%20-%20Portraits.md) accompany the export.

Passed **8,439 local structural/reference/preservation checks and 181 script checks/fixtures**. This is not a live Studio import or combat playtest. Time has no documented native hidden/locked-skill flag; its learning restriction and the Spellcraft invention gate depend on AI guidance. Test the resource migration and invention flow in a fresh game. Existing saves are not migrated.

## Historical export — Alpha 15: Guild and Court, 2026-10-28

Use [GlowhavenAlpha15 - Guild and Court.json](GlowhavenAlpha15%20-%20Guild%20and%20Court.json), identical to WorldAlpha - World.json. This merges the latest user export, preserving its prison map and 28 edited coordinates. It adds eight court characters, Komugi Hanabishi and the Adventurer’s Guild with its seven-area hall, story start, exam, four badge ranks and initial contracts. Ordinary Silken packs now use type-based encounter requests rather than fifteen prewritten NPCs. The sigil reads naturally; its actual possession gates the one-time bazaar Easter egg.

Current totals: 141 NPCs, 174 locations, 714 areas, 42 quests and 169 general triggers. [Patch notes](Alpha15%20-%20Guild%20and%20Court%20Patch%20Notes.md), [character cards](Court%20and%20Guild%20-%20Character%20Cards.md), [artwork](Court%20and%20Guild%20-%20Artwork.md) and [live tests](Guild%20and%20Court%20-%20Playtest%20Scenarios.md) document the update. Nine PNG portraits and one guild interior await manual upload; existing hosted artwork is preserved.

Passed **8,145 local structural/reference/preservation checks and 174 script checks/fixtures**. This is not a Studio import or live playtest. Encounter hooks request NPC generation through supported story effects; no direct spawn-from-type effect is documented. Generated counts, personal exam recipients and procedural guild contracts need live verification. Start a fresh game after full import; old saves are not migrated.

## Historical export — Alpha 14: Portal Hub and Dungeon Packs, 2026-10-28

Use [GlowhavenAlpha14 - Portal Hub and Dungeon Packs.json](GlowhavenAlpha14%20-%20Portal%20Hub%20and%20Dungeon%20Packs.json), identical to WorldAlpha - World.json. Every external return arch ends at Evertree Base - Portal Room. Explicit portal entry works from local staging areas, and a same-turn state backstop protects the fixed landing. The Silken Descent now has six finite native enemy groups and two unique boss retainers. Vhalessra Veyrath is level 45; this is a dangerous optional party encounter, with retreat and preparation intact.

There are 147 NPCs, 173 locations and 134 general triggers. Your existing image URLs, map positions and Alpha 13 map art are unchanged. [Patch notes](Alpha14%20-%20Portal%20Hub%20and%20Dungeon%20Packs%20Patch%20Notes.md) include the encounter roster and documented HP comparison; [live checks](Portal%20Hub%20and%20Dungeon%20Packs%20-%20Playtest%20Scenarios.md) cover portal behavior and normal-stat party balance.

Local verification: **6,644 structural/reference/preservation checks and 195 script checks/fixtures passed**. This is not a live Studio import or balance playtest. Import the complete world and start a fresh game. The prior complete baseline and earlier non-derived reports are retained in authoring/portal-packs-2026-10-28.

## Historical export — Alpha 13: Silken Descent Revamp, 2026-10-28

Use [GlowhavenAlpha13 - Silken Descent Revamp.json](GlowhavenAlpha13%20-%20Silken%20Descent%20Revamp.json), identical to WorldAlpha - World.json. The Spider Realm has four distinct chambers across two vertically adjacent regions. Two earned passages and one route guard prevent direct lower-room jumps while preserving free retreat, cleared-room revisits and the existing boss/reward/follow-up mechanics. The old warrens and reliquary are now side areas.

The [map folder](maps/Silken%20Descent%20Alpha13) contains the 627 × 1254 full map, two 627 × 627 region tiles, pin CSV and import guide. Upload those tiles in Studio before a fresh-game test. All other map images, coordinates and characters are retained. See [patch notes](Alpha13%20-%20Silken%20Descent%20Revamp%20Patch%20Notes.md) and [live tests](Silken%20Descent%20Revamp%20-%20Playtest%20Scenarios.md).

Local verification: **4,771 structural/reference/preservation checks and 98 script checks/fixtures passed**. The suite includes script compilation as well as simulated movement, passage, portal and reward cases. It does not certify live Voyage timing or narration. Existing saves are not migrated. The current world contains 130 NPCs, 173 locations, 707 areas, 9 regions and 127 general triggers.

## Historical export — Alpha 12: Silken Boss Fix, 2026-10-28

Use [GlowhavenAlpha12 - Silken Boss Fix.json](GlowhavenAlpha12%20-%20Silken%20Boss%20Fix.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). Vhalessra Veyrath intercepts intruders at the Crucible entry. Native defeat grants the exact Matron's Anchor Sigil through a mechanical reward watcher without depending on the map label, journal entry or an AI death verdict. Genuine surrender still works. The existing later Ryūka Marufuji confrontation retains its proof gate.

All other characters, media and map coordinates are preserved. The world has 130 NPCs, 175 locations and 128 general triggers. See [patch notes and defect analysis](Alpha12%20-%20Silken%20Boss%20Fix%20Patch%20Notes.md) and [live checks](Silken%20Boss%20Fix%20-%20Playtest%20Scenarios.md). The broader dungeon traversal pass remains separate.

Local verification: **5,722 structural/reference/size/preservation checks and 233 simulated fixtures passed**. This is not a Studio import or a live playtest. Test a fresh game; this world export does not migrate an existing save. The single prior full baseline is in authoring/silken-boss-fix-2026-10-28/world-baseline.json; prior non-derived reports are beside it in previous-documents.

## Earlier exports

## Historical export — Alpha 11: Ryūka Rivalry, 2026-10-28

Use [GlowhavenAlpha11 - Ryuka Rivalry.json](GlowhavenAlpha11%20-%20Ryuka%20Rivalry.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). Ryūka Marufuji is the approved green-eyed, platinum-haired second-year Dragon Hoard student from the portrait chat. She occupies the replacement roster slot; the academy still has twelve students and the full roster 130 NPCs. Her actual local portrait is ready for Studio upload; the retired student's hosted portrait is not reused.

The recorded Silken victory grants Matron's Anchor Sigil once, including genuine nonlethal victory. Holding it later in Four Sages Bazaar starts her confrontation once, preserving prior acquaintance. Two optional quests support practice, an exhibition, real favoritism and freely chosen future company. No fixed romance, forced duel, trophy seizure or recruitment is added. See [patch notes](Alpha11%20-%20Ryuka%20Rivalry%20Patch%20Notes.md) and [live checks](Ryuka%20Rivalry%20-%20Playtest%20Scenarios.md).

The world contains 130 NPCs, 36 quests and 127 general triggers. Maps, coordinates, Asterveil content, other NPCs and all other images are retained from the latest current working file. Relevant student years, placements, relationships and forward-looking story notes are cleaned up. Older named exports, batches and authoring snapshots below are historical and must not be used to recreate the retired character.

Local checks: **4,775 structural/reference/size/preservation checks and 190 fixtures passed**. These are simulated engine effects with supplied semantic outcomes, not a live Studio import or playtest. Use the complete import and a fresh game; existing saves are not migrated. Standalone canonical sections match the full file. Previous working files and references are backed up in backups/2026-10-28-before-alpha11-ryuka.

## Historical notes

The sections below describe earlier snapshots and their then-current roster, geography and results.

## Historical export — Alpha 10: Asterveil, 2026-10-28

The latest supplied full export adds hosted map images to all four Asterveil regions and updates the coordinates of 20 Asterveil locations. The two full-world copies, standalone regions and locations, and placement tables are synchronized. See [Latest World File Sync Report](Latest%20World%20File%20Sync%20Report.md).

Use [GlowhavenAlpha10 - Asterveil.json](GlowhavenAlpha10%20-%20Asterveil.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). Built on the current Alpha 9 AI Systems file, it develops Asterveil into **four regions / 28 locations / 122 areas** using the author's selected four-cluster map. This is a midgame realm: regional bands **10–25, 20–35, 30–45, 40–55**, with lower hub bands and one exceptional **55–60** site. No premade NPC is added.

Read [patch notes](Alpha10%20-%20Asterveil%20Patch%20Notes.md), [realm lore](Asterveil%20-%20Realm%20Lore.md), [location catalogue](Asterveil%20-%20Location%20Catalogue.md), [creature types](Asterveil%20-%20Creature%20Types.md), [commissions](Asterveil%20-%20Commissions.md), and [map placement/routes](Asterveil%20-%20Map%20Placement%20and%20Routes.md). The coordinate CSV and placement manifest reflect the latest pin positions and include whole-image percentages for review. The supplied export now includes hosted region-map URLs; crop suggestions remain a planning reference.

The complete world now has **175 locations, 708 areas, eight regions, five realms, 94 NPC types, 25 factions, 34 quests and the same 130 premade NPCs**. Thirty new creature types and six local commission lifecycles support fieldwork. Existing cast, all 299 URL fields, other maps/coordinates, progression, starts and the one-time portal anomaly are preserved. The ordinary Asterveil portal now reveals its renamed entry region while keeping its fixed room endpoint.

**5,687 local checks and 161 script fixtures passed.** This is local validation with simulated engine effects and supplied semantic decisions, not live Studio validation, generated-creature quality or balance testing. The [playtest sheet](Asterveil%20-%20Playtest%20Scenarios.md) gives the next live checks. Use a fresh game.

Canonical standalone files and readable AI are synchronized. The full import is required for regional, type, quest and trigger changes. Prior working copies are in backups/2026-10-28-before-alpha10-asterveil.

## Historical notes

The notes below describe earlier snapshots and their counts, geography and test results at that time.

## Historical export — Alpha 9: AI Systems, 2026-10-28

Use [GlowhavenAlpha9 - AI Systems.json](GlowhavenAlpha9%20-%20AI%20Systems.json), byte-identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). This is built from the author's latest Downloads export, including the arranged Drakenspire map and latest portraits. Every coordinate, area path, NPC record, image URL, crop and original entity order matches that supplied export. The old Drakenspire grid is historical reference only.

All 18 AI tasks are revised. Setting-specific generation scaffolds replace generic presets. Four short planning reminders reinforce travel, practice, crafting and sparring. Two stale references to the renamed Drakenspire Portals location are repaired. Existing world lore, starts, factions, modes, progression and character systems remain as supplied.

Read the [patch notes](Alpha9%20-%20AI%20Systems%20Patch%20Notes.md), [reference comparison and design decisions](Alpha9%20-%20Luxcellia%20AI%20Comparison.md), and [live playtest scenarios](Alpha9%20-%20Playtest%20Scenarios.md). The complete import is required for all changes; the AI-only section omits generation scaffolds and triggers.

World totals remain **152 locations, 601 areas, 130 NPCs, 64 NPC types, 23 factions, five realms and five regions**. All **299 media URL fields / 292 nonempty URLs** are preserved. Local checks: **5,125 structural/reference/size/preservation checks and 115 fixtures passed**. These are local checks with simulated engine effects, not live Studio validation, model evaluation or a playtest.

Standalone sections are synchronized from this exact export. AI Instructions - Readable.md also includes the generation scaffolds. The previous working copies are backed up in backups/2026-10-28-before-alpha9-ai-systems; the two supplied exports and patch notes have immutable authoring snapshots. Use a fresh game to test changed world definitions.

## Historical notes

Everything below records previous releases. Their current-file, map-placement, count and test statements applied to those earlier snapshots.

## Historical export — Alpha 8: Drakenspire, 2026-10-28

Use [GlowhavenAlpha8 - Drakenspire.json](GlowhavenAlpha8%20-%20Drakenspire.json), byte-identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). This includes the author's image-updated world and expands Drakenspire to **60 locations / 253 areas**, compared with Glowhaven's 67 / 273. World totals are **152 locations, 601 areas, 130 unchanged NPCs, 64 NPC types, 23 factions, 5 realms and 5 regions**.

Read [update notes](Alpha8%20-%20Drakenspire%20Update%20Notes.md), [national lore](Drakenspire%20-%20National%20Lore.md), [location catalogue](Drakenspire%20-%20Location%20Catalogue.md), [map art brief](Drakenspire%20-%20Map%20Art%20Brief.md), and [intended routes](Drakenspire%20-%20Intended%20Routes.md). Grid data is available as JSON and CSV. The 8-column grid is provisional and currently affects travel distances until the markers are rearranged.

All 289 nonempty media URLs and existing crops are preserved. Existing quests, portal/anomaly scripts, roster, starts, progression and global image prompts are unchanged. New regional NPCs and actual map art have not been created. Glowhaven is first in the realm list.

Local structural/preservation checks and 92 mechanics fixtures passed; this is not live Studio validation or a live playtest. Canonical standalone sections match the complete world. Backups are in backups/2026-10-28-before-alpha8-drakenspire.

## Historical notes

Everything below records earlier snapshots and their own counts and validation results. Their current-file statements applied at the time they were written.

## Current working draft — Drakenspire planning, 2026-10-28

The canonical **WorldAlpha - World.json** retains the latest 28 added location images and now includes the confirmed dragonkin anatomy/lore update. [Dragonkin Appearance Guide](Dragonkin%20Appearance%20Guide.md) supplements the read-only art guides. [Drakenspire Planning](Drakenspire%20Planning.md) contains the national-lore questionnaire and unapproved suggestions.

No regional expansion has been authored yet: Drakenspire remains 5 locations / 16 areas, while Glowhaven has 67 / 273. The intended next pass creates a comparable location catalogue on a temporary grid, after the author's answers. No new NPCs or map image have been created. Existing global image prompts, images, geography, quests and mechanics are preserved; two dragonkin appearance descriptions are aligned with the new canon.

World lore, NPC types, NPCs, AI and readable AI files are synchronized. The named Alpha 7 export is retained as the last complete image-updated snapshot before this planning/lore pass; it is no longer byte-identical to the current working draft. Local preservation/size checks passed. Custom-species portrait compliance is untested live.

## Prior published snapshots

The following notes describe earlier revisions at their publication time.

## Historical export — Alpha 7, 2026-10-28

The latest supplied full export adds establishing images to 28 locations. The matching standalone location section is updated; both current full-world files are exact copies of the supplied export. See [Location Image Sync Report](Location%20Image%20Sync%20Report.md).

Use [GlowhavenAlpha7 - World.json](GlowhavenAlpha7%20-%20World.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). See [Alpha 7 Update Notes](Alpha7%20-%20Update%20Notes.md), the [problem/scope report](Alpha7%20-%20Prompt%20Scope%20and%20Curriculum%20Audit.md), and [core subjects](Academy%20Core%20Subjects.md).

Generated NPC levels now have region/location bands. The first ordinary keyed portal crossing at player level 20+ can interrupt once, independently of a briefing. First arrival in Silken Portal Room supplies the new key and optional investigation; immediate return is free. The interrupted field-test sitting is postponed, while the separate authorized expedition keeps its own mechanics. Vhalessra Veyrath is the level-24, strongly hostile authored matron. Silverthread Stalker is removed.

All four academies now have three named core subjects, including Magic Theory, with appointments independent of affinity. Fixed personal examples/private facts are removed from general AI procedures; the dedicated roster lookup remains. Confirmed malformed name references are repaired.

Current totals: **130 NPCs, 48 students, 62 NPC types, 13 starts, 28 quests, 79 general triggers, 21 party quest triggers, 17 factions, 5 realms, 5 regions, 97 locations and 364 areas**. The subsequent image pass added 28 location establishing images. Core progression, skills, attributes, player resources, modes and the stable overview/narrator are unchanged.

Local structural/reference/preservation checks and **92 fixtures passed**. The scripts run locally with mocked typed effects and supplied semantic outcomes; this is not a live Studio or balance result. Existing generated save-state NPCs are not automatically repaired by editing world definitions. Use a fresh test game for the new lifecycle and level generation.

The canonical standalone NPC, AI, location, lore, faction, region, type and start files are synchronized. The full export applies the connected quest/trigger/location changes together. Backups are under backups/2026-10-28-before-alpha7. This remains Alpha 7 for testing and the author's image pass.

## Historical exports

Everything below describes earlier snapshots, including their own counts, behavior and test results. Their canonical-copy claims applied at publication time.

## Historical export — Alpha 6, 2026-10-28

Use [GlowhavenAlpha6 - World.json](GlowhavenAlpha6%20-%20World.json). [WorldAlpha - World.json](WorldAlpha%20-%20World.json) is its identical canonical working copy. See [Alpha 6 Update Notes](Alpha6%20-%20Update%20Notes.md) for the full changes and check limits.

This pass revises the stable world overview and quest-design brief, authors eleven fixed opening scenes, adds native Write Your Own, consolidates village starts in Brookmeadow, moves Random last and expands NPC types from 8 to 61. The friendly-reply event and its dependent tutorial chain are removed. Moltback Silkguard is now a type-backed local encounter rather than a fixed roster NPC.

Current totals: **131 NPCs, 48 students, 61 NPC types, 13 starts, 28 quests, 0 narrative events, 78 general triggers, 21 party quest triggers, 72 lore entries, 17 factions, 5 realms, 5 regions, 97 locations and 364 areas**. All 261 nonempty image URLs remain intact. All remaining NPC cards, combat and character systems, map geometry, and general trigger definitions are preserved.

Updated standalone NPC, AI, location and lore files match the complete world; new standalone Story Overview, Story Starts and NPC Types files and a readable opening collection are supplied. Existing standalone factions, realms, regions and game modes still match their unchanged sections. The complete world is needed to apply the event/quest/arc cleanup together.

Local structural/reference/preservation checks and 122 fixtures passed. This is not a live Studio validation or gameplay result. Native Write Your Own input, authored opening performance and type-backed encounter persistence need fresh-game checks. This remains alpha for the author's image pass.

## Historical revision notes

The sections below record earlier snapshots. Their references to a file being identical to the canonical copy, their counts and their test results apply at that revision's publication time, not to the current working copy.

## Historical Playtest One revision — 2026-10-27

Use [GlowhavenAlpha4 - Playtest One.json](GlowhavenAlpha4%20-%20Playtest%20One.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). The local Portals export was the confirmed baseline. The update addresses the author's first playtest and implements the later reusable-key design instead of a separate hidden portal room.

Three actual inventory keys control outbound portal routes. The first regional field examination comes due at level 20 for enrolled students; outsiders can volunteer and developers must explicitly request the test. A committed, accepted and briefed examination transit is displaced once into The Silken Descent. The entrance has an immediate return. First return grants the Silver Web key; normal travel remains available and the deeper matron investigation is optional.

There are **132 NPCs, 5 realms, 5 regions, 97 locations, 364 areas, 61 lore entries, 14 story starts, 29 quests, 75 general triggers and 34 item types**. The original 128 NPC identities, roster order, numerical combat values and all 268 media fields are retained. Their appearance is now in narrator-facing basicInfo; Reika's five approved abilities are restored. The six attributes, 42 skills, ten techniques and existing resource/progression settings remain.

The four school starts share enrollment and orientation. Merchant, three village choices, four employment starts, Random and a developer inspection start support other roles. Natural speech can use titles, surnames and honorifics while records keep canonical full names. Private production rules no longer appear in the affected public lore and descriptions.

See [Playtest One Review and Patch Notes](Playtest%20One%20Review%20and%20Patch%20Notes.md), [new cast review](New%20Cast%20-%20Playtest%20One.md) and [reference decisions and next checks](../research/Playtest%20One%20-%20Reference%20Decisions%20and%20Next%20Checks.md). Local structural/reference/preservation checks and 35 mocked script/lifecycle fixtures passed. No live Studio import, full platform validation or playtest was performed. New artwork is not supplied; use a new test game for these changed starts and definitions.

## Portals revision history — 2026-10-27

Use [GlowhavenAlpha3 - Portals.json](GlowhavenAlpha3%20-%20Portals.json), identical to [WorldAlpha - World.json](WorldAlpha%20-%20World.json). The main realm and map region are **Glowhaven**. Evertree Base now contains a Portal Room linking two authored destination maps: **Drakenspire Mountains** and **Asterveil Sky Archipelago**. New-region generation is disabled. The student expedition requirement now means leaving the entire Glowhaven region; local countryside and Wraith Island Prison do not count.

Current totals: **4 realms, 4 regions, 91 locations, 345 areas, 58 lore entries, 128 NPCs, 23 quests, 44 general triggers, 22 party quest triggers, 43 traits, 42 skills, 10 abilities and one developer premade**. Forty-one traits remain the ordinary creation catalogue; the extra two support developer setup. All 268 existing media fields and every existing NPC are retained. New destination imagery and casts are not yet authored.

**Developer Playtester** grants all actual skills/techniques, large HP/MP pools, testing funds and a runtime level/attribute setup to 100. It remains separate from normal creation choices. Naming now uses 261 token-appropriate filters; narrator guidance supports martial, occupational and noncasting play alongside magic. Normal character balance still needs ordinary saves.

See [Portals Patch Notes](GlowhavenAlpha3%20-%20Portals%20Patch%20Notes.md), [Alpha Missing Pieces](Alpha%20Readiness%20-%20Missing%20Pieces.md), and [research decisions](../research/Portals%20Naming%20and%20Narration%20-%20Implementation%20Notes.md). Local reference, preservation, naming, size and 19 script/lifecycle fixtures passed. No Studio import, full platform validation or live gameplay test was performed. Earlier sections below describe historical snapshots. Use a new test game for the changed quest key and definitions.

## Schools of Magic revision history — 2026-10-27

Use [GlowhavenAlpha3 - Schools of Magic.json](GlowhavenAlpha3%20-%20Schools%20of%20Magic.json), identical to the canonical [WorldAlpha - World.json](WorldAlpha%20-%20World.json). It uses the user's latest full-world attachment, including newer map changes, and merges the accepted Schools of Magic lore with the user's Dragon Hoard exploration-and-relics direction. Retired one-word academy creeds are replaced by civic mandates and institutional traditions.

Current totals: **128 NPCs, 81 locations, 313 areas, 54 lore entries, 23 quests, 39 general triggers, 22 party quest triggers, 42 skills, 41 traits, 10 abilities, 23 item types, two resources and two realms**. All **268 media URL fields** from the latest input are preserved. Six attributes and all level/check caps of 100 remain.

The gameplay additions are variable 1–3 MP passive recovery around the prior +2 mean, a chosen court-authorized expedition record, and official-tournament state. Five NPC ability/doctrine clarifications align existing characters with learned bodily Enchantment and trainable body casting; identities, affinities and power levels are retained. The standalone NPC, location, lore and game-mode files match the full world.

See [Schools of Magic Patch Notes](GlowhavenAlpha3%20-%20Schools%20of%20Magic%20Patch%20Notes.md) and [research and implementation](../research/Schools%20of%20Magic%20-%20Lore%20and%20Mechanical%20Implementation.md). Local preservation/reference/size checks and 15 mocked script/lifecycle fixtures passed. No live Studio validation, import, gameplay test or existing-save migration was performed. Earlier sections below are historical snapshots.

## Six-attribute revision history — 2026-10-27

Use [GlowhavenAlpha3 - Six Attributes.json](GlowhavenAlpha3%20-%20Six%20Attributes.json), identical to the canonical [WorldAlpha - World.json](WorldAlpha%20-%20World.json). Endurance is merged into Force; Guarded Combat uses Force. Attributes are Force, Finesse, Logic, Passion, Empathy and Intuition. The skill level cap, shared check-contribution cap and character level cap are 100. The magical groupings are unchanged.

This is a narrow consistency update. Two obsolete Endurance aptitude choices were removed, leaving 41 existing draft traits; other ability and creation design is unchanged and deferred. Roster, media, map, prison, quests, HP/MP and progression rates are preserved. Earlier reports describe historical snapshots. See [revision notes](GlowhavenAlpha3%20-%20Force%20Merge%20Patch%20Notes.md).

## Seven-attribute system history — 2026-10-27

Use [GlowhavenAlpha3 - Seven Attributes.json](GlowhavenAlpha3%20-%20Seven%20Attributes.json) for the complete current export. [WorldAlpha - World.json](WorldAlpha%20-%20World.json) is the identical canonical copy. This supersedes the earlier six-attribute polished export.

The current player system has **7 attributes**, **42 skills**, **43 creation traits** in **5 categories**, **10 learnable techniques**, and **23 item types**. All 18 magical disciplines use the user's approved approach mapping. HP/MP, progression, all 128 NPCs, all 267 existing media URLs, 81 locations, 313 areas and the circular prison layout are preserved. See [Seven Attributes Patch Notes](GlowhavenAlpha3%20-%20Seven%20Attributes%20Patch%20Notes.md) and [Implementation and Play Checks](../research/Seven%20Attributes%20-%20Implementation%20and%20Play%20Checks.md).

Local reference, field-shape, size, trait-arithmetic, technique-gating and preservation checks passed. This is intended for new games; no live import, Studio validation, AI-routing playtest or existing-save migration was performed. Earlier exports and logs below describe their own snapshots.

## Systems polish history — 2026-10-27

Use [GlowhavenAlpha3 - Polished.json](GlowhavenAlpha3%20-%20Polished.json) for the complete updated world. [WorldAlpha - World.json](WorldAlpha%20-%20World.json) is the identical canonical copy. This revision polishes AI, narrator style, naming, skills, HP/MP, factions, and story starts while retaining the corrected prison hierarchy and all NPCs and media.

Current system totals: **46 skills**, including **18 magical disciplines**; **2 resources**; **8 factions**; **5 story starts** (four academies and Random). All **128 NPCs**, **81 locations**, **313 areas**, **267 URL fields**, and **14 circularly arranged prison facilities** are preserved. See [Systems Polish Patch Notes](GlowhavenAlpha3%20-%20Systems%20Polish%20Patch%20Notes.md) and [Reference Decisions](../research/Systems%20Polish%20-%20Reference%20Decisions%202026-10-27.md).

Local structural, preservation, size, and reference checks passed. This revision has not been uploaded, validated in Voyage Studio, or playtested. The earlier named exports and update logs below describe their own snapshots; use the polished export for the current full file.

## Alpha3 prison layout history — 2026-10-27

The prison correction used the user's GlowhavenAlpha3.json baseline and is preserved in the current polished export. Wraith Island remains a location in Glowhaven; Wraith Island Prison is a realm containing 14 distinct facility locations arranged in a non-overlapping circle. No prison-named placeholder location remains. See [the fixed Alpha3 export](GlowhavenAlpha3%20-%20Prison%20Realm%20Fixed.json) and [layout patch notes](Alpha3%20-%20Prison%20Realm%20Layout%20Patch%20Notes.md). Current totals: 128 NPCs, 81 locations, 313 areas, 2 realms. All relevant standalone sections match the canonical full world.


## Latest NPC visibility correction — 2026-10-27

`WorldAlpha - NPCs.json` now uses `initialKnown` for all 128 NPCs and contains no legacy `known` fields. Nine leaders start visible: Ilyra Stillglass, the four Archons, and the four headmasters. The other 119 NPCs start undiscovered. Images, character text, stats, placements, and roster order are preserved. The embedded NPC section in the local full world matches this correction.

The subsequent Alpha3 prison restructure supersedes the earlier map-snapshot warning. The full world now uses GlowhavenAlpha3.json as its baseline and contains distinct prison facilities; it does not recreate the deleted single prison location. See `Alpha3 - Prison Realm Layout Patch Notes.md`.

## Canonical WorldAlpha files

- [WorldAlpha - World.json](WorldAlpha%20-%20World.json) — the complete Alpha world export.
- [WorldAlpha - Locations.json](WorldAlpha%20-%20Locations.json) — the complete standalone location file.
- [WorldAlpha - NPCs.json](WorldAlpha%20-%20NPCs.json) — the complete standalone NPC file.
- [WorldAlpha - World Lore.json](WorldAlpha%20-%20World%20Lore.json) — the organized World Lore section, ready to copy separately.

These are the user's latest files and are the active WorldAlpha sources from here on. The standalone sections match the current full world: 128 NPCs and 81 locations. Use the standalone files for individual section updates; refresh the embedded sections when preparing a new full-world export.

The current synchronized files contain **132 NPCs**, **97 locations**, **364 areas**, **61 lore entries**, **29 quests**, **34 item definitions**, **5 realms**, and **12 game modes**. There are **75 general triggers** and **22 party quest triggers**. Standalone NPC, location, lore, game-mode, realm and region sections match the full export. Use the Playtest One revision at the top for current details; earlier reports describe historical snapshots.

[Lore Update Report](WorldAlpha%20-%20Lore%20Update%20Report.md) records the preservation checks and the targeted corrections to the supplied Studio diagnostics. The exact original input is retained in [the backup](backups/WorldAlpha%20-%20Before%20Lore%20Update%202026-10-27.json).

## Reference material

- [base-world-v37.json](base-world-v37.json) — preserved community API seed; reference only, not an active world.
- [World Lore Draft Notes](World%20Lore%20Draft%20Notes.md) and [Character Creation Format](../research/Character%20Creation%20Format.md) remain supporting material.
- [validation-report.md](validation-report.md) records a community validation of an older prototype. It does not validate the current WorldAlpha files.

The WorldAlpha files have not been imported into Voyage Studio or playtested in this update.

## Location visibility history — 2026-10-27

Before the prison realm restructure, the standalone location section used the supplied location section, with `known` converted to `initialKnown`. It contains 63 initially known locations and five initially unknown locations: Wraith Island, Hermit's hut, Shadowspire, Wraith Island Prison, and Evertree Base. All other supplied fields, images, and location order are preserved. The original supplied section is retained in `backups/WorldAlpha - Locations Before initialKnown 2026-10-27.json`. The full-world location snapshot was subsequently refreshed by the current-files sync and now matches this standalone section. JSON parsing and content-preservation checks passed; this visibility change has not been tested in a live Voyage game.

## Minor-location cast — 2026-10-27

The latest academy placement pass uses the user's newer 128-NPC attachment. It distributes 68 academy NPCs across 38 existing campus areas, changing 45 placements and preserving all other supplied fields, portraits, roster order, and non-academy characters. See [Academy NPC Placement Report](Academy%20NPC%20Placement%20Report.md) for every group and its rationale. The canonical combined roster remains `WorldAlpha - NPCs.json`; the full-world NPC snapshot was subsequently refreshed by the current-files sync and now matches this standalone section. These are starting placements, with no recurring schedules installed.

Added 59 NPCs across 58 eligible locations, followed by 59 single-pass portraits in writing order. All 69 original NPC records are preserved. The academy and palace group, Shadowspire, and Hermit's hut were excluded; the palace group includes Stargarden Manor, Sage's Spire, and Evertree Base.

- [Illustrated cast gallery](npc-batches/minor-locations-2026-10-27/Cast%20gallery.html) — portraits, expandable full cards, and review notes. Contains narrator secrets.
- [Batch report](npc-batches/minor-locations-2026-10-27/Batch%20report.md) — scope, generation order, static checks, and portrait caveats.
- [NPC additions only](npc-batches/minor-locations-2026-10-27/NPC%20additions.json) — the 59 new entries; the combined roster remains `WorldAlpha - NPCs.json`.
- [Generation order and review flags](npc-batches/minor-locations-2026-10-27/generation-order.csv).
- [Exact portrait prompts and reviews](npc-batches/minor-locations-2026-10-27/portrait-prompts.json).

Every new PNG is saved in `npc portraits/` under the NPC's full name. Twenty-five images have recorded caveats, including borderline framing and subtle affinity cues. Céline Desrosiers has a major extra-hand defect. Results were retained without rerolling under the portrait guide's one-pass rule. No image uploads, Studio import, schema validation, or playtests were performed.

## Current files sync — 2026-10-27

Replaced the three canonical world, location, and NPC files with exact copies of the latest user attachments. Previous versions are preserved in `backups/Current Files Sync 2026-10-27 112738/`. See [Current Files Sync Report](Current%20Files%20Sync%20Report.md) for checks and scope. No Voyage Studio import, schema validation, or playtest was performed.

## Gameplay expansion history — 2026-10-27

The earlier gameplay-expansion snapshot added playable services and situations to 27 locations including the prison, 21 optional quests, an everyday marks economy, roster-first and richer scene guidance, and a separately represented Wraith Island Prison realm. All 128 NPC identities, portraits, placements, and 269 URL fields are preserved. Adult level/type metadata and five officers' combat capability received the documented cleanup. Existing geometry is retained; Wraith Island Prison now belongs to the new custody region. New prison areas extend its existing graph. Local preservation, reference, size, and fixture-based trigger checks pass. This is not a live Studio import, full schema validation, or a playtest. The full public schema download was refused by its host (HTTP 403).


## 2026-10-28 — AI overhaul and portal follow-up

Current complete export: [GlowhavenAlpha4 - AI Overhaul.json](GlowhavenAlpha4%20-%20AI%20Overhaul.json). Canonical working file remains WorldAlpha - World.json. [AI-only sections](WorldAlpha%20-%20AI.json) contain imagePromptConfiguration and aiInstructions; they do not install portal mechanics. [Comparison, changes and tests](AI%20Overhaul%20-%20Comparison%20and%20Patch%20Notes.md) explain scope and live checks. Older named exports remain snapshots.


## 2026-10-28 — Alpha 5

Current complete export: [GlowhavenAlpha5 - World.json](GlowhavenAlpha5%20-%20World.json), identical to WorldAlpha - World.json. Matching AI, NPCs, Locations, World Lore, Realms, Regions and Factions standalone files are synchronized. See [update notes](Alpha5%20-%20Update%20Notes.md) and [student years](Academy%20Student%20Years.md). The AI-only file cannot install portal/faction/profile changes. Earlier named exports remain historical snapshots.
