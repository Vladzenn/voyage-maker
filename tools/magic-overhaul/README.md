# Magic Overhaul — implemented hybrid build

6 November 2026. The author explicitly requested implementation and selected **hybrid reactions with mechanical bookkeeping** after the interface limitations were explained. This is Minor Patch 5. The earlier mechanical proposal is retained as design history; this document describes the delivered implementation.

## Merge base and scope

The complete supplied Studio export `0e0a46a8-91ce-41db-bcf2-d041c45b9b1b` is the input, raw SHA-256 `813f12485175d20fb4da47882bac8ffde207e7756af97360e81ef97d5434c9c3`. Its newer pins at The Pearl and Thistle, Opaline Arcade, Caelrath Amphitheatre, The King's Lists and House Orselle Salon are preserved exactly, including the Amphitheatre's region change.

`world-draft/WorldAlpha - World.json` is the applied canonical world. The delivery copy is `output/magic-overhaul-2026-11-06/The Schools of Magic, Arise! - Magic Overhaul.json`. The raw SHA-256 of both is `660c50c1f5a720e18b4f601333596c519e3ca4d91b6ffbdd0798c017e1e57cd0`.

All NPC cards, portraits, items, abilities, quests, arcs, starts/order, regions, media, music, voices, progression settings and Spider-specific events/content are preserved. Twenty-four NPC type defense arrays and Venom-Hardened only migrate the exact `poisoning` channel to `poison`; their protection is equivalent. No new quests, cast, equipment, art or threshold-reducing items were added.

The scoped review is [review.json](review.json), with original values and exact post-change hashes. `previous_world.cjs` reverses only this exact reviewed world for historical fingerprint tests. Current mechanics are tested against the delivered world separately, not against the inverse. [Change Review](../../output/magic-overhaul-2026-11-06/Change%20Review.md) lists the affected records without requiring a large textual JSON diff.

## What is mechanical, and what still relies on AI

| Concern | Delivered owner | Verification limit |
| --- | --- | --- |
| Damage names, icons and existing defenses | Native combat settings and defense arrays | Structural/reference checks |
| Actual landed element, target and previous-turn imprint | Action Info and short combat memory guidance | No generic resolved-hit API was verified |
| Reaction damage, brief NPC/player debuffs and their expiry | Action Info, Story and summarization | AI-guided; not exact scripted combat math |
| Recognition of a real reaction / surge release | Two declared player-scoped semantic rules | Local fixtures supply answers, not AI judgments |
| Charge, readiness, reset and visible gauge | Typed player-scoped effects and native character traits | Tested in local phase/recipient fixtures |
| Successful scroll-study judgment | One declared player-scoped semantic rule | Reader/formula completion needs live recognition |
| Scroll formula, ability and one-copy consumption | That rule's native effects, filtered to satisfying holders | All 130 formulas and multiplayer fixtures tested |

No invented `onDamage`, `damage-type` trigger, ability `damageType` member, NPC stat-modifier effect or armor-penetration field is used. NPC base attributes, level, armor and damage are never rewritten to imitate a temporary debuff. The narrator cannot apply a second Health subtraction after supplied combat results.

Native damage and success configuration is deterministic; the proposed percentage math and temporary combat penalties remain instructions to the engine's AI resolver. A correct JSON file and passing fixtures cannot establish that the live resolver follows those instructions on every turn.

## Reactions

[reactions.json](reactions.json) is the compact source table. It has 24 unique unordered pairs across sixteen nonphysical channels, exactly three partners per channel. Each channel has one 20% damage recipe, one 10% plus small-debuff recipe and one 0% plus stronger-debuff/utility recipe. Sixteen reactions therefore do something beyond damage.

- One actual landed eligible hit leaves one imprint on its exact target through the following completed party turn.
- A separate compatible hit consumes it. The reaction leaves no fresh imprint. Same element refreshes; an unlisted eligible element replaces.
- Slashing, piercing, bludgeoning and Soul neither prime nor consume imprints. Weather, harmless displays, misses, full immunity and a technique combining its own elements do not establish a reaction.
- At most one reaction per target and one earned point per human finisher per party turn. The finisher earns the point, not the first caster or the entire party. Enemies can use the same reactions, without acquiring a generic NPC Resonance pool.
- A target has at most one reaction debuff. A newer one replaces the old one. It ends on the next applicable resolution or at the end of the following party turn, and is cleared on combat end or scene departure. An output penalty is consumed by a qualifying attempt even on a miss. No automatic turn loss, disarm, fall or duplicate contextual penalty.
- Apply anatomy, actual senses, equipment and immunity. An effect referring to an existing metal weapon cannot manufacture one. Rimebind's defense penalty is an accuracy/check penalty, not a subtraction from armor.

The damage layer aims for ordinary hit damage plus 0/10/20% reaction and, when already ready, 50% Resonance, added together before mitigation: maximum 170%, rather than multiplying two separate bonuses. This is a balancing instruction, not an observed native multiplier.

Soul is the twentieth registered channel and has no reaction partners. Where worn armor's contribution can genuinely be distinguished, the instruction proposes using 90% of that contribution for a Soul hit. It gives no universal +10% damage, immunity bypass, ward bypass or guaranteed native penetration behavior. Support and restoration do not automatically cause damage.

## Earned Resonance and phase timing

The visible resource starts at 0/20, with no passive recharge, rest gain or per-level gain. Native leveling can nevertheless refill resources. A resource-only design could therefore award an unearned burst. This build preserves earned charge independently with native traits and mirrors it back to the gauge.

There are 23 new trait definitions, not 23 simultaneous character buffs: one capability marker, one temporary earned-reaction receipt, and twenty-one mutually managed charge states (0 through 20). A character ordinarily has the capability marker and one charge state, with a receipt pending settlement after a real reaction. These traits provide no attributes, skills, items or resource maxima. They are absent from creation categories and blocked from level-up offers above the configured level cap. Their player-facing descriptions describe energy rather than implementation instructions. The trade-off is that native character status can expose an extra charge condition alongside the meter.

Forty-three purely mechanical rules initialize or settle/mirror the twenty-one states. Only the matching native player group is changed. Two semantic rules recognize an earned reaction and a valid ready surge. The full Resonance subsystem has 45 rules; these are small native rules because no verified arbitrary-player-ID effect target exists. No per-reaction state machine or shared party charge counter is created.

1. Initialization gives each actual player their own empty charge, including late joiners.
2. A real reaction adds one receipt to that finisher. The following planning settlement consumes it and advances that actor's charge once.
3. Full charge is ready for a subsequent damaging technique. The final charging action cannot retroactively boost itself.
4. A landed paid/otherwise valid damaging spell or trained technique that began already ready consumes the old charge. Misses, unaffordable attacks, healing and utility retain it.
5. If the burst also reacts, its earned receipt survives the reset and starts the next cycle at one.
6. Mechanical mirroring repairs a native refill/drift to the earned value. Receiving the resource alone does not manufacture readiness.

The fixture tests sequential and phase-snapshot condition evaluation in both trigger orders. It does not prove Voyage's action-info/phase timing. Turn-20 readiness, turn-21 damage and burst-plus-reaction need a live sequence check. Base capacity stays 20; future capacity-changing gear will need an explicit extension to the state model, not merely a resource-max bonus.

## One shared scroll-learning gate

The old thirty individual study triggers and ten registry controllers are removed. The bootstrap also retires their runtime-generated `rb_study_*` definitions if this logic is deliberately introduced into existing runtime state. Importing a new world does not automatically migrate existing games.

Three root rules replace them: a one-time catalogue bootstrap, a mechanical formula scheduler and one declared semantic study rule. The catalogue covers all 130 existing formulas. Original practical/advanced/masterwork expectations, learned-formula exclusivity and Space's Gravity Magic 25 foundation remain. Time has no scroll. Substantive research may compensate for low discipline; it grants no skill ranks.

The scheduler selects among actually held, unlearned scrolls from current action/story context. This selection is lexical/contextual; it is not proof of learning. A natural-language declared `story` condition judges actual successful study and controlled testing. Merely opening, possessing or naming a scroll is insufficient. Known formulas never consume another copy.

Only one formula is evaluated at a time. Multiple successful holders of that formula are independently filtered by native player scope; different formulas rotate across consecutive turns. Query rewrites activate next turn, so completed study can await verification for up to eight turns. Preserve the exact reader/formula in recent story memory. Selling or dropping the last copy before settlement blocks the transaction. Large simultaneous queues may need another study action after expiry; there is no claim of unlimited parallel settlement.

Successful settlement adds that actor's exact Formula trait and ability and removes one of that actor's own copies. It does not spend an ability point, teach a new affinity, grant ranks or automatically cast. The ordinary ability-generation/inventory tasks are instructed not to duplicate the transaction. Medicine handlers are unchanged.

## Success names and instruction limits

Names are Spectacular Blunder, Unfortunate Mishap, Imperfect Result, Little Triumph, Splendid Work, Stroke of Brilliance and Storybook Triumph. All seven IDs, score bounds, images and the first-successful ID are unchanged. Five name-based fishing conditions migrate with the names. The labels do not change XP, difficulty, damage bands or success probabilities.

The previous Action Info and Story functions were nearly full. Overlapping method-routing, travel, cost, practice, law and aftermath guidance was compacted to fit this update; actual routes, permissions and action ownership remain. No whole-world prompt rewrite was attempted. Compact UTF-16 sizes after implementation: Action Info 19,736/20,000; Story 29,737/30,000; Item Generation/Usage 19,849/20,000; Learned Abilities 18,138/20,000; summarization 19,713/20,000. The unchanged quest-generation field remains checked against 5,000.

## Semantic budget and remaining runtime risks

Root definitions change from 548 (456 semantic, 92 mechanical) to 556 (429 semantic, 127 mechanical). The reduction is from shared scroll learning; it is not a promise that every scene costs fewer checks.

The initialized-character audit explicitly includes the new charge traits. Tested scenes have at most eleven eligible root semantic checks. The original empty-trait fixtures would miss the reaction gate and are not presented as a full budget proof. If all six native arcs also request surfacing in the same turn, the conservative Crucible upper bound reaches seventeen against fifteen before a focused scroll adds a possible further check. That is an unverified contention risk, not evidence of a reproduced live failure or a safe universal ceiling. Active quests change the documented budget and add completion work. The test report records upper-bound warnings rather than assuming all arcs always run or silently relaxing the platform limit.

Live priorities:

1. Real hit vs miss/immunity; exact target, separate actions and one-turn imprint expiry.
2. Water/Ice Rimebind on a real NPC, followed by the appropriate defense; verify expiry and no permanent stat change.
3. A lower-output reaction, including a missed next attack, and no duplicate advantage.
4. Charge 19 → reaction → ready → landed burst; inspect actual damage and retain charge after a miss/heal.
5. Two players with different charge values; burst plus reaction; level-up/resource refill; late joiner.
6. Two different teaching scrolls studied simultaneously, failed/known scroll retention, own-copy consumption and delayed verification.
7. Busy Crucible scene with arcs, accepted quests and a ready surge. Watch whether completion/charge checks are delayed by budget contention.
8. Renamed success comparisons in ordinary/rare fishing.

## Validation and external status

Local validation checks structure, references, limits and emitted scripts. The new suite exercises all formulas, scoped transactions, four phase/order variants, charge boundaries, incoming-pin preservation and defense equivalence. Historical suites use the strict reviewed inverse only for old fingerprints; current tests exercise current rules. No fixture tests AI language recognition or exact live combat arithmetic.

The current official OpenAPI and agent guide were read, version `1.3.0-preview`. The authenticated `POST /validate` draft check was **not executed**: automatic approval review rejected sending the full private world to the official API without specific payload approval. `validate_official.py` is a reviewed read-only helper for a later approved check; it reads a process credential, an external secret file or a no-echo terminal and records no key. Nothing has been saved to or published in Voyage Studio.

Relevant references, checked 6 November:

- [Official Creator API contract](https://api-alpha.aidungeon.com/creator/v1/openapi.json) and [agent guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md): Studio authoring/validation contract, not a gameplay combat webhook.
- [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): native scopes, phases, read-only check results, declared semantic judgments and next-turn rewrites.
- [Success Levels](https://wiki.unofficial.voyage/mechanics/successLevelSettings): conditions match display names; score bounds and first-successful ID control outcomes.
- [Traits](https://wiki.unofficial.voyage/mechanics/traits): native direct grants and level-up requirement gates.
- [Action Info](https://wiki.unofficial.voyage/ai/generateActionInfo) and [Combat Settings](https://wiki.unofficial.voyage/mechanics/combatSettings): resolution guidance and damage presentation.

Rebuild without applying:

```sh
python tools/magic-overhaul/build.py --base "/path/to/the-current-supplied-full-export.json"
node tools/test_magic_overhaul.cjs "output/magic-overhaul-2026-11-06/The Schools of Magic, Arise! - Magic Overhaul.json"
```

Use `--apply` only for this original complete merge base, after checking for newer Studio edits. The builder accepts the exact reviewed before/after canonical states and fails if unrelated edits have intervened. It does not reset a checkout or silently reconstruct from an old Alpha candidate.
