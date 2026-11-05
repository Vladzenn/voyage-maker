# Ardelis capital implementation

Completed local build on 5 November 2026. The actual delivery status and later edits live in `docs/CURRENT_STATE.md`.

The approved merge base is the canonical Rebirth world from `eda234f`, raw SHA-256 `77d47b4384db822c6021fb5c9ef29bde3daabfb557bf948b62f2a3bd3ccf8b59`. The supplied Locations section preserves all 307 old locations and adds eighteen unfinished pins. `source.json` retains those complete incoming records and the twelve author-supplied map regions, including exact images, crops, grid coordinates and original names. The grid is four columns by three rows. `placements.json` and its CSV distinguish preserved pins from sixty-six new approximate placements.

The final expansion contains 115 NPC cards (twenty-three new principals), 84 locations, 64 native quests, eleven factions, 24 items, twenty techniques, 27 type definitions, one developing arc and four beginnings. The capital's supporting cast includes workers, households, nobles, performers and serious adventurers. Ordinary church, paladins, household guards, the independent criminal group and the splinter cult have different interests and knowledge. Rebirth continues through Noelle and her command apparatus. The separate palace descent and sewer site remain optional. The earlier port proposal and Glowhaven academy expeditions are excluded.

## Files and rebuild boundaries

- `build.py`: guarded historical builder. It accepts only the verified original Rebirth base and refuses to overwrite a newer canonical world. After installation, do not reset the current world merely to rerun this builder. Future edits must use the then-current canonical world or a newly supplied Studio export.
- `review.json` / `previous_world.cjs`: exact reversible preservation manifest and historical test projection. Original reference fingerprints are not weakened.
- `major-people.jsonl`, `paladins.jsonl`, `people.txt`, `locations.txt`, `quests.txt`: reviewed authoring seeds, separate from the native output schema.
- `portrait-jobs.json`, `portrait-revisions.json`, `location-jobs.json`, `art-directions.txt`: saved built-in image-generation prompts. Final Noelle and Vladimir requests supersede their earlier drafts. No unrequested portrait rerolls.
- `portrait-files.json`, `location-files.json`: exact selected filenames and byte hashes. Twenty-four portraits and eighty-six scenes; no discarded portrait draft is packaged.
- `upload_art.py`: reviewed official upload sequence, resumable by target/name/hash. Credential comes from process environment only. It never writes Studio world data. `watch_uploads.py` picks up newly saved scenes without parallel receipt writers.
- `upload-receipts.json`, `portrait-urls.json`, `location-urls.json`, `area-urls.json`: successful official hosted URLs, with no API key or signed direct-upload URL. Exact rejected image moderation is not blindly retried.
- `verify_art.py --complete`: checks all twenty-four portrait and eighty-six scene assignments against actual PNG bytes and the candidate world; emits `art-verification.json`.
- `remote_validate.py`: reads the live official contract and sends only the draft candidate to `/validate`. `official-validation.json` identifies the exact full-file SHA and response. This is not a Studio save or publication.
- `landmarks.py`: regenerates the map handoff and complete placement CSV from actual records.
- `delivery.py`: packages the reviewed full world, guides and selected artwork in ignored `output/ardelis-2026-11-05/`.

## Mechanics and verification

Ordinary undertakings use typed native completion conditions and one reward owner. The local guild has one semantic board request check and offers one planned eligible job per actual request; it never automatically accepts a notice. Restricted key issuance verifies the actual recipient. Transit preserves existing route/anomaly behavior and fixed keyless return. The palace gate uses a narrow planning guard plus state backstop, with native semantic completion recognizing an actual feasible technical solution. These checks are not a state machine for every conversation.

`node tools/test_ardelis.cjs` executes real emitted scripts with supplied semantic answers. All historical behavior suites continue through exact reviewed projections. Local tests verify configuration and selected logic, not live AI interpretation, combat timing, multiplayer or Studio crop previews. The development notes contain the release playtest checklist. The final candidate passed official draft validation with zero errors and warnings.

The item catalogue remains close to its 250,000-unit cap. Do not expand it by copying verbose policy into every item. The historical worst-scene trigger budget reaches the documented limit; there is no claim of spare live scheduling capacity.
