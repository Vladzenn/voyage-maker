# Glowhaven: seven attributes and magical approaches

Full export: **GlowhavenAlpha3 - Seven Attributes.json**. The canonical **WorldAlpha - World.json** contains the same content. This revision follows the polished Alpha3 world and preserves its map, prison hierarchy, roster, portraits, quests, economy, and modes.

## Attributes

The six previous attributes are replaced by **Force, Finesse, Endurance, Logic, Passion, Empathy, and Intuition**. Every skill now references one of these exact attributes. There are no obsolete structured attribute references.

| Attribute | Function |
| --- | --- |
| Force | Physical power, leverage, committed blows, grappling, lifting. |
| Finesse | Coordination, precision, timing, accurate attacks, agile movement. |
| Endurance | Physical resilience, sustained exertion, braced fighting and holding position. |
| Logic | Analytical precision, structures, calculated control and investigation. |
| Passion | Expressive energy, conviction, creative release and performance. |
| Empathy | Relational attunement, living systems and conceptual balances. |
| Intuition | Instinctive timing, subconscious recognition and perception beyond deliberate reasoning. |

These are capabilities, not compulsory personality traits or moral ranks. A quiet Passion caster and a selfish Empathy caster are valid. Existing NPCs keep their actual personalities and affinities.

## Exact approved magical grouping

| Approach | Disciplines |
| --- | --- |
| Logic | Arcane, Metal, Gravity, Enchantment |
| Passion | Fire, Lightning, Earth, Wind, Water |
| Empathy | Healing, Nature, Light, Summoning |
| Intuition | Divination, Void, Illusion, Ice, Sound |

All 18 existing disciplines remain learnable. Natural affinity, learned skill, and governing attribute are distinct. Starting study is not a selection of natural affinity or academy membership.

## Combat and skills

The catalogue now contains **42 skills**. Seven older weapon/defense skills were replaced by three approaches:

- **Force Combat:** committed strikes, leverage, overpowering and grappling.
- **Finesse Combat:** timing, precise strikes, agile fighting and physical ranged aim.
- **Guarded Combat:** actual braced contact, shield work, sustained pressure and holding position.

These can describe trained weapon or unarmed methods. Carrying a weapon does not grant mastery of it, and every sword is no longer forced to use the same attribute. Athletics and acrobatics remain available for ordinary physical tasks. Other practical skills now reference the new attributes, such as Logic for analysis and Artifice, Empathy for Insight, and Intuition for Perception.

Mixed-action guidance selects **one primary check**. A physically delivered magical punch or thrust uses the relevant physical approach when landing it is decisive. It still requires actual learned magic and pays its MP. A detached fire wave, remote gravity working, or independently shaped spell uses its magical discipline even when a weapon is the focus.

The supporting school grants no automatic extra accuracy roll, skill-total bonus, hit, doubled damage or extra action. A token punch cannot reroute a large remote spell through Force. Finesse does not grant extra turns, and Endurance grants no universal passive damage reduction.

## Character creation

Five categories provide **43 traits** using supported trait fields:

| Category | Choice | Result |
| --- | --- | --- |
| Primary Aptitude | Up to one of seven | +4 to the chosen attribute; common foundational skills at level 0. |
| Secondary Aptitude | Up to one different attribute | +2 to the chosen attribute; the matching primary is excluded. |
| Starting Magical Study | Up to two disciplines | Each selected school begins at skill level 3. |
| Practical Training | One chosen option | Force, Finesse or Guarded Combat at level 3; alternatively spellcraft 2 and investigation 1. |
| Starting Equipment | One chosen option | One basic kit, or introductory Hand-Casting Practice without an extra item. |

Base attributes are **10**. Selecting primary and secondary aptitudes produces **14 / 12 / 10 / 10 / 10 / 10 / 10** before any other supported changes. The existing creation cap is 16. The obsolete fallback allocation pool is set to zero; bonuses come from actual selected traits.

Voyage categories define maximum selections, not minimums. The descriptions tell players how to choose; omitted choices are left unspecified rather than silently assigned by the narrator. No unsupported `required` or `minSelections` fields were added. A user who skips aptitude traits keeps the base values.

Equipment is independent of fighting style. Options are the existing Simple Casting Wand, a Plain Casting Staff, Student Grimoire, Practice Blade, Training Shield, Padded Handwraps, or Hand-Casting Practice. The five new item definitions grant no numerical bonuses or free mastery. A character receives only the kit actually selected; a brawler is not automatically issued a sword. Existing items and economic anchors are unchanged.

No school-allegiance, mandatory enrollment, personality, species, or natural-affinity trait was imposed. Custom background and identity remain available.

## Learnable techniques

Added ten bounded techniques with skill prerequisites, +3 check bonus, zero cooldown, and a stated 6 MP cost. They are not granted by starting traits.

| Technique | Required skills, each level 5 |
| --- | --- |
| Furnace Knuckle | Force Combat + Fire Magic |
| Gravitic Drive | Force Combat + Gravity Magic |
| Needleflash | Finesse Combat + Lightning Magic |
| Rime Feint | Finesse Combat + Ice Magic |
| Rooted Guard | Guarded Combat + Nature Magic |
| Current Brace | Guarded Combat + Water Magic |
| Arcane Stitch | Arcane Magic |
| Current Lash | Water Magic |
| Gentle Closure | Healing Magic |
| Borrowed Outline | Illusion Magic |

All listed requirements must be met. Meeting them makes the technique eligible through the existing ability system; it does not give ownership automatically or waive ability points. Starting skill level 3 does not satisfy these thresholds. Descriptions identify primary execution, scope, cost and limits. Further teaching and generated learned abilities use the same existing skill keys and requirement rules.

## HP, MP, lore and continuity

HP remains 80 initially, +10 maximum per level and +1 passive recovery per tick. MP remains 100 initially, +6 maximum per level and +2 passive recovery per tick. Rest settings and resource instructions remain unchanged. No attribute is mandatory to obtain either base pool, and no third resource was introduced.

Added one World Lore entry explaining the approaches and martial training in finished in-world prose. The user's declaration is recorded in World Lore Draft Notes. AI action interpretation, learned abilities, character backgrounds, opening guidance, narration, memory and NPC generation now recognize the system. The Character Creation Format retains its existing card structure and explains the approach mapping in guidance only; no new NPC stat-profile section was added.

## Preservation and verification

Preserved all **128 NPC cards**, their order, journal flags, levels and placements; all **267 existing URL fields**; all **81 locations**, **313 areas**, realms, prison coordinates and internal paths; all existing items, quests, triggers, story starts, modes, resource settings and progression rates.

Local checks passed for JSON, documented field shapes and size limits, attribute/skill/item references, exact mapping, category order, trait exclusions, **42 valid primary/secondary combinations**, six representative builds, all ten technique gates, and source/media preservation. The report and build fixtures are saved in `authoring/seven-attributes-2026-10-27/validation.json`.

**This is not a live Studio validation, AI-routing test or gameplay playtest.** Trait bonuses and skill links are structured configuration. Choosing the primary skill for an imaginative combined action remains AI-guided and should be checked in actual play. These values are an initial balance implementation, not a claim of proven balance. Existing saves were not migrated; the new creation flow is intended for new games.
