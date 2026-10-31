# Alpha 17 — Ability Batch 1: Arcane and Guarded Combat

Implemented 18 Arcane spells and 8 purely physical guarded techniques. One entry, Arcane Stitch, already existed and is preserved exactly;25 records are new. The full world now contains 35 abilities. Existing spells, NPCs, portraits, maps, coordinates, quests, triggers, resource capacities and skill-acquisition settings are retained.

## More early and middle choices

The catalogue target expands from 12 to 18 spells per public discipline. Each ordinary discipline is planned around 5 introductory,6 trained,3 advanced,2 expert and 2 master techniques. This gives 11 spells below skill 40 and 14 by skill 59. The numbers are skill thresholds, not character levels. Space still needs its special preparation and Time has no public batch.

Twenty disciplines now account for 360 spells. Keeping 64 martial/tactical,40 mixed and 16 Magitech entries gives a flexible full-programme target of 480 abilities, including the original ten. This is a planning target, not 480 implemented records. Single-discipline batches avoid inflating a paired review into 36 spells at once.

## Starter grants and access

- Arcane Studies grants **Mana Knock** and **Halfmoon Pane**, alongside its existing Arcane Magic 3.
- Guarded Training grants **Doorholder** and **Measured Reprisal**, alongside its existing Guarded Combat 3.
- Other batch entries remain eligible choices through their exact native skill requirements; reaching a threshold does not automatically own them.
- The noncanonical Developer Playtest Kit includes every current authored ability once for inspection. It still grants no Time Magic.
- Character creation’s present study menu remains in place. No 1–3 affinity menu or teacher/book acquisition policy is activated in this update.

## Arcane repertoire

Rank 1–19: Mana Knock, Halfmoon Pane, Arcane Stitch, Glasshand Cradle, Prism Javelin.

Rank 20–39: Borrowed Stair, Rebound Seal, Counterweight Cuff, Lattice Snare, Hollow Knight, Orbit of Needles.

Rank 40–59: Hammerfall Diagram, Glassless Citadel, Twelvefold Procession.

Rank 60–79: Pressure Psalm, Severance Diagram.

Rank 80–100: Aegis of the Last Bell, Quiet Meridian.

The repertoire includes close pressure, interception, fine handling, rescue/load support, terrain supports, area control, directed constructs, breach work and major defense. It is not a numbered upgrade chain. Controlled force constructs use the caster’s attention and actions rather than inventing independent NPC turns or replacing Summoning.

Quiet Meridian is a modest master recovery action: exactly 5 Mana on actual uninterrupted completion, cooldown 10, no Mana or Stamina cost. It does not run alongside an attack, another spell or demanding exertion. Native passive uptake remains unchanged and is not duplicated. The effect’s spending/restoration behavior is AI-interpreted from its description and resource guidance; no new regeneration trigger or deterministic effect field was invented.

## Guarded repertoire

Doorholder, Measured Reprisal, Iron Hinge, Crossbar Catch, Shoulder Lantern, Low Roof Advance, Breakwater Turn and Shelter Behind Me.

All 8 require only Guarded Combat, through skill 35. They spend Stamina and require actual positioning/equipment where applicable; they do not spend Mana or require Spellcraft. Ordinary attacks, routine defense and normal movement stay free. Techniques provide deliberate positional choices rather than passive invulnerability or automatic counters.

## Research result

The documented schema has no per-skill teacher/book switch. Trait grants can introduce a discipline after a completed lesson. Spontaneous-learning coefficients are global, so turning them off affects all skills. As requested, current acquisition remains unchanged; the research note explains options for the later affinity-creation update and provides player-facing category copy. A category description is supported; a custom tooltip property is not documented.

## Verification

Passed 1,023 local structural/reference/preservation checks and 224 script checks/fixtures, including inherited dungeon/portal/guild cases, skill-threshold boundaries, starter eligibility, no Time leakage, developer repertoire and resource configuration. Existing ten abilities are unchanged. Native fields remain name, description, requirements, bonus and cooldown.

No live Studio import or combat balance test was performed. Targeting, duration, costs, restoration and tactical effects are described for the AI; native bonus and cooldown values are exact. Test a fresh Arcane student, a physical guarded build, an ordinary attack at zero Stamina, interception timing, construct action use and Quiet Meridian before expanding those patterns. Existing saves are not migrated by the full-world export.
