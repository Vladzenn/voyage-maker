# Glowhaven systems polish: reference decisions

Research and edit date: 2026-10-27. The six files under `sources/` were read as examples and remain unchanged. The active baseline was `world-draft/WorldAlpha - World.json`, incorporating the corrected Alpha3 prison hierarchy.

## What the examples contributed

| Reference | Useful pattern | How Glowhaven uses it |
| --- | --- | --- |
| ChikaraOld | Routines, distinct staff, school-life activities, and relationships beyond the player | Preserve independent jobs and friendships; use ordinary activities as playable scenes; keep a large roster from becoming a compulsory party. |
| Luxcellia | Clear skill scopes, strongly characterized openings, task-specific prompts, and usable public/private faction information | Give each established magical discipline a distinct scope; introduce a small authored cast in each opening; put instructions in the task that uses them. |
| Konosuba | Comedy driven by conviction, flaws, and conflicting priorities | Let a ridiculous character remain capable and a serious character remain funny; do not turn every scene into humiliation or erase sincere stakes. |
| Larion | Plain prose and explicit resource non-triggers | State what does not spend HP/MP, distinguish old wounds from new harm, and avoid applying authoritative results twice. |
| DnD | Broad skills alongside magical schools and institutional reach | Cover ordinary investigation, craft, movement, and fighting without requiring a separate skill for every sword style. |
| Overlord | Credible differences in capability, political limits, and supported state changes | Keep staff and Archons trained and powerful without inventing invulnerability; preserve knowledge, professional duties, and actual outcomes. |

These are authoring decisions based on observed examples, not evidence that one file is universally optimal. Unique reference-world lore, named characters, factions, class systems, and power scales were not imported.

The machine-readable `world-draft/authoring/systems-polish-2026-10-27/design-manifest.json` records each reference's measured skill, faction, and opening counts. Reference counts measure scale, not quality.

## Evidence and platform behavior

**Official:** Voyage's [Closed Beta release overview](https://voyage.io/releases/closed-beta) confirms creator-authored resources, quests, triggers, flexible traits, and narrator/background guidance. It is not a complete current JSON schema.

**Community, beta-specific:** The [Unofficial Voyage Wiki](https://wiki.unofficial.voyage/) identifies itself as independent and tracks beta build 2.52.0 / V37. Field-level choices below use its current guidance together with the supplied export. They are not claims of a successful Studio import.

- [AI Instructions](https://wiki.unofficial.voyage/ai/aiInstructions): exact editable default keys replace the relevant default section; deleting them can restore defaults on load. Conflicting NPC rules were replaced directly rather than contradicted by another appended paragraph. Supported task IDs and the combat-intent output protocol were preserved.
- [Skills](https://wiki.unofficial.voyage/mechanics/skills): skills link to existing attributes and registered types. The exact `combat` type has attribute-based damage behavior; offensive magical disciplines therefore use it, while five support disciplines use `magic`. This is a deliberate difference from Luxcellia's broad use of `magic` labels.
- [Skill Settings](https://wiki.unofficial.voyage/mechanics/skillSettings): disabling new skill generation prevents invented catalogue entries while leaving the separate chance to learn authored skills intact. Those learning rates were preserved.
- [Resources](https://wiki.unofficial.voyage/mechanics/resourceSettings): `rechargeRate` is a whole-number amount per tick; `restRechargeMultiplier` is a pool fraction, with `1` meaning full recovery on rest. Usage prose provides flexible casting and injury guidance, not a deterministic spell-cost implementation.
- [Name Filter Settings](https://wiki.unofficial.voyage/other/nameFilterSettings): use actual names and nonempty replacements. No attempt was made to ban prose through this field. Candidate pools and full-name instructions supplement the filter; they do not guarantee that the model can never invent a duplicate.
- [Factions](https://wiki.unofficial.voyage/world/factions): use the existing public/private fields, valid major/minor type, and `initialKnown`. Public faction facts were synchronized into matching lore entries. A public institution does not expose its hidden information.
- [Story Starts](https://wiki.unofficial.voyage/world/storyStarts): pair actual locations and their own areas, keep optional quests appropriate to their opening, and distinguish scene cast from `startingPartyNPCs`. Empty party lists were preserved.
- [Combat Settings](https://wiki.unofficial.voyage/mechanics/combatSettings): register the remaining offensive school damage labels without changing other combat tuning or existing resistance profiles.
- [Image Prompts](https://wiki.unofficial.voyage/ai/imagePromptConfiguration): the five supported content-type fields contain fallback art direction. No image was generated, uploaded, or replaced. The project's portrait and location guides remain the detailed authoring references.

## Design decisions and limits

The skill catalogue covers all 18 affinities explicitly listed in the current NPC roster. It does not introduce a new affinity-selection trait or turn affinities into exclusive classes. A skill definition describes learned competence; it does not grant every character all 46 skills or create a player spell library. The existing empty trait and top-level ability catalogues were preserved.

Skills use six established attributes rather than sending every action through Intelligence. A primary attribute is a mechanical association, not a claim that only one personality or species can learn a discipline. Physical weapon work and a projected spell select the skill governing the main intended effect, avoiding duplicate rolls or hits for one combined description.

The resource plan is deliberately small: existing level-one HP stays at 80 with +10 maximum per level; MP starts at 100 with +6 maximum per level. Health recovers 1 per tick and mana 2; both use full recovery on actual rest. No third meter was introduced. The explicit fallback costs and healing bands are starting balance choices that require gameplay observation, not proven optimal values.

All four academy openings retain room for a student or another chosen role. They do not force affiliation. Phoenix remains the default and keeps its optional First Words quest. Other campuses do not inherit a Phoenix-specific objective. Random uses 18 explicitly paired public-facing areas; map knowledge is not treated as permission to enter a private office or bedroom.

## Verification performed

Local checks parse JSON, reject duplicate object keys, inspect documented field shapes and size limits, check catalogue coverage and references, verify opening cast placement and starting-quest wiring, preserve the NPC roster and media paths, verify unrelated sections, and compare source hashes. They also preserve the separate prison realm and its 14 circularly arranged facilities.

No live world upload, Voyage Studio validation, model-generation evaluation, or gameplay playtest was performed. Local preservation and wiring checks cannot establish how reliably the narrator follows every prose instruction.

## Focused play checks

1. Open each academy start with a student, then with a visitor background. Confirm the right small cast, the correct room, no invented history, and no automatic party members.
2. Open Random several times. Confirm the selected public-facing area rather than an arbitrary room at that location.
3. Use an ordinary weapon strike, a small spell, a missed released spell, and an unaffordable spell. Check the selected skill and that MP changes only once where appropriate.
4. Apply Clean Bandages and Standard Healing Draught. Confirm +8 and +25 HP without a second generic treatment bonus.
5. Take actual damage, then continue talking about the wound. Confirm there is no second damage charge just for mentioning it.
6. Meet a cruel, lazy, selfish, or delusional student. Confirm their authored flaw persists and private information does not become narration.
7. Visit a professional, decline a quote, and leave. Confirm no payment, ownership transfer, friendship, or recruitment is silently applied.
8. Enter Wraith Island through the existing crossing. Confirm facility routing, custody permissions, property records, and the unchanged prison map.
