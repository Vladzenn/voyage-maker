# Glowhaven AI Overhaul — Comparison and Patch Notes

Completed 2026-10-28. Built from the supplied Glowhaven AI snapshot and the current local Playtest One world. The supplied AI snapshot matched the local world's two AI sections exactly before this work.

## Main finding

The previous configuration had substantial setting restrictions but uneven operational depth. Story was already close to its limit; many earlier stages had much less guidance about how to make a decision. Putting every correction in Story left item handling, character updates, memory and encounter selection responsible for interpreting constraints that were clearer elsewhere. This rewrite gives each stage its own procedures, examples and review rules, while consolidating duplicated Story instructions.

The AI instruction text increases from **90,663 to 175,318 characters** across the same **17 supported tasks**. That is a coverage measure, not a performance score. Story itself remains approximately its earlier size. The improvement is in where the rules run and how concrete they are, rather than filling every section to its maximum.

## What the references contribute

| Reference | Useful observed approach | Adaptation for Glowhaven |
|---|---|---|
| Luxcellia | Detailed task-specific procedures; cast reuse; relationship context; item ownership; places with several services; consequential memory | Explicit decision steps for identity, actions, purchases, updates, learning and summaries; services use actual role holders; existing cast and its jobs persist |
| Konosuba | Specific comedy engines and callbacks; consequences that follow actual incidents; distinct voices; resistance to repeated questioning; precise transaction state | Sincere shonen action alongside petty comedy; character-driven timing; remembered embarrassments and promises; no automatic bills or punishment; direct answers and completed tasks stay resolved |
| Chikara | Grounded institutional life; careful action and ability limits; party participation; meaningful practice; respect for real materials and work | Graduated adult competence, actual class/service roles, physical and magical routing, practical training, limited crafting inputs and party membership based on agreement |

These are reusable authoring patterns. Their distinctive plots, named cast, guild ladders, currencies, resource pools and special powers are not transplanted.

The references also disagree. Their NPC intent protocols differ, and some include task keys whose runtime use is not documented in the current community reference. Luxcellia and Konosuba's social-intent procedures are adapted into Story and Dialogue; Glowhaven keeps the current combat-only intent protocol. Chikara's different intent counts and supporting-skill bonuses are not adopted. Neither reference's extra `generateFactionDetails`/`generateAbilities` task is added without evidence that the engine uses it.

## Changes by function

**Narration and scene direction.** The eight editable Story defaults are deliberately rewritten. Turns resolve the actual player action, use supplied results, distinguish current payload from past prose, and end at a usable response point. Conversation, inspection, arrival, work and requested time intervals have different shapes. Direct answers can be complete; quiet scenes need no emergency. Four redundant custom Story blocks are consolidated into those defaults. Full names remain in records and speaker identifiers; normal spoken address can use names, titles and honorifics naturally.

**People with their own decisions.** The addressed character leads the exchange. Unaddressed people need perceptual access, a reason to react and something new to contribute. A crowd need not become a chorus. Actual desires, role, knowledge, flaws and relationships drive behavior. Cruelty, stupidity, vanity and selfishness remain real where authored; there is no universal hidden kindness. Friendship, work, courtship, jealousy and recruitment remain distinct. A professor can help and then return to work.

**Stable identities.** Resolve descriptions, names, offices and previous introductions against the existing cast before creating another person. Unknown journal status does not mean the NPC is absent from the world. An absent official needs directions or communication, rather than an invented replacement. Appearance, equipment and power stay individual; mere role, school or age is not permission to redesign someone. Generated recurring people also persist.

**Actions and magic.** Identify the actual objective, method, target, access and scope. Routine feasible actions need no invented check. Real practice can matter without becoming lethal combat or guaranteed XP. Use exact actual skills rather than the highest owned statistic. One physically delivered infused strike gets one primary physical accuracy resolution. Existing impact scale, six attributes, costs, caps, cooldowns and resource rules remain intact. A claim or successful social check cannot rewrite truth or manufacture universal authority.

**Items and the economy.** Inventory distinguishes display, offer, ownership, loan, consignment, acquisition, consumption and deposit. A purchase requires a quote and agreement before transfer. Existing item keys and actual holders matter; typed rewards pay once. Receipts and keys preserve established information without duplicating goods or adding powers. Crafting needs real materials, tools and completed work. Item prose does not invent reserve capacity, bonuses or reliable on-use scripts.

**Memory.** Summaries keep consequential facts, not every gesture. They distinguish accepted versus completed work, quoted versus paid prices, spoken claims versus facts, interrupted versus accepted confessions and temporary escort versus party membership. Names, evidence, holders, promises, refusals and actual elapsed time survive compression. A specific callback can recur in a changed context rather than becoming a repeated catchphrase. Current structured state takes priority over unsupported old narration.

**Locations and encounters.** Significant places explain actual activities, responsible people and conditional situations. They do not all need a conspiracy. Encounters begin by checking whether an interruption belongs. Existing authored cast, local causes and unresolved consequences come first. School culture does not predetermine student personalities. Actual geography, fixed endpoints, safe spaces and resolved outcomes persist. New-region generation stays disabled.

**Learning.** A technique needs a supported acquisition event, actual skills, bounded operation and a real cost/limit. Existing repertoire is checked first. Cosmetic variation is not another ability. Mixed techniques do not summon absent allies, add free attacks or award traits and levels. Rare Freeform, soul extraction and perfected mana transfusion do not become default rewards.

**Image guidance.** All five image categories now have more specific identity, anatomy, rendering, framing and setting controls. NPC portraits follow the project's 2D anime, standing hip-up, 2:3 composition and headroom requirements; settings distinguish a destination gate from a view through its portal. Existing art is preserved. The local portrait guide's actual randomized pose-selection workflow still runs outside Voyage; prompt text does not pretend to execute a random draw or save a PNG by itself.

## Section coverage and size checks

Before/After measure instruction string characters. The final column measures each whole task as compact JSON, including keys and escaping. Small chat tasks remain short enough for their purpose rather than copying a long campaign prompt into every reply.

| AI stage | Before | After | Compact JSON / cap |
|---|---:|---:|---:|
| `generateStory` | 27,850 | 28,550 | 29,095 / 30,000 |
| `generateInitialStart` | 2,264 | 7,970 | 8,222 / 20,000 |
| `generateActionInfo` | 10,287 | 18,926 | 19,378 / 20,000 |
| `generateCharacterBackground` | 4,525 | 8,803 | 8,973 / 20,000 |
| `generateConversationStarters` | 632 | 1,861 | 1,951 / 20,000 |
| `generateDialogue` | 2,979 | 6,994 | 7,245 / 20,000 |
| `generateNpcChatSummary` | 695 | 2,180 | 2,250 / 20,000 |
| `generateNPCIntents` | 7,121 | 13,206 | 13,671 / 40,000 |
| `generateNewNPC` | 4,750 | 11,127 | 11,341 / 20,000 |
| `generateNPCDetails` | 7,487 | 13,645 | 14,101 / 28,964 |
| `generateNPCUpdates` | 4,664 | 10,717 | 11,090 / 24,000 |
| `generateLocationDetails` | 4,081 | 8,857 | 9,061 / 20,000 |
| `generateRegionDetails` | 1,340 | 4,046 | 4,136 / 20,000 |
| `generateEncounters` | 2,424 | 8,619 | 8,856 / 20,000 |
| `ItemGenerationAndUsage` | 3,826 | 11,562 | 11,893 / 20,000 |
| `summarization` | 3,225 | 10,999 | 11,277 / 20,000 |
| `generateLearnedAbilities` | 2,513 | 7,256 | 7,422 / 20,000 |

The five image fields total 10,860 compact JSON characters, below 15,000; each is below 5,000. All task leaves fit their applicable limits. These are local checks against the current community guidance, not a complete Studio validation.

## Portal fixes prompted by the two playtests

The transcripts establish a mismatch: prose repeatedly describes Glowhaven while saved placement remains Drakenspire. They also show an invented Asterveil landing, repeated destination demands, and a court-access misunderstanding. Without live engine traces, the exact failed condition cannot be proven. The patch addresses the observable failure paths rather than claiming a confirmed engine bug.

1. Existing portal queries accept a committed crossing without requiring the player to repeat ceremonial key-use wording. Actual key inventory is still required for normal outbound travel.
2. A narrow mechanical **solo return fallback** handles clear commands such as `I enter`, `I enter the portal back to Glowhaven`, and `I then turn back and head to Gloomhaven` at existing return arches. Mere approach, questions, quoted speech, negation and arbitrary destinations are rejected. Complex wording and multiplayer travel retain the existing semantic route.
3. All existing portal routers share a per-tick movement guard, preventing one command from causing an outbound crossing and then a second return crossing in the same tick.
4. A **Glowhaven Portal Key** is granted by a typed item-add follow-up after the first actual ordinary Evertree departure. Missing-key recipients receive one; held copies are not duplicated. It identifies the home endpoint and is reusable. The issuance trigger is one-time: losing it does not create an infinite automatic replacement supply.
5. Fixed return arches remain usable without any key. The return key works at the actual destination return arches; it is not an anywhere-in-the-world recall spell. Returns land at **Evertree Base - Portal Room**, without another choice of city landing.
6. The level-100 developer did not automatically qualify for the student event by the earlier agreed design. An explicit developer-only solo command now makes this easy to test: **`Start the portal field-test scenario`** in the Portal Room. It arms the examination; entering either actual normal keyed route next triggers the one-time displacement. It does not teleport during setup, repeat a completed incident or bypass the normal student's briefing.
7. First return from the Silken Descent still grants its Silver Web discovery once. Immediate retreat remains possible; descent and the matron are optional. No enemies, quest progress or companion ownership reset.

## Court-controlled access — latest canon

Outbound portals are controlled by the court. Travelers need a genuine issued key and a legitimate approved reason. Academy enrollment is the easiest ordinary basis; approved trade, court duties and credible noble connections or sponsorship can also support a request. Status is not itself a key grant. Only the court or its explicitly delegated official issues normal keys. The actual issuance triggers now require approval and a real handover; an apprentice, porter or helpful acquaintance cannot invent permission.

The paired Developer Playtester / Developer: Portal Inspection setup retains its configured test keys. Its kit already supplies both normal route keys, so the start does not add duplicate copies. The new return key is issued under the existing court-approved passage. Valid granted authorization remains valid within its scope; this is not a repeated court-audience requirement at each crossing. Keys do not open private palace rooms or erase warrants. No new magical owner-binding system is invented; legal authorization, physical possession and actual security response remain distinct.

## Preserved and changed data

- All **132 NPC records**, their order and their existing portrait URLs are unchanged.
- All **272 stored media fields** are preserved, including empty slots; no image is generated or replaced.
- Realm/region definitions, map coordinates and paths, attributes, skills, abilities, traits, currencies, resource configuration, game modes, faction records and existing quest definitions are unchanged.
- Seven root sections change: AI instructions, image prompt guidance, triggers, item types, the developer start, three portal-area descriptions, and existing portal lore entries.
- Three new triggers are added: direct solo return, first-crossing return-key issuance, and explicit developer test setup. Existing relevant portal scripts/queries are patched.
- `WorldAlpha - World.json` is the updated canonical world. Locations and World Lore standalone files are synchronized. Earlier named exports remain historical snapshots. Sources stay read-only. A complete pre-change world backup is retained.

## Checks completed and limits

**76 local fixtures pass.** They execute the actual trigger scripts and direct-command parsers in a JavaScript VM, with documented typed condition/effect behavior represented by a local harness. Semantic AI decisions are supplied in these fixtures. Covered cases include normal and displaced transit, retreat, discovery once, repeated travel, actual companions, court-issuance rejection, return-key quantity, same-tick routing, developer opt-in, enrollment and earlier quest behavior.

JSON parses, section/leaf sizes, trigger shape/caps, referenced destination/item/quest keys, source hashes, unchanged sections, NPC identity/order and media preservation are checked locally. These checks do **not** prove that a live AI will choose every correct action. No new live Voyage session, Studio import or complete platform validator run was performed. Existing session state has not been edited; importing an authored world is not a demonstrated migration/repair of a running save.

## Focused live playtest

Use Developer Playtester with Developer: Portal Inspection. Confirm both ordinary keys are present once. Enter Drakenspire; verify the journal/map and scene agree, then check that one Glowhaven return key appears. At the Arrival Gate type `I enter` and verify the actual location becomes Evertree Base / Portal Room. Repeat with Asterveil and confirm the fixed Cloudbloom endpoint. No second landing prompt or extra key should appear.

Then explicitly start the portal field-test scenario, enter either keyed route, verify Stranded Threshold in both the map and prose, and retreat immediately. Confirm the silver key appears once and ordinary routes still work. Finally test a normal nonstudent asking an unofficial apprentice for a key: no key grant. A court application with an actual qualifying purpose should be processed without requiring a Great Sage audience or repeated proof after approval.

For AI quality, test a quiet café visit without a forced incident; an existing role requested by title without a duplicate NPC; a shop quote without purchase; a successful finite official request without repeated objections; and a familiar character after summary compression. Compare actual replies and state changes, not prompt length.

## Documentation and evidence

The three supplied maintained-world AI snapshots are the primary examples; their inventory and hashes are in the authoring folder. Current community documentation supplies the task integration and compatibility guidance. It is unofficial and not a claim of Latitude endorsement.

- [AI instruction integration and limits](https://wiki.unofficial.voyage/ai/aiInstructions): exact default-key overrides versus additive custom sections; supported task identifiers and size rules.
- [NPC intent protocol](https://wiki.unofficial.voyage/ai/generateNPCIntents): current combat-only defaults, attempt semantics and tier budgets.
- [Item generation and usage](https://wiki.unofficial.voyage/ai/generateItemGenerationAndUsage): the actual JSON key is `ItemGenerationAndUsage`; awareness and possession differ.
- [Trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): typed item-add/remove, movement cascade, raw action input and planning/state behavior. AI guidance is probabilistic; supported typed effects change state when their conditions pass.
- [Image prompt configuration](https://wiki.unofficial.voyage/ai/imagePromptConfiguration): the five content categories and their size limits.

The regression report explicitly records the live-testing limits. This is a substantive authoring upgrade, not a claim that any instruction set can make the base model infallible.
