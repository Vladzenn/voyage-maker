# Alpha 9 — Luxcellia AI Comparison

Compared on 2026-10-28 using the two newly supplied exports and the creator's supplied patch-note history. Findings about those files are observations. Documentation claims below are labeled separately. Proposed behavioral benefits are not live test results.

## What the comparison actually shows

Both worlds have the same 18 AI task IDs. Our supplied AI was already substantial: 267,241 characters of compact task objects, versus Luxcellia's 308,814. Many safeguards were already present. The useful difference is how consistently each task owns its decisions, how generation inputs reinforce the setting, and how concrete state changes are connected to prose.

Luxcellia's patch history is valuable partly because it records failed ideas and limits. The newest room-prefix patch calls itself an experiment. The following clock update removes an earlier scripted clock after bad time jumps. Some model tests reproduced an error, others did not. We should inherit that distinction between evidence and intent, rather than treating every historical patch as a feature to install.

## Feature decisions

| Feature in the reference or notes | Our supplied file | Alpha 9 decision |
| --- | --- | --- |
| Place-qualified room names | Already present for 596 of 601 areas; the other five keep the old Drakenspire parent prefix after its location rename. All are globally unique. | Preserve all keys and paths. Enforce parent qualification for genuinely new authorized areas. No bulk rename is needed. |
| Present travel choice before destination matching | Present in several rules, but not fully coordinated. | Strengthen action reading, story and memory; add a short conditional story reminder. Natural adjacent-door references remain valid. |
| Engine independently matching a place word | No exposed switch in the inspected configuration. | Do not claim prompts disable it. Test live; the reference also calls its mitigation experimental. |
| Exact portal destination state | Current export has stale Drakenspire references after a manual rename. | Repair router parent and reveal target. Local tests reproduce five baseline failures and pass after repair. |
| Local guild/inn/market references | Existing place and area lookup rules. | Generalize local-reference handling without adding a foreign guild or remote landmark. |
| Trigger-driven world clock | Not needed by our current setup. | Do not add it. Use current time, actual elapsed actions and appointments separately. The creator later removed his own clock. |
| Duration-aware special regeneration | Our actual-rest settings already restore resources. Reference cheats have their own mechanics. | Retain existing resource settings; no second regeneration script or imported cheat. Distinguish actual rest from a brief pause. |
| Fewer ordinary-use ability cards | Already partly present. | Strengthen the dedicated learned-ability task; ordinary skill use is normally not a new card. |
| Practice of an unowned skill | Existing training guidance, with room for classifier confusion. | Name the actual practiced skill and preserve supported learning checks; never promise acquisition or XP. |
| No invented exhaustion penalties | Basic HP/MP rules already exist. | Make the action task reject invented stamina, hunger and low-MP arithmetic. |
| Correct hostile/allied effect recipients | General combat tactics existed. | Add actor/side/beneficiary checks in action reading and NPC intents, including objects and taunts. |
| Friendly spars without accidental lethal fights | Restraint guidance existed. | Clarify the boundary between controlled practice and a genuine hostile combat attempt. This is not damage immunity. |
| Enacted retreat rather than repeated suggestions | Existing end-state guidance. | Require a concrete supported escape/surrender attempt in an actual fight; resolution still decides success. |
| Permanent party membership for summons | Incompatible with our distinction between temporary support and chosen companions. | Do not copy automatic recruitment. Preserve real duration, identity and allegiance. |
| Generated-item categories and rarity ceilings | Our catalogue and bonus scale differ. | Use our seven categories and actual slots; adapt anti-bootstrap crafting rules without adding foreign rarity tiers. |
| Closed caches, payments and deposits | Existing ownership rules. | Reinforce item generation, story and summaries so completed acts remain completed once. |
| Stable opening and continued identity | Existing authored starts and memory rules. | Add a compact opening anchor and form/identity checks; do not copy the reference's universal rebirth framing. |
| Distinct dialogue with knowledge limits | Already established; the supplied direct-chat task is not merely a placeholder. | Consolidate its custom section around answers, settled business, actual knowledge and voice. No fixed named-cast examples. |
| Non-nagging teachers, healers and companions | Inconsistent across tasks. | Respect a reply/refusal until circumstances materially change, while preserving genuine immediate danger. |
| Parallel romantic scoring | Conflicts with our single configured relationship ladder. | Use one score, measured scene changes and actual compatibility. Trust, consent, romance and recruitment remain distinct. |
| Higher difficulty when skill passes mastery thresholds | Risks punishing improvement and conflicts with our approach model. | Do not copy mastery-based difficulty increases. Task, method and conditions determine difficulty. |
| Guild contract counters, promotions and quest fixes | Reference-specific state machines. | Carry the general persistence principle into memory and faction details, not the foreign guild's counters, ranks or quests. |
| Long-range magical travel cards | Reference-specific skills and access design. | Do not add them; retain our court-issued portal keys and actual abilities. |
| Author seeds and archetype inputs | Our file retained shipped defaults. The reference's count alone is not a quality measure. | Add setting-specific inputs, with one consistent author seed and varied optional character patterns. |
| Lived-in spaces and entry-first arrivals | Already strong authored map; details generation still used broad scaffolds. | Improve generation guidance and receiving-room image descriptions without changing geography. |
| Advanced game-mode intent instructions | Supported and already present in the mode structure. | Preserve modes; no second contradictory combat protocol. |
| Special species/form support | Our custom species rules already differ from the reference. | Use our actual anatomy and active form, including dragonkin and transforming fae; do not transplant theirs. |

## Where the rules now belong

This is the maintenance map for future changes. A fact may be relevant to several tasks, but its detailed rule should have one owner and a brief compatible reminder elsewhere.

| Task | Primary responsibility |
| --- | --- |
| `generateStory` | Render resolved facts, distinct voices, scene pacing and the next player decision. |
| `generateInitialStart` | Perform the selected authored opening without deciding the player's response. |
| `generateActionInfo` | Classify the current method, real skill, target, impact and chosen movement. |
| `generateCharacterBackground` | Build a biography and appearance consistent with actual creation choices. |
| `generateConversationStarters` | Offer plausible optional lines from observable or genuinely known information. |
| `generateDialogue` | Speak as the selected person with their knowledge, purpose, voice and boundaries. |
| `generateNpcChatSummary` | Preserve disclosures, commitments and actual outcomes of that conversation. |
| `generateNPCIntents` | Construct supported attempts in a real fight, with correct sides and recipients. |
| `generateNewNPC` | Resolve identity before creating an uncovered individual; respect local power bands. |
| `generateNPCDetails` | Fill genuinely missing character detail without replacing authored facts. |
| `generateNPCUpdates` | Apply supported changes and relationship developments without phantom state. |
| `generateLocationDetails` | Detail the actual place, its usable areas, services, access and local connections. |
| `generateRegionDetails` | Maintain existing geography, culture and daily life without inventing new map regions. |
| `generateEncounters` | Decide whether an interruption is useful, then develop one appropriate local situation. |
| `ItemGenerationAndUsage` | Maintain actual item definitions, ownership, transactions and bounded crafting. |
| `summarization` | Preserve durable events and unresolved matters while closing settled accounts. |
| `generateLearnedAbilities` | Distinguish an earned new technique from ordinary use of existing skills. |
| `generateFactionDetails` | Preserve existing institutions and create only a justified persistent organization. |

The main narrator cannot repair every earlier classification or later update error. A beautiful paragraph that says the party crossed does not replace a missing location effect. Conversely, a prompt improvement should not become an unrelated new trigger, resource or field.

## Why the same kinds of bugs recur

**Rules reach different moments.** A restriction in Story may arrive after action reading has already chosen the wrong place. If memory later compresses a planned journey into a visit, the next scene inherits another false premise. The corrective rule must reach the decision that owns it.

**Content can behave like an instruction accidentally.** A named example in generic chat guidance can become the current speaker's colleague or secret. A region-specific plot in broad world foundations can dominate unrelated sessions. Reference-only proper nouns in prohibitions still put those nouns into context. This release removes the confirmed foreign terms in those prohibitions and keeps fixed cast lookup in its dedicated roster section.

**Generation inputs can undermine the main style.** Broadly cheerful narration can still produce an endless sequence of damaged, conspiratorial strangers if random background scaffolds keep asking for wounds and hidden agendas. The new scaffolds allow those traits where appropriate without requiring them for everyone.

**Renaming keys has mechanical dependencies.** The current Drakenspire rename updated visible content but missed script literals and a reveal target. General prose cannot reliably repair a stale structured destination. Preserve keys where possible and test every referenced route after a rename.

**More instructions can create more disagreement.** We removed three redundant custom example sections and consolidated direct-chat guidance. All 18 tasks changed, but not every task received the same list of recent bugs. Existing world foundations, authored NPCs and systems remain authoritative.

## What the documentation supports

The following are community documentation, not official Latitude guarantees:

- Editable default keys replace their corresponding built-in section; custom keys append. Deleting a default key can cause it to be backfilled, so a missing key is not a reliable way to disable behavior. This pass removes only redundant custom sections and retains the default override keys. [AI Instructions](https://wiki.unofficial.voyage/ai/aiInstructions)
- Author seeds are selected randomly for strong/elite/boss/mythic detail generation. One comprehensive seed gives that step a consistent style; it does not govern every weak incidental NPC. [NPC Author Seeds](https://wiki.unofficial.voyage/other/authorSeeds)
- Planning triggers can inject short story instructions. Our four additions use raw text checks and persistent per-tick deduplication, rather than spending semantic condition checks. They still steer an AI response rather than mechanically enforcing the injected prose. [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions)
- Published limits distinguish compact task objects, JSON-encoded instruction leaves and raw image-prompt text. The audit measures those separately, including UTF-16 length. [Size Limits](https://wiki.unofficial.voyage/appendix/size-limits)

Official release notes also show that AI-key validation and field handling change over time; old exports should not be treated as an immutable schema. The [2.46.4 notes](https://voyage.io/whats-new/patch/patch%3A100002348) specifically address validation of AI instruction keys. The existing mode layer is consistent with the [2.33.7 announcement](https://voyage.io/whats-new/patch/patch%3A100000946) of per-mode NPC intent guidance. No undocumented fields are added here.

## What is still a hypothesis

We have not proved that the new wording reduces unwanted map jumps, nags, ability spam or repetitive chat in live Voyage. The creator's reported model tests are his evidence for his configuration, not our results. Our address prefixes were already largely present, so a second rename pass would have little obvious benefit and considerable migration cost.

Likewise, four lexical reminders may help by making a relevant constraint recent, but can miss uncommon wording or activate on an irrelevant mention. They are not an intent classifier or an invulnerability system. Existing independent engine behavior remains outside this file's direct control.

Quality should be judged with the same short scenarios on the supplied baseline and Alpha 9, on the same Voyage model/mode, repeated enough to see variance. The accompanying playtest sheet defines concrete pass/fail observations. Only that evidence can establish whether this release matches or exceeds the reference in actual play.
