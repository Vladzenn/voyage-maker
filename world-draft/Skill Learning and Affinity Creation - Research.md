# Learning Disciplines Through Study — Research and Creation Plan

Status: researched for the upcoming affinity-based creation update. Alpha 17 does not change spontaneous learning, add instruction triggers or replace the present Starting Magical Study menu.

## What the documented system supports

The documented skill record contains name, type, attribute, description and startingItems. There is no per-skill teacher/book requirement. A trait can add an absent skill and its starting level; a trigger can award that trait. The separate player-skill effect changes an already-owned skill rather than creating it. This gives us a supported instruction-grant pattern, with source/completion recognition still needing a real gate. [Skills](https://wiki.unofficial.voyage/mechanics/skills), [Traits](https://wiki.unofficial.voyage/mechanics/traits), [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)

Automatic acquisition is global: baseChanceToLearnNewSkill plus the relevant attribute times skillLearningBonusModifier. Setting both coefficients to zero stops that spontaneous route for all skills. newSkillGenerationEnabled instead controls invention of entirely new skill names; false does not stop learning an existing configured discipline. Our existing values remain 0.1 and 0.01, with generated skill names disabled. At attribute 10 this describes a 20% acquisition chance when the engine considers an absent skill attempted, not a guarantee about a particular scene. [Skill settings](https://wiki.unofficial.voyage/mechanics/skillSettings)

The character-creation category description is displayed above the choices, making it a supported information panel. maxSelections 3 enforces an upper bound of three, but the documented menu permits zero through that maximum and has no minSelections field. A strict minimum of one would need a separate validated creation/intro approach. Trait descriptions can explain individual choices. Do not invent a tooltip or requiresTeacher property. [Trait categories](https://wiki.unofficial.voyage/mechanics/traitCategories)

Official release material confirms creator-authored traits, resources, quests and triggers broadly; the detailed behavior above comes from the community-maintained schema reference, not an official guarantee of a dedicated school-learning feature. [Voyage release](https://voyage.io/releases/closed-beta)

## Recommended teaching flow

1. Establish the actual source: a qualified teacher, a usable book, an academy lesson or genuine independent study with appropriate material. Enrollment, carrying a closed book or meeting someone with an affinity is not completed instruction.
2. Resolve the learning activity at a scale that fits the discipline. A simple introduction can be short; a difficult school can need sustained work. Learning a prepared lesson is distinct from inventing a spell, so Spellcraft is not automatically a compulsory check on every known cast.
3. Award a one-time instruction trait through a supported player-scoped trigger after actual completion. Its skills modifier supplies the new discipline at the intended introductory level. Do not grant the same level bonus repeatedly, apply one person’s lesson to every co-player, or charge again merely for returning to class.
4. Let the character train the discipline and acquire its authored techniques through their normal requirements/ability points. Starting affinity traits can supply their initial discipline and starter spells directly. A trait that lists an ability grants it regardless of its ability prerequisites, so only intended starting moves belong on that trait.

This supports teachers, books and schools as different sources for the same discipline without writing a separate skill for each source. A story-recognition condition can allow flexible sources, while named lesson proofs or book items can make authored paths more inspectable. Neither a trigger nor a trait can independently verify that a fictional lesson really occurred; the chosen source/completion gate determines that part’s reliability.

## Two implementation choices for the creation update

| Approach | Benefit | Limit |
|---|---|---|
| Keep natural learning and guide magical instruction through AI plus lesson-grant traits | Ordinary skills can still emerge through play; less general-system work. | An unintended attempt can still be routed into a configured magic skill and acquire it. This is not a strict per-discipline lock. |
| Disable spontaneous acquisition globally and award absent skills through controlled trait grants | Removes that automatic acquisition path and makes skill entry depend on supported grants. | Also affects Medicine, Trade, weapon skills and every other skill. Those need legitimate learning routes too; this should be a deliberate whole-system decision. |

For strict instruction-based magical acquisition, the second pattern provides a firmer ownership boundary, but it still does not independently prevent every raw untrained attempt: Action Info must honor the character’s actual knowledge. Do not describe a trait gate as a native ban on any imaginable spell attempt. No global acquisition change is made in this batch.

## Proposed affinity information text

“Choose one to three affinities. Your affinities determine the magical disciplines you begin with and make those disciplines easier to study. You can learn other disciplines through books, study or mentorship.”

This is proposed player-facing copy, not a claim that affinity bonuses automatically change native XP rates. The category description can present it above the choices. Individual affinity traits would grant starting study and suitable basics; the final values and menu belong to the creation update.

Two existing rules need to survive that change. **Time is never an affinity or starting study. Space still requires Gravity preparation.** Because the current starting studies begin at 3 and the Space preparation benchmark is Gravity 25, a selectable Space affinity cannot silently grant novice Space proficiency while bypassing the parent rule. We should either exclude Space from ordinary starting choices or let that affinity begin on a Gravity foundation path. That choice remains part of the future creation design.

The one-to-three player choice is separate from the weighted 65/25/10 count used for newly generated NPC affinities. An affinity is not an exclusive spell list, does not imply an institution and does not automatically confer advanced power. Nonmagical and hybrid play remain supported.

## Live checks when implemented

An untrained character asks to cast an unfamiliar element without a source; instruction should not be silently invented. Another character actually completes a teacher’s lesson or studies a suitable book; the correct player should receive the discipline once. A co-player watching should not receive the same grant automatically. Repeated class attendance should train normally, not keep reapplying a level bonus. Test Time exclusion, Space preparation, the exact creation menu and whether minimum selection is enforced as intended. None of these new acquisition paths has been implemented or playtested in Alpha 17.
