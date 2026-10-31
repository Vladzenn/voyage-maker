# Alpha 11 — Ryūka Marufuji and the Silken Victory

Ryūka Marufuji replaces the retired Dragon Hoard student in the same roster slot. The academy retains twelve students and the complete world retains 130 NPCs. This is a replacement character: the old student's personality, bad-luck history, relationships, equipment and portrait are removed rather than transferred to her.

## The character

Ryūka Marufuji is the approved twenty-year-old, second-year human Dragon Hoard student from the Portrait generation chat: platinum hair, green eyes, smoky eye makeup, large black hoop earrings, yellow tie and a slim Arcane wand. Her latest portrait changes are carried into both narrated appearance and visual description. She remains a capable level-15 student, with pride, classism, precise teasing, private effort and easily bruised invitations. A stronger player does not cause her to acquire boss-level powers.

The longer authoring reference was condensed into a detailed NPC record within the 8,000-character entry bound, with room for a normal hosted portrait URL. Her canonical identity is Ryūka Marufuji, not Malfoid or a second alias NPC. Her initial journal visibility is false and initial relationship is neutral; the event never resets a relationship acquired earlier.

The finished green-eyed portrait is already saved at `world-draft/npc portraits/Ryūka Marufuji.png`. No hosted Voyage URL was available for it. Her portraitUrl is blank rather than pointing to the removed student's picture or a local path. Upload that existing PNG in Studio to attach it; no replacement portrait was generated in this pass.

## The requested event chain

```text
Actual portal anomaly
    → actually overcome Vhalessra Veyrath
    → recorded victory issues Matron's Anchor Sigil once
    → later hold the item in Four Sages Bazaar
    → Ryūka Marufuji confrontation once
    → optional practice / exhibition continuation
```

`gh_spider_victory_sigil` checks the persistent anomaly-entry and actual matron-resolution flags. It grants one marked anchor fragment to each current player and records issuance. It does not depend on accepting Silver Threads Below, completing the investigation or reporting to the court. The existing victory logic still decides whether the matron was genuinely overcome.

The fragment is released by the damaged anchor, so a genuine restraint or surrendered defeat also produces it without inventing a corpse. An ordinary conversation, flattery, a claimed kill or possession of the portal key does not. Killing the matron after surrender produces no second grant. Sale or loss does not regenerate the item.

The item is a Document-category physical keepsake and evidence. It has no stats, teleport function or mana restoration. The court can inspect it without automatically taking it. Its stable authored item identity anchors later recognition even after the prose summary compresses the fight.

## The bazaar confrontation

`gh_ryuka_bazaar_confrontation` checks:

- The party is in Four Sages Bazaar.
- At least one player actually holds Matron's Anchor Sigil.
- The matron's real resolution is recorded.
- The confrontation has not already begun.
- Play has started beyond tick zero.

It runs in planning, places the existing Ryūka Marufuji in the party's actual bazaar area, reveals her journal identity and makes the first optional quest available. It moves no player, consumes no trophy, changes no relationship score and recruits nobody. A separate started flag plus the nonrecurring trigger prevents replay.

The script preserves whether she was already known and which players held the proof. Strangers receive an introduction; existing rivals, friends, enemies and companions keep their real history. Missing runtime health for an uninstantiated premade does not block a first meeting. Actual death, an ongoing relevant fight or her being away from Glowhaven defers the scene instead of resurrecting or abducting her. A deferred attempt does not consume the event.

She is shopping for precise wand fittings and exhibition materials. Her provocation is that an exciting story does not prove polished technique; she wants to show preparation matters and secure the attention of someone capable of answering back. If the player shows the sigil, she can appraise it, question the account and be unsettled by real achievement. A concealed item remains concealed. The inventory gate schedules the encounter; it does not grant her secret knowledge or invent a public victory report. She can issue a backhanded invitation without knowing the queen's fate.

The first beat ends at the player's response. There is no forced street duel, accepted challenge, romantic interest or trophy surrender. Leaving or rejecting her is valid. Once this scene starts, another bazaar visit does not replay her introduction.

## The two-quest continuation

### A Measure of Polish

Her challenge can become controlled wand/weapon practice, moving targets, an agreed item appraisal or a practical demonstration suitable for a scholar, artisan, trader or noncaster. The actual activity, limits, venue, permission and supervision are agreed first. Her own invitation does not overrule faculty or enroll an outsider.

Practice uses Training Court; a practical display can use Exhibition Hall. A meeting trigger brings the same available character to the attended agreed venue, without moving the player or creating a traveling party. A win, loss, contribution or honest unsuccessful attempt can complete the session once actually played. The quest requires no apology, attraction or praise. It pays 400 XP once, without fixed affection, money or a free technique.

She is not automatically scaled to the player. A level-100 developer can outclass her; a weak participant can negotiate a suitable format. Safety follows the actual controlled activity rather than an imposed invisible handicap. Her response depends on treatment as well as outcome.

### You Could Have Asked

A later actual invitation, rather than quest completion alone, opens a small student exhibition episode. It adapts the earlier proposed arc: the spare invitation, shared preparation, family-backed favoritism and a chance to speak plainly. Romance remains one possible direction among rivalry, friendship, cooperation, complicity and distance.

Her household contributes ordinary materials. She uses that contribution to demand the best placement and omit Mai Kajiwara's genuinely agreed paid technical work from the credit. That work and a real approved display must first be established. Mai Kajiwara is not made a free servant, and faculty are not assumed complicit. The player can support correction, negotiate, refuse involvement or knowingly back favoritism. The actual outcome is stored; every branch is not relabeled as fair.

After a completed display or a real cancellation, the episode ends with an honest answer about further company, or an explicit refusal of that conversation. A rival's rematch, friendly meeting, mutually wanted adult date or estrangement can each be valid. No kiss, forgiveness or confession is required. Completion grants 650 XP once and preserves the actual outcome and boundaries.

The two invitations may be declined or rejected. Native quest UI rejection remains available. Spoken refusal is respected in narration; it does not require another mandatory scene. The trigger bank has no invented quest-rejection effect, romance meter or numerical affection gate.

## Cleanup

Removed the old identity from the active world, academy roster lookup, placement and year notes, the shield incident, and related character relationships. Daigo Bando keeps his existing Retsu Arakida sparring relationship. Suzune Mikazuki's shield care is grounded in her own judgment and Mai Kajiwara's expertise. The delayed-discharge quest keeps its actual replacement-collar fault without an unlucky student to blame. Those histories are not reassigned to Ryūka Marufuji.

Current future-story proposals are cleaned of the retired identity. Historical named exports, backups and old authoring snapshots remain recoverable history and are not active roster files. The current canonical roster remains the JSON; no retired NPC folder is recreated.

All map coordinates, areas, regions, image prompts, existing trigger definitions, progression and unrelated cast remain as in the current working baseline. All other portrait/map URLs are retained. The original one-time anomaly, return routes, postponed field test and separate authorized expedition are preserved. Asterveil's midgame bands and content are unchanged.

## Verification and installation

All 190 local fixture checks passed: the previous 161 regressions plus 29 replacement, item, confrontation, availability and quest cases. The structural/reference/size/preservation audit passes separately. The fixtures execute real scripts with simulated condition/effect handling and supplied semantic answers. Lazy-premade materialization is simulated, not observed in Studio. These are not live narration, schema import or balance results.

The current [community trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents raw inventory gates, persistent storage, one-time firing, NPC placement and planning-phase story injection. Those are the mechanisms used here; no unsupported spawn, forced dialogue-result or rejection field was added.

Use the complete **GlowhavenAlpha11 - Ryuka Rivalry.json** export and a fresh game for the roster replacement. This file does not delete or migrate a character already instantiated in an older save. Importing only the NPC or AI section would omit the trophy and event machinery. The canonical world and standalone sections are synchronized; previous working files are backed up.
