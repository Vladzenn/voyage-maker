# Voyage Technical Guide

**Research date:** 2026-10-26 (Asia/Shanghai).  
**Purpose:** current, source-labeled guidance for the separate drafts in `../world-draft/`. The source exports remain examples, and the public community validator is not Voyage Studio's validator.

## 1. Evidence layers and release-channel caution

Use these labels when discussing platform details:

- **Official product/release behavior** — Latitude's Voyage product pages and release notes. The official-domain [What’s New archive](https://voyage.io/whats-new) currently lists Patch 2.46.4, dated October 5, 2026, as its newest October entry. The r/Voyage release posts dated October 12 and October 19 report later V37 and Studio changes; that publication timeline differs from the official-domain archive, so confirm the active release channel before relying on a channel-specific behavior. The official [Open Beta page](https://voyage.io/releases/open-beta) confirms that Creator Studio is a supported world-authoring surface, but Latitude does not publish a complete JSON schema there.
- **Community schema documentation** — the [Unofficial Voyage Wiki](https://wiki.unofficial.voyage/) is independent and not affiliated with Latitude. Its [methodology page](https://wiki.unofficial.voyage/appendix/methodology) says the field names, value types, validator rules, and size limits are extracted and checked against the current Beta build. At research time it reports Voyage Beta 2.52.0, schema V37, last verified 2026-10-24. Use it as the best field-level reference found here, while checking changes in the Studio release channel that will actually author or run the world.
- **Observed export pattern** — a fact read from one or more supplied JSON files. It establishes what those files contain, not what today's Studio accepts.
- **Untested inference** — a plausible explanation from structure or instructions. Label it and test it before depending on it.

**Export/runtime shape mismatch:** all six supplied example worlds and the supplied Alpha export use root-level `triggers`, `questTriggers`, `quests`, `narrativeEvents`, and `arcs`. Current community V37 documentation calls the root trigger map `triggerDefinitions` and places `arcs`, `narrativeEvents`, `quests`, and `questTriggers` under `parties[""]`. The project base seed contains empty root placeholders plus an empty `parties` object; the Studio-generated `world.json` stores the four party sections under `parties[""]`. Treat older exports as observed examples, not the current authoring schema.

**Read the Studio error literally:** the screenshot says party fields `questTriggers` and `arcs` were `undefined` (missing at the reported path). An empty JSON object `{}` is a present, empty map; it is not `null`, and JSON has no `undefined` value. The sources also show that some maps can validly be empty: Luxcellia and four other supplied examples have no authored arcs, while ChikaraOld and Luxcellia provide populated quest-trigger examples. The current Alpha copy mirrors authored arc/quest/event/quest-trigger maps at root and under `parties[""]` to cover the two observed layouts. Its test loop contains one quest, one quest trigger, one narrative event, and one small one-quest arc patterned on Chikara’s schema.

**New likely cause of the generic conversion error:** the Alpha export lacked `imagePromptConfiguration`; all six supplied reference exports and the current V37 base seed have this object. The base seed also includes `characterCreationMusic` and `compatibilityRevision`, which the older source exports omit. These exact current-seed defaults are now present in the working copy. This is a stronger structural candidate than malformed trigger records, but only a Studio save can confirm the failing field.

The current Alpha copy preserves the supplied file’s two intentionally open success-score endpoints as `null`; the current schema explicitly uses null for the lowest minimum and highest maximum. They are also present in the base seed and are not the missing-object cause.

The current Alpha copy preserves the supplied file’s two intentionally open success-score endpoints as `null`. They are valid bounds in the original success-level tiers and are unrelated to missing object maps.

The official release archive and the Wiki are on visibly different release timelines in this snapshot: the official-domain archive's latest listed patch is October 5, the r/Voyage notes report V37 changes on October 12 and October 19, while the Wiki says it tracks Beta 2.52.0 as of October 24. Verify Alpha/Beta/production selection in Voyage before transferring schema claims or files. [October 12 V37 release notes](https://www.reddit.com/r/Voyage/comments/1x490rl/october_12th_2026_patch_notes/), [October 19 release notes](https://www.reddit.com/r/Voyage/comments/1xa7x32/october_19th_2026_patch_notes/).

## 2. How the world data fits together

A Voyage world combines persistent structured state with AI-generated narration. Latitude's [Open Beta announcement](https://voyage.io/releases/open-beta) describes Creator Studio as a natural-language creation surface and Voyage as a persistent roleplaying experience. The official [Closed Beta release summary](https://voyage.io/releases/closed-beta) describes creator-authored quests, custom resources, triggers, progression, and a move away from required race/class fields toward flexible traits.

| Layer | Main purpose | Dependencies to check |
|---|---|---|
| World overview and lore | `storySettings` provides the core world context; `worldLore` supplies deeper facts when relevant. | Keep the always-present overview concise; attach a single canonical name to each important place, group, and rule. |
| Geography | `realms` contain `regions`; `locations` belong to regions; locations may contain named `areas` linked with paths. | Region-to-realm, location-to-region, area path-to-area, NPC current location/area, story-start location/area, quest location, and trigger location references. |
| People and groups | `npcs`, `factions`, `npcTypes`, `worldVoices`, and archetype/seed sections shape recurring characters and generated cast. | NPC `type`, faction, voice, location, area, and any combat traits must resolve according to the target schema. Keep identity keys stable. |
| Character build and mechanics | Attributes, resources, skills, traits, abilities, item types, and settings determine player choices and roll behavior. | Trait category members must exist; skill attributes/types must be supported; trait grants and ability requirements must agree; item keys/slots must match. |
| Story flow | `storyStarts` and root `triggerDefinitions` control authored openings and deterministic rules. Current community V37 documentation puts `arcs`, `narrativeEvents`, `quests`, and `questTriggers` under `parties[""]`; supplied legacy exports put them at root. The Alpha draft mirrors authored arc/quest/event/quest-trigger maps to cover the observed Studio and runtime shapes. | Every predefined quest needs an intentional entry path; objective IDs, event IDs, trigger values, locations, and effects must agree. Validate the target representation in Studio before treating either shape as universal. |
| AI behavior | `aiInstructions`, `narratorStyle`, per-record prose, and game modes guide generation. | Use task-specific prompts for the behavior that task controls. Use typed mechanics for exact state changes. Keep prompt text within task-specific caps. |
| Presentation and authoring | Images, voices, music, archetypes, game modes, tips, and other settings affect rendering and generated content. | Separate frozen visual references from editable data and verify each interface-specific setting in Studio. |

The Unofficial Wiki provides field-by-field pages and a [machine-readable API](https://api.unofficial.voyage/). Its [validator](https://wiki.unofficial.voyage/tools/validator) and schema explorer are useful cross-checks, but Voyage Studio remains the final validator for a draft intended for a specific release channel.

## 3. Character creation, classes, and progression

### Traits and categories

The current trait system is flexible: traits can represent species, classes, backgrounds, professions, status, or other world-specific choices. `traitCategories` controls the visible selection axes and selection limits; the ordered categories matter because `unlockedBy`/`excludedBy` character-creation checks look at earlier choices. `requirements` gate level-up trait offers and do not gate starting character creation. Current docs distinguish player-facing `description` from `traitNarrativeEffects`, the narrator's guidance for play. [Traits](https://wiki.unofficial.voyage/mechanics/traits), [trait categories](https://wiki.unofficial.voyage/mechanics/traitCategories).

No supplied file has a root `classes` field. Class-like builds appear as trait categories and traits. Official Closed Beta notes say Voyage replaced required race/class choices with flexible traits; that does not prohibit a world from offering a category called `Class` or `Combat Class`.

A common mechanical chain is:

- **Trait category** lists eligible trait keys and `maxSelections`.
- **Trait** carries selection text, narrative behavior, skill/attribute/resource modifiers, starting items, ability grants, and optional dependencies.
- **Skill** defines a rolled action and its linked attribute/type.
- **Ability** defines a named special action, requirements, bonus, and cooldown.
- **Progression settings** decide XP cadence and how often a character receives ability points, attribute points, trait picks, or milestone titles.

Important dependency trap: a trait's `abilities` array grants those abilities directly. It can therefore bypass an ability's learnability requirements. Use trait/skill rules intentionally and test a new character against the ability panel. [Trait authoring details](https://wiki.unofficial.voyage/mechanics/traits), [abilities](https://wiki.unofficial.voyage/mechanics/abilities), [skills](https://wiki.unofficial.voyage/mechanics/skills), [level progression](https://wiki.unofficial.voyage/mechanics/progressionSettings).

### Attributes, resources, skills, and abilities

- Attributes are named in `attributeSettings.attributeNames`; modifiers and skill links should use those names exactly.
- Resources are world-defined meters such as health, mana, stamina, or setting-specific reputation/heat. Their maximums, starting values, and per-level changes need a coherent progression plan.
- Skills define the action types the engine can roll, the linked attribute, and AI-facing guidance. Current Wiki documentation calls the exact string `combat` mechanically special for attribute damage; other custom types should have deliberate `skillTypeDifficultyBonus` settings. Confirm in Studio and a playtest before relying on custom type names for combat.
- Abilities have named requirements and their own bonus/cooldown fields. Avoid building hundreds of narrow abilities when a smaller reusable set of skills and broader abilities will cover the intended play.

Observed choices across the exports: DnD uses standard six attributes and 1,449 abilities; Larion adds `attunement`; Overlord uses five different names (`strength`, `agility`, `intelligence`, `vitality`, `luck`); ChikaraOld defines 18 resources; Konosuba and Luxcellia each use two. These are patterns, not a recommended mechanics balance.

## 4. Geography, NPCs, quests, and events

### Map and location data

The current Wiki's location schema includes `complexityType` (`simple`, `complex`, `wilderness`), `detailType` (`basic`, `detailed`), coordinates, radius, region key, areas, paths, hidden information, factions, and image crop information. A `complex` location can hold multiple playable areas; `detailType` controls whether generated details are expected or authored details are treated as complete. Story starts pair `locations` and `locationAreas` by index. Areas have their own `description` and `paths` fields. [Regions](https://wiki.unofficial.voyage/world/regions), [locations](https://wiki.unofficial.voyage/world/locations), [areas](https://wiki.unofficial.voyage/world/areas), [story starts](https://wiki.unofficial.voyage/world/storyStarts).

The supplied `Final2_upscaled.png` is a frozen visual reference for city map Version 1. It does not establish Voyage's map coordinates, location keys, or area graph. Preserve the image while separately creating a location/area index that makes the structure playable. No map changes were made as part of this research.

### NPC data

Current NPC records distinguish identity, type/tier, location/area, initial-known status, base/hidden information, personality, narrative abilities, combat settings, and voice/presentation. The Wiki notes that the NPC `abilities` prose is narrative context, not references to the top-level playable `abilities` map; it also recommends placing a story NPC outside the opening area if it should not appear in every run that begins there. [NPC schema and authoring notes](https://wiki.unofficial.voyage/world/npcs).

Official patches have addressed duplicate identity references, same-display-name scene confusion, wrong NPC targets, unplaced NPCs appearing at game start, and quest NPCs arriving at the accepted destination. Keep the reference fields explicit and test scene entry, arrival, departure, and combat targeting. [Patch 2.45.3](https://voyage.io/whats-new/patch/patch:100001203), [Patch 2.43.0](https://voyage.io/whats-new/patch/patch:100001188).

### Quests and narrative events

Current Wiki documentation describes pre-authored quests as starting hidden; story starts can make specific quests available, while triggers can initialize, accept, progress, or complete them. A quest location is a location key, not an arbitrary region label. A quest trigger's conditions should constrain where/when its narrative condition is evaluated. Narrative events are useful for multi-beat scenes and can interact with quests and state through triggers. [Quests](https://wiki.unofficial.voyage/world/quests), [narrative events](https://wiki.unofficial.voyage/world/narrativeEvents).

Official Patch 2.43.0 added more control over when predefined quests become available or accepted, trigger-only quests, follow-up quests/events, NPC health/location/party checks and mutations, and story-start-based trait availability. Patch 2.45.3 later fixed a hidden-predefined-quest issue that could prevent first-turn detection of an explicit quest offer and reduced unnecessary trigger-check text that could prevent quest/world triggers from processing. [Patch 2.43.0](https://voyage.io/whats-new/patch/patch:100001188), [Patch 2.45.3](https://voyage.io/whats-new/patch/patch:100001203).

### Triggers and scripts

The Wiki documents triggers as condition/effect rules. A trigger's typed conditions are ANDed; structural checks should filter first, with AI-judged `story` or `action` checks added only where natural-language context is genuinely needed. Effects provide explicit state changes. Scripts extend logic but have per-phase execution budgets and a sandbox; malformed or slow scripts can fail or be skipped. [Trigger definitions and scripting](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [trigger size limits](https://wiki.unofficial.voyage/appendix/size-limits).

The Wiki currently reports: up to 4,000 mechanical and 500 semantic triggers; 15 semantic checks per turn plus 5 per active quest; at most 5 conditions and 10 effects per trigger; 10,000 compact characters per trigger; and 500 ms total script execution per phase. Treat these as community-extracted Beta values and confirm them with the active Studio. Larion's 466 semantic trigger definitions and 759 scripts illustrate why gating, budgets, and log inspection matter.

## 5. AI instructions: what they can and cannot do

`aiInstructions` is task-specific. The Wiki says named built-in sections can be overridden, while other second-level keys are appended as custom prompt material. A task's `custom` text is appended after named sections. Use the task responsible for a behavior: story style in `generateStory`, action checks in `generateActionInfo`, NPC goals in `generateNPCIntents`, location generation in `generateLocationDetails`, and so on. `storySettings.worldBackground` is broad always-present context; `worldLore` is detailed context that is retrieved when relevant. [AI instructions](https://wiki.unofficial.voyage/ai/aiInstructions), [story overview](https://wiki.unofficial.voyage/world/storySettings), [advanced instruction techniques](https://wiki.unofficial.voyage/appendix/ai-advanced-techniques).

Narrator instructions are interpreted by a model. They can improve consistency, but they are not state enforcement. Use triggers for guaranteed one-time narration, quest gating, numeric thresholds, or state transitions; use prose for flexible framing, motivations, tone, and scene choices.

Selected current Wiki caps: `worldBackground` and quest-generation guidance 5,000 characters each; narrator style 2,000; story starts 101 entries, 8,000 compact characters per entry; skills 250 published entries (the official Patch 2.46.4 notes allow drafts up to 375 while editing); abilities 1,500; entire traits section 1,750,000 compact characters; locations and NPCs 2,000,000 each. AI prompt caps are task-specific: `generateStory` 30,000; `generateNPCIntents` 40,000 total, with up to 8,000 per string leaf; `generateNPCDetails` 28,964; and `generateNPCUpdates` 24,000. General tasks have a 20,000 compact-character cap. Consult the current [size-limits table](https://wiki.unofficial.voyage/appendix/size-limits) and [Patch 2.46.4](https://voyage.io/whats-new/patch/patch:100002348) before writing.

## 6. Latitude AI issues, released fixes, and practical workarounds

These are not all the same kind of evidence. The “official fix” column describes problems Latitude says it fixed; the handling column is a workflow recommendation based on current documentation or the supplied examples.

| Issue pattern | Official release-note evidence | Practical handling for future authoring |
|---|---|---|
| A skill check can omit the linked attribute, or a combat skill name differs only by capitalization. | Patch 2.45.3 says untrained checks now include the linked attribute modifier and combat damage bonuses recognize case-only attribute-name differences. | Still make skill and attribute names match exactly in new data. Test a trained and untrained roll, including combat damage. Do not rely on a past fix to compensate for inconsistent names. |
| A failed/retried turn can leave delayed prose or skill results behind. | Patch 2.43.0 says late skill checks and story paragraphs from failed turns were fixed. | Include one failed turn followed by a retry in the regression checklist for any world with heavy triggers or scripted state. |
| NPCs can target poorly, duplicate, or appear at the wrong time/place. | Patch 2.45.3 lists targeting and duplicate identity fixes; Patch 2.43.0 fixes unplaced NPCs spawning at start and warns on missing area placement; Patch 2.45.3 fixes quest NPC destination placement. | Give each authored NPC a stable unique key and correct type/location/area; avoid colocating a recurring story NPC in a universal opening area unless intentional; test encounters with actors first mentioned in story. |
| A hidden predefined quest or excessive trigger context can stop an offer from being processed. | Patch 2.45.3 fixes both hidden-quest first-turn detection and a cause of quest/world triggers not being processed. | Provide one clear authored activation path per predefined quest; put cheap mechanical gates before semantic gates; keep semantic queries specific and test each quest from a fresh save. |
| Repeating arc-surfacing triggers can stop after one use. | Patch 2.46.4 specifically fixes recurring `arcSurfacing_<arcId>` triggers stopping after the first use. | For any intended repeatable system, test the second and third cycle, not just initial activation. Prefer explicit, small recurring triggers and verify the current Studio's behavior. |
| Story-start placement may not match a chosen location. | Current Wiki says location and area arrays are paired by position. Official Patch 2.45.3 added Studio area naming and Patch 2.43.0 warns about location/area assignment. | Validate every start pair; avoid parallel arrays generated from independently sorted lists. Test one run per start and inspect the actual opening position. |
| AI prompt rules are treated as if they were hard mechanics. | The Wiki explicitly distinguishes probabilistic instructions from deterministic trigger effects. | Do not ask prose to enforce exact currency, unlock, quest, damage, or movement results. Apply mechanics through supported fields/effects; use prose to explain what the result means in the fiction. |
| World JSON migrations or legacy fields produce confusing warnings. | Patch 2.46.4 says Studio now uses quest `status` instead of old `initialStatus` and corrected JSON validation for AI instructions and archetype/authoring sections. | Use current Studio-generated keys and validator results. Review warnings after opening/migrating an export; do not blindly preserve legacy aliases or rename every root key without validation. |

Other official changes to account for: Patch 2.42.8 added trait dependencies, progression trigger effects, and editable initial NPC relationships; Patch 2.43.0 added story-start trait gates; Patch 2.45.3 added NPC-in-combat/type trigger conditions and clarified that resurrection instructions concern successful revivals and final endings in permadeath modes. [2.42.8](https://voyage.io/whats-new/patch/patch:100001176), [2.43.0](https://voyage.io/whats-new/patch/patch:100001188), [2.45.3](https://voyage.io/whats-new/patch/patch:100001203), [2.46.4](https://voyage.io/whats-new/patch/patch:100002348).

## 7. What remains to verify in the user's Voyage environment

- The user-designated current sources are [WorldAlpha - World.json](../world-draft/WorldAlpha%20-%20World.json), [WorldAlpha - Locations.json](../world-draft/WorldAlpha%20-%20Locations.json), and [WorldAlpha - NPCs.json](../world-draft/WorldAlpha%20-%20NPCs.json). Their location and NPC sections matched when received.
- Earlier overlapping drafts were removed. No Voyage Studio import or playtest has been confirmed for the current WorldAlpha files.
- The community V37 validator reported 0 errors, 0 warnings, and 19 recommendations on 2026-10-25. The accepted recommendations are recorded in [the validation report](../world-draft/validation-report.md); this result is not a Studio validation or a playtest.
- Confirm the target Voyage release channel and Studio build, then import/open the draft and compare the editor's JSON and behavior with the community schema.
- Playtest the Phoenix Wing default start first: character creation, Arrival Court, Hinae's introduction, the affiliation-neutral `First Words` quest, and one Spellcraft check. Add other academy starts after those openings are authored.
- When later content adds mechanics, extend the test suite to cover trait gates, quest chains, NPC combat, travel, repeated triggers, and failed-turn retries.

The [Worldbuilding Playbook](Worldbuilding%20Playbook.md) now includes a focused playability procedure and records which setting details are established, provisional, or still open.

## 8. Historical Glowhaven Alpha playability pass (2026-10-26; superseded)

The earlier playability pass analyzed the now-removed GlowhavenAlpha Playable.json. Its findings are retained below as historical notes; they do not establish the contents, validation, or playability of the current WorldAlpha files.

The role baseline is Archons 85, headmasters 70, teachers 50, students 15, with Ilyra Stillglass remaining at 100. Student levels now use a working 10–20 band based on reference-world comparisons; all named students start at 15. Tier is assigned separately and reflects combat threat; eight `weak`-tier students remain level 15. Four academy locations set `npcLevelRange` to 1–60 for generated party-scaled NPCs. One `spellcraft` skill is defined for general magic checks, but no character-creation trait grants it; current skill settings leave unknown-skill learning probabilistic. Traits, learned spells/abilities, items, and a mechanical affinity bonus remain later work.

The user later showed Studio’s `World → Advanced → Quests` editor displaying `{}` and reporting missing party `questTriggers`/`arcs`. The working copy now populates quest, narrative-event, quest-trigger, and arc maps and mirrors them into the default party. The tiny arc follows the Chikara structure but uses only the generic first-conversation playtest. This follows the literal missing-field error and current community schema; a fresh Studio import/save still needs confirmation.

The historical static checks below applied to the superseded playable copy. The current WorldAlpha files parse as JSON and their split location/NPC data matches the corresponding sections in the full world file. No Voyage Studio import or gameplay playtest has been confirmed for the current files. See [Glowhaven Alpha Playability Audit](Glowhaven%20Alpha%20Playability%20Audit.md) for findings and remaining checks.
