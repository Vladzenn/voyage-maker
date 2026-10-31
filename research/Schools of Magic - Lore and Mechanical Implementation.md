# Schools of Magic: Lore and Mechanical Implementation

Implementation date: 2026-10-27. Input: the user's latest full-world attachment and `Schools_of_Magic_Lore_Sheet_01_Revision_1_4.md`. The user's accompanying correction establishes Dragon Hoard's exploration-and-relics direction, superseding its pending status in the sheet. Questions and rejected proposals in that sheet remain questions and rejected proposals.

## What belongs in which system

| Rule | Implementation | Practical limit |
|---|---|---|
| Academy responsibilities and traditions | World Lore, faction descriptions, relevant existing locations, world background and AI tasks | These guide play; membership confers no new automatic public power. |
| Ordinary body casting, optional catalysts, personalized blueprints | Spellcraft and magical skill descriptions; existing study/kit descriptions; action and NPC guidance | Actual learning and a resolved check still matter. A tool alone grants no skill. |
| Bodily enhancement is Enchantment | Enchantment description and five targeted NPC consistency clarifications | No new affinity, numerical bonus, or power reduction. |
| Variable ambient uptake | A once-per-tick script emits a typed MP addition | One party-wide random amount of 1–3 MP, averaging the previous +2. This is a draft game calibration, not a newly asserted physical rate. |
| Rest restores usable MP more efficiently | Existing completed-rest restoration retained; clarified resource instructions | The game abstraction is a full usable pool on completed rest. No new meditation, species or environmental multiplier. |
| Consciousness at zero usable MP | Resource/death/action instructions and a fresh-zero reminder | The reminder cannot undo unrelated unconsciousness; it applies no damage, revival or free cast. |
| Extremely difficult last spell at zero | Action-generation instructions request an authoritative relevant-skill check | AI-dependent routing. No hardcoded DC, guaranteed success, negative casting MP or HP conversion. |
| Student expedition requirement | One optional-to-accept quest recording an actual authorized assignment | A party record of this assignment, not an individual graduation database or forced player enrollment. |
| Tournament external-reserve ban | Persistent active-duel flag and bounded start/stop scene records | Rule adjudication and evidence remain narrative; the flag is not a detector, item lock or automatic penalty. |
| Theoretical extraction, shock and mana medicines | Specific lore plus action, item, medical and memory guidance | No witnessed humanoid drain technique, soul resource, routine transfusion, new potion dose or invented clinical threshold. |

## Current technical evidence

**Official platform documentation:** Voyage describes custom resources, authored quests and triggers that react to state and change it. This supports using stateful mechanics for persistent consequences. It does not establish every JSON field or prove any particular implementation works. [Voyage Closed Beta](https://voyage.io/releases/closed-beta)

**Independent beta-schema reference:** The community resource guide documents native tick recharge, completed-rest restoration and usage instructions. Setting native MP recharge to zero avoids combining it with the new scripted recovery. HP settings and MP capacity/level gains remain unchanged. [Resources](https://wiki.unofficial.voyage/mechanics/resourceSettings)

The community trigger guide documents typed effects, semantic story gates, JavaScript `check`, persistent JSON `storage`, and conditional `skip`. The implementation reads state directly and keeps semantic decisions in declared conditions; script-side `check({type:'story'})` would only return text. Structural flags and quest status gate the expensive story checks. [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)

Quests use the current party layout and `status`. The new quest omits an automatic `completionCondition`; explicit objective and completion effects drive its sequence. Quest acceptance follows an actual player decision rather than arrival. [Quests](https://wiki.unofficial.voyage/world/quests)

The item guide describes equipment bonuses. A potion-shaped item with such a bonus is insufficient evidence of reliable once-on-consumption restoration. This update therefore establishes medicinal lore without inventing a stock potion, universal dose, price or claimed on-use implementation. Existing unrelated item bonuses were preserved. [Item Types](https://wiki.unofficial.voyage/world/itemTypes)

These are community schema claims, not official guarantees. Local tests exercise authored code and relationships; live Studio validation and gameplay remain separate evidence.

## What the supplied worlds contributed

All six supplied worlds were inspected for resource, script and quest patterns. Their content was kept read-only; their unique lore and characters were not copied. Their older top-level layout was not transplanted into the current world.

- **ChikaraOld:** Scripted technique/training entries demonstrate separating a persistent training record from the scene describing it. Its resource effects and objective-completion effects support the design pattern of explicit state changes. We use a small expedition ledger instead of reproducing its extensive training machinery.
- **Luxcellia:** Its passive-regeneration script, scripted chance-based systems and many quest-progress effects illustrate how resource math and continuing records can live outside ordinary narration. We borrow that separation of responsibility, not its cheat systems, numeric rewards or large trigger collection.
- **Larion:** Its numerous scripted encounters show that local situations can have durable progress. Their existence is an observed authoring pattern, not proof of current compatibility.
- **Konosuba:** Quest-progress effects and descriptive consumables illustrate that a readable item description and a reliable consumption implementation are different questions.
- **DnD and Overlord:** These offer different balances of narrated and scripted content; neither makes a new generic soul or medical subsystem necessary for Glowhaven.

Exact example paths and scan results are recorded in `world-draft/authoring/magic-lore-2026-10-27/reference-patterns.json`. String-match counts there are search evidence, not counts of validated mechanics.

## Persistent expedition flow

1. A player actually chooses an academy field assignment. The hidden authored quest becomes accepted.
2. The Great Sage or court actually authorizes its purpose, route/site, scope, supervision and participants. The authorization scene is recorded.
3. The actual team completes the authorized field task outside the city. The script checks the current location against the existing eligible exterior locations before awarding that objective.
4. A responsible office or supervisor receives the evidence and truthful debrief. The quest completes and records the result.

The stored record contains bounded scene text, ticks and field location. It does not automatically grant money, relic ownership, a political office, graduation, or credit to absent students. Private travel remains available. A teacher can prepare or request an expedition without silently acquiring the court's authority. The existing Genzō Iwakura fieldwork quest now respects this distinction when used as an academy assignment.

This draft tracks one expedition assignment per party. It does not implement repeatable assignment IDs, individual student transcripts, automatic authority revocation, schedules, or separate-party expeditions. Generated locations beyond the current exterior list need a deliberate extension to the location gate.

## Details deliberately left open

The sheet's unanswered questions do not become new laws: genetic formulas, exact capacity growth per cast, physiological thresholds, species recovery rates, catalyst attunement/contact requirements, a universal Freeform DC, potion regulation agencies and prices, treatment protocols, automatic relic ownership, named founder history, and a demonstrated monster soul-drain ability remain unestablished.

The existing +6 maximum MP per character level remains a game abstraction. It is not an implementation of the still-unspecified usage-driven growth curve. Likewise, 1–3 passive MP per tick preserves the old two-point mean without claiming that a story turn equals a fixed number of physical minutes.

## Verification and focused live checks

Local JSON, reference, size, preservation and script-fixture checks passed. Semantic decisions in the fixtures are supplied test inputs; they do not prove live AI understanding. No Studio import, full platform validator or live playtest was performed.

Useful first live checks are: ordinary body casting without the kit trait; a learned movement enchantment outside affinity; a zero-MP desperate spell producing the intended difficult check; rest versus ordinary dialogue; a tournament spectator versus an actual competitor; legal non-battery focus use; a stopped duel permitting emergency medicine; expedition refusal; a private walk; a full authorized expedition; and a nonparticipant receiving no educational credit. Also confirm the real runtime clamps recovery at maximum MP and observe regeneration's timing around a last spell.

Use a new test game for the updated definitions. An existing save may retain its earlier triggers, quest state and resource settings; this update does not claim an existing-save migration.
