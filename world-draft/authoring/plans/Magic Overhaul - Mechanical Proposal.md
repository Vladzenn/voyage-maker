# Magic Overhaul — implementation brainstorming

Planning only, 5 November 2026. Intended release classification: **minor update**, as requested by the author. No gameplay JSON or public patch notes changed.

The supplied full Studio export is the planning reference: attachment `0e0a46a8-91ce-41db-bcf2-d041c45b9b1b`, raw SHA-256 `813f12485175d20fb4da47882bac8ffde207e7756af97360e81ef97d5434c9c3`. Relative to the current canonical world, it contains location edits at The Pearl and Thistle, Opaline Arcade, Caelrath Amphitheatre, The King's Lists and House Orselle Salon. Do not overwrite these when implementation begins. This document does not merge them or replace the canonical full world.

## Accepted direction and open recommendations

The author approved reactions on both sides of combat, a base Resonance threshold of 20, and future equipment or other bonuses that can lower the threshold. Everything numerical below is a balancing proposal, not an implemented guarantee. Enemy reactions do not automatically give every NPC a player-style Resonance meter; that remains a separate design choice. Recommend player meters first, with any special enemy burst authored and telegraphed.

Recommended scope: complete damage presentation, rename `poisoning` to `poison` with its references, add Soul as a distinct non-reacting channel, introduce one short-lived imprint per target, use one shared table of 24 reactions and add one personal Resonance meter. The author's latest request expands the former eight-channel shortlist to fair coverage of all sixteen existing nonphysical damage channels. Each gets exactly three partners: one damage-focused, one modest damage/debuff mix and one debuff/utility-focused reaction. Sixteen of the twenty-four recipes have a non-damage payoff. Explicit short-lived NPC and player debuffs, including weakened defense and outgoing damage, are part of the requested design. This replaces the earlier Fire/Water-heavy table; it does not mean every pair reacts. Do not build a different status controller for every pair or introduce all possible combinations. Keep the maximum 20% reaction damage bonus, lowering it to 10% or 0% when a concrete tactical effect carries the benefit. Every reaction also needs distinctive narration. Pairings, names and detailed numbers below remain proposals for review.

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

| Discipline or mechanism           | Registered type                         | Proposed icon |
| --------------------------------- | --------------------------------------- | ------------- |
| Fire                              | `fire`                                  | 🔥            |
| Water                             | `water`                                 | 💧            |
| Ice/cold                          | `ice`                                   | ❄️            |
| Lightning                         | `lightning`                             | ⚡            |
| Earth working                     | `earth`                                 | 🪨            |
| Wind                              | `wind`                                  | 🌪️            |
| Metal working                     | `metal`                                 | ⚙️            |
| Nature working                    | `nature`                                | 🌿            |
| Arcane force/energy               | `arcane`                                | ✨            |
| Light                             | `light`                                 | ☀️            |
| Sound                             | `sound`                                 | 🎵            |
| Gravity                           | `gravity`                               | 🪐            |
| Void                              | `void`                                  | 🕳️            |
| Established dark energy           | `dark`                                  | 🌑            |
| Actual psychic harm               | `psychic`                               | 🧠            |
| Poison                            | `poison`                                | 🧪            |
| Cutting / puncture / blunt impact | `slashing` / `piercing` / `bludgeoning` | 🗡️ / 🏹 / 🔨  |

Add `soul` with 👻 to the implementation plan, following the author's Markdown note. This would take the registered vocabulary from nineteen to twenty channels when implemented. Soul does not create or consume an imprint, trigger a reaction or earn reaction-based Resonance. Its proposed separate identity is modest penetration of ordinary worn armor, where applicable; the conditional 10% suggestion is investigated below.

Do not make every school its own damage type: healing is normally restoration, enchantment can modify an ordinary sword strike, summoning uses the creature's actual attack, and an illusion does not injure Health merely by being believed. A mundane thrown stone remains blunt impact; moving it magically does not automatically turn it into psychic damage. A flame-shaped harmless display applies no fire imprint. Fair representation here covers the sixteen registered nonphysical channels, including Arcane, Light, Dark, Psychic, Sound, Gravity, Void and Poison; it does not manufacture damaging versions of every support discipline or reopen restricted Time/Space learning.

The author explicitly excludes slashing, piercing and bludgeoning from reactions. Keep those damage types and their ordinary combat behavior, but do not let their hits create or consume an imprint, trigger a reaction or earn Resonance. The heavy-blunt Shatter proposal remains withdrawn. An actual eligible elemental component may qualify on its own; a weapon's appearance or delivery does not turn its physical damage into an element.

### Poison key migration

The author requests **`poison`**, replacing the existing registered key `poisoning`. All proposed pair keys and presentation entries use `poison` from here on. The current gameplay JSON still uses the old key because this is a Markdown-only planning revision.

At implementation, migrate the registration, presentation, exact immunity/resistance/vulnerability values, relevant generation guidance and any stored imprint/catalogue aliases together. The inspected canonical world has 26 exact `poisoning` string values (25 defense entries plus registration) and two prose fields in Venom-Hardened referring to that damage label. Recount against the actual incoming merge base. Change damage-type references, not every English use of the word poisoning, and preserve Venom-Hardened's existing protection. Do not leave both keys registered as independent damage types. Existing saves may need the old key normalized at the reaction boundary, but do not claim a new world export automatically migrates old saves. Read-only source worlds retain their historical spellings. This is a naming migration, not a nerf to any creature's defenses or a change to the protected Spider event.

### Author's notes: Soul and generated abilities

The two notes added to this Markdown are preserved here as design inputs:

> “we can do soul as a damage type, but it doesn't have elemental reactions. we can just make it ignore 10% of someone's armor if possible and appropriate”
>
> “For created abilities, the damage types auto apply, right? How does Luxcellia or Chikara handle this?”

**Soul penetration is conditional, not a verified native statistic.** Registering a damage label and emoji does not give it armor penetration. Neither the inspected ability shape nor the documented damage presentation provides a per-channel armor-penetration field. Treat the requested 10% as a proposed relative reduction of the worn-armor contribution for that hit: armor 40 would be treated as 36, not 30, and this does not mean +10% final damage. Do not change the defender's stored armor, bypass Soul immunity or penetrate all wards and resistance. Armor-free targets receive no penetration benefit. If the engine does not expose the armor contribution at the correct resolution stage, keep Soul's identity and prototype a narrowly worded action-resolution instruction; label that effect AI-guided rather than claiming exact arithmetic. Do not fake penetration with a universal extra Health subtraction or an invented `armorPenetration` field. Soul may still use an already earned Resonant burst under the ordinary eligible-technique rule; it simply cannot generate a reaction itself.

**Created spells can be interpreted as typed damage, but do not acquire a verified persistent type tag merely because they were created.** Our 868 authored abilities and both reference exports use `name`, `description`, `requirements`, `bonus` and `cooldown`; none of their ability records has a dedicated `damageType` field. A Fire Magic prerequisite is an eligibility requirement, not proof that the resulting hit was fire. The current world already tells action resolution to use the damage mechanism that actually lands.

- In the supplied `sources/Luxcellia.json`, school/weapon routing, ability descriptions and the target's type-based defenses guide the action. Its ability records do not add a hidden per-spell damage field. This is observed configuration, not proof that live classification is infallible.
- In `sources/ChikaraOld.json`, `Layered Moves` explicitly tells the AI that a layered hit carries the fighting lane's and power's damage types. `Move Synergy` explicitly includes created techniques' stated elements/states, and its created-fusion rules deliberately allow an immediate combination. These are authored AI instructions, not evidence of an automatic mechanical hit callback. Our one-action/no-self-reaction design intentionally does not import that fusion behavior.

For implementation, generation guidance should write the actual existing damage channel plainly into an offensive created ability's description, alongside its concrete effect and cost: for example, a burning projectile deals `fire`, while a hurled rock lands as `bludgeoning`. Non-damaging abilities need no invented damage type. Use the same classification guidance for authored and created abilities, then verify the actual resolved channel before priming. A stable shared catalogue may describe authored abilities, but do not add unsupported native members or a separate trigger per generated spell. Ambiguous or mixed hits must not earn guessed reactions. The community [ability reference](https://wiki.unofficial.voyage/mechanics/abilities) likewise distinguishes exact bonus/cooldown fields from AI interpretation of descriptive effects; this still does not establish script access to the resulting hit.

## 2. One imprint, then one reaction

A qualifying hit leaves one inert imprint keyed to the exact target's runtime identity. It lasts through the next completed party turn: a mark from turn 12 can react on turn 13 and is expired on turn 14. Do not use in-world hours or days for this window.

- A compatible later hit consumes the old imprint and produces one reaction. It leaves no fresh imprint.
- An incompatible elemental hit replaces the old imprint. The same element refreshes its expiry.
- A purely physical attack preserves an unexpired imprint without participating in this reaction system.
- One mixed-element hit cannot react with itself. Identify its actual primary channel; another real action is needed.
- Misses, harmless visuals and fully immune hits do not prime a target or award charge. Meaningful contact/positive damage must be established. Deliberate non-damaging primers can be designed separately later.
- Reaction bonus damage cannot prime another reaction, generate its own charge or create a free follow-up attack. No damage-over-time reaction chains in the first release.
- At most one reaction per target per party turn; at most one Resonance point per player per party turn. This prevents multihit/AoE farming. Ordinary AoE damage is unaffected.
- Natural wetness and weather can support the fiction, but should not silently create universal mechanical primers for everyone standing in rain. Environment priming is a later, explicit rule.

## Proposed launch reactions

Pairs are order-independent. Percentages are provisional bonuses to the triggering action's ordinary damage, not percentages of the victim's maximum Health. They are design targets until the delivery bridge is verified. This 24-pair revision replaces the previous nine-row shortlist, including its multi-partner Galeweave wildcard. Rimebind is retained as a defense debuff; Fire/Water Steamshock, Lightning/Metal Induction and the other unlisted old pairs are no longer extra recipes. Each channel has exactly one partner in each of the following three groups; the coverage matrix below makes that distribution reviewable.

### Damage-focused: +20%, no separate debuff

| Pair | Reaction | Narration cue |
| --- | --- | --- |
| Fire + Ice | **Thermal Shock** | Frost cracks from within and breaks into a bright rush of vapor. This is the extra hit damage, not additional armor destruction. |
| Water + Lightning | **Conduction** | Blue-white filaments race across the wet imprint and converge in one sharp discharge. No added stun or action penalty. |
| Earth + Sound | **Faultsong** | A low chord travels through a stone-colored lattice, which fractures in time with the note. No free wall demolition or armor loss. |
| Wind + Metal | **Silver Shear** | Metallic ribbons whistle along a cutting gust and flash away on impact. No bonus attack, projectile spread or automatic disarm. |
| Nature + Poison | **Bitterbloom** | A dark flower of green motes opens and collapses at the point of contact. No second poison dose or damage-over-time chain. |
| Arcane + Void | **Nullbloom** | A violet mana knot folds into a silent black center, then snaps outward once. No erasure, dispelling or deletion of possessions. |
| Light + Dark | **Eclipse** | A bright corona closes around a dark center and breaks in a single pulse. No universal blindness or removal of darkness. |
| Gravity + Psychic | **Mindfall** | A deep pressure note and a brief inward ripple strike together. No forced movement, mind control or lasting mental injury. |

### Mixed payoff: +10% and one brief, narrow debuff

| Pair | Reaction | Tactical effect and narration cue |
| --- | --- | --- |
| Fire + Lightning | **Flashburst** | A hot report and pressure pulse spoil a susceptible target's balance: proposed -3 to its next footing-dependent defense check. No automatic knockdown. |
| Water + Wind | **Sprayveil** | Sparkling spray interrupts aim: proposed -3 to the target's next visually aimed attack check. No universal blindness or penalty to attacks guided by another sense. |
| Ice + Nature | **Frostflower** | Leaf-shaped frost catches along a joint or supporting growth: proposed -3 to the next movement-dependent check. No full-turn freeze or permanent new vegetation. |
| Earth + Gravity | **Burdenfall** | A dust-ring settles heavily: proposed -5% outgoing damage on the target's next grounded physical strike. No flight cancellation, universal spell weakening or pinning. |
| Metal + Sound | **Bellshock** | A bright note vibrates an existing metal implement: proposed -5% damage on its next attack with that implement. No automatic disarm or lasting deafness. |
| Arcane + Light | **Prismwink** | A prismatic afterimage offsets contact: proposed -3 to the next visually aimed check. No invisibility or inevitable miss. |
| Dark + Poison | **Nightshade** | A numb-looking dark tracery briefly weakens a susceptible living body: proposed -5% outgoing damage on its next physical attack. No extra toxin stack or paralysis. |
| Void + Psychic | **Hollow Echo** | Uncanny silence jars an actual mind's focus: proposed -3 to its next concentration-dependent check. No spell cancellation or effect on a mindless frame. |

### Utility-focused: +0% extra damage

| Pair | Reaction | Tactical effect and narration cue |
| --- | --- | --- |
| Fire + Nature | **Cinderbloom** | A bloom of warm ash saps the next exertion: proposed -10% outgoing damage on the affected target's next physical attack where its body is susceptible. No second damage tick, forest fire or automatic exhaustion. |
| Water + Ice | **Rimebind** | Frost tugs at joints or footing: proposed -5 to the target's next movement-dependent block/evade check. This lowers relevant defense accuracy, not permanent armor or every roll. No frozen turn. |
| Earth + Metal | **Ironburr** | Grit and metallic burrs briefly foul an existing metal weapon: proposed -10% outgoing damage on its next attack. No destroyed equipment or impairment of an unrelated hand-cast spell. |
| Lightning + Arcane | **Sparkstitch** | The mana imprint crackles and sputters: proposed -10% outgoing damage on the next damaging spell. No loss of learned spells, cancelled action or increased Mana cost. |
| Wind + Poison | **Bitterwake** | A sharp draft of stinging motes spoils aim: proposed -5 to the next visually aimed attack check when the target has susceptible eyes. No free poisoning of new targets or cure of existing venom. |
| Sound + Psychic | **Echochatter** | A displaced echo troubles an actual mind: proposed -5 to the next hearing/concentration-dependent check. No forced speech, hallucinated orders or stolen action. |
| Gravity + Dark | **Nightweight** | A dark tether of apparent weight drags at a grounded target: proposed -5 to its next movement-dependent check. No guaranteed immobilization or universal flight denial. |
| Void + Light | **Afterglow** | A pale outline lingers on an already perceived target: proposed -5 to its next concealment-dependent defense or hiding check. No seeing through walls or universal invisibility detection. |

### Coverage check: three distinct partners for every channel

| Channel | +20% damage partner | +10% mixed partner | +0% utility partner |
| --- | --- | --- | --- |
| Fire | Ice | Lightning | Nature |
| Water | Lightning | Wind | Ice |
| Ice | Fire | Nature | Water |
| Lightning | Water | Fire | Arcane |
| Earth | Sound | Gravity | Metal |
| Wind | Metal | Water | Poison |
| Metal | Wind | Sound | Earth |
| Nature | Poison | Ice | Fire |
| Arcane | Void | Light | Lightning |
| Light | Dark | Arcane | Void |
| Dark | Light | Poison | Gravity |
| Psychic | Gravity | Void | Sound |
| Sound | Earth | Metal | Psychic |
| Gravity | Psychic | Earth | Dark |
| Void | Arcane | Psychic | Light |
| Poison (`poison`) | Nature | Dark | Wind |

This is equal recipe access and the same offered damage/debuff budget, not proof that all combinations are equally useful in every scene. Debuffs can depend on a real mind, sense, surface or implement. Test those frequencies before tuning; do not invent missing materials or compensate an inapplicable debuff with unlisted damage. A valid reaction still consumes the imprint and earns its ordinary single Resonance point when its debuff is inapplicable. The triggering attack retains its ordinary damage at +0%; zero extra damage is not a promise that the attack becomes harmless. All pairs use one shared lookup/controller and the same cap/expiry rules; twenty-four catalogue entries do not justify twenty-four semantic triggers. Pair keys use exact planned lowercase channels, including `poison`, after the documented migration.

The damage budget is 20% for a damage-focused reaction, roughly 10% for a small additional tactical effect, and 0% when utility is the main payoff. These are not equivalent in every fight: briefly preventing a boss's whole turn would be much stronger than 20% damage even at 0% bonus, so full-turn denial is not part of the launch proposal. Actual anatomy, footing, material, strength and established immunities limit the consequence. A poor combination can be tactically unhelpful; do not create a hedge, metal weapon or vulnerable body solely to make its utility work.

### Temporary debuffs on NPCs and players

The author explicitly requests real debuffs, not just a list of extra-damage percentages or cosmetic staggering. The table now distinguishes **defense accuracy**, **attack accuracy**, **outgoing damage**, and **movement/concentration**. A -5 defense-check modifier is not a 5% damage-reduction change; -10% outgoing damage is not +10% damage taken. Start with the modest proposed values above and verify their actual effect against Voyage's score bands before tuning.

Use one shared, target-keyed reaction-aftermath record for an NPC or player. Each debuff has one eligible-use charge and expires after that relevant resolution or at the end of the following completed party turn, whichever comes first. A defense debuff is consumed on the next qualifying defense against an incoming attack; merely having an unrelated conversation or making a spell attack does not consume it. An outgoing-damage debuff is consumed on the next resolved qualifying attack attempt, including a miss, and then clears; it is not a permanent punishment stored until a hit finally lands. Do not reduce the triggering attack retroactively. There is at most one active reaction debuff per target; a new one replaces the older entry instead of stacking penalties. No stun, skipped turn, automatic disarm or permanent stat reduction is introduced.

Conceptual record only, **not a native NPC/trait schema**:

```text
aftermath[exactEntityID] = {
    reaction, sourceActionID, affectedCheckOrDamageKind,
    penaltyOrMultiplier, remainingUses: 1, expiryPartyTurn: t + 1
}

before the next verified eligible resolution:
    apply this one contextual modifier or output multiplier once
    consume the record after that resolution
at expiry, combat end, death or departure from this combat:
    remove the record; do not edit permanent character values
```

**Verified building blocks and remaining gap:** authored NPC cards have `successBonus`, `damageModifier` and `damageReductionModifier`. The first affects rolls generally, the second outgoing damage and the third incoming damage reduction. They are not interchangeable defense statistics, and their existence does not establish a safe runtime trigger that temporarily changes just the next defense. The inspected typed NPC effects cover Health, relationship, placement, portrait and party membership, not a generic `npc-debuff` or `npc-stat` effect. Do not invent either. The community [NPC reference](https://wiki.unofficial.voyage/world/npcs) and [trigger vocabulary](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) support this distinction; a timed state record by itself does not alter combat math.

Preferred implementation is an engine-supported temporary modifier applied to the exact eligible resolution, with mechanical ownership/expiry. If that hook is not exposed, use the tracked record to supply a precise condition to action resolution, and describe it honestly as a hybrid AI-applied penalty until playtesting proves the numerical behavior. A story cue alone must not be advertised as exact -5 or -10%. Do not permanently subtract from NPC base modifiers, lower NPC levels, grant/remove training traits, mutate an entire npcType, fake defense loss by removing Health, or give a global `successBonus` penalty while calling it defense-only. A relative 10% output reduction means multiplying the qualifying outgoing result by 0.90 before the target's ordinary mitigation; it does not mean subtracting 10 points from an existing percentage modifier. Missing, immune or irrelevant targets receive no guessed modifier.

Clearly narrate which limb, aim, footing or spell flow is affected and when it recovers. Do not give the same debuff both an exact numerical penalty and an additional easier difficulty step for the same opening. The rules are symmetric: enemies can inflict these conditions on players, and player reactions affect eligible enemies, including bosses with relevant anatomy/equipment. Boss status alone does not erase every debuff, but actual immunities and impossible conditions remain. This changes no protected Spider encounter or boss definition.

### Situational advantages already exist

This update is not adding a generic advantage/disadvantage subsystem. Current Glowhaven action guidance already considers opposition, environment and preparation, and explicitly recognizes actual injury, terrain and active conditions through supported resolution. The narrator establishing a genuine condition can therefore change a subsequent action's feasibility, difficulty, context or impact. A cosmetic recoil is not automatically a persistent Off Balance status; a player's claim that an enemy is helpless is not a resolved condition.

The reference exports reinforce different approaches:

- `sources/Luxcellia.json`, `generateActionInfo` → `Difficulty, Bonuses and Impact`: circumstance changes difficulty, while numerical bonuses are restricted to actual sheet sources. Its footing/injury/preparation rules are authored instructions, not proof of a universal +5 rule.
- `sources/ChikaraOld.json`, `generateActionInfo` → `Combat Guidance`: explicitly considers situational advantages. Its `Layered Moves` block separately authors a numerical support context modifier. This is an older supplied export, not evidence of the latest live Chikara behavior.

Voyage's [ability/check reference](https://wiki.unofficial.voyage/mechanics/abilities) includes context modifiers among check contributions. The AI can judge a favorable situation; that does not guarantee the exact text `Opponent off balance +5` or any fixed number each time. The precise live UI presentation has not been tested here.

For a reaction, define the real consequence and let the existing action resolver account for it. An off-balance foe may be easier to strike or evade when balance matters; this does not improve unrelated conversation, every magical defense, or every action for the remainder of combat. Do not award another roll modifier merely because a reaction's visual description sounds impressive. Do not count the same opening twice as both a flat context bonus and an easier difficulty tier. If a later playtest justifies a standardized +5 context rule, author it explicitly then; no new universal fixed bonus is approved now.

Conditions arising from an action affect later eligible resolution. Do not retroactively change an attack whose roll already happened because the following narration used the word staggered. Existing native buffs, defenses and contextual resolution should carry as much of this as the platform supports, with custom bookkeeping reserved for imprint/aftermath expiry and Resonance ownership.

Sound, Gravity and the bounded Light/Dark interaction are now part of the equal-coverage roster above, rather than deferred privileges. The previous candidate names Fracture and Collapse are superseded by Faultsong and Burdenfall. No additional unlisted pair, physical Shatter or Soul reaction is implied.

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

This is system pseudocode, not supported Voyage JavaScript. The italicized design requirement is the critical bridge: _obtain a confirmed resolved hit with the correct actor, target and actual primary element_. The public contract inspected does not expose that general callback.

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
            apply that row's direct bonus and/or one bounded aftermath
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

For a reaction combined with a Resonant hit, propose additive custom bonuses: ordinary 100% + maximum reaction 20% + Resonance 50% = **170%**, not recursively multiplied bonuses. This caps only the new custom layer and does not rewrite the engine's separate success, resistance, equipment or injury calculations.

### What we can promise before a prototype

Custom resource definitions, explicit tick counters and typed health/resource changes are available building blocks. Correct identification and ordering of arbitrary hits, temporary NPC penalties, and exact multiplication of an already resolved attack have not been proven. Native action-info impact instructions are a sensible hybrid prototype, but their compliance must be observed in game; do not advertise guaranteed 1.5× from prose alone.

Start with a one-target, two-element prototype. If it cannot reliably distinguish two enemies, the attacking caster and the real hit in multiplayer, stop there and choose a smaller scope. Do not compensate with a trigger for every spell, every NPC and every pair. If exact damage multiplication cannot be supported, offer an openly specified, separately tested fixed burst or an AI-guided impact bonus as alternatives; never silently subtract guessed extra Health from total Health loss, since healing, simultaneous attacks, fall damage and resistance can contaminate that calculation.

## 5. Selected whimsical success-level names

The current world and the author's screenshot still use the seven default names. The author selected the following global ladder, with gently storybook language that also fits cooking, conversation, exploration and martial actions. Normalize the supplied spelling “Splended Work” to **Splendid Work**. This changes labels and narrator phrasing, not the probability or magnitude of an outcome. The selection is recorded here; it has not been applied to the world.

| Current tier | Selected display name | Same outcome meaning |
| --- | --- | --- |
| Critical Failure | **Spectacular Blunder** | A severe failure within the action's real stakes; adversary skill or bad circumstances can explain it without humiliating the character. |
| Failure | **Unfortunate Mishap** | The attempt fails; show the actual obstacle or opponent's response. |
| Mixed Results | **Imperfect Result** | Meaningful partial success with a specific limitation, compromise or cost. This remains the first successful tier. |
| Basic Success | **Little Triumph** | The intended task succeeds modestly, without an invented complication or extra prize. |
| Success | **Splendid Work** | A clean, confident success with a concrete useful result. |
| Great Success | **Stroke of Brilliance** | An especially effective execution with a benefit appropriate to the actual action and engine outcome. |
| Critical Success | **Storybook Triumph** | An exceptional result rendered memorably, within the action's scope and supplied mechanics. |

The labels do not force a comic mishap into torture, bereavement or another serious scene, nor make every brilliant action lucky or magical. Spectacular Blunder need not make the character incompetent: opposition and circumstances can defeat a capable attempt. Storybook Triumph grants no free ability, extra attack, critical multiplier, item or plot victory beyond the actual result. Preserve existing outcome semantics. Narration can be warm or vivid without announcing a chosen hero.

Implementation migration must be atomic:

1. Preserve all seven stable tier IDs and exact current score bands: critical failure at -66 or lower; failure -65 to -51; mixed -50 to -26; basic -25 to -1; success 0 to 24; great 25 to 49; critical success 50 or above. Keep `firstSuccessfulTierId: "mixed-results"`.
2. Rename the seven display names and revise their tier `prompt` strings to express the same outcomes above. Retain `{{characterName}}` where needed.
3. Migrate the five current declarative success-name conditions: three `mixed results` references become the case-normalized Imperfect Result name, and two `basic success` references become Little Triumph. Also inspect scripts, dynamic scroll templates, AI instructions, tests and other exact-name comparisons. Do not assume the five root conditions are the complete string-reference inventory.
4. Verify every score boundary and existing fishing/scroll success branch. Only then synchronize the derived section files and deliver the full JSON. No changes to XP, levels, tier thresholds or impact/damage bands belong to this cosmetic migration.

The community [Success Levels reference](https://wiki.unofficial.voyage/mechanics/successLevelSettings) documents that `action-success-level` matches the **name**, not the ID. Renaming only the visible entries can therefore break existing checks; preserving IDs alone is insufficient. No tier image generation or new emoji requirement is bundled.

## 6. Gate before full implementation

**Readiness: design-ready to begin implementation with a small prototype; not yet verified for release.** The release may be presented as a minor update. That classification does not establish that the engine exposes resolved hit types or temporary modifiers. Start by proving one target, two elements and one actual debuff, then add the shared table, both-side handling and Resonance after the result is dependable. Exact damage/temporary-penalty application and multiplayer scroll-recipient routing are the outstanding technical questions, not reasons to reopen the agreed names or expand the update into new quests, cast or maps.

Safe first-pass edits are the selected tier labels plus their dependent references, damage presentation, the atomic poison rename and the supported Soul/resource definitions. Keep unproven reaction effects out of the delivery candidate until their resolution path works. If numerical effects require an AI-guided hybrid, report that limitation and resolve it with the author rather than silently presenting them as mechanically exact. Consolidate scroll settlement through the separately documented universal path and test cross-player grants/consumption before retiring either old implementation.

1. Validate presentation and the resource shape against the current official draft validator; this has not been done for a candidate yet.
2. In live play, verify hit/element/target ownership, no reaction on miss/immunity, expiry after the next turn and exactly one consumed imprint.
3. Verify enemy-to-player, player-to-NPC and multiplayer ally-primed reactions; never leak one player's charge to everyone.
4. Verify one mixed attack cannot self-react, bonus damage cannot recurse and area/multihit actions do not multiply charge.
5. Verify the meter starts empty, rests/day changes/level-ups cannot fill it for free, threshold changes preserve only earned charge and the twentieth reaction boosts the following action.
6. Verify damage receives each bonus once with the actual native result. Respect nonlethal duels, surrender, death and existing immunity rules. Do not alter the Spider Realm's authored content or fixed surprise event.
7. Test all renamed success tiers, including existing fishing/scroll checks. No level, XP or success-threshold rebalance is bundled by default.
8. Check the full roster as data: exactly 24 unique unordered pairs, all sixteen eligible channels used exactly three times and once at each 20%/10%/0% budget. Reject Soul/physical entries and wildcard partners. Sample the practical usefulness of material/sense-dependent utility rather than equating recipe count with proven balance.
9. Verify generated abilities against their actual resolved channel, including a mundane rock moved by magic and a mixed technique. Separately verify any Soul penetration against armor 0 and a known armor contribution; do not advertise exact 10% bypass from descriptive guidance alone.
10. Verify Rimebind affects only the next relevant defense; output weakening affects only its stated attack/spell category; every debuff clears on eligible use/expiry/combat end and repeated applications never permanently lower a stat. Test NPC-to-player and player-to-NPC effects, existing NPC base modifiers, mindless/eyeless/airborne targets and nonlethal bouts. Do not call tracked narrative debuffs exact arithmetic without this resolution test.
11. Recount and migrate exact `poisoning` references to `poison`, preserving all original defenses and source files. Verify the emoji, generated/held ability guidance and reaction lookup agree on the new key; flag old-save compatibility separately.

The first implementation decision is the verified hit/target/bonus delivery bridge. The reaction table and 20-charge design can be kept while adapting that bridge to what Voyage actually supports.

## 7. Trigger architecture and current semantic budget

The author prefers a mechanical damage-driven controller followed by varied narration. That is the design goal: confirmed typed hit → exact target imprint → table lookup → supported effects/Resonance → a short narration cue. No new gameplay triggers have been implemented yet. An actual damage type is structured combat information, but the current documented trigger condition/read vocabulary inspected here does not establish that scripts can read a resolved hit's type, attacker and target. Verify that bridge before claiming an entirely mechanical implementation. Do not substitute an action-text regex that detects a spell's name for confirmation that its hit landed.

A trigger with a `story` **effect** can still be mechanical. It becomes semantic when its **conditions** contain an AI-judged `story` or `action` query. JavaScript does not make a semantic trigger mechanical: those conditions are evaluated before the script runs. A later `skip` cannot recover that semantic-check budget. Keep the arithmetic, expiry, duplicate prevention and charge bookkeeping mechanical; if hit recognition still needs semantic classification, label the result a hybrid and resolve that scope with the author before implementation.

### Inventory of the supplied export

`tools/magic-overhaul/semantic-trigger-inventory.json` records the inspection and exact input hash. There are **548 authored root triggers: 456 semantic and 92 mechanical**. Each of the 456 has one semantic condition in this export.

| Authored bank                                              | Semantic definitions |
| ---------------------------------------------------------- | -------------------: |
| Core guild, academy and legacy events (`gh`, `q20`, `q23`) |                  241 |
| Ardelis                                                    |                   52 |
| Original medicines and teaching scrolls                    |                   42 |
| Adventurers and general activities                         |                   43 |
| Crucible                                                   |                   22 |
| Akitsuhara                                                 |                   18 |
| Rebirth                                                    |                   14 |
| Glowhaven outer activities                                 |                   10 |
| Fishing                                                    |                   10 |
| Crime and introductory spellcraft                          |                    4 |
| **Total**                                                  |              **456** |

These are definitions, not 456 checks performed every turn. Their location, quest, inventory, progress and other mechanical gates usually exclude most of them. The community [trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents a 500 semantic-definition ceiling and 15 semantic checks per turn, plus 5 for each active quest. Static headroom is therefore 44 definitions before runtime registration. Generated or temporarily registered rules are not included in the 456 figure. There are also six authored arcs and 265 native quests with story-based completion conditions; these are not all simultaneously active and must not be added to the root total as if they were.

Broad eligibility deserves measurement in real session states. `gh_lore_expedition_accept` remains eligible while its quest is hidden. `cp_first_spell_offer` checks while the introductory spell quest is hidden after tick zero. Crime detection can qualify in ordinary Glowhaven scenes until its custody/pending/poster gates exclude it. Each held, mapped medicine can make its separate use check eligible; each held, unlearned original scroll can make its separate study check eligible. Live Crucible outcomes and active Rebirth chapters bring their own semantic checks when their state gates pass.

The existing synthetic scene-budget fixture covers selected inventories and scene states; it does not prove that a late-game bag of medicines, many scrolls and several active activities stays under budget. No live per-turn profile was obtained here. Do not remove unrelated quest functionality just to create room for the magic update.

### Universal scroll resolution remains an unmet requirement

The author expected one shared semantic or mechanical scroll-use/learning path. Inspection shows that this is **not what the current export fully implements**:

- The original thirty teaching scrolls still have thirty separate `item31_study_*` semantic triggers. The other twelve `item31` semantic definitions are medicine-use checks.
- The newer hundred scrolls have ten mechanical `rb_scroll_registry_*` controllers. They dynamically create per-scroll semantic study rules for focused scrolls and later delete them. Their shared registration/catalogue does not make resolution universal.

The earlier `Schools of magic, Rebirth! - Development Notes.md` explicitly recorded the old thirty-rule migration as deferred pending a live multiplayer prototype. That explains the preserved implementation; it is not evidence that the universal requirement was completed. Treat it as unfinished work rather than describing the shared template as a universal handler.

The required revision is one data-driven scroll-learning path: a catalogue supplies the scroll item, formula trait, ability, requirements and study standard; a mechanical controller tracks each player's real held item and current focus; a shared completion gate confirms the actual successful study when semantic judgment is necessary; mechanical settlement checks ownership and requirements again, grants the formula/ability once, then consumes that learner's one copy once. Prefer zero new semantic checks if a verified structured event can establish the whole transaction; otherwise prefer one shared semantic gate, rather than a separate definition per scroll.

Do not claim consolidation until it works for pronouns/continuations and for two players studying different scrolls. Native `satisfyingPlayers` targets a qualifying group; a naive shared script emitting two different formula grants can cross-grant both to both people. Correct per-player routing or an explicitly bounded settlement queue must be proven with the actual effect vocabulary. Preserve learned formulas and existing study progress during migration. Ambiguous actor/scroll identification must not consume an item or grant a guessed spell.

This section records a required follow-up design correction, not an implemented repair. The supplied world remains unchanged, including both sets of old scroll handlers, until the shared replacement is implemented and tested.
