# ⛩️ Portal to the Oni Nation — Research and Map Plan

Planning revision: 2 November 2026. **No canonical JSON changes, generated art or implemented features.** This document is for approval before production. National, settlement, clan and site names below are working proposals unless identified as existing canon. The date attached to the older handoff is not a requirement or authority for this update.

## 1. Direction and confirmed decisions

This is a large, continuous, inland Oni nation on Earth, represented through a separate Voyage realm following our existing convention for distant countries. It is not an archipelago or a new planet. The map is **four square columns across, three rows down**, with twelve geographical regions. **Forest surrounds all four outer edges; no coastline is visible.** Rivers can continue through that forest beyond the illustrated frame without making the frame a coast or an impassable magical wall.

The author selected **one substantial capital and two smaller castle towns**, with most land given to agriculture, forests, mountains and other wilderness. A terraced Shogunal castle and a **sacred mountain behind the capital** establish the principal silhouette. Individual buildings stay small at national scale; the map does not become twelve oversized settlements.

The country combines Japanese-inspired countryside, shinobi and samurai traditions, distinct towns, shrines, bamboo, grain fields, onsen and yokai with restrained Arcane/Soul magitech. Edo-inspired craftsmanship and buildings can coexist with fantasy devices. No modern neon skyline, dense electrical wiring, copied Hidden Leaf layout or carved cliff faces of rulers.

Its peace is real but fragile. A capable Shogun seeks more consistent law, taxation and military coordination; semi-independent clans defend territory, rights and obligations. Neither side is uniformly righteous or villainous. Civil war is not the starting state, and the player need not become a political operative.

### Two different gates

1. **Capital Transit Shrine:** the ordinary, authorized Evertree-network arrival. A torii stands within a controlled shrine compound with an actual arrival area and staff. Its network return leads to **Evertree Base - Portal Room**, not a selected Glowhaven neighborhood.
2. **Soul Torii:** a different, initially dormant site in the sacred mountain's lower cedar country. An earned local quest item awakens a route to separately authored spirit wilderness. Its return leads back to this Oni site. It is not another ordinary network gate.

The capital also receives an **Adventurer's Guild branch**, explicitly requested during this planning pass. It belongs to the existing international organization, recognizes the existing badges and maintains its own local clients and staff.

### Earlier decisions carried forward

- Court authorization and actual route keys remain separate from guild badges. Existing authorized returns remain reliable.
- The existing once-only Silken Descent anomaly is preserved. A new outbound route must use the same crossing decision owner rather than race it with another teleport.
- The Soul Torii's earned-item idea and spirit wilderness remain. The older small-map/cast recommendation is superseded by this larger nation.
- Ordinary creatures and crowds use npcTypes; a persistent named yokai or boss can justify an NPC card. No authored roster of twenty identical spiders or guards.
- Current card/portrait conventions apply: native JSON; full canonical names in factual references; hair/eye colors; selective named relationships; real flaws and ordinary interests; flashier major portraits. Affinity-count RNG remains 65% one, 25% two, 10% three, subject to authored concepts and existing exclusions. Do not turn every Oni into a Soul caster.
- Noncasting and martial player builds remain valid. Spell invention still uses Spellcraft. No free Time affinity, default Space study, universal mastery or new race bonuses are implied.
- Property keys preserve an actual address, owner and agreement after a genuine acquisition. Local homes are not an excuse for a catalogue of hundreds of fixed key items.
- The chained dragon, Vladimir Kujo and Citadel of Dreams remain separate planned arcs. The nation is not a compulsory connection to them, and primordial origins remain undiscoverable.

## 2. Geography before buildings

The image should read as an inhabited landscape. A main northern watershed supplies the central basin and southwestern lake country. Ridges divide tributaries; roads use valleys, bridges and actual passes. All twelve cells belong to one continuous place, not twelve self-contained themed squares.

Use early-autumn warmth in low country: gold wheat/barley plots, irrigated paddies, white susuki grass, red maples and green bamboo. These are different land uses and plants, not one generic yellow texture. Northern snow belongs to elevation, with forested foothills and intermediate slopes. A region boundary must not produce an abrupt season change at the same elevation.

The Japanese landscape references are useful for relationships between places: post roads combine villages, paddies, rest stops, shrines and wooded passes; bamboo can support crafts and nearby shrine life; sacred mountain approaches link cedar stairs, lodgings, falls and a summit precinct. These are inspirations, not literal imports of real shrines or a historical claim about one uniform Japan. [JNTO Nakasendo](https://www.japan.travel/en/au/story/walking-nakasendo-road-magome-tsumago/), [Arashiyama](https://www.japan.travel/en/spot/1141/), [Dewa Sanzan](https://www.japan.travel/en/spot/2130/).

Sucker Punch's environment team describes distinct foliage, strong local color and a balance between natural scenery and built order. Our adaptation is to give each province a recognizable silhouette and vegetation character without using a different visual style in every tile. We do not borrow its invasion plot or promise its game's traversal systems. [Crafting the world of Tsushima](https://blog.playstation.com/2020/07/09/crafting-the-world-of-tsushima/).

## 3. The proposed 4 × 3 atlas

North is up. A–D run west to east; 1–3 run north to south. Coordinates in parentheses are future native region-cell positions, not location coordinates.

| | A — west | B | C | D — east |
|---|---|---|---|---|
| **1 — north** | **Blackpine Frontier** (0,2): deep forest, ravine, abandoned defense | **Thundercrag Highlands** (1,2): ridges, quarry roads, mountain workshops | **Mount Shiun Pilgrimage** (2,2): sacred peak, cedar stairs, falls, Soul Torii | **Snowcedar Pass** (3,2): high pass, cold forest, isolated lodges |
| **2 — middle** | **Western Castle March** (0,1): smaller river-fortress town | **Bamboo Veil Valleys** (1,1): bamboo, working hamlets, concealed routes | **Capital Basin** (2,1): Shogunal capital, ordinary transit torii, guild branch | **Eastern Castle Terrace** (3,1): smaller hill-castle town, craft terraces |
| **3 — south** | **Mirror-Reed Lowlands** (0,0): freshwater lake, marsh, boat villages | **Golden Grain Plain** (1,0): wheat/barley, paddies, farms and markets | **Redleaf River Country** (2,0): maple valley, river trade, onsen | **Lanternwood Border** (3,0): old forest, memorial roads, yokai country |

Mount Shiun is a working name. Its peak is the northern focal point above the capital, with the lower slopes continuing into the capital region. Place the castle near that approach, not an implausible isolated summit hundreds of kilometers above its people. Avoid cutting either city center or hero peak on a tile seam where feasible.

### Continuous water and roads

- Main river: C1 headwaters → C2 capital basin → C3 valley → B3 low fields → A3 lake. A visible outlet continues through the southwest forest. The lake does not receive several rivers without an outlet or a deliberately established closed-basin explanation.
- Western tributary: B1 → B2 → B3. Eastern tributary: D1 → D2 → C3. Smaller streams join them down-gradient. No unexplained river splitting uphill or identical sources at every square's top edge. [USGS drainage reference](https://www.usgs.gov/water-science-school/science/streamflow-and-water-cycle).
- Main road: western castle → bamboo valleys → capital → eastern castle, bending with terrain rather than following straight grid lines.
- Pilgrim road: C3 river towns → C2 capital → C1 mountain approach. The Soul Torii is reachable as a physical local site before its supernatural route works.
- Southern working road links the lake villages, grain markets, maple towns and eastern border. Northern roads reach actual passes and hamlets, with risky alternatives away from established traffic.
- Most settlements have a practical water source, cultivated surroundings and access to a route. Secret routes and remote sanctuaries are exceptions with believable support.

## 4. Landmark reserve: 74 concrete anchors

These are map-composition anchors, **not 74 mandatory giant buildings or a final location JSON**. Some will become complex locations; small features can be areas or scenery. Several capital services share districts. Keep secrets visually plausible without labels advertising their reward.

| Cell | Proposed visible anchors and uses |
|---|---|
| **A1** | **1. Blackpine Watch Ruin:** broken stone base above the trees. **2. Wolf-Track Ravine:** split forest floor and one narrow bridge. **3. Resin-Cutter Hamlet:** a few working roofs. **4. Hollow Drum Cairns:** old memorial stones. **5. Northwood Ranger Lodge:** practical shelter. **6. Moonlit Sinkhole:** a dark geological opening, not a glowing portal. |
| **B1** | **1. Thundercrag Quarry:** terraced rock cuts and haul route. **2. Storm-Lashed Tor:** distinctive forked ridge. **3. High Bell Pass:** a guarded saddle. **4. Mountain Forge Hall:** modest smoke and workshop roofs. **5. Seven Rill Falls:** tributary cascades. **6. Ropewalk Hamlet:** bridge workers and stores. |
| **C1** | **1. Mount Shiun:** the national hero mountain. **2. Long Cedar Stair:** an actual ascent. **3. Summit Shrine:** restrained roof cluster. **4. White Veil Falls:** water descending toward the capital. **5. Pilgrim Lodgings:** settlement at the accessible foot. **6. Soul Torii Grove:** old gate among cedars, with no active vortex painted into the base map. |
| **D1** | **1. Snowcedar Pass:** cold forest and a narrow traversable saddle. **2. Frost-Eave Lodge:** warm roofs beside the road. **3. Abandoned Signal Tower:** a modest ruin. **4. Frozen Mirror Tarn:** a high lake. **5. Antler Ridge:** jagged natural skyline. **6. Snowmelt Chapel:** a remote local sanctuary. |
| **A2** | **1. Western Castle Town:** low river-facing fortifications. **2. Twin-Arch Bridge:** the controlled crossing. **3. Iron Market:** craft/work district. **4. Reedbank Barracks:** bounded military precinct. **5. Ferry Hamlet:** boats, homes and mooring. **6. Old Checkpoint Court:** a public place suited to disputed tolls. |
| **B2** | **1. Bamboo Sea:** the principal green-gold grove. **2. Lantern Cut Road:** road through tall stalks. **3. Whisperfall Gorge:** a crossing with a visible watercourse. **4. Bamboo Craft Village:** basket, paper and instrument work. **5. Veiled Lodge:** a secluded inhabited training/courier compound. **6. Rain-Listening Pavilion:** small scenic structure with no mandatory quest. |
| **C2** | **1. Shogunal Castle:** layered roofs and retaining walls. **2. Capital Wards:** compact city fabric with market/residential differences. **3. Capital Transit Shrine:** the authorized torii compound. **4. Adventurer's Guild Branch:** near transit, inns and work traffic. **5. Great River Bridge:** a recognizable civic crossing. **6. Canal and Workshop Quarter:** limited magitech integrated into ordinary craft. **7. Public Shrine Gardens:** festivals and everyday visits. **8. Martial Hall District:** actual schools and practice courts. |
| **D2** | **1. Eastern Castle Town:** elevated hill keep, unlike the western river fort. **2. Lacquer Terraces:** artisan streets. **3. Eastward Assembly Hall:** a local political/civic landmark. **4. Magitech Waterworks:** channels and compact mechanisms. **5. Ginkgo Schoolhouse:** ordinary learning. **6. Terrace Muster Ground:** field training outside dense housing. |
| **A3** | **1. Mirror-Reed Lake:** the main freshwater basin. **2. Willow Landing:** an inland boat village. **3. Reedwheel Mill:** a working shoreline mill. **4. Sunken Causeway:** old path, partly flooded. **5. Lotus Sanctuary:** a quiet waterside precinct. **6. Fisher's Lantern Isle:** a small lake islet, not a sky island. |
| **B3** | **1. Golden Grain Plain:** separate gold dry fields and green paddies. **2. Harvest Market Town:** small trading center. **3. Granary Court:** food storage and inspection. **4. Wind-Grass Ridge:** wild white susuki above cultivated land. **5. Terraced Farm Village:** homes beside irrigation. **6. Broken Scarecrow Shrine:** modest local oddity. |
| **C3** | **1. Redleaf River Town:** merchant roofs and boat landings. **2. Three Weirs:** stepped water management. **3. Maple Onsen:** one compact baths/inn cluster. **4. Old Theater Grove:** outdoor stage and seasonal gathering. **5. Waterwright's Yard:** repair, hauling and ordinary employment. **6. Autumn Bridge:** smaller scenic crossing. |
| **D3** | **1. Lanternwood:** the eastern/southern forest mass. **2. Mossbound Shrine:** old roof among trees. **3. Last Rest Post Town:** roadside hospitality, not a fortress. **4. Battlefield Memorial:** physical remains of a particular past conflict. **5. Root-Hollow Descent:** a cave entrance. **6. Boundary Stones:** an old path into deeper wilderness. |

A shrine, bridge or hamlet should have a distinct silhouette, approach or landscape relationship. We do not need six reskinned torii corridors. Guild halls, shops and houses remain architecture-sized, with no oversized signs on the clean master.

## 5. Map production: reliable first, elaborate second

### Verified constraints versus our choices

The current official Creator API contract specifies **at least 600 × 600 pixels** for gameplay uploads, **5 MiB per file**, accepted PNG/JPEG/WebP MIME types, and **1000 × 1000 recommended** for REGION_MAP_IMAGE. It declares no mandatory upload aspect ratio or maximum pixel dimensions. The community reference separately describes the **square region display**, so square tiles avoid an extra crop. **1254 is our existing working convention, not Voyage's required tile size.** [Official live contract](https://api-alpha.aidungeon.com/creator/v1/openapi.json), [official agent guide](https://api-alpha.aidungeon.com/creator/v1/agent-guide.md), [region reference](https://wiki.unofficial.voyage/world/regions).

The final atlas target is **5016 × 3762**: 4 × 1254 by 3 × 1254. This is an export canvas. It is not a promise that the built-in image tool will produce those native pixels or that enlarging a smaller result invents reliable architectural detail.

### Recommended pipeline

1. **Approve this geography.** Resolve the three settlements, watershed, principal roads, sacred mountain and two gates before ornamental detail. Nation/capital final names can wait because the clean map has no lettering.
2. **Prepare a fixed planning overlay.** Use a deterministic 4 × 3 grid, watershed/road lines and landmark anchor points as the composition reference. This is a later production step; no image asset was generated for this planning document.
3. **Generate one continuous 4:3 master composition.** High oblique national atlas, colorful polished 2D fantasy illustration, tiny buildings, continuous forest margin, no labels or grids burned in. Ask for the actual available native size, inspect its dimensions and retain the original. Use the supplied reference for landmark hierarchy and density, not its geography or distinctive buildings.
4. **Review geometry before enhancement.** Three cities must be distinct; the capital/peak relationship must read; rivers and roads must connect across future seams. Correct the master while it is still one image. Do not approve a pretty image that cannot support the location plan.
5. **Resize once to the exact export canvas.** Preserve aspect ratio. If the generator returns another ratio, choose a deliberate crop or composition edit rather than stretching the nation. Keep the native master as the quality reference.
6. **Slice the finished master mathematically.** Export twelve exact 1254-square PNG tiles. Reassembling them must reproduce the export master pixel-for-pixel. No independent enhancement after slicing in the default path. Deterministic cropping is supported by ordinary image tools. [ImageMagick crop reference](https://usage.imagemagick.org/crop/).
7. **Prepare a separate labeled guide.** It can show A1–D3, roads and landmark IDs for Studio placement. The clean playing map remains unlabeled. Save a coordinate/anchor manifest so later edits do not depend on guessing from memory.
8. **Upload and inspect.** Use REGION_MAP_IMAGE for each square, exact region identity, centered focus, zoom 100. Existing `regionMapBorderFeatheringEnabled: false` is retained. Measure encoded file size; use lossless optimization or an approved high-quality encoded format if a tile exceeds 5 MiB. Do not invent URLs or silently lower detail.
9. **Assemble in a disposable Studio draft.** Test cell ordering, all 17 internal neighbor seams, six four-cell intersections, crop and marker alignment. The guaranteed route is twelve per-region images at explicit coordinates. A convenient whole-atlas Studio import/split UI should be tested on a disposable example before being promised; it is not needed for the API route.

### If one master's detail is insufficient

Use **selective landmark refinement**, not twelve free reinterpretations. Edit a few overlapping windows with surrounding context, keep the base terrain and boundary collars, and composite only approved interiors into the master. Reliable boundary preservation requires a real mask/layer operation; a prompt alone cannot guarantee it. Our built-in image tool does not expose a mask parameter, so any hard protected composite must be handled as a separately approved image-editor step. Re-slice only after master-level review.

If refinement becomes a patchwork, stop and return to the coherent master. At national scale, location/area art is the right place for room and street detail. We should not spend hours forcing every workshop roof into the atlas.

| Approach | Use here | Main cost or limitation |
|---|---|---|
| One master, deterministic slicing | **Default** | Seam geometry stays coherent; enlargement cannot manufacture genuine fine detail. |
| Independently generated region tiles | Reject for this continuous nation | Roads, scale, rivers, color and lighting drift. |
| Overlapping edits/outpainting | Limited corrections with approval | Context helps; exact geometry is still not guaranteed by generation. |
| Layered landmark assembly and masked fills | Fallback for a small number of anchors | Strong placement control, more editor labor and consistency review. |
| Alpha/color seam blending alone | Finishing only | Cannot repair a shifted river, duplicate town or mismatched road. |
| Fully procedural terrain | Optional planning underlay | Excellent repeatable geometry; does not automatically deliver the requested illustrated finish. |

The community map-piece guide offers a useful layer-and-repair technique. Its **1537 × 1023 repair tile is that author's workflow**, not a Voyage requirement. It was illustrated with campus-scale pieces; copying its cutaway-building assembly wholesale would undermine a tiny-building national atlas. [Community map-piece guide](https://wiki.unofficial.voyage/guides/build-a-fantasy-map-from-ai-pieces).

## 6. Region and location data plan

The realm contains twelve regions at `(column, 2-row)` for zero-based column/row indices. Region-local locations keep the current range around −50…+50 because `regionSize` is 100. Do not change that global setting to fix one map. Existing Asterveil already demonstrates adjacent region coordinates; the world currently keeps new region generation and border feathering disabled.

For a landmark at source pixel `(u,v)`, width W and height H:

```text
tile = W/4 = H/3
column = floor(u/tile)             # A=0 ... D=3
row = floor(v/tile)                # north=0 ... south=2
region = (column, 2-row)
local_x = ((u-column*tile)/tile - 0.5) * 100
local_y = (0.5 - (v-row*tile)/tile) * 100
```

Handle points exactly on a cut deliberately rather than letting floating-point rounding assign them. Under the current documented units, the atlas spans roughly 400 × 300 km. The drawing is stylized; native travel still needs tests over multiple cells. [Location geometry](https://wiki.unofficial.voyage/world/locations), [current location settings reference](https://wiki.unofficial.voyage/other/locationSettings).

### Working content budget

| Region | Locations | Areas | Emphasis |
|---|---:|---:|---|
| A1 | 7 | 20 | wilderness and former defenses |
| B1 | 7 | 24 | mountain work, routes and isolated sites |
| C1 | 9 | 40 | pilgrimage, lodgings, sacred mountain and Soul Torii |
| D1 | 6 | 18 | high-pass exploration |
| A2 | 13 | 64 | western castle-town life |
| B2 | 9 | 30 | bamboo, craft villages and covert fieldwork |
| C2 | 20 | 120 | capital districts, institutions and households |
| D2 | 13 | 64 | eastern castle-town life |
| A3 | 7 | 22 | lake villages and marshland |
| B3 | 8 | 28 | farms, markets and local livelihoods |
| C3 | 9 | 34 | river work, onsen and cultural life |
| D3 | 7 | 24 | border communities and supernatural wilderness |
| **Working total** | **115** | **488** | Flexible scope; prune redundant markers before writing JSON. |

This exceeds either current Glowhaven's 68 locations/292 areas or Drakenspire's 59/251. The supplied reference export uses 223 locations across its sixteen main-world cells; our lower average is appropriate for more open country. Density and useful activity matter more than matching its count.

A town district can be a map location; its inn rooms, counters, shops sharing a block and household interiors are areas. An isolated shrine, ferry, cave or distant village can merit its own marker. Use smaller positive radii for tightly packed city services and test overlap resolution; do not blanket every shop with a five-kilometer catchment. Preserve short local player references while resolving exact stored addresses.

## 7. Government and social institutions

The Shogun's court sets policy through actual offices and negotiates with clan delegates. Provincial administration, town magistrates, tax officers and military commands have bounded duties. A decree does not instantly convince every town or give every official omniscient records.

Proposed major houses, **working names only**:

| Institution | Public interests | Internal disagreement and playable friction |
|---|---|---|
| Shogunate / ruling household | common law, revenue, patrol coordination | reform-minded officials, older retainers and ambitious relatives disagree about method and pace |
| House Kanetsuru, west | forge towns, crossing rights, longstanding military obligations | younger merchants like standard tolls; a household elder fears losing the family's bargaining power |
| House Mizunoe, east | waterworks, land surveys, terrace towns | capable engineers favor shared standards while retainers resist central interference |
| House Amakusa, south | agricultural estates, grain storage and transport | tenant livelihoods, warehouse profits and wartime duties divide relatives and clients |
| House Kagetsura, north | pass defenses, pilgrimage roads and inherited custodial duties | some welcome funded road repair; others distrust outside troops and attempts to standardize sacred obligations |

These are influences, not occupation/species/personality sorting. Individuals can oppose their house's policy or be concerned chiefly with a wedding, craft, rivalry or meal. Do not assign one faction exclusive control of every resident in a region.

Two proposed shinobi organizations provide actual service contexts: a **Reedshadow Lodge** of field couriers, scouts and specialists taking contracts, and a smaller **White Thread Office** within Shogunal intelligence. Membership and secrecy vary; neither is automatically a criminal gang or the true power behind everything. Public messenger work is real work, not just fake cover for every resident.

Town councils, shrine custodians, water associations, merchant/craft bodies, martial schools and the international guild create interests beyond the great houses. Independent yokai neighbors can have agreements, occupations and property without being a uniform supernatural faction. Gods, spirits and ancestors are not all interchangeable.

## 8. Capital Adventurer's Guild branch

Place the branch near the transit quarter, practical inns and the road toward the main bridge. It should be easy to find without treating arrivals as automatic enrollment. Suggested areas: reception/job counter, request hall, appraisal bench, common room, training court and a small staff office. Add an infirmary only if it has a real staffed role rather than duplicating a nearby healer gratuitously.

Proposed recurring staff: branch master, memorable contracts clerk, appraiser and assessment/field officer; a fourth or fifth support role depends on actual workload. They have personal interests and different opinions beyond quest administration. Capital roster allocations include them; they are not counted twice.

Use existing **Bronze, Silver, Gold and Platinum badges**, real licensure, recognized service and assessed promotion. A Glowhaven badge remains valid. Posted rewards are the player's net payout; the guild's in-world commission never causes an extra deduction. No new national badge currency or duplicate rank items. Court-issued portal keys remain unrelated.

Following the existing major-guild treatment, propose an image for the branch and each of its six core areas. This does not imply images for all 488 proposed areas. Elsewhere begin with important establishing shots and selected interiors; location art and later runtime generation cover different needs. Review a small art pilot before a large production batch.

The first local board offers a useful low-risk action job and a noncombat job. Examples: a grain-store nuisance, a faulty household ward, delivering a waterwright's part, surveying a safe pilgrim stretch. Midgame notices introduce real route threats, materials, escort and investigation. A level-1 applicant should not be sent to a level-30 yokai because the country looks impressive.

Implementation should keep the existing Glowhaven dispatcher intact and add a **location-gated capital-board dispatcher** with a compact local table. They cannot both be eligible at different branches. Share badge identities and reward rules, not a second promotion economy. Expand existing promotion/assessment scope carefully where staff and authority support it. Do not copy Komugi Hanabishi or Hinae Komori into this country under a new name or start their personal story again.

An optional sixth opening, **licensed adventurer arriving at the capital branch**, is worth considering after the five requested starts. It is a proposal, not an approved free badge for every background. Alternatively the civilian start can discover the branch naturally.

## 9. Population strategy

Recommend **120–140 named characters**, with **128 as a working coverage budget**, roughly thirty major roles and the rest supporting people. This supersedes the old small-cast sketch. It is a production ceiling/guide, not a promise to fill unused slots with shallow people.

| Primary coverage | Working NPC count |
|---|---:|
| capital, including guild, court, households, work and leisure | 34 |
| western castle town | 16 |
| eastern castle town | 16 |
| eight village/post-town clusters | 32 |
| shrine, pass and remote working residents | 12 |
| wandering people with a real route | 8 |
| individually authored yokai/creatures with persistent identities | 10 |
| **Total** | **128** |

Allocate each person once by their main home/work, even when they travel. Most inhabited establishments have authored coverage; remote scenery and ordinary enemies do not need named custodians. Reusable types supply crowds, animals and nonunique threats without silently inventing replacements for established people.

Major status should include more than officials: a troublesome guild regular, an inn host, a martial rival, a performer, a yokai neighbor, a researcher or a difficult craftsperson can be central. Keep sympathetic, selfish, foolish, petty and genuinely cruel people. Do not resolve every flaw into hidden kindness or make every shinobi emotionally identical.

Named ties are selective. Build several households, rival colleagues, old friends, established partners and resentments, while allowing unrelated residents. Not everyone is single, noble, competent or romantically available. Appearance, silhouette, age presentation, horns, hair/eyes, weapons and everyday clothing should vary. No portraits or cards are generated during this phase.

The inhabited cast is predominantly Oni, with other established ancestries naturally present in trade, households and travel. Do not make ancestry an employment caste or introduce a new playable yokai race without a separate decision. A named nonhumanoid keeps its coherent anatomy and appropriate naming rather than automatically receiving a human surname.

Use the nation as the ordinary civic affiliation when appropriate, or an actual house/organization as a person's primary faction. Keep additional ties in the existing relationship prose rather than inventing a new multi-faction NPC property. An international guild employee need not be assigned a duplicate local guild faction to work here.

Routines mainly stay within a person's home/work district. Use narrative habits for ordinary life; reserve a supported placement controller for a small roaming cast, couriers and a few explicitly scheduled visitors. Do not simulate 128 people's full calendars. A quest participant or actual companion should not be teleported away mid-scene because a route tick changed.

Portraits later follow the approved one-pass workflow and exact canonical filenames. Major people receive more memorable staging/effects; supporting people remain polished. Review and upload in small approved batches using the existing authenticated uploader, hash/identity receipts and explicit replacement rules. Originals stay on R:, with no keys in Git or logs.

## 10. New starts and ordinary play

All five openings are native starts in actual local locations with one immediate playable situation. Their emoji display names and stored keys must match exactly. Existing starts remain intact. Do not force a sex, ancestry, advanced power, personal loyalty, owned house or romance. Service/training premises explain initial contacts, not a lifetime restriction.

| Opening | First scene and actual next action |
|---|---|
| **Samurai** | A junior retainer or newly accepted trainee is given a bounded escort/inspection duty at the western town. Meet the immediate superior and another retainer; choose how to handle a concrete discrepancy. No instant mastery or automatic command over civilians. |
| **Shinobi** | A trainee/field member receives a real courier or observation task from their organization, with an actual contact and a safe approach. Recognition should use the deed's meaning, not a brittle exact typed password. |
| **Wandering rōnin** | Arrive at a post town with independence and available work. An offered escort, dojo introduction and local problem provide options without compulsory desperation or a secretly inherited estate. |
| **Shrine apprentice** | Prepare a public observance and handle a small practical disturbance with an actual custodian. Cleaning, provisions, visitors and ritual are responsibilities; Spirit Torii access is not granted at birth. Non-Soul casters and noncasters can participate. |
| **Civilian / independent life** | Begin through an actual trade, household or work arrangement: merchant, artisan, farmer, healer or another profession. The first scene has a concrete task/contact and room for social choices, without making combat the only progress. |

Markets, teahouses, meals, seasonal gatherings, bathing, performances, household friction, paid shifts, repairs, hunting, practice and quiet scenery supply play between adventures. A local custom need not become a quest. A failed first task can change the approach rather than demand twenty administrative turns before anything happens.

Small rentals and work spaces can use the existing actual-transaction/address-key policy. A viewing or proposed lease does not create ownership. Generated houses for established local acquaintances belong as areas in appropriate residential locations, not as new regions beyond the map.

## 11. Independent adventures

Working launch envelope: **40–60 native quests** distributed across direct work, personal stories and several multi-part undertakings, plus **three or four developing arcs**. Arcs represent situations that can evolve; accepted jobs still use native objectives and one completion/reward owner. No trigger-per-conversation machine. A useful simple hunt can stay simple.

| Proposed thread | Play and possible outcomes |
|---|---|
| **Two Seals, One Road** | western tolls conflict with a new standard. Investigate, negotiate, escort, expose misconduct or work for an interested party. A specific road agreement can change without simulating national tax policy. |
| **The Courier Who Arrived Twice** | incompatible dispatches and actual witnesses create an intelligence problem. Follow the objects and people; do not make it a universal conspirator controlling the country. |
| **The Bell That Answers No Shrine** | a local spirit agreement, a town's account and a retainer's orders conflict. Resolve enough of the actual disturbance to earn the unique gate-awakening object. Observation, testimony, repair or fighting can contribute; Soul affinity is not compulsory. |
| **A Shrine Without Its Guests** | a festival has lost the neighbors it normally welcomes. Social or practical repair may matter more than defeating someone. No promise that every spirit is friendly. |
| **The Rōnin's Winter Pay** | a finite escort and disputed final payment reveal loyalties and self-interest. Protection, negotiation, refusal or exploitation remain choices. |
| **The Ledger Beneath the Granary** | shortages connect food, contracts and people concealing their decisions. The player can help, profit, expose or leave. Avoid duplicating a full financial simulator. |
| **A Voice Behind the Bamboo** | a named yokai neighbor supports recurring comedy and uneasy company. Ordinary requests can stay ordinary instead of unlocking a monster war. |
| **Forge at the Third Bell** | a costly device fails during real work. Practical diagnosis, permitted salvage and ownership matter; repair grants no automatic discipline ranks. |
| **Floodmark** | a damaged weir puts several settlements' interests in conflict. A limited repair and agreement has a visible local consequence. |
| **Schools With Open Doors** | willing practice, rivalries, lessons and teachers. Use actual trained characters; do not build a second Crucible tournament engine for every dojo. |

Add direct guild work at beginner, practiced and experienced bands: pests, deliveries, safe surveys, escorts, missing equipment, nuisance spirits, creature/material work. Leave major threats geographically legible and optional. One quiet bridge or beautiful grove can remain a place to talk or pass through.

## 12. Soul Torii and spirit wilderness

Keep the older design's clear ownership while leaving its exact item name provisional:

```text
optional local quest chapters -> actual final resolution
native onCompleteEffects -> one genuine earned item
at exact Soul Torii + actual item + not yet opened -> awakening event
awakening -> reveal the authored spirit foothold; stop before entering
later committed crossing -> spirit entrance
spirit return threshold -> same Oni Soul Torii
```

The earlier working item **Soul Bell** is a useful proposal. Its public description can hint at an answering tone near the gate, without trigger instructions or an assertion that every similar bell works. No shop-generated copy grants access. Ordinary quest rewards and the gate's opening have one owner each.

**Recommended, still requiring approval:** opening is permanent once legitimately awakened. Losing the bell before opening means actual recovery or a specifically authored replacement route; losing it afterward does not close a world passage. The user has approved earned-item awakening, not yet this persistence detail.

First spirit slice: one region, approximately 6–8 wilderness locations and 24–32 areas. Possible glade, pale river, lantern wetland, root crossing, silent shrine, old battlefield and a distant clearing. Do not add the later Citadel of Dreams or a spirit metropolis here. Establish an immediately credible return and actual routes between sites.

This gate is **outside the Evertree network**. Update network wording to distinguish public-network returns from this local return. Every regular network return still goes to Evertree; spirit return goes to its own anchor. The existing Spider return and its mechanics remain exact.

## 13. Threats, techniques and equipment

The author approved broad progression: safe civic routes and first jobs for **levels 1–5**, growing into optional remote threats around **55**. This is not a nation of level-50 farmers. Working adults and trained guards use existing world power anchors; rank, age and portrait flair do not inflate levels.

Use location-level bands where a dangerous site or starter-friendly working area differs from its broader region. Do not set a high regional minimum that turns every generated shopkeeper into a veteran. Existing NPC power is not rewritten to match the player. Higher-risk work is an informed choice; no hidden elite on the first guild job.

Proposed creature catalogue: **30–45 carefully differentiated npcTypes**, not forty humanoid reskins. Categories can include mundane nuisances, bamboo/forest wildlife, marsh predators, bounded constructs, local spirits and unusual yokai. A general yokai type is not a hostility flag. Unique enduring adversaries receive named records only when their identity matters. Avoid inexhaustible reinforcements and automatic opening burst damage.

Proposed equipment/technique scope: roughly **40–60 useful item designs** and **48–72 targeted techniques**, revised after auditing the existing large catalogues for overlap. Use swords and spears, bows, staves, chained or hooked tools where training supports them, practical armor, work tools, travel gear and limited magitech. Samurai are not all identical katana users; shinobi need not all throw explosives. Build meaningful drawbacks and utility rather than adding renamed copies or raising all numerical bonuses.

Skills, learned spells, innate affinity and item assistance remain separate. Physical moves use Stamina where appropriate; casting uses Mana and its discipline; invention uses Spellcraft. Existing generation/refinement ceilings and temporary-conjuration rules remain.

## 14. Technical risks and scope discipline

| Risk | Implementation direction and live test |
|---|---|
| Map seams | one master and exact crop manifest; inspect 17 joins and six intersections in Studio, not only a file viewer |
| Native square crop/fading | explicit square files, focus 50/50, zoom 100, existing feathering false; no overlaps/padding in final tiles |
| Country borders and untracked travel | keep newRegionGenerationEnabled false, distinguish fictional distant existence from available destinations; do not claim this alone blocks all untracked movement |
| Radius overlap/city density | small supported positive radii and deliberate anchors; test arrivals between adjacent services |
| Network crossing races | extend the existing destination recognizer/decision owner; existing anomaly has priority, one actual position update per crossing |
| Foreign-origin permissions | decide the actual bilateral authorization procedure; do not require a native starter to first be in Glowhaven to request access, or silently grant every local a court key |
| New torii arrival presentation | use a precise dedicated capital compound/area; scope old “enclosed room” wording to its actual routes rather than narrating a courtyard as a random wilderness gate |
| Quest floods | offer a couple of relevant public situations without automatic acceptance; measure eligible semantic checks before adding monitors |
| NPC schedules | small selected itinerary table, no all-cast clock; do not move actual companions/active scene participants out from under play |
| Guild duplication | one international badge/rank system; separate location-gated boards and correct local staff; one payout owner |
| Foreign justice | bounded Oni institutions; do not expand solo Glowhaven wanted-poster/Wraith custody triggers to this country by accident |
| Start validity | exact location/area names, emoji key=name, real contacts, one clear first action; no invented starting mastery or property |
| Existing saves | fresh-start delivery first; test platform-supported updates separately, no automatic migration or reset of old NPC/quest state claimed |
| AI instruction space | New NPC currently 19,632/20,000 and Encounters 19,956/20,000 UTF-16 units. Country detail belongs in scoped lore/locations, not appended everywhere. Consolidate only where justified. |
| Content size | NPC section currently ~1.116 million units; current community section cap is 2 million. At 128 new records, target proportionate cards averaging roughly 3,500–4,500 units, measure actual output and keep future headroom. Whole world is ~4.703 million against the current 12.5-million portable check. |

The public API provides media upload capability, not proof of a whole-map import UI or a native daily schedule feature. Current geography and code observations are evidence; untested engine behavior stays a live-test obligation. Reference-world counts and systems are examples, not guarantees.

## 15. Implementation sequence and approval gates

1. **Map direction approval:** twelve cells, main watershed, forest edges, three settlements, sacred mountain, two gates and landmarks. Confirm the final name separately; it does not need to appear on the artwork.
2. **Master-map pilot:** one complete composition, reviewed at full view and simulated region zoom. If needed, one focused revision before any tile expansion. Do not generate twelve regions independently.
3. **Map export pilot:** twelve square slices, per-region upload receipts and a disposable Studio assembly. Verify orientation and travel placement before writing all locations.
4. **Geographic world skeleton:** latest author-supplied world as base; realm/regions, roughly 115 locations and area paths, local lore and basic access. Preserve all existing media and realms. Validate before new plot controllers.
5. **Capital/branch and five starts:** small first population batch plus basic work, permissions and ordinary life. Play each opening before expanding to the full cast.
6. **Population and content waves:** villages and the two castle towns, shrine/mountain residents, wilderness/types; cards and portraits in curated batches. Add independent personal and political stories without making every person a quest giver.
7. **Soul Torii slice:** one verified earned-item/open/cross/return loop, then the spirit wilderness. No separate event may steal an ordinary portal action.
8. **Equipment, techniques and polish:** fill actual playstyle gaps; audio per situation and existing optional ownership. Do not expand a catalogue just to reach the suggested counts.
9. **Live release audit:** fresh starts, existing visitors, noncasters, low-level contracts, refusal, party travel, lost keys, returning after absence and completed quests. Public patch notes follow actual delivered scope, not this entire wishlist.

### Specific acceptance tests

- Every grid neighbor lines up; a river is neither duplicated nor cut off at a seam; region crop and markers agree.
- Each of the five starts produces a useful action quickly, including a civilian who never fights.
- A Bronze holder from Glowhaven can use the capital guild without a duplicate badge or deducted cut. An unlicensed local cannot acquire licensure merely by browsing.
- Local early work is viable for a level-1 solo character. Traveling with a powerful NPC does not raise it to a hidden veteran job.
- The ordinary gate works before and after the existing once-only anomaly; returning updates structured location to Evertree Base - Portal Room. No narration-only arrival.
- The Soul Torii ignores an unrelated bell, reveals only after real earned possession, does not force entry and returns to the same local site.
- A rumor does not create an unapproved region. Asking to visit an actual friend's house can resolve to an appropriate residential area.
- Finishing a short job finishes it and pays once. No missing offered flag, compulsory extra report or auto-generated sequel rewinds its result.
- Political refusal is playable. Neither avoiding the Shogun nor declining clan employment blocks ordinary life.
- A second human does not duplicate rewards, seize another player's earned object or cause unsupported whole-party custody. No broad all-party move is hidden in a personal quest.
- No NPC knows the primordial account; the sacred mountain and spirit route do not become explanations for it.

## 16. Decisions still open

Final nation/capital names; final house names and Shogun identity; whether Soul Torii opening persists after losing its item; exact foreign-start transit authorization; which optional sixth guild opening to include; final cast/content counts after coverage review; and whether any particular villain/yokai concept is reserved by the author.

These do not require generating hundreds of cards before seeing the map. The next production milestone is approval of the geographical composition, followed by **one** master-map image.
