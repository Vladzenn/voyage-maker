# Magic and Combat — Research Decisions

Reviewed on 2026-10-28 against our Alpha15 baseline, the latest user export, LuxcelliaUpdated.json and sources/ChikaraOld.json. Reference files remained read-only. This is a design and schema review, not a comparative combat playtest.

## What was already present

Our world had 42 skills, 18 magical disciplines and ten authored abilities. Spellcraft was already included at level 0 through each primary aptitude; Scholarly Practice added training. Its scope emphasized analysis and did not explicitly require its use for invention. The new foundation makes that requirement explicit and adds a zero-bonus startup trait as a fallback for custom creation and late joins. It teaches no discipline and preserves trained Spellcraft levels.

Artifice already covered most requested technical work. Renaming and expanding it to **Magitech** avoids dividing the same repair between overlapping skills. Space, Soul and reserved Time are new configured skills, making 45 skills after the rename. Skill and character level caps remain 100.

## Observed reference patterns

LuxcelliaUpdated contains 102 skills and 1,500 authored abilities. Its useful skill-writing pattern is a positive definition, concrete applications, boundaries and examples of increasingly demanding work. Our revised disciplines adapt that structure while preserving this setting’s different boundaries: Light is not Healing, Water has no blood or Ice control, Nature heals plants, and Soul now includes spell-specific necromancy.

Luxcellia’s Space collection has 21 entries. Its Waystep separates journey-scale travel from tactical displacement, requires a visited destination, limits passengers and identifies restrictions. Its recurring waystep_rules trigger emits a story instruction; it does not apply a typed location change. That is useful narrative guidance, not evidence of a deterministic teleportation implementation. We adapt the distinction and will require actual native destination updates when the travel-spell batch is implemented. We do not copy its blessing exceptions, unique abilities, universal dungeon prohibition or arbitrary failure destination.

Luxcellia also has 18 Soul entries and 16 Time entries. Their low starting thresholds and special traits do not fit the requested scarcity of Time here. Its evolution and blessing machinery is also outside our design: this catalogue uses independent spell designs. Chikara’s physical approaches and resource-limited combat techniques are useful models for making martial actions distinct; its numerous additional meters are unnecessary for the requested Health/Mana/Stamina system.

## Native data, AI guidance and limits

Official Voyage material establishes supported custom resources, persistent characters and trait/ability progression broadly. It does not document all details of custom spell creation. [Voyage release](https://voyage.io/releases/closed-beta)

The community reference documents a maximum 1,500 authored abilities, native prerequisite lists, exact check bonuses and individual cooldowns. Other effect details are interpreted from descriptions. Eligibility and ownership differ, and the personal learned-ability task produces new character abilities rather than handing out existing catalogue names. Those distinctions inform the library/invention split. [Abilities](https://wiki.unofficial.voyage/mechanics/abilities), [Learned abilities](https://wiki.unofficial.voyage/ai/generateLearnedAbilities)

The documented skill shape has no individual hidden or prerequisite field. Time is therefore configured but excluded from creation, ordinary trait grants, developer defaults and affinity generation. Its exceptional learning restriction is AI guidance, not a hard engine lock. The Space/Time numeric preparation benchmarks are also guidance until reviewed abilities receive native prerequisite entries. [Skills](https://wiki.unofficial.voyage/mechanics/skills)

Resource keys and names must match, so this is a migration to **Health** and **Mana**, not a display-only edit. Stamina uses the supported resource structure and native recharge. Usage instructions guide contextual spending; they do not make every described cost deterministic. [Resources](https://wiki.unofficial.voyage/mechanics/resourceSettings)

The current generated-ability setting couples reuse cooldown and acquisition spacing. It was 20 turns; the approved setting is 4. A design calibration also lowers the generated default bonus from +10 to +5, while existing authored bonuses stay +3. Individual future library entries can have their own reviewed values. [Combat settings](https://wiki.unofficial.voyage/mechanics/combatSettings)

## Spellcraft implementation

The intended flow is: describe a design → determine actual discipline knowledge and complexity → resolve Spellcraft → preserve a reproducible success or useful failed test → use the supported original-ability acquisition path if a distinct technique was established. Casting the learned design subsequently uses its discipline. A teacher’s existing blueprint and a cosmetic nickname do not become newly invented spells by definition.

Simple familiar-scale experimentation can complete in one scene. Difficult work needs proportionate research, materials, instruction and tests, without endless invented approvals after success. A novel spell must not require the rare Freeform gift; Freeform concerns devising a working live without a prepared blueprint. Martial invention uses martial practice. Magitech needs Spellcraft only for a new magical operation, not a mundane repair.

These changes guide Action Info and Learned Abilities at their relevant stages. They do not create a new engine callback that independently verifies every invention. A live test must confirm the correct check is requested and its actual result is honored. Automatic native skill learning remains a reason not to promise a perfect Time lock. [Skill settings](https://wiki.unofficial.voyage/mechanics/skillSettings)

## Martial and mixed play

Keep Force Combat, Finesse Combat and Guarded Combat. They cover delivery and trained method rather than forcing all swords through one attribute or making a brawler invest in an intellectual casting attribute for every hit. Remote spells use their discipline. Infused physical techniques can require both kinds of training while resolving one primary action.

Ordinary weapon attacks, routine guard and ordinary movement remain free. Demanding techniques spend Stamina; spells spend Mana; an explicitly demanding hybrid can spend both. The initial Stamina calibration is 60 starting capacity, +2 per level, +1 per tick and full restoration on a genuine rest. Zero Stamina permits routine action and retreat; it does not cause automatic injury, unconsciousness or helplessness. Those numbers are deliberately scarcer than the initial proposal, and still require combat testing.

The six existing hybrids now explicitly add 4 Stamina to their existing 6-Mana commitment. This implements the new meter without adding dozens of per-ability deduction triggers or charging basic physical attacks. Costs are interpreted from supported prose and must not be applied twice. No unsupported per-NPC skill or resource dictionaries were added.

## Focused live tests

Test a custom character with no primary aptitude and a late-joining player: Spellcraft should appear through startup without extra levels or a forced mage build. Test successful and failed simple invention, a difficult research project, ordinary known casting and a martial invention. Time requests must not generate a teacher, affinity, easy manual or skill award. Check that Space preparation is respected and that parent study is not imposed on Ice, Metal or Sound.

Check the three resource bars after full import. Use actual bandages, a hybrid attack, pure casting, a demanding nonmagical maneuver, routine defense at zero Stamina, passive recovery and completed rest. Verify no double costs or recovery. Existing saves are not migrated by importing this world.

Spatial travel, active Mana recovery, summons with independent actors and conjured-material persistence remain special review cases for their actual batches. No new travel spell, resource-regeneration ability or 360-entry library is implemented in this foundation pass.
