# Skill system comparison: Glowhaven, Chikara, Luxcellia

Reviewed 2026-10-27. This is a file-based design assessment, not a gameplay comparison. The references are the supplied `sources/ChikaraOld.json` and `sources/Luxcellia.json`, not claims about the latest published versions. Glowhaven is the current seven-attribute `world-draft/WorldAlpha - World.json`. No world content was changed for this review.

## Verdict

Glowhaven has a coherent, setting-specific foundation and a simpler creation flow. It supports credible physical/magical combinations without requiring Intelligence for every serious caster. It does not yet match the authored progression, starting techniques, or tactical specificity of the reference files. Its best current qualities are clarity and thematic fit; its weakest are progression depth, uneven rewards, and the amount left to AI interpretation.

The seven attributes do not need replacing on this evidence. The next work should finish the rewards and advancement around them, rather than adding another large catalogue of skills.

## Measured scope

| Measure | Glowhaven | ChikaraOld | Luxcellia |
| --- | ---: | ---: | ---: |
| Attributes | 7 | 6 | 6 |
| Skills | 42 | 44 | 102 |
| Creation categories | 5 | 15 | 15 |
| Total traits | 43 | 345 | 2,041 |
| Authored abilities | 10 | 411 | 1,500 |
| Level-up trait-pool entries | 0 | 102 | 83 |
| Resource definitions | 2 | 18 | 2 |

Counts indicate authoring depth and maintenance load, not quality scores. Luxcellia's 831 Appearance Builder entries account for a substantial part of its trait catalogue; cosmetic breadth should not be mistaken for combat depth. Conversely, Glowhaven's nearly equal skill count to Chikara does not imply equal campaign support.

## What holds up

**World identity.** Logic, Passion, Empathy and Intuition give the magic system vocabulary suited to Glowhaven. Force, Finesse and Endurance support physical expression without assigning every caster to a conventional intellectual archetype. The explicit separation between capability and morality preserves characters such as selfish healers and restrained expressive casters.

**Build composition.** Primary/secondary aptitudes, studies, practical training and equipment are separate choices. The native trait data makes their starting numbers inspectable. A brawler is not forced to take a sword, a dedicated caster can select two magical aptitudes, and a chosen study is not confused with a natural affinity.

**Action economy.** One primary check for an infused physical attack is a useful design rule. The current guidance avoids automatically stacking two skill totals, generating another hit, or imposing two successful accuracy checks. It preserves a distinction between a charged physical delivery and a remotely shaped spell.

**Manageable scope.** Two resources, five creation categories and a bounded skill catalogue are reasonable for this world. Chikara's many meters and Luxcellia's extensive creation options should not be copied merely because they exist.

## What Chikara does better

Chikara differentiates power definition, power approach, physical approach and combat role. Force/Finesse/Endurance variants make physical builds legible, while class and core choices provide recognizable packages.

Its Elemental Power trait immediately grants basic shaping abilities. Its Awakened, Breakthrough and Pinnacle traits occur at character levels 10, 20 and 30, and their prose changes what the character can do: greater control, area influence and a demanding large-scale release. Those stages supply something to anticipate beyond increasing the same check bonus.

The file also contains tiered techniques, defenses, tactics, upgrades and creation instructions. These are authoring patterns worth adapting to a smaller Glowhaven progression ladder.

The complexity has costs. Its Layered Moves guidance adds a support-skill modifier up to +15, increases impact and asks for multiple damage types, alongside other synergy rules. Those are prompt-authored instructions, not demonstrated deterministic mechanics. Its power skills are tagged utility even while action prose calls them fighting skills. That discrepancy merits checking against the active engine rather than assuming every reference pattern is correct.

## What Luxcellia does better

Luxcellia's character packages provide an immediate practical identity. Its Spellblade trait grants two named abilities, physical and magical skill bonuses, HP/MP modifiers and a coherent equipment kit. Its Storm Fist package similarly introduces movement and lightning-themed abilities immediately. This does not prove balance, but it gives a player explicit things to try from the beginning.

Many abilities have a clear positive function. Mana Blade changes reach for one thrust; that changes a tactical decision. Glowhaven's initial techniques often spend more wording preventing abuse than describing a distinct advantage.

Luxcellia also supplies broad skill-threshold coverage, including later thresholds up to its skill cap of 100. Glowhaven's ten techniques all unlock at skill 5. The difference is an authored long-term route, not just a larger number of spells.

Its conventional attributes still concentrate many magical schools and technical activities under Intelligence. Its large menu and overlapping bonuses can increase decision burden and balance work. It is not evidence that Glowhaven should return to the old six-stat model.

## Concrete weaknesses in Glowhaven

### 1. Advancement has not been completed around the new model

The current skill cap is 25, character cap is 100, and every authored technique requires skill 5. This can be a valid compact scale, but there are no authored intermediate or high-skill technique rungs.

`levelUpTraitPool` is empty. The every-ten-level trait-pick cadence therefore has no authored reward options. The attribute cap is still the permissive default 999. These settings were retained during implementation and should have been reconciled before describing the system as mechanically mature. Local structural checks do not establish progression quality.

The [community progression reference](https://wiki.unofficial.voyage/mechanics/progressionSettings) documents the pool as the source of level-up trait offers. The [skill reference](https://wiki.unofficial.voyage/mechanics/skills) distinguishes trainable level from the cap on an individual contribution to a check. Raising caps without deciding the reward curve would not solve the missing progression.

### 2. Technique coverage is uneven

Nine disciplines have no authored technique: **Metal, Enchantment, Earth, Wind, Light, Summoning, Divination, Void and Sound**. They remain usable through ordinary skill-based action interpretation, so they are not nonfunctional. However, their players receive less concrete guidance and fewer explicit unlocks.

No creation trait grants an ability. Starting studies give skill level 3 and every authored ability requires 5. That is an intentional small training gap, but it leaves the first ability panel empty and makes the opening experience more dependent on free-form narration than in the references.

A compact set of recognizable starting applications for each school, followed by a few genuinely new capabilities at higher levels, would be more useful than adding another dozen schools.

### 3. Attribute payoff remains uneven

| Attribute | Linked skills |
| --- | ---: |
| Force | 2 |
| Finesse | 3 |
| Endurance | 1 |
| Logic | 10 |
| Passion | 7 |
| Empathy | 10 |
| Intuition | 9 |

Counts alone do not measure power: Force Combat is broad, and a single valuable defense can justify an attribute. Nevertheless, Endurance currently has only Guarded Combat, with no attribute-derived HP or passive reduction. Its value depends heavily on whether guarded actions actually protect, contest position or help allies in play. That needs stronger authored payoff and testing.

Passion also controls five direct-damage-capable schools, while other approaches include more support disciplines. This need not be changed; the groups should earn comparable practical value through their different functions rather than equal numbers of attack spells.

### 4. The three physical approaches are not yet tactically distinct enough

They use different attributes and different descriptions, but their numerical backbone is similar. Many example techniques use the same +3 bonus, 6 MP cost and zero cooldown. Force's pressure, Finesse's timing and Guarded Combat's protection need benefits the player can recognize in actual decisions.

Possible directions are leverage and displacement for Force, useful positioning and precision for Finesse, and protecting people or holding a contested objective for Guarded Combat. These are design directions, not new mechanics already implemented. They should use supported results and tested effects without simply awarding speed builds extra attacks.

### 5. Generated and authored ability tuning differ sharply

All ten authored techniques have bonus 3 and cooldown 0. The retained generated-ability settings are bonus 10 and cooldown 20. Neither automatically dominates the other: the larger check bonus has a much longer cooldown. But this is not an intentionally documented progression ladder, and could reward improvised abilities very differently from curated ones.

The [community combat reference](https://wiki.unofficial.voyage/mechanics/combatSettings) distinguishes generated-ability defaults from the per-ability values of authored entries; it also describes the generated cooldown setting as limiting learning cadence. The [ability reference](https://wiki.unofficial.voyage/mechanics/abilities) separates exact bonus/cooldown fields from interpreted descriptive effects. These settings need a shared balance plan.

### 6. Hybrid XP and physical/magical boundaries require an actual test

An infused strike is directed through its physical skill, while an advanced technique can require both that skill and its magical study. The world does not explicitly award supporting-school XP for every such strike. It needs checking whether a player who mostly fights with infusions progresses naturally or must deliberately train the magical study separately.

The AI also decides which part of an imaginative action is primary. Instructions reject token punches used to reroute huge remote spells, but this is not a hard-coded classification rule. Chikara and Luxcellia also rely on action interpretation; extra prose does not make any of the three perfectly reliable.

### 7. Player affinity remains less explicit than player study

NPC affinity is established in the roster. Player creation currently selects studied schools, with natural affinity preserved when the player supplies it in the background. There is no explicit affinity selection category. That is a usable distinction, but the interface should communicate it or give the player a clear declaration point if affinity is expected to be central to their identity.

## Recommended order

1. Reconcile the retained progression settings, generated-ability defaults and intended level-up rewards.
2. Give every starting school a clear usable identity and at least one recognizable technique or explicit starting application.
3. Make physical approaches pay off differently, with special attention to Endurance, protection and hybrid training.
4. Add a compact beginner/intermediate/advanced/mastery ladder that fits the chosen skill cap; do not chase the reference ability counts.
5. Provide a few recommended player build recipes and explain affinity versus study.
6. Play the same small scenarios with a heavy spellblade, fast duelist, guarded protector, pure caster and support caster. Check skill routing, actual defenses, MP, XP and unlock pacing.

The strongest design move is to keep the seven-attribute identity and improve the decisions and rewards around it. No file-based comparison can certify that its balance or generated scenes outperform the two reference worlds without those tests.
