# Alpha 7 — Identified Problems and Future Audit Rules

2026-10-28. This report distinguishes configuration defects, narrative risks and confirmed data corruption. The supplied playtest shows what was said; it is not a complete live state dump.

## 1. The level-87 clerk was a configuration problem

The old Glowhaven, Drakenspire, Asterveil and prison regions supplied no fallback NPC level range. Our health settings are 12 per level plus 66 base, so an average level-87 NPC on neutral modifiers has exactly `12 × 87 + 66 = 1110` HP. That precisely matches the report.

The community reference describes automatic NPC levels as a party-near roll constrained by location/region bands. A level-100 developer encountering unpinned new workers therefore exposes the missing bands. Our prose said to use believable competence but did not constrain that engine path. This is a strong explanation, rather than a claim that we inspected Voyage's running implementation. [NPC behavior](https://wiki.unofficial.voyage/world/npcs), [health settings](https://wiki.unofficial.voyage/other/otherSettings).

The fix adds fallback bands everywhere and tighter bands at public hubs, plus role-aware generation guidance. Explicit authored levels remain unchanged: the Great Sage, Archons, headmasters and faculty retain their intended power. A location band constrains unpinned generation; it does not replace a fixed authored level. [Region/location bands](https://wiki.unofficial.voyage/world/regions).

Already generated NPCs in an existing game are not shown to be repaired by a new world definition. Use a fresh run to test generation, or repair those existing individuals explicitly in that save. We have not performed a live repair.

## 2. Global personal examples were the wrong kind of context

The old direct-chat Style, Tone, and Length field supplied these existing characters as cadence examples: Haruki Saitō, Ririka Kujō, Kei Aoki, Reika Saionji and Akane Todo. None was a nonexistent character. The defect was giving every selected speaker a fixed set of other people's voices to imitate, even when none was relevant.

Similar examples appeared in general NPC intents, creation, details, relationship updates and location service guidance. One NPC-detail procedure even repeated particular characters' private facts. Stronger models can respect the intended scope; weaker models may blend identities, mention an unrelated person, borrow a motive, or treat an example as current scene cast. That is a risk mechanism, not proof that these lines caused a particular generated sentence in the transcript.

The current instructions replace those examples with general behavioral rules and require the actual speaker/actor's record. The global direct-chat portal case study is also replaced with relevant-role, access and current-placement rules, so a shopkeeper's conversation is not constantly steered toward court transit.

A canonical-name scan now finds authored personal names only in the dedicated Academy Roster Reference lookup block, rather than scattered through generic procedures. Exact identities still belong in actual character relationships, quests, triggers, location staffing and the roster. Removing every name from world data would make duplicate generation worse.

The scan and its baseline/current results are saved as `prompt-reference-audit.json` in this revision's authoring folder. It is not a full semantic audit: partial aliases, unsupported claims, unlisted invented names and subtle contradictions need separate review.

## 3. A previous name replacement damaged three records

These cards contained `Gen'ichirō Mizuhara’ichirō` in hidden information:

- Ririka Kujō
- Kei Aoki
- Sōichirō Takamine

That concatenation is a confirmed data error, not a stylistic concern. It is consistent with expanding a shortened name inside a longer name and leaving its suffix attached. The exact malformed string is repaired to the existing canonical `Gen'ichirō Mizuhara`. The Archon's actual record and identity remain intact. No broad first-name substitution or speculative alias expansion was used for the repair.

## 4. Affinity had been used as a shortcut for a teaching appointment

The old role labels included Arcane Fundamentals for an Arcane-affinity professor, introductory Void studies for a Void-affinity instructor, and several element-named departments. A person's comfortable element can inform their demonstrations, but it does not establish their subject, qualifications, learned breadth or the academy's timetable.

I introduced that shortcut while filling the earlier cards without an explicit curriculum. The issue is in the authored content; the engine did not require those labels.

There is now one explicit three-subject roster per academy, with exactly one Magic Theory teacher each. The same assignments populate the public professor profiles, academy descriptions, teaching-room notices, relevant lore and enrollment guidance. Their existing affinities and combat capabilities remain unchanged. Creation/detail instructions state that affinity cannot automatically assign a subject or invent another department.

## 5. Why these problems recurred

The repeated pattern was using a salient example as a general rule. A recent portal bug became broad transit exposition; a recognizable character became a generic voice example; an affinity became a job assignment. Duplicating those details across different fields then made later corrections incomplete. The malformed name is a separate, mechanical example of an overbroad text replacement.

These are authoring and maintenance mistakes I introduced. Calling the runtime model unreliable does not resolve the source defects. The useful fix is to put facts at the right scope, use supported engine controls for mechanical constraints, maintain explicit assignments, and verify references after edits.

## Rules for the later full-file audit

1. **Foundation:** Does the broadly included overview describe enduring premise and rules, or a walkthrough of the newest quest?
2. **Procedure:** Is an AI field describing how to perform its task, or smuggling in a fixed cast, private secret or specific live situation?
3. **Reference:** Are names used to identify real data or as unnecessary imitation examples? Are all identity/area references exact and uncorrupted?
4. **Scope:** Can this fact apply to the actual speaker, location and active quest? A private record is not universal knowledge.
5. **Mechanics:** Is a numeric constraint represented by a supported field/effect, or merely requested in prose? Do explicit values bypass a default?
6. **Independent facts:** Keep affinity, learned repertoire, subject taught, employer, rank, competence and personality separate. Connect them only where actually justified.
7. **Persistence:** Test first discovery, refusal, retreat, repeat visits and an already completed branch. A type is not an inexhaustible individual.
8. **Synchronization:** Compare the full world and standalone sections after edits. Preserve images and distinguish current files from historical snapshots.
9. **Claims:** A local consistency check is not a live model-quality test. Record what was actually tested and what still needs play.

The general AI personal-example scan, subject-roster checks, exact reference checks and preservation checks now run as local regression guards. They will catch these particular failure patterns; they do not prove the whole file is free of semantic problems.
