# Glowhaven — eastern ocean extension

Built-in image_gen output: **1079 × 1457 native pixels**, copied unchanged. Source master is the author's supplied `MasterMapOne_upscayl_2x_remacri.png`, **2896 × 2172**. The source is already user-upscaled; the generated panel is not described as native at the source height.

## Photoshop placement

The extension working area represents **1608 × 2172** source pixels: **1448 pixels of new ocean** plus **160 pixels of repeated left-edge terrain/water** for blending. New ocean is half the original map width. Intended final composition: **4344 × 2172**, equivalent to a 6-column × 3-row layout if the old map uses 4 × 3 square regions.

1. Expand the original canvas to 4344 × 2172, keeping the old map at (0,0).
2. Import the native ocean PNG as a separate layer. Match its height to 2172 in the working Photoshop document, with proportions locked; its width should be approximately 1608. This is a working-layer resize, not extra generated detail.
3. Start its top-left at **(2736,0)**. The first160 source-equivalent pixels overlap the master's last160 pixels.
4. Align the northern mountain/water transition, existing islet fragments, wave lines and lower coastal edge, then mask through the repeated strip. Generated geometry may shift locally; these are initial positions, not proof of a seamless join.

## Artwork brief

Open sea with scattered small islets/reefs, a few separate sea-monster sightings and one ornate blue/gold/ivory sailing-ship landmark. Existing colosseum is the scale reference: ship hull, monsters' visible portions and island structures remain modest at regional scale. Preserve the supplied western map, its Wraith Island and other established places. No extra city, duplicate skull island or new large eastern continent. No labels, pins, baked grid, fade or seam-hiding cloud bank.

Exact prompt and source/crop/output hashes: `tools/glowhaven-ocean-extension-2026-11-03.json`. World records, hosted map and coordinates remain unchanged. No live Studio upload or final six-region slicing was performed.
