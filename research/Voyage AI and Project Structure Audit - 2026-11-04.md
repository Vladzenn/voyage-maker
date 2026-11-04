# Voyage AI and project structure audit

The pasted AI export matches both `aiInstructions` and `imagePromptConfiguration` in the canonical world at commit `767f841`. It contains 18 task blocks and 298,627 UTF-16 units of instruction text, plus five image prompts. Those are stored text totals across separate tasks. The repo does not measure the assembled context for a live turn.

The prompt inspection found repetition within individual tasks and fragile size headroom. The import hotfix changes the four fishing condition values. The prompt changes below are proposals for a separate, testable pass.

## Studio error and verification

The four reported condition values had 99 UTF-16 units when decoded and 106 when serialized as JSON strings. The escaped backslashes and quotes account for the difference. That reproduces the six-unit overflow reported by Studio. The replacement measures 94 decoded and 99 serialized. It keeps the word groups for fishing, angling, reeling, lures, bait and bobbers, plus cast/lower with line, rod or hook.

The builder, local validator and fishing fixtures now check the serialized condition value. The schema regression restores the previous string and requires a rejection for each affected trigger. The local checks exercise literal matching and scripted effects. The Studio import and the live AI’s interpretation remain separate verification steps.

## Prompt size

The table uses the same compact JSON count and caps as `tools/project.py`. These are authoring checks. Studio’s current Size Limits panel is the final check for an import.

| Task | Serialized units | Local cap | Headroom |
|---|---:|---:|---:|
| Story | 29,983 | 30,000 | 17 |
| Action Info | 19,981 | 20,000 | 19 |
| Item Generation and Usage | 19,963 | 20,000 | 37 |
| Encounters | 19,956 | 20,000 | 44 |
| Character Background | 19,834 | 20,000 | 166 |
| Location Details | 19,699 | 20,000 | 301 |
| New NPC | 19,632 | 20,000 | 368 |
| Summary | 19,120 | 20,000 | 880 |

The NPC image prompt has 4,869 text units against the local 5,000 cap. Quest-generation guidance has 4,957 against 5,000. Four task blocks are within 44 units of their local limits, so routine additions are already difficult.

## What to trim first

| Area | Observed overlap | Proposed edit and verification |
|---|---|---|
| Story turn boundaries | `Turn Structure` and `Turn Boundaries and Endings` both resolve the chosen action, finish finite success and stop before the next player decision. | Keep one instruction sequence. Retain the second block’s distinctions between current payloads and past memory, and its examples of natural endings. Check a finite task, “continue,” and a turn with two players. |
| Portal classification | `Portals and Movement — Current Input` states the Evertree return endpoint and sole hub twice. `Local Movement and Explicit Commitment` adds distinct ambiguity and Asterveil movement cases. | Remove the repeated endpoint sentence and preserve its unique detail about the staging floor. Keep a short endpoint reminder in Story because that task renders the resolved trip. Check viewing a portal, crossing once, and returning. |
| Chat suggestions and chat summary | `Specific Openings Without Assumed Knowledge` repeats much of `Conversation Starter Guidance`. `Evidence, Commitments and Closure` repeats principles from `Summary Guidance` and `custom`. | Fold the unique private-profile and known-name constraints into the existing starter fields. Keep attribution, paid obligations and who understood an aside in the summary. Verify which keys Studio retains after a save and re-export before dropping any field. |
| Long-term quest summary | `Quest Persistence and Completion` and `Quest Completion Evidence and Cast Continuity` both preserve the accepted quest, real progress, final event and settled payment. | Merge quest evidence into one block. Keep the separate guidance on generated people, who knows what and where characters actually are. Check paid work, an optional report and a fresh recurring contract. |
| Academy roster | Story carries a 1,460-unit list of 64 people. All 64 already have NPC records with matching academy affiliations. Five other NPCs also have academy affiliations, so a complete faction list and the formal school roster have different scopes. | Consider moving the formal list to an academy reference that can be retrieved on demand. Keep the existing text until a roster question reliably finds the reference in live play. |

Several repetitions have a purpose. Action Info decides feasibility, Item Generation and Usage guides item handling, and Story renders outcomes. The short Mark rules in Action Info and NPC chat guide two different decisions. Fishing’s skill route and inventory guidance also serve different tasks. Keep typed triggers and quest effects as the owners of exact item, XP and state changes.

Latitude documents editable Action Info guidance and native quest effects. The project’s current rule placement can be compared with those features. The community reference adds task-by-task details about seeded fields and task-specific limits. Its round-trip notes are useful leads to verify in Studio, especially for the small NPC chat tasks. [Latitude’s Creator Studio update](https://voyage.io/whats-new/patch/patch%3A100001188) · [Latitude’s JSON validation update](https://voyage.io/whats-new/patch/patch%3A100002348) · [Community Story reference](https://wiki.unofficial.voyage/ai/generateStory) · [Community Conversation Starters reference](https://wiki.unofficial.voyage/ai/generateConversationStarters) · [Community NPC Chat Summary reference](https://wiki.unofficial.voyage/ai/generateNpcChatSummary)

## Project structure

| Area | Current role and finding |
|---|---|
| `world-draft/WorldAlpha - World.json` | Canonical import and merge target. The 24 section exports, including `WorldAlpha - AI.json`, are generated from it by `project.py sync`. Together they add about 6.23 MiB of useful section views. Editing both copies independently invites drift. |
| `world-draft/AI Instructions - Readable.md` and older patch notes | The readable AI snapshot labels itself historical and predates Alpha28. Use the current JSON for a prompt review. Group old guides by release or label their links more visibly if navigation becomes a problem. |
| `docs/`, `research/`, `sources/` | The state and decision docs carry current policy. Research contains dated audits and playtest plans. The reference worlds under `sources/` supply examples. Keep those roles distinct when importing a new Studio export. |
| `tools/` and CI | Portable validation and per-feature fixtures are useful. The historical fishing projection also asserts a whole-world hash, so even an unrelated prompt edit requires re-reviewing historical data before older preservation fixtures can run. A future maintenance pass could scope those older invariants to the sections they actually protect while keeping live feature tests on the current world. |
| Media | About 1,196 MiB of tracked media in the working tree dominates its size. Prompt cleanup would improve authoring headroom. Any checkout-size work should start with the media inventory and verify referenced files before changing storage. |
| Publish scope | `start` refuses a dirty checkout and `publish` stages all visible changes. This audit encountered an untracked reference export. A preflight review of the proposed staged paths is especially useful when a new reference or draft is sitting in the workspace. |

Start prompt cleanup with Story, Action Info and the two chat tasks. Measure the serialized sizes again, then compare a small set of player actions and NPC conversations in Voyage. This gives a behavior check before tackling the longer encounter and NPC prompts.
