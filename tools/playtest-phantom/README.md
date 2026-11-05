# Private playtest patch — 6 November

The canonical world contains this patch. [Copyable personal changelog](../../world-draft/Playtest%20Phantom%20-%20Personal%20Notes.md). No public patch number or announcement.

## Merge and scope

The official Alpha Creator API successfully downloaded the author's existing `0kL8UR7rgsu2` draft. It matches the current authored content, including the preceding NPC-conversation patch. Its additional native quest-progress handlers, party entities, compatibility revision and character-creation music are preserved as the fresh base. The API also normalizes object ordering; the semantic review is more useful than raw line counts.

`build.py` applies the approved creation, isekai, civilian-level, display and progression changes to that checkpoint. Do not use an old ignored checkpoint to overwrite subsequent Studio work. Read a fresh draft and reconcile first. `level-review.json` lists all 285 actual level reductions. The author explicitly rejected the provisional HP-only candidate. Eligible background civilian levels above six now use ceil(old level / 6), capped at eight; existing levels six or below stay intact. Original health multipliers, tiers, ability descriptions, personality, placement and portraits remain exact. Native HP and damage follow level, with ordinary difficulty scaling intact. Trained-role and major-character exclusions are applied first. New ordinary noncombatants generally use 1–6, exceptional civilian specialists 7–8; age and craft seniority do not set combat level.

## Native mechanics

Otherworld Rebirth grants Summoned one only to its actual holder through one player-scoped mechanical rule. It initializes an absent campaign at the actual tick, without resetting an existing campaign. The existing public delegation still requires a calm Glowhaven town scene after 100 ticks. Later interception and pursuit gates remain unchanged.

Quickened Chorus uses the native trait resource modifier `Resonance: -4`, reducing actual capacity to 16. One early-earn branch reaches the existing Resonant state; four conversion rules preserve already-earned charge of 16–19 if the talent is added later. Separate full/mirror branches keep the native meter at 16. Untalented characters retain 20. Spending, missed attacks, utility, player ownership and charge receipts retain the existing system. These eight new rules, including the origin grant, are mechanical; no new semantic check is introduced. Combat recognition and the 50% damage intention remain AI-guided.

## Verification

Local schema/reference/size validation passed with 34,805 checks. Item mechanics passed with 1,269 checks. `test_playtest_phantom.cjs` exercises the actual emitted rules with four phase/order variants, two players with different capacities, no free charge from refill, later capacity reduction, owner-only origin grants, campaign continuity, tick/place/combat gates, civilian-only level changes, relationship bounds and resource order. These are local fixtures, not live gameplay.

Older suites retain their original fingerprints through a strict reviewed inverse. `review.json` separates incoming Studio normalization from authored changes. It rejects unrelated changes rather than blessing a new arbitrary baseline. The fixture's resource maximum now includes native trait resource modifiers. Current patch tests run in both publish and GitHub CI.

## Official draft status

Current official contract and guide: preview `1.3.0-preview`, fetched from `https://api-alpha.aidungeon.com/creator/v1/`. The author's previously supplied credential authenticated the read; it was used only in process memory, not source files or reports.

Automatic approval review blocked the attempted validation command before transmission. The stated reason is that transmitting the entire private world needs specific payload/destination approval despite the general request to update it. Do not bypass that rejection. No validation POST, draft PUT or publication occurred.

The reviewable complete candidate is `output/playtest-phantom-2026-11-06/world.json`, SHA-256 `7a71e689ee1efdb03cb97b9f7f3a95fa868710e3be361cd961c72d57d0532823`. Approval is needed to transmit its complete private content, including hidden NPC/story information, to the official Alpha `/validate` and `/worlds/0kL8UR7rgsu2` endpoints. Only after approval: re-read the draft if necessary, reconcile a changed ETag, validate, save with If-Match, then read back and verify actual values and the revision. Do not call `/publish`; publication stays with the author.
