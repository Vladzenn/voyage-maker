# Tempting Rebirth: feature review and proposed Glowhaven updates

Date: 31 October 2026. Scope: comparative analysis and proposals. The active world was not edited.

## Recommendation

The most valuable next improvements are quest discoverability, equipment consistency, a few dependable daily routines, and persistent social groups outside the player's party. Our world already has substantial content and covers the same eighteen AI task categories as the supplied reference. The next pass should make that content easier to encounter and more dependable during play.

Kato's strongest practice is the feedback loop: identify a concrete player failure, isolate its cause, change the responsible subsystem, and explain what a rehearsal did and did not establish. That is worth adopting alongside the features.

## Sources and limits

Compared:

- User-supplied patch history for *The World After My Rebirth Is Far Too Tempting*; 7,091 lines, including older experiments and their subsequent reversals.
- User-supplied reference JSON, SHA-256 `cf32e15c4100bbdffacf90b3e516d98b9753dfc5fc89d8f6c723e6b4be813baf`.
- Our `world-draft/WorldAlpha - World.json`, SHA-256 `251b27f06704dbe6782e22bfe050af98d280456744c9a03ef5811fe46a7fe400`.
- Current community documentation for triggers, item policies, mods, and voices. These are community technical references, not an independent live-engine test.

**The supplied reference is not a complete verification of the latest patches.** It references three mods, including `G6w21MEkYhdY` version 248. Compared with the older local `LuxcelliaUpdated.json`, the only changed top-level section is `mods`, whose main version advances from 247 to 248. Several base instructions and potion values still describe earlier behavior. The newer changes may depend on the mod contents or their application state; those payloads have not been resolved here. Accordingly, this report distinguishes patch claims from directly observed configuration.

The community [modding guide](https://wiki.unofficial.voyage/mods/modding) describes partial world configurations and versioned dependencies. It also says applying mods writes merged content into the world. A listed version alone does not prove that every patch feature is present in the supplied saved sections. For a definitive implementation comparison, obtain the effective configuration after the current mods have been applied.

No live Voyage playtest, model rehearsal, or Studio import was performed during this review.

## What the files actually contain

| Content | Our current world | Supplied reference base |
|---|---:|---:|
| NPCs | 210 | 372 |
| Locations / areas | 173 / 710 | 279 / 1,603 |
| Realms / regions | 5 / 9 | 2 / 28 |
| Quests | 119 | 380 |
| Abilities | 480 | 1,500 |
| AI task categories | 18 | 18 |
| Root triggers | 309 | 863 |
| Party quest triggers | 0 | 380 |
| Music families / variants | 17 / 38 | 21 / 176 |

These counts describe breadth. They cannot establish encounter quality, runtime reliability, or whether a player will find the content. Our smaller item catalogue is also intentional: the player can acquire generated equipment without hundreds of predefined weapons.

The three recent reference-character review cards are separate from the active 210-NPC roster. Ragnar Leonhart's intended level is now **67**, following the user's adjustment; the earlier local review card still records 90. That older number must not overwrite the user's revision in a future merge.

## Useful features and how they fit us

### 1. Public opportunities that reach the player

**Patch claim:** 59 public situations can appear as local chatter, with a shared fifteen-turn interval, one mention per situation, and exclusions for combat and private scenes. Hearing about something does not automatically accept its quest.

**Our position:** location-generation guidance already permits visible quest situations, and `gh_guild_board` supplies posted offers. There is no comparable general, mechanically paced public-rumor delivery system.

**Proposed update: Word Around Glowhaven.** Start with 12–20 existing situations across markets, inns, academy common spaces and the guild. A queue selects an eligible public situation in an appropriate place and delivers a small visible incident or piece of conversation. The player can investigate, ask about it, ignore it, or walk away.

Examples could concern a faulty enchanted commission, a missing fieldwork delivery, a disputed clan shipment, or an upcoming student duel. These would refer to existing cast and quests wherever possible. Hidden motives, secret lairs, and undiscovered bosses should not become public rumors merely because they are interesting.

Use one shared delivery interval, eligibility checks, and a record of mentioned hooks. Avoid a separate elaborate state machine for every rumor. The interval is a pacing control, not an obligation to inject a hook whenever it expires. Quest acceptance remains a separate action.

### 2. Quest checks that get another opportunity to recognize success

**Patch claim:** completion can consider the most recent scene and the preceding scene; objectives are kept short and observable; ordinary ways of accepting a guild posting are recognized promptly.

**Our position:** we already distinguish acceptance, fieldwork, reporting and rewards, and simple quests use native completion conditions. More scripts are not automatically necessary. The eight newer guild contracts without native completion queries have explicit completion owners; that absence alone is not a defect. The previously questioned offer flags also have a dynamic writer in `gh_guild_board`.

**Recommended refinement:** audit every quest for a clear terminal event, its one completion owner, and its one reward owner. For suitable semantic completion queries, allow narrowly bounded recovery of a recently witnessed finishing event while the quest remains accepted. This is wording and memory discipline, not an invented `previousScene` schema field. Retain stronger state checks when actual inventory, permissions, or alternate outcomes matter.

Do not broaden every event detector. Crime detection, one-time portal anomalies, custody, and current consent have different timing requirements. A historical event must not be repeatedly reinterpreted as a new occurrence.

The community [trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents budgeted AI evaluation for `story` and `action` conditions, with mechanical conditions checked first. It currently lists fifteen semantic checks per turn plus five per active quest. That makes per-scene competition worth measuring; trigger-bank size alone is not the measure.

Static comparison:

- Our 266 root rules containing semantic conditions all have at least one other typed condition; 187 have three or four.
- The supplied reference has 411 such root rules, including five with no mechanical gate, plus its separate quest-trigger collection.
- A broad tick condition may do little to reduce candidates. These counts are not a runtime cost profile or proof that our checks will always be selected.

A useful next audit measures candidates at the guild counter, during an ordinary lesson, in the bazaar, and during dungeon combat. A script-side `skip` runs too late to prevent a declared semantic condition from being evaluated.

### 3. Equipment improvements that preserve the item

**Patch claim:** reforging preserves established bonuses, item cards remain authoritative, consumables restore their displayed amounts, and failed crafting does not silently destroy existing equipment.

**Our position:** four native tiers, price ranges, generation permissions, and bonus-count limits already exist. Our crafting guidance does not spell out bonus preservation and refinement limits as precisely as it could. The tier policies currently set `initialMaximumPicks`, without explicit `allowedBonuses` or `refinedMaximumPicks`.

**Proposed update: Honest Craft.** Keep Mundane, Artisan, Special and Legendary. Define native bonus bounds and refinement ceilings, then give commissions clear before-and-after behavior. A repair restores the commissioned object; a successful upgrade preserves its identity and valid existing features unless a replacement was agreed. Failure has the stated cost, without an invented catastrophe. A promise of an upgrade is not an inventory modification.

The community [item settings guide](https://wiki.unofficial.voyage/mechanics/itemSettings) documents `refinedMaximumPicks` and allowed bonus targets with numeric bounds. These are practical native controls to investigate in a copied Studio world before choosing balance values.

Also test an actual healing item's consumed quantity and actual Health change against its description. A sentence promising healing is not proof that the intended resource update occurred. Permanent equipment bonuses and consumable restoration must not be confused.

### 4. People who can be found, and who have lives beyond the scene

**Patch history:** characters receive ordinary routines and private spaces, while advisers stop repeatedly offering food, rest, referrals, or unsolicited errands. A later patch removes an automatic clock after it incorrectly advanced time from quoted words and ordinary building entry.

**Our position:** autonomy, refusal, knowledge limits and avoiding repeated advice are already covered. Orivelle has an explicit four-day circuit with pauses for scene presence, combat, party membership, confinement and injury. Most townspeople do not have equivalent explicit schedules.

**Proposed update: Lives Between Lessons.** Add a small first set of dependable routines: a clerk's duty location, faculty offices and lessons, a few students' recurring haunts, and the three traveling reference characters once their cards are approved and merged. Use a few meaningful daily blocks. Pause movement during an actual conversation, combat, captivity, or agreed travel.

Make ordinary service access dependable, with sensible cover or opening hours. A schedule that repeatedly removes the only clerk when the player needs them is frustrating. Exact placement should use the existing world time and actual NPC state; do not build a clock from regex matches against words such as “evening.”

A voice-quality pass should protect diversity: older people can be lively, vain, warm, awkward, cruel, or distracted. Existing stern veterans should keep their personalities. “Answer then stop” should apply when the answer is complete, without making every talkative character unnaturally terse.

### 5. Adventurer companies and recurring professional rivals

**Observed reference design:** adventurers can belong to persistent chartered companies, with membership and reputation distinct from personal rank and the traveling party.

**Our position:** the guild, personal badges, service credits, licensure and promotion reviews exist. There is no similarly established company system. Individual issuance already uses player scope and targeted effects, so we should test its recipient handling rather than describe it as missing.

**Proposed expansion of the existing Adventurers of Glowhaven roadmap:** introduce three or four local companies with a small cast each. They can recur as competitors, collaborators, employers or friends without following the player everywhere. Company membership should not automatically recruit its whole roster. Personal Bronze–Platinum access remains separate from a company's reputation, and neither grants court portal authorization.

Start with existing or planned characters and a few linked contracts. Company halls can initially be areas within existing premises. Avoid another compulsory grind meter. Reviews should recognize the actual participants and the quality of their work; multiplayer must test that a spectator does not receive another player's promotion.

### 6. A place to belong

**Observed reference design:** property, rentals, households and ordinary rooms support play outside dungeon progression.

**Our position:** there is general home-and-property guidance and many service interiors, but limited concrete tenancy or ownership progression. For example, Roseberry Inn has a Guest Stair and Seabreeze Inn a Guest Landing, without individual guest rooms in their current authored area lists. Willowbend and Eastbloom establish residential streets and shared spaces, without particular household interiors.

**Proposed update: A Place of Your Own.** Offer a rented room, a student dormitory room, and eventually an apartment or workshop. Add the appropriate private area inside the existing location. Record actual tenancy or installation with an ordinary key, agreement or receipt when useful. Never put maintenance instructions into the document's player-facing description.

The payoff is a place for personal possessions, invitations, domestic comedy, practical projects, and recurring neighbors. Income generation, property markets, and dozens of purchase triggers are unnecessary for the first pass.

## Other worthwhile improvements

- **Skill-routing regression tests.** The reference's healing fix identifies a useful category of failure: the engine selecting the wrong skill. Preserve our dedicated Healing discipline. Light does not acquire Healing, Nature remains plant work, and Water does not acquire Ice because another world's design permits it. Test casting, weapon techniques, Spellcraft creation, Magitech, private Space travel and their actual selected skills.
- **Combat and travel consistency.** Test critical outcomes, nonlethal victory, allied support, escape, and existing-area teleportation. Distinguish a combat reposition from a public portal crossing. Preserve the Evertree hub and court-key policy.
- **Long-rest recovery.** Check the relationship among elapsed time, actual rest and resource restoration. `gh_daily_resource_recovery` currently issues a cue to refill Mana and Stamina when the day counter advances, even without explicitly checking rest. This is an observed rule worth testing against the desired scarcity of Stamina, not a proven live exploit.
- **Boss music.** We already have 38 variants across seventeen families. No explicit pin/clear music effects were found. Selected boss fights and authored gags could gain more reliable musical timing, with cleanup on victory, escape, interruption and defeat. The trigger documentation includes native music pin and clear effects. Avoid leaving a boss theme active through ordinary city life.
- **Instrument and profession expression.** The reference's bard kits suggest useful optional instruments and tools. We already have Performance-related play and Sound abilities; add meaningful equipment choices and interactions without imposing a new mandatory class system.
- **Voice validation.** The three recent review cards contain descriptive tags rather than exact catalogue tags. Adoha's was confirmed during this review. Unknown tags can receive a substitute stock voice according to the community [voice catalogue](https://wiki.unofficial.voyage/appendix/voice-catalog). The user will adjust them manually; this review leaves those cards unchanged. Future validation should flag unfamiliar tags rather than claim a desired accent or celebrity voice has been selected.

## What we are still missing or have not demonstrated

1. **A dependable discovery layer for the content already written.** This is the highest-value content addition.
2. **Measured completion and reward reliability in live play.** Local structural tests cannot show that every finishing event reaches the journal or every reward reaches the right player.
3. **A fully specified generated-item refinement policy.** Native tier foundations exist; bonus bounds and upgrade behavior need a focused pass.
4. **Findable routines for a selected recurring cast.** Authored habits and story-start placements are not complete schedules.
5. **More private, ordinary spaces and modest ownership goals.** Existing locations can accommodate these without expanding the map.
6. **Persistent adventurer social groups.** Companies can support the already planned guild expansion and the player's preference for a few close companions among many acquaintances.
7. **A later-game progression bridge.** The character cap is 150, while most regional danger bands top out around 55. Powerful authored NPCs exist above those bands, but the planned Crucible, chained dragon, Shadowspire and Dreams arcs still need to supply sustained later-game play. This does not require turning Asterveil into an endgame realm.
8. **A repeatable runtime test record.** Preserve screenshots or logs for travel state, inventory, quest state and resource changes alongside the narrative that caused them. Include two-player tests for every personal reward system.

There is no evidence here that we need to triple the roster, reach the ability limit, add every reference species, or give every quiet location a conspiracy. The empty `arcs` and `narrativeEvents` collections are also not automatically defects: our quest chains and event triggers already carry those responsibilities.

## What to leave out

- The reference's multi-school Healing mapping, because it contradicts our established disciplines.
- Its old automatic clock: the patch history itself reports why it was removed.
- Its exact currencies, company names, rarity ladder, isekai powers, and relationship scale.
- Blanket two-scene recognition for crime, consent, custody and all other events.
- A full trigger rewrite merely to resemble the other world's counts.
- Global replacement of our four-chamber dungeon with an eleven-guardian floor structure. The useful lesson is encounter pacing and correct boss placement.
- Hardcoded internal bookkeeping in trophies, room descriptions or other public-facing prose.

## Proposed release order

| Order | Update | Main result |
|---|---|---|
| 1 | Word Around Glowhaven | Public hooks, clear acceptance, completion audit, semantic-candidate measurements |
| 2 | Honest Craft | Bounded generated gear, trustworthy refinements and consumable/resource tests |
| 3 | Lives Between Lessons | A manageable set of routines, varied voices, useful private rooms |
| 4 | Adventurers of Glowhaven | Persistent companies, recurring rivals, targeted personal progression |
| 5 | A Place of Your Own | Rentable rooms, modest home goals and personal spaces |
| Alongside later arcs | Combat and music pass | Later-game challenge, clear outcomes, purposeful boss themes |

These can be combined into fewer releases. The ordering is about fixing access and reliability before adding another large volume of content.

## Minimum acceptance tests for the first two updates

| Test | Expected observation |
|---|---|
| Visit a quiet eligible public place | A relevant hook can occur; no accepted quest is forced |
| Fight or hold a private conversation | Public-rumor delivery waits |
| Return repeatedly to the same place | The same one-time rumor is not repeated |
| Accept a posting in ordinary language | The correct quest appears without a ritual phrase |
| Finish a simple accepted quest | Its actual terminal event is recognized; no additional ceremony is invented |
| Repeat or recall a completed event | No duplicate quest completion, money or item reward |
| Report one player's licensed work in multiplayer | Only the actual eligible participants receive personal credit |
| Repair and then improve a weapon | The actual item and legitimate existing features persist |
| Fail an agreed crafting attempt | Costs match the stated stakes; the original gear is not silently replaced |
| Consume one healing item | Inventory decreases once and actual Health changes by the displayed amount |
| Discard starting equipment | A permanent trait does not regenerate the missing object |
| Cross a portal or attempt private teleportation | Actual realm/location/area and party placement match the narrated result |

The local evidence record is in `research/reference-audits/tempting-rebirth-2026-10-31/verified-comparison.json`; the patch-title index provides the source line numbers for each release discussed here.
