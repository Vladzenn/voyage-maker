# Alpha 12 — Silken Boss Encounter and Victory Proof

The Silken Descent now recognizes the actual authored boss's defeat directly and grants **Matron's Anchor Sigil** through its item trigger. Vhalessra Veyrath intercepts intruders at the chamber entrance with hostile intent. This update preserves the rest of the world and leaves the broader dungeon traversal/challenge pass separate, as requested.

## What the playtest showed

- From the Portal Room, a find-and-kill request produced a generic arachne and a narrated death before the authored boss was present.
- A request for Widow's Crucible was routed to an invented Mineral Vein Arena. Vhalessra Veyrath appeared later, but greeted the party too passively.
- The log eventually reports the actual named NPC's combat defeat. It also repeatedly mixed death with continued breathing and further finishing blows.
- Taking the narrated fragment created **Silver-black Weave**. Asking the assistant to create the sigil later created **Silver-black Sigil**. Neither is the authored inventory identity the bazaar event checks.

Those are observed transcript facts. The transcript does not expose the saved trigger flags or full NPC state, so it cannot prove which old victory condition failed. In particular, the lack of a displayed Travel Update at the first Crucible scene suggests a location mismatch; it does not establish one conclusively.

## Why the previous implementation was fragile

The old item-add trigger already existed. Its upstream victory trigger required all of these: exact party location, a discovered boss journal entry, native boss health at zero, an unset resolution flag, and an AI judgment that the correct defeat happened there. A missed journal introduction, movement update or semantic judgment could therefore block a real combat result from ever reaching the reward.

The boss also started in the Weaving Dais area while a normal arrival entered the Outer Ring. A fixed NPC placed in another area could be omitted from the immediate scene. Her first-contact trigger then required a narrated introduction before marking her known, rather than arranging that introduction mechanically.

The earlier local fixtures supplied the correct location, known identity and successful semantic verdict. They tested the happy-path wiring, but did not establish reliable live identification or first-contact loading. The new cases explicitly remove those assumptions. This is an authoring/verification gap; more prose alone would not repair it.

## Encounter changes

- Vhalessra Veyrath begins at **Widow's Crucible - Outer Ring**. On the first actual chamber entry, her placement trigger brings the same authored NPC to the party's current area, reveals the encountered chamber and identifies her. Entering via another area also works.
- Her **-85** initial relationship is preserved. Her card and encounter instruction explicitly describe hostility to humanoid outsiders, the player and traveling companions. She threatens, blocks access and attempts restraint or attack if intruders press on. Damage still requires a resolved attack.
- A dead boss is not moved or revived. A resolved living boss is not reset into another first encounter. An earned truce or prior relationship is not overwritten.
- Local queen/matron references point to Vhalessra Veyrath. A scoped reminder rejects substitute queens, replacement chambers and the invented arena. This instruction does not teleport the player, reveal a secret by itself, kill anything or resolve intervening challenges.

## Victory and reward changes

- The native-defeat check runs mechanically after combat damage, without an exact party-location check, journal gate, quest-acceptance requirement or semantic death confirmation.
- The single reward watcher independently reads the named boss's live health as well as an already recorded genuine resolution. It does not need the upstream trigger to run first. Missing health is not treated as zero.
- A real native zero-health result grants **one Matron's Anchor Sigil per player** and records the resolution in the same reward operation. No corpse search, finishing blow, return trip or court report is required.
- Genuine living surrender/restraint remains a separate semantic route. It requires the actual boss in the current scene, alive and out of combat. A flattering sentence or a distant remembered conversation is insufficient.
- The issued flag prevents repeated drops, including after killing a surrendered queen, revisiting, selling or losing the proof. The watcher's polling may retry before resolution; the award itself occurs once. Its default effects are empty, so a skipped script grants nothing and can retry later.
- The persistent record captures the actual source, basis, tick and player names. It never awards victory for possessing a lookalike item or defeating a generated stand-in.
- Court reporting remains separate. The existing later **Ryūka Marufuji** confrontation checks the same authored proof and resolution flag. Reusable portal keys and return routes remain intact.

## Documentation basis and limits

The current [Unofficial Voyage Wiki trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents named NPC health checks, planning-phase reactions after combat, persistent storage, placement effects and exact-key item-add effects. It also documents that script skip preserves retry eligibility and that script errors can leave default effects unchanged. These are **community-maintained documentation**, not an official guarantee of every live-engine edge case.

The [NPC reference](https://wiki.unofficial.voyage/world/npcs) documents initialRelationship and authored placement. There is no documented hostile boolean or combat-start effect used here: hostility comes from the negative relationship and the NPC's actual behavior instructions.

Local structural checks and script simulations are recorded in the companion validation report. They simulate typed state and supply semantic surrender decisions. They do not execute Voyage's live model, import this file into Studio, or verify live turn scheduling/scene refresh. A fresh-game playtest must confirm those parts.

## Preservation and importing

Use **GlowhavenAlpha12 - Silken Boss Fix.json** as the full import. Its content matches **WorldAlpha - World.json**. All other NPCs, portrait URLs, other media, coordinate values, realm/region ordering, progression, academy subjects, Asterveil content, ordinary expedition quests and unrelated triggers are preserved. Four existing boss triggers were revised and one scoped reference reminder was added; there are still 130 NPCs and 175 locations, with 128 general triggers.

The broad Silken traversal/hazard design is still unfinished. The alias reminder prevents an invented route from becoming authored canon, but it does not create a complete traversal-check system.

Importing an updated world does not patch an already running saved game. For this particular run, a reliable repair would need the saved state to inspect the canonical boss record, inventory identities and stored victory flags. The transcript alone cannot establish them. Avoid treating a newly generated similarly named sigil as repaired state. Test the updated world in a fresh game first.
