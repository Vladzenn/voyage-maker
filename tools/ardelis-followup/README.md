# Ardelis complete-cast follow-up

Build on canonical commit `1b42222`. The original Ardelis builder and one-time naming/story/section migrations are historical; never rerun them against the completed world. Current deliverables and review status are in `docs/CURRENT_STATE.md`.

`review.json` reverses this exact delta for historical regressions. `section-merge.json` binds the latest complete Studio Locations/Regions exports to normalized section hashes. `names.txt` records 108 approved character renames; Noelle and Elven names are retained. `placements.json` and its CSV now reflect author-corrected pins.

`portrait-jobs.json` records the supporting cast's once-drawn compatible poses and prompts. `portrait-files.json` selects one PNG per NPC. Replacement metadata records explicit authorization and the superseded selection; a later screenshot identifying Kaede is not a second replacement request. Jōji's original remains selected. Writes to the selection ledger use an exclusive lock and atomic replacement so overlapping generation/replacement saves cannot lose another selection.

`watch_uploads.py --once` uploads only a selected name/hash that lacks a matching official receipt. Supply `VOYAGE_CREATOR_API_KEY` through the process environment, never a source file. The uploader resumes successful stages by content hash. It does not save or publish a Studio world. A rejected exact image is not blindly resubmitted; generation of a new replacement requires the author's approval. No watcher remains running after completion.

`python tools/ardelis-followup/deliver.py` verifies exact selected file/hash/target/URL assignments, applies the approved URLs to the current world, refreshes the reversible proof and creates the complete world, complete section exports and selected-art ZIPs under ignored `output/ardelis-followup-2026-11-05/`. `--contact-sheets` adds QA thumbnails under ignored `tmp/`; it never modifies selected images. Never supply a partial additions file as an entire Studio section.

`remote_validate.py` reads the current official contract and submits the exact current full world to draft validation only. Its receipt binds the response to the full file hash. This does not prove a live Studio save, runtime semantic accuracy or multiplayer scheduling.

Run the normal sync/validate and behavior suites. `test_ardelis_followup.cjs` covers the approved progression changes. `audit_snapshot.cjs` is read-only diagnostic evidence for the separate Gemini review; its defects are deliberately not repaired in this update. Encounter guidance and the travel toggle remain unchanged.

`publish.py` runs the existing project publisher with task-only staging/media selection, preserving unrelated untracked reference/port work. It includes every normal publish check and never force-pushes. Credentials and superseded media stay out of Git.
