# Crucible audit, reference comparison and simplification proposal

**Implementation follow-up:** the user approved the smaller card and then simplified withdrawal further: explicit forfeiting ends the entry; movement alone does not. The suggested immediate venue-exit rule below is superseded. No bench-specific parser was retained. Read [current v2 mechanics](../world-draft/Crucible%20Championship%20Card%20-%20Mechanics.md) for the implemented flow. The reproductions below remain historical evidence of v1 failures.

2 November 2026. Research and reproduction only: the playable world has not been rewritten in this pass. The current tournament should be held for repair before publication. Earlier successful fixtures establish only the cases they actually exercise.

## Findings reproduced

Audited canonical world SHA-256: `f149fc434b8468de31cd3182fdf6f8d049c5e5949ae464cb1c86987891f488c8`.

Run `node tools/audit_crucible.cjs research/crucible-audit-2026-11-02/reproductions.json` to exercise the emitted scripts through the existing harness. The diagnostic supplies semantic answers; it does not prove that Voyage understands natural language or reproduces its exact dispatch/death timing.

| Case | Actual observed fixture result | Assessment |
|---|---|---|
| Scheduled opponent becomes incapacitated before opening | `ready` enters review with no `startedTick`; review then records a player win and advances | Confirmed erroneous unstarted-match victory. No authoritative start check in review. |
| Both contestants reach zero Health | Enters review; repeated review leaves no winner and no care entitlement | Confirmed missing recovery/ruling path. Explicit withdrawal can close it, so it is not an absolutely irreversible storage deadlock. It still fails the intended ordinary recovery flow. |
| Leave during a live bout and return promptly | `away` remains `away`, then closes as withdrawal despite return | Confirmed incomplete grace-period implementation. Choose immediate forfeit or a real suspension/resumption rule. |
| Entrant already has zero Health | Readiness enters `live`, storing starting Health zero | Confirmed missing participation check. Positive Health/actual capacity is distinct from demanding full bars. |
| Nonplayer contestants become unfit after registration | Offscreen calculation awards wins to zero-Health NPCs; Natsume Aiba becomes champion at zero Health | Confirmed absent live-availability checks in NPC bracket resolution. |
| Sit in Grand Stands before being called | Remains `ready`, same recorded match | Mechanically allowed, provided the location remains The Eternal Crucible and semantic readiness/withdrawal do not falsely match. |
| Sit in Grand Stands between bouts | Remains `between`, same recorded match | Mechanically allowed. No need to withdraw, fight immediately or receive treatment. |
| Walk to Grand Stands during a live bout | Observer leaves the bout `live` | Native observer checks leaving the location, not ring boundaries. Actual ring-out/referee outcomes depend on semantic recognition. |

The earlier double-knockout fixture manually restored both actors before review. That verified replay behavior after recovery, not whether the system offered or performed recovery. Pre-start unavailability and returned-within-grace cases were not in that suite. Schema and happy-path success did not establish these transition invariants. The audit is a correction to the earlier assessment of readiness.

## What “I leave to the benches” means

Bench seating should resolve to **The Eternal Crucible - Grand Stands**, inside the existing parent location. Before/between the player's bouts, changing to that area must preserve registration and the announced opponent. Waiting, watching, talking, browsing concessions or visiting the infirmary should not automatically start a match, invent an injury or abandon the edition.

The word “leave” alone is not a withdrawal. The current observer already distinguishes location from area, but the withdrawal action still relies on a semantic query. Supplied false answers in a mock are not proof the live AI will interpret every phrase correctly. A revised withdrawal query should explicitly exclude benches/stands/lounge and require an explicit cancellation of entry or an actual exit from the whole venue. Resolved geography should support the decision rather than a regex searching for “leave.”

When a live bout exists, leaving its ring is a separate sporting question: a referee can stop it under announced rules. That is different from an entrant watching during their free interval. An ambiguous statement should not silently create a tournament loss.

The current controller does not independently stage NPC-versus-NPC combats that unfold while the player waits. It stores a bracket and resolves nonplayer branches abstractly. Spectating can be narrated, but claiming a complete independent live tournament simulation would be inaccurate.

## Luxcellia: narrative tournament adventures

Inspected read-only `sources/Luxcellia.json`, plus the newer Kato export supplied in attachment `5f2c3317-f5d6-44fd-aabf-64f3b95caeb0`. The former Downloads/LuxcelliaUpdated.json path is unavailable locally; this was not a fresh live inspection of its creator's world.

Relevant records:

- `Tournament Arcs`: a nonconclusive quest template whose goal is receiving the final result of a run. It asks generation for rounds, distinct rivals, stakes and aftermath. Its authored completion query is empty; no script manages a full eight-person bracket in the inspected record.
- `Rookie's Festival: The Rookie Bracket`: a more specific finite story-chain segment centered on the player's earned placement and recurring rival. Chain triggers surface the next story once the preceding quest is completed.
- `arena-and-tournament-culture`: social context for sporting traditions, spectators, rivalries and associated events.
- `Knight's Tournament Grounds`: arena, training yards, armory, stands and hospitality areas inside one parent location. This gives competitors room to do things between bouts.

The newer supplied Kato export retains this overall tournament approach. Dedicated tournament/bracket scheduling scripts were not found in either inspected export. This is configuration evidence, not proof that its live AI never loses track of a match. Nor is its insistence on a hidden conspiracy in every generic tournament a fit for Glowhaven's ordinary sporting editions.

**Borrow:** specific rivals, an understandable run goal, strong between-round setting, normal quest progression and aftermath that can include a loss. Keep mundane championships possible. Do not replace the prize's exact one-time grant with a vague narrative claim.

## Chikara: narrative events with a small results ledger

Inspected read-only `sources/ChikaraOld.json`. It is explicitly an older snapshot; no claim is made about its current published revision.

Relevant records:

- `Power Circuit Registration`: registration and willing roster selection are distinct from a later event's format. Unused competitors can watch, train or socialize.
- `Power Circuit: Open Qualifier`: calls a competitor to a real arena, permits preparation and spectating, then establishes a result and future options.
- `Power Circuit Event`: native quest objectives cover format, roster, rules, scheduled bouts and aftermath. The narrative handles match progression rather than a JavaScript tree of all contestants.
- `Power Circuit Ledger: Win` and `Power Circuit Ledger: Loss`: recurring story-text token checks grant Circuit Points. Separate threshold events announce ranks.
- The system lore explicitly separates being registered from being an active combatant and supports different individual/team formats narratively.

**Borrow:** registration is not readiness, a call to one's own match matters, spectators retain agency, and a small ledger can record important outcomes while normal play supplies the scene.

**Do not copy literally:** its visible win/loss markers are not independent evidence of a real match. Its inspected points effects target all players, and the two marker triggers do not carry a distinct match/edition receipt preventing repeated processing of the same result. Those are not suitable replacements for our entrant-scoped, idempotent trophy dispatch. A large amount of tournament lore is not the same as a verified mechanical bracket.

## Recommended direction: a simpler player-facing championship card

Keep the thirty-two competitors, portraits, actual levels, arenas, staff, prize and hundred-turn edition cooldown. Simplify the scheduling model instead of deleting the interesting people or relying entirely on narrative memory.

At registration, create a fixed player-facing card of suitable named opponents and arena assignments. A normal large championship can retain opening bout, semifinal and final; a smaller field can retain two bouts. Record only this entrant's meaningful scheduled bouts. Announce the card once; no reroll from repeated registration. Other matches can appear as brief announced results or spectator scenes rather than a scripted simulation of every nonplayer branch.

Suggested state:

```text
edition, entrant, cup, levelDivision
card = [{opponent, arena, startedTick, result}, ...]
currentBoutIndex
phase = waiting | live | closed
outcome = competing | champion | eliminated | withdrawn | cancelled
prizeOwed / prizePaid
nextEditionTick
```

This is a design sketch, not a new Voyage schema. Store it through supported trigger storage; do not add fields to native NPCs or quests. The selected card and outcomes are the small exact ledger; ordinary scenes remain narrative. It is deliberately a player-facing championship run, not a claim that a complete independent tournament tree is still being mechanically computed.

### Consistency rules

1. **Waiting is free:** walking among existing venue areas, watching, eating, talking or resting does not advance or cancel the card. An announced call and explicit readiness begin only the current bout. No exact full-resource gate.
2. **A bout must really start:** record its start before accepting a result. Pre-start NPC incapacity never becomes a combat win. Announce a suitable substitute from unused eligible entrants, or postpone/cancel that edition if none is available. No duplicate opponent or resurrected eliminated rival.
3. **Capacity matters:** do not begin when the registered player is incapacitated. This is not a demand for maximum Health, Mana or Stamina. Optional treatment remains appropriate to actual condition, including unharmed fighters.
4. **One result per actual player bout:** observe only the started entrant/opponent pair. Another match watched from the stands, a dead summon, a boast or an earlier edition cannot advance the card. Actual knockout, surrender or referee stoppage can decide it.
5. **Announce a finite double-knockout rule:** recommended first-release simplification is both eliminated from title contention, with immediate closure and appropriate care. No replay/review loop and no championship trophy. That is a sporting rule to announce before entry, not a surprise penalty.
6. **Use an honest departure rule:** leaving the whole venue withdraws the entry immediately; remove the broken grace period. Moving to benches inside it is not departure. A true medical/referee suspension would require a deliberate explicit rule, not an accidental `away` state.
7. **Care follows a stopped bout:** include simultaneous falls and medical stops, not just a completed win/loss handler. An unharmed competitor can decline and continue. Medical narration cannot reverse the result.
8. **Keep the reliable reward owner:** only a completed championship card creates an owed trophy/purse. Actual collection grants it once, with the existing owned item retaining its role in the portal discovery.
9. **Use native quests where useful, without duplicate ownership:** an optional journal entry can describe the entered edition and current opponent, but it must not independently award the championship trophy. A lost/withdrawn run should close clearly, not sit forever waiting for a win objective. Normal quest repair must not manufacture championship proof.
10. **Keep the first implementation's human scope:** this proposal does not silently expand controlled championships to multiplayer. Team/parallel human tournament support remains a separate design problem.

There is an alternative: repair the full bracket by adding started-attempt checks, explicit no-contest handling, availability validation at every NPC fixture, and consistent departure rules. Those repairs are feasible, but maintain substantially more state for NPC-only outcomes that add little to the player's chosen run. I recommend the smaller card for this world.

## Conservatory guard: separate confirmed timing weakness

`cc1_grove_inner_gate` has mechanical conditions and no explicit phase. The community reference says that defaults to the state phase, after narration. Its current behavior is corrective: the party has reached the heart address, then it moves the party back if the circuits are incomplete. The mock proves correction, not prevention of a prematurely narrated boss scene.

Recommended repair in the subsequent implementation: use an explicit planning correction so narration receives the permitted address, inspect the attempted-route pattern already used by the Spider Realm, and retain a state-phase safety check for actual UI movement/reconciliation. Verify actual map and area clicks in Voyage; do not claim a pre-action navigation interception API that has not been documented. Read the Spider implementation as a pattern without changing that protected realm.

## Evidence and next validation

- [Community trigger timing and supported reads/effects](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): mechanical-only triggers default to state; explicit planning runs before narration after action outcomes. This is current community documentation, not a firsthand engine trace.
- `research/crucible-audit-2026-11-02/reproductions.json`: exact observed outcomes for the current world hash.
- `tools/audit_crucible.cjs`: read-only diagnostic, deliberately separate from the existing passing release fixtures. It reports known-bug observations rather than asserting they must remain broken forever.

Before a revised release, test pre-start incapacity, double falls without manually healing first, interrupted readiness, internal bench movement, actual venue departure, unavailable scheduled opponents, spectator fights, repeated result prose, duplicate collection and old-edition callbacks. Then perform live Studio/normal combat tests, including actual geography updates and nonlethal/Permadeath behavior. A simpler design still needs those tests; fewer scripts alone do not establish correctness.
