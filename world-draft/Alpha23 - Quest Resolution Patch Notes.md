# Alpha23 — Quest Resolution Revamp

Includes the complete Alpha22 runtime-text cleanup: 151 text fields cleaned; actual rules retained under the hood. See Runtime Text Audit - Alpha22.md for the exact scope.

All 112 quests were classified and checked for activation and completion coverage. Sixty simple, finite undertakings now use detailed native completionCondition queries. Eight short guild commissions have one final verified fieldwork-and-settlement check rather than a field counter and separate report gate. Forty-four quests keep explicit stages where exams, authorization, evidence items, a longer adventure or consequential choices require them.

Removed 53 author-maintained world triggers (361 → 308) and replaced 21 manual quest completion triggers with native conditions. Native conditions can generate runtime completion checks; these numbers are not a promise of fewer runtime evaluations. No quest was deleted. Fixed money/experience rewards and consequential completion flags remain. Five older guild service-credit grants moved from all-player quest rewards to the existing player-scoped verification effects.

Fixed all four recurring guild acceptance gates to admit a completed previous run only when the existing 20-turn delay and fresh offer conditions pass. The board can show available or deliberately reopened abandoned/rejected/expired jobs. Browsing is still distinct from acceptance. The alleged eleven missing offer writers were traced to dynamic writes in gh_guild_board and tested; redundant writers were not added.

Portal anomaly, key grants, spider victory/trophy rules, rival confrontation, dungeon gates and academic pacing remain protected world-event systems. Their original behavior is preserved. The existing useful staged curriculum and once-per-playthrough thesis remain.

Validation: 2304 local coverage, reference, budget and preservation checks; 399 script/state fixtures and compilations. No live Voyage import, semantic model evaluation, multiplayer playtest or existing-save migration. All 205 NPC records/portraits, map images/coordinates, abilities, skills and equipment retain their post-cleanup state.

Playtest on a fresh game: one native personal quest; native field commission with later report; one explicit academic assessment; each of four repeating guild contracts twice with a real new offer and cooldown; refusal/abandonment and return; all portal/trophy/rival events. Verify no duplicate reward, phantom report or stranded next-step marker. In multiplayer test mixed badge ranks, absent/unlicensed players, who accepts, proof handover and service-credit recipients. Any-player badge checks and party-shared quest state remain a limitation requiring live validation; this release is not certified multiplayer-safe.
