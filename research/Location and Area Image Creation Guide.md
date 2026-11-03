# Voyage Location and Area Image Creation Guide

**Purpose:** Create a coherent visual world across Voyage locations while letting each place express its own purpose, mood, and social context. Use this guide to read a location, form an art direction, generate a small batch, and prepare files for Voyage Studio.

**Research checked:** 2026-10-26. Platform behavior below distinguishes official Voyage notes from the community-maintained Unofficial Voyage Wiki. The current Voyage Studio build remains the final check.

## 1. World art-style preset

### Shared visual language

Use polished **2D fantasy-anime environment illustration**: deliberate linework, stylized forms, painterly color and lighting, clear depth, and the finish of a high-fantasy JRPG background. The shared world should feel richly colored, medieval, magical, and full of wonder. Whimsy and visual surprise are welcome parts of the world language; local context decides how strongly they appear.

Use the NPC portrait guide for anime rendering, not portrait framing. Use the supplied Glowhaven city map as a reference for scale, saturation, grandeur, and readable architectural silhouettes. Its buildings are simple at map scale; in close environment images, give the focal space more useful detail, furnishing, and visual storytelling. Do not copy the map's geography, skyline, or lighting into unrelated scenes.

### Give each place a visual personality

Do not stop at naming a place type or mood. Build an image direction that says what makes this place feel like itself. Consider its purpose, social context, condition, and established identity, then deliberately choose:

- **Palette:** select a memorable local palette that belongs to the world. Avoid defaulting every building to pale stone and every interior to brown wood. A proposed palette is an art-direction choice, not canon, unless the user confirms it as a permanent identity.
- **Architecture and shape:** distinguish places through silhouette, layout, scale, materials, ornament, and how spaces connect. Shared world style should not make every school, palace, shop, or home look interchangeable.
- **Props and environmental storytelling:** give the scene several functional, readable prop clusters that show how people use it. A classroom might have open books, notes, a demonstration surface, and lesson tools; a shop should show the goods and work surfaces that make it recognizable; a quiet room should still feel furnished and used. Prefer a handful of purposeful details over empty rooms or random clutter.
- **Magic and whimsy:** treat everyday magic as part of the world's visual vocabulary when it fits. Small enchanted lights, subtly active objects, magical craft details, or playful spatial touches can make a scene feel wondrous without turning every image into a spell effect. Use a stronger display where the place's purpose invites it and less overt magic where the local context calls for restraint.
- **Atmosphere:** use color, light, wear, density, and activity to make a place cheerful, curious, solemn, melancholy, or tense. A sad or poor district can be less whimsical and less visibly magical while still belonging to the same saturated medieval-fantasy world.
- **Detail hierarchy:** use crisp, selective detail near the focal feature and simplify distant architecture. The map's low building detail is a scale choice, not a rule to make close interiors bare.

### Background life and recurring motifs

- Keep a named creature's changeable presence, sleeping state or combat state out of a static location shot unless explicitly requested. Show its habitat and durable traces; use its NPC portraits for the creature. Ordinary secondary wildlife and unnamed background people can still fit a place. Bluecoil Rest's empty resting reef is the approved example.
- Add a small number of scene-appropriate background people when the place would naturally be occupied. Make them read as ordinary users of that space and keep them visually secondary, with no prominent faces or named-character designs. Leave places empty when their description calls for solitude, abandonment, restricted access, or another condition that makes people inappropriate.
- Use established heraldry and recurring motifs selectively. When no heraldry is established, build identity through palette, architecture, props, and atmosphere instead of inventing a crest or covering the scene in banners.
- For repeated institutions or districts, prepare a short visual identity note before generating: core value or purpose, palette proposal, architectural character, characteristic props, and the level or behavior of visible magic. Use that note to keep images within one institution coherent and to make different institutions visibly distinct.

**Illustrative reads, not canon additions:** a potion shop in a magical city can feel whimsical through a lively palette, playful arrangement, useful shop goods, and a few subtle magical touches. A slum in that same city can feel sadder and less whimsical, with worn, crowded spaces and little visible magic, while retaining the world's saturated medieval-fantasy look. These examples describe ways to express mood; they do not establish features for a particular location.

### Facts, interpretation, and invention

Use three separate layers when planning an image:

1. **Scene facts:** exact names, layout, landmarks, materials, and activities come from the current location JSON and confirmed lore.
2. **Art direction:** infer a fitting palette, mood, architectural treatment, props, and level of ambient magic from the place's purpose and context. A short JSON description is a set of scene anchors, not a command to leave the image bare.
3. **New canon:** do not invent major landmarks, unique artifacts, official emblems, named characters, or plot-bearing magical effects. Ordinary functional props and subtle atmospheric magic may be proposed to make the place feel inhabited and wondrous. Treat an unconfirmed signature palette or motif as a visual proposal, not established lore.

Ask only when a missing choice would define the location's canon. Otherwise, make a clear, context-sensitive visual choice and keep it consistent within the image set.

## 2. Choose the right view

### Location image

Show the whole place's identity at a glance: its scale, overall silhouette, and one or two defining features supported by its description. Prefer a broad exterior for a location with several areas. For a single building or shop, choose a recognizable exterior or the main public interior. Make the place's context and mood legible without turning the image into a city map.

### Area image

Show one specific playable sub-location from its own description. Use a closer scene-level view with a different camera position and focal feature from the parent image. Carry the same world style and the parent's established architectural language, palette, and mood into the area, while letting the area description determine its own layout and focus.

### Interiors and small locations

Keep the same world style at every scale. For an interior, show a readable layout, purposeful furnishings, and prop clusters that communicate how the space is used. A minor location can have a simpler composition, but it should still have color, character, and lived-in detail. Scale changes the view and detail budget; it does not remove the world's visual identity or sense of wonder.

### Crop safety

The community reference says a location image may appear as both a tall arrival card and a wide banner in Map → Location. Keep the defining feature inside the central safe area and inspect available crop previews in Studio. The current community reference lists **600 × 600 pixels as the minimum** for uploaded location art and does not prescribe one universal aspect ratio. Compose for the actual previews rather than assuming a single target crop.

## 3. Prepare a visual read before writing prompts

For each image, briefly identify:

- **World baseline:** the shared 2D anime, colorful medieval high-fantasy language.
- **Place identity:** what makes this location distinct from similar places in the same world.
- **Place read:** what the location is for, its social context, condition, and tone.
- **Scene facts:** the exact features from the location or area description that must appear.
- **Treatment:** a deliberate palette, architecture, several purposeful props, background activity, and an appropriate level of whimsy or visible magic.
- **Composition:** location-wide or area-level view, camera angle, focal subject, and crop-safe placement.
- **Boundaries:** unsupported features to avoid and any open choice that would create new canon.

Proceed with a reasonable art-direction inference when it affects mood or presentation. Ask only when a missing choice would materially define the place or introduce new canon.

## 4. Prompt recipe

Write one concrete prompt per image. Lead with positive art direction and scene facts, then specify boundaries. Include:

1. Exact location or area name and image role.
2. The described focal feature and spatial layout.
3. The shared world style and this place's contextual mood.
4. Viewpoint, scale, light, palette, and level of architectural detail.
5. Crop safety and exclusions.

### Reusable prompt scaffold

~~~
Create a [location establishing shot / area environment view] for [exact name]. Show [scene facts and layout from the JSON] from [clear viewpoint and distance]. Use the project's polished 2D fantasy-anime style for a saturated, whimsical medieval high-fantasy world, with deliberate shapes, painterly color, and clear depth. Make this place distinct through [palette proposal, architectural character, purposeful props, and mood]. Include [several functional prop details] and [a few small, scene-appropriate background people / no people if solitude fits]. Use [subtle everyday magic / stronger magical atmosphere / little visible magic] according to the place's context. Keep [main focal feature] within the central crop-safe area. Use heraldry only if established and keep repeated motifs selective. Do not add unsupported major landmarks, unique artifacts, named characters, or plot-bearing magical effects. No readable text, lettering, labels, maps, logos, UI, signatures, or watermarks.
~~~

Fill in the palette, props, magic, and mood fields with concrete choices. Adapt the shared style to the place rather than pasting the same mood words into every prompt. Use specific scene details from the JSON and contextual props instead of generic quality adjectives.

## 5. Small-batch workflow and deliverables

1. Read the current location JSON, confirmed lore, portrait style guide, and relevant visual references. Treat files in sources/ as read-only.
2. Recommend one location image and two area images as a pilot. Confirm the exact keys before generation.
3. Generate a small batch with one prompt per distinct image. Keep parent and area compositions distinct.
4. Review the images side by side for style, scene accuracy, mood, crop safety, accidental text, and unsupported additions. Refine the shared art direction from the pilot before expanding.
5. Save each selected image separately in the project workspace. Keep a simple manifest mapping each filename to its exact location or area key, plus generation/review status and any crop notes.
6. Upload through Voyage Studio only when requested or otherwise authorized. Use the current model selector, choose the appropriate location or area image guidance, inspect crop previews, and retain the image URL provided by Voyage if editing JSON.
7. Never claim Studio accepted, saved, or previewed an image unless that actually happened. A generated preview alone does not confirm Studio upload.

## 6. Voyage Studio notes

These platform details are separate from the art direction above.

### Image fields and crop

The current community schema documents this establishing-shot shape for locations and areas:

~~~json
{
  "images": {
    "establishingShot": {
      "imageUrl": "Voyage-hosted image URL",
      "crop": {
        "focus": { "x": 50, "y": 50 },
        "zoom": 100
      }
    }
  }
}
~~~

This is a schema illustration, not a complete location record. Preserve the current record shape and use the URL Voyage provides after upload; do not invent an image host or an unverified field. If an establishing shot exists, its crop is required in the current community schema. Set crop values in Studio when possible.

### Model and image prompts

- **Official product note:** Voyage Patch 2.33.7 introduced a unified editor image-model selector for Creator Studio and the legacy editor, while retaining image-type prompt fields. The model list in that patch is historical; choose from the options currently shown in Studio.
- **Community schema:** the editor model selection is stored in imageModelSource and affects art generated while editing. In-game image generation is configured separately.
- Voyage's imagePromptConfiguration offers world-wide prompt additions for locations and areas. These guide images by type; they do not replace each location's or area's description. The guide is for the creator and assistant; Voyage's generator does not automatically read this Markdown file.
- The Unofficial Voyage Wiki locates these controls at Files → AI → Image Prompts and the editing model at Files → Other → Image Model. Check the live Studio labels if they have changed.

### Evidence and limits

- **Official:** [Voyage Patch 2.33.7 notes](https://voyage.io/whats-new/patch/patch%3A100000946) describe the unified image-model selector and image-type prompt fields.
- **Community schema:** the [Locations reference](https://wiki.unofficial.voyage/world/locations) documents location and area establishing shots, image generation, and crop behavior. [Image Prompts](https://wiki.unofficial.voyage/ai/imagePromptConfiguration) documents world-wide location and area prompt fields; [Image Model](https://wiki.unofficial.voyage/other/imageModelSource) describes editor-only model choice. The Wiki's [methodology](https://wiki.unofficial.voyage/appendix/methodology) explains its extraction and verification process and its non-official status.
- Composition, art direction, batch workflow, and review guidance in this file are project recommendations, not Voyage engine requirements.

## 7. Review checklist

- Does the image follow the shared world style while fitting this place's purpose and mood?
- Does it have a distinct palette, useful props, and visual identity rather than reading as a generic environment?
- Does its level of whimsy and visible magic fit the context without flattening the world's high-fantasy character?
- Do related institutions or areas feel coherent while remaining visually distinct from one another?
- Are the exact location or area features supported by the JSON and confirmed lore?
- Does the parent image establish the whole location and the area image focus on its own sub-location?
- Are scale and detail appropriate for a major landmark, interior, or minor location?
- Does the image communicate tone through color, light, shape, props, and condition without inventing canon?
- Are important features central and readable in the Voyage crop previews?
- If background figures are present, do they fit the place, stay visually secondary, and avoid introducing named or distinctive NPCs?
- Are banners and heraldry used selectively, without overwhelming the location's other visual features?
- Are readable text, logos, UI, signatures, and watermarks absent?
- If JSON was edited, does every image URL and crop use the current supported structure?

## Local references

- [NPC Portrait Creation Format](Portrait%20Creation%20Format.md) — rendering style for the project's anime art.
- [WorldAlpha - Locations.json](../world-draft/WorldAlpha%20-%20Locations.json) — current location and area descriptions.
- [World Lore Draft Notes](../world-draft/World%20Lore%20Draft%20Notes.md) — confirmed setting names and lore.

