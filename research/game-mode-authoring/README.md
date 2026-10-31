# Glowhaven game modes

**Authored:** 2026-10-27, Asia/Shanghai.  
**Deliverable:** [WorldAlpha - Game Modes.json](../../world-draft/WorldAlpha%20-%20Game%20Modes.json).  
**Status:** 12 fully authored mode briefs. Local structure, identity, field-length and section-size checks passed. No Voyage Studio import, community-validator submission, runtime execution or playtest was performed.

## How to use the file

In Voyage Studio, open Files -> Other -> Game Modes and replace the entire empty `{}` with the contents of the deliverable. The file is the mode map itself, beginning with `"Balanced"`; do not add a second `gameModes` wrapper inside that section. If manually integrating into a complete world JSON instead, this map is the value of its existing `gameModes` field.

This delivery does not modify the complete WorldAlpha export, its AI settings, NPC roster, locations, lore, quests or progression. It is the standalone section requested for copying into Studio. There is no automatic import or publication.

## Research and evidence

The implementation uses the documented six fields: `name`, `description`, `difficulty`, `instructions`, `npcIntentInstructions`, and `askTheNarratorPrompt`.

- **Official:** Voyage [Patch 2.33.7](https://voyage.io/whats-new/patch/patch%3A100000946) confirms mode-specific `npcIntentInstructions` and its 5,000-character cap. The [official release archive](https://voyage.io/whats-new) was also checked. Official release notes do not supply the entire section schema.
- **Community reference:** The [Game Modes page](https://wiki.unofficial.voyage/other/gameModes) and its [machine-readable section reference](https://api.unofficial.voyage/sections/gameModes.json) supply field definitions, key/name matching, allowed difficulty presets, and the size constraints used in local checks. This is community documentation, not official Studio validation.
- **Observed examples:** All six supplied files under `sources/` were inspected for their mode structures and authoring choices. They remain unchanged. No distinctive reference-world lore or characters are adopted.
- **Design judgment:** The particular loops, pacing and character guidance are our authored choices. Their reliability is an untested hypothesis until observed in actual play.

### Inspiration from the supplied worlds

| Example | Useful pattern | Adaptation in Glowhaven |
|---|---|---|
| ChikaraOld | Different activities and NPC priorities for academy, everyday and fighting modes | Academy and Action receive distinct objectives and pacing. A tournament is not required for regular action. |
| DnD | Explicit separation of mood, threat scale and story focus | Comedy stays mechanically medium; Action increases the focus on conflict while Hard Mode presets harder combat. |
| Konosuba | Repeated gameplay loops and relationship-aware NPC behavior | Each mode specifies an activity sequence, aftermath and ways existing people initiate interaction. |
| Larion | Concrete everyday activities and restrained local openings | Slice of Life gives ordinary tasks choices and lasting results. Quiet scenes can continue. |
| Luxcellia | Specialized academy, investigation, romance and power-focused play | Adapt the strong focus while avoiding automatic admiration, invented resource increases and instructions that contradict progression records. |
| Overlord | Preserve power differences, selected roles and existing world rules | Modes do not grant institutional access or cancel recovery settings. A successful plan remains successful. |

## Compatibility decisions

### Social behavior belongs in story instructions

The current full-world file explicitly limits `generateNPCIntents` to actual combat. Its `core_principles`, `when_to_generate`, `what_is_not_action` and `story_driver` sections repeatedly require an empty intent batch outside a real fight and delegate ordinary activity to narration. It also excludes practice and consensual sparring from actual combat unless an attempt to injure or subdue begins.

Therefore each mode's `instructions` contains its social NPC behavior, and `npcIntentInstructions` contains task boundaries and combat-specific priorities. This preserves the current division of labor rather than giving the intent task contradictory instructions. If that base setup changes later, review both fields together.

### Mechanical settings and limits

Balanced, Academy, Comedy, Action, Drama, Romance, Mystery, Exploration and Contracts & Adventure preset `medium`. Slice of Life and Power Fantasy preset `easy`; Hard Mode presets `hard`. Those are existing recognized values. The presets affect combat difficulty; they are not general social-check, income or advancement multipliers.

Mode text is guidance. It does not install recurring NPC movement, an academic calendar, a guild, monsters, new quest definitions, crafting rules or deterministic memory. Power Fantasy emphasizes satisfying legitimate progress and gentler opposition; this section cannot independently accelerate XP or increase resource pools. Build any desired mechanical changes separately and test them.

### Death and recovery

The inspected world has `death.permadeath: false`. Its instructions specify knockout, healed next-day return near a city with the party, retained memories and retained possessions. All modes defer to those rules; Hard Mode explicitly preserves them. No mode adds item loss, a revival tax or permanent death.

### Content that is still planned

Contracts & Adventure uses appropriate existing employers until the world actually defines an adventurer's guild. Action and Exploration can use additional monster and wilderness content when it exists. They do not establish new guild ranks, monster species or inaccessible-place entrances. Major Eternal Crucible tournaments remain occasional events.

## Local checks performed

The authoring utility checks:

- Exactly 12 mode entries with unique identities.
- Every map key exactly matches its `name`.
- All six documented fields are present, nonempty strings, with no invented fields.
- All presets are recognized lowercase difficulty values.
- Names <=120, descriptions <=500, story and NPC instructions <=5,000 each, help prompts <=1,000 characters.
- Entire compact JSON section <=100,000 characters, including JSON escaping.
- JSON serialization and parsing preserve all content.
- The full-world export and six source JSON files retain their hashes during generation.

All authored characters are ASCII, so the local character counts match UTF-16 code-unit counts. The compact section is **62,204 characters**, leaving **37,796** characters of section headroom. Longest story instructions: **3,366**; longest NPC instructions: **1,385**. Exact per-mode figures are in [static-checks.json](static-checks.json).

These checks establish local structure and size compliance against the consulted reference. They do not establish Studio acceptance, prompt obedience or runtime playability.

## First import and playtest pass

Import this section into Studio and review its actual diagnostics. Confirm all twelve choices appear, their descriptions display, and the chosen mode's help text appears in the separate narrator-help chat. Confirm a mode change preserves the character and ongoing scene. Use comparable short situations in separate saves where feasible.

| Mode | Main behavior to observe |
|---|---|
| Balanced | Follow a chosen pursuit, then finish its aftermath without an unrelated emergency. |
| Academy | Receive a specific exercise, meaningful feedback and a useful follow-up without assumed enrollment. |
| Comedy | A successful plan succeeds; humor comes from characters and circumstances, not a canceled result. |
| Action | Receive a credible conflict opportunity with an objective, visible tactical choices and recovery. |
| Drama | A motivated disagreement changes after an honest explanation or repair. |
| Slice of Life | Complete several peaceful activities with tangible results and no compulsory danger. |
| Romance | An invitation follows actual interest; declining it is respected. |
| Mystery | Revisit clues and test a correct early hypothesis without the answer changing. |
| Exploration | Discover a supported feature or route without automatically exposing gated locations. |
| Contracts & Adventure | Clarify an offer, accept deliberately and receive only recorded completion and payment. |
| Power Fantasy | Actual strengths work against lesser obstacles; no invented XP, mana or powers appear. |
| Hard Mode | Preparation can prevent a setback, real enemies act competently and knockout retains possessions. |

Across modes, check that ordinary dialogue and practice do not produce combat-intent batches. In an actual fight, inspect available logs for targeting, action counts, available abilities and resolved outcomes. Compare intended guidance with observable behavior; revise a prompt only when a concrete failure or contradiction justifies it.

## Authoring maintenance

`build_game_modes.py` contains the authored common boundaries and twelve distinct briefs. Running it rebuilds only the standalone section and static-check report. If the JSON is edited directly, update the authoring source before rebuilding to avoid replacing those edits. Rerun size checks after any substantive expansion and repeat affected playtests after a behavioral change.
