# Leveling pace and local place names

Read-only reference comparison and the approved two-field pacing update, 2 November 2026.

## Documented mechanics

The current [community Level Progression reference](https://wiki.unofficial.voyage/mechanics/progressionSettings), fetched directly after the web reader failed, defines the requirement for target character level N as `startingCharacterLevelUpRequirement + (N - 2) * extraRequiredXPPerCharacterLevel`. Level 2 therefore uses the starting requirement. These fields control character progression, not discipline skill XP. No new schema field or XP trigger is required.

The community reference is not official engine source. The official Creator API contract was also fetched; the existing native fields and our local world provide the observed configuration. Local schema/script checks do not measure live XP recognition or actual turns per level.

## Approved change

Only the two native character-XP requirements change: starting requirement 1,000 → 400, increment 400 → 50. Actual cast levels, all XP sources, skill requirements, resource growth, level rewards and the 150 character cap remain unchanged. This supersedes the tentative general cast-nerf idea for this patch.

| Character-level advance | Previous required XP | New required XP |
| --- | ---: | ---: |
| 1 → 2 | 1,000 | 400 |
| 2 → 3 | 1,400 | 450 |
| 4 → 5 | 2,200 | 550 |
| 9 → 10 | 4,200 | 800 |
| 19 → 20 | 8,200 | 1,300 |
| 29 → 30 | 12,200 | 1,800 |

These are individual advancement requirements, not promised turn counts or an assertion that any particular action awards XP. Fresh tests should compare actual quest, combat and skill-growth play. Faster access to a configured level gate is an intended consequence; the Spider event and boss themselves are unchanged.

## Observed Luxcellia configuration

Latest supplied reference: attachment `5f2c3317-f5d6-44fd-aabf-64f3b95caeb0`, identical to the later-audited `5cea9875-694c-4946-ac86-59cfaa9d471d` file, containing 279 locations and 1,603 nested areas. The older `sources/Luxcellia.json` remains untouched.

Its character curve is still 1,000 + 400. Other rewards differ: its `charXPPerSkillLevel` is 40 against our 5, and discovery XP is 30 against our 10. These observed values do not establish overall play speed. We did not copy those rewards on top of the new curve.

For names, `Adventurer's Guild Central Branch` contains a mix of longer keys and shorter scoped keys such as `Central Branch: Mess Hall` and `Central Branch: Materials Desk`. `generateLocationDetails / Scoped Area Names` requires exact parent-qualified structured references. `summarization / Location Continuity` explicitly permits a short local nickname when its parent is established. Its movement instruction resolves ordinary rooms, doors and local guilds within the current scene, avoiding a global search by shared nouns. The observed area records contain description, paths and images; no area-alias field is used in that export.

Our `generateActionInfo / Local Movement and Explicit Commitment` already resolves shortened area names within the current parent before asking for clarification. The current canonical guild title is verbose; a future reference-safe rename could shorten its location and area prefixes while retaining unique scope. No keys were renamed in this patch, and short-reference AI guidance is not a guarantee of perfect native destination matching.
