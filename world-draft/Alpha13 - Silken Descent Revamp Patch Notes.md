# Alpha 13 — The Silken Descent Revamp

The Spider Realm is now a four-chamber dungeon across two vertically adjacent map regions. The safe threshold leads through a cold web gallery and flooded machinery before the matron's heated crucible. Lower rooms require earned connecting passages. A small route guard checks explicit destination requests before narration and verifies the resulting state afterward. Cleared routes remain usable for return visits.

## The four chambers

1. **Silken Portal Room — entrance.** A dry, sheltered threshold with cargo grooves, a cracked depth marker and a stable home arch. The room supports regrouping, observation and immediate retreat. Its arch is separate from the matron's experimental apparatus.
2. **Threadfall Galleries — first chamber.** A tension bridge over a dark drop, luminous fungus, a territorial Giant Spider and dry molting alcoves. Players may stabilize or cross the bridge, use a real movement technique, or negotiate the alcove detour. The dry survey shelf supports observation and rest after threats are handled. Shed shells and worn clips make the defenders' habits and the rigging below legible.
3. **Sunken Broodworks — second chamber.** Mineral pools, raised platforms, bronze winding gear and one Arachne broodwarden. The winch and Pattern Wall reveal a physical load-and-release mechanism. Players can fight, evade or credibly negotiate with the defender, then make the lattice passable through tools, learned magic, careful timing or another actual viable method. Examining symbols is useful evidence, not instant completion.
4. **Widow's Crucible — boss chamber.** Pillars, stone ribs, a weaving dais and warned ember vents provide meaningful positions. The real Vhalessra Veyrath intercepts outsiders with hostile intent. Strained anchor fittings corroborate the accidental transit snag; no new prophecy, stolen-soul device or deeper substitute boss is introduced.

Molting Warrens is now the first chamber's **Molting Alcoves** area. Silkbound Reliquary is folded into the second chamber's **Pattern Wall**, **Rest Ledge** and **Matron Gate**. This retains their exploration functions while removing two redundant map locations. The area graphs are connected and bidirectional.

## Progression mechanics

Three map rules keep the dungeon compact:

- The entrance and first-chamber pins become visible after entry. The two lower chambers remain hidden until their connecting challenges are actually resolved.
- Two passage triggers record the gallery crossing and the broodworks gate. Each accepts a real viable bypass as well as a direct solution. Neither requires a particular affinity, an enemy kill, a court report or an accepted investigation quest. Both remain open once earned.
- One route-guard implementation remembers the last valid chamber, greatest reached depth and first visits. A planning pass checks explicit map/travel requests and current position; a state pass catches a native travel update that arrives later. They share the same authored script and progress record. This addresses the previously observed turn-lag risk without duplicating a floor generator. The guard rejects an unresolved passage, a skipped first descent or an invented cave destination, restoring party placement and explaining the actual obstacle. A requested destination never counts as a room visit. No health, damage, loot or attack result is created. Reached rooms permit backtracking and revisits without replaying cleared challenges.

The finite Giant Spider and Arachne defender are introduced using the existing NPC types. Their actual generated identities and outcomes should persist. The authored queen remains a distinct NPC. The physical hazards matter even if a defender is avoided; no respawn loop is needed to pace the descent.

Passage success still uses Voyage's semantic evaluation of an actual resolved method. The guard itself uses mechanical location and stored-state checks. A map destination alone never sets a passage flag. This distinction is deliberate: the engine can enforce the route while allowing the player to solve an obstacle in several ways.

## What was preserved

The level-20-or-higher first ordinary crossing anomaly, one-time occurrence, manifested reusable key, free entrance return, optional investigation, cancelled field test and separate expedition assignment are unchanged. Vhalessra Veyrath retains her portrait, level 24, abilities, numeric tuning, hostile initial relationship and actual defeat state. Her evidence reference now points to the merged Pattern Wall.

The Alpha 12 native-health reward watcher is unchanged: actual defeat or genuine achieved surrender grants the exact **Matron's Anchor Sigil** once. The report remains separate. Ryūka Marufuji's later bazaar confrontation and continuation are unchanged. All other characters, hosted images, map coordinates, progression and unrelated quests/triggers are retained.

The world now has **130 NPCs, 173 locations, 707 areas, 9 regions and 127 general triggers**. Compared with Alpha 12, two redundant locations and three obsolete route triggers were removed; one lower region and two passes of the small route guard were added. The realm has fewer total triggers than before.

## Luxcellia comparison and research

Reference: the supplied **LuxcelliaUpdated.json**, especially the Riftmaw Floors 1–5 description, `delve_state`, `delve_advance`, and the dungeon narration instructions. Its useful patterns are a visible depth hierarchy, fixed landmarks, changing environmental character, remembered progress and correction when narrative/map position drifts.

There is an important distinction in that export: its Story instructions say **The Riftmaw Below has no DELVE lines** and is traveled by named regions/locations. The larger scripted DELVE framework also serves other dungeons. We therefore did not copy its whole procedural floor generator or assume every Riftmaw map pin was already mechanically locked. A four-chamber authored route needs far less machinery. No Luxcellia creatures, unique locations or lore were transplanted.

The official [Expanded Beta release](https://voyage.io/releases/expanded-beta) confirms map/discovery improvements, but does not specify a dungeon lock or tile importer contract. Detailed field behavior was checked against the community documentation:

- [Regions](https://wiki.unofficial.voyage/world/regions): square map cells, minimum 600 × 600, grid coordinates with positive y north.
- [Locations](https://wiki.unofficial.voyage/world/locations): hidden locations can be revealed through effects; descriptions and area paths do not establish a documented locked-door system by themselves.
- [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): typed placement, party movement, persistent state and planning-phase mechanical reactions.
- [Location settings](https://wiki.unofficial.voyage/other/locationSettings): region size is a shared world setting; edge feathering can be disabled for joined tiles.

These detailed references are **community-maintained documentation**. The local fixtures execute the configured scripts with simulated typed effects and supplied semantic judgments. They do not certify the live model or Studio importer. See the validation report and live checklist for the remaining tests.

## Map format, scale and import

The full art is exactly **627 × 1254 pixels**: one column, two rows of **627 × 627** squares. Each tile exceeds the documented 600-pixel minimum. The upper tile belongs to **Silken Chasm (0, 1)**; the lower tile belongs to **Silken Depths (0, 0)**. Top-to-bottom image rows correspond to decreasing region y. No blank spacer region is needed.

Upload the two provided square tiles to their respective regions, leaving crop centered at 100% and border feathering off. If Studio offers a full-map grid importer, use one column and two rows with the full PNG and verify its preview against these region assignments. We have not operated that live importer; the separate-tile method avoids relying on an undocumented slicing UI. Uploading the tall full PNG directly as one region image would crop it to a square. Local file paths are not hosted image URLs, so no fake path or base64 data was inserted into the world JSON.

The artwork is a zoomed cutaway. Its seam passes through the continuously connected upper portion of the flooded workshop, rather than implying a second physical entrance. Pins were aligned to the finished art; the room and its connected stairs remain one location even where the illustration crosses the cartographic seam.

Voyage's documented region size is shared across the world; no per-realm physical scale field was invented. This dungeon's canonical connections are short stairs and galleries, taking minutes of ordinary cleared travel. Map coordinates and any generated kilometre labels are diagram measurements here. Glowhaven's world scale is unchanged. Live testing must check both travel narration and any engine time advancement, since text guidance cannot redefine an undocumented engine distance calculation.

Generated art was resized proportionally to the exact requested dimensions and split into contiguous square crops. It contains no text, UI, pins or labels. The original generated image remains intact. The map manifest records dimensions, source and tile hashes. No images have been uploaded to Voyage by this task.

Use **GlowhavenAlpha13 - Silken Descent Revamp.json** as the full import, upload the region tiles in Studio, then start a fresh game. Existing saves are not migrated.
