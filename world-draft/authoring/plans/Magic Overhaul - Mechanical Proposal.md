# Magic Overhaul — implementation brainstorming

Planning only, 5 November 2026. No gameplay JSON or public patch notes changed.

The supplied full Studio export is the planning reference: attachment `0e0a46a8-91ce-41db-bcf2-d041c45b9b1b`, raw SHA-256 `813f12485175d20fb4da47882bac8ffde207e7756af97360e81ef97d5434c9c3`. Relative to the current canonical world, it contains location edits at The Pearl and Thistle, Opaline Arcade, Caelrath Amphitheatre, The King's Lists and House Orselle Salon. Do not overwrite these when implementation begins. This document does not merge them or replace the canonical full world.

## Accepted direction and open recommendations

The author approved reactions on both sides of combat, a base Resonance threshold of 20, and future equipment or other bonuses that can lower the threshold. Everything numerical below is a balancing proposal, not an implemented guarantee. Enemy reactions do not automatically give every NPC a player-style Resonance meter; that remains a separate design choice. Recommend player meters first, with any special enemy burst authored and telegraphed.

Recommended scope: keep the existing damage vocabulary, complete its presentation, introduce one short-lived imprint per target, use a small reaction table and add one personal Resonance meter. Do not build a different status controller for every elemental pair or introduce 171 combinations for the nineteen current damage types.

## What the current configuration actually contains

- Nineteen registered damage types. Only `fire` has a custom presentation entry.
- 868 ability records, with names, descriptions, requirements, bonus and cooldown, but no dedicated `damageType` member. Existing action guidance already tells the resolver to use the mechanism that actually lands.
- Five resources: Health, Mana, Stamina, Renown and Infamy. No Resonance.
- Seven configured success tiers, starting success at Mixed Results. Five declarative conditions directly test success-level names: three use `mixed results`, two use `basic success`.

The official public [Creator API contract](https://api-alpha.aidungeon.com/creator/v1/openapi.json) and [agent guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md) were fetched read-only. They describe Studio world editing and validation; they do not supply a combat-event subscription API. They do not prove which internal battle values trigger scripts can read. No credential or Studio mutation was used.

Community references document the following, with important limits:

- [Combat Settings](https://wiki.unofficial.voyage/mechanics/combatSettings): register damage names and configure their emoji; presentation does not add a side effect. The native ability bonus influences a check, not a damage multiplier.
- [Scripting Patterns](https://wiki.unofficial.voyage/appendix/scripting-patterns): timed conditions need custom bookkeeping or narrative handling rather than an assumed generic status-effect collection.
- [Action Info](https://wiki.unofficial.voyage/ai/generateActionInfo): impact influences damage, but requests to adjust impact are AI guidance, not guaranteed arithmetic enforcement.
- [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): stored values, typed effects and phase timing are available. No general resolved-hit event with stable actor, target, element and damage identifiers was verified here.

These are configuration observations and community documentation, not live combat tests. In particular, do not invent an `onDamage` API or a `damageMultiplier` trait field.

## 1. Damage identity and presentation

Keep existing lowercase keys to preserve damage profiles. Complete presentation through the supported emoji map, without inventing display-name or color members.

| Discipline or mechanism | Registered type | Proposed icon |
| --- | --- | --- |
| Fire | `fire` | 🔥 |
| Water | `water` | 💧 |
| Ice/cold | `ice` | ❄️ |
| Lightning | `lightning` | ⚡ |
| Earth working | `earth` | 🪨 |
| Wind | `wind` | 🌪️ |
| Metal working | `metal` | ⚙️ |
| Nature working | `nature` | 🌿 |
| Arcane force/energy | `arcane` | ✨ |
| Light | `light` | ☀️ |
| Sound | `sound` | 🎵 |
| Gravity | `gravity` | 🪐 |
| Void | `void` | 🕳️ |
| Established dark energy | `dark` | 🌑 |
| Actual psychic harm | `psychic` | 🧠 |
| Poison | `poisoning` | 🧪 |
| Cutting / puncture / blunt impact | `slashing` / `piercing` / `bludgeoning` | 🗡️ / 🏹 / 🔨 |

Consider `soul` with 👻 only if actual offensive Soul abilities require a distinct resistance category. Do not make every school its own damage type: healing is normally restoration, enchantment can modify an ordinary sword strike, summoning uses the creature's actual attack, and an illusion does not injure Health merely by being believed. A mundane thrown stone remains blunt impact; moving it magically does not automatically turn it into psychic damage. A flame-shaped harmless display applies no fire imprint.

For the initial reaction table, use the explicitly elemental damage channels Fire, Water, Ice, Lightning, Earth, Wind, Metal and Nature. Physical hits have a particular follow-up role but do not all apply elemental residue. Leave the other channels out of the launch table unless a specific interesting combination is approved.

## 2. One imprint, then one reaction

A qualifying hit leaves one inert imprint keyed to the exact target's runtime identity. It lasts through the next completed party turn: a mark from turn 12 can react on turn 13 and is expired on turn 14. Do not use in-world hours or days for this window.

- A compatible later hit consumes the old imprint and produces one reaction. It leaves no fresh imprint.
- An incompatible elemental hit replaces the old imprint. The same element refreshes its expiry.
- A physical attack preserves an unexpired imprint unless it consumes it through an approved reaction such as Shatter.
- One mixed-element hit cannot react with itself. Identify its actual primary channel; another real action is needed.
- Misses, harmless visuals and fully immune hits do not prime a target or award charge. Meaningful contact/positive damage must be established. Deliberate non-damaging primers can be designed separately later.
- Reaction bonus damage cannot prime another reaction, generate its own charge or create a free follow-up attack. No damage-over-time reaction chains in the first release.
- At most one reaction per target per party turn; at most one Resonance point per player per party turn. This prevents multihit/AoE farming. Ordinary AoE damage is unaffected.
- Natural wetness and weather can support the fiction, but should not silently create universal mechanical primers for everyone standing in rain. Environment priming is a later, explicit rule.

## Proposed launch reactions

Pairs are order-independent. Percentages are provisional bonuses to the triggering action's ordinary damage, not percentages of the victim's maximum Health. They are design targets until the delivery bridge is verified.

| Pair | Reaction | Proposed result |
| --- | --- | --- |
| Fire + Water | **Steamshock** | +25% damage; a short scalding burst, no automatic blindness |
| Fire + Ice | **Thermal Shock** | +30% damage from abrupt temperature change |
| Water + Lightning | **Conduction** | +25% damage to the actual target; no automatic chain to bystanders |
| Water + Ice | **Rimebind** | Restrained movement until the target's next action or one party turn, whichever comes first; no lost turn or universal paralysis |
| Fire + Lightning | **Flashburst** | +25% damage; no free area explosion |
| Ice + a real heavy blunt hit | **Shatter** | +25% damage; an ordinary physical route for martial characters |
| Fire + Nature | **Cinderbloom** | +20% immediate damage; no recurring burn tracker |
| Lightning + Metal | **Induction** | +20% damage; no guaranteed disarm or control of someone's equipment |
| Water + Earth | **Mire** | Briefly hinders the next repositioning action; grounded targets only, no forced immobilization |
| Wind + Fire/Water/Ice/Lightning | **Galeweave** | +15% damage from carrying the existing element through the hit; consumes the primer, no spread in the first release |

The launch has a damage category and a movement-interference category, rather than ten unique debuff timers. Rimebind and Mire use the same short-lived hindrance representation. If numeric penalties are used, choose one modest shared penalty after testing; do not invent a native stun effect or force the engine to skip a turn. Boss anatomy and established immunities still matter. No universal execution, boss freezing or armor deletion.

Later candidates include Sound + a solid imprint (**Fracture**), Gravity + Earth (**Collapse**) and a carefully bounded Light/Dark interaction (**Eclipse**). They are deferred, not automatically added to every available school.

## 3. Resonance and future threshold modifiers

Use **Resonance**, a base range of **0/20**; the first earned reaction displays 1/20. A personal successful reaction adds one charge. An ally may supply the primer, while the finisher earns the point in the simplest version. Awarding both contributors can be considered later but needs ownership tracking.

At the effective threshold the player becomes **Resonant**. Recommend that the next landed damaging spell or combat technique receives **+50% damage**, then expends the charge. A missed attack leaves it ready; healing, ordinary conversation, crafting and invalid/unaﬀordable actions do not consume it. Reaching the threshold on an attack arms the following eligible attack, not the one that earned the final point. If the empowered action itself causes a reaction, consume the old charge first and then award that action's new point.

Twenty reactions is a long buildup: solo play using a setup hit and finisher generally requires at least forty landed actions. With equal-damage actions, a single +50% attack spread over forty hits is only about a 1.25% average damage increase before other effects. The number is a large moment, not necessarily a large overall damage buff. Keep 1.5× as the initial target and test pacing rather than lowering it reflexively.

Resonance persists between battles, has no passive/day/rest refill and gains nothing from trivial demonstrations, empty air, cooperative practice targets or repeated effects after a fight has ended. Already earned charge may be used by a normal single-element damaging technique. We should discuss a non-reaction earning route later if mono-element characters need independent access.

Future tuning pipeline:

```text
baseThreshold = 20
effectiveThreshold = max(proposedFloor10,
                         baseThreshold - verifiedEquippedReductions)
charge = clamp(earnedCharge, 0, effectiveThreshold)
ready = charge >= effectiveThreshold
```

Potential future examples: a **Conductor's Ring** lowers the requirement by 2; a rarer **Harmonic Focus** lowers it by 4. These are examples only, not new items. Resource bonuses exist in the supplied equipment format, so native maximum reductions are a candidate for implementation, but their equipped-only application and effect on current charge need testing. Do not assume an arbitrary storage field can read an equipped modifier.

Changing gear never creates charge, refunds a spent burst or fills an empty meter. Existing earned charge can meet a newly lowered threshold; that is the equipment's intended benefit. Clamp excess charge, recalculate readiness and do not lock in a free permanent readiness state after unequipping the item. Start with the strongest reduction rather than additive stacking if necessary.

The resource should have zero recharge, zero rest multiplier and zero level gain. Test native level-up refill behavior anyway: zero level gain is not proof that a custom resource cannot be filled by a level-up. If needed, keep one authoritative earned-charge counter and mirror it to the visible resource; do not allow two independent sources of charge.

## 4. Conceptual controller pseudocode

This is system pseudocode, not supported Voyage JavaScript. The italicized design requirement is the critical bridge: *obtain a confirmed resolved hit with the correct actor, target and actual primary element*. The public contract inspected does not expose that general callback.

```text
BEGIN COMPLETED PARTY TURN t
    expire imprints whose expiryTurn < t
    snapshot which actors were Resonant before these actions

    FOR each confirmed resolved action, in actual resolution order:
        if its stable resolution key was processed: continue
        if attacker, target, contact or damage channel is ambiguous: defer
        if miss, harmless display, immunity or invalid target: continue

        bonus = 0
        if actor was already Resonant AND its burst is not spent
           AND this is an eligible technique:
            bonus += 50%
            consume that actor's existing charge once for this action
            mark that actor's previously ready burst as spent

        prior = imprint[exactTargetID]
        reaction = lookup(prior.element, thisHit.actualChannel)
        if prior is live AND from another action AND reaction exists
           AND target has not reacted this turn:
            remove prior
            apply one reaction's bonus OR one short movement hindrance
            award finisher +1 charge, at most once this party turn
            record target's reaction this turn
        else if this hit has an eligible elemental channel:
            imprint[exactTargetID] = {element, expiryTurn: t + 1,
                                      sourceAction, combatID}

        deliver combined bonus exactly once through verified combat path
        record this action as processed

    clamp charge, recalculate readiness, synchronize visible meter
    clear abandoned/dead targets and imprints when combat ends
END
```

Do not infer the recipient from the nearest name in action prose. Do not apply an effect to every scene NPC because a query says one NPC was struck. Party storage does not make player counters party-owned. Stable multiplayer actor and target identity must be verified; names/traits alone can be ambiguous.

For a reaction combined with a Resonant hit, propose additive custom bonuses: ordinary 100% + reaction 25% + Resonance 50% = **175%**, not recursively multiplied bonuses. This caps only the new custom layer and does not rewrite the engine's separate success, resistance, equipment or injury calculations.

### What we can promise before a prototype

Custom resource definitions, explicit tick counters and typed health/resource changes are available building blocks. Correct identification and ordering of arbitrary hits, temporary NPC penalties, and exact multiplication of an already resolved attack have not been proven. Native action-info impact instructions are a sensible hybrid prototype, but their compliance must be observed in game; do not advertise guaranteed 1.5× from prose alone.

Start with a one-target, two-element prototype. If it cannot reliably distinguish two enemies, the attacking caster and the real hit in multiplayer, stop there and choose a smaller scope. Do not compensate with a trigger for every spell, every NPC and every pair. If exact damage multiplication cannot be supported, offer an openly specified, separately tested fixed burst or an AI-guided impact bonus as alternatives; never silently subtract guessed extra Health from total Health loss, since healing, simultaneous attacks, fall damage and resistance can contaminate that calculation.

## 5. Success-level presentation proposals

These labels apply to cooking, conversation and exploration too. A clearly readable global ladder is preferable to calling an ordinary success a divine awakening.

| Current tier | Recommended clear adventure scheme | More stylized alternative |
| --- | --- | --- |
| Critical Failure | Disaster | Calamity |
| Failure | Setback | Faltered |
| Mixed Results | Mixed Outcome | Uneven |
| Basic Success | Success | Accomplished |
| Success | Strong Success | Impressive |
| Great Success | Outstanding Success | Brilliant |
| Critical Success | Triumph | Masterful |

Keep the present score bands and `firstSuccessfulTierId` unless changing balance is separately approved. Preserve tier IDs and migrate all references to renamed display names: [Success Levels](https://wiki.unofficial.voyage/mechanics/successLevelSettings) documents that `action-success-level` matches the **name**, not the ID. That includes the five existing conditions, relevant AI guidance and fixture labels. Renaming the display alone can break the fishing and scroll success checks.

## 6. Gate before full implementation

1. Validate presentation and the resource shape against the current official draft validator; this has not been done for a candidate yet.
2. In live play, verify hit/element/target ownership, no reaction on miss/immunity, expiry after the next turn and exactly one consumed imprint.
3. Verify enemy-to-player, player-to-NPC and multiplayer ally-primed reactions; never leak one player's charge to everyone.
4. Verify one mixed attack cannot self-react, bonus damage cannot recurse and area/multihit actions do not multiply charge.
5. Verify the meter starts empty, rests/day changes/level-ups cannot fill it for free, threshold changes preserve only earned charge and the twentieth reaction boosts the following action.
6. Verify damage receives each bonus once with the actual native result. Respect nonlethal duels, surrender, death and existing immunity rules. Do not alter the Spider Realm's authored content or fixed surprise event.
7. Test all renamed success tiers, including existing fishing/scroll checks. No level, XP or success-threshold rebalance is bundled by default.

The first implementation decision is the verified hit/target/bonus delivery bridge. The reaction table and 20-charge design can be kept while adapting that bridge to what Voyage actually supports.
