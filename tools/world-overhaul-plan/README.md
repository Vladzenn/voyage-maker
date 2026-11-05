# World overhaul planning artifacts

This is a planning-only delivery for the 5 November 2026 whole-world overhaul request. It does not modify the playable world.

The primary implementation handoff is `world-draft/authoring/plans/Glowhaven - World Overhaul Implementation Handoff.md`. Its PDF is the reading copy. The companion CSV files and baseline JSON make the scope resumable; inventory rows are pending, not completed editorial review. The ZIP in `output/glowhaven-world-overhaul-planning-2026-11-05/` bundles the handoff and companions.

`build.py` uses the bundled Python runtime with ReportLab and pypdf to create the PDF, bind the inventory to source hashes and package the deliverables. It deliberately refuses a different world hash or a coverage ledger with implementation progress. Create a new implementation baseline when the Studio merge base changes; preserve this historical plan. The script does not read sources/, attachments, authentication or unrelated projects.

`seed_ledgers.py` records the original proposed retcons and design assignments. It rewrites those planning CSVs and must not be run over ongoing implementation ledgers. Retcon and undertaking entries are proposals, not applied canon or native quest keys. Live cases begin untested. Relationship seeds are baseline facts that require verification against the implementation source.

Build commands, using the bundled runtime returned by load_workspace_dependencies:

```text
python tools/world-overhaul-plan/build.py
pdftoppm -r 110 -png "world-draft/authoring/plans/Glowhaven - World Overhaul Implementation Handoff.pdf" tmp/pdfs/world-overhaul-plan/final
```

QA includes PDF section coverage, a unique source pointer and matching hash for every coverage row, complete NPC/location/area/quest counts, package contents and a byte-identical canonical source. All final PDF pages were rendered and visually reviewed. The project publish command runs existing regression suites; none of this is a live Voyage playtest.
