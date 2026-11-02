# Oni nation — map and production research

Checked 2 November 2026. Companion to [the complete planning document](../world-draft/authoring/plans/Portal%20to%20the%20Oni%20Nation%20-%20Research%20and%20Map%20Plan.md). Research and proposals only: no generated map, uploads, cards or canonical world changes.

## Evidence classes

| Finding | Evidence | What it does not prove |
|---|---|---|
| Direct gameplay image uploads require both dimensions at least 600, allow up to 5,242,880 bytes, and accept PNG/JPEG/WebP; REGION_MAP_IMAGE recommendation is 1000-square | Live official Creator API OpenAPI `1.3.0-preview`, `x-media-constraints`; official agent guide retrieved successfully | A 1254 tile requirement, 5K native generation, or a particular Studio atlas-import dialog |
| Official upload contract has no required aspect ratio or maximum pixel dimensions | Same live official contract | That a rectangular file will render uncropped inside the map's square cell |
| Region image renders in a square cell and includes crop data | Current community Regions reference; current world uses the same shape | Official proof of every crop behavior in the current running Studio build |
| World already has a 2×2 Asterveil layout, with top row y=1 and bottom row y=0 | Actual current JSON | A 4×3 map has been imported or live tested |
| Region size is currently 100; new region generation and border feathering are both false | Actual current JSON | Full prevention of untracked native travel just because region generation is disabled |
| Native geometry composes region position with local location offsets; local positive y is north | Community Locations/Location Settings reference, compatible with current layouts | Road following or collision with mountains painted into a bitmap |
| Exact crop/reassembly is deterministic | Standard raster operation, ImageMagick crop documentation | That a separately regenerated neighboring tile will have matching geography |

Official sources: [live OpenAPI](https://api-alpha.aidungeon.com/creator/v1/openapi.json), [agent guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md). This research made only unauthenticated documentation requests, with no remote world writes or media generation.

Community references, explicitly not Latitude documentation: [Regions](https://wiki.unofficial.voyage/world/regions), [Locations](https://wiki.unofficial.voyage/world/locations), [Location Settings](https://wiki.unofficial.voyage/other/locationSettings), [NPC size limits](https://wiki.unofficial.voyage/world/npcs). Some initial requests returned errors before subsequent requests succeeded. The community per-realm design advice favors fewer realms; our author-approved convention already uses separate realms for distant physical countries. That advice is not a schema ban on our convention.

## Production recommendation

Use a **4:3 continuous master**, export at **5016×3762** and cut twelve **1254-square** region files. The official minimum is lower and recommendation differs; this output target preserves the project's established working tile size. Do not imply the image generator guarantees the export resolution. The available built-in generation interface does not expose a pixel-size parameter; actual outputs need inspection.

One generated master, one deliberate resize and exact crops remove the principal geometry-seam failure introduced by independent tile generation. They do not guarantee fine detail or a compelling map. Roads, hydrology, settlement scale and landmarks still need visual review. An upscale is not a newly authored roof plan.

The default plan uses no independent post-slice generative enhancement. If local refinement is necessary, use context windows and restore hard boundary collars through actual masks/layers. Prompt-based preservation alone is insufficient. The built-in tool has no explicit mask parameter, and an image editor's protected composite is a separate operation to plan honestly. Do not install external generators or run copied scripts blindly.

The [community map-piece workflow](https://wiki.unofficial.voyage/guides/build-a-fantasy-map-from-ai-pieces) describes controlled layer assembly and gap repair. Its 1537×1023 repair rectangle is a workflow-specific example, not a native Voyage map specification. Its campus/cutaway examples are unsuitable as a wholesale national-map method. Borrow placement control and source preservation; avoid making each country tile a campus collage.

[ImageMagick's crop documentation](https://usage.imagemagick.org/crop/) supplies the deterministic operation. A later implementation can use an already available image library rather than requiring that application. Reassemble the twelve final crops and compare against the export master exactly. Test all seventeen neighboring edge pairs and six four-cell intersections in Studio. Final tiles have no overlap/padding and keep centered focus/zoom 100; the current world already disables edge feathering.

Per-region upload is supported through the existing official workflow. Whole-atlas Studio import/slicing was **not** exercised in this research and is not the critical path. Verify it in a disposable draft before recommending UI-specific steps or claimed automatic region naming. No image needs to be uploaded in this planning stage.

## Geography and cultural design references

Use the following as distinct sources of visual relationships, not buildings or storylines to copy:

- [Sucker Punch: Crafting the world of Tsushima](https://blog.playstation.com/2020/07/09/crafting-the-world-of-tsushima/): coherent local vegetation/color and natural versus built composition. Our proposal uses a few strong terrain/architecture anchors per province rather than random biome noise.
- [Sucker Punch: concept-art process](https://blog.playstation.com/2020/10/26/from-brush-to-blade-the-concept-art-process-behind-ghost-of-tsushima/): establish architectural rules and a settlement's activity before designing its visual identity. Our history, politics and supernatural plots remain original.
- [JNTO Nakasendo journey](https://www.japan.travel/en/au/story/walking-nakasendo-road-magome-tsumago/): connected post towns, agricultural land, passes and roadside amenities. Useful for playable travel country between the three urban centers.
- [JNTO Arashiyama Bamboo Grove](https://www.japan.travel/en/spot/1141/): grove, shrine and craft settlement can belong to a shared lived-in landscape. Bamboo is not merely background texture.
- [JNTO Dewa Sanzan](https://www.japan.travel/en/spot/2130/): a mountain approach can combine cedar stairs, lodging, worship and altitude-specific conditions. Our Mount Shiun is an original working proposal, not the same sacred site or religion.
- [USGS streamflow/watersheds](https://www.usgs.gov/water-science-school/science/streamflow-and-water-cycle): a main drainage and tributaries should follow the terrain. The proposed A3 lake has an outlet beyond the forested frame; the image does not end in ocean.

The lowland art combines distinct dry grain plots, paddies and wild susuki grass for the requested ronin atmosphere. It does not insist that every gold field is the same crop or that all real Japanese periods shared identical landscapes.

## Existing-world and reference measurements

The canonical world has 272 NPCs, 176 locations, 737 areas and 200 lore entries. Glowhaven has 68 locations/292 areas; Drakenspire has 59/251. Asterveil has four native regions. These are observations, not automatic quotas for the next release.

The available local reference export `5f2c3317-f5d6-44fd-aabf-64f3b95caeb0` has sixteen main-world grid regions, 223 main-world locations and several guild branches, with 5–9 areas in the sampled branches. This supports the usefulness of localized service hubs and varied landmarks, not copying its content or implying it is the creator's latest online version.

Current compact UTF-16 unit measurements: NPCs 1,116,374; locations 529,903; lore 205,124; npcTypes 98,302; total world 4,702,629. The community NPC section limit is 2,000,000, and our portable whole-world check is 12,500,000. The proposed 128-person coverage budget can fit if card sizes stay proportionate; measure actual data before approval of the final cast count. Do not casually fill every card to the 8,000-unit per-NPC maximum.

New NPC instructions already occupy 19,632/20,000 units; Encounters uses 19,956/20,000. There is almost no safe append-only room. Use scoped records and relevant lore; a new realm should not prompt another giant global instruction block. No existing instruction was shortened or changed in this planning pass.

## Decisions and pending work

Confirmed in this chat: horizontal four-by-three grid; all four edges forested; one capital and two smaller castle towns; capital castle backed by sacred mountain; distinct ordinary and earned-item torii; capital Adventurer's Guild branch; level-1–5 entry routes with optional distant danger up to about 55. Current JSON, media and progress remain unchanged.

The comprehensive plan supplies twelve proposed provinces, seventy-four landmark anchors, an estimated 115 locations/488 areas, 120–140 named people with a 128-person allocation, five requested starts and an optional guild arrival opening, politics, independent adventures, spirit-gate behavior and release tests. All new proper names, quantities and unapproved persistence rules remain proposals.

Next production is one master-map composition after the author approves the direction. The older blueprint remains historical context; no reliance is placed on the handoff's erroneous date reference.
