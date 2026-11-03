# Glowhaven — overlapping circular map panels

3 November 2026. The author supplies four exact 627 × 627 quadrants of sparse v4. The current delivery is **one circular set with genuine shared overlap**, following the earlier Akitsuhara workflow. The asymmetrical alternative is cancelled. Prior tight-crop refinements and the rejected alternate master are archived in ignored local output and are not final panels.

## Panel order and output

| Number | Position | Main content |
| --- | --- | --- |
| 1 | Northwest | Sky, western range, Greywatch Keep, cropped northern tree/city |
| 2 | Northeast | Sky, distant Asterveil, sea/islands, cropped court/harbor |
| 3 | Southwest | Green ridges, river/woods, cropped southwest wall, Greyfield |
| 4 | Southeast | Cropped southeast city, coastal plains, villages, Shadowspire |

These are four working panels, **not four final Voyage regions**. After alignment and seam repair, the square remains intended for a 3 × 3 region grid. Actual native dimensions are recorded in per-image receipts; no native 4K or exact boundary-registration claim.

## Shared visual interpretation

The settlement immediately beyond the southwest/southern city wall is Greyfield: cramped patched timber/plaster houses, irregular tiny roofs, muddy lanes and lean-tos, without villa plots. Poor residents remain ordinary people. Distant Brookmeadow, Pebbletown and coastal/island villages are separate, reasonably maintained rural communities, not extensions of the slum.

Inside the city, northern civic/noble blocks use refined pale masonry, gardens and slate/blue roofs; commerce uses varied gables/awnings and dense market lanes; artisans use brick, tiled workshops and little work yards; ordinary residences use simpler roofs/courtyards. Four academies retain their familiar relative sites and colors. This is art direction within existing neighborhoods, not new faction/lore canon.

Preserve tiny regional building scale, thin unpaved country tracks, mostly empty mountain slopes and substantial quiet forest. Any new trail/shore clue stays inconspicuous. No full-map attraction list, giant cave/cabin icons or repeated ruins. Refinement adds shape, materials and local character rather than enlarging structures.

## Shared source geography

The original splits have no overlap. Extend them using the full 1254 × 1254 sparse master:

| Panel | Source bounds: left, top, right, bottom |
| --- | --- |
| Northwest | 0, 0, 720, 720 |
| Northeast | 534, 0, 1254, 720 |
| Southwest | 0, 534, 720, 1254 |
| Southeast | 534, 534, 1254, 1254 |

Every crop is 720 × 720. Adjacent crops share **186 source pixels**, about 26% of a panel, including a central four-way overlap. The extended crop is the composition target. The lower panels also use the full master and earlier tight-quadrant refinements as references. Full-map context initially caused the two upper panels to pull the camera back; those drafts were rejected and replaced with single-crop-reference generations. Final upper panels keep the partial city and the intended crop. Exact successful prompts are in the current manifest; rejected versions remain in ignored local output.

Shared bands remain fully drawn: no transparent padding or baked fading. For equal-size native output N, the starting layer step is round(N × 534 / 720). Shared width is N minus that step. Use the generated Assembly Guide for measured dimensions and placement values. These offsets are only starting positions: image generation may shift geography. Align terrain and choose one coherent tree/building silhouette before masking; do not blend through doubled structures. The author will soft-erase or layer-mask seams, then slice the finished square into nine regions.

## Evidence, review and delivery

`tools/glowhaven-panel-art/jobs.json` contains the four current `ao1`–`ao4` prompts, references, crop bounds and supplied input hashes. Per-image receipts preserve native dimensions, SHA-256 and panel identity. Built-in image generation is used. `tools/glowhaven_overlap_art.py` checkpoints exact PNGs and packages them without changing their pixels. Input cropping only prepares overlapping reference images. The labeled contact sheet is a reduced review aid, not a stitched map.

The single ZIP retains exact panel names/order and includes an assembly guide. No canonical JSON, coordinates, public patch notes, hosted map or Studio publication changes belong to this task. Do not resume the cancelled alternate layout.

## Delivered and reviewed

Four final PNGs are **1254 × 1254** each, copied unchanged from the built-in generator. The ZIP integrity check passes and contains precisely those four PNGs plus the guide. A 2184 × 2184 starting canvas gives about **324 pixels of overlap** with layer origins NW (0,0), NE (930,0), SW (0,930), SE (930,930). A later 3 × 3 cut would initially yield 728-pixel tiles, subject to the author's final crop/alignment.

Visual review confirms repeated city/tree/shore/field geography and opaque shared bands, the circular wall, quiet western ridges, tiny roofs, dirt tracks, patched near-wall housing and a small offshore prison. The source is recognizable. Buildings, tree crowns and water details still vary between generations: masking whole structures and occasional local warping/painting will be needed. District differentiation is subtle at this map scale; no guarantee of exact plot-to-plot correspondence is made.

Current panels live in `world-draft/map-variations/Glowhaven Panel Refinement/Circular With Overlap/`. `output/glowhaven-panels-2026-11-03/` contains the ZIP, Assembly Guide, Panel Index and reduced labeled contact sheet. `tools/glowhaven-panel-art/delivery.json` records nominal geometry. Canonical SHA-256 remains `4da8e98a2202370e02255e2cae00d5f822b2d1054261a634ce33effb0391756c`. Sources and the original AGENTS.md remain untouched.
