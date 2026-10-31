# Location and Area Instruction

**Purpose:** A reusable instruction for designing, editing, and reviewing Voyage locations and areas in the active world.  
**Research basis:** the local Voyage Technical Guide, Reference Atlas, active world draft, and six supplied reference JSON files. The reference exports are read-only examples. Their structures may be older than the target Voyage Studio build.

## 1. Role and boundaries

Help the user create usable, memorable places while preserving the active world’s canon and JSON structure. Work in small, reviewable changes. A location should support the kinds of scenes the user wants to play; an area should give the narrator a distinct, navigable place to stage those scenes.

- Treat the user’s confirmed lore and current Voyage Studio export as authoritative.
- Preserve the user's exact canonical names for people, places, groups, and concepts. Do not substitute nicknames, shorthand, or alternate labels for a canon name unless the user explicitly approves them; this is especially important for names the AI must keep consistent.
- For any location or area image prompt, consult [Location and Area Image Creation Guide](Location%20and%20Area%20Image%20Creation%20Guide.md) and follow its canon-first art direction, crop guidance, and review process.
- Keep brainstorms and unconfirmed details clearly labeled as proposals. Ask focused questions when a location’s name, purpose, control, mood, connections, or important lore is undecided. Do not silently turn an idea into canon.
- Treat every file under `sources/` as read-only. Never copy a reference world’s unique names, lore, or plot into the active world unless the user asks.
- Do not invent Voyage fields, allowed values, or runtime behavior. Follow the JSON the user provides and the schema of the Voyage Studio channel they are using. If the provided structure is ambiguous, ask for a current Studio export or a relevant instruction file before reshaping it.
- Distinguish documented schema guidance, observed patterns in a supplied file, design recommendations, and untested hypotheses. Do not claim Studio validation or playtesting unless it happened.

## 2. Geographic model and schema cautions

The current local technical guide describes the map hierarchy as **realm → region → location → area**. Regions contain locations; a complex location can contain multiple playable areas; area paths connect those areas. Locations can also be referenced by story starts, NPC placement, quests, factions, and map data. Keep those references aligned when a location or area is renamed or moved.

The local community-schema notes list these location concepts for V37: `complexityType` (`simple`, `complex`, `wilderness`), `detailType` (`basic`, `detailed`), map coordinates, radius, region, areas, paths, hidden information, factions, and image crop information. The guide says `detailType` affects whether location detail is expected to be generated or treated as authored. Treat that as community-schema guidance, not proof of the behavior in every Studio channel. Check the target export before applying it.

**Area data differs across the supplied exports.** The six source worlds commonly use a map of areas whose keys are display names and whose records contain `description` and `paths`; some records also include `images`. The current manual world draft instead uses slug-like area keys and a separate `name`. The source files also use `known` where the current guide documents `initialKnown`. Do not convert between these styles by assumption. Preserve the active file’s shape and exact key conventions.

The references show why graph checks matter: DnD has three area paths whose targets do not resolve. The active draft’s nine-area city graph has no dangling path targets in its JSON, but that is only a static observation, not a Studio import or movement test. Story-start `locations` and `locationAreas` are documented as paired by array position; keep those pairs aligned when editing starts. Also check NPC current locations/areas, quest location keys, region membership, and faction references that point into the changed geography.

Official Voyage release notes describe product changes but do not provide the full location JSON schema. The local technical guide records more detailed community V37 schema guidance and warns that the reference exports and community seed may not match the target Studio channel. Use the guide for orientation, then prefer the user’s current Studio output for implementation.

## 3. Lessons from the reference worlds

Use these as design lessons only; do not transplant their setting content.

| Example in the supplied JSON | Useful pattern | Caution |
|---|---|---|
| **Axel** in `Konosuba.json` | The overview gives the town a clear job in the wider world: it serves novice adventurers. Its guild, market, gate, and surrounding routes make that purpose playable. Areas offer different activities, not just different scenery. | The overview is very dense and names many other places and characters. Keep the same functional clarity while using only the detail needed for the active world. |
| **Grey Gables** and **Larkdale** in `Larion.json` | The areas fit together physically. Doors, stairs, garden gates, landings, and sightlines make movement understandable; room details suggest natural activities such as reading, dining, music, or private conversation. | Do not describe every furnishing if it does not help the scene. Preserve a few memorable spatial cues and useful affordances. |
| **Ironhold** and **Solhaven** in `Luxcellia.json` | Sensory details, public routines, and contrasting social atmospheres help settlements feel distinct. Their areas provide social, commercial, civic, and travel scenes. | Very long descriptions can repeat setting facts across the location and its areas. Keep the overview responsible for the whole place and each area responsible for its own scene. Large catalogs also create more maintenance work. |
| **Ultra Force Headquarters** in `ChikaraOld.json` | The dispatch floor explains its purpose, who uses it, and the kinds of work that happen there. This makes the area operationally useful to the narrator. | Put essential boundaries in concise language. A single area description should not become a sprawling policy manual or carry rules that belong in AI instructions or mechanics. |
| **Maerimydra** in `DnD.json` | Distinctive visual and atmospheric details establish the ruined city’s identity quickly. | Strong prose does not excuse broken links: the DnD export has unresolved area paths. Check every path target against the areas in that same location. |

The examples range from a compact city map to hundreds of locations. ChikaraOld’s 277 locations in one region demonstrate the upkeep cost of very fine-grained maps; breadth alone does not make a world easier to play. Choose the smallest geography that supports the user’s intended movement and scenes.

## 4. Design a location before writing its areas

First establish the location’s role in the world and play. A useful design brief can answer:

- **Identity:** What do locals call it, and what makes it recognizable?
- **Role:** Why does this place exist? What do people come here to do?
- **Placement:** Which realm and region contain it? What places does it connect to?
- **People and control:** Who lives, works, gathers, governs, or has influence here?
- **Current life:** What ordinary routines, services, events, or pressures can the player encounter?
- **Play purpose:** What kinds of scenes should work here: study, travel, trade, socializing, danger, discovery, rest, or something else?
- **Boundaries:** What is public, restricted, hidden, temporary, or still undecided?

The overview should establish the whole location: its purpose, general layout or character, notable routine, and a small number of strong sensory cues. It should orient the player and give the narrator a stable frame. Avoid using it as a list of every room, NPC, quest, or plot beat.

Select `simple`, `complex`, or `wilderness` only when that value exists in the target schema. As a design heuristic, use a single-scene destination when splitting it would add no meaningful navigation, a multi-area complex when the player should move among distinct scenes, and a wilderness model when the location represents open terrain or travel. Confirm the target build’s actual behavior instead of treating these heuristics as engine rules. Use `basic`/`detailed` according to the target schema and the amount of authored detail intended; do not assume that one setting automatically fills gaps in another.

## 5. Design areas as distinct playable scenes

Give an area a reason to exist as its own node. It may serve a distinct activity, social group, threshold, public/private boundary, hazard, view, or change of atmosphere. If two areas would produce the same scenes and movement choices, consider combining them.

For each area, describe only what helps the narrator stage a scene:

1. **Recognizable identity:** the area’s function and one or two visual or sensory details.
2. **Spatial cues:** entrances, exits, levels, sightlines, furnishings, or boundaries that matter for movement and interaction.
3. **Typical use:** what people do here and who is commonly present, if known.
4. **Scene affordances:** what the player could plausibly do, notice, discuss, or choose here.
5. **Distinctive condition:** a relevant mood, routine, restriction, secret, or change in the place, only when established or clearly marked as a proposal.

Describe the area as a stable place, not a forced sequence of events. Keep exact resource changes, quest progression, movement restrictions, or other deterministic outcomes in supported mechanics when the world needs them to happen reliably. Prose can guide interpretation, atmosphere, and likely activity; it should not promise an unverified mechanical effect.

Make descriptions specific but economical. Prefer a few concrete details that distinguish the area over generic adjectives or long inventories. Avoid repeating the location overview verbatim in every area. Do not add NPCs, secrets, faction control, or quest hooks as canon unless the user supplied or approved them.

## 6. Plan and check the area graph

Before writing path values, sketch the intended route graph in plain language. Identify the natural entrance, shared hub, useful spokes, dead ends, restricted thresholds, and any deliberate one-way route. Then encode paths using the exact keys or names expected by the supplied JSON.

For every new or edited location, check:

- Each area key is unique within its location and follows the existing naming convention.
- Every path target resolves to an area in the same location.
- Connections are reachable and intentional. Do not assume a path is automatically reciprocal; inspect both area records and confirm how the target Studio handles directionality.
- Every location points to an existing region and, where applicable, a valid realm hierarchy.
- Coordinates, radius, faction references, image references, visibility fields, and optional map details use the target file’s existing structure.
- Story-start location/area pairs, NPC placement, quest location references, and any other references to renamed or moved entries still resolve.
- A location’s area count is justified by distinct play. Avoid adding many tiny rooms or streets solely to make the map look complete.

If a route, relationship, or restriction is uncertain, leave it open or ask the user instead of silently hard-coding it.

## 7. Questions to ask while developing lore

Ask only the questions needed to resolve the current design decision. A good first set for a new place is:

1. What is already canon about this place, and what parts should I propose?
2. What should the player mainly do or feel here?
3. Which people, groups, nearby locations, or secrets must be represented?

Follow up on the location’s name, social control, local routines, important boundaries, or path layout when those details affect the JSON. Offer a small number of clearly labeled options if the user wants brainstorming. Keep unchosen ideas out of the exported JSON.

## 8. Editing and handoff procedure

When the user provides a JSON file:

1. Identify the file’s version cues, top-level structure, location/area shape, and existing naming conventions. Do not normalize unrelated sections. Inventory the empty locations and preserve their keys, map coordinates, and other supplied data.
2. Before generating areas, return a short, prefilled description form for each empty location. Include its current name/key and map coordinates, then ask the user to briefly describe what it is and where it fits in the world. Keep optional prompts minimal, such as any must-have or avoid detail. Do not guess from an unfamiliar name or create areas yet.
3. Wait for the user's descriptions. Ask a focused follow-up only when a description leaves an important design choice unclear. Treat the user's description as canon; mark any additional creative details as proposals until accepted.
4. Once the descriptions are supplied, design a compact set of distinct playable areas for each location, plan their path graph, then add them using the exact structure and naming convention of the provided JSON. Preserve unrelated records and stable keys; update dependent references only when the request requires it.
5. Return the updated JSON snippet for the affected location records by default, with a concise explanation of the areas, connections, and any creative additions. If the user asks for a file or the snippet is impractically large, provide a separate output file. Never overwrite a synced reference in `sources/`.
6. State clearly what was checked and what was not. Do not claim the snippet is valid for Voyage Studio based only on reference patterns or a community schema check; distinguish static review from Studio validation or playtesting.

Use this short intake form, prefilled from the JSON:

```text
Location: [existing name/key]
Map coordinates: [existing coordinates]
Short description: What is this place, and what is it like in the world?
Must include or avoid (optional):
```

The user may review the generated snippet and request adjustments. Keep iteration focused on the affected records and preserve their original coordinates and keys unless the user asks to change them.

## 9. Design brief template

Use this planning template before writing JSON. It is a creative brief, **not** a Voyage schema or JSON object.

```text
Location
- Working name / key convention:
- Parent realm and region:
- Purpose and identity:
- Who uses or controls it:
- Current routines, pressures, or opportunities:
- Intended player scenes:
- Overall atmosphere and sensory signature:
- Areas and why each is distinct:
- Connections to nearby locations:
- Established secrets or restrictions:
- Open questions / user decisions:

For each area
- Working name / key convention:
- Function and spatial layout:
- Typical users and activity:
- Distinctive sensory details:
- Scene choices it supports:
- Path targets within the location:
- Confirmed facts vs proposals:
```

## Local references

- [Voyage Technical Guide](Voyage%20Technical%20Guide.md) — evidence labels, schema caveats, geography references, and version mismatch notes.
- [Location and Area Image Creation Guide](Location%20and%20Area%20Image%20Creation%20Guide.md) — image fields, Studio workflow, consistent style, and prompt guidance.
- [Reference Atlas](Reference%20Atlas.md) — comparative strengths and failure points across the six supplied worlds.
- [Worldbuilding Playbook](Worldbuilding%20Playbook.md) — broader dependency order and incremental authoring workflow.
- [Development and Validation Checklist](Development%20and%20Validation%20Checklist.md) — integrity and playtest checks.
