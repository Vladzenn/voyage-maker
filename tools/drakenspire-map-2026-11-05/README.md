# Drakenspire map and standalone prompt - 5 November 2026

Current canonical source: `world-draft/WorldAlpha - World.json`, SHA-256 `59483a52a9fb20f841300ed4db14615234d48fd0477e990712bc4093c588880c`. Read directly before the last map revision. There are 59 Drakenspire locations and 251 areas; the older 60-site catalogue is not the source. Dusklamp Quarter is absent in the current world.

## Deliverables

- `world-draft/maps/Drakenspire Highlands 2026-11-05/Drakenspire - High Stone City and Highlands.png`: native 1536 x 1024 built-in imagegen artwork, a proposal for review. Rotated fortress-left composition, dense compact stone town high on the mountain, fortress higher still, surrounding countryside below. Ardelis and Akitsuhara are actual image references; their geography and architecture are not copied.
- `world-draft/maps/Drakenspire Highlands 2026-11-05/Drakenspire - Landmark Locator.png`: 3420 x 1920 deterministic numbered overlay with a 59-name key. Its map panel is enlarged for annotation; enlargement adds no rendered detail. Markers preserve their artwork anchors through leaders if displaced for legibility. Proposed placements are not imported world coordinates.
- `world-draft/authoring/plans/Drakenspire - Standalone Fresh Map Prompt.pdf`: 43 pages; author brief/corrections, independent copy-ready prompt, actual art references, canon summary and current full public realm/region/location/area descriptions. No numerical location coordinates, old Drakenspire artwork or rejected drafts are embedded. Page images were rendered with bundled Poppler and visually checked; pypdf extraction verifies all 59 location names and 251 area names.
- `world-draft/authoring/plans/Drakenspire - Fresh Map Prompt and Canonical Reference.md`: editable canonical reference.
- `Standalone Prompt.txt`: plain-text copy-ready prompt.

## Provenance

`brief-input.json` preserves the author's brief, copy-ready prompt and built-in generation prompts. The first two images reused the old composition and were explicitly rejected. A new composition was subsequently requested, followed by the high-elevation/density correction. The former images remain only in ignored working storage/generated-image history, not deliverables. The user explicitly requested deletion of the custom `build-voyage-maps` skill; the exact local directory was deleted. It was not applied to the fresh takes.

`canonical-descriptions.json` contains only current public source descriptions and their exact names, without original coordinates, hiddenInfo, scripts or image URLs. `manifest.json` records selected files, native dimensions, hashes and art references. `suggested-placements.json` and CSV cover all 59 locations with image-relative top-left percentages and interpretation notes. Major silhouettes are identifiable; small shop roofs and several remote terrain anchors remain visual proposals. No exact lore-to-roof recognition claim is made.

`build_pdf.py` uses the bundled runtime's ReportLab/Pillow/pypdf. `build_locator.py` uses Pillow to place exact text and markers over the selected base without asking a model to redraw it. `pdf-verification.json` records name coverage, page count and source/PDF hashes.

No world JSON, coordinates, hosted image URL, source reference, Spider content or Studio state was edited. No live Studio validation or playtest is claimed. Public artwork notes describe a preview only.
