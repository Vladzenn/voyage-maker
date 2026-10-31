# Alpha 9 — Live Playtest Scenarios

These are tests to run in Voyage, not completed results. Local scripts and structural checks have already passed; narration, classification, engine matching and balance still need these fresh-game checks.

Use the same model and game mode for baseline/Alpha 9 comparisons. Repeat short tests in at least three fresh or safely branched runs. Keep the exact input, last narration, displayed realm/location/area, relevant inventory and observed outcome. A screenshot without the preceding input often cannot identify which step failed.

## First checks

| Scenario | Setup and input | Pass observation |
| --- | --- | --- |
| Import and preservation | Import the full Alpha 9 file. Inspect Drakenspire map markers and the newest portraits. | Markers, maps, crops and roster order match the author's latest export. No new schema error from the revised sections. |
| Sub-threshold normal crossing | Use a genuine issued Drakenspire key below player level 20, from Evertree Base - Portal Room. “I enter the Drakenspire portal.” | Location becomes Drakenspire Portals and area Drakenspire - Portal Room in the crossing turn. Prose describes the enclosed snowy-region receiving hall. |
| Ordinary return | At that receiving hall, “I go back through the Glowhaven arch.” | One return to Evertree Base - Portal Room, without demanding another key or approval. No extra outbound round trip. |
| Unauthorized crossing | With no issued destination key, ask about and then attempt an outbound crossing. | Asking does not travel. The attempt does not grant a key, invent authorization or bypass the arch. |
| One-time anomaly | At actual player level 20+, attempt the first eligible ordinary outbound crossing without accepting the briefing. Also test the level-100 developer start. | One interruption to Silken Portal Room. It does not depend on the examination quest or trigger a second time. |
| Immediate retreat | On first Silken arrival, decline deeper exploration and return at once. | The initial key/lead is issued once, free return works, and the investigation is not auto-accepted or completed. |
| Later ordinary travel | Cross outward again after returning from the anomaly. | Normal chosen destination. No repeated anomaly, key multiplication or reset investigation. |
| Expedition independence | Accept an authorized expedition, encounter the anomaly, return, then perform the actual expedition. | The field test is postponed independently. The real expedition retains authorization and can complete through its own objectives. |
| Ordinary NPC levels | At developer level 100, meet a genuinely new incidental worker in a safe market and receiving room. | Generated level follows the local band, not the developer's level. An authored Archon remains their authored level. |

## Travel and time

From a busy existing place, ask “What is the mountain mine called?” and describe following someone across the current courtyard. Neither should relocate the party across the map. Try a local invented camp or tower as scene detail; it should not become a remote authored landmark because the nouns overlap.

Then test positive cases: “I follow her through that doorway” when a real adjacent doorway has just been established, and an explicit journey to an existing named distant place. The safeguards should allow both. Record a blocked legitimate move as a failure too.

Have someone arrange a meeting tomorrow evening. Step outside and back inside. Briefly discuss the appointment. The present day/time should not jump to the appointment. Then explicitly spend several hours on safe work, and separately sleep for the night; each real span should be counted once. Verify actual resource restoration rather than relying on a sentence saying the character feels refreshed.

## Dialogue and relationships

Talk to three contrasting authored people: a vain person, a reserved professional and someone genuinely unkind. Ask one simple question, request a longer explanation, disagree, then decline an optional offer. Their voices and values should differ. A longer answer should be possible when requested; otherwise replies should not become speeches.

Ask a factual question the person can answer and one beyond their knowledge. The first should finish with a usable answer. The second should admit the limit without inventing lore or turning into a cryptic task. Repeat neither prompt immediately unless testing repetition deliberately.

After declining a meal, lesson or healer visit once, continue an ordinary chosen activity. New people should not form a chorus prescribing the same action. Introduce a real immediate danger separately; appropriate intervention should still occur.

Disclose a private fact in selected-NPC chat, then talk to an uninformed person. They should not know it without a real channel. Make an appointment or receive an offer in chat; verify it remains a promise/offer rather than a completed transfer, journey or recruitment.

A greeting, routine full-price purchase or repeated compliment should not award a large relationship increase. A meaningful appreciated act may cause a modest change for the person who experienced it. Professional trust should not silently become romance, consent or party membership. Test a genuinely hostile character too; charm should not erase their established motive in one exchange.

## Combat and practice

Arrange a controlled friendly spar with clear limits. Win one trial and lose another. Both should allow real technique and meaningful outcomes without a lethal attack invented by the intent generator. Separately initiate an actual hostile fight: restraint guidance must not erase the hostility or authoritative damage.

Have an ally defend a vulnerable companion against an enemy, then use a taunt against the enemy. Inspect who receives the protection and hostile pressure. Test striking an object with its owner nearby. The owner should not become the target merely because they were mentioned.

Use a physical projectile moved by magic and an elemental strike. Damage classification should follow the mechanism and actual configured types. Test an enemy trying to retreat; there should be a concrete attempt with a plausible route or cover, not repeated dialogue while they remain still. Success should remain resolvable.

Practise a real skill the player does not yet own through a meaningful drill or instruction. The action should reference that skill. Acquisition/XP can fail legitimately; substituting an unrelated owned skill is the failure being tested. Ordinary repeated bolts or wards should not each create an ability card. An actually earned distinct technique is a separate positive test.

## Craft, property and memory

Request a repair quote, decline it, then inspect inventory and money. No transaction should have occurred. Accept a finite repair and finish it successfully; it should end without a freshly invented defect or signature. Return later; the paid bill should remain paid.

Craft a feasible item with actual materials. Attempt to use its claimed tool bonus to craft an even stronger copy, then repeat. The process must respect existing quality limits rather than recursively inventing larger bonuses. Generated definitions should use the actual configured categories and slots. A critical should not invent a rarity system.

Loot a resolved recoverable container once, leave and return. Its contents should remain removed. Leave property on deposit or in custody and recover it under the actual terms; neither silent deletion nor a fresh generic replacement inventory is acceptable.

Continue long enough for a story-summary update. Check that current location, opening identity, generated service staff, learned secrets, closed debts, accepted permissions and genuine outstanding objectives survive. A plan should not become a completed journey after compression.

## Bodies, scenes and modes

Generate a dragonkin, a nonhumanoid creature and a character using an established real transformation. Check descriptions, interactions and any new portraits against current anatomy. A recalled familiar should remain the same individual. A temporary summon should not automatically join the permanent party.

Visit a quiet social place and choose to relax. It should be allowed to stay quiet. Visit a dangerous field site separately; danger should remain credible and proportionate. These are two positive cases, not a universal “no encounters” rule.

Try an academy start, a nonstudent start and Write Your Own. The opening should honor the selected premise, actual equipment and body, and stop before choosing the player's next act. Test at least one ordinary mode as well as developer inspection; high-stat testing alone cannot establish normal balance.

## Failure classification

| Observation | Inspect first |
| --- | --- |
| Correct prose, wrong displayed location | Action classification, current resolved movement, actual portal trigger and key state. |
| Correct position, wrong room description | Story context, area record and image prompt. |
| An old problem reopens after time passes | Memory summary, quest state and whether the original completion actually fired. |
| Wrong buff target or unexpected injury in sparring | Resolved action/intent target and combat-state entry, not only final narration. |
| A paid service creates another charge | Transfer scope and item/update history; preserve exact inputs. |
| A newly generated stranger is overleveled | Actual generated record, location and region bands; distinguish an authored existing NPC. |
| A new NPC duplicates someone | Both canonical keys, the introduction text and the identity resolution input. |
| A conditional reminder appears in dialogue | Story instruction handling leaked into fiction; this is a failure, not intended UI. |

Keep failed cases with the current complete world version. Do not immediately add one example to every prompt. Identify the owning step, make a scoped change, and rerun the failing case plus its legitimate positive counterpart.
