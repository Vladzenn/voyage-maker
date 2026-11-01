# Crucible championship card — current mechanics

Controller v2 · 2 November 2026. This supersedes the full-bracket/review design in the original Crucible guide. It is implemented in the canonical world; live Studio and combat behavior still require testing.

## Merge and scope

The merge base is the author's Studio export `eefdd39e-e77a-4b8e-b870-5216d4c9022a`, SHA-256 `c5fc0b2262b280d8c6c0632f7c16c558b78b74bd1967ee95787583cb9a64dc74`. It adds the Conservatory region map, the three location images and adjusted marker coordinates. All those edits are retained exactly. Every incoming NPC, item and ability is preserved. The protected Spider Realm, its events and existing portal behavior are unchanged.

The tournament remains an optional persistent activity, not a new Game Mode. Controlled championships/exhibitions support one human. NPC companions can attend outside the ring. Adding another human or changing entrant identity cancels the controlled entry without transferring it or an earned prize.

## The smaller exact record

Trigger storage `cc1` now holds version 2, edition, entrant, named cup, division, a fixed list of two or three player bouts, current index, outcome, optional-care entitlements, uncollected prizes and next-edition tick. Each bout has an actual opponent, arena, stage label and—only after opening—a start tick. One result can then be recorded. There is no NPC-versus-NPC tree, `fill()` simulation, `away` grace period, review state or replay loop.

The active phases are **waiting** and **live**, alongside idle/closed. A fixed championship card is announced at registration. Opponents retain actual levels; the ordinary candidate band is ±2 at player levels 1–10, otherwise the greater of four or 30%. A smaller available pool can use nearby lower-level candidates without over-level padding. At least two eligible opponents are required. Three yields opening bout, semifinal and final; two yields semifinal and final. This represents the player's scheduled title route, not an independently simulated full tournament field.

Candidates must be at the venue, outside the player's party/combat and not known incapacitated. The same rule applies to existing visitors such as Ragnar Leonhart. Selected scheduled visitors remain reserved through the unchanged touring hold. Repeated registration does not redraw an active card. If the player outgrows the existing pool, the officials announce the actual lower-level opponents rather than inflating their levels.

Cup names and purse are unchanged: First Bloom Cup, Highsun Clash, Harvest Crown and Frostglass Championship; `80 + min(700, floor(entryLevel × 10))` marks for the title. Names do not imply a reliable seasonal calendar. A closed title entry waits **100 completed engine ticks** before another championship. Exhibitions do not change that cooldown.

## Waiting and spectating

Before and between bouts, the entrant can use the Grand Stands/benches, Competitor Lounge, Infirmary, Concourse, Practice Gallery and other areas inside The Eternal Crucible. No timer forces readiness. Moving internally does not withdraw or advance the entry. Normal narrative scenes handle food, conversation, training and watching other matches.

The final user steering deliberately removes bench-specific parsing. A plain semantic question recognizes actual agreement to start the called bout; another recognizes explicit forfeiting of the entry. Movement and spectating alone do neither. No bench keywords, special movement cases or regex decision tree determine tournament status. Tests supply those intended semantic answers; they do not prove the model will always recognize the meaning correctly.

Watched NPC matches do not write the player's result. They can be narrated using appropriate actual characters, without claiming an independent combat simulation or changing scheduled future opponents. A named NPC's real incapacity is still respected if they later become unavailable for the player's card.

## Opening and settling a bout

The official calls the current pairing; explicit readiness opens it. Readiness is not an attack. Actual incapacity blocks opening, but partial Health, Mana or Stamina is allowed and no exact maximum-resource check exists. Player resources are never silently filled to meet a gate.

If a scheduled opponent is incapacitated, absent, in combat or otherwise unavailable before opening, no combat victory is recorded. The officials announce an unused suitable substitute and wait for fresh readiness. If none remains, the edition is cancelled with no unearned trophy. Substitution does not change anyone's authored level or duplicate an already scheduled opponent.

Only a **started, unresolved current bout** can receive a result. The planning observer checks actual Health after the opening tick. Semantic conditions handle genuine surrender, referee stoppage, ring-out and disqualification for the exact current pair. A semantic win outside the current arena is rejected; an actual referee/ring-out loss can settle after the entrant has left the ring within the venue. An incapacitated player cannot be converted into a winner by celebratory narration. Missing NPC Health is not zero.

**Double knockout:** both contestants are eliminated from this title run under rules announced at entry. The run closes immediately, grants no title prize and creates the normal care entitlement. There is no review or replay dead end. In a friendly exhibition, a simultaneous fall is a draw, with care and no title effects.

Results are stored before treatment. Native NPC health recovery after a real stopped bout can restore the opponent's recorded starting Health; it never undoes their loss. Player care remains ordinary supported narrative/resource updating. Exact revival/combat-removal behavior in Voyage is not proven by local fixtures, especially in native Permadeath.

## Care, exit and prizes

All actually stopped bouts—including simultaneous falls—create appropriate optional-care entitlement. An unharmed fighter needs no fabricated wound and can continue directly. Care can be accepted while waiting or after closure, not during a live bout. No duplicate healing item is granted by these controllers.

Voluntary withdrawal means **explicitly forfeiting the entry**. Movement alone does not close it, whether to another area or outside the venue. A waiting entry remains available until continued or forfeited. A started bout can still be settled through a genuine surrender, knockout, ring-out or referee ruling; officials may rule a live departure a loss, but there is no location-driven automatic withdrawal or grace-period state. Returning never reopens an already settled loss or forfeit. This supersedes the earlier proposal for immediate venue-exit withdrawal.

A win records the result and calls the next pairing without starting it. The final win closes the card and records an owed purse/trophy. Explicit collection grants the native Mark payout and one Crucible Championship Trophy once, retaining its owner's identity across later entries. Existing unpaid prizes survive. An ordinary practice win, pre-start absence, cancelled entry or journal repair cannot mint the trophy.

A loss closes the player's title run without inventing a champion among unobserved NPCs. Other sporting activity can continue narratively. `Crucible status` reports the current card, phase, opponent and owed awards without changing them. Semantic recognition and an interruption exactly between persistent mutation and native effect dispatch still require live verification; idempotent scripts are not a platform transaction guarantee.

## Existing-playthrough transition

The initializer recognizes older v1 stored state. It preserves history and earned unpaid awards. An unfinished old bracket is explicitly cancelled without a fabricated result, prize or new cooldown penalty; officials explain the schedule change on the next venue visit. Old closed entries retain their existing cooldown. This migration only matters if updated definitions actually reach an existing playthrough; importing a world in Studio is not a guarantee of live-save migration.

## Conservatory navigation

The same compact route script now runs in planning before narration and again in state as a position-only backstop. It operates across the Conservatory realm and recognizes common directed requests for the Grafting Heart/Threnvoss. Until both actual tending circuits are settled, a requested or actual jump retains/restores the last safe location and area. If no safe address has yet been observed, it uses the outside of the inner lattice. NPC companions receive the same placement correction.

This borrows the protected Spider Realm's two-pass navigation approach without changing its records. It uses supported state/effect operations, not an invented cancel-navigation API. Actual map-click ordering and native movement must still be tested in Voyage. The Mourning Garden remains an optional side location; no new mandatory three-location progression was requested. Existing chamber paths, encounters, boss, trophy resolution and portal returns are preserved.

## Verification

`node tools/test_crucible.cjs` dispatches to the v2 fixtures. They execute actual emitted scripts and exercise the five previously missed transitions, including double falls without manually healing first, pre-start NPC incapacity, incapacitated readiness, exit/return and unfit background contestants. Additional cases cover ordinary movement/spectating without invented forfeiture, explicit withdrawal, ring-outs, prize duplication/ownership, partial-health readiness, cancelled substitution, human-roster changes, exhibitions, v1 transition, portal return and both navigation passes.

Preservation fingerprints cover every incoming NPC/item/ability, all unchanged sections, all location media/coordinates and protected Spider configuration. `tools/crucible/revision-preservation.json` records the source and allowed changes. Existing item, creation, adventurer, schema and budget checks also run. These are local fixtures, not a live Studio import or a model-recognition test.

Before release, test one fresh entry from registration through victory, a genuine loss, watching other matches, both knockout cases, partial-health readiness, ordinary care, an unavailable opponent, actual venue exit and repeated prize collection. Test the Conservatory with typed movement and map/area clicks before/after both circuits. Verify actual UI addresses, actors, resources and inventory independently of narration. Use ordinary play before relying on nonlethal handling in native Permadeath.

Mechanics reference: [Voyage trigger timing and supported reads/effects](https://wiki.unofficial.voyage/mechanics/triggerDefinitions). Narrative pacing reference: the read-only Luxcellia tournament templates and Chikara Power Circuit records documented in the preceding comparison report.
