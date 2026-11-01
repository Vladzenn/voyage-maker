# Champions of the Crucible — design and implementation plan

Planning edition 1.0 · 1 November 2026 · **Not implemented in the playable world.**

The aim is a repeatable sporting activity with memorable people and reliable endings. Its machinery must distinguish a real result from an attractive sentence about winning. This document supersedes the provisional Crucible chapter in the older seven-update blueprint. Names, cast concepts, counts beyond the approved fighter pool, and balance values below remain proposals.

Baseline: `world-draft/WorldAlpha - World.json`, SHA-256 `3c8203be654cd4d38cde5e356dafdb458da38210290c37ef9b6fa1530d9d3464`. Rebase implementation onto any newer supplied Studio export. Preserve images, coordinates, audio, voices and user edits.

## Decisions confirmed during this planning session

- Individual championships first; team championships are a separate later extension.
- Regulated bouts are nonlethal, including in Permadeath mode.
- Championship cooldown: **100 completed game turns**, using the engine tick rather than narrated dates. Ordinary sparring remains available.
- Full Health, Mana and Stamina recovery between bouts through actual medical treatment, once per finished bout.
- Finite learned summons are legal; attacks, healing and buffs from outside companions are prohibited during a live bout.
- Leaving the venue between bouts withdraws the entrant from that edition. Departure during a live bout normally forfeits it. A genuine emergency stoppage is handled separately.
- About **32 new named fighters**, supplemented by suitable, willing existing characters.
- New dungeon: Nature and Soul magic, plant-bodied undead golems, approximately **levels 35–50**.
- Its portal appears at the Evertree Portal Room when a player carries a Crucible championship trophy and the existing **Silver Web Portal Key**. No spider-queen victory requirement was requested.
- Oni content in this release is preparation through lore and small ancestry adjustments, not the Oni country expansion.
- Additional abilities and shady work in Glowhaven and Drakenspire belong in this package.

## What is already present

The Eternal Crucible has an Arena Floor, Grand Stands, Concourse and Competitor Passage, a hosted establishing image, and coordinates the user arranged. Keep those addresses and artwork. Add interior areas rather than another arena location.

Tomoe Enokida, level 28, is the existing competitor-arrival coordinator. She has her own history and should remain a person, not become the implementation's all-purpose referee, surgeon and prize dispenser. Ragnar Leonhart currently starts here at level 67 and has a touring routine. His presence does not mean that he competes in every edition.

The current lore prohibits mana potions and external stored-mana assistance during official tournament duels. Ordinary control catalysts are allowed; emergency treatment after stoppage is permitted. Keep these rules and their evidence-based enforcement.

`gh_lore_tournament_start` and `gh_lore_tournament_stop` currently recognize an official duel and record its opening/closing. They do not create a bracket, seed entrants, determine a champion or award a trophy. Their active flag also applies to academy tournament duels. The new system must not take ownership of those unrelated academy activities.

There is no configured championship trophy. The exact existing dungeon key is **Silver Web Portal Key**, not a newly invented “Silken Depths Key.” That item is issued on first arrival, so it separates this discovery from an untouched anomaly playthrough in normal play. Item possession is not proof of defeating Vhalessra.

## Evidence and platform boundaries

| Evidence | Useful conclusion | Boundary |
|---|---|---|
| [Voyage Patch 2.43.0](https://voyage.io/whats-new/patch/patch%3A100001188) and [2.45.3](https://voyage.io/whats-new/patch/patch%3A100001203) | Native NPC health, placement and combat-membership checks exist. | These are building blocks, not a tournament service. |
| [Community trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) | Tick reads, JSON-shaped persistent storage, mechanical/semantic gates, typed effects and planning/state phases support a small competition controller. | Scripts execute after conditions; semantic recognition remains fallible. Effects and scripts have budgets. |
| [Game Modes](https://wiki.unofficial.voyage/other/gameModes) | These are creation-time instruction/difficulty packages. | They do not supply a bracket lifecycle. |
| [Arcs](https://wiki.unofficial.voyage/world/arcs) and [Quests](https://wiki.unofficial.voyage/world/quests) | Useful for a rival's developing story or finite work. | A generated arc should not choose championship results or replay a final. |
| [NPC Intents](https://wiki.unofficial.voyage/ai/generateNPCIntents) | Combat attempts resolve before their narration; present actors and real participation matter. | Neither an intent nor a story announcement proves a win. |
| [Death Rules](https://wiki.unofficial.voyage/mechanics/death) | Native permanent death is world-wide. | No documented per-bout safety switch was found. |
| [Resources](https://wiki.unofficial.voyage/mechanics/resourceSettings) | Native bars and treatment/rest rules already exist. | Character resource maxima vary with traits and growth; do not derive them from level alone. |

Current official release notes and the community reference were checked on 1 November. No documented tournament/bracket API or native per-match nonlethal toggle was located. This is a finding about the available evidence, not a promise that an undocumented feature cannot exist.

Reference audit: the newer creator export supplied in attachment `5f2c3317-f5d6-44fd-aabf-64f3b95caeb0` has 863 triggers; its file SHA-256 is `cf32e15c4100bbdffacf90b3e516d98b9753dfc5fc89d8f6c723e6b4be813baf`. It includes `delve_enter_the_mirage_colosseum`, a reusable `delve_*` progression family, local activity state, and tournament-related quest chains. Bracket mentions in Rival's Confession and Rookie's Festival are narrative quest objectives; this inspection did not find a complete reusable eight-entrant bracket/result ledger. Borrow its locality, reusable configuration and specific social hooks; do not claim its arena text is a tested sports engine. The older `sources/Luxcellia.json` and `sources/ChikaraOld.json` contain tournament lore but no root trigger bank. All reference material stays unchanged.

## Architecture: a persistent world activity

Use one active championship edition per adventure/party. This does not mean a tournament shared between unrelated saves or servers. Registration is opt-in at the Crucible; no worldwide summons, mandatory academy milestone or unsolicited tournament quest.

Keep four responsibilities separate:

| Component | Owns |
|---|---|
| Competition controller | Edition, fixed roster, bracket, legal result, advancement, settlement and cooldown |
| Native combat | Actual attacks, checks, damage, incapacity and surviving state |
| Narrator and NPC dialogue | Presentation, banter, tactics, hospitality and responses to recorded developments |
| Native quests/arcs | Distinct undertakings involving people, crime, teaching or the new dungeon |

The controller is justified here because this activity repeats, branches and pays prizes. It is not a template for converting every new quest into a state machine.

Do not create one repeatable native quest for each bout. There is no verified general quest-reset API in this plan. A finite introduction quest may acknowledge a first actual bout, win or lose; its completion gives no championship trophy. Later editions use the activity record and ordinary venue announcements. Existing `quest done:` repair must not settle a bracket or award its purse.

### A small, inspectable ledger

The following is a **proposed application data shape inside supported storage**, not new WorldConfig fields:

```text
storage.cc1 = {
  version, editionSerial, titleId, divisionId, phase,
  entrant, roster[], matches[], currentMatchId,
  registeredTick, closedTick, nextEligibleTick,
  champion, participantOutcome, payoutStatus,
  recoveryForMatch, originalPlacements[], history[]
}

match = {
  id, attemptSerial, round, left, right, arenaId,
  startedTick, resultTick, winner, loser, reason,
  resultSource, reviewed
}
```

Phases: `registration → ready → live → medical → ready`, followed by `settlement → closed`. `review` holds an ambiguous match without declaring a result. Withdrawal is a terminal participant outcome, while the remaining bracket can still acquire an NPC champion.

Use a few flat mirrors only when native trigger conditions need them, such as `cc1_active`, `cc1_phase` and `cc1_next_eligible_tick`. The controller is their sole writer. They are cached views, not independent authorities. A build manifest names every reader/writer and reset rule.

Store only JSON-shaped values. Never place functions, Maps, Sets, circular objects or engine entities in persistent storage. Keep recent sporting history compact; retain championship identities and payouts without an endlessly growing prose log.

### Invariants

1. A match has zero or one settled winner. Its result can be committed once.
2. A fighter eliminated in this edition cannot advance again in it.
3. The next match uses the winners of its actual parent matches.
4. A final cannot be created after that edition has settled.
5. One component owns money and trophy issuance; no quest or narrator issues a second award.
6. Leaving, losing or withdrawing cannot convert into “not finished yet” championship progression.
7. Healing never clears a recorded loss. Friendly rematches never reopen an edition.
8. A missing NPC lookup is unknown, not zero Health or a victory.
9. Treatment, publication of results and cooldown are independent of whether the player admires the ceremony.
10. A stored ledger is not automatically narrator context: transitions supply a concise factual scene brief, and the venue's activity instructions preserve it.

## Editions, divisions and opponent selection

Propose four seasonal presentation families: **First Bloom Cup**, **Highsun Clash**, **Harvest Crown** and **Frostglass Championship**. Each can have an edition number, visual decorations and a favored layout. Their season names are sporting traditions; no fragile season calendar gates registration.

Select the title and candidate roster once when an eligible edition is offered. Confirm the bracket at actual registration. Re-entering a room, reloading a scene, inspecting the board or declining cannot reroll it repeatedly. Refresh only through a deliberate new edition or a genuinely invalidated roster.

Default to eight entrants and three player bouts. A four-entrant novice card is a useful fallback when there are not seven genuinely suitable opponents. Never fill an underpopulated beginner bracket with much stronger people to satisfy the number eight.

Selection process:

1. Determine the registered fighter's actual level and relevant capability. For individual bouts, nonparticipating companions do not raise the division. Future team divisions can use their registered members' average with a check for a highly uneven team.
2. Offer a division suited to the entrant. Announce the field's level/risk range before commitment.
3. Filter authored candidates for range, availability, willingness, injuries, existing commitments and previous encounter state. Do not select dead, incapacitated or actively accompanying party members as automatic enemies.
4. Choose without replacement and store the result. Spread matchups across martial, spellblade, ranged, control and support-oriented styles. Relationships influence chemistry, not a guaranteed winner.
5. If the candidate band is sparse, propose a smaller card or another division. Entering a more dangerous field requires an explicit informed choice.

Suggested divisions are **Initiates**, **Rising**, **Veteran** and **Crown**, populated through overlapping candidate bands rather than hard-coding everyone into broad level buckets. Begin low-level tests with opponents within about two levels; widen the allowed difference gradually and test actual damage and tier action counts. Level alone is not balance. Initial high-level coverage must be announced honestly: do not invent multiple level-120 residents merely to match every possible level-150 player. A high-level entrant can enter a lower available field knowingly or wait for a deliberately authored exceptional division.

Keep Ragnar Leonhart at 67, Ilyra Stillglass at 100, and every existing authored level unchanged unless separately approved. An official does not need exceptional combat power just to run the tournament.

### Thirty-two new competitors

Allocate provisionally: eight developing fighters, twelve trained competitors, eight seasoned veterans and four exceptional headliners. Rebalance this distribution after the first candidate-coverage audit; all eight-entrant fields need enough alternatives. Most new adults should not become level-60 prodigies. Selected existing academy students and adventurers add variety where the band fits.

Make the pool interesting outside brackets. Suggested people include a dockworker whose chain techniques began at work; an immaculate noble shield duelist who is atrocious at small talk; a cheerful undertaker practicing Soul wards; a sleep-deprived parent competing for a school fee; a boastful loser whose opponent analyses are excellent; a retired soldier learning performance magic; a deaf Sound specialist with a carefully authored casting method; and a traveling oni bodyguard who misses home cooking. These are concepts, not yet named cards.

Each card needs a livelihood or studies, two ordinary pleasures, a real flaw, at least one named relationship, a reason to enter or decline, and something to discuss after elimination. Elimination belongs to an edition, not a permanent NPC trait. Defeat need not create hatred; kindness need not make someone easy to beat.

Add roughly four staff around Tomoe Enokida: a referee, two complementary medics and an announcer/registrar. Reuse existing contacts where that makes sense. Separate crime contacts need not all be tournament regulars. Full JSON cards and portraits belong to implementation, after the combat prototype passes.

## Bracket simulation without an invisible combat campaign

Create the complete bracket on registration, but do not predecide the player's results. NPC-only pairings can use a small recorded sporting resolution, based on authored capability plus a bounded stored draw. Resolve each when its round becomes relevant, once. This represents the tournament's other bouts; it is not a fake native combat trace and cannot fabricate actual wounds, deaths or loot.

The player can hear an announced result or meet the winner afterward. They need not watch six fights to reach their own. Ordinary conversation cannot overturn a recorded result. If sabotage or a real emergency disrupts an upcoming match, record an official stoppage, replacement or walkover before advancement instead of pretending the scheduled fight occurred normally.

When the player loses or withdraws, settle their exit immediately. Resolve the remaining NPC field in a bounded summary, name its champion, archive the edition and start the cooldown. No mandatory spectator quest. There must not be a permanently active semifinal waiting for an absent player who already lost.

## Result authority and unexpected actions

The documented engine exposes some numeric combat state and some semantic events. It does not expose a verified universal `getBoutWinner()` function. These are implementation rules, not claims that every result has a direct API.

| Situation | Intended result |
|---|---|
| Registered fighter is actually knocked out or medically stopped | Loss, regardless of celebratory prose |
| Current opponent is actually defeated in this bout | Win, provided the player was not also stopped |
| Both fall in the same exchange | Medical stoppage and referee review; never automatic player victory |
| Actual surrender is accepted/recognized | Loss for the conceding side |
| Player declares “I won” without a resolved result | No advancement |
| Someone discusses a prior defeat | No new result |
| Opponent has low Health before the opening bell | Unfit entrant; replace or postpone before starting |
| Opponent disappears or cannot be resolved | Review; absence alone is no victory |
| Player leaves the active ring to another arena or venue | Forfeit unless an authorized emergency stop explains it |
| Player leaves the Crucible between bouts | Withdrawal; completed results remain |
| Player leaves after winning the final but before collecting | Championship remains won; agreed unpaid prize stays claimable once |
| NPC eliminated last edition enters a later edition | Legal if willing and fit |
| All remaining opponents withdraw | Official walkover can settle the championship; no invented combat XP |
| Known cheating or outside interference | Referee ruling under announced terms; no hidden automatic guilt |

Priority: confirmed withdrawal/stoppage and actual incapacity must be reconciled before awarding a player win. Do not heal first and then infer that a knockout never happened. Freeze the result before medical effects. A result review is preferable to inventing a champion, but it must have a way out.

An exact OOC **Crucible status** command can report edition, bracket and the last recorded result. A proposed **Crucible review** command asks the referee to reconcile the current match against actual evidence. It is distinct from `quest done:` and is not an unconditional “give trophy” command. Unresolvable contradictory state should cancel or schedule a clearly announced replay, with player agreement and no duplicate fee. It must never erase a verified loss to make a quest finish.

### Settlement pseudocode

This is implementation design, **not a claim that uppercase helpers are Voyage APIs**. The future implementation must translate each observation into documented native checks or a narrowly gated semantic condition. There is no free-form `check()` call that asks the AI to decide an arbitrary question from inside a script.

```text
RECONCILE_CURRENT_MATCH(observation):
    edition := current stored edition
    match := edition.currentMatch
    if edition.phase != LIVE or match.resultTick exists: return NO_CHANGE
    if observation refers to another edition, fighter or match: return NO_CHANGE
    if required actor data is missing: enter REVIEW; return

    # Current native evidence outranks narrator celebration.
    if both contestants actually incapacitated: enter MEDICAL_REVIEW; return
    if entrant actually incapacitated: outcome := OPPONENT_WIN
    else if current opponent actually incapacitated: outcome := ENTRANT_WIN
    else if verified entrant surrender/forfeit: outcome := OPPONENT_WIN
    else if verified opponent surrender/forfeit: outcome := ENTRANT_WIN
    else if actual official disqualification: outcome := VERIFIED_RULING
    else: return NO_CHANGE

    if evidence conflicts about ordering or legal participant: enter REVIEW; return
    commit one result with reason, source and tick
    mark the actual loser eliminated in THIS edition
    if entrant lost:
        close entrant participation
        finish remaining NPC-only bracket once
        close edition and schedule cooldown
    else if this was the final:
        record champion
        prepare the single prize settlement
        close sporting competition and schedule cooldown
    else:
        enter MEDICAL
        prepare this match's one recovery entitlement

TREAT_COMPLETED_MATCH(actual_treatment):
    require completed match and actual registered recipient
    require no active combat and recovery not already dispatched
    issue the supported full-recovery effects
    record that recovery belongs to this match
    prepare next bracket match only after recovery is confirmed

PREPARE_NEXT_MATCH:
    require both parent matches have settled winners
    require neither winner is eliminated or unfit
    require chosen arena and opponent identities are already recorded
    place the actual available opponent; announce the real matchup
    await the fighter's readiness and the official start
```

Do not let a native defeat check and a semantic surrender check settle the same match separately. Both feed the same guarded settlement operation. The serial and result marker prevent a scene from replaying that operation; tests must also cover duplicate observations in one tick. A review is a held current match, not another final appended to the bracket.

An authorized replay gets a new attempt serial while preserving the stopped attempt's reason. It does not erase a verified defeat. A replay's medical entitlement and any fee adjustment explicitly refer to that new attempt, preventing an old treatment marker from blocking legitimate care or being reused for unlimited healing.

### Nonlethal prototype: the main release risk

Preserve subdual intent in Action Info, NPC Intents and narration. Use referee stoppages before dangerous continuation and treat genuine knockout as defeat. Consider a published technical-stoppage threshold as an additional safeguard, but only after testing real Health maxima and same-turn ordering. A low-health rule cannot prevent an unexpectedly lethal single hit by itself.

Do not turn native Permadeath off and on around a bout. It is global and could protect the wrong event or player. A planning-phase health reaction is also not proof that death resolution has been safely intercepted. Test nonlethal exchanges in both the ordinary optional mode and the separate native-Permadeath export. If native permanent death still kills a regulated knockout, do not claim safety: investigate a documented engine solution before advertising regulated championships as safe in that export. AI instructions and revival prose are not substitutes for a native guarantee.

Ring-out, surrender and referee technical stops are useful additional endings. They should not become a contrivance that prevents actual fights merely to hide the engine risk.

## Recovery and championship rules

Add a **Competitor Lounge** and **Infirmary** within the existing location. Register at the current passage/counter, introduce one or two actual opponents in the lounge, enter the assigned arena when ready, fight, settle, and visit medics before the next bout.

Recovery belongs to the completed match serial. Actual treatment restores the registered fighter's Health, Mana and Stamina fully once; it grants no maximum increase, inventory restock, reserve item, cleared cooldown or erased withdrawal. NPC opponents receive their own appropriate recovery. Do not heal all scene NPCs or outside companions by accident. Never rely on the world's daily NPC healing to prepare a same-day semifinal.

Use supported native resource effects and verify actual maxima and targeting in a live prototype. Do not reconstruct a maximum from base + level alone: traits and other modifiers exist. If capped resource-fill behavior cannot be demonstrated, this is an implementation question to resolve before the full bracket, not permission to add an unsupported `restoreAll` effect. NPC resource handling also needs its actual supported route rather than invented `npc-mana` or `npc-stamina` effects.

Post the rules before entry: nonlethal subdual, surrender, referee stoppage, physical boundaries, permitted equipment, finite summons, no outside assistance, no mana potions/reserve batteries during a bout, treatment after it, fee and purse. Illusions, feints and legal traps are tactics; a failed spell is not cheating. Ordinary catalysts remain legal. A summoned helper must be a real supported participant/technique, with actual costs and action limits, not an unbounded extra hit.

A trophy and agreed prize have exactly one settlement owner. Propose a native **Crucible Championship Trophy** item with natural commemorative prose and no concealed instructions. Keep the canonical item identity across editions; the activity history records which title was won. Losing or discarding an issued trophy does not cause automatic reissuance.

Keep a payout marker per edition. All monetary/item effects fit one bounded settlement packet. Validate after applying it rather than declaring ACID transaction guarantees the engine does not document. If a script/effect error leaves dispatch uncertain, record it for review; blindly paying again is not recovery. Optional later winnings must not duplicate combat XP already awarded natively.

### Cooldown

```text
ON official edition closure:
    closedTick = engineTick
    nextEligibleTick = closedTick + 100

ON voluntary request for another championship:
    offer only when no edition is active
    and engineTick >= nextEligibleTick
```

Compare the native tick directly; do not increment a custom timer in several phases. A narrated “three months later” does not necessarily advance 100 ticks. Until a documented effect for game-tick advancement is available, do not promise that sleeping or a calendar skip bypasses this cooldown. Show the remaining turns on request. Exhibition matches, lounge conversation and learning keep the venue useful during the interval.

## Six genuinely different arena layouts

Use actual authored areas inside the existing Crucible, not merely six names for the same floor. Present the assigned terrain before the fighter commits to the bout. Choose without replacement across one edition where possible. Store each choice, so it does not reroll midfight.

| Layout | Physical design and interesting choices |
|---|---|
| Open Ring | Existing floor; clear sight lines, marked safe boundaries and room for movement |
| Pillar Court | Staggered solid pillars; deliberate cover, flanks and destructible cover already established in the scene |
| Verdant Ring | Waist-high growth, two shallow channels and clear raised paths; concealment and footing without universal plant obedience |
| Frostglass Platform | Icy central dais, broad low side platforms and safe stopping margins; balance, displacement and route choice |
| Broken Stair Arena | Three low connected elevations; controlled approach and plunging angles without lethal falls |
| Mirrorwater Garden | Shallow reflective water and stone islands; visual deception and channels without automatic electrocution |

State the limits of each structure. Cover changes persist for the rest of that bout; an announced arena reset prepares the next bout. No unannounced hazard rotation. Mechanical positioning remains engine-interpreted; these areas are not a new tile-based combat system. Spectator safety and legal ring-out boundaries are consistent.

Use the actual chosen area for native geography and scene art. Clicking a different arena is movement, not an automatic fight, advance or new layout. A live-match departure is handled by the result controller. Do not put lethal chasms under a supposedly nonlethal platform.

## Multiplayer and companions

Individual bouts mean one registered player, not “the whole party may attack.” Native party travel is shared; there is no promised independent teleport for one player. Spectating players and authored companions may remain present but cannot add attacks, healing, buffs or stored mana during a regulated match.

A temporary registered-entrant trait can help native player-scoped effects target the right person, but matching must be tested. A stored display name is not a guaranteed immutable player ID. Renames, joining/leaving players and multiple simultaneous registration actions must not change the entrant silently. One party has one active edition; do not run parallel independent rings in version one.

Release gate: demonstrate that a spectator's low Health does not eliminate the entrant, treatment/prize effects do not reach spectators, and possession tests do not pool different people's inventories. If current targeting cannot support this, restrict championship registration to single-player adventures initially and explain that limit; do not disable multiplayer in the world as a whole. This fallback is a proposal, not yet a user-approved blanket restriction.

## The new dungeon: The Sepulchral Conservatory

**Proposed premise:** an abandoned sanctuary tried to grow new bodies for the dead. Nature magic made the vessels; Soul magic maintained their impressions and commands. The conservatory kept tending them after its keepers disappeared. Its guardians are timber, bone and funerary growth rather than ordinary zombies wearing leaves.

Proposed conflict: a caretaker believes no soul under its charge can safely leave. Some vessels hold recognizable spirits; others are empty animated frames. Distinguish those cases in encounter lore. Avoid a revelation that every creature is secretly harmless, and avoid making every undead automatically irredeemable.

Possible ending: destroy the binding heart, persuade the caretaker to release its charges after solving the actual failure, or redirect its work through a credible costly alternative. Combat remains substantial; negotiation should follow discoveries and action, not one flattering sentence. The final boss and threat cessation have a single recorded resolution and reward owner.

Propose one new realm, one region, a ruined **Portal House**, the main **Conservatory**, and a smaller optional **Mourning Garden**. Put most chamber detail in roughly twelve connected interior areas rather than many redundant map locations. A sunken rotunda branches through root walks, a memorial orchard and an ossuary greenhouse before the grafting heart. No full-world map or new nation is implied.

The target is levels 35–50. Start with small guardian packs, readable hazards and usable retreat routes. Propose a named level-50 strong caretaker, **Threnvoss, the Rootbound Regent**, subject to balance testing. Ordinary enemies are npcTypes: Gravewood Golem, Rootbound Pallbearer, Censer-Willow, Hollowseed Swarm, Ossuary Trellis and a finite elite graftguard variant. Only genuinely individual beings need authored NPC records.

Use local encounter instructions and actual supported generation to register those npcTypes as actors. A story effect requesting a pack is not a documented native spawn command; do not invent `spawnNpcType` or report precise enemy counts as guaranteed until tested. Small packs must actually exist before dealing damage. Soul is a discipline, not currently a configured damage-type string: route effects through appropriate existing `nature`, `bludgeoning`, `psychic` or `dark` types unless a separately reviewed change adds a native type. Never write unconfigured resistances or assume Nature and Soul are interchangeable.

Nature affects living plant structures; Soul interacts with the binding. Fire can damage dry growth but may threaten trapped spirits or create smoke; it is not an instant dungeon-delete button. Noncasters can cut exposed supports, exploit the irrigation system, read memorials, protect a specialist or hire help. No required unique affinity or mandatory consumable solves every route.

### Portal discovery and travel

Exact discovery conditions:

```text
actual location = Evertree Base
actual area = Evertree Base - Portal Room
same qualifying player carries Crucible Championship Trophy
same qualifying player carries Silver Web Portal Key
new portal has not been discovered
no portal transit has already claimed this turn
```

Opening reveals the authored route and describes a new arch. **It does not transport anyone.** Crossing requires a separate committed action. The return goes directly to Evertree Base - Portal Room. Reveal can remain permanent once discovered; trophy/key possession is the discovery gate, not a new repetitive toll. Propose a retained route key on first arrival, with natural inventory prose, if the public network needs one.

Use a new portal-reveal owner and respect the existing `ghPortalTransitTick` lock. This should coexist with the unchanged anomaly, not replace its conditions or force another examination. The required silver key normally follows anomaly entry; the additional discovery must not turn one outward crossing into two competing teleport effects. If ordinary transit already owns the turn, defer the revelation. No automatic reveal while the party is narratively home but mechanically elsewhere.

Test false positives: only trophy; only key; items split between two players; a mention or drawing of either; a forged differently identified item; wrong room; final victory without the actual carried trophy. Exact possession remains the user's intended switch, not an anti-cheat security system against Studio-generated items.

Dungeon progression can reuse the existing project's successful local encounter and access lessons without modifying the Silken Descent. Test map/area clicks, optional branches, retreat and cleared-room persistence. Do not declare a `paths` array an impenetrable travel lock. Implement only the few gate rules actually needed after that test.

## Oni lore preparation

The new direction combines an Edo-inspired countryside and towns with trained samurai, shinobi and independent factions in a wider political society. Keep the earlier Shogun, distinct settlements, broad fields, wilderness and yokai. Do not reduce the nation to a single neon city or a copy of one academy culture.

Magitech is locally more developed than in Glowhaven in particular applications and is based mainly on Arcane and Soul techniques. Propose spirit-message relays, discreet warded tools, articulated prosthetics and workshop machinery alongside paper screens, wooden streetscapes and agricultural life. There is less conspicuous wiring and no carved-face mountain. “More advanced” does not mean ubiquitous modern electronics, firearms or an automatic industrial economy.

Future independent houses, martial schools and mission-taking organizations can produce the desired political texture. Avoid importing chakra, tailed beasts, Leaf Village, Kage titles or another franchise's named factions as canon. The country's name, mapped towns and specific organizations can be authored during the actual expansion.

This release should add focused lorebook entries for society/governance, traditions of samurai/shinobi, Arcane–Soul magitech and yokai. Reserve the mysterious Soul-emitting torii and its quest-item spirit route for Portal to Oni City. No destination, new start, open spirit portal or travel permission ships just because its lore is mentioned.

The Oni ancestry remains humanlike, individually horned and varied. Remove the obsolete implication that no homeland has been established once the lore entries exist. Keep its current +1 Force, +2 Intimidation and +15 Health unless a separate balance reason is approved; culture does not grant every oni Soul affinity, ninja training or a new weapon. Optional horns, complexion and small fangs can add visual variety without changing species into monsters.

## General ability expansion

The current catalogue has 534 abilities and 20 public magic disciplines. Most disciplines have twenty directly gated spells: six through skill 15, seven at 16–40, four at 41–70 and three above 70. Cross-discipline entries inflate some counts, notably Gravity; a raw reference count is not proof it has twice the distinct useful repertoire.

Flexible target: **about 160 additions**, taking the catalogue to roughly 694:

| Group | Planning allowance |
|---|---:|
| Twenty public disciplines, six useful additions each | 120 |
| Force, Finesse and Guarded techniques, eight each | 24 |
| Mixed/spellblade techniques filling real gaps | 12 |
| Magitech techniques | 4 |

For each discipline, aim for two foundation, two trained, one advanced and one mastery technique. These are skill bands, not character levels. Every entry needs a distinct use: movement, control, protection, interruption, terrain manipulation, recovery, utility or a meaningful attack trade-off. Replace redundant concepts in the plan instead of writing six renamed bolts.

Proposed naming: **Cinder March**, **Thunderclap Reversal**, **Mourning Bell Release**, **Iron Orchard**, **Paper Moon Feint**, **Crownless Meteor**, **Gatebreak Shoulder**, **Needle After Rain**. Flashy names must still explain range, target, cost, limitation and effect plainly. These are examples, not approved catalogue records.

All abilities use supported `bonus`, `cooldown` and complete requirement records with numeric `amount`, including trait requirements. Do not turn prose into unconfigured auto-hits, guaranteed stuns or extra turns. Preserve resource cost ownership and existing starting repertoires. No new universal discipline-acquisition gate; Spellcraft still governs invention. No public Time spells or Space creation shortcut. Learned tournament tricks should be a few earned optional opportunities, not thirty-two mandatory tuition chains.

## Shady work and new crime contacts

Propose eight finite native quests, four in each city, with about six new contacts who have independent lives. Most need ordinary typed completion conditions and a single reward owner. They do not need eight new police-state subsystems.

| Realm | Working premise | Credible choices |
|---|---|---|
| Glowhaven | An unlicensed enchantment repair is being sold as certified | Perform illicit work, expose it, refuse, or arrange legitimate repair |
| Glowhaven | A collector pays for diverted confiscated goods | Steal, substitute lawful recovery, inform the owner, or walk away |
| Glowhaven | A bookmaker offers money to throw a real bout | Refuse, report, or deliberately lose; no fake champion award |
| Glowhaven | A forged recommendation is needed for a restricted commission | Forge, obtain genuine sponsorship, expose the broker, or decline |
| Drakenspire | A dealer wants sacred shed scales diverted before clan inspection | Smuggle, return, renegotiate authorized purchase, or expose the buyer |
| Drakenspire | A mine tally understates crystals owed to another household | Alter records, investigate, negotiate, or reveal the scheme |
| Drakenspire | A fence offers payment for a stolen heirloom blade | Fence it, identify its owner, negotiate restitution, or keep the dispute alive |
| Drakenspire | A rival trader hires sabotage of a delivery | Sabotage, warn the carrier, fake cooperation with real consequences, or refuse |

Do not reveal hidden motives through a quest title or offer. People can be selfish, funny, frightened or genuinely malicious without becoming quest kiosks. Local discovery only; no simultaneous stack of all crime offers on entry.

Preserve the approved automatic wanted-poster scope. Theft, smuggling, forgery, torture alone and ordinary fraud do not suddenly invoke the deliberate-killing/multiple-building-destruction loop. They can still have ordinary local, commercial and relationship consequences. Drakenspire does not automatically ship offenders to Wraith Island through Glowhaven's arrest system.

## Trigger and prompt budget

Propose roughly a dozen reusable competition trigger responsibilities rather than per-fighter/per-round copies: registration, dispatch, mechanical result reconciliation, semantic concession/ruling, withdrawal, medical settlement, prize settlement, cooldown offer, exhibition consent/result, and review. Some can share a safe dispatcher; others must remain separate because they run in different phases or target different players. The final count follows the prototype, not a quota.

Relevant native gates precede semantic checks. At rest there should be no worldwide “did someone win a tournament?” query. During a bout, expose only its result/withdrawal/ruling checks. Scripts do not prefilter the semantic conditions in their own trigger. Do not make a controller recompile the entire trigger bank every turn.

Baseline headroom: 378 root triggers, including 330 with a semantic `story` or `action` condition. The current reference allows 500 semantic trigger definitions but only 15 semantic checks per turn before active-quest allowances. Aim for zero added competition queries outside the venue/activity, and at most two or three eligible during a bout. Re-run the existing scene-budget probes with ordinary quest checks included; collection headroom is not per-turn capacity. These counts are an inspection of this baseline, not a live engine trace.

The existing start/stop lore triggers remain useful for academy duels. Give the new Crucible controller sole ownership while its activity is active, preventing the old handler from clearing its flags or medical rules early. Prefer a narrow active-activity exclusion to rewriting unrelated tournament behavior. A new portal uses the existing transit lock, not a second competing global travel system.

Prompts receive the minimum needed current activity fact: registered fighter, opponent, selected arena, rules and actual latest result. Put private IDs, payout guards and storage instructions in scripts/development notes, not trophies, public room descriptions or spoken announcements. A past champion is a known person, not an excuse to generate a duplicate record.

Music can use the current combat cue initially. If a championship theme is later pinned, give it an owner and release it only for that bout's actual ending; do not let a joke or unrelated clinic scene clear another event's music.

## Implementation sequence and proof gates

1. **Evidence prototype.** Two existing consenting test actors, one ring, one registered player. Prove native combat participation, knockout ordering, nonlethal outcomes and positive-Health surrender. Test ordinary and native-Permadeath variants. No new portraits yet.
2. **One four-entrant edition.** Fixed roster, one layout, result ledger, loss/withdrawal, treatment, payout and 100-tick cooldown. Exercise every terminal route. Do not enlarge a broken prototype.
3. **Full competition engine.** Eight entrants, fixed-seed offscreen pairings, optional review, multiple layouts, exhibition-only activity and scoped multiplayer if proved. Produce a state-writer manifest and eligibility/budget probes.
4. **Cast and presentation.** Author the thirty-two fighters and supporting staff in reviewed batches, with relationships and portraits. Roster selection uses actual records. Add cup families, lounge dialogue and a modest teaching offering.
5. **Dungeon.** Add the new realm and return route, Nature/Soul encounters, named caretaker, local progression, one investigation arc or short questline and its separate settlement. Prove the championship/key discovery alongside the untouched anomaly.
6. **Bundled content.** Review ability gaps, generate bounded batches, add crime contacts/quests and focused Oni lore. These do not silently change tournament result rules or expand the Oni map.
7. **Release merge.** Merge the latest Studio export, preserving media/order. Validate full and section files, publish concise public notes under the major update title, and retain private test evidence. Do not present planned content as shipped.

### Required scenario matrix

Run local fixtures against the actual emitted scripts, then manually repeat critical paths in Voyage. Fixtures are not live playtests.

- Registration refusal, insufficient fee, repeated registration, duplicate action submission, save/resume, no legal candidate pool, already dead or committed opponent.
- Ordinary win, real knockout loss, simultaneous incapacitation, surrender, false victory claim, stale prior victory, missing NPC value, wrong NPC harmed, positive-Health concession.
- Leaving during a bout, entering another arena, leaving between bouts, visiting the infirmary, stepping outside to shop, returning after withdrawal, leaving after a settled final.
- Each NPC-only match resolves once; eliminated entrants never reappear in that edition; another edition can include them normally.
- Full treatment only once per completed bout, no spectators healed or rewarded accidentally, no reserve duplication, no reset of native cooldowns.
- Final winner paid once; reload/return, lost trophy, unclaimed prize and dispatch error do not duplicate it; friendly wins do not count as championships.
- Cooldown at closure +99 and +100; no double counter increments; no repeated final or automatic next edition; calendar-skip prose alone gives no tick credit.
- Terrain is genuinely present, chosen once, and affects actual movement/cover. No map click starts or advances a match.
- Ordinary optional Permadeath and the strict native export: regulated knockout must remain nonlethal; actual deliberate lethal misconduct must not be falsely described as a harmless routine.
- Multiplayer: different players attempt registration, spectator falls, nonentrant acts, participant renames or disconnects, rewards and discovery items belong to different players. Explicitly document any unsupported case.
- Portal combinations: trophy only, silver key only, both, wrong area, same-turn transit, next-turn revelation, actual crossing, return home, discovery already done, stolen/manufactured catalogue item identity. Spider Realm fingerprints remain identical.
- Dungeon: retreat, branching route, prior clear state, generated npcTypes register before attacks, combat/credible release endings, boss reward exactly once.
- Crime quests: actual success/failure/refusal, legal alternative, offered payment owner, no automatic wanted-poster expansion and no reward for merely promising a crime.
- Creation and catalogue: no accidental free additions to every start; complete requirement amounts, tier prices, valid native references, no public Time affinity/spells.

### Acceptance standard

A fresh ordinary character can voluntarily enter, understand the field, complete or leave an edition, receive the correct outcome and return later without a stale final. Named people remain recognizable after losing. The new dungeon opens through the requested carried objects, offers an actual independent adventure and returns to the Evertree hub. The remaining bundles improve choice without weakening those guarantees.

No claim of “flawless” implementation follows from this plan. The specific unresolved risks are native-Permadeath nonlethal behavior, same-turn defeat ordering, precise resource filling and individual targeting in multiplayer. Resolve them in the prototype or state the supported release scope honestly.
