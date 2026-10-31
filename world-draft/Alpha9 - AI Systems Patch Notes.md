# Alpha 9 — AI Systems

Built on the author's latest **The Schools of Magic, Arise - Alpha.json**, supplied on 2026-10-28. The updated Luxcellia export and supplied creator patch notes are references. This release changes generation behavior and repairs a portal reference; it does not expand the map or roster.

## Complete file

Import **GlowhavenAlpha9 - AI Systems.json** as the complete world. **WorldAlpha - World.json** is its identical working copy. Importing the AI-only section would omit the portal repair, the four contextual reminders and the generation scaffolds.

The supplied export takes precedence over the previous Alpha 8 working copy. All **152 locations, 601 areas, 130 NPC records, 23 factions, 64 NPC types, five realms and five regions** are retained. Every location coordinate, area path, portrait, map image, crop and roster ordering matches the supplied export. All **299 media URL fields, including 292 nonempty URLs**, are preserved. Your newly arranged Drakenspire markers remain in place; the old temporary grid has not been reapplied.

## What changed

### Travel follows the actual address

The action-reading task now checks present movement intent and resolves local references before looking for a distant place. Narration and memory carry the same distinction between current position, a chosen destination, a view through a portal, and an appointment elsewhere.

An unmistakable adjacent doorway still works with natural language. A question, quotation, chase or incidental scenery noun does not select a remote map destination. Authored forced transfers, including the one-time portal anomaly and actual custody, keep their resolved effects. These are prompt safeguards; they cannot disable Voyage's independent location matching.

The supplied export renamed the arrival location to **Drakenspire Portals**. Its command router still used the old parent name, and the alternate outbound trigger revealed the wrong entity. Both references are repaired. The area remains **Drakenspire - Portal Room**: its existing key, paths and placement are preserved.

### Dialogue keeps a distinct person and finishes the exchange

Direct chat uses the selected NPC's actual voice, education, mood and knowledge. Replies can be warm, dry, vain, hostile, foolish or unhelpful according to the person. Answers have a plain meaning; a refusal can be final without becoming a new riddle or compulsory errand.

Repeated meal, rest, lesson and healer advice is discouraged after the player has already answered it. A genuine new danger can still justify intervention. Settled permissions and met conditions remain settled. A character does not need to repeat a catchphrase, ask a question, flirt or perform a gesture in every reply.

Chat summaries retain what was disclosed, what was promised and what actually happened. A private conversation does not move the party, transfer an item, recruit someone or broadcast a secret to everyone else.

### Combat attempts have the right recipients

The action and NPC-intent tasks identify actor, side, target and beneficiary before constructing an effect. An ally guarding someone benefits the protected ally; a taunt pressures the enemy. Attacking a lock or training dummy targets that object rather than the nearby instructor. Damage follows the actual mechanism, within this world's existing damage types.

Controlled friendly practice remains distinct from a hostile fight. Safe sparring can still have technique, skill checks, scoring and a loser. It does not acquire lethal intent just because a participant is powerful or fails. Real hostile actions and authoritative damage results still count. In a real fight, retreat and surrender are concrete attempts with counterplay rather than endless dialogue about leaving.

### Practice and learning stay useful without flooding ability cards

Meaningful practice can name the actual unowned skill; the classifier need not substitute an unrelated owned skill. This is eligibility guidance, not a guaranteed skill or XP grant.

Ordinary use of a school or an existing technique normally creates no new ability. New cards need an earned, reproducible distinction. The generator must check existing abilities, costs, cooldowns, requirements and this world's scale. It cannot award points, add affinities or spend learning resources merely to make a scene satisfying.

The prompts also reject invented hunger, sleep-debt, stamina and low-MP numeric penalties. Actual configured resource rules, real injuries and supported effects still apply. High mastery does not itself make the same task harder.

### Crafting and ownership resist runaway rewards

Generated items use the configured categories: **Currency, Armor, Weapon, Tool, Consumable, Key and Document**. The guidance follows the actual armor slots and existing equipment bonus limits, without importing Luxcellia's rarity or inventory scheme.

A self-made tool, station or blueprint cannot recursively justify ever-larger bonuses. A critical improves a feasible result; it does not create limitless quality. Upgrades replace the changed property rather than stacking duplicate versions.

Quotes, loans, customer property, custody deposits and completed purchases stay distinct. A successful finite repair can finish. A settled debt, collected payment or emptied container does not regenerate on the next visit.

### NPC identity and ordinary life persist

New-NPC generation checks authored and previously generated people before making someone else. An unknown journal entry, nickname, changed outfit or recalled familiar is not a new person. Unique offices and sacred creatures do not become random service staff because their type appears in the catalogue.

Existing NPC levels, health controls and biographies remain stable. Location generation bands do not rescale a visiting veteran or student. The current form and species determine anatomy. Dragonkin retain their established human faces, horns, side scales, slit pupils, scaly outer arms/hands, human palms and thick tails, without default wings or muzzles.

One findable habit or off-duty haunt can make a generated recurring person easier to revisit. It is not an automatic timetable or permission to move every record each turn. A summoned individual is not automatically a permanent party recruit.

### Memory closes accounts and preserves causes

The memory task keeps a compact opening anchor, canonical identities, current address, actual travel, witnessed knowledge, relevant commitments and unresolved objectives. It distinguishes a plan from a completed act and a rumor from an established fact.

Completed work and paid obligations close. Real elapsed spans are counted once. An NPC naming tomorrow's appointment does not advance the day. A contradictory sentence does not override current structured state or require an invented illusion to explain it.

### Generation templates now fit this world

The supplied export still used the shipped author seeds and generic character, location, region and encounter scaffolds. Some strongly favored wounds, secrets and conflict. Those are replaced with:

- One comprehensive ensemble-character seed for consistency when the task consults author seeds.
- 18 optional character starting patterns, allowing selfishness, mediocrity, sincere kindness, eccentricity and contentment.
- 12 place patterns grounded in services, work, privacy, ordinary social life and appropriate adventure.
- Eight regional texture patterns subordinate to the existing map and national lore.
- 14 encounter ingredient groups that include quiet life, comedy, chosen relationships, craft, exploration and real danger.

These are generation prompts, not newly spawned people or map entries. Archetypes do not determine species, affinity, level, morality or romance. Teaching appointments remain independent of innate affinity. Existing authored character cards are untouched.

### Four short contextual reminders

Added planning-phase reminders for travel references, crafting, practice and controlled contests. They inspect action text with ordinary pattern matching, filter some quoted/question-only inputs and deduplicate within a tick. They make no semantic AI calls.

They inject private story guidance only. They do not move anyone, apply damage, grant items or skills, advance time, create quests or make sparring mechanically invulnerable. A reminder can miss unusual phrasing or match an irrelevant word; the general task instructions remain the fallback. Their benefit to live narration still needs testing.

### Images describe the actual instance

The area image brief now gives an unambiguous interior description for receiving portal rooms. The previous brief carried conflicting old outdoor and newer interior instructions. NPC image guidance checks the actual body, form, colors and equipment. These changes affect future generation; existing pictures and crops are intact.

## Deliberately retained

The stable overview, quest-design brief, narrator style, character creation, name filters, game modes, species lore, factions, story starts, item catalogue, progression, attributes, skills and HP/MP settings remain as supplied. No new currency, romance meter, rarity system, clock, free teleport ability or summon-recruitment mechanic is added.

The level-20+ anomaly still interrupts one eligible ordinary outbound crossing, without requiring the briefing. The first arrival's key and immediate return remain available. The field-test postponement and separate expedition quest remain separate. Apart from the Drakenspire rename repair and four reminders, existing triggers are unchanged.

## Verification and limits

**5,125 local structural, reference, size and preservation checks passed. All 115 script/fixture checks passed.** The same older 92-fixture set failed five travel scenarios against the supplied baseline; the renamed-parent repair resolves those failures.

The fixtures run configured JavaScript with simulated conditions/effects. Semantic decisions are supplied. The NPC clamp and health tests model documented behavior rather than generating live NPCs. These checks do not establish live narration quality, balance, import acceptance or reliable engine name matching. No live Voyage game, Studio validator or comparison model was run.

The AI totals 285,623 characters of compact task objects, compared with 267,241 before and 308,814 in the supplied reference. Length is an audit measure, not a quality score. All revised tasks and image briefs fit the published bounds documented by the [community size reference](https://wiki.unofficial.voyage/appendix/size-limits), including encoded leaf and whole-task measurements.

Use a fresh test game after importing. This file does not migrate an existing save's world snapshot. The accompanying comparison and playtest documents identify what was adopted, what was already present and which effects remain unproven.
