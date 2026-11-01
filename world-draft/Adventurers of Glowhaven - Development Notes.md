# Adventurers of Glowhaven — implementation and playtest notes

Implemented 1 November 2026 from the user's latest Studio export. The latest export differs from our preceding baseline only by nineteen item images. All nineteen URLs are retained. The full world remains the canonical record; derived section files are synchronized from it.

## What is in the release

Sixteen new NPCs, with six major and ten supporting portraits; three native arcs; sixteen standalone native quests; eighteen public situations pointing toward existing work and three additional arc leads; six creature types; twelve equipment choices; six private rooms/properties; two small company factions; and touring routines for three existing people. Orivelle's existing circuit is preserved.

The new companies are Bellwether Company and Copper Laurels. The first is a competent four-person expedition crew with a gap in its magical investigation skills. The second is an opportunistic four-person crew with genuine work behind it and dishonest schemes now. Neither is a replacement guild rank, player party or universal enemy faction.

Each person has a specific appearance, equipment, training, private want, concealment/knowledge boundaries, relationships, behavior and ordinary interests. New native cards use detailed records, exact placed addresses, low initial journal visibility and no invented prominence/schedule schema fields. Reciprocal relationships are added to nine existing contacts. Affinity counts were independently drawn with the approved 65/25/10 weighting: this sample happened to yield twelve single and four double affinities. No triple was forced into the sample. The recorded seed, eligible poses and actual selections are in tools/adventurers/portrait-briefs.json.

## Quests, arcs and triggers do different jobs

The native arc map is at parties[""].arcs. Each arc supplies its actual premise, theme, expected conclusion and private facts. It has no fabricated authored quest arcId. Voyage creates chapter association and surfacing state during play. The two substantial investigation arcs have a two-quest minimum; the comic interference arc can conclude after one convincing undertaking. Three meaningful developments remain a pacing aim, not a demand for three reports.

- **The Woman Beyond the Frost:** investigate Ysolenne's retaliation, then actually secure the commissioned route through force, banishment, disrupted cold-fed nodes or a carried-out agreement. Her grievance against Orrum is real; the attacks on unrelated people remain her responsibility. Orrum's power, elusiveness and location rules remain unchanged.
- **A Thesis No One Would Fund:** Suzuha Midorise is a weak combatant and excellent fourth-year Hydra Head researcher. The Stillwind Pearl exists, but records a short-lived air/mana pattern instead of powering island levitation. A sound sample, intact pearl or convincing in-place evidence can support a corrected thesis. This does not graduate her or complete the player's capstone.
- **A Very Reasonable Recovery Fee:** the Copper Laurels' bluster can end in exposure, bargaining, restitution, defeat or internal fracture. Actual theft needs a resolved outcome and actual inventory changes. No cloned crew, automatic confiscation or compulsory massacre.

The sixteen finite jobs use typed native completion conditions and one completion/reward owner. The finishing condition repeats the actual final objective and names its people, object and place. Eight are licensed guild postings; the others are personal work or authorized prison tasks. Rewards are full posted amounts, settled once through effects. Public leads never accept a quest or create a journal entry. Prison errands do not grant release. No new Silken Descent quest is added.

Luxcellia's useful pattern is local discovery, a clear offer, a specific playable obstacle and a definite ending. We retain those strengths without turning every job into an independent progress-counter system. The supplied Kato patch notes also informed exact combat routing and checkable endings, but the accompanying export did not contain the described quest-done command or new charge clauses. Those behaviors were designed here from documented interfaces rather than claimed as copied, inspected code.

## Trigger workload

We added twenty-seven root triggers and changed twelve existing definitions: the guild board, eight older Canopy acceptance gates, tournament locality and the two court-key issuance localities. Existing portal-crossing, anomaly, queen, trophy, rivalry and prison consequence triggers remain unchanged. There are 378 root triggers after this update.

A shared planning dispatcher supplies one relevant private offer and one current Canopy offer. The older Canopy queries now evaluate in the state phase against the dispatcher's current conversational gate. A natural yes can use the actual named offer in the previous scene; the player need not type a title. This is a relevance filter, not a claim that scripts preempt semantic checks inside one trigger. Scripts run after their typed conditions have passed.

The initial conservative Canopy probe counted eighteen possible checks including three generated arc-surfacing checks against a fifteen-check no-active-quest budget. The narrowed probes put ordinary scenes at seven to ten, including those three generated checks; a specific Canopy acceptance uses eight. The active Bronze-job probe uses eight against twenty. These are configuration eligibility probes with controlled state, not runtime logs or measurements of the model's actual selections. Holds, active quests and player choices can change the load. Recheck live logs after import.

Public situations use one mechanical script, no semantic query, a shared nine-turn minimum spacing and per-situation memory. It avoids ongoing combat and explicit rest, intimacy, buying or portal movement. A separate small client-return script shares the same spacing. A returning client can acknowledge an actual result once, without generating another debt, reward or job.

## Travel routines

Ragnar Leonhart, Adoha Aonuma and Karia Morino have eight half-day stops across a repeating four-day circuit. The actual day and time-of-day choose a preference. Native npc-placement moves the existing NPC, never a player or a duplicate. An NPC already in the scene, in the player party, fighting, downed, absent from the runtime state or held by an actual commitment is not moved. Explicit long commitments/confinement have pause and release gates. Dead paused characters do not keep consuming a release query.

Adoha Aonuma's Asterveil stops are both in Asterveil Canopy. Karia Morino can visit the maintained remote shelters. Their own standing travel authorization does not give a player a portal key. Their speech, memories, portrait URLs and voice settings remain intact. Ragnar Leonhart's horse stays ordinary lore, not a new authored horse NPC.

## Homes, keys and workshop use

Three paid stays and three purchases are areas in existing locations, with no new map pins:

| Arrangement | Price | Contact |
|---|---:|---|
| Roseberry Attic Room | 30 marks | Inn proprietor |
| Whitepass Drying-Loft Room | 28 marks | Akemi Fushida |
| Canopy Guest Bough | 24 marks | Yuzuri Takase |
| Willowbend Courtyard Cottage | 1,200 marks | Nae Komorida |
| Merchant's Row Bench Workshop | 850 marks | Nae Komorida |
| Snowmelt Landing Flat | 1,100 marks | Atsuko Ōhira |

For these fixed offers, player-scoped native effects remove the quoted marks once and give the correct key/deed to the actual paying person. Conditions require the agreed transaction, funds, location and no duplicate key. Browsing does not pay; mere possession of somebody else's viewing key does not buy a property. Joint purchases should designate the actual payer and ownership terms, not charge every party member silently. Live multiplayer testing remains necessary.

The generic handover rule asks the supported item-generation workflow to retain an individualized key/deed after a different actual acquisition. Native item-add only names an existing itemType; it cannot invent an arbitrary property name/description by itself. Accordingly the six fixed grants are mechanical, while arbitrary new household keys still depend on item generation. We do not claim that story-effect narration alone guarantees a custom inventory mutation.

Keys and deeds have natural descriptions and no stat bonuses. Losing a physical key does not magically undo legal ownership. No rent is deducted offscreen and no eviction timer, passive business income, free stock or endless specialist tools are simulated. Extensions require actual agreement. A home provides space for later play, not a new management game.

## Equipment and combat

Generated/refined equipment now has native allowedBonuses ranges and refinement pick ceilings. Initial/refined picks are Mundane 1/2, Artisan 2/3, Special 3/4 and Legendary 4/5. Native per-pick ranges cover damage, armor, real attributes, actual skills and Health/Mana/Stamina maxima. Generated Time, Renown and Infamy bonuses are excluded. Legendary random generation remains disabled. Existing 360 item definitions—including all nineteen new images—are unchanged; native generation policy is not retroactive catalogue rewriting.

Repair restores function. Refinement changes one actual inventory instance after an agreed result, materials, labor and payment; it creates no duplicate or automatic resource refill. The new starting kits are affordable ordinary weapons and practical combinations, not mastery grants. One kit remains the selection limit.

Weapon-led charges, leaps and dives follow actual Force/Finesse/Guarded delivery; a body tackle remains a bodily action. An infused physical strike is one accuracy resolution, and a detached spell uses its discipline. We do not import Luxcellia's many weapon-family skills into our deliberately different system. Ally orders are not the player's own attack. Tactics, Animal Handling, Summoning or Soul apply only to a genuinely relevant uncertain coordination/control task. Useful allied attacks, protection and finite healing retain native intent budgets and actual results; no unsupported acted-this-turn condition or damage backstop was invented.

Seventy-four existing levels were recalibrated. Academy faculty/headmasters generally occupy 28–32; Archons 52–55; court elites 42–45; Karia Morino 42. Most ordinary working adults remain below that exceptional range. Ilyra Stillglass remains 100 and Ragnar Leonhart 67. Rovakthuun, Orrum, Orivelle and all Spider Realm records are protected. Existing tiers still distinguish training and combat role; a headmaster's office gives no level promotion. Faculty generation bands and AI power anchors agree with the new scale.

## Quest journal repair

Use the complete out-of-character action:

```text
quest done: The Exact Name in Your Journal
```

The script queries the actual runtime quest key or unique name, including a generated quest not in the export. Only accepted work is completed. Hidden, planned, available, abandoned, rejected and completed work is refused. Duplicate same-turn commands settle once. It issues quest-complete, not its own payment; normal completion effects handle rewards. NPCs do not hear the command and no fictional deed is fabricated. This intentionally works on the player's honor. A typo gets a short OOC note, not a fuzzy match.

## Ironman: important distinction

The normal full world adds optional solo Ironman Mode while retaining death.permadeath=false. Like the inspected Luxcellia implementation, its mode/death instructions make lethal outcomes final; a solo Health-zero ending trigger reinforces the result when the semantic fatality/mode condition is recognized. Nonlethal practice, sleep and empty Mana/Stamina do not count.

A game-mode record cannot override the native permanent-death field. For a strict mechanical run, the separate **Native Ironman — Solo** full-world export enables death.permadeath=true and offers only Ironman Mode. Import that as a separate world/copy and start solo. It is not a runtime switch in the main world. The native variant still needs an actual live defeat test; the main world's narrative exception must not be advertised as a hard native per-mode toggle.

## Portrait delivery and remaining manual work

All sixteen portraits were generated once using the built-in image tool, saved as exact NPC-name PNGs, and visually inspected in two QA sheets. They use colorful crisp 2D anime, actual equipment, relevant backgrounds and individual expressions. Some headroom is tighter than the requested target; no unasked reroll or image-edit chain was performed. The source prompts and original outputs are retained. Upload these sixteen PNGs in Studio and populate the currently blank new portraitUrl fields with genuine hosted URLs; no local path or invented upload URL was inserted.

Local checks cover structure/caps, old-record preservation, real script compilation, mocked effects and static eligibility. They are not live Studio or playtest validation. Before release, test native arc surfacing and chapter labels; one winter fight and one negotiated settlement; corrected research evidence; two encounters with the same thief crew; day/half-day schedule movement and commitment holds; a fixed rental/purchase and a generated household key; actual repair/refinement inventory replacement; accepted generated-quest repair and a typo; solo Ironman lethal defeat versus training; and multiplayer transaction recipients. Repeat the simple Bronze opening as a balance smoke test. Existing saved runs can retain old NPC levels, triggers and generated enemies.

## Technical sources

Release verification: 6,491 structural assertions; 1,209 item-mechanics assertions with all 169 real scripts compiled; 572 Adventurers fixtures; and 2,793 preservation assertions. Preservation includes 439 existing hosted media values, all 360 preceding items, all 119 preceding quests and 339 unrelated triggers. Both full-world variants passed local structural validation; all sixteen PNGs and the portrait ZIP were checked. These are local results only.

The shared canonical world, sixteen PNGs and `tools/adventurers/export.py` can regenerate the delivery packages on either desktop or cloud. Run the export script without arguments to package current canonical data; it does not rebuild from an old Alpha or require a private temporary cache.

- Community [Arcs](https://wiki.unofficial.voyage/world/arcs), [Quests](https://wiki.unofficial.voyage/world/quests) and [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): native records, completion/lookup, phases, effects and budgets.
- Community [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings): allowed bonuses and refinement policies.
- Community [Game Modes](https://wiki.unofficial.voyage/other/gameModes), [Death Rules](https://wiki.unofficial.voyage/mechanics/death) and [NPC Intents](https://wiki.unofficial.voyage/ai/generateNPCIntents): actual boundaries and output guidance.
- Supplied reference worlds and Kato's patch notes were inspected as examples. None substitutes for current Studio validation, and their reported rehearsals were not represented as our own tests.
