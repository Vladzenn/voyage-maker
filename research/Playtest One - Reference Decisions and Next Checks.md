# Playtest One reference decisions and next checks

This review separates observed playtest behavior, supplied-world patterns, community schema documentation and untested runtime assumptions.

## Evidence from the examples

Luxcellia's **NPCDetails/basic_info** and **Appearance Discipline** put stable narrated appearance in basicInfo. Its **Roster Before Creation** matches a needed role to an existing person rather than creating a replacement. These are useful patterns for the appearance drift and identity concerns in PlaytestOne. They do not prove that its complete narrator configuration prevents every hallucination.

Chikara's **Regional Travel** keeps journeys anchored to the selected map and plausible local routes. Its source uses repeated short area names such as reception under different locations. Luxcellia uses more globally distinctive area names. Both approaches illustrate naming choices rather than an established special anti-teleport syntax.

The current community reference explicitly says the narrator reads basicInfo and does not read visualDescription. Accordingly, appearance was added to the actual narrated input while retaining the existing portrait field. It also describes NPC abilities as prose capability context, not references to the player ability catalogue; Reika's approved prose list was restored on that basis. [NPC reference](https://wiki.unofficial.voyage/world/npcs)

The location reference uses short examples such as Council Hall, and describes area references through keys, paths, NPC currentArea and story-start locationAreas. No location-prefix requirement is documented. Existing prefixes were retained to avoid an unrelated reference migration; natural dialogue uses a short room name. Location and area are still both needed for unambiguous movement. [Location reference](https://wiki.unofficial.voyage/world/locations)

## Public knowledge versus production instructions

The sentence about “authored realms” had a direct counterpart in our lore. It was not merely spontaneous model behavior. The production rule belongs in AI map guidance; a resident can instead say which routes the Evertree serves. Public lore, region summaries and affected area text were cleaned. Shadowspire's private narrator note was moved into its hiddenInfo rather than left as a publicly styled lore entry.

Canonical full-name rules remain useful in records. Applying them to every spoken mention produces stiff dialogue and unnecessary repetition. New instructions explicitly map natural address back to canonical identity without an undocumented alias field. UI speaker labels may still display full names; this update changes speech and narration, not the platform's speaker-label rendering.

## Why keys and state are both used

The three key descriptions carry stable, useful information in the inventory. The normal keys identify the destination and operating room. The Silver Web key records the first return and the route it anchored. The keys are actual item types with no passive bonuses or consumable behavior.

Typed item-count conditions gate outbound access. Persistent booleans separately record whether the examination was armed, the one-time displacement happened, the silver route was discovered and the matron was overcome. This keeps a lost or deposited key from erasing past events. It also prevents ownership of a key from masquerading as victory. Native key possession does not itself certify legal ownership or command over a place.

The trigger reference documents item-count gates, item grants, quest objectives, location/area movement, NPC placement selectors and persistent script storage. The travel branch uses supported effects and records the actual intended destination, players and party companions. No portal schema, inventory alias system or per-area hidden field was invented. [Trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)

## What is local code and what still relies on AI

Deterministic script behavior: an armed accepted examination redirects an actual keyed crossing once; retreat unlocks the silver route once; possession gates later entry; route discoveries persist; an actual dead boss does not revive from a return trip; the explicit quest reward is not repeated.

AI-judged gates: recognizing a genuine latest-scene key handover, identifying an enrolled student from the actual background, accepting a real briefing, whole-player-party consent, a passage genuinely bypassed and a matron genuinely surrendered. The fixture suite supplies those decisions. A passing fixture does not prove the real classifier will make the same decision.

Companion effects use the documented allPartyNPCs selector, not a loop that might exceed the effect cap or accidentally move nearby classmates. However, the community reference says a downed NPC cannot be moved with this effect. A live evacuation/carrying test is required; the implementation does not silently heal them or claim this edge case is solved.

## Next live playtest sequence

1. **Ordinary academy opening.** Begin at level 1 in one academy. Confirm the correct admission packet, guide appearance, check-in and orientation. Request the complete roster. Check that the response uses all twelve actual students without summoning them or inventing a timetable.
2. **A different life.** Try Merchant, one village and one employment opening. Confirm no compulsory student identity, fake owned shop or replacement of an existing professor. Employment still uses normal character-creation stats; experienced-faculty builds need a separate design.
3. **Natural names and visual continuity.** Meet Akane, Tōru and Reika. Check hair, eyes, ram horns, equipment and individual voice. Use a title or honorific and verify no duplicate NPC is created. Observe whether displayed speaker labels differ from spoken words.
4. **Verification once.** Present a genuinely accepted credential and make a feasible request. Confirm the scene acts on the result rather than demanding the same proof every turn. Keep an order's scope distinct from a false new claim.
5. **Normal keyed travel.** Obtain each ordinary key through an actual handover. Open the route in Portal Room, return through the destination gate, inspect inventory and verify the key remains. A drawing or a named claim must not work.
6. **Explicit developer examination.** Use Developer Playtester and Developer: Portal Inspection. Visit Mihoshi Kagamihara at the court observatory and explicitly request the field-examination test. Accept the actual briefing, return to Portal Room and use the selected ordinary key. Developer level 100 by itself must not activate it.
7. **Immediate exit.** At Stranded Threshold, return without descending. Verify one Silver Web key, no separate hidden room, no boss completion and normal routes still working.
8. **Repeat entry and loss.** Use the silver key, return again and check for duplicates or repeated displacement. Test depositing or losing a key with a recoverable save; the threshold exit must still work. Test legitimate replacement afterward.
9. **Actual companions.** Travel with one real recruited companion and a nearby nonparty NPC. Only the real companion should move. Then separately investigate a downed companion and a multiplayer split, which local fixtures cannot establish.
10. **The descent.** Work through each visible passage with a caster, then with physical tools or a martial character where plausible. Confirm route revelation does not teleport the party or award an invented victory.
11. **The matron.** Observe fight difficulty for a normal level-20 group. A developer body cannot assess fair damage. Compare a real combat defeat, an actual surrender and an empty victory claim. Return later and confirm the same outcome persists.
12. **Debrief.** Deliver the actual evidence to Mihoshi Kagamihara. Confirm the case completes once and inspect the explicit 1,800 XP effect alongside any platform-provided completion awards. No unrelated graduation, property grant or forced relationship should appear.

Use new games for changed definitions and retain a known-good export. No migration of the existing playtest save is claimed. New portraits, dungeon maps, full schedules, broader progression and ordinary-character balance remain unfinished alpha work.
