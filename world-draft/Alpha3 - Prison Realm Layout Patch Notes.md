# Alpha3 — Prison Realm Layout Fix

2026-10-27

Built from the supplied GlowhavenAlpha3.json, preserving its current NPCs, images, visibility settings, and unrelated world content.

## Correct structure

- Glowhaven City realm → Glowhaven City region → Wraith Island location.
- Wraith Island Prison realm → Wraith Island Custody District region → 14 distinct prison-facility locations.
- No location named Wraith Island Prison remains.

The exterior Skullshore Landing is restored beneath Wraith Island, along with the ledge and island track. Its original coordinates (42, 27) and initially unknown status are retained. Mirei Shiozaki remains there.

## Circular facility placement

The 14 location centers are evenly distributed around a circle centered at (0, 0), radius 1.5. Each location radius is 0.2, so the circles do not overlap. Coordinates are a provisional arrangement for the user to place against the planned map; no new map artwork was generated.

| Location | X | Y | Internal areas |
| --- | ---: | ---: | ---: |
| Prison Landing | 0.0 | -1.5 | 3 |
| Intake and Property Office | 0.651 | -1.351 | 3 |
| Prison Records Office | 1.173 | -0.935 | 3 |
| Holding Cells | 1.462 | -0.334 | 3 |
| High-Security Cellblock | 1.462 | 0.334 | 3 |
| Prison Work Yard | 1.173 | 0.935 | 3 |
| Prison Stores | 0.651 | 1.351 | 3 |
| Prison Infirmary | 0.0 | 1.5 | 3 |
| Prison Visiting Hall | -0.651 | 1.351 | 3 |
| Prison Mess Hall | -1.173 | 0.935 | 3 |
| Prison Exercise Yard | -1.462 | 0.334 | 3 |
| Prison Security Headquarters | -1.462 | -0.334 | 3 |
| Prison Watchtowers | -1.173 | -0.935 | 3 |
| Prison Sea Wall | -0.651 | -1.351 | 3 |

## Connected references

- Akira Oritsu now starts at Prison Work Yard → Muster Point. All other NPC fields and all other NPC records match Alpha3.
- The two prison quests and their offer/completion gates target Prison Work Yard and Prison Records Office.
- Inbound travel targets Prison Landing → Arrival Quay. Lawful departure and escape return to Wraith Island → Skullshore Landing in Glowhaven.
- Realm-wide discovery, worker classification, and escape checks now use the prison realm instead of the deleted placeholder location.
- Intake targets Intake and Property Office; departure targets Prison Landing.
- Location-generation guidance preserves distinct facilities and prevents recreating a location named Wraith Island Prison.
- Area paths stay inside their own facility. Travel between facilities remains location travel, with access restrictions described in the records.
- Facility locations start known within the initially unknown prison realm. Visibility is not permission to enter restricted sections.

## Preservation and checks

All 128 NPC identities and portraits, the nine-known/119-undiscovered journal policy, and all 267 URL fields in the supplied Alpha3 export are preserved. Unrelated locations, game modes, items, character systems, and other world sections are unchanged. The source file in Downloads was not edited. The current standalone NPC, location, lore, and game-mode sections match the saved full export.

Local checks passed: 2,677 assertions covering parenting, names, NPC placements, quest/trigger destinations, original-data preservation, internal paths, text sizes, circular spacing, and source-file preservation. No live Voyage import, full codec validation, or gameplay test was performed.

The world now contains 81 locations and 313 areas, with the same 128 NPCs, 41 lore entries, and 22 quests.

[Full fixed export](GlowhavenAlpha3%20-%20Prison%20Realm%20Fixed.json)
