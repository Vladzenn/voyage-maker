> Historical snapshot: this document predates Alpha28. For the current import use `world-draft/WorldAlpha - World.json` or `GlowhavenAlpha28 - Milestone Traits and Equipment.json`; consult Alpha28 patch notes before following older configuration instructions.

# Development and Validation Checklist

This checklist now applies to the first-pass world draft. The source atlas, outline, and local JSON exist; the community V37 validator reports zero errors and warnings. The draft has not been imported into Voyage Studio or gameplay-tested.

## Current foundation

- [x] Keep all supplied JSON under `sources/` read-only; keep the active draft separate in `world-draft/`.
- [x] Record the six-source inventory and comparative atlas.
- [x] Record established canon, proposed student-life loop, draft assumptions, and open questions in [World Outline](World%20Outline.md).
- [x] Save an untouched community V37 seed separately from the editable JSON.
- [x] Run the public community V37 validator after correcting its reported errors; latest result: 0 errors, 0 warnings, 19 recommendations.
- [ ] Import the JSON into a separate Voyage world and record Studio validation. The user approved this, but the available logged-in Studio tab currently has an unrelated map-import workflow open; it was left unchanged.
- [ ] Playtest all four story starts, one class/social scene, and one magical challenge.

## A. Before extending the draft

- [x] Keep `sources/` read-only and keep the active draft in a separate folder/export.
- [ ] Record the active Voyage environment (Alpha/Beta/production), Studio build, and date.
- [x] Preserve the untouched community V37 seed and the editable draft separately. This seed is not a Studio export.
- [x] Compare the relevant source-export structures and community V37 guidance; record layout differences rather than copying old root structures.
- [ ] Confirm current field names, allowed values, reference rules, and size caps from Studio plus the current Wiki.
- [ ] Preserve `C:\Users\VladCodes\Downloads\VoyageWorldWIP\Map\Final2_upscaled.png` as the frozen Version 1 visual reference. Do not redesign, recolor, recompose, or replace it unless asked.
- [ ] Start a change log and unresolved-reference list.

The first-pass draft intentionally leaves character mechanics, quests, narrative events, and triggers empty. Complete those parts only after the outline and intended play loop call for them.

## B. Design brief and system contract

- [ ] State the intended player experience, world scope, opening loop, content boundaries, and success criteria.
- [ ] Separate setting facts, narrator guidance, and exact mechanical rules.
- [ ] Identify each resource/attribute and define its starting value, maximum, change sources, and narrative meaning.
- [ ] Identify the skill list, linked attributes, skill types, and action categories.
- [ ] Define the progression cadence for XP, levels, skill improvement, abilities, attributes, traits, and item rewards.
- [ ] Decide which build choices use traits and categories, and which abilities are granted versus learned.
- [ ] Write down keys and cross-section dependencies before adding a large catalog.

## C. Data integrity checks

### Geography

- [ ] Every region has a valid realm, unless realm omission is intentional and supported.
- [ ] Every location has a valid region and valid `complexityType`/`detailType` values.
- [ ] Every area uses the current required fields and has at least one intentional path when it should be traversable.
- [ ] Every path resolves to the intended destination area under the current Studio schema.
- [ ] Coordinates and radius fit the chosen world/map scale.
- [ ] All location and area names match the frozen map index; visual labels and JSON identifiers are tracked separately.
- [ ] Every `factions` value used on a region/location resolves to a defined faction key.

### Character creation and mechanics

- [ ] Every trait category member and subcategory member resolves to a defined trait.
- [ ] Every trait attribute/resource/skill/item/ability reference resolves to a supported entry.
- [ ] `unlockedBy`/`excludedBy` choices are in earlier categories where required; same-category conflicts use selection limits.
- [ ] Trait abilities do not accidentally bypass ability requirements.
- [ ] Every skill uses a current attribute name and a skill type with intended difficulty/damage behavior.
- [ ] Ability requirements use current skill/trait/resource/attribute keys and tested thresholds.
- [ ] Resource modifiers and starting items have the intended effects at creation and on level-up.
- [ ] Progression pools and level-up rewards contain valid traits and do not offer duplicates or mutually exclusive picks.

### NPCs, factions, items, and voices

- [ ] Every NPC key/name follows current equality rules and remains unique for the intended identity.
- [ ] Every NPC `type`, faction, current location, current area, world voice, and playable ability reference uses the correct current key semantics.
- [ ] NPC placement is consistent with area descriptions and each story start's opening scene.
- [ ] `initialKnown`/visibility matches the discovery plan.
- [ ] NPC prose separates `basicInfo`, `hiddenInfo`, behavioral personality, and narrative capability descriptions as intended.
- [ ] NPC and NPC-type combat settings are deliberate; do not apply per-NPC overrides to the whole cast accidentally.
- [ ] Every item grant/removal uses a valid `itemTypes` key and quantity.
- [ ] Every nonempty voice reference resolves to the current catalog or a defined world voice.

### Story starts, quests, events, and triggers

- [ ] Every story start has a valid location list; each area pairs by the current rule with its location.
- [ ] Every starting NPC, item, and quest resolves to the intended record.
- [ ] Each authored quest has a defined access path: starting quest, trigger initialization/acceptance, or another validated current mechanism.
- [ ] Quest locations use valid location keys; objectives and active objective IDs resolve.
- [ ] Each trigger key/name, conditions, operators, values, effects, and targets match the current schema.
- [ ] Every quest/event/location/NPC/trait/resource in trigger conditions/effects resolves.
- [ ] `recurring`, scope, phase, and one-time behavior are intentional; repeated systems are tested more than once.
- [ ] Semantic story/action conditions are specific and placed behind appropriate structural gates.
- [ ] Script storage keys, expected data types, conditions, and effects are documented; scripts stay within current budgets.
- [ ] Each narrative event has a clear start, beat sequence, completion behavior, and next-step handoff.

### AI instructions and size limits

- [ ] Each custom instruction belongs to the generation task that owns the behavior.
- [ ] World overview contains concise always-relevant facts; detailed background belongs in lore.
- [ ] Prompt additions do not contradict built-in rules, each other, traits, mechanics, or authored records.
- [ ] Exact state changes are implemented in structured mechanics rather than left to narrator compliance.
- [ ] Every task/section/record stays below the target Studio's current character and count caps, with room for later edits.
- [ ] Current validator warnings for unsupported/legacy fields are resolved or explicitly accepted with a documented reason.

## D. Minimum playtest suite

For each significant batch, record release channel, starting conditions, action sequence, expected behavior, observed behavior, and result.

- [ ] Start a fresh game from Phoenix, Hydra, Dragon, and Pegasus story starts; inspect school, location, area, opening cast, items, quests, and first-turn narration.
- [ ] Create characters that exercise each trait category and at least one unlock/exclusion boundary.
- [ ] Change an earlier trait or story start and check that later trait options update correctly.
- [ ] Attempt one trained and one untrained skill action, including a combat action if the world uses combat.
- [ ] Exercise an ability at its requirement boundary and verify its cooldown/effects.
- [ ] Gain a level and check resource scaling, points, trait choices, and item/ability awards.
- [ ] Enter a location, use each intended area path, move between locations, and verify the map/player location updates.
- [ ] Talk to an authored NPC, leave and return, and verify identity, location, relationship, knowledge, and memory consistency.
- [ ] Start a quest through its intended hook; complete each objective; test completion, next-step updates, and follow-up quests/events.
- [ ] Trigger each non-recurring event twice to confirm it does not repeat; trigger recurring systems three cycles to confirm they do repeat.
- [ ] Test NPC combat targeting and a target first introduced in story.
- [ ] Cause one failed turn and retry; confirm no stale story, action result, or trigger effect leaks from the failed attempt.
- [ ] Test empty/optional AI outputs and story pacing in a calm scene so the AI does not invent mandatory escalation.
- [ ] Inspect errors, warnings, script logs, and semantic trigger behavior; label anything not tested as unverified.

## E. Release/readiness gate

- [ ] Current Studio validation has no unexplained errors.
- [ ] Warnings are resolved or logged with a reason and expected consequence.
- [ ] Critical paths pass the minimum playtest suite in the target release channel.
- [ ] The draft and last-known-good export are saved separately.
- [ ] Change log records schema/build, scope, results, known limits, and rollback point.
- [ ] The map image remains the frozen Version 1 asset unless the user explicitly authorized a redesign.
- [ ] No publishing or setting/cast expansion occurs before the user authorizes those stages.

## F. Current reference risks to address before using examples as templates

- [ ] Distinguish the Studio-authored world-file format from community runtime-state exports. The current community V37 validator expects party-state sections under `parties[""]`, but a Studio import in this project showed an empty Quests editor and missing party fields with that layout. Use the target Studio's own export/import view as the final authority, and record which representation was validated.
- [ ] Resolve DnD's faction, trait-category, story-start-area, and area-path mismatches before reusing its map mechanics.
- [ ] Resolve ChikaraOld's missing NPC types, quest locations, and quest activation gaps before reusing those records.
- [ ] Audit Larion's 153 quests and Luxcellia's 59 quests without an obvious static activation path; inspect scripts for dynamic wiring.
- [ ] Review Konosuba AI task caps and Luxcellia section/prompt limits in current Studio before adapting their scale.

See [Voyage Technical Guide](Voyage%20Technical%20Guide.md) for the sources behind current schema limits, official release fixes, and the distinction between deterministic triggers and probabilistic AI guidance.
