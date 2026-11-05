# NPC conversations — private phantom update

Applied to the canonical world on 6 November 2026 after the author's explicit implementation request. No public patch notes.

## Applied scope

Exactly three existing AI instruction strings changed:

- `generateStory.Character Behavior`: a short exchange between nearby NPCs can occupy one foreground beat. They have their own reason to speak; not everyone must react to the player.
- `generateStory.Social Decision Rules`: ordinary banter, arguments, gossip and practical exchanges may arise without player initiation or automatic quest offers. Overhearing depends on perception and access; partial claims are not verified facts. Detection needs a plausible tell. Essential clues have another credible route.
- `generateNPCUpdates.Knowledge Boundaries and Reference Capture`: preserve meaningful information, commitments and relevant relationship changes with source and audience, through supported memory/updates. Suspecting a listener does not establish their identity.

Retained combat-only intent generation, direct-chat scope, privacy and established personalities. No new fields, triggers, counters or content records. A recursive before/after comparison confirms every other world value is unchanged, including media, coordinates, quests, combat settings, elemental reactions, scrolls and Spider-specific content.

The story task is 29,834 compact UTF-16 units against its 30,000 limit; NPC Updates is 22,954 against 24,000. The story task grew by 97 units through replacement of overlapping guidance. Keep future additions concise.

## Basis and limits

The supplied Chikara export (`0ec5cc4a-4fd5-4545-b063-905e77f7acc0`) supplies examples of independent conversations and eavesdropping, not proof of a background simulation. Its newer combat-only instructions conflict with a retained social `other` intent rule; that conflict was not imported. Its duplicate conversation text under a nonstandard top-level `aiInstructions.custom` task is not relied upon.

The [19 October release notes](https://www.reddit.com/r/Voyage/comments/1xa7x32/october_19th_2026_patch_notes/) describe ordinary noncombat activity being handled through story narration. The community references distinguish [main story generation](https://wiki.unofficial.voyage/ai/generateStory), [direct NPC chat replies](https://wiki.unofficial.voyage/ai/generateDialogue), and [combat intentions](https://wiki.unofficial.voyage/ai/generateNPCIntents). These are current research observations; the applied text remains AI-interpreted guidance.

Local verification: 34,324 structural/schema/size/reference checks and 1,269 item-mechanics fixture checks passed. The synchronized AI section matches the canonical world. A recursive comparison verifies the three-field scope; these checks do not execute narrative behavior.

Historical preservation suites lock the exact earlier world hash. Their [strict adapter](../tools/npc-conversations/previous_world.cjs) restores only this patch's three reviewed strings before the existing Magic Overhaul inverse; the old fingerprints remain unchanged. The [review delta](../tools/npc-conversations/review.json) records the previous values and exact hashes. Verified both exact reconstruction and rejection of an unrelated NPC-level mutation; this adapter is test infrastructure and is not part of the Voyage world.

## Live review still needed

- At a lesson or guild counter, two established nearby NPCs discuss their own concern without demanding player participation or an automatic journal entry.
- In a quiet private exchange, ordinary distance, closed doors, language and actual abilities restrict what the player can perceive. Listening should not expose hidden records.
- Deliberate concealed listening can succeed, yield fragments or be noticed through ordinary action resolution. Mere listening is not guaranteed discovery; a partial clue is not proof.
- A direct private chat remains a reply from its addressed speaker. Uninvolved or absent NPCs do not acquire the conversation's knowledge, and quiet chosen activities remain possible.

No live Studio validation, playtest, world save or publication was performed by this patch. Local structural checks cannot establish dialogue quality or guarantee AI compliance.
