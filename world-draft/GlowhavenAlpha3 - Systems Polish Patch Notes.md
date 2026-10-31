# Glowhaven Alpha3: systems polish

The complete export is **GlowhavenAlpha3 - Polished.json**. The active **WorldAlpha - World.json** contains the same world. This pass continues the corrected Alpha3 prison-realm version.

## 1. AI

Reviewed all 17 existing AI tasks and the five image-prompt settings shown under AI. Tasks now agree on the setting's identity, adult school cast, full canonical names, limited knowledge, actual professional roles, and the difference between meeting someone and recruiting them.

Replaced conflicting defaults in NPC Details. They previously prohibited names in descriptions, prohibited quirks, restricted public information to exterior appearance, and prescribed a different hidden-info structure. The replacement follows the established Character Creation Format: public role and equipment, the existing profile facts, six hidden-info labels, behavioral personality cues, and actual magical competence. It preserves authored cards rather than rewriting the cast.

Action guidance now distinguishes theory, casting, equipment work, physical attacks, and support skills. Chat, summaries, encounter generation, new people, NPC updates, and learned abilities have separate responsibilities. The existing combat-only NPC intent protocol remains intact.

Item instructions agree with the actual consumables. Prison guidance, knowledge limits, property ownership, accepted work, and one-time quest payments remain in place. Image-prompt settings are fallback art direction only; no images were generated or changed.

## 2. Narrator style

Expanded the warm fantasy-anime voice: vivid everyday magic, clear action, expressive individual dialogue, ordinary pleasures, comedic clashes, and sincere consequences. Third-person present tense remains the shared default.

Comedy comes from people pursuing incompatible priorities, not from mandatory jokes or making every adult incompetent. Cruelty, foolishness, selfishness, laziness, prejudice, and delusions remain real character traits. Quiet moments and serious emotion can land without an immediate gag, threat, or teaser.

The narrator resolves the chosen action and gives the player room to respond. It does not invent player speech, feelings, consent, enrollment, romance, or decisions. A large cast offers options rather than a compulsory crowd or traveling party.

## 3. Name filter

Replaced the generic naming defaults with 20 actual name-replacement rules, supported by 60 candidate full names: mostly Japanese-inspired local names with French-inspired foreign alternatives. Existing NPC names are preserved. Candidate names are not newly added NPCs.

The filter contains no prose bans, blank replacements, or loops. Candidate first names were checked against the authored roster. Generation instructions require First name Last name, collision checks, and reuse of existing role-holders. The filter is one aid to consistency, not a guarantee against every possible generated duplicate.

## 4. Skills

Expanded from 8 to **46 skills**: the original eight, 18 magical disciplines, six martial skills, and fourteen additional practical skills. No starting gear is awarded for learning a skill.

| Magic discipline | Linked attribute | Mechanical type |
| --- | --- | --- |
| Arcane Magic | Intelligence | combat |
| Fire Magic | Intelligence | combat |
| Water Magic | Wisdom | combat |
| Earth Magic | Constitution | combat |
| Wind Magic | Dexterity | combat |
| Lightning Magic | Dexterity | combat |
| Ice Magic | Intelligence | combat |
| Light Magic | Wisdom | combat |
| Metal Magic | Constitution | combat |
| Nature Magic | Wisdom | combat |
| Sound Magic | Charisma | combat |
| Gravity Magic | Intelligence | combat |
| Void Magic | Intelligence | combat |
| Healing Magic | Wisdom | magic |
| Enchantment Magic | Intelligence | magic |
| Summoning Magic | Charisma | magic |
| Illusion Magic | Charisma | magic |
| Divination Magic | Wisdom | magic |

These cover every affinity explicitly listed in the 128 NPC cards. Affinity still eases learning; it does not bar other disciplines or confer mastery. Offensive disciplines use the documented combat type so attribute-based damage applies. Summoning resolves an actual summoned attack rather than adding an automatic second hit.

Martial skills cover Swordsmanship, Polearms, Flexible Weapons, Ranged Weapons, Unarmed Combat, and Shield Combat. Additional practical skills cover Defense, Stealth, Perception, Insight, Deception, Etiquette, Animal Handling, Medicine, Alchemy, Artifice, Cooking, Perfumery, Trade, and Tactics.

Spellcraft remains general analysis and theory. Artifice handles practical equipment work; Enchantment Magic changes magical properties. Skill descriptions define scope, result, and important boundaries. This prevents a diagnosis from automatically becoming a repair or a Void affinity from becoming universal erasure.

New skill invention is disabled to keep this catalogue coherent. The existing chance to learn authored skills and existing XP/progression tuning remain unchanged. Seven missing offensive-school damage labels were added; existing damage types and other combat tuning were preserved.

## 5. Resources

Only two resources exist:

| Resource | Starting pool | Maximum growth per level | Passive recovery per tick | Actual rest |
| --- | --- | --- | --- | --- |
| health / HP | 80 | +10 | +1 | Full pool |
| mana / MP | 100 | +6 | +2 | Full pool |

Existing HP key, starting pool, and growth remain compatible with current items. Exactly one resource is marked as health.

Fallback MP costs: minor cantrip **1–3**, basic spell **6**, moderate working **14**, powerful working **30**, extreme technique **55**. A specifically authored cost takes priority. Costs apply once when actually committed, including a released spell that misses. Discussing a spell or observing someone else's magic spends nothing. An unaffordable working cannot be paid for by an invented health-overdraw rule.

Clean Bandages restore **8 HP** and Standard Healing Draught restores **25 HP**, matching their existing item definitions. Resource guidance prevents double damage, double healing, duplicate passive recovery, and instant cures for aging or permanent injuries. Death, recovery, and prison custody rules were preserved.

Casting-cost and fallback-healing prose is interpreted by Voyage's AI. Passive recharge, starting pools, and growth are structured settings. These starting balance choices have not been playtested.

## 6. Factions

All **eight existing factions** now have developed public and private information and explicit public journal visibility. Public facts are synchronized into their matching World Lore entries.

- Academy descriptions identify leaders, actual activities, access, reputation, and internal tensions without sorting students by personality or element.
- The Conclave and larger Council have distinct functions. The succession remains open; Ilyra Stillglass's academy of origin stays unknown.
- The Elite Strikeforce has citywide military, sensitive-security, and diplomatic relevance. It is classified major, with separate responsibilities from ordinary police.
- The City Guard follows evidence, actual authority, trained tactics, and the existing court/custody system.

Removed production-placeholder language from these faction entries and their paired lore. No new named official, institution, exclusive academy civic monopoly, or fixed council membership was invented.

## 7. Story starts

| Order | Opening | Foreground cast |
| --- | --- | --- |
| 1 | Phoenix Wing: Arrival Court — default | Hinae Komori |
| 2 | Gryffin Tail: Arrival Steps | Chiharu Arai, Mitsuki Amano |
| 3 | Dragon Hoard: The Missing Staff | Noriaki Takatsuki, Kōsuke Shishido |
| 4 | Hydra Head: Garden Walk | Kaoruko Hanazono, Suiren Ryūgū |
| 5 | Random | Existing people at one of 18 paired public-facing areas |

Every opening uses actual locations and areas. The three new academy casts are already at their opening areas; Hinae Komori retains the existing Phoenix-only placement override. First Words remains an optional Phoenix opening quest and is not copied into other academies.

All starts have empty starting-party and starting-item lists. Scenes may include local people without recruiting them. A chosen student background can shape the welcome; visitors and other roles remain possible. The small first-connection arc's wording now fits the selected opening instead of directing every newcomer toward Phoenix Wing.

## Preservation and verification

Preserved all **128 NPCs**, their order, cards, levels, placements, and journal flags; all **267 URL fields**; all **81 locations** and their images/areas/coordinates; the **two realms** and **14 circular prison facilities**; existing items, quests, quest triggers, custody routing, game modes, attributes, progression, traits, and top-level abilities.

Local JSON, reference, field-shape, documented size-limit, opening-placement, media-preservation, and read-only source-integrity checks passed. The validation report is in `authoring/systems-polish-2026-10-27/validation.json`.

**No live Voyage Studio validation or gameplay playtest was performed.** The reference decisions, linked documentation, and focused play checks are in `research/Systems Polish - Reference Decisions 2026-10-27.md`. This pass polishes the requested systems; it does not claim that prompt wording alone guarantees the best possible play experience.
