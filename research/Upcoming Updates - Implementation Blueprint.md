<!-- PAGE: Cover -->
# THE SCHOOLS OF MAGIC, ARISE!
## Seven updates: implementation blueprint
Mechanical design, quest architecture, NPC requirements and release tests

**Planning edition 1.0 | 30 October 2026 | Baseline: Alpha28**

This is a build guide, not an implemented expansion. It incorporates the creator's release description and answers supplied during planning. New names, quantities, balance values and plot details are proposals unless explicitly marked confirmed. The active world JSON remains unchanged.

**The promise:** independent lives and optional authored adventures. Enter the Crucible because you want to fight. Visit the Oni countryside without enrolling. Investigate Vladimir Kujo without making him the mandatory final boss. Summon the chained dragon deliberately, then face a relentless consequence.

**Current foundation**
205 NPCs / 173 locations / 710 areas / 116 quests / 299 triggers / 480 abilities / 45 skills / 5 realms.

**Seven deliveries**
Prison Life; Adventurers of Glowhaven; The Champions of the Crucible; Portal to Oni City; The Wizard of Shadowspire; The Eternal Chained Dragon; Citadel of Dreams.

**Design position**
Native quests carry undertakings and endings. Triggers record exact changes and independent events. Major opposition uses persistent named actors. Implementation language stays out of dialogue, item descriptions and public lore.

<!-- PAGE: Decisions -->
# 01 / Confirmed decisions and notation
**Creator decisions**
- Prison: playable key days, optional skips over uneventful time.
- Oni country: traditional Japanese-inspired countryside, several towns, wilderness, yokai, samurai and a Shogun. A Soul-magic torii opens to spirit wilderness when brought a quest reward.
- Crucible: optional extracurricular fighting. The player goes to it; no intrusive invitations or spectator-job progression.
- Shadowspire: Vladimir Kujo, human and immortal, extraordinarily powerful, indignant, pouty and immature. His capability may exceed Ilyra Stillglass.
- Chained dragon: distinct from Rovakthuun; driven mad by mage captors. Deliberate summoning exchanges an item for a pursuit item. It relentlessly follows the carrier across realms, including cities, flying directly above where possible. Possession controls pursuit. Disposal is subtly foreshadowed rather than advertised. Death removes the pursuit item. The hunt is not a quest.
- Dreams: an inverted cavern-ceiling city of devils, succubi, arachnes, lamias and others. Residents distrust outsiders but are not uniformly hostile. A villain causes real-feeling nightmares; defeating it ends the curse permanently and grants a remembrance trophy.
- Shadowspire, dragon and Dreams remain independently playable, with optional connections.

**Notation**
SCHEMA FRAGMENT uses documented structures, still needing real entity keys and Studio validation. PLAN CODE is pseudocode: uppercase helpers and arrows are design shorthand, not extra Voyage APIs. State tables are local build documentation, not new exported JSON sections.

**Provisional choices**
Eight entrants; cast counts; map sizes; level bands; reward amounts; the Somnarch working villain title; Dream Magic under Intuition. These are adjustable proposals, not established canon. Prefixes pl_, ag_, cc_, oc_, ss_, cd_ and dc_ separate new state namespaces.

<!-- PAGE: Contents -->
# 02 / Route through this guide
**Foundation**
03 - Mechanical contract
04 - Native quest pattern
05 - Trigger pattern and state hygiene
06 - Timing, budgets and multiplayer

**Update plans**
07-10 - Prison Life: playable sentence, ledger, transitions and cast
11-13 - Adventurers: people, contracts, promotion and repeatability
14-16 - Crucible: format, bracket, results and prize ownership
17-20 - Oni country: map, portal network, torii and spirit wilderness
21-23 - Shadowspire: Vladimir Kujo, access, quests and consequences
24-27 - Chained dragon: acquisition, activation, pursuit and ending
28-30 - Dreams: city, new discipline, permanent cure and trophy

**Handoff**
31 - Build order and budgets
32 - Validation and executable fixtures
33 - Implementation handoff and save compatibility
34 - Sources and evidence

**How to use the plan**
Choose one update. Resolve its open decisions, register real keys, implement a narrow playable slice, validate it, then play it with an ordinary character. Do not paste PLAN CODE into Studio. Do not implement all seven in one untested export.

Every update should produce one current full export, a changed-entity list, a state-writer manifest, executable fixture results, patch notes, a live checklist and a rollback reference. Preserve player-facing prose separately from technical design notes.

<!-- PAGE: Mechanical contract -->
# 03 / The mechanical contract
**Three layers**
Native quests hold ordinary work. A simple undertaking gets a typed story completionCondition and onCompleteEffects. Multi-stage work keeps explicit stages only where evidence, permissions or intermediate decisions matter. A conversation or walk to a desk rarely needs a new flag.

World triggers handle exact transitions: item exchanges, portal travel, custody changes, bracket results, awakening, boss defeat and permanent outcomes. Effects are exact once conditions pass; story/action recognition is still AI judgment. Calling a trigger deterministic does not make its semantic recognition infallible.

AI instructions handle dialogue, tactical interpretation, ordinary generated equipment, scene texture and flexible approaches. A story effect requesting enemies is not a native spawn command. Until the enemy exists as an actual actor, no real attack, damage or defeat may be attributed to it.

**Supported building blocks [S2-S8]**
quest-init / quest-accept / quest-progress / quest-complete; typed completionCondition; item-add / item-remove / player-item; NPC health, scene and combat checks; npc-placement; party-location and party-area; storage; music-track-set / music-track-clear.

**Do not invent**
spawnNpc(), arbitrary playerId targets, direct enumeration of all inventory instances, custom onUseEffects, a universal locked-area flag, a separate aggro meter or a custom combat-phase API. PLAN helpers must be translated to supported clauses/scripts or explicitly left narrative.

Ordinary homes can be areas inside existing residential locations. New capitals and spirit realms are authored before entry. Keep runtime region generation disabled. Hidden markers and paths alone are not certified protection from every map-click travel action.

<!-- PAGE: Quest pattern -->
# 04 / Native quest pattern
Use for returning an object, completing fieldwork, meeting a witness or demonstrating a practical result. Give each ending one owner.

SCHEMA FRAGMENT - illustrative future quest:
```json
{
  "name": "A Blade Returned Safely",
  "questSource": "Komugi Hanabishi",
  "questLocation": "Four Sages Bazaar",
  "detailType": "detailed",
  "status": "hidden",
  "questStatement": "A client needs a repaired blade delivered.",
  "mainObjective": "Deliver the blade to its agreed recipient.",
  "questDesignBrief": "Use a real client and real delivery.",
  "completionCondition": {
    "type": "story",
    "query": "Actual recipient verified this delivery; a promise is false."
  },
  "onCompleteEffects": [
    {"type":"item-add","item":"Mark","quantity":40,
     "target":"allPlayers"}
  ],
  "conclusive": true
}
```
The sample payment is suitable only if 40 Marks per actual participant was agreed. A shared 40-Mark fee needs a verified recipient instead of allPlayers. Register the real blade item and recipient before exporting this example.

A local hook offers the undertaking with quest-init after actual contact. Offering is not acceptance. The player accepts explicitly or through supported UI. A chapter's onCompleteEffects can offer its successor without a second monitoring trigger. Do not auto-accept unrelated follow-up work.

Native completion is semantic detection, not a guarantee. Test plans, hypothetical results, wrong items, false reports and genuine failed attempts that nevertheless satisfy an agreed exercise.

<!-- PAGE: Trigger pattern -->
# 05 / Exact events and state hygiene
A trigger should represent one meaningful transition. Example: carrying an earned item to a torii opens a route, without requiring another quest.

SCHEMA FRAGMENT - unresolved PROPOSED names are not import-ready:
```json
{
  "name":"oc_torii_awaken",
  "recurring":false,
  "conditions":[
    {"type":"party-location","operator":"equals",
     "value":"PROPOSED Torii Location"},
    {"type":"player-item","item":"PROPOSED Soul Bell",
     "operator":"greaterThan","value":0},
    {"type":"game-tick","operator":"greaterThan","value":0}
  ],
  "effects":[
    {"type":"write-boolean","key":"oc_torii_open",
     "operator":"set","value":true},
    {"type":"story","instruction":"The gate opens with a low note. Stop before crossing."}
  ]
}
```
Register the destination, item and return route before export. Opening is not crossing. A separate committed travel action applies party-location and an explicit destination area.

**State rules**
Every key has a writer, reader, reset rule and scope. Unset boolean is false; unset number is zero. Initializers must not reset existing saves. Computed script keys count as writers and need executable fixtures.

One owner grants each reward. A trophy trigger and quest reward must not both pay. Repeating work needs a fresh instance and fresh proof. A once-only event is not a daily schedule. Outer trigger key equals name; use exact operators such as greaterThanOrEqual.

Tick-zero story effects do not deliver an ordinary initial scene. Use storyStart for authored opening prose; stage later events at tick 1 or beyond.

<!-- PAGE: Timing -->
# 06 / Timing, budgets and multiplayer
Alpha28 has 299 world triggers; 262 use story/action conditions. Current community limits describe 500 semantic triggers, five conditions and ten effects per trigger, plus a shared 500 ms script budget per phase [S2]. Recheck current Studio rather than filling the allowance.

Action recognition can affect the same turn's narration. Story recognition runs after narration, so a resulting scene instruction can arrive next turn. Purely mechanical planning rules can react to results already known before narration. Do not put semantic story/action conditions under explicit planning phase.

Gate semantic checks by actual location, quest state and event flags. Seven broad worldwide queries every turn are unnecessary. Scripts have no network/filesystem access. Include native auto-generated quest checks when assessing runtime work.

**Party and individual state**
Native quest progress and geography are shared. A party-location effect moves the party. Personal licenses, payment and custody are not automatically group qualifications. Player scope and satisfyingPlayers help, but cross-condition actor matching needs live tests. Do not invent named-player targets.

Initial target: solo or a coherent traveling party. Mixed custody, split travel and separately enrolled cohorts remain unverified until tested. A name-keyed storage ledger is an application convention, not a guaranteed immutable player identity; renames need migration.

**Music ownership**
Use one shared owner marker for the active boss, bout or scene. A gag cannot clear a boss's override. Boss combat takes priority; actual fight end, withdrawal or interruption releases its own music. No precisely timed two-second stinger is promised.

**Why not just more triggers?**
Exact world changes deserve them. Ordinary dialogue and finite undertakings usually do not. Keep logic small enough to reproduce failures and distinguish a missed semantic check from a missing state producer.

<!-- PAGE: Prison loop -->
# 07 / Prison Life: a playable sentence
**Confirmed:** key prison days with optional skips. Long sentences do not require hundreds of compulsory turns. Imprisonment is a consequence, not the main campaign. Workers and visitors keep their actual legal roles.

Actual arrest/surrender -> recorded intake -> understand the case -> work, relationships, review or escape preparation -> meaningful day -> serve or contest the sentence -> discharge or actual escape. A skip requires player agreement and stops at relevant decisions.

Reuse Wraith Island as the Glowhaven exterior and Wraith Island Prison as its physical-campus realm. Existing facilities cover intake, holding/high security, records, work, medical care, visits, meals, exercise, security, watchtowers, sea wall and landing. Add useful areas before duplicate buildings.

**Three proposed arcs**
The Wrong Number: conflicting transport dates affect one review; investigation and advocacy work without proving all officials secretly evil.
A Quiet Shift: a dangerous repair during work tests competence and trust. Work reduces a term only when the actual order permits credit.
The Long Way to the Shore: reconnaissance, tools and execution create an escape route. Knowing it is not escaping it.

Expand A Shift Behind the Sea Wall and A Date in the Ledger before adding synonymous quests. Akira Oritsu remains the existing custody officer. Tomoe Hoshizaki and Ryōichi Naruse retain their court roles.

**Vertical slice**
Intake, one meaningful work incident and a review on a playable key day. A normal character can ask questions, refuse optional work, investigate or deliberately plan an escape. Avoid repeating meals and signatures as mandatory objectives.

<!-- PAGE: Prison ledger -->
# 08 / Prison Life: dates and property
Bridge gh_in_custody, gh_prison_role and gh_prison_wanted rather than inventing a second custody authority.

**Proposed pl_ case ledger**
Case identity; detained/sentenced/reviewed/released; intake day; review day; fixed release day if applicable; permission to credit work; credited days; last credited day; named property holder; receipt; final legal outcome. A pending trial date is not a sentence deadline. Escape changes physical custody, not the verdict.

PLAN CODE:
```text
IF fixed lawful sentence AND new day > last credited day:
    credit eligible elapsed days once
    last credited day := current day
IF player accepts an uneventful-time skip:
    stop at earliest review/release/known major incident
    advance native day/time once; narrate transition
IF term satisfied:
    offer discharge processing, not instant teleportation
```
Ten conversations are not ten served days. Repeated rests on the same date cannot farm work credit. A skip cannot bypass a known medical emergency, required hearing or active escape attempt.

**Inventory limitation**
The documented reader counts item types; it does not expose a general inventory-instance snapshot API for every generated item's properties. Do not delete everything and return generic replacements. MVP preserves the real objects, records sealed custody and blocks use through Action Info. This restriction is AI-mediated, not a guaranteed native inventory lock.

A fully mechanical seizure/return system waits for a verified instance interface or tested Studio procedure. Known type-specific removals need exact quantities, one return owner and duplicate-return tests. Returning a receipt is not restoring property. A knockout in prison preserves custody and unavailable equipment.

<!-- PAGE: Prison transitions -->
# 09 / Prison Life: transitions and quests
**Refine existing rules**
gh_custody_intake records completed lawful intake of the sole player or coherent whole party. Initialize a new case once; never detain workers/visitors accidentally.
gh_prison_authorized_work must not overwrite a prisoner into a free employee as a shortcut.
gh_prison_discharge verifies release and property disposition, then moves to Wraith Island - Skullshore Landing.
gh_prison_escape records actual escape to shore and preserves wanted status.

**Proposed additions**
pl_review_offer: Records Office + active case + due review + actual request -> offer hearing work.
pl_skip_agreed: safe custody + accepted explicit skip -> bounded time advance. Script handles arithmetic; actual agreement remains a semantic condition.
pl_term_ready: fixed sentence + served threshold -> one notice; no automatic forgiveness of unrelated crimes.
pl_work_credit: verified shift + reduction permitted + new shift identity -> one credit.

A hearing quest ends on its actual ruling, which may be denial. It does not guarantee innocence. An exact revised release date follows only a specific ruling. A work quest ends on the checked safe repair. An escape quest ends when escape is actually resolved, not when a route is discovered. Do not require all side stories to leave.

**Tests**
Visitor mistaken for prisoner; failed appeal; prison knockout; lawful completed term; repeated discharge; same-day work repeat; refused skip; sentence extension by an actual order; escape without property retrieval. Reload preserves case dates and actual belongings. Mixed-party incarceration must not teleport free companions into cells.

**Build budget**
Aim for 4-7 new/changed rules and 3-5 undertakings, reusing existing mechanisms. Do not script every meal. The law should provide understandable consequences without making a missed semantic check a permanent progression lock.

<!-- PAGE: Prison cast -->
# 10 / Prison Life: a cast with leverage
**Proposed: 9 new people plus Akira Oritsu**
Warden: severe about escape, protective of staff, willing to defend lawful review. Major, capable and not omniscient.
Infirmary practitioner: blunt and tired, refuses to turn treatment into interrogation. Supporting or major.
Records clerk: scrupulous about dates, timid about correcting a superior.
Senior guard: treats rules as personal status; challengeable through evidence, not an automatic secret villain.
Workshop supervisor: prisoner or staff with actual delegated access; values competence.
Three inmates: unrepentant fraud; angry minor offender; someone whose apparent innocence is complicated.
Visitor/advocate contact: preserves an outside connection without becoming everyone's follower.

These are design briefs, not final cards. Later authors use the existing NPC format, adult ages, full names, explicit hair/eyes, usual equipment, concealment/knowledge and real combat methods. Affinity does not dictate occupation. Support staff need not become bosses.

**Situations**
Who gets a safe work assignment? Is an inmate's shortcut worth reporting? Can justified safety concerns coexist with abusive conduct? Does helping someone cost access elsewhere? A relationship consequence or work restriction is often enough; do not silently add years to a term.

**Acceptance definition**
An ordinary imprisoned character understands the case, plays a meaningful day, skips uneventful lawful time, addresses the same belongings and leaves under a real order. Actual escape preserves the warrant and property history. Inventory enforcement limitations remain explicit in developer notes.

**Optional role entry**
A worker can accept a legitimate prison assignment and witness these stories without being arrested. Keep that employment route separate from the custody case ledger. Existing court figures may hear an appeal without relocating permanently to prison.

<!-- PAGE: Guild cast -->
# 11 / Adventurers: recurring professionals
Keep the international guild, court-permitted branch, Bronze/Silver/Gold/Platinum badges and licensure. Promotion needs a genuine assessment; portal permission remains a separate court decision. Posted payment is received in full, with no extra player-side commission deduction.

**Proposed 6 adventurers + 2 staff**
A Silver spear fighter: encouraging toward rookies, reckless about her own recovery.
A Gold magitech explorer: meticulous with tools, disastrous at negotiating.
A weathered Bronze courier: satisfied with a useful career rather than desperate for rank.
A charismatic recovery specialist: salvage claims repeatedly create disputes.
A healer: charges fairly and refuses permanent recruitment.
A brilliant solo hunter: poor cooperation keeps costing contracts.
Add a board steward and promotion assessor; Komugi Hanabishi remains the established clerk.

Reuse Natsume Hibari for mountain expertise and Yuzuri Takase for occasional Asterveil work. Actual willingness and availability matter. A badge does not oblige either to accompany the player.

**First package**
8 people, 8-10 contracts and a three-chapter recovery story. Bronze work includes rescue, delivery and local pests; Silver adds hazardous salvage; Gold includes a difficult mountain recovery; Platinum adds a bounded high-risk expedition with a consequence that survives return.

Rank is not a level. A veteran newcomer can pass assessment; a strong character cannot simply invent a badge. A licensed specialist can contribute without becoming a front-line fighter. New people need outside relationships, opinions and reasons to decline work.

**Creative position**
Some adventurers should dislike each other. A frictionless recruitment shop would flatten the update. Competence, rivalry, money and affection can produce different loyalties without every disagreement hiding a villain.

<!-- PAGE: Guild contracts -->
# 12 / Adventurers: one board, fresh work
Extend gh_guild_board rather than building a competing offer system. Add catalogue entries to its existing jobs list. Computed q20_offered_* writes are real producers; test them instead of adding redundant literal writers.

**Build-time contract ledger**
Quest key; required rank; client; destination; return contact; quoted net payment; repeatable status; fresh-instance proof; completion owner. These are planning fields translated into supported structures, not extra exported quest fields.

Use native completionCondition for finite delivery, repair, rescue or hunt. A named target and actual evidence can justify explicit stages in a consequential multi-chapter hunt. Test hypothetical claims, stale trophies and returning to the wrong contact.

**Promotion**
Preserve current 5/10/20 service-credit thresholds and genuine accepted assessments unless later changed. Author memorable reviews for Silver, Gold and Platinum; actual approval feeds the existing badge exchange. A failed assessment can conclude its attempt without granting rank. Do not leave two badge writers active.

**Repeatability**
Allocate a new serial only after cooldown and actual fresh acceptance. Old proof cannot complete the next run. Mark that serial paid once. Prior missing people do not resurrect for a repeatable rescue. A new request needs a new credible incident.

PLAN CODE:
```text
ON actual fresh acceptance:
    instance := previous instance + 1
    accepted tick := current tick
ON actual completion of this instance:
    IF paid instance != instance:
        deliver agreed payment once
        award actual participant credit once
        paid instance := instance
```
Equipment rewards use the existing bounded generator. Fixed money and generated property have one settlement owner. Mere proximity to the return counter is not participation. Portal return alone is not a delivered report.

<!-- PAGE: Guild promotion -->
# 13 / Adventurers: exact exchange, clear tests
SCHEMA EFFECT FRAGMENT - already-supported badge exchange:
```json
[
 {"type":"item-remove","item":"Guild Badge: Bronze",
  "quantity":1,"target":"satisfyingPlayers"},
 {"type":"item-remove","item":"Guild Service Credit",
  "quantity":5,"target":"satisfyingPlayers"},
 {"type":"item-add","item":"Guild Badge: Silver",
  "quantity":1,"target":"satisfyingPlayers"}
]
```
Apply behind qualified-player checks and a real passed assessment. Enough credits, flattering the clerk or discussing a future exam do not qualify. This exchange is the promotion itself, not permission for a second AI inventory grant.

**Test cases**
Unlicensed player sees licensure work. Bronze and Gold players do not automatically license each other. Lost badge leads to legitimate reissue without duplicate rank. Simultaneous settlements do not duplicate money. Declined jobs do not reappear every visit. Old proof does not become new work. A promotion gives no portal key. Partial failure receives only the actually agreed compensation.

**Questline proposal: Separate Claims**
A recovery commission is contested by another team; the evidence reveals a genuine ownership dispute rather than a secret world-ending relic. The player can negotiate shared recovery, establish a claim, expose misconduct or leave. Later chapter geography is already mapped. Each outcome changes specific professional relationships; no universal guild hostility for disagreeing with one adventurer.

**Definition of done**
One Bronze contract, one fresh repeat, one multi-stage recovery and one assessment play through with ordinary characters. Check accepted/rejected/abandoned states, exact reward, eligible recipients and a return visit. At least one cast member offers interesting company without a quest being accepted.

<!-- PAGE: Crucible format -->
# 14 / Crucible: optional fighting
**Confirmed:** players actively go to the Crucible to fight. It is extracurricular, open to adult students, adventurers and other eligible entrants. No mandatory academy milestone, intrusive invitation or spectator-job progression.

**Proposed first format**
Eight entrants; three player bouts: quarterfinal, semifinal and final. A normal loss ends the title run. Optional exhibition fights may remain, without pretending the loser won the tournament. Entrant count is provisional.

Start with a novice/intermediate division using fixed authored opponents and an announced risk band. A later open division features formidable professionals. Never shrink a famous level-70 character to level 20 to fit the player. Stronger players seek a suitable division; weaker entrants can knowingly attempt an upset.

**People**
Tomoe Enokida remains coordinator. Kōhei Sanada or Ritsu Kurogane can officiate only where duties allow. Propose four recurring fighters, a referee and a medic. Existing students fill suitable slots while retaining personalities and levels. A celebrated champion can be a future opponent rather than the unavoidable novice final.

**Announce before entry**
Stop conditions; surrender; boundary rules; incapacity; nonlethal intent; banned mana potions and external reserves; legal catalysts; recovery intervals; entry fee and exact purse. Failed casting is not cheating. No surprise rule after the player pays.

**My recommendation**
Fewer memorable opponents are worth more than anonymous waves. Give each fighter a recognizable plan, counterplay and a reason they care. The route should deliver combat quickly after registration without making every bout a form-filling exercise.

<!-- PAGE: Crucible state -->
# 15 / Crucible: bracket and result authority
**Proposed cc_ state**
Edition; division; entrant names; results; round index; opponent; active bout; bout serial; resolved serial; entry paid; prize paid; player eliminated. This is one actual competition, not a simulation of the entire sporting calendar.

Register on explicit request at Competitor Passage under announced terms. Combat starts when the referee actually begins a valid bout. Entering Arena Floor is not combat consent. Move opponents for the bout, then let them recover or leave coherently.

PLAN CODE:
```text
IF valid accepted registration AND not entered this edition:
    record entry; charge agreed fee once
    seed fixed entrants and first opponent
IF referee starts bout:
    active := true; bout serial += 1
IF actual opponent incapacity OR verified concession:
    IF active AND resolved serial != bout serial:
        record one result; active := false
        resolved serial := bout serial
        offer next round or settle championship prize
```
Mirror loss, withdrawal and legitimate disqualification. npc-in-combat false alone is not victory: it may mean flight. Health thresholds can detect incapacity; concessions, ring-outs and cheating require narrow semantic checks tied to this opponent and bout.

Stopping a fight does not resurrect someone or erase injury. Announced treatment uses supported effects for actual participants. Do not set an opponent to zero Health merely to narrate a dramatic player victory. Ordinary actions use the existing combat engine, not a parallel dice system.

Use either one tournament undertaking with stored results or several useful bout quests. Avoid a native final completion and a competing prize trigger. Reuse existing tournament-active state rather than adding another inconsistent match authority.

<!-- PAGE: Crucible ending -->
# 16 / Crucible: editions and consequences
A finite announced purse, a naturally described medal and earned recognition make a good initial prize. An optional generated commission can add character. Store edition results; an old medal does not authorize another payout.

A narrow loss, sensible surrender, cheating violation and genuine victory should produce different reactions. Preserve performance rather than forcing every loss into humiliation. Do not pay everyone who stood near the finalist. This release does not create a spectator questline.

**Later editions**
After the prior edition concludes and a sensible preparation gap, the player can request another announced competition. Allocate a new serial and eligible field. Old results stay historical. Abandonment becomes withdrawal rather than freezing the city indefinitely. Do not create an automatic daily tournament.

**Rule outline**
cc_register; cc_start_bout; cc_opponent_down; cc_player_down; cc_concession_or_ringout; cc_award_prize. Consolidate real bracket arithmetic in a small script only where useful. A resolved serial blocks duplicate processing. Keep actual opponent identities in the ledger.

**Tests**
Surrender before lethal damage; simultaneous incapacitation; leaving mid-bout; interrupted combat; opponent death; banned reserve; disputed ruling; reload before prize; re-entry after loss; party member speaking while another fights. No duplicate purse or automatic opponent recruitment.

**Audio**
Use a regular fight theme and an optional final theme. A referee's stop, interruption, defeat or withdrawal clears the bout's owned override. Do not clear an unrelated active boss theme.

**Definition of done**
A player wins an edition, loses another and withdraws from another, receiving exactly the correct results each time. The competition stays optional and does not block morning classes, guild work or ordinary city life.

<!-- PAGE: Oni countryside -->
# 17 / Oni country: an authored countryside
**Confirmed:** Japanese-inspired countryside under a Shogun, divided towns, wilderness, samurai, yokai and strange magic. The title Portal to Oni City does not require one oversized capital.

**Proposed first map**
One realm, two adjacent countryside regions, 12-16 locations, roughly 45-60 areas. Four inhabited clusters host services; roads, forests, river country, ruins and the torii take the rest. Shops and side streets become areas unless genuinely separate destinations.

Arrival town and staffed portal room; Shogun's castle town; agricultural market town; riverside craft/onsen town; shrine hill; road station; cedar forest; bamboo ravine; terraced farms; abandoned watchpost; mountain pass; yokai boundary grove; Soul Torii. Final names and coordinates wait for the lore/map pass.

**Proposed civic conflict**
Retainers and town officials dispute protection of old roads: who pays, who receives guards and whose testimony counts. Samurai, farmers, shrine keepers and merchants have credible competing interests. Yokai can be neighbors or threats; not every unusual being is a hostile monster.

**Cast target**
14-18 adults: Shogun, retainer, magistrate, shrine keeper, two samurai with conflicting loyalties, portal attendant, innkeeper, craftsperson, farmer, courier and several memorable yokai. Repeatable hostile fauna use npcTypes. Fame can justify initialKnown; reputation does not create friendship.

**Balance proposal**
Accessible towns and maintained roads; wild dangers around levels 25-50; deeper spirit wilderness is a separate slice. A farmer's level is not scaled to the visiting player. Ordinary livelihood, food, repair and travel coexist with exorcism stories.

<!-- PAGE: Oni network -->
# 18 / Oni country: Evertree network integration
Author the realm, regions, locations and areas before opening the route. Court permission remains separate from badge rank. The new route key can be granted for real trade, study, duty or expedition. Oni ancestry alone is not a key or foreign authority.

Destination arrival is another portal room with its own architecture. Return always goes to Evertree Base - Portal Room. Preserve the existing once-only level-20 anomaly intercept if it has not happened; the new route must not accidentally bypass it.

PLAN CODE:
```text
ON actual committed Oni-route crossing at Evertree:
    require real key and legitimate access
    IF already transported this turn: stop
    IF existing anomaly condition qualifies:
        use existing anomalous destination and grant
    ELSE:
        reveal intended route destinations
        move party to authored arrival portal area
        move actual companions with party
ON destination return:
    move to Evertree Base - Portal Room
```
Integrate this into the existing action recognizer, command router and state fallback rather than creating a competing teleport that can fire later in the same turn. A view through an arch is not arrival. Crossing must update structured position, not just the prose.

The Soul Torii is a different mechanism: a local earned item awakens an authored spirit route. Soul affinity is not required to carry the reward. This does not open every torii in every generated story or authorize new nations beyond the map.

**Tests**
Key without commitment; commitment without key; crossing before/after anomaly; return with companions; asking about the arch; two destination requests; denied access; lost route key. Keep permissions and ordinary body-casting capabilities distinct.

<!-- PAGE: Soul Torii -->
# 19 / Oni country: the earned item and torii
**Proposed chain: The Bell That Answers No Shrine**
1. A roadside memorial rings without wind. Investigate a specific disturbed site through observation, testimony, repair or learned magic. No mandatory Soul caster.
2. Restore a broken agreement between a town and a spirit, or establish why it failed. A samurai's orders and a farmer's account conflict. Choosing a side is not automatically solving it.
3. Resolve the disturbance and receive Soul Bell, a working item name. Its description hints at the old torii without containing trigger instructions.

Each ordinary chapter has a native completionCondition. The final chapter grants the real item once through onCompleteEffects. At the torii, player-item greaterThan 0 fires awakening. No redundant completion flag is needed merely to prove a genuinely granted item exists. Do not casually generate identical rewards in shops.

Awakening writes oc_torii_open, reveals a foothold and delivers a scene. Stop before movement. A later committed crossing enters the authored spirit destination. Recommended proposal: the gate stays open after the bell is lost; the item caused an event rather than acting as a permanent subscription. Confirm that persistence decision before build.

**Proposed public item text**
A small bronze bell recovered from the abandoned roadside shrine. Its note carries no echo, but a faint answering hum rises near the old soul-marked torii.

**Spirit wilderness slice**
One region, 6-8 locations: entry glade, lantern marsh, root bridge, silent shrine, pale river, old battlefield and remote clearing. No full spirit city yet. Provide a reliable return threshold. Custom npcTypes distinguish bodies, speech, hostility and warning signs; a yokai category alone is not a combat disposition.

Retreat, permitted collection, negotiation and fighting can produce different legitimate results. Do not let an investigative spirit encounter require killing every creature just because it is in a dangerous realm.

<!-- PAGE: Oni ledger -->
# 20 / Oni country: ledger and acceptance tests
**Producer / reader / lifecycle**
Court route key: verified court authorization produces it; ordinary network crossing reads possession. Travel does not consume it.
Soul Bell: final local quest produces it; torii awakening reads possession. Loss before awakening needs real recovery or a deliberately authored replacement path.
oc_torii_open: awakening writes it; crossing/discovery read it. Do not reset on departure.
Spirit return: fixed geography and actual committed movement; no invented new nation.

**People to flesh out**
The Shogun has an agenda beyond the portal mystery. A samurai can be superb at discipline and poor at admitting affection. A shrine keeper may know ritual practice without knowing the hidden cause the player assumes. An abrasive yokai neighbor can still be a helpful local. Oni horns do not imply violence or allegiance.

**Tests**
Unrelated bell; claimed reward not in inventory; real reward lost; carrying it elsewhere; a nonmage approaching; witnessing the opening but declining entry; returning later; one party member carrying without duplicate grants to everyone; retreat from first spirit opposition; direct map-click into an unearned destination.

Critical travel barriers need actual handling and live tests. Paths and hidden markers alone are not a universal click lock. A successful opening is also not a teleport. Inspect native geography after every outbound and return test.

**Build boundary**
Ship the countryside and one reward-to-gate loop first. Expand spirit wilderness after that works. No forced Shogun succession crisis, immediate national war or random realm generation. Optional connections to other updates can be discoveries, never mandatory prerequisites.

**Public-text rule**
The shrine keeper speaks of the bell and souls, not completion flags. The item describes what the player holds. Trigger names, true/false states and authoring instructions belong only in technical fields and development documents.

<!-- PAGE: Vladimir -->
# 21 / Shadowspire: Vladimir Kujo
**Confirmed:** human, immortal, potentially more capable than Ilyra Stillglass, indignant, pouty and immature. Preserve Vladimir Kujo's name and the creator's old-campaign identity. His immortality's origin and exact limits remain undecided.

**Proposed dramatic tension**
His exclusion system is excellent at keeping out people he does not want to deal with. It is less helpful when his pride prevents admitting he needs assistance. An unresolved mundane commission exposes a genuinely dangerous containment fault. Cooperation, not raw technical ability, becomes the problem.

This is a proposed story, not a replacement biography. Do not silently equate immortality with universal invulnerability, Time affinity or revival from every injury. Ask before defining his old-campaign history, relatives or metaphysical origin.

**Use existing geography**
Shadowspire already contains forest, twisting trail and outer clearing. Add threshold, reception, study, work gallery and apparatus as areas inside the location. Update the old absolute statement that entry is impossible while retaining an initially inaccessible approach. No second secret realm is required for one tower.

**Power**
Stay within level cap 100; use supported NPC success, damage and health modifiers for exceptional capability. Do not create level 120 or raise every court guard to compete. Define a bounded learned repertoire later. An optional duel may be extremely dangerous; the first visit must not require beating him.

**Cast**
Vladimir Kujo as major; two supporting contacts or individually important constructs. Ordinary animated defenses use npcTypes. Immense power does not make him an effective head of government or give him authority over the court.

**Tone**
Let him sulk, complain and demand an absurd courtesy. Do not polish away his immaturity or turn every line into a punchline. He can be formidable and socially exasperating at once.

<!-- PAGE: Shadowspire access -->
# 22 / Shadowspire: path, threshold and quests
**Proposed chain**
SS1 - A Complaint Nobody Can Deliver: an existing craftsperson has a returned parcel or disputed commission. This gives a reason to approach without publicly revealing the owner's name.
SS2 - The Path That Refuses Directions: follow repeatable physical clues through the forest and solve an actual exclusion condition. One good roll does not invent an interior.
SS3 - A Perfectly Minor Catastrophe: meet Vladimir Kujo and address a bounded apparatus fault. Different learned, physical and social methods can work.
SS4 - The Favor He Definitely Did Not Need: optional later personal story; not paperwork required to receive the first reward.

**State**
ss_approach_understood is written by the solved-path event. ss_threshold_open follows admission or a genuinely resolved breach. Ordinary chapter completion offers successors. A small access handler prevents direct inner-room travel from bypassing the sealed threshold.

PLAN CODE:
```text
ON valid entry commitment:
    IF admitted OR actual barrier overcome:
        move to authored threshold/interior
    ELSE:
        preserve current reachable position
        resolve approach or explain actual obstruction
ON departure:
    preserve repaired apparatus and actual opinion
    do not reset puzzle for an already welcomed visitor
```
Hidden state is discovery, not a certified lock. Test supported movement paths and command fallbacks together. Do not teleport players back from legitimate scenes merely because a badly written story condition missed admission.

**Rewards and property**
Inspection is not theft. His library does not teach every discipline by ownership. A bounded commission or access to particular teaching is enough. Time remains exceptional; the mere presence of an ancient wizard does not unlock it. Use existing item generation for ordinary equipment, and authored IDs only for consequential pieces.

<!-- PAGE: Shadowspire outcomes -->
# 23 / Shadowspire: outcomes and tests
Respectful problem-solving can earn repeat access. Theft creates a specific debt or broken trust. Exposing a genuine danger can bring civic scrutiny without declaring automatic war. Refusing flattery is not a lethal attack trigger.

Optional remarks may recognize the dragon's restraint work or a dream ward. Vladimir Kujo is not secretly every expansion's mastermind. The other stories neither explain his immortality nor become required keys to his door unless the creator later chooses that connection.

**Build tasks**
Full NPC card in the existing format; 3-5 combat-relevant capabilities and limits; 5-7 interior areas; revised outer descriptions; 3-4 quests; approach/threshold handling only where needed. Identify all existing instructions reserving ownership and update them at the correct scope when the secret becomes authored canon.

**Tests**
Ask who owns the tower before discovery. Arrive without a quest. Solve the approach by a credible alternative. Attempt direct map travel. Receive admission then revisit. Refuse repairs. Threaten him. Steal a grimoire. Ask for Time Magic. Finish the apparatus while an unrelated quest remains active.

No ordinary NPC knows private history merely because a journal card exists. A powerful player does not make a difficult magical apparatus harder by existing. Failed methods should change the situation concretely, not require repeating the same roll until success.

**Open decisions**
Immortality limits; actual affinities and breadth; what project he isolates; how much old-campaign lore transfers; which behavior earns or loses access. These are flagged for the creator rather than silently settled in a public character description.

**Definition of done**
One approach, one admission, one substantive encounter and one resolved problem work without combat, alongside a credible optional conflict route and a persistent return visit.

<!-- PAGE: Dragon concept -->
# 24 / Chained dragon: an event hunt
**Confirmed:** a different ancient dragon from Rovakthuun. Mage captivity drove it mad. A questline earns a summoning item; deliberate use exchanges it for a pursuit item. Carrying that item enables relentless pursuit across realms and cities, overhead where possible. Death removes the pursuit item. The hunt is not a quest.

**Within that intent, my recommendation**
Make the warning honest. Touching an interesting object is not activating it. The player should know this calls a major boss that can follow them home. Once deliberately committed, ordinary urban safety is not an escape clause. No permadeath does not justify an endless instant-knockout loop.

**Acquisition chain, proposed**
CD1 - The Links That Remember: investigate old mage restraint work.
CD2 - A Debt in Iron: recover a specific binding core on a dangerous expedition.
CD3 - What Was Never Released: learn enough to choose deliberately, then receive the summoning relic. Refusing activation does not leave the acquisition story unfinished.

**Public item language, proposed**
Clasp: A scorched clasp from the ancient binding. Opening it calls what its makers failed to silence; the dragon's pursuit will not respect the safety of a city wall.
Link: A broken chain-link that warms against the skin. Its pulse follows distant wingbeats; when set apart, that pulse briefly weakens.

The second description foreshadows possession subtly without presenting a discard tutorial. Do not lie about an actual disposal result.

**Initial balance proposal**
Level 70 unique boss for prepared mid/high-level groups, tuned against ordinary parties before release. Its draconic name, size, element, health and modifiers need a dedicated boss pass. Do not scale automatically to the player. Bounded capabilities should still make its rage frightening.

<!-- PAGE: Dragon activation -->
# 25 / Chained dragon: activation and ownership
**Working IDs, not final canon**
Items: Chained Summoning Clasp; Pursuit Chain-Link. Actor: CD_DRAGON_NAME, a reserved placeholder requiring a real draconic name. Storage: cd_hunt_started, cd_dragon_resolved, last pressure tick and last arrival.

**Activation conditions**
Actual clasp held; unresolved dragon; explicit deliberate use after a real warning. Exchange one clasp for one pursuit link for the true activator. Reveal/register the one authored dragon and stage arrival. Shared activation guarding prevents two simultaneous summons.

PLAN CODE:
```text
ON deliberate warned use of genuine clasp:
    IF hunt already started OR dragon resolved: no new summon
    remove clasp from actual activator
    give pursuit link to that same activator
    mark started; reveal the single authored dragon
    stage arrival without automatic opening damage
```
This needs verified actor correlation. Never grant the link to allPlayers. If the target engine cannot correlate actor, possession and effects safely in mixed multiplayer, certify solo/coherent-party play first. Do not invent a named-player target field.

**The item remains the switch**
A native player-item count checks possession. Dropping/depositing stops tracking until somebody carries it again. Preserve the dragon's wounds and existence; do not delete or respawn it. Ordinary merchants can refuse the dangerous object, not silently confiscate it. Theft/transfer requires an actual outcome, never an unsolicited insertion into another player's inventory.

**No quest wrapper**
The acquisition chapters and hunt have separate owners. Do not create a Hunt the Dragon quest simply to track the event. A later trophy callback can be optional. Starting the hunt does not require another journal acceptance.

**Lifecycle**
Unstarted -> deliberately activated -> active with carrier / suspended without carrier -> resumed on possession -> permanently resolved on actual dragon death. Only the resolved state forbids future reactivation, including stale links.

<!-- PAGE: Dragon pursuit -->
# 26 / Chained dragon: relentless pursuit
The dragon flies directly above the carrier wherever physically possible. This is a persistent threat, not a distant random encounter. City guards and familiar streets do not make the carried mark inert.

**Placement controller**
A recurring controller reads started/resolved state, the real actor's health and possession. In shared-party geography, carrier and party are together. On realm/location change, move the same actor to the mapped overhead/outdoor approach using npc-placement. Establish any supernatural boundary-crossing capability in its actual card rather than inventing it mid-play.

PLAN CODE:
```text
IF started AND not resolved:
    carriers := player-item counts greater than zero
    IF no carriers: suspend tracking; preserve dragon
    ELSE IF dragon alive:
        IF party moved OR dragon at wrong approach:
            place same actor at mapped pursuit position
        deliver its actual hostile intent
        preserve wounds, restraints and previous actions
```
Indoor spaces alter the angle, not the pursuit rule. A huge dragon should menace the enclosing street, roof, cavern approach or doorway rather than fit into a cupboard. Author an area fallback for each realm. Portal placement is technically supported; the supernatural explanation and attack reach need coherent design.

**Actual combat only**
No extra scripted damage after narrated attacks. Guards and powerful residents may respond at actual strength, including killing it; do not guarantee the player the finishing blow. Buildings can suffer concretely resolved harm without a new city-destruction simulator. The dragon is not given free infinite actions for being angry.

**Knockout**
A player knockout neither kills the dragon nor erases the held link. Pursuit resumes at the real recovery location. Finish the recovery transition and allow a genuine next action before renewed pressure; avoid repeated automatic incapacitation without input.

The discovery of disposal is permitted, but not advertised as the primary goal. Do not add a hidden permanent curse that contradicts possession-based pursuit.

<!-- PAGE: Dragon death -->
# 27 / Chained dragon: death and cleanup
Guard the ending by a real engaged actor and started/unresolved state. Health <= 0 can detect its fall; it must not interpret a missing actor's default or temporary incapacitation as confirmed death. If the build distinguishes death only through narration, use one narrow death verification after mechanical fall. Do not invent a native death flag.

SCHEMA EFFECT FRAGMENT - after confirmed death:
```json
[
 {"type":"write-boolean","key":"cd_dragon_resolved",
  "operator":"set","value":true},
 {"type":"item-remove","item":"PROPOSED Pursuit Chain-Link",
  "quantity":1,"target":"allPlayers"},
 {"type":"music-track-clear"}
]
```
Assumes one link per carrier and that the dragon owns the current music. Removing one does not delete every possible duplicate. Prevent duplicate grants at source or use verified count/recipient handling. Unheld items are not globally enumerable by this effect; resolved state prevents a dropped link restarting the hunt after death.

The cleanup has one owner. A death trophy, if desired, is granted there once under an agreed participation policy. The acquisition quest does not independently grant victory rewards.

**Tests**
Use without warning; hypothetical use; double activation; every realm; cellar, cavern and prison; knockout; dropping, storing, recovering and losing link; theft; another player carrying; dragon killed by a guard; wounded escape; reload; native daily NPC healing; duplicate ending; picking up an old dropped link after death.

**Done when**
One persistent dragon follows the real carrier with coherent positioning, does not duplicate damage or actors, pauses when possession ceases, and never resumes after confirmed death. City entry is not a safe reset. The intended hard fight remains avoidable before deliberate activation and supports the agreed obscure disposal mechanic afterward.

<!-- PAGE: Dreams city -->
# 28 / Citadel of Dreams: the inverted city
**Confirmed:** an inhabited city hanging from a vast cavern ceiling. Devils, succubi, arachnes, lamias and others live there. Residents distrust outsiders but are not uniformly hostile. A villain causes intense, real-feeling nightmares; defeating it ends the citywide curse permanently and grants a trophy recording the outcome.

**Proposed map**
One realm, two regions: upper city and lower cavern approaches. About 10-14 locations and 40-55 areas. Orientation stays stable; do not reverse coordinates every turn. Bridges, lifts and gravity-bound streets allow ordinary nonflying travelers to navigate.

Working sites: portal vestibule; hanging market; residential galleries; civic court; silkworks; clinic/refuge; suspension lifts; lower cisterns; collapsed observatory; nightmare focus; villain stronghold. Shops and individual homes can be areas. No extra realm for each person's dream.

**Society**
Suspicion comes from actual priorities and history, not a rule that every devil lies or every succubus pursues the player. A lamia lift engineer and arachne innkeeper can have ordinary work and disagreements. The city should be worth saving before it becomes a boss objective.

**Cast proposal**
8-12 authored residents; one major antagonist; at most two unique lieutenants. Ordinary nightmare manifestations use npcTypes. Working antagonist title: the Somnarch, an individually authored hostile being, not a regenerating template. Final name and nature remain open.

**Proposed tension**
Residents reorganize their lives around avoiding sleep. Work, trust and caregiving fray before combat begins. The cure should visibly restore ordinary life, not award a trophy over unchanged streets. Ending the curse does not automatically erase trauma, debts or the city's distrust of every outsider.

<!-- PAGE: Dream discipline -->
# 29 / Dream Magic: a bounded new discipline
**Provisional:** Dream Magic under Intuition. The creator intends a new type but has not fixed its name or full scope. Add one deliberate definition rather than several synonymous skills. Do not call it Time Magic.

Proposed scope: sleeping perception, prepared shared imagery, recognizing intrusion and defending sleep. Waking hallucination overlaps Illusion and needs a specific learned working. Domination, remote access and injury are not automatic benefits of owning the skill.

**Implementation**
One configured skill, stable lore entry and targeted generation guidance. Decide later whether initial teaching is city-specific. No invented hidden/locked skill flag. Character-creation affinity and study choices are a separate approval. Personal invention still uses spellcraft.

**Proposed first techniques**
Quiet Sleep: ward a willing sleeper against minor intrusion.
Dream Lantern: make a recognizable light within an entered dream.
Lucid Thread: remember and recognize an established dream intrusion.
Borrowed Scenery: alter a bounded dream image, not real inventory.
Wakeful Anchor: support a willing sleeper's return to awareness.
Shared Reverie: a prepared consensual shared dream scene.
Nightmare Screen: resist a specific hostile projection.
Sever the Dream: break a known active link after real opposition.

Give each actual requirements, Mana cost, cooldown and counterplay using existing schemas. No automatic success, free permanent mind control or removal of the Time restrictions.

**Curse incidents**
The villain's focus projects the curse. Gate selected incidents by actual sleep/rest or established local events, not a damaging query every turn for every resident. Fear narration alone costs no Health. A hostile manifestation must exist as an actor before attacks resolve. Interrupted rest needs concrete circumstances.

No new sanity meter in this release. Existing resources, individual incidents and lasting narrative consequences are sufficient. The city can be strange without a second combat engine.

<!-- PAGE: Dreams cure -->
# 30 / Dreams: defeat, cure and remembrance
**Proposed chain**
DC1 - A City That Dreads Morning: witness a concrete incident and verify a pattern. Outsiders are not instantly trusted.
DC2 - The Shape Behind the Dream: locate the real focus using evidence, negotiation or exploration. No invented unmapped dimension completes the investigation.
DC3 - The Last Nightmare: confront the Somnarch and defenses. Named boss, fixed risk band, distinct opponents; not endless anonymous waves.
DC4 - When the Lamps Go Out: optional short aftermath with residents able to sleep. No extra report required to make the cure count.

**Permanent state**
dc_nightmares_ended is written once by the confirmed outcome owner. All future curse-incident producers require it to be false. Close already queued incidents coherently. A later lost trophy does not restart the curse. Do not resurrect dead victims automatically.

**Proposed trophy**
A fractured crown from the Somnarch, ending their reign and the curse of nightmares in the City of Dreams forever.

Readable keepsake and memory aid, with no embedded AI instructions. The persistent flag is the world-state authority. Choose either quest completion or victory trigger as its one grant owner. If the villain is defeated before the quest is accepted, the cure must still occur; a broad outcome trigger can own cure/trophy and the quest can recognize that state without paying twice.

**Tests**
Early victory; broken focus first; lying about cure; trophy loss; returning days later; an old nightmare incident resolving after cure; generated jobs trying to revive the same curse. Dreams cannot erase real possessions, reverse actual time or declare past consequences imaginary.

**Boss identity**
Use a deep-negative initialRelationship, explicit hostile motives and actual combat behavior. This does not make all city residents hostile. A citizen's species is not allegiance to the villain.

<!-- PAGE: Sequence -->
# 31 / Build order and boundaries
**Recommended release order**
Prison Life finishes the consequence loop. Adventurers deepens the repeatable profession. Crucible delivers bounded authored combat. Oni country establishes geography and the item-to-torii loop. Shadowspire reveals Vladimir Kujo independently. Chained Dragon ships after cross-realm pursuit and recovery tests. Dreams introduces the city, one discipline and permanent cure.

This is an authoring order, not a required player campaign. No prison completion prerequisite for the tournament. No mandatory dragon victory to enter Vladimir Kujo's tower. Optional discoveries can connect stories without swallowing the sandbox.

**First-release allowances, proposed**
Prison: 9 people, 3-5 undertakings, existing map.
Guild: 8 people, 8-10 contracts and 3 recovery chapters.
Crucible: 6 people and one small competition.
Oni: 14-18 people, 3 central chapters, local work and small spirit wilderness.
Shadowspire: 3 people, 3-4 quests and tower areas.
Dragon: one boss, acquisition contacts, 3 acquisition chapters and trigger-only hunt.
Dreams: 8-12 residents, boss, up to 2 lieutenants, 3 chapters and aftermath.

**Rule budgets**
Aim for 4-8 additional rules in compact updates, 8-14 for Oni routes, 8-12 for dragon activation/pursuit/cleanup. These are review allowances, not quotas. Reuse custody, board, promotion, anomaly and portal logic. Count native generated quest checks as runtime work too.

**Release criterion**
Each update needs a small complete loop with a credible failure/decline path and a persistent return visit. More locations or triggers do not compensate for an unplayable ending. Tune enemy density using actual ordinary-character play, not the removed developer preset.

<!-- PAGE: QA -->
# 32 / Validation and executable fixtures
**Static gates**
Real keys resolve; typed completionCondition objects; required trait arrays; initialKnown rather than known; canonical full names; valid paths/areas; actual itemTypes; supported effect/operator/target shapes; current field caps. PROPOSED names and PLAN helpers never enter the export.

List each key's initializer, writer, reader, reset and scope. Execute computed-key scripts. Terminal flags must disable future incident producers. A literal search is not a sufficient writer audit.

**Minimum fixtures**
Prison: fresh case, same-day repeat, accepted/blocked skip, review, discharge, escape, knockout, property.
Guild: ranks, missing badge, wrong participant, stale proof, fresh instance, failed review, promotion, duplicate settlement.
Crucible: start, incapacity, concession, loss, interruption, duplicate result, prize, next edition.
Oni: authorized route, anomaly intercept, genuine/unrelated item, torii opening without entry, fixed return.
Shadowspire: no admission, solved approach, revisit, refusal, theft and unknown ownership.
Dragon: zero/one/multiple carriers, double summon, each realm, indoors, disposal/recovery, fall versus death, repeated cleanup.
Dreams: before/after cure, pre-quest victory, trophy loss, old queued incident and return.

Mocks must reflect check() return shapes and effect targeting. Include missing/empty values and simultaneous events. A fixture proves its model only; an untested actor correlation is not multiplayer certification.

**Live gate**
Import a fresh copy in current Studio; record build/channel/date; save successfully; play with ordinary characters. Measure time to meaningful choice, false completion, missing actors, duplicate reward and movement delay. Test refusal, failure, retreat, reload and repetition. Do not reintroduce the developer kit.

No full-world implementation, Studio import or live gameplay certification is claimed by this planning document.

<!-- PAGE: Handoff -->
# 33 / Handoff and save compatibility
Use world-draft/WorldAlpha - World.json as baseline. NPC edits belong in the JSON roster, not a retired npcs folder. Synchronize affected section exports after publishing a new full world.

If a newer user export exists, three-way merge against the actual baseline and preserve image URLs, crops and coordinates. Never overwrite the user's recent Studio work with an older generated candidate.

**Per-update package**
Full export; patch notes; changed entities; state-key manifest; fixture results; local validation; live checklist; known limits; rollback. Keep this document's editable source with it so decisions can be revised.

**Existing saves**
A new export is not an automatic save migration. Preserve IDs where practical. Renamed actors require a full reference audit and identity preservation. Initialize missing keys only. Never reset a completed quest, replace a saved trophy or restart a resolved dragon. Verify which edits propagate before offering migration instructions.

**Protected behavior**
The existing level-20 anomaly is once-only and independent of briefing. Evertree Base - Portal Room stays the hub. Court keys remain permissions. Silken trophy and Ryūka Marufuji callback preserve their identities. Thesis stays a capstone. Broad magic learning and Time restrictions remain. Mandatory morning classes and free afternoons continue around optional content.

**Open decisions**
Final cast names/cards and affinities; map keys/coordinates; exact health/modifiers; fees and prizes; Oni government specifics; torii persistence after item loss; Vladimir Kujo's immortality limits and history; Dream Magic scope and creation access. Resolve each at its build pass. The proposals here do not silently declare those facts canonical.

The following two appendices give concrete boss and test skeletons. They are design tools, not additions to the world file.

<!-- PAGE: Sources -->
# 34 / Evidence register
**S1 - Observed project baseline**
Alpha28, WorldAlpha - World.json. SHA-256:
4a54f064fbc25712d765f710dd842f971076097db46b1d7f022e38d046280c68
Existing geography, quests, custody, portal, promotion and actor definitions were inspected. The file remains unchanged.

**S2 - Community Triggers**
https://wiki.unofficial.voyage/mechanics/triggerDefinitions
Effects, conditions, scripts, phases, scope and budgets. Recheck Studio before build.

**S3 - Community Quests**
https://wiki.unofficial.voyage/world/quests
Typed completion, state and completion effects. Example designs here are original.

**S4 - Community scripting patterns**
https://wiki.unofficial.voyage/appendix/scripting-patterns
Reference for bounded state logic.

**S5 - Geography and generation**
https://wiki.unofficial.voyage/world/realms
https://wiki.unofficial.voyage/other/locationSettings

**S6 - Actors and objects**
https://wiki.unofficial.voyage/world/npcs
https://wiki.unofficial.voyage/world/npcTypes
https://wiki.unofficial.voyage/world/itemTypes
Local Character Creation Format and Runtime Content Boundary Checklist were consulted.

**S7 - Official feature evidence**
https://voyage.io/whats-new/patch/patch:100001188
Patch 2.43.0, 21 September 2026: quest controls and NPC-aware triggers. Establishes availability, not every current field shape.

**S8 - Music**
https://wiki.unofficial.voyage/other/gameplayMusicSettings
https://voyage.io/whats-new/patch/patch:100001203

**S9 - Creator decisions**
Release-description Markdown and planning answers, 30 October 2026. They override provisional suggestions. ChikaraOld and LuxcelliaUpdated informed lightweight routine/event comparisons; unique lore was not transplanted.

<!-- PAGE: Boss specification -->
# Appendix A / Major opposition build sheet
**Named NPCs versus npcTypes**
Vladimir Kujo, the unique chained dragon and the nightmare villain are authored NPCs. Repeatable defenders, animals and ordinary nightmare creatures are npcTypes. Only individually meaningful lieutenants need permanent cards. Never replace a dead authored boss with a same-role generated stranger.

**Dragon proposal**
Tier boss; level 70 as first calibration; initialRelationship -100; initialKnown false until a real revelation. Define size, movement, mage-captor hatred, carried-link tracking, cross-realm following, finite attacks and a clear weakness in its remaining restraint. A hostile score supports the disposition; NPC Intents and personality must also establish actual attacks.

**Somnarch proposal**
Tier boss; level 60-70 provisional; deeply negative initialRelationship. Select a real creature identity and full canonical key before export. Its curse comes from an established focus; loss of that source limits its methods without inventing an automatic player win.

**Phase design using existing mechanics**
A one-time npc-health-percent threshold can write a phase flag and inject a changed tactic. Example: <=65% exposes a damaged restraint; <=30% causes desperate aerial aggression. Never heal back to full for a phase or replay it after reload. These flags cue tactics, not a native custom phase API.

A preplaced lieutenant can become active through supported placement, but summoning narration alone cannot resolve its damage. The player may win early or bypass one defense through a genuinely resolved approach. Do not force the boss immortal until every planned cutscene occurs.

**Boss tuning evidence**
Record ordinary party levels, current resources, successful hits, rounds to victory/defeat, retreat opportunities and cost enforcement. Change supported stats from evidence. Level alone is not a complete difficulty model. Native daily healing must be considered during a multi-day chase rather than silently resetting wounds on each map transition.

<!-- PAGE: Fixture skeleton -->
# Appendix B / Fixture and state manifest skeleton
PLAN DATA - local authoring record, not exported game state:
```text
key: cd_dragon_resolved
scope: traveling party / this unique dragon
initial value: false only when absent
writer: confirmed dragon-death handler
readers: activation, pursuit, phase and trophy handlers
reset: never during this campaign
item relationship: stale links cannot restart resolved hunt
```
PLAN CODE - mock contract:
```text
given state:
    started = true; resolved = false
    dragon alive; carrier has 1 link; party moved
when pursuit controller evaluates:
    expect one placement of same dragon
    expect no inventory grant
    expect no scripted automatic damage
    expect no new dragon identity
```
Repeat with zero carriers: no tracking move; actor and wounds persist. Repeat with resolved true: no pursuit even if link remains. Repeat death cleanup twice: one ending, one trophy owner, no second payout.

**Acceptance trace for each feature**
Record actual input; structural gates; semantic result if used; exact effect array; storage before/after; target recipients; next-turn position; visible narration. A map location change that arrives a turn late is a failure to investigate, not proof the prose fixed it.

**Final design guard**
A required flag without a producer is a blocker. A computed producer without a fixture is a risk. A permanent outcome without disabled future incident writers is incomplete. A perfect mock run without Studio/playtesting is not a release certificate.

**No world changes were made for this blueprint.**
