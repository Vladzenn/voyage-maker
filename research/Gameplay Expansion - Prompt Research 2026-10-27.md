# Gameplay Expansion — Prompt and Behavior Research

2026-10-27

## Purpose

Improve Glowhaven's playability and scene texture through focused instructions, original situations, a small practical economy, and consistent custody consequences. Research informs design; it does not establish that the resulting world outperforms another world in live play.

## Official Voyage evidence

The official [Closed Beta announcement](https://voyage.io/releases/closed-beta) confirms persistent RPG state, authored quests, flexible character systems, and state-changing triggers. It establishes the availability of those building blocks rather than detailed field syntax.

[Patch 2.45.3](https://voyage.io/whats-new/patch/patch%3A100001203) discusses memory selection, identity-reference fixes, combat intent reliability, and quest/NPC handling. Those notes support paying attention to stable identities and current engine behavior; they are not a guarantee that custom prompt prose will work perfectly.

## General prompting evidence

Anthropic's [prompting best-practices guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables) recommends explicit desired behavior, relevant context, clearly separated examples, and purposeful structure. The transferable choices here are concise task-specific rules and three short examples covering different scene types. Claude-specific model settings, internal thinking instructions, and agent orchestration advice were not imported into Voyage.

This pass does not claim that any prompt trick ensures a particular quality increase across Voyage's available models.

## Voyage-specific community guidance

The [Story task reference](https://wiki.unofficial.voyage/ai/generateStory) explains that replacing an existing seeded instruction key changes that instruction; simply adding a contradictory custom rule leaves both in play. Therefore the expansion replaces the sparse narrator and style text directly while retaining player agency, outcomes, and responsive turn boundaries.

The [NPC Updates reference](https://wiki.unofficial.voyage/ai/generateNPCUpdates) separates actual saved NPC changes from narration. The new instructions request changes grounded in the latest scene and retain explicit agreement for traveling-party membership.

The [quest reference](https://wiki.unofficial.voyage/world/quests) describes explicit completion effects as an alternative to automatic semantic completion. New quests deliberately use separate accepted-status completion triggers. Empty automatic completion queries prevent an additional automatic completion route. Fixed fees live in one completion path rather than multiple prose and inventory grants.

The [trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents mechanical gates, semantic predicates, effects, phase timing, stored flags, placement, and travel. The expansion uses geographical/status gates before semantic judgments, keeps clauses within caps, and treats an actual completed crossing differently from an intended one. The opening contact uses mechanical placement at tick zero; initial scene prose already establishes the same cast.

The [realms reference](https://wiki.unofficial.voyage/world/realms) describes realm/region/location parenting and discovery. Although its general authoring advice favors single-realm physical settings, the user expressly selected a separate prison realm. The export treats that as a map organization choice for a physical campus. No planar magic or new dimension was added to canon.

The [items reference](https://wiki.unofficial.voyage/world/itemTypes) supplies the item definition shape and supported bonus kinds. Prices remain descriptions and lore; no unsupported price or shop-stock schema fields were invented.

The [Encounter Elements reference](https://wiki.unofficial.voyage/other/encounterElements) documents a map of string values. The new encounter ingredients use that shape rather than character-style objects.

The [published size limits](https://wiki.unofficial.voyage/appendix/size-limits) inform the local checks. The checker distinguishes raw string size, JSON-encoded string size, and compact object size, including UTF-16 measurement appropriate to JavaScript strings.

These are unofficial community references, distinct from official announcements. The public API schema download was attempted without transmitting the world, but returned HTTP 403. No claim of full current codec validation is made.

## Observed reference-world techniques

The updated local Luxcellia export demonstrates:
- Role-matched reuse of existing cast.
- Locations with public services and separate hidden causes.
- NPC pressures tied to choices and recurring relationships.
- Authored quest dependencies and separate completion triggers.
- Consistent economy guidance across lore, items, and narration.
- A clock supporting availability and scene continuity.

Those are observed authoring techniques, not playtest results. No unique setting lore, named reference NPC, quest text, currency, or clock script was copied into Glowhaven.

## Applied design choices

1. Rich but compact arrivals: two concrete details, a relevant person or activity, and an opportunity to respond.
2. Flaws have consequences: selfishness, prejudice, gullibility, vanity, laziness, and poor academic performance are not rewritten into concealed virtues.
3. Services work without plots: buying a meal or enjoying tea can remain the whole scene.
4. Opportunities stay optional: agreement follows a disclosed premise and terms; refusal does not summon a new crisis.
5. Consequences persist: evidence, corrected records, a repaired device, unpaid fees, and a warrant survive the immediate exchange.
6. Cast reuse respects availability: established role-holders come first, but offstage people are not teleported in to answer every question.
7. A small social circle is supported: most contacts remain at work; assistance and courtship do not recruit them.
8. Custody has several kinds of play: work, visits, serving time, appeals, and escape follow actual legal role and practical access.
9. Exact payouts are typed effects: ordinary negotiations remain mediated by the game's actual inventory and narrative behavior.
10. Existing combat architecture remains intact: scenery and wit do not override resolved outcomes.

## Live behavior checks still needed

A useful live pass should verify:

- Buy only an inspection at Rune and Raven's; confirm no unapproved repair or charge.
- Accept and finish a paid job; confirm exactly one fee and a persistent result.
- Refuse a job and enjoy a meal; confirm that content is not forced.
- Challenge Ranka Kagari; confirm selfish resistance and earned evidence rather than instant kindness.
- Ask an existing fitter or clerk for help; confirm no replacement NPC is generated.
- Meet a warm NPC; leave alone and confirm no automatic recruitment.
- Enter through authorized prison work; confirm worker access without prisoner status.
- Receive a real custody order after actual capture and a hearing; verify the transfer and intake record.
- Lose consciousness while imprisoned; confirm recovery remains under custody.
- Attempt a failed escape; confirm no successful transport or cleared sentence.
- Complete a lawful term/review and discharge; confirm belongings and warrants follow their real records.
- Resolve an actual successful escape; confirm physical freedom without erasing the case.
- Begin the Phoenix opening; confirm Hinae Komori's scene and saved placement agree.
- Take the supervised field trip; confirm travel, warning signs, instructor competence, and actual combat outcomes.

These checks are a test plan, not a record of completed live sessions.
