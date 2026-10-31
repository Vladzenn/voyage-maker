# Current state

Updated 1 November 2026 during the desktop/cloud workflow pivot.

## Active world

The current full world is `world-draft/WorldAlpha - World.json`. It incorporates the user's latest Crime and Consequence export, followed by Curios, Scrolls and Gentler Adventures. Its cast includes the user's final portraits and voice settings for Ragnar Leonhart, Adoha Aonuma and Karia Morino. Ragnar is level **67**, not the older review card's 90.

Current content: 213 NPCs, 173 locations, 710 areas, 5 realms, 9 regions, 119 quests, 360 items, 510 abilities, 448 traits, 100 NPC types and 351 root triggers. Character cap 150; skill cap 100. The five resources are Health, Mana, Stamina, Renown and Infamy.

The latest item pass adds 300 items including thirty teaching scrolls, thirty scroll-only spells and their learned-formula traits. Twelve medicines have typed self-use effects. Successful study consumes one scroll; failed study and known formulas retain it. Research can compensate for low discipline proficiency, but casting still uses real skill, Mana, scope and cooldown. Space retains its Gravity 25 foundation; Time has no scroll.

The balance pass lowers generation bands at 58 locations and five regions, screens ordinary guild postings by the least experienced human participant, and gives beginner work weaker opponents. The Spider Realm's configuration and all authored NPCs are unchanged. The degree to which generated NPCs follow damage/tier guidance still needs live testing.

The previous local checks passed 11,937 structural assertions, 1,209 mechanics assertions and compilation of 164 scripts. These are historical local results, not live playtesting. Use the portable validation commands for the present checkout. The user's approved shortened questGenerationGuidance is now applied to the canonical world and its section export. Portable validation now includes its 5,000-character cap.

## Next major update: planning only

**Adventurers of Glowhaven** has not been implemented. Read its planning brief before proceeding. Confirmed scope:

- 14–18 new NPCs; proposed package sixteen, with independent identities beyond quest roles.
- Drakenspire arc: a martial party needs magical investigation of an intelligent snow spirit disturbing the outskirts. She rivals Orrum. Negotiation and fighting can resolve it. Orrum remains elusive and level 68.
- Asterveil arc: an adult fourth-year **Hydra Head** researcher seeks an actual near-mythical item; her theory is partly wrong. Shy, enthusiastic, poor in combat; Sucrose-like inspiration adapted to the setting.
- Asterveil comic opportunist party harasses adventurers and steals loot through actual resolved events. They are bullies, not secretly altruistic or automatically lethal villains.
- Midgame stories roughly levels 25–50. Native arcs need a pilot to verify surfacing, generated quest association and conclusions; do not invent an authored quest arcId.
- Cross-realm touring routines for Ragnar, Adoha and Karia. Adoha only visits Asterveil's settlement. No horse NPC for Ragnar. Pause schedules for scene presence, combat, party travel, incapacitation and commitments.
- Additional finite contracts in existing realms except the Silken Descent, a few new creature types, and broader starting equipment.

Other discussed features—public rumor delivery, property, full equipment refinement and formal companies—are proposals, not shipped systems or an instruction to bundle them automatically.

## Important ongoing limits

Do not claim the world is flawless or all quests work. Review recognition, reward recipients, consumption, travel placement and multiplayer in Voyage. Existing adventures may retain already-generated enemies and old data; fresh runs are the clearest balance comparison.

The repository and cloud environment status must be verified at the end of setup. Never equate a prepared Git repo with a completed Cloud environment.
