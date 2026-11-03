# Fishing — implementation and review

Implemented 4 November 2026. The latest full Studio export (`366606e8-3528-434f-80b6-fef091104a73`) is the merge base. Its three music edits are preserved exactly. No NPC, portrait URL, location, area, map pin, map image, region, realm, existing quest, arc, progression value, starting currency or Spider record changes.

## Content and entry

- Native utility skill **Fishing**, linked to Intuition; the existing skill cap and normal practice progression apply. No custom skill-XP counter or extra XP per catch.
- The existing Fisher profession now gives Fishing +2 and Perception +1. Other professions remain exact.
- A Fishing Starter Kit adds one ordinary rod, eight bait portions and a field ledger. No starting selections are compulsory.
- First genuine setup/practice at a supported water area can grant Angling Basics to an actual rod holder with zero Fishing. Its native skill modifier creates rank 1. No second grant once skill exists.
- Thirty fish item types and eleven tackle/supply types. Species catalogue values are modest per-fish references, not guaranteed buyback prices. No fish has equipment bonuses or resource-restoration effects. No invented per-instance weight or item metadata.
- Eighteen exact existing areas form the fishing registry: river, harbor, estuary, shore and offshore. No location/area is added. Indoor rooms, the serpent ledge, turtle nesting shelf and dungeon areas are excluded.

## Resolution

Native action conditions recognize an actual cast and select qualifying players. Native `action-success-level` distinguishes success/mixed results from failure. Scripts do not ask the model semantic questions or roll a second accuracy check.

The two successful cast modes are exclusive: reusable lure, or an actually held and deliberately used bait portion. A basic rod includes a reusable spinner. A successful or mixed ordinary attempt selects one fish from its habitat table; a failed cast grants none. Baited failure consumes one portion, as does a successful baited cast. There is no automatic extra Health, Mana or Stamina cost.

Weights vary by habitat, the persistent local forecast and bait. A favored weather doubles the relevant weight approximately; bait increases the relative presence of uncommon and bottom-feeding fish. It never grants an additional fish or guarantees a rare one. Exact rolls are stored as results rather than rerolled during narration.

There are thirteen fishing/weather/discovery triggers, not a trigger per species. Short native water-area gates run before semantic checks; scripts then require the exact registered area and Glowhaven realm. Carrying a rod into the Crucible therefore adds no fishing semantic checks. Each remains below five conditions, ten effects and 10,000 compact UTF-16 units. Scripts have empty static rewards unless the applicable gated path supplies the effect. Retry guards prevent repeated successful grants or failed bait charges in the same tick.

### Rare catches

Moonmirror Dace, Lanternjaw Angler and Crownfin Sailfish first grant the temporary **Rare Fish on the Line** trait, not a fish item. The script retains species, measured length, exact area and expiry (six further ticks). A real subsequent handling action uses Fishing:

- Basic success or better lands that exact species, grants one item and clears the trait.
- Mixed results or worse lets it escape and clears the trait.
- Deliberate release/abandonment clears the trait without a fish.
- Leaving the ground/realm or waiting past expiry clears the unlanded catch. It does not destroy the rod or other property.
- An already landed inventory fish can be released through ordinary actual item handling; the hooked-fish release trigger cannot remove another fish.

The shared hook record is swept once no party member retains the trait. Ordinary anglers can continue while another holds a rare hook; another rare-hook roll cannot overwrite its identity.

## Multiplayer boundary

Native player scope, native inventory conditions and `target: satisfyingPlayers` own fish grants, bait costs and temporary traits. An acting character cannot qualify using a spectator’s rod or bait.

The engine’s documented script interface does not expose the satisfying-player list. Accordingly, simultaneous qualifying anglers in the same cast mode share the local shoal/species and size roll, and each receives their own catch. The travel party’s discovery/best-length record is shared. It counts landing events, not a reliable per-person catch count. No fabricated individual statistics are shown. Different native action outcomes still determine which players qualify.

## Weather

One mechanical planning controller maintains separate inland/coastal forecasts in persistent JSON storage. States: clear, overcast, rain, fog, wind and occasional storm. Weighted transitions retain a state for 12–24 game ticks. Large time jumps advance to a current forecast without replaying missed weather scenes; no wall-clock or assumed day length is used.

Weather cues reach narration on forecast/context changes. They do not soak interiors, change another realm’s climate, force movement, cancel quests, damage resources, spawn enemies or pin combat music. Exposed offshore casts in a storm return a warning without a catch or bait charge. Existing named creatures keep their locations, behavior and danger.

This is not a native weather widget or a global climate simulator. Storage is not assumed to be visible to the narrator: explicit story effects carry the actual forecast.

## Studio objective-schema correction

Studio rejected the initial three fishing quests because their objectives used a description/completed array. Only those three objective fields were corrected to a native keyed map of `{id, text, status}` records. The authoring source and validator now enforce this structure; a regression reproduces all three rejected arrays and invalid record fields. No other world values changed in this hotfix.

## Native commissions and narrow repair

Three optional finite native quests: **A Fisher’s First Lesson**, **Supper before the Tide Turns**, **A Color beneath the Scales**. Each has a real existing client and one native completion/reward owner. Honest procurement remains valid where appropriate; a fishing grind is not compulsory. Actual handovers use ordinary inventory changes once. Offers do not accept jobs.

The eight earlier personal local commissions had a real script defect: `check({type:'action', query:...}) !== true` compares raw action text against a Boolean. They now use declared native semantic conditions, exact quest-status/location gates and a shared one-offer-per-tick guard. Existing quest definitions, acceptance and rewards remain unchanged. The original generator and the misleading Boolean test mock were corrected too.

## Portrait correction — private patch detail

Both runtime prompt owners, selected default style traits and the Hip-up trait now agree on drawn anime faces and a crop through both hips to the upper thighs. Explicit waist-up, close-up, alternate style and camera choices remain. No existing image is regenerated or replaced. Future image compliance remains a generator test, not a guaranteed visual result.

## Validation and live checklist

`tools/fishing/review.cjs` proves the field-level delta against the incoming export. All unrelated top-level sections and all existing NPCs, locations, areas and maps remain exact. Historical preservation fingerprint files were not rewritten. A separate read-only projection verifies this patch by whole-world before/after hashes for old preservation assertions; a mutation canary confirms unrelated edits cannot disappear through it. Current behavior fixtures still execute current scripts.

Run the normal project checks plus `node tools/test_fishing.cjs`. Conservative eligibility fixtures cover river, estuary, reef, ship and a live Crucible bout while carrying tackle; these retain the documented budget (including existing generated arc checks). Fixtures supply semantic answers and action outcomes. They test emitted JavaScript, inventory ownership, retries, weather persistence, all habitats/conditions, rare outcomes and preservation; they do not test the live model’s recognition or engine scheduling.

Before public release, test in Voyage:

1. New and existing characters: buy/receive a real rod, use a plain spinner, use a bait portion, fail a cast, and inspect actual inventory/skill updates.
2. Natural phrasings for fresh casts versus talking/buying/releasing. Ensure the narrator and item task do not grant or consume a second item.
3. Rare handling success, failure, deliberate release, leaving, timeout, and return. Check effect timing and trait removal.
4. Two human players: one fishing, a spectator with tackle, simultaneous anglers, mixed outcomes and independent bait ownership.
5. Visit/revisit indoor and outdoor places during rain/fog/storm. Cross a portal and confirm other realms retain their climate. Check visible weather against the catch table.
6. Ask for each new commission and the eight repaired personal offers. Accept/decline/complete through the native journal; check one payment and a real handover.
7. Generate one default and one selected Hip-up player portrait. Check anime facial treatment and visible upper thighs; compare an explicitly selected Waist-up crop.

No live Studio save, publication or gameplay test is claimed.

Reference: [Voyage trigger conditions, effects, phases and scripts](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [randomness and persistent scripting patterns](https://wiki.unofficial.voyage/appendix/scripting-patterns). These are community technical documentation; current official Creator API material documents upload/edit wrappers, not all game-runtime semantics.
