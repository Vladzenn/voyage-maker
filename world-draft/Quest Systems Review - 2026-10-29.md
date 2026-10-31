# Quest Systems Review — 29 October 2026

## The distinction that guides Alpha23

The portal anomaly, a boss trophy and a trophy-dependent rival encounter are conditional world events. Their exact once-only state and item effects justify triggers. They do not establish that every conventional quest requires a numerical progress machine. Academic progression legitimately combines shared activities, assessments, prerequisites and paced invitations; an ordinary finite favor generally does not.

The earlier implementation applied explicit progress bookkeeping too widely. It increased the number of prerequisites a completion check had to satisfy, sometimes without adding a meaningful player decision. The remedy is to assign each quest one clear completion owner and add stages only where they represent actual intermediate commitments or durable requirements.

## What the references actually show

The supplied updated Luxcellia export has 863 world triggers, 635 static story effects in that map and a separate bank of 380 quest triggers. Those quest triggers contain accepted-status checks, semantic story conditions and quest-progress effects. Its quest completionCondition query strings are empty. Thus comparing only its world-trigger map to our explicit completion effects omits much of its completion system. The older synced Luxcellia reference has 847 world triggers; version choice matters. These counts are observed export facts, not evidence of better play.

The community reference documents that a detailed quest’s story completionCondition generates a completion trigger; an omitted condition requires an explicit completion effect. Native completion is simpler to author, but it still needs semantic recognition. Completion effects can chain subsequent work without another monitoring rule. [Quest reference](https://wiki.unofficial.voyage/world/quests).

Mechanical trigger gates constrain when semantic checks run. Once conditions pass, typed effects provide exact state changes; the story/action interpretation itself remains uncertain. Scope controls supported player effects, while conditions can match any player. A party-wide badge scan is not proof that a particular accepting player owns that badge. Evaluation budgets also make large banks of simultaneously eligible semantic checks worth testing. [Trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions).

## Completion ownership in Alpha23

| Kind | Implementation | Why |
|---|---|---|
| Finite personal favor, practical episode or single outcome | Detailed native completionCondition | Removes a manual stage flag and extra completion watcher |
| Short guild job with personal service credit and/or replay | One final verified settlement trigger | Keeps recipient-specific credit and replay bookkeeping at the actual handover |
| Real multi-stage assessment, expedition or consequential adventure | Explicit objectives | Preserves decisions, evidence or permission that genuinely must carry between scenes |
| Anomaly, trophy, rival encounter, access gate | World trigger | Exact one-time conditions and effects are the feature itself |

The classification covers all 112 quests: 60 native outcome checks, eight single guild settlements and 44 retained staged quests. Five older guild credit grants were moved out of all-player completion rewards into their existing player-scoped verification triggers. Fixed money and experience payments remain at their original values.

The export has fewer author-maintained world triggers, 308 instead of 361, plus native conditions replacing 21 manual quest triggers. Voyage can create completion checks from those native conditions at runtime. Do not present the lower authored count as a guaranteed speed improvement or absence of semantic checks.

## The alleged missing offer flags

All eleven flags have a dynamic writer in gh_guild_board.script: storage['q20_offered_'+j.slug]=true. The board also records an offer tick. Literal searches for a complete key or a typed write-boolean effect miss this expression. Executed fixtures covered each job: before browsing the flag was false; the board wrote it and the acceptance script could generate acceptance afterward. This establishes a writer in the current local file, not that every older upload or live semantic decision works.

A separate defect was genuine: four recurring guild jobs had completion-aware reset code behind outer acceptance conditions that excluded completed status. Alpha23 admits that status only for those repeat jobs, preserving the 20-turn cooldown and fresh-offer requirement. The board can also show eligible available, rejected, abandoned and expired postings when the player deliberately requests work.

## Multiplayer and testing limits

Shared quest outcomes and personal credentials are different. A rescued courier can be a shared result; licensure, badge promotions, service credit and academic eligibility must not be inferred for absent or unqualified bystanders. The new credit targeting removes an unconditional award to everyone, but it is not proof of correct live recipient selection.

The existing guild rank scan still checks all party members. That may fit a qualified team taking a shared contract, but it does not enforce an individual-license interpretation. Shared quest keys and storage also cannot represent several independent simultaneous copies of the same contract. Neither switching to native completion nor deleting triggers resolves those policy and engine-state questions. Live mixed-rank testing remains necessary; the release is not certified multiplayer-safe.

Test on a fresh game: one simple native quest completed away from the original scene; an actual field commission followed by its later report; a staged assessment; all four repeating jobs twice; rejection and return; mixed licensed/unlicensed players; and the complete anomaly → trophy → rival sequence. Confirm one completion owner, one payment, correct recipients, preserved evidence and no invented extra sign-off. Existing saves may retain old generated quest triggers and counters; an export change is not a save migration.

## Validation actually performed

The text cleanup indexed 25,304 string fields, changed 151 text fields and passed 55,146 local structural/preservation/length checks. The eleven dynamic offer writers passed 259 script-fixture and compilation checks. The quest revamp passed 2,304 coverage/reference/budget/preservation checks and 399 script/state fixtures and compilations. These checks do not evaluate Voyage’s language model or constitute live playtesting. Candidate files, manifests and exact test results are in the two authoring directories for this update.
