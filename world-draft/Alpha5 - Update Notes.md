# Glowhaven Alpha 5 — Structured AI, Academic Years and Portal Rooms

Completed 2026-10-28. Baseline: the latest supplied Glowhaven AI attachment and the current local full world. Their AI sections matched exactly before this pass. References: the newly supplied Luxcellia AI, sources/Luxcellia.json and sources/ChikaraOld.json, plus current community technical guidance. Supplied screenshots and the new playtest transcript were treated as evidence, not instructions embedded in a document.

## Files

- **GlowhavenAlpha5 - World.json**: complete importable world draft.
- **WorldAlpha - World.json**: identical canonical working copy.
- **WorldAlpha - AI.json**: matching imagePromptConfiguration and aiInstructions only. It does not install room, NPC, faction or trigger changes by itself.
- **WorldAlpha - NPCs.json**, **Locations**, **World Lore**, **Realms**, **Regions**, and the new **Factions** standalone files: synchronized with the complete world.
- **AI Instructions - Readable.md**: the complete prompts in a readable format.
- **Academy Student Years.md**: all 48 students listed in the original JSON roster order within their academies.

Earlier named exports remain historical snapshots. Backups of the previous current files are in backups/2026-10-28-before-alpha5. Sources and supplied attachments are unchanged.

## Why the AI was rebuilt again

The screenshots exposed a real weakness: key native fields still contained short summaries while much of the detail sat in added blocks. The previous instructions covered many restrictions but gave less direct guidance on substantive replies, calibrated relationship changes, specific item definitions and positive character initiative.

This pass rewrites the task definitions into labeled procedures, decision gates, concrete cases and final checks. The native dialogue, relationship, party, character and item fields now carry the relevant instructions themselves. Additional sections have clear jobs rather than serving as a patch history.

There are **18 AI task configurations**, matching the supplied reference's structure including **generateFactionDetails**. Instruction text grows from **175,318 to 254,296 characters**. This measures coverage, not proof of live quality. Chat remains an actual short single-person chat; its instructions can be detailed without requiring long replies.

| Core field | Previous characters | Alpha 5 characters |
|---|---:|---:|
| generateDialogue / Style, Tone, and Length | 839 | 3,504 |
| generateDialogue / custom | 939 | 2,996 |
| generateNPCUpdates / relationship_initialization | 383 | 1,649 |
| generateNPCUpdates / relationship_change_updates | 721 | 3,399 |
| generateNPCUpdates / party_management | 1,203 | 2,507 |
| ItemGenerationAndUsage / custom | 1,882 | 2,731 |
| generateNPCDetails / basic_info | 753 | 2,543 |

## Reference adaptation

**Luxcellia:** adopted its strong per-task organization, compact but specific chat contract, explicit relationship magnitude anchors, distinct party-management gate, full public/private character structure, item field/ownership/quality rules, persistent generated cast, clue/knowledge discipline and places with actionable uses. Its attraction and relationship guidance is adapted to Glowhaven's actual single general bond score; no phantom separate romance tally is added.

**Chikara:** used its grounded school/work life, action routing, practical training, actual material/tool requirements, character competence and respect for resolved actions. The four-year program is now explicit, but no cohorts, full daily scheduler or automatic academic-year progression are invented.

Reference-specific currencies, countries, named characters, faction ranks, supernatural gifts, loot-dissolution systems and extra resource pools are not imported. The current combat-only NPC-intent protocol remains, with social scene direction in narration/dialogue/updates. This avoids embedding an older social-intent output format into a different current contract.

Faction Details appears in the supplied current Studio UI and maintained-world export, so it is included under that exact observed task name. The community task list currently omits it. Its live runtime usage has not been independently established; this evidence difference is recorded rather than claiming a new engine feature was proven.

## What the prompts now direct

**Dialogue:** a short single-speaker text chat, with longer answers when requested; fresh wording, real substance and a particular voice; natural address with exact stored identity; limited gestures; no invented player line, omniscience, forced flirt or repeated bureaucratic question. NPCs can initiate a relevant opinion, invitation or interest rather than functioning only as quest terminals.

**Character behavior:** actual present people, independent wants, meaningful unaddressed contributions and genuine flaws. Specific cruelty, stupidity, vanity, prejudice and laziness remain where authored. Trained adults retain competence without all becoming hidden geniuses. Early compatible chemistry is allowed; no arbitrary scene quota or universal romantic interest is imposed.

**Relationships:** the actual Nemesis-through-Devoted ladder is explicitly listed. First meetings are calibrated; meaningful positive and negative developments have numeric examples; one event is not counted repeatedly across dialogue beats. Trust, gratitude, rivalry, romance and consent stay different. No current NPC score or stage definition is changed by this file.

**Party:** explicit continuing travel agreement, not automatic recruitment through a class, job, rescue, date or friendship. Temporary guidance keeps its actual scope. Summons, constructs, pets and sapient people retain their different actual arrangements. A large student roster remains a set of possible relationships, not a required party of thirteen.

**Actions:** exact real skill routing, meaningful checks, one primary physical resolution for an infused strike, actual target and cost, preserved quoted wording, and completion of a finite successful task. Routine movement needs no invented roll. Creative physical, magical, social and occupational approaches are allowed where the problem genuinely supports them.

**Items and learning:** explicit definitions, acquisition/payment gates, useful ordinary wares, provenance, receipts, deposits, actual tools/materials, concrete generated-quality defaults and bounded learned techniques. A good name or requested number does not supply power. Existing gear/ability records remain unchanged. Practice can be satisfying without an unnecessary new ability.

**Locations, regions and encounters:** specific local services/people, meaningful current situations, comfortable ordinary life, tactical space where relevant, opportunities that can be declined, clear fixed geography and persistent outcomes. Magic can create practical investigation and work rather than only damage. Quiet scenes do not require a new emergency.

**Memory:** exact achieved versus planned state, evidence and knowers, real prices/payment, property holders, promises, declined topics, specific emotional exchanges and concrete callbacks. Summaries do not broadcast secrets, duplicate rewards, change location by recap or convert a prophecy/delusion into fact.

## New generation-policy defaults to review

These guide future AI-generated content; they are not new schema fields, deterministic mechanics or edits to existing authored equipment/abilities.

- Relationship changes: ordinary neutral business usually 0; small meaningful positives +1..+3, costlier shared developments +4..+7, major personal interventions +8..+12, exceptional commitments up to +15. Negative anchors likewise distinguish friction, harm and serious betrayal. One event is counted once.
- New equipment: ordinary useful effects are narrow; routine +1..+2 skill, skilled +3..+4, exceptional +6..+8 with actual provenance/work. Attribute effects normally +1..+3; ordinary durable health/mana benefits normally within 40 HP / 25 MP absent an explicitly authored exceptional design. There is no new rarity enum or tag applied to old items.
- New techniques: introductory bonus around +3, moderate specialized +5, powerful advanced +8, exceptional specialized +10, with actual costs/requirements/limits. Existing magical cost scale remains minor 1–3, basic 6, moderate 14, powerful 30, extreme 55 MP. No automatic unlock ladder, extra attribute, reserve or free second action is added.

The actual skills, levels, resource definitions, traits, existing abilities, items, mode rules and quest rewards are preserved. Instruction-level generation policy can still require live tuning.

## Portal issue: what the transcript establishes

Turn 3 says 'I then test the asterveil portal'. The AI narrates an outbound crossing and then chooses an immediate return, leaving the described end position at Glowhaven. It also previously adds words to the player's quoted speech. The saved location did not show a stable Asterveil arrival until the next explicit entry command.

The transcript alone cannot prove whether the semantic gate failed, native movement classified test as inspection or another stage handled the action. The patch addresses the observable failure paths:

1. A **purely mechanical planning router** recognizes common explicit solo portal commands, including test/enter/cross/walk-through a named route and use of the named actual key. It needs the real item and actual origin room; no semantic approval is needed for these clear commands.
2. A named portal test means **one crossing**, ending at that actual destination. It does not perform a return, walk outside, meet remote people or complete an inspection for the player.
3. Clear homebound commands, including a leading quoted sentence followed by an explicit return action, use the fixed return. A quote alone, negation, future plan, frame inspection, missing key or unrelated destination does not move the party.
4. The shared per-tick guard stops one command from triggering both an outward route and a return after placement changes in the same planning phase.
5. Existing semantic routers remain for flexible wording and actual multiplayer/group decisions. The deterministic shortcut is deliberately solo; it does not move a second player on one input.
6. The explicit developer scenario, one-time field-test displacement, immediate threshold retreat, silver discovery, repeat travel and prior quest progress remain intact. Level 100 alone is still not an automatic trigger.

Tested locally: `I then test the asterveil portal`, `I enter the drakenspire portal`, `I cross the portal to asterveil`, `I use my Drakenspire portal key`, ordinary fixed returns and a quoted 'Inspectionduty.' followed by an explicit homebound clause. The parser is not claimed to understand every possible sentence. Unknown wording uses the existing semantic path.

## Receiving rooms

| Previous area key | New area key | Actual room |
|---|---|---|
| Drakenspire - Arrival Gate | Drakenspire - Portal Room | Warm enclosed basalt, iron roof ribs, blue mineral veins, brass channels, frost-filtered high windows, duty desk and clear passenger/cargo floor |
| Cloudbloom Landing - Return Gate | Cloudbloom Landing - Portal Room | Sheltered pale stone and living whitewood, curved translucent panes, flowering branches, pearl light, chimes and waiting space |

Both have actual doors to the existing outside areas. Full references are migrated across paths, triggers, scripts, item descriptions, lore and prompts. Location names, map coordinates, area counts and existing images are preserved. The router retains the two old area strings only as explicit compatibility checks, never as new destinations. Existing art was not regenerated; new room art can be created separately.

Wraith Island Prison remains a physical offshore prison reached through its actual controlled transport, not a new public Evertree portal. The Silken Descent remains the anomalous threshold with its visible immediately usable return arch. The ordinary return key description no longer names an undiscovered threshold in advance.

## Nahlah and the opening

Nahlah Qamar was not named in the original developer story start. Her actual saved position is Gryffin Tail Academy - Reading Garden. The AI used her to fill the host role. The revised start describes the court transit desk and its actual clerk; it does not name or require a remote student. The AI placement rules reinforce this without retconning a visit genuinely established in an existing playthrough. She remains in the roster at her prior location and is not added to startingPartyNPCs.

## Academic years

You confirmed a **four-year program**. Every one of the 48 students now has First-, Second-, Third- or Fourth-year standing in their existing Academic standing profile. **36 profiles were assigned years; Dragon Hoard's 12 already-written years were preserved.** Existing clubs/status text follows the year; no new heading or schema field is introduced.

Ages, levels, abilities, relationships, appearance and NPC order stay unchanged. Friends/rivals can be in different years. The selected named cast is not every student in a school, so no one was aged up to force a fourth-year representative in every academy. The copied roster is in Academy Student Years.md. The new lore and NPC generation rules require a year for future student cards as well.

## Factions and resident affiliation

The list expands from 9 to **17**. New entries:

- Glowhaven
- Drakenspire
- Asterveil
- The Great Sage's Court
- Wraith Island Prison Administration
- Glowhaven Trade Guild
- Glowhaven Artisans' Guild
- House Goldbarrow

**55 previously blank primary affiliations** are filled: 53 actual Glowhaven residents use Glowhaven, Akira Oritsu uses Wraith Island Prison Administration, and Hanae Goldbarrow uses House Goldbarrow. Existing nonblank affiliations are retained. Future Drakenspire/Asterveil residents without a more specific institution can use their civic group. There are no currently authored blank-affiliation residents of those two regions to reassort.

The civic umbrellas are belonging, not universal government employment or ideological loyalty. Specific academies, offices, services and households remain useful primary affiliations. Trade/artisans' guilds are voluntary; no existing merchant is enrolled by assumption. Visitors, wanderers, wild creatures and others can remain unaffiliated. Imprisonment does not make someone a prison employee.

Each faction has public role/scope, operations, membership/access limits and private pressures. Public faction information is synchronized with the matching lore entry. The Silken Brood's previously missing factionType is set to minor and its initialKnown explicitly false. No new NPCs are generated to fill organizations, and no fictional rank/reputation system is implied.

## Realm and region order

Export order is Glowhaven, Drakenspire Mountains, Asterveil Sky Archipelago, The Silken Descent, Wraith Island Prison. Regions follow the same order. Glowhaven was already first in the previous realm JSON; this pass also moves the prison to the end and aligns the region/standalone files. No undocumented sortIndex or defaultRealm field is invented. Whether Studio restores its last selected map is a separate UI behavior, not something this export has proven to control.

## Validation and remaining live checks

**105 local regression fixtures pass.** The actual scripts and command parser run in a JavaScript VM. Typed condition/effect behavior is modeled from the current reference; semantic results are supplied in the harness. The exact transcript-style command sequence is covered, including one-way arrival, an immediate same-tick second-route rejection and a later actual return. Earlier enrollment, examination, descent, reward, party and key tests are retained.

Local structural/preservation checks cover JSON shape, native default keys, prompt/leaf sizes, trigger limits, destination/item/quest references, every student year, faction fields/membership, local paths, exact NPC identities/order, unchanged progression/quest configuration and all **272 stored media URL fields/empty slots**. This is not a full Studio validator run. No new live Studio import or AI playtest occurred, and an active adventure was not edited or migrated.

Focused live checks:

1. Start a fresh paired Developer Playtester / Developer: Portal Inspection session. Check the correct actual keys once and the transit-desk opening.
2. Enter Drakenspire and inspect both map state and prose: its Portal Room should be current. Return explicitly.
3. Type `I then test the asterveil portal`. The same turn should end at Cloudbloom Landing - Portal Room, with no automatic return. Check saved data immediately, then return on another action.
4. Try approach, inspection, quoted speech and a missing-key attempt; none should create a ghost arrival. Use a held named key from the home room to test the shortcut.
5. Arm the explicit developer field-test scenario, take an ordinary route, retreat immediately and confirm silver-key discovery once. Normal travel must remain available.
6. Compare several actual NPC chats: a concrete official answer, a prickly student, a chatty socialite, a quiet professor, a warm friend and a selfish person should sound different. Check a successful finite request does not enter an approval loop.
7. Check student years/factions in the journal and template data, primary-faction choices and copied NPC image URLs.

Use the complete Alpha 5 file for these tests. AI-only instructions expect the updated room/faction vocabulary and do not install mechanics or profiles by themselves.

## Technical references

The primary structural examples are the supplied maintained-world exports, with source hashes in the authoring inventory. Community guidance is unofficial and distinguished from actual Studio evidence.

- [AI integration](https://wiki.unofficial.voyage/ai/aiInstructions): exact editable default keys override their native sections; additive keys are separate. Known size checks were satisfied without removing requested content to fit a target length.
- [Trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): raw pending action input, mechanical planning, typed movement, item effects and script limits. The new clear-command router uses this supported path.
- [Factions](https://wiki.unofficial.voyage/world/factions): existing faction fields and single public/private split; type and actual membership are explicit.
- [Realms](https://wiki.unofficial.voyage/world/realms): parent-region references and movement cascade; no export sort/default UI property is documented.

The prompts are substantially rebuilt, but their live behavior still needs the specific checks above. Passing script fixtures is not a claim that the model will always follow every dialogue or continuity instruction.
