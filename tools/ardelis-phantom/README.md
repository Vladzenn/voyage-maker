# Ardelis local beginnings — private implementation record

Approved on 5 November 2026. This is a phantom patch: **no public patch notes**. It does not implement the separate comprehensive world-overhaul handoff or the deferred Gemini audit repairs.

## Merge base and preservation

The supplied complete Studio export, attachment `3d775af4-a56c-4c9b-b245-c9998b514342`, is authoritative. Its raw SHA-256 is `5ab7ae00b798f1be449821cd637447a93a68f63a4fcc2158db6949dbd2197630`.

Compared with the previous canonical world, the author changed the Elsewhere region/map and eight location records, uploaded the three missing courier/usher portraits, added a residential pin, added Portal Hall area artwork, and changed combat damage-type presentation. These edits are retained. `review.json` records only this patch relative to that export. `historical-review.json` also captures the incoming author changes so older exact-fingerprint fixtures can reconstruct their previous baseline without relaxing assertions. Neither projection edits the delivered world.

## Delivered content

- Six new native fish items: Crownwater Dace, Violetfin Perch, Terrace Trout, Goldscale Bream, Lanternbelly Smelt and rare Bellglass Carp. The catalogue is now 57 species. Both bait and lure tables use Ardelis code `i`; existing rows are unchanged. The carp uses the existing hook/land/release/failure/expiry flow. Reservoir/aqueduct habitat recognition was added to the three existing cast contexts. Actual reachable fish-bearing water remains a semantic eligibility requirement; a sealed conduit or ornamental basin is insufficient. Weather remains mechanical only in Glowhaven; Ardelis uses neutral local weather, with no dependency on Glowhaven weather storage.
- Three native story starts grouped after the four existing Ardelis starts: an adult junior noble at the Minazuki table, a novice Starward paladin, and an established homeowner. Each has an immediate situation, distinct social pressure and room to refuse or choose another direction. No automatic job acceptance, party recruitment, rank, ability, extra fortune or compulsory main-story knowledge is added. Existing starts retain their descriptions, prose, quest suggestions, items and relative order; their hidden guidance now explains local transit.
- The author's `residential area` pin is finished as Crownwater Row. Region, coordinates and radius remain exact. Number 14 has a sitting room, bedroom and small garden. The home start supplies one ordinary key-and-deed item; the completed purchase predates play. No additional sale, rent deduction, furnishing allowance or property state machine was added. The existing custom-property handover rule already excludes an individualized key/deed that has been recorded.
- One player-scoped semantic issuance trigger, `ar_local_key_issue`, at Caelrath Portal Hall. A genuine local connection established by a selected start or actual play permits a routine desk check and one held Ardelis Portal Key. Existing sponsorship remains another valid path. Requests for directions, invented claims, remote requests and another person's permission do not qualify. A held key blocks duplicate issuance. No campaign-wide flag can authorize an unrelated player through this route.
- Portal travel scripts are unchanged. Caelrath's fixed arch is already keyless toward Glowhaven; the issued Ardelis key permits the journey back. Original foreign sponsorship, the exact landing rooms, shared transit lock and Spider anomaly remain intact. The officer, hall and travel lore describe the two permission routes consistently.

## Rebuild, validation and delivery

`build.py --base <full-Studio-export>` applies only the approved patch. The first run records the prior canonical world as a reversible delta; later runs require the same reviewed output. Do not rerun old Ardelis or Universal Fishing builders directly over this patch. Future work must use the new canonical full world or a newer user export.

`python tools/project.py sync` updates the derived native sections. `python tools/project.py validate` checks local schema/reference/size rules. `node tools/test_ardelis_phantom.cjs` executes the real cast scripts with controlled RNG and supplied semantic outcomes, exercises the new carp lifecycle, verifies no species leaks into other realms and reconstructs the incoming export exactly. Older regression suites use the strict reversible projection; their exact baseline checks remain enabled. The normal project publish workflow includes this new focused suite.

Local structure validation passed **33,754 checks**; the focused suite passed **3,206 assertions**, and the previous Ardelis follow-up suite passed **427**. These are not live Studio validation or playtests. No Creator API credential is configured in this process; no official `/validate`, Studio save or Studio publication was performed for this patch. The final item collection uses **249,536 of 250,000 UTF-16 units**, leaving only 464; the next item expansion needs an explicit size-budget decision.

Full world and complete changed-section copies are in `output/ardelis-phantom-2026-11-05/`. `publish.py` invokes the normal checked publisher with task-scoped Git staging and no unrelated media ingestion. Untracked source references and the pending port proposal remain untouched.

## Live checks still needed

1. Start each new beginning. Confirm the native premise, personal choices, actual skills and lack of automatic quest/companion grants. Nina is a temporary delivery visitor, not permanently relocated.
2. As a native Ardelis starter, ask Akihisa for a return-route key before leaving. Cross to Glowhaven without any Glowhaven key, then return with the Ardelis key. A level-20+ first crossing may still encounter the deliberately preserved Spider anomaly.
3. Try the local desk with no established connection, while already holding the key, and with a second eligible or ineligible human player. Semantic verification and player identity remain engine responsibilities.
4. Fish at an accessible canal, reservoir, harbor and coast. Land/release/lose a Bellglass Carp. Sealed aqueduct interiors and decorative basins should not acquire fish merely because the classifier knows the word aqueduct.
5. In the home start, check that the key and deed exist once, no purchase is charged again and modest possessions are not turned into free luxury inventory.

The pre-existing shared simultaneous-angling limitation and narrative quest-resolution risks are unchanged. They belong to the separately reviewed audit, not an unrequested repair bundle here.
