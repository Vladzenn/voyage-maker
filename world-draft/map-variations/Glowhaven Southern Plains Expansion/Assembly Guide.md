# Glowhaven — southern plains extension

Built-in image_gen output: **2060 × 763 native pixels**, copied without resampling, cropping or sharpening. Boundary source: the author's `MasterMapTwo_upscayl_2x_remacri.png`, 4344 × 2172. This source is already user-upscaled; the generated image is not native at that source width.

## Photoshop placement

The new southern area represents **4344 × 1448** source pixels, or height:width **1:3**. With **160 pixels of overlap above**, the full working panel represents **4344 × 1608**.

1. Extend the source canvas downward to **4344 × 3620**, keeping the current map at (0,0).
2. Import the native southern PNG on a separate layer, and match its width to **4344** with proportions locked. Its working height should be about **1608**. This layer resize adds no generated detail.
3. Start the panel at **(0,2012)**. Its top 160 source-equivalent pixels overlap the old map's last 160 rows (y2012–2172).
4. Register the western treeline/rocks, river, tracks/field edges and small northeast coastal corner, then mask through the shared top strip. The author explicitly permits repainting the overlap and clearing obstructing trees to connect the true northern road. Use that corrected road through the join. Generated fine geometry can differ; these are initial coordinates, not a claim of pixel-perfect alignment.

After assembly the six-column grid can extend to five rows of 724 × 724 source-pixel regions. No slicing or live grid update was applied.

## Art direction and scope

Mostly open plains and rural travel space, western forest continuing the old boundary, and coast only in a small northeastern corner. No sea along the southern edge or continuing down the eastern edge. Small rural settlements, manor/keep and incidental countryside structures use the existing colosseum as a scale ruler; tiny houses remain comparable to existing houses. After the scale correction the author requested an eastward river mouth at the small northeast coast, removal of the former southern river leg, and one small bridge where the corrected approach road crosses north of the village. The main road must visibly connect through the northern overlap; trees can be cleared there. Latest refinement: a small widening tidal estuary with shallows/sandbars/marsh at the river mouth, rural dirt-road treatment narrowing toward the southern exit, and bridge deck aligned with the north–south road across the east–west river.

Match the supplied light, palette, perspective and world scale. No new city or duplication of existing master landmarks. Exact prompt/references and measured file hashes are in `tools/glowhaven-south-extension-2026-11-03.json` and its prompt manifest.

The source file is untouched. Canonical world SHA-256 remains exact; no NPC/location records, coordinates, hosted map, upload or live Studio publication changed. Photoshop seam repair and later location lore are separate steps.
