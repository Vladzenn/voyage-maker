# Second audit: findings and implemented response

2 November 2026. Baseline: current controller-2 full world, followed by the author's NPC export `75209dda-5945-4619-a577-43038ded7c7f`. User requests restore a simpler bracket, redo the full portrait roster, and give the cast a less uniform moral/personality range. The later rental question is clarification only; rental mechanics are unchanged.

| Finding | Judgment | Response |
| --- | --- | --- |
| Four earlier failures were addressed | Supported by prior actual-script fixtures | Retained start, incapacity, double-KO and explicit-forfeit safeguards. |
| The card is a gauntlet rather than an elimination bracket | Correct design discrepancy, not a hidden runtime bug | Restored a small four/eight-entrant bracket with recorded NPC eliminations and an eventual champion after player loss. |
| Zero Health in the lounge can settle a live bout | Reproduced for both opponent and player | Native settlement now requires both actors in the exact arena. An interruption latches a need for an actual official semantic ruling; later return cannot launder unrelated incapacity. |
| A second human cancels the entry | Reproduced; originally an explicit solo-only safeguard | Changed to suspension without cancellation/transfer, retaining the solo-only controlled format. Full multiplayer spectators are not falsely claimed. |

Historical reproductions: `second-audit-v2.json`. Tests execute the actual emitted JavaScript in an isolated fixture; they are not live Voyage tests. A supplied `true` semantic answer proves what a script does after a match, not whether the AI would judge that scene correctly.

## Complexity kept out

There is no live simulation of every NPC attack, bracket-specific combat resource engine, bench keyword classifier, review/replay loop, absence grace period or new conversation state machine. The bracket only records official abstract NPC results. Registration, readiness, official outcomes, withdrawal, care and collection still use semantic gates. Health checks are a narrow contradiction safeguard rather than the meaning of every result.

## Documentation and limits

The [current trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions) documents semantic `action`/`story` checks, mechanical filtering, planning/state timing, persistent script storage and native effects. The implementation retains existing IDs and adds one semantic double-elimination ruling, so a medical move/recovery cannot obscure a genuine simultaneous knockout. Each emitted trigger is checked against the live authoring size/condition/effect limits.

No changes to the Spider Realm or rental implementation. Supplied map and location artwork/coordinates remain unchanged. The NPC merge preserves all unrelated records and every authored level, affinity, item and ability. Forty-two cast cards receive individual behavior/secrets; Threnvoss's card is unchanged apart from the explicitly replaced portrait URL.
