# Reusable Voyage Worldbuilding Playbook

**State:** reference research is complete and the project is officially in Beta as of 2026-10-30. The active import target remains WorldAlpha - World.json (legacy repository filename); this beta playtest update is JSON-checked, but Voyage Studio import, platform validation, and runtime playtesting remain open.  
**Companion references:** [Reference Inventory](Reference%20Inventory.md), [Reference Atlas](Reference%20Atlas.md), [Voyage Technical Guide](Voyage%20Technical%20Guide.md), [Development and Validation Checklist](Development%20and%20Validation%20Checklist.md).

## Current writing and release guides

Use [Narrative Writing and Quest Craft Guide](Narrative%20Writing%20and%20Quest%20Craft%20Guide.md) for story starts, arcs and quest scenes; [Patch Note Creation Guide](Patch%20Note%20Creation%20Guide.md) for every release post; and [current player portrait defaults](Player%20Portrait%20Creation%20-%20Current%20Defaults.md) for character-creation portraits. These are authoring guides, not prose to duplicate into runtime records.

## Working rules

1. **Studio is the final authority for the active release channel.** Use [WorldAlpha - World.json](../world-draft/WorldAlpha%20-%20World.json), [WorldAlpha - Locations.json](../world-draft/WorldAlpha%20-%20Locations.json), and [WorldAlpha - NPCs.json](../world-draft/WorldAlpha%20-%20NPCs.json) as the current sources. Their matching sections were confirmed when received; import and runtime behavior remain unverified.
2. **Keep references and the active draft separate.** `sources/` stays read-only. The outline and research are in `research/`; drafts and their supporting cards are in `world-draft/`. Keep the original user export unchanged.
3. **Treat the Version 1 city map as frozen.** Preserve `C:\Users\VladCodes\Downloads\VoyageWorldWIP\Map\Final2_upscaled.png` and its visual composition. Later city planning may derive labels, locations, and areas from it, but no redraw or redesign is implied.
4. **Separate facts, guidance, and mechanics.** Use world overview/lore for setting facts, task-specific AI instructions for flexible interpretation, and supported structured mechanics/triggers for outcomes that must be exact.
5. **Design dependency order before content volume.** Define IDs and relationships first, then add only the content needed to exercise them.
6. **Work in small, reviewable batches.** Make one coherent change group, validate it in Studio, record warnings, then playtest its key loop before expanding.
7. **Record what is known and what is still a hypothesis.** Official patch notes, current Wiki schema, source-export patterns, and playtest observations should not be merged into one undifferentiated claim.

## Focused procedure for the first playable pass

Use this order when turning an existing world export into a small, reviewable first session. It follows the user's sequence and adds the checks needed to make each section playable.

### Step 0 — Confirm current Voyage documentation

- Read the official Voyage product guidance and the latest release notes relevant to Studio, story starts, character creation, NPCs, quests, and migration.
- Check the current Unofficial Voyage Wiki schema for the active V37 fields and limits. Label official behavior, community schema notes, observed export patterns, and hypotheses separately.
- Record the target Studio release channel/build before import. Prefer its generated JSON and validator output when available; do not assume two exports labeled V37 use identical fields.

### Step 1 — Set NPC role and level bands

- Read the approved character cards using [Character Creation Format](Character%20Creation%20Format.md); inventory Archons, headmasters, teachers, students, and any separate civic authority.
- Choose one shared level band per role before assigning individuals. Keep peers in the same band and record any unique exception separately.
- Treat numeric NPC level and combat `tier` as different controls. A low combat tier does not imply a low level, and a high office does not dictate a personality.

### Step 2 — Place NPCs and set combat tiers

- Give every authored NPC a valid `currentLocation` and `currentArea` that match the card and the location's area keys. Decide who should be physically present in the opening area.
- Set `tier` from actual combat capability and intended combat behavior, not social worth or school rank. Use a shared NPC type only for a real shared role/category; keep damage profiles aligned with the world's exact damage-type keys.
- Set location `npcLevelRange` only for party-scaled generated NPCs. Explicit named NPC levels are separate.

### Step 3 — Define factions

- Settle canonical faction keys and public descriptions before linking NPCs or locations. Use current names and canon; keep unresolved formal names visibly provisional.
- Make every NPC/location faction reference resolve. Mirror faction public information in World Lore when the current schema recommends it, and keep both copies identical.

### Step 4 — Author one playable story start

- Choose a concrete starting location and exact area, plus one immediate social or action choice for the player.
- Keep one or two relevant NPCs in that scene; avoid making every major character appear in every opening.
- If the start has an authored quest, wire its exact key into `startingQuests`, use a valid quest location/source, and give it an observable completion condition. Keep the opening flexible enough for the player to accept or refuse.

### Step 5 — Fill World Lore

- Add compact, self-contained facts for rules the narrator must remember: institutions, magic limits, succession, language, and other established canon.
- Keep names consistent and leave undecided details undecided. Put character secrets in NPC records and local place details in locations instead of duplicating them broadly.

### Step 6 — Fill the Story Overview

- Put the one-paragraph premise and current situation in the always-relevant world overview. Keep deeper facts in World Lore and the opening scene in the story start.
- Do not let the overview predetermine the player's identity, allegiance, or choices.

### Step 7 — Build the minimum useful mechanics

- Ensure the first session has a meaningful character setup, one representative skill check, and any resource or item changes it actually needs. Distinguish skills merely defined in the catalog from skills guaranteed at character creation; use supported character-creation grants if the opening depends on a particular skill.
- Start with a small skill/trait/ability surface. Do not add a large progression catalog to support a one-scene playtest. Record which rules are narrative-only and which have structured mechanics.

### Step 8 — Tune AI instructions

- Use only the task that owns the behavior: opening structure in initial start, checks in action info, NPC intent in NPC-intent guidance, and global tone in narrator style.
- Use prompts for flexible narration and structured fields/triggers for exact changes. Keep the opening's low-stakes tone, NPC individuality, level/tier separation, and player agency explicit without repeating the same rule across every task.

### Step 9 — Review Other settings

- Check only settings needed for the first session: game modes, character customization, tips, music/voices, visibility, and presentation. Confirm location images with the project's image guide before creating or replacing them.
- Leave optional catalog expansion and polish for a later pass unless a setting blocks the opening.

### Step 10 — Validate and playtest

- Run the current Studio validator after import. Resolve errors and warnings that affect the opening, record accepted warnings, and retain the community validator result separately if used.
- Start a fresh game from the default opening. Check character creation, exact location/area, opening NPC, first quest, one skill check, and one alternate player choice. Record actual observations; do not mark unplayed loops as passed.

### Step 11 — Record the batch

- Update the change log with the export/build, fields changed, validation evidence, playtest evidence, unresolved questions, and next authorized batch. Keep the original export and source worlds untouched.

**Current playability acceptance target:** a new player can create a character, begin in the selected academy area, meet the intended NPC, see one understandable objective, take a meaningful action, and continue or decline without a forced backstory or combat encounter.

## Stage 0 — Keep the project boundary clear

- Keep every supplied JSON under `sources/` unchanged.
- Keep the city map image marked as a frozen visual reference.
- Keep research, the outline, and the active JSON in their separate folders.
- Distinguish user-established canon from provisional implementation choices and open questions in [World Outline](World%20Outline.md).
- Record the active Voyage release channel and Studio version when the draft is opened there.

**Current state:** source and map boundaries are recorded; a first-pass outline and draft exist. The Studio environment is still unverified.

## Stage 1 — Establish the authoring basis

1. Preserve the untouched community API seed in `world-draft/base-world-v37.json`.
2. Keep the three WorldAlpha files as the active sources. The full world includes locations and NPCs; keep its embedded sections aligned with the standalone files.
3. Compare the seed and source exports with current Wiki guidance and the public validator; record mismatches rather than silently copying them.
4. The earlier V37 validator report is historical evidence for a removed prototype. It does not establish that the current WorldAlpha files pass Studio validation.
5. When the user imports/opens the draft in Voyage Studio, record its release channel, version, generated root shape, and validation result.

**Current state:** the prior prototype and playable copy were superseded by the three user-provided WorldAlpha files. The old validator result does not apply to them. The new files have not been imported into Voyage Studio in this pass.

## Stage 2 — Write a system brief without drafting prose

Define the intended experience in neutral fields before writing lore:

| Decision | Brief field |
|---|---|
| Play scope | solo/multiplayer expectations and campaign length |
| Core loop | what players repeatedly choose, risk, gain, or change |
| Character range | what a player can become and what remains outside the player sheet |
| World scale | geographic/map scope and how travel should work |
| Mechanics boundary | what requires exact tracking versus narrative interpretation |
| Tone boundary | what the narrator should preserve across scenes |
| Content boundary | intended rating and excluded content |
| Success criteria | observable checks for a satisfying first session and a longer campaign |

Do not resolve these blanks by borrowing named content or lore from the references. This is the design frame to use only after the user opens the brainstorming stage.

**Exit condition:** the brief fits on one page, has explicit constraints, and contains no contradictions.

## Stage 3 — Define identifiers and system dependencies

Create a small registry of canonical keys before creating many entries. For each key, record its display name, owning section, inbound references, and whether players can see it. Use stable spellings and avoid duplicate names. For every section, identify its dependencies:

- World and geography: realm → region → location → area/path.
- Character creation: trait category → trait → attribute/resource/skill/item/ability grants.
- Mechanics: attribute → skill → action check; resource/level → progression; trait/skill → ability requirements.
- Cast: NPC → type/faction/location/area/voice; NPC combat guidance → combat behavior.
- Story: story start → location/area/party NPCs/starting items/starting quests; quest → location/objectives/activation path; event → trigger conditions/effects.

Keep an explicit unresolved-reference list and close it before adding more content. Current key-name rules vary by section: do not assume quests use the same key/name equality rule as NPCs or locations.

**Exit condition:** every planned section has a clear owner and all cross-section names have one canonical key.

## Stage 4 — Build the mechanical foundation

Set attributes, resources, skill types, checks, damage/combat behavior, starting values, and progression before writing a large catalog of traits or abilities.

For each mechanic, document:

- player-facing name and meaning;
- structured field that owns the number or eligibility rule;
- how it changes during play;
- which AI task explains its narrative meaning;
- what happens at minimum/maximum or at failure;
- one test that proves the behavior.

Use traits for character build packages and narrative constraints. Use abilities for named player actions with supported requirements and effects. Keep NPC combat ability prose separate from player ability definitions. Check starting gear at the correct layer: universal opening items versus build-specific starting gear.

**Exit condition:** a minimal character can be created, make a representative check, spend/gain a resource, and receive the intended progression choices.

## Stage 5 — Build character creation and progression

1. Choose a short list of character axes that create meaningful choices.
2. Define their order, descriptions, and selection limits.
3. Add a small number of traits per axis and validate all category member keys.
4. Add dependencies using `unlockedBy`/`excludedBy` only after checking category order and current Studio behavior.
5. Connect trait grants to valid skills, attributes, resources, items, and abilities.
6. Set level-up cadence, point grants, max levels, and trait pools.
7. Test a normal character, a boundary character, and a changed earlier selection to see whether later options update as expected.

Avoid using prose instructions as a substitute for selectable options, requirements, or numeric progression.

**Exit condition:** choices show in the intended order; no option grants an unintended ability/item; progression tests match the brief.

## Stage 6 — Build geography from the locked visual reference

Preserve the map artwork. Derive an index of named destinations and playable areas from the frozen Version 1 image without changing its composition. Treat map coordinates, map labels, and Voyage location keys as separate data that need to be aligned deliberately.

For each region/location/area, add only the information required for navigation and play: key, parent, coordinates or placement, visibility, area description, paths, relevant factions, and NPC presence. Use `basic`/`detailed` generation settings intentionally; do not duplicate long description text across overview, lore, and every location.

Test each route and story-start location/area pair. Keep visual labels, JSON keys, NPC placement, and quest locations in sync.

**Exit condition:** all named map destinations have valid parent links and reachable paths, while the map asset remains unchanged.

## Stage 7 — Add factions, NPCs, and recurring cast

Create only the NPCs needed for the opening and first gameplay loops. For each one, define the stable identity, type/tier, faction, location/area, visibility, basic and hidden facts, personality behavior, and optional combat guidance. Use a unique key/name for recurring NPCs and avoid placing a central NPC in a universal opening area unless that is intended.

Build faction records before referencing them in region/location/NPC fields. Ensure every faction reference resolves. Test entrance, dialogue, movement, combat, party membership, and return to scene. Use current official Studio fixes and release notes as context, but do not assume they remove the need for reference integrity.

**Exit condition:** cast members are identifiable, placed, and testable; no dangling references remain.

### Character portrait brief workflow

Keep the generated portrait brief separate from gameplay background facts. Build it from explicit visual selections and route each selection to one job:

- **Framing:** crop, camera distance and angle, visible body range, subject scale, pose visibility, and edge spacing.
- **Style:** linework, palette, shading, lighting treatment, material rendering, and finish.
- **Character:** anatomy, body type, skin or other surface, hair, face, eyes, outfit, and any selected visible props.
- **Scene:** physical location and background objects. Environment rendering may add depth, atmosphere, and light, but cannot move the camera or hide the character.

Give framing and style their own categories with `maxSelections: 1` when one of each is required. A subcategory’s “recommended: 1” label is only guidance; Voyage’s documented limit is shared across all picks in a category. Keep appearance options optional when a world default can produce a usable portrait without them. [Trait category schema](https://wiki.unofficial.voyage/mechanics/traitCategories).

For every framing option, store the full visible composition in its selected trait effect: crop, angle, pose, gesture, subject placement, and the one or two details that make that shot distinctive. Pass that full text into the portrait brief. Do not rely on a trait name such as “Offering” or a short waist-up label to carry an unspoken pose. Generate a final prompt with a stable, compact order such as:

```text
[frame lock: exact crop, angle, pose, subject scale, visible boundaries, signature action]
[style lock: medium, linework, palette, lighting, finish]
CHARACTER — [selected permanent visual details and frame-visible outfit]
SCENE — [selected physical setting and key objects]
RENDERING — [depth and atmosphere; preserve frame and subject readability]
GOAL — [one sentence about identity and mood]
AVOID — [likely crop, anatomy, prop, and text failures]
```

Avoid contradictory framing instructions, model names that may age out, and repeated prose that does not improve a visible choice. If a world uses a custom pass-through marker to stop global image instructions from rewriting a player prompt, document it as a prompt convention and test it in current Studio; do not assume the marker is a platform feature.

Review generated prompts and images separately. For each test character, confirm every selected permanent visual anchor appears in the prompt, then compare the image against the selected crop, signature pose, style, outfit, and scene. Record which failures persist across rerolls. Voyage supports portrait regeneration from art direction in the in-game Assistant and Studio after confirmation, so iteration can be part of the workflow. [Official Patch 2.36.9](https://voyage.io/whats-new/patch/patch%3A100000954).

## Stage 8 — Wire quests and narrative events

For each quest, specify its entry condition, source, location, objectives, active objective, completion condition/effect, next step, and whether it is conclusive. Decide whether it appears at game start, on a mechanical condition, or after a story-discovery gate. For each event, define its start condition, beats, target pacing, completion effects, and handoff into quest/world state.

Use typed triggers for exact effects. A useful organic pattern is:

1. A location/turn gate establishes a scene and records that the hook is available.
2. A specific story condition confirms that the player actually encountered the hook.
3. A one-time trigger initializes the quest.
4. Completion triggers start follow-up quests/events only after the intended state change.

Use structural conditions to limit semantic checks. Use scripts only where plain conditions/effects cannot express the logic; comment state keys and intended repeat behavior.

**Exit condition:** every authored quest has an explicit intended entry path and an exercised completion path.

## Stage 9 — Add task-specific AI instructions

Start from Voyage defaults and change only the sections that conflict with the design brief. Use:

- world overview for concise, always-relevant premise and current situation;
- world lore for detailed facts that should be retrieved when relevant;
- task-specific AI instructions for story, action resolution, openings, NPC intents/details/updates, items, and other generation steps;
- narrator style for global voice/tone, not for mechanics;
- triggers and supported fields for exact state changes.

Prefer named instruction sections when changing a default behavior and `custom` for additive world-specific rules. Use labeled, short rules with observable intent. Remove contradictions and repeated versions of the same rule. Stay below current task-specific caps and leave revision margin.

**Exit condition:** each modified prompt has a named owner, expected behavior, and at least one playtest case.

## Stage 10 — Validate, playtest, and record

Use the checklist in [Development and Validation Checklist](Development%20and%20Validation%20Checklist.md). At minimum validate structural references and current size limits in Studio, then playtest one full character start, a representative check, a quest hook, a quest completion, travel, and NPC interaction. Keep logs of the exact build/release channel, test setup, expected result, actual result, and any bug workaround.

**Exit condition:** validation and playtest results are recorded as pass/fail/untested. Never label an untested behavior as passed.

## Batch/change record template

Copy this blank block for each future implementation batch:

```text
Batch ID / date:
Scope:
Sections changed:
Canonical keys added or renamed:
Dependencies updated:
Current Studio version / release channel:
Validation result and warnings:
Playtest setup:
Expected behavior:
Observed behavior:
Known failures or hypotheses:
Rollback/export reference:
Next authorized batch:
```

The current project has begun world ideation and initial JSON authoring. Continue from [World Outline](World%20Outline.md), add content in small batches, and keep provisional assumptions visibly separate from canon.
