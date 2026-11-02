# Beginner contracts and fieldwork — 2 November 2026

## Scope and design

The author requested starter nuisance fights, further options at levels 7 and 15, and a few interesting contracts rather than a rewrite of the quest catalogue. The opening and guild licensure are unchanged. Nineteen finite native quests and eighteen NPC types are appended. Six existing introductory briefs are the only old quest prose edited; the boar notice also now describes the juvenile in its brief. Every old objective, completion condition, work-proof trigger and reward effect remains exact. No cast rebalance was made.

New jobs: seven beginner commissions, six practiced Bronze commissions and six experienced commissions. The latter include four Silver and two experienced Bronze postings. Higher badges can take lower work. The first ordinary licensed browse offers the inn rats and the existing parcel delivery; later browsing rotates a combat/problem-solving posting alongside another kind of work. Native acceptance remains the player's choice. A named harder request can open an eligible-badge notice with a warning; it never auto-accepts. Mixed-human routine offers use the lowest human level, not a veteran companion's power.

Newly created types describe finite creatures and useful counterplay. They do not spawn an encounter by existing. The accepted quest's work site and the encounter task guide actual generation. The inn gains one connected cellar area; no new map location or existing image is changed. Ordinary fields and the protected Spider Realm retain their existing settings.

Most jobs are direct. A few have a modest reveal or choice: lamp polish attracting moths, an imp bargaining over stolen working parts, a broken rescue signal. There is no universal twist rule, guaranteed capture, required spell discipline, concealed alpha or compulsory next quest. Existing salvage/competing-party jobs were already interesting and remain unchanged.

## Reference comparison and mechanics

- The latest supplied Luxcellia reference (`5f2c3317-f5d6-44fd-aabf-64f3b95caeb0`) has briefs that describe motives, obstacles, choices and possible endings, including Guild Bounties and Academy Trials. That narrative structure is useful. Its template-heavy completion architecture and universal bounty-twist suggestion are not copied. A large reference catalogue is not proof that every engine path works.
- [Community quest reference](https://wiki.unofficial.voyage/world/quests): detailed quests can have typed `completionCondition: {type: "story", query: "…"}` and completion effects. `quest-init` surfaces an available quest; native acceptance is distinct. New contracts use this ordinary lifecycle, without authored acceptance/completion state machines or per-job offer flags.
- [NPC-type reference](https://wiki.unofficial.voyage/world/npcTypes): type-level fields include description, damage arrays and successBonus. Individual level, tier, healthMultiplier and damageModifier are not invented type fields.
- [NPC reference](https://wiki.unofficial.voyage/world/npcs): level and actual individual modifiers affect power. The New NPC task supplies explicit modest profiles for generated guild creatures; the encounter task stages them at the actual work site. This is AI-guided creation, not a verified hard spawn clamp or per-hit damage cap.
- The official public [Creator API contract](https://api-alpha.aidungeon.com/creator/v1/openapi.json) was retrieved as `1.3.0-preview`. It describes the API envelope but does not contain `completionCondition` or a detailed game-state Quest schema. It cannot independently certify these native fields. The community reference, existing current-world schema and local validators support this implementation; a fresh Studio import remains necessary.

Root triggers remain **409**. Only the existing `gh_guild_board` script changes. It retains all eleven old `q20_offered_*` writers and the old repeat cooldown. Each new finite job has one native completion query and one effect list paying Marks, XP and one Guild Service Credit. Existing older jobs retain their original, sometimes separate, settlement/service-credit owners. No quest progression flags were added.

## Calibration and limits

Beginner individuals normally use level 1–3, weak/trivial tier, damageModifier -50, damageReductionModifier 0 and healthMultiplier 0.7. Practiced Bronze creatures use the stated local band, weak tier, damageModifier -20 and healthMultiplier 0.85. Routine new opponents are capped in guidance at the least experienced human +2 within their described band. Explicit warned harder requests retain posted danger. Experienced work is around levels 13–18 with ordinary average-tier modifiers. Type successBonus is used; extra bonuses are not stacked on top.

These profiles need actual generated-record and combat observation. The engine's damage output remains authoritative. No second narrative damage deduction, free follow-up hit, continuous lethal poison, endless reinforcements or live rescaling of a resolved actor is authorized. Foreseeable retreat and effective alternatives are preserved. This does not weaken authored people, existing bosses or the anomaly dungeon.

## Validation and review

`tools/fieldwork/manifest.json` records the baseline hash, all additions, exact unchanged quest/effect fingerprints, all untouched triggers and sections, and original creature types. The older Crucible preservation fixture was refreshed only for the two appended sections and the inn's explicit area addition. Original NPCs, media, starts, skills, equipment, maps, coordinates, quest triggers and Spider fingerprints are unchanged.

Portable tests exercise rank/level filtering, first browsing, level-7/15 availability, mixed-human groups, deliberate harder requests, completed/accepted job exclusion, old offer-flag writers, single reward ownership and preservation. Full project schema, item, creation, adventure and Crucible regressions pass locally. No live Studio save, AI-recognition guarantee or existing-save migration is claimed.

### Voyage test checklist

1. Fresh guild start: finish the existing licensure route normally; browsing offers a basic fight and a utility choice without enrolling the player automatically.
2. Accept the rats, enter the connected cellar, inspect the generated individual: exact type, explicit level, modest tier/modifiers. Check actual hit damage, escape and the separated second rat. No extra nest appears.
3. Complete with either a fight or trapping and close the gap. Native completion pays once; reopening the board or returning to the cellar gives no second payout or respawn.
4. Check level-7 and level-15 offers with Bronze and Silver badges; test a low-level human alongside a veteran human. Explicit harder requests get a useful warning.
5. Try the imp bargain, a repair solution and a straightforward hunt. An ordinary job should end at its actual agreed scope, without a universal return report or compulsory sequel.
6. Recheck the original parcel proof handoff and a fresh recurring boar job. Their original settlement behavior must survive the brief edits.

## Release

The author confirmed **Champions of the Crucible is unreleased**. Bundle this content and the already-applied 400/+50 XP curve into that major announcement. The separate Minor Patch 4 leveling draft is superseded, not published. Full import: `output/fieldwork-2026-11-02/The Schools of Magic, Arise! - Beginner Contracts and Fieldwork.json`; canonical world and current revised full-world alias match it.
