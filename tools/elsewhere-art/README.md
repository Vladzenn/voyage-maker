# Elsewhere artwork and complete Rebirth announcement

The author requested a map and one scene for each of Vladimir's Elsewhere's eight destinations, plus portraits for the Ash-Cloaked Courier, Reed-Cloaked Courier and Brass Usher. They will upload the images manually. No world JSON, existing art URL or live Studio data is changed.

The author explicitly overrides the staged map skill: use built-in imagegen directly, with no black-and-white sketch/refinement sequence. The first rigid two-row map was rejected. The requested fresh second map uses the original Glowhaven map as an actual style-only reference; it freely rearranges the eight landmarks. It is the sole selected map; the first remains superseded under ignored tmp. No old-map geography is copied. Scene images reference the selected map's architecture and palettes, not its aerial camera. Portraits follow existing cards and one recorded compatible pose draw each.

`brief.json` records the exact world facts and unchanged canonical hash at task start. `prompts.json`, `map-revision.json` and `jobs.json` preserve image prompts. `save.py` saves each selected output once with actual PNG dimensions and hashes. The three portraits have no existing valid URL and receive one generation apiece.

`package.py` checks the twelve unique selected images and unchanged canonical bytes, creates a manual-upload archive, an exact-key upload CSV and optional visual-estimate pin coordinates. Those coordinates are proposals only; positive native y is north. The world remains on its existing coordinates until the author moves them.

`world-draft/Rebirth - Complete Update Patch Notes.md` covers implemented work after Universal Fishing commit `48445de`, including the full Rebirth/Shadowspire and Ardelis package. It excludes deferred port work, unimplemented Gemini audit proposals and an encounter rewrite. The public announcement assumes the author installs these manual images before posting it.

`publish.py` runs the existing checked project publisher with only this task's paths and twelve selected media, preserving unrelated reference and port files. It does not upload to Voyage.
