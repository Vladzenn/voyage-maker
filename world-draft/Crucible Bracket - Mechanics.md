# Crucible: recorded elimination bracket

Current implementation: **controller 3, 2 November 2026**. This replaces the championship-card revision. The earlier full-bracket and card documents remain historical.

## Player experience

At the Eternal Crucible, explicitly register for an announced individual championship. Registration costs nothing. Officials choose a suitable four- or eight-person field from actual available competitors, preserving their authored levels. A small field has a semifinal and final; a larger field adds an opening round. Named cups rotate by edition rather than pretending to track reliable seasons.

The initial draw is stored once. Repeating the request cannot reroll it. Other competitors eliminate one another, so later opponents emerge from the bracket rather than a preselected list of people who all fight the player. An entry closes on a genuine loss, explicit forfeit, championship victory or an administrative cancellation. The next title edition waits 100 completed engine ticks. Exhibitions remain separate and do not award title prizes or change this cooldown.

Conversation, spectating, resting and movement remain ordinary play. They do not automatically start a fight or withdraw an entry. Explicit readiness opens only the currently called bout. The fighter must actually be conscious and assessed, but need not have full resource bars. An unavailable opponent is replaced by a suitable unused competitor and announced before another readiness decision. If no replacement exists, the edition closes without inventing a fight or a trophy.

## What is exact and what is semantic

The stored ledger owns the field, bracket nodes, current player bout, real start, terminal result, champion, cooldown and owed/paid prize. Registration, readiness, explicit forfeit, official surrender/referee outcomes, accepted care and prize collection use narrow semantic conditions. Dialogue, ordinary social reactions and recovery do not have their own state machines.

The planning observer supplies one narrow native-Health safeguard: after an actual start, both contestants must still occupy the assigned arena for a zero-Health result to settle automatically. If either leaves that arena, the bout needs an official semantic ruling. Returning does not convert an unrelated lounge injury into victory. There is no bench parser, departure grace timer, extra review phase or replay loop. A movement alone is neither a result nor a voluntary forfeit.

An actual knockout can override contradictory victory prose while the uninterrupted participants are still in the ring. Outside that scope, the official ruling supplies the meaning. This cannot make the AI infallible; it stops the reproduced automatic location/Health error without demanding a new evidence flag for every attack.

## NPC-only matches

Each NPC-only match receives one seeded, stored abstract official result when its round can resolve. Actual levels influence the draw. Entrants must still be present, not committed to the player party, and not known incapacitated. Unavailable competitors cannot win a newly resolved match; an administrative advance is recorded separately from a played victory. Both unavailable means a vacant advancing slot.

This is a bracket simulation, not offscreen native combat: it does not spend NPC Mana, fabricate wounds, run attack turns or award the player the NPC's winnings. After the player loses or forfeits, the remaining NPC rounds conclude abstractly and history records the resulting champion, or no champion if no valid field remains. Already recorded results never reroll. A historical winner who later becomes incapacitated does not retroactively lose an earlier valid result.

## Stops, care and prizes

Surrender, knockout, ring-out and referee stoppage settle a real started bout. Simultaneous knockout eliminates both and provides a care opportunity; it does not strand a review phase. Regulated bouts use nonlethal sporting intent, finite legal summons and no outside attacks, healing or buffs. Live-bout mana potions and external reserves remain prohibited.

The result is recorded before care. Appropriate treatment or rest is optional, and an unharmed person needs no invented injury. Player recovery uses normal resource updates, without a full-bar gate. The controller can restore a stopped opponent toward its recorded starting Health; native incapacitation/recovery ordering still needs a live test.

Only a player who wins the actual final gets an owed prize. Collection grants the announced Marks and one exact championship trophy once. NPC champions get no player inventory grant. Pending earned prizes survive new editions and old-controller transitions. An unfinished older entry is closed honestly during the revision rather than transformed into an invented bracket victory.

## Multiplayer boundary

Controlled bouts currently support one human session. A second human joining **suspends control without cancelling or transferring the entry**. It can resume when the original entrant is the sole human again. No prize is paid to a spectator. This is deliberately not a claim that party-shared area movement can isolate a multiplayer fighter from spectators.

## Release checks and live tests

Local fixtures execute the emitted scripts and cover field selection, eliminations, eventual NPC champions, substitutions, unavailable finalists, repeated callbacks, double knockout, unrelated lounge incapacity, return after interruption, explicit forfeit, identity changes, spectator suspension, cooldown, prize ownership and preserved dungeon routes. They supply semantic answers and are not live AI tests.

Live checks still needed: real combat/knockout timing, ordinary-language referee recognition, nonlethal stoppage in native Permadeath, simultaneous falls, leaving a live arena, joining/leaving humans, opponent placement and post-bout recovery. The official Creator API draft validator accepts the resulting world; that confirms schema/authoring validity, not runtime behavior.
