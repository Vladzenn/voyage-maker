# Beta playtest 2 - findings and changes

2026-10-30. Active import file: [WorldAlpha - World.json](../world-draft/WorldAlpha%20-%20World.json). The WorldAlpha filename remains a legacy repository name; the project is in Beta.

## Voice audit and restoration

The ten voices below were present in the user's latest supplied full export and two earlier supplied exports from 2026-10-30. They were absent in the active local full world and NPC section file. This was a merge omission, not evidence that the user had left these characters unassigned. Only their voice fields were restored from the latest user export; the current NPC biographies, placements, portraits and other fields were preserved.

| NPC | User-assigned voice |
| --- | --- |
| Ilyra Stillglass | female posh british |
| Akane Todo | female harsh commanding |
| Gen'ichirō Mizuhara | male deep calculating |
| Tōru Shizunami | male southern gritty |
| Reika Saionji | female soft flirtatious |
| Yūma Kurobane | male young charismatic |
| Miyabi Tsukishiro | female sly smooth |
| Ryūka Marufuji | female calm controlled |
| Vhalessra | female harsh commanding |
| Rovakthuun | male commanding gruff narrator |

Ritsu Kurogane keeps the previous update's female harsh commanding assignment, giving the active draft eleven pinned NPC voices. The latest supplied export has no custom worldVoices entries. Other NPCs have no explicit authored voice field in that export; this does not establish what a live save may have assigned during play.

The community [NPC reference](https://wiki.unofficial.voyage/world/npcs) distinguishes a stock voiceTag from a worldVoiceId override. The restoration checks both fields, rather than treating an empty worldVoices dictionary as proof that no voices were assigned.

## Location level ranges

Violet Thread explicitly contains npcLevelRange min 1, max 25. This is the band used for newly generated or level-less NPCs at that location; it is not a player entry requirement, a shop item tier, or a mandatory combat difficulty. NPCs with explicit authored levels retain them.

An absent location band falls back to its parent region. Glowhaven's regional band is 1-30. The current world has 173 locations: 132 have explicit bands and 41 inherit. These differences are permitted and no ranges were removed or fabricated during this pass. The map's presentation can make the band look like a recommended player level, but the JSON field itself concerns NPC generation.

Source: current local JSON and the community [Locations reference](https://wiki.unofficial.voyage/world/locations). This is schema interpretation, not a newly run gameplay test.

## Practice, studying and learning

The old action instructions already mentioned practice of an unowned skill, but another paragraph referred to a practiced skill and left room for safe practice to be treated as inconsequential. The new text explicitly makes dummy strikes, forms, defensive drills, instruction, a first magical attempt, and applied study attempts at the exact configured skill, including when the character does not yet own it. No enemy or combat stakes are required. Studying means exercises, analysis, transcription with understanding or testing knowledge, rather than merely holding a book.

Native skill settings changed:
- baseChanceToLearnNewSkill: 0.1 to 0.3.
- skillLearningBonusModifier remains 0.01.
- trainingCooldown: 10 to 5.
- newSkillGenerationEnabled remains false, preventing invented skill names while permitting acquisition of existing configured skills.

At attribute 10 the documented acquisition formula changes the eligible-attempt chance from 20% to 40%. At 15 it is 45%. These are probabilities when the engine registers an eligible attempt, not guaranteed acquisition within a set number of turns. Native XP, level results and cooldowns remain authoritative; the narrator must not invent a level-up or duplicate an XP award.

The supplied Luxcellia snapshot has trainingCooldown 5 but still base chance 0.1 and modifier 0.01. Kato's newer screenshot states a practice/learning hotfix; it is evidence of the creator's intent, not proof that the older supplied snapshot contains that live implementation. Glowhaven uses the supported settings and its own skill catalogue.

Sources: observed reference JSON; user-supplied patch-note screenshot; community [Skill Settings](https://wiki.unofficial.voyage/mechanics/skillSettings). Official [Patch 2.45.3](https://voyage.io/whats-new/patch/patch%3A100001203) confirms that untrained checks include the linked attribute modifier.

## Mana and Stamina recovery

User decision: retain explicit recovery items and techniques; normal recovery requires rest or a new day.

Removed gh_lore_variable_uptake, the trigger that added random 1-3 Mana each tick. Set both Mana and Stamina rechargeRate to 0; both retain restRechargeMultiplier 1. Health settings were preserved. Quiet Meridian, potions and other actual explicit recovery effects retain their stated values; their text no longer assumes ordinary passive Mana uptake.

A new gh_daily_resource_recovery monitor reads the actual party day counter. The first observation establishes a baseline without refilling an imported save. A later increase emits one normal-recovery cue; later turns of the same day do not repeat it. Merely changing time-of-day does not qualify. The cue directs the supported AI resource update to fill each living character's actual current maximum once, respecting an already applied rest update. It is not a fixed tick-to-day conversion and creates no additional clock.

The native rest setting and disabled recharge are structured mechanics. The new-day cue's numeric application is narrator-mediated because the documented script getter exposes current resources, not a per-character maximum getter. No undocumented getter or guessed maximum was introduced. Verify actual new-day delivery in Voyage; the local script tests cover signal timing and deduplication, not the AI's resource update.

Sources: community [Resources](https://wiki.unofficial.voyage/mechanics/resourceSettings) and [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions).

## Afternoon work and starter quests

All four academy First Day starts now have two additional optional personal goals:
- Find Afternoon Work: agree a paid job or trial shift, including duties, hours compatible with class, pay and a first shift. Agreeing employment completes the arrangement goal; wages require actual earned work.
- Visit the Glowhaven Guild: entering the existing public guild location completes the visit. No conversation, registration, application, fee, test, badge or contract is required.

The original first morning lesson remains the immediate activity. Other story starts retain their configured quests. General student narration also mentions afternoon work when plans arise, including for students established through a custom background.

Work leads appear in the four academy public arrival halls, first-day scenes and afternoon guidance. Actual town opportunities are kitchen preparation/cleanup with Daichi Kamado at The Golden Ladle, room turnover/common-room work with Noriko Hanesawa at Roseberry Inn, and shelving or qualified copying with Lucien Delorme at The Everlight Public Library. Ordinary half-day help pays 8-12 Marks for a completed agreed shift; qualified work is separately quoted. No automatic job acceptance, skipped class, time jump, wage payment or relationship gain follows from reading a notice or completing the job-arrangement quest.

The four first-morning quest statements also now correctly say student day rather than teaching day.

## Portraits and mods

Observed export data:

| World | Installed mod IDs and pinned versions |
| --- | --- |
| ChikaraOld | yPtGs6C93Y6D v17; OBBcaEsdfdDo v3; CbmL5QbhpgBD v204 |
| Luxcellia | nK9E8qi2UNik v2; -hHKpJT95NUH v2; G6w21MEkYhdY v230 |
| Active Glowhaven | None |

Both reference worlds use mods. Their exports include IDs and versions but do not include the separate mod definitions or readable mod names. Public lookup did not resolve those definitions. Their presence alone cannot establish which mod contributed portrait instructions or whether a mod is the reason for the observed image quality. Luxcellia also contains dsar-prefixed character-generation blocks, whose specific provenance is unverified.

The community [Modding reference](https://wiki.unofficial.voyage/mods/modding) explains that mods can contribute ordinary world and AI sections, and applied contributions can persist in saved world data. A mod is therefore not evidence of a secret image renderer.

A direct, visible difference is Luxcellia's player Appearance priority/bypass block, separately from its generic character default. Its image direction also emphasizes anime key-visual rendering, variable linework, controlled gradients, rim light and atmosphere. Glowhaven's old shared character prompt spent much of its space on prohibitions and crisp cel-shaded default rendering. This plausibly contributes to a more generic result, but it is a prompt-based inference, not an A/B image result.

Changes made:
- Player Appearance begins with a project-specific GLOWHAVEN PLAYER PORTRAIT marker.
- Matching instructions in the existing shared character image field defer to that complete player visual brief. This is prompt-level priority guidance, not a new native engine field or parser.
- Appearance now puts frame and positive art direction first, with character-specific facial design, gesture, motivated light, material rendering and a coherent palette. Its length target is 2,500-4,200 characters only when supported details justify it, with a 4,800 ceiling.
- Stylized anime faces remain required, while soft painted fabric transitions and environmental depth are allowed.
- The established standing, centered hip-up 2:3 composition and 12.5-15% headroom remain consistent with the project's portrait guide.

This pass does not install unidentified mods or change the runtime Image Model. The selected model is not recorded in these exports and the user is unsure which is selected. Official [Patch 2.33.7](https://voyage.io/whats-new/patch/patch%3A100000946) describes the unified Image Model selector and GPT Image 2 Medium default; that does not prove which model a given session currently uses. Compare portraits under the same chosen image model when judging the prompt change.

The [paste-ready example](../world-draft/Beta2%20-%20Player%20Portrait%20Example.txt) is based on the adult black-haired, violet-eyed human described in the initial screenshot. It is a test brief, not a change to any player or NPC record.

## Local checks and remaining playtests

Passed:
- All edited JSON parses and full/split section copies match.
- Ten user voice assignments match the latest export; Ritsu's additional voice remains. All other NPC fields match the pre-update backup.
- The revised user ItemGenerationAndUsage object remains an exact semantic match at 20,000 compact characters.
- The four student starts point at both defined new quests, with no duplicated starting-quest entries. Other starts are unchanged.
- Guild completion uses a supported story completion query describing actual entry into the public hall; neither new quest awards money or membership.
- Both passive resource recharge rates are zero and the old Mana trigger is absent.
- Eight daily-monitor cases cover initialization, repeated turns, advancing days, skipped days, backwards days, invalid input and importing an existing save.
- All 173 location identities, images, coordinates, radii and level ranges are preserved.
- Updated AI leaves and relevant task/combined-image caps pass. Character background task: 19,741 compact characters; Action Info: 19,800; Story: 29,772. Shared character image field: 3,226 characters; all image fields combined: 10,951.

Not performed: Voyage Studio import/schema validation, live NPC voice playback, acquisition/XP playtest, actual day refill, new quest execution, or a Voyage portrait generation/A/B test. Native probability and AI-interpreted prompts are not proven by local parsing.

Exact pre-update copies are in world-draft/backups/Beta Playtest 2 20261030.

## Studio quest schema correction

The user's Studio validation caught three errors in the two newly authored quests: both omitted the required string questSource, and the guild quest used a trigger-only party-location condition directly as a quest completionCondition. Quest completion supports only a story/query object or a narrative-event-completed/eventId object.

Fixed in both the full export and standalone quest file:
- Find Afternoon Work: questSource is Town work noticeboard. An explicit blank questLocation keeps this flexible employment goal locationless.
- Visit the Glowhaven Guild: questSource is the existing guild location, and completionCondition is a story query describing actual entry into its public hall. Registration, conversation, fees, tests and contracts are not completion requirements.

This corrects an authoring error in the previous pass. The earlier local checks verified JSON structure, references and intended behavior but did not validate this quest-specific union. The Studio error is the authoritative evidence. A reusable local quest-shape check now verifies the required source fields, allowed completion-condition shapes, objectives, start references and split-file synchronization across the full quest catalogue.

Reference: [community quest schema](https://wiki.unofficial.voyage/world/quests), checked against the exact Studio error supplied by the user. A new Studio import/validation result has not yet been observed.