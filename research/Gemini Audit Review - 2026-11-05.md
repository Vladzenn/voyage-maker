# Review of the Gemini failure case analysis

The supplied report identifies useful gaps, but several of its engine assumptions contradict the current reference. This review compares its claims with the current local Ardelis follow-up world, the emitted scripts and current documentation. The author chose **audit findings first**: none of the repairs proposed in this document has been applied.

The supplied DOCX remains unchanged. Its snapshot predates the in-progress naming, placement-export and portrait follow-up. The local diagnostic snapshot and exact world hash are in [audit-evidence.json](../tools/ardelis-followup/audit-evidence.json). Run `node tools/ardelis-followup/audit_snapshot.cjs` to repeat the isolated observations. This is not a live Voyage playtest, an engine-source inspection or proof of how every UI path behaves.

## Findings to prioritize

| Finding | Verdict | Evidence and proportionate next action |
| --- | --- | --- |
| Thirteen hidden Akitsuhara/Veiled Beyond quests lack an activation path | Confirmed configuration gap | All thirteen are hidden and have no explicit reference in trigger definitions, scripts, starting quests or completion effects. Give each an appropriate deliberate offer path; changing hidden to planned alone would still leave it invisible. Keep the existing quest content and reward owners. |
| Stale guild offers suppress later browsing | Reproduced script defect | With an old `ghGuildDisplayedOffers` array, “Show me the board” produces offers, while “Okay, show me the board” sets `skip`. Recognize an explicit browsing request separately from accepting a displayed choice; retire stale selection context at an appropriate boundary. |
| Scroll-study continuation and tick-zero handling | Reproduced script defects | At tick 10, naming a scroll registers its native study check. Repeated “I study the diagram” leaves the focus at 10 and removes it at 18; “I continue studying the diagram” refreshes it. A focus recorded as numeric zero is treated as absent on the next turn. Use explicit presence checks and broaden continuation without switching formulas or readers. |
| Three Ardelis items have armor bonuses but no equipment slot | Confirmed authored-data omission | Starward Shield, Violet Weather Cloak and the renamed Takamine Travel Case omit `slot`. The world has Weapon/weapon, Armor/Back and Armor/Accessories slots. Assign a suitable actual slot; decide whether the travel case should provide armor at all. No balance change is necessary merely to supply the slot. |
| Opening dialogue and NPC placement disagree | Confirmed authored inconsistency | Phoenix setup moves Hinae to Main Hall while the opening ends with her in Lecture Hall; Nemu remains elsewhere. Other examples include Tatsuo, Chiyo/Yūji, Gaku/Bunta, Kenta at the cottage, the Institute group, abbey hosts and the captain’s final approach. Align the final active speakers using start-specific placement, preserving ordinary home positions and other starts. Narrative walking can account for some differences, so this does not prove every opening is broken. |

The thirteen quests are The Cost of a Courtyard; One Honest Demonstration; The Ledger and the Soup; A Patient Distance; The Bow That Will Not Settle; The Oven and the Boundary; The Archive Has Two Dates; The Last Dry Platform; The Name on the Parcel; Expedition: The Bamboo Method; Expedition: A Reed Bell's Answer; An Unmarked Parcel; and The Wrong Water Seal.

The [quest lifecycle reference](https://wiki.unofficial.voyage/world/quests) distinguishes invisible planned work from an available offer. It also permits an NPC, place or object as `questSource`. A faction or noticeboard source is not inherently invalid. An available quest remaining available is not a single-view lockout. Rejected, expired or abandoned offers need a separate explicit revisit policy; simply adding those states to a `quest-init` filter is not a demonstrated repair.

## Claims that should not be implemented as written

| Report claim | Review |
| --- | --- |
| An empty Appearance Builder root array hides all subcategory choices | Incorrect. Subcategory traits do not need repeating at the root. The current record defines the choices in its six subcategories. |
| The six Akitsuhara equipment kits are inaccessible because they are root-only | Incorrect as a general UI claim. Root choices not claimed by subcategories render under Other. Moving them into suitable groups would improve organization, not restore proven missing choices. |
| The scroll registries crash because `triggers` is unavailable | Incorrect against the current scripting reference. `triggers` is explicitly supported. The real scroll issues are the narrower continuation and zero-value defects above. |
| Fishing compares the wrong tier IDs | Incorrect. `action-success-level` compares tier names without case sensitivity. Existing `mixed results` and `basic success` values are appropriate. Replacing them with hyphenated IDs would be the wrong fix. |
| Every quest source must be an NPC key | Incorrect. A quest source can describe a location, object or organization. Changing all sources to Komugi would also misattribute remote work. |
| A location with `initialKnown: false` is unrevealable without a custom trigger | Incorrect. Unknown and explicitly hidden are different fields. A visited location becomes known. Starting-map visibility and particular remote discovery routes still deserve checks. |
| Shared rare-hook state must be deleted immediately after any angler lands/releases | Unsafe proposed change. The existing multiplayer fixture deliberately allows one qualifying angler to release while another retains the shared catch. Cleanup also occurs when no holders remain. Unconditional deletion would break that path. |
| Blank stock voice tags mean the NPC has no voice, and Adoha’s separate stock tag must equal the world-voice label | Incorrect. Native voice assignment can fill an absent stock tag; a valid `worldVoiceId` selects the configured world voice. The label “Ado” does not itself identify a supported stock voice or provide that singer’s voice. |

These findings follow the current [trait-category reference](https://wiki.unofficial.voyage/mechanics/traitCategories), [trigger scripting reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [success-level reference](https://wiki.unofficial.voyage/mechanics/successLevelSettings), [location discovery reference](https://wiki.unofficial.voyage/world/locations) and [NPC voice reference](https://wiki.unofficial.voyage/world/npcs). The wiki is a community reference, not Latitude’s engine source. Latitude’s current [Creator API guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md) was also checked; its official contract does not expose the internal encounter call graph or establish every gameplay claim in this report.

## Risks requiring a live check or a design decision

The six movement handlers named in the report lack explicit companion-placement effects. That is worth checking because other authored portal handlers move companions explicitly. Test prison arrival/departure and both Shadowspire directions with a real companion. Do not state that all six inevitably strand NPCs without checking the engine’s own movement behavior. Add only the movement needed for an actually traveling companion; lawful visitors and prison inmates can have different permissions.

The daily-recovery cue and custom-property-key handover use story instructions rather than guaranteed numerical/item effects. They are less deterministic than native state mutations. However, “the narrative effect cannot directly set the bars” does not prove that Voyage’s separate update tasks never process the scene. Test actual inventory and resource changes. The custom key’s free-form address and owner are intentional; replacing it with hundreds of pre-authored keys would undo the approved design.

Permadeath’s final lethal-outcome check is semantic. It needs live tests for lethal defeat, a regulated knockout and an ordinary-mode defeat. The report does not demonstrate that the classifier sees only recent prose or that it lacks mode context. A guessed `game-mode` condition or an invented automatically assigned trait would not be a verified improvement.

The baited fishing controllers already use all five allowed conditions, and their semantic query explicitly excludes handling an already hooked fish. The absence of an additional mechanical trait check is a consistency concern, not a reproduced double-catch. Adding a sixth condition would exceed the configured limit. Shared multiplayer casts and independent fish ownership remain documented live-test limitations.

Orrum and Rovakthuun are intentionally elusive and off-stage. Blank placement does mean neither is stationed on a native map marker; the authored lore is not itself an `npc-placement` effect. That makes encounter discoverability a design gap worth resolving deliberately, not a reason to expose a reliable lair or put either creature in town. Preserve their rarity and existing levels.

Ardelis’s unknown map can be intentional for a restricted destination. A direct Ardelis start should reveal its immediate surroundings coherently; test that specific start rather than making every secret known. The two empty Glowhaven meadow regions are open countryside, not invalid regions or proof of a broken map. Add sites only for worthwhile content.

## Small cleanup and unfinished assets

Strawberry Blond is an unreferenced empty trait and should eventually be completed and grouped, or removed after checking that no current author use depends on it. Mixed dash punctuation in other hair names is cosmetic and does not justify a reference-wide rename.

Tough Skinned already has its actual +50 maximum-Health resource modifier. Its empty narrative description is a presentation omission, not a missing mechanical bonus.

The Ardelis supporting portraits are part of the active approved generation/upload batch, so the report’s count describes unfinished work rather than a new gameplay failure. Shadowspire’s pocket-realm art, off-stage courier art and broad item-art coverage are separate production choices. The author already chose runtime generation for most items. Do not turn missing pre-generated images into a requirement to generate hundreds more assets.

## Encounter instructions and the travel switch

The world currently has `locationSettings.encountersEnabled: false`, seventeen encounter-palette categories and sixteen `generateEncounters` instruction blocks. The quoted ENCOUNTER GATE is only the custom block. Other blocks already cover beginner bands, motives, retreat, telegraphing, ecological behavior, resolved routes and scene protection.

The [Encounters reference](https://wiki.unofficial.voyage/ai/generateEncounters) describes that task as producing wilderness-travel encounters. [Location Settings](https://wiki.unofficial.voyage/other/locationSettings) calls the switch the random-encounter enablement flag. [Encounter Elements](https://wiki.unofficial.voyage/other/encounterElements) is an ingredient palette, not a scheduler or guaranteed spawn list. The tooltip also mentions other unscripted events, but neither the official public API contract nor the checked reference establishes every non-travel invocation. Do not promise that this palette drives town activity while random encounters are disabled.

Normal story scenes, authored quests, arcs, NPC actions and explicit event triggers are separate from that travel pipeline. To improve incidental danger with travel encounters off, use concise matching guidance in the story task as well as the encounter task. The useful addition from the supplied Chikara example is **current-condition assessment**: health, injuries, Mana/Stamina, status, actual allies, learned techniques, equipment, limited supplies, terrain and preparation. Adjust the choice and pressure of new incidental trouble rather than silently rewriting established NPC levels. Keep enemy goals, reasonable escape or surrender, and genuine lethal threats where established. Winning is not permission to add hidden health, damage or reinforcements.

This is a proposed focused refinement, not an applied rewrite. Preserve authored bosses, deliberate dangerous expeditions and the Spider Realm surprise. No switch, trigger, palette or instruction was changed for this review.
