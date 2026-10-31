# Alpha 16 — Magic Foundation and Cast Fixes

This full world merges the latest user export with the approved magic foundation and cast corrections. It preserves all 16 user-edited paths: uploaded court/clerk/rival portraits, two Silken region map images and four coordinates for two mountain landmarks. The adapted lawyer retains the exact uploaded portrait URL. No existing hosted images were regenerated or overwritten.

## Magic foundation

- Expanded all established discipline descriptions with scope, practical applications, mastery and meaningful boundaries. Added Space, Soul and reserved Time as configured skills. There are 20 public disciplines, one reserved discipline and 45 total skills.
- Logic: Arcane, Metal, Gravity, Enchantment, Space. Passion: Fire, Lightning, Earth, Wind, Water. Empathy: Healing, Nature, Light, Summoning, Soul. Intuition: Divination, Void, Illusion, Ice, Sound. Reserved Time uses Logic. Capability does not imply a personality or morality.
- Ice/Water, Metal/Earth and Sound/Wind are historical relationships without parent-study requirements. Space requires Gravity preparation; Time requires exceptional Space/Spellcraft preparation and an actual rare source. Initial design benchmarks are Gravity 25 before Space, and Space 75/Spellcraft 80 before Time. These numbers are calibration choices, not new user declarations or native skill-prerequisite fields.
- Time is never an affinity, including for oracles; it has no creation study, ordinary teacher/manual seed, public ability batch or automatic developer grant. No unsupported hidden flag was invented. Restricting learning in play is still AI-dependent.
- Merged Artifice into **Magitech** and migrated skill references. It covers equipment, foci, circuits, devices and magical-mechanical engineering. It is not an affinity.
- Spellcraft is explicitly mandatory for spell invention or substantial blueprint redesign. Known casting uses its discipline; ordinary martial techniques do not require Spellcraft. Simple experimentation and difficult research have different scales. A startup foundation trait fills missing Spellcraft at level 0 without raising trained levels or supplying a magical discipline.
- Soul includes exorcism, spirits and spell-specific necromancy. Each spell distinguishes animated remains from conscious spirits. Raising undead is not automatically resurrection or vital-mana extraction.
- Temporary conjured matter fades; real material altered or processed can remain changed. No permanent conjured bullion, food or factory stock.

## Resources and existing abilities

Renamed resource keys/names to **Health** and **Mana**, migrating item bonuses, traits, trigger scripts and explanatory text. Added **Stamina**: start 60, +2 capacity per level, native recovery 1 per turn, full restoration on a real rest. Ordinary attacks, routine defense and normal movement stay free. Demanding physical techniques use Stamina; pure spells have no automatic Stamina fee. Zero Stamina does not cause unconsciousness or disable ordinary defense.

The six existing hybrids explicitly cost 4 Stamina alongside their existing 6 Mana. Existing bonuses, requirements and individual cooldowns are unchanged. Generated personal abilities now use cooldown 4, as requested; a matching design calibration changes their default bonus 10→5. This is distinct from each authored entry’s own values. Resource costs remain supported prose-guided behavior rather than new cost fields or dozens of semantic triggers.

The world still contains **ten authored abilities**. The separate 360-ability proposal includes those ten and approximately 350 new entries, divided into 17 review batches. No spell batch was imported in advance of review and no evolution tree was added.

## Spider court and lawyer

- **Vhalessra Veyrath → Vhalessra**, including exact NPC keys, trigger selectors, scripts, lore and quest references. Level 45, hostility, existing portrait and one-time trophy flow are retained.
- **Khessik Threadwarden → Kharvess**: adult female arachne spear bodyguard, Nature affinity, level 30. Explicitly hostile to humanoid intruders and the player’s traveling party; initial relationship−80.
- **Orruk Cindershell → Orrhask**: revised to an adult male arachne staff-caster, age 47, Fire affinity, level 28. He is sapient and carries a coalwood staff with red mana-bearing amber. Explicit hostility and initial relationship−80. His former ordinary-spider design is superseded.
- All three are authored NPCs in **Widow’s Crucible — Outer Ring**, the shared boss encounter area. The first-entry trigger still brings all three into the actual party area. They have separate health and actions, preserve real defeats and allow actual surrender/retreat rather than mandatory cleanup kills. Ordinary dungeon packs remain type-based requests.
- Generated two final arachne portraits. Orrhask received one replacement pass after the user changed his species presentation. The PNGs await manual upload; existing portrait URLs are preserved.
- **Phoenix Wright → Ryōichi Naruse**: a Glowhaven advocate and Phoenix Wing Academy graduate. The public visual description is a natural account of his hair, eyes and cobalt court clothing; it contains no explicit crossover identification. The uploaded portrait remains unchanged.
- Removed **Dusklamp Quarter** and its four areas from Drakenspire, and removed the remaining adult-nightlife-district sentence. No replacement location was invented. All other map pins and images remain as supplied.

## Validation and limits

Passed 8,439 local structural/reference/size/preservation checks and 181 script checks/fixtures. The latter include inherited portal, dungeon, guild and trophy cases, plus resource rename, startup Spellcraft, named-identity cleanup and shared hostile arachne placement. All configured scripts compile.

No live Studio import, balance test or generated-invention playtest has been performed. Time and invention gates are AI guidance; the schema has no native per-skill lock or prerequisite. Normal pack hooks request runtime NPC generation rather than directly spawning a type. Private long-distance teleportation will need actual supported movement handling when its spell batch is reviewed. Existing saves are not migrated. Use a fresh game to test the full import.
