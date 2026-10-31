# Alpha24 — Character Creation and Relationships

Merged the useful creation additions from GPT-Chat's world file.json onto the current Alpha23 world. The supplied file was an older branch: importing it wholesale would restore earlier quest triggers and public authoring language. Existing 205 NPCs and hosted portraits, 173 locations and coordinates, 480 abilities, 112 quests, 308 world triggers and fourteen starts remain exactly as Alpha23.

## Creation

- Eight ancestry choices: Human, Elf, Dwarf, Dragonkin, Fae, Beastfolk, Oni and Mixed Ancestry. No Orc, Gnome, Halfling or Tidefolk choice. Avianfolk is not a separate ancestry; bird features belong under Beastfolk. Oni use individually chosen humanlike faces and horns, without an invented homeland or obligatory monstrous body.
- Thirteen categories and 152 total traits: 107 additions, with existing trait grants retained. Affinities and starting studies remain separate. Optional personality categories remain, with arbitrary +1 temperament bonuses removed so personality is not a build tax.
- Every introductory study retains two named starter techniques. Time is absent from creation; Space affinity does not bypass Gravity preparation. New practical kits use existing items once. Current progression and later skill acquisition rules are unchanged.
- Removed Creator Overlay banners, version labels and source-only production prose. New public descriptions describe the actual choices. Relevant instructions are scoped to character background/opening tasks rather than copied into every AI task.

## Relationships

The pasted NPC Updates section matched the current one. Its normal loss bands were too small for the requested betrayal consequences. The new calibration is -15..-30 for knowingly violating an explicit exclusivity boundary before a confirmed affair, -30..-50 for confirmed cheating, -50..-80 for a sustained double life/repeated manipulation, and exceptional -80..-100 for compounded severe betrayal. Scores remain clamped to the existing -100..100 ladder. There is no new romance or jealousy meter.

Consequences can include breakup, declined intimacy, withdrawn personal favors, ended shared plans and an actual voluntary party departure. A high score or successful persuasion cannot force reconciliation. Gifts and repeated apologies do not erase the event. Each discovery is counted once; continuing hurt affects conduct rather than causing another penalty every turn. Only informed people react. An honest incompatibility discussion and a freely agreed open arrangement differ from concealed cheating; a monogamous partner may reject or leave an incompatible arrangement. No universal gossip, automatic assault or faction punishment is granted.

These numerical bands are AI update guidance, not a live-proven deterministic penalty. The community [NPC Updates reference](https://wiki.unofficial.voyage/ai/generateNPCUpdates) documents configurable relationship pacing; actual emitted deltas and remembered breakups need playtesting. The [trait reference](https://wiki.unofficial.voyage/mechanics/traits) documents separate public descriptions/narrative effects and earlier-category creation gates.

## Guild review correction

Both the supplied file and final merge contain a writer for all eleven alleged missing q20_offered_* flags in gh_guild_board.script. It builds them with storage['q20_offered_'+j.slug]=true. The source and candidate were separately executed for every job: each expected flag was written and the acceptance script produced acceptance. The tests used supplied badge/status/action fixtures; they do not prove live recognition of a browsing request. Existing Alpha23 repeat-gate fixes remain intact.

## Validation and beta boundary

3109 local creation/reference/gate/size/preservation checks passed. Offer-writer fixtures and script compilations passed in both supplied (259) and merged (226) files. All nineteen standalone section maps match the complete export. No live Studio import, model evaluation, multiplayer playtest or existing-save migration occurred. This is beta preparation, not a claim that every gameplay loop is already tested.

Use a fresh character to test the creation flow, then play the guild board and one ordinary quest. Test betrayal with actual known exclusivity, discovery, a second unchanged turn, an apology and a genuinely new later event. The score should move once for the original discovery, while the person’s boundaries remain consequential.
