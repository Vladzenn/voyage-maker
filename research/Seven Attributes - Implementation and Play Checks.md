# Seven attributes: implementation and play checks

Implemented 2026-10-27 from the user's approved system. Current full export: `world-draft/GlowhavenAlpha3 - Seven Attributes.json`; canonical copy: `world-draft/WorldAlpha - World.json`.

## Sources and boundaries

- **User-approved design:** physical Force/Finesse/Endurance alongside Logic/Passion/Empathy/Intuition, with the user's exact 18-school grouping. This supersedes the earlier proposed assignment of Water, Earth and Sound.
- **Observed reference pattern:** `sources/ChikaraOld.json` separates power approaches and physical fighting approaches, with primary-skill routing in action instructions. Its large bonus-stacking and automatic highest-attribute routing were not copied. Observing those prompts is not a playtest of them.
- **Community beta reference:** [Attributes](https://wiki.unofficial.voyage/mechanics/attributeSettings) supports custom attribute names and skill/resource references. New names use lowercase identifiers consistently. The seven-stat model is an authoring choice, not a built-in Voyage class system.
- **Community beta reference:** [Skills](https://wiki.unofficial.voyage/mechanics/skills) gives each skill one linked attribute. Physical styles and offensive schools use the documented combat type. No invented combined-attribute, weapon-attribute or support-skill formula was added.
- **Community beta reference:** [Traits](https://wiki.unofficial.voyage/mechanics/traits) supplies native attribute/skill modifiers and starting items. All required arrays are present; advanced abilities are not granted through trait lists, which could bypass their requirements.
- **Community beta reference:** [Trait Categories](https://wiki.unofficial.voyage/mechanics/traitCategories) supports maximum selection counts and earlier-category gates. The secondary exclusion refers to the primary choice in the earlier category. Minimum required selections are not represented as unsupported fields.
- **Community beta reference:** [Abilities](https://wiki.unofficial.voyage/mechanics/abilities) supports skill prerequisites, a check bonus and cooldown. Mixed prerequisites are AND, not OR. Described MP costs and effects remain interpreted prose alongside existing resource settings.
- **Community beta reference:** [Action Info](https://wiki.unofficial.voyage/ai/generateActionInfo) is the task that interprets possibility, skill choice and contextual difficulty. This is where the combined-action routing guidance is placed.

The reference wiki is independent and tracks a beta build. These field-level checks do not substitute for the actual Voyage Studio validator or a playtest on the user's release channel.

## Implementation choices

Base 10 avoids treating every unspecialized aptitude as weak. Primary +4 and a different secondary +2 give an inspectable 14/12/10 profile. These are initial balancing choices, with the existing cap of 16 retained. There is no new attribute-derived HP, MP, global damage or passive reduction bonus. A character can specialize in two magical approaches, a magical and physical pair, or two physical capabilities without an exclusive class gate.

One or two studies grant actual school skills at level 3; they do not set natural affinity. Practical training grants a physical style at level 3 or analysis practice. Gear is a separate choice to avoid handing every martial caster a sword. Item grants are native starting items, with no invented bonus mechanics.

Mixed physical delivery selects one primary skill. Relevant school training constrains the infusion's scope; physical skill alone cannot provide advanced magical power. Detached and remotely controlled effects use their school. The AI must not add a support-skill total, demand two successful rolls for one attack, or create a second attack from an infusion. Actual outputs are authoritative.

All ten techniques require skill level 5 and add +3 when actually used. Six require both physical and magical study; four demonstrate the magical approaches without a physical requirement. No technique is an automatic starting grant. The small catalogue is not intended as an exhaustive spell list: ordinary studied effects remain possible through skills and the normal action system.

NPCs retain their existing cards and actual abilities. New approach labels are not new NPC JSON score fields, moral classifications, affinity changes, or personality rewrites.

## Local checks performed

The authoring validator checks exact school mapping, the seven linked-attribute identifiers, category order, 42 valid distinct aptitude pairings, trait arithmetic and item grants in six sample builds, technique AND gates and starting-level nonqualification, media preservation, and the unchanged world graph and existing content.

These fixtures model documented configuration arithmetic; they do not execute Voyage's runtime, its AI or its validator. Full results are in `world-draft/authoring/seven-attributes-2026-10-27/validation.json`.

## Focused live checks

1. Create Force/Passion with Fire Studies, Force Training and Handwrap Kit. Confirm 14/12/10 attributes, Fire Magic 3, Force Combat 3, and exactly one pair of handwraps.
2. Select Finesse as primary. Confirm Secondary Finesse is excluded, but all four magical secondary choices remain available.
3. Create Finesse/Intuition with Ice Studies and a blade or staff. Confirm weapon choice does not override the selected technique's physical skill.
4. Create Logic/Empathy with Arcane and Healing Studies and Scholarly Practice. Confirm no martial skill, compulsory sword, or extra HP/MP attribute tax appears.
5. Cast Water and Sound as ordinary spells. Confirm Passion and Intuition respectively, including when the character is calm or unsociable.
6. Attempt a learned small fire infusion on a punch. Confirm one Force Combat resolution, one actual MP charge and one hit result. An unlearned large fire effect must not bypass study merely because the character punches.
7. Launch a detached fire arc with a sword. Confirm Fire Magic rather than Force/Finesse; then use a physical charged thrust and confirm the actual delivery skill.
8. Train one mixed technique's two requirements to 5 separately. Confirm the technique is eligible only when both qualify and that eligibility does not silently grant ownership.
9. Use a guarded action. Confirm no automatic hit cancellation, passive immunity or free counterattack. Use a fast action and confirm no extra turn appears.
10. Skip an optional creation category. Confirm it remains unselected, with no invented item, school, affiliation or aptitude supplied in the opening.
11. Revisit an existing NPC, quest and prison crossing. Confirm portraits, roster identity, local role, custody and map layout are unchanged.

Use a new game for these checks. No existing-save migration was implemented or claimed.
