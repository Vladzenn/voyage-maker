# Runtime Text Audit — Alpha22

The complete working world was indexed: 25,304 string fields, including identifiers, URLs and technical state. Pattern matches were reviewed by field purpose rather than deleted blindly. This is a static content and preservation audit, not proof that every phrase is optimal or a live model evaluation.

## What caused the problem

Local authoring instructions were copied into runtime prompts, and machine-facing continuity notes were appended to public descriptions. The text was often useful to an author but addressed the wrong consumer. Previous validation concentrated on references and selected field caps; it did not catch these content-boundary mistakes or the later Asterveil prompt-size additions.

## Fixed

- Applied the supplied shorter NPC-generation section and the newer strict anime portrait prompt with its style blacklist.
- Removed local guide-file dependencies, PNG naming/saving workflow and claims about editing saved state from image prompts. Rendering instructions remain.
- Rephrased repeated “authored contact” and “reuse the existing character” notes as natural public place information. Names and roles remain.
- Removed the guild’s contract-authoring recipe, obsolete temporary-pin note and imported Luxcellia rank reference. Actual badge rules and reward terms remain.
- Cleaned implementation vocabulary from the spider trophy recess, beast sightings, public faction descriptions, item/ability text and four skill descriptions.
- Replaced schema-limit commentary and selected production language in world lore with world facts. Actual Time restrictions remain in the appropriate skill and task guidance.
- Shortened seven public starting-choice descriptions while retaining their existing mechanical grants and hidden narrative rules.

The exact before/after path ledger is `authoring/runtime-content-audit-2026-10-29/change-ledger.json`. It contains 151 changed text fields. No quest, world trigger, objective gate, badge grant, NPC level, faction assignment, image URL, map coordinate or portrait was changed. Three boss public summaries received wording cleanup; hostility and native relationship values remain intact. Developer test labels are intentional and were retained. “Lecture Studio,” crafting mechanisms and similar false positives were retained.

## Offer-flag investigation

The claimed eleven missing writers are present in this local export. `gh_guild_board.script` iterates job records and writes `storage['q20_offered_'+j.slug]=true`, plus the corresponding offer tick. The literal field names do not occur as typed write-boolean effects because the script constructs them dynamically.

The board and acceptance scripts were executed for all eleven affected jobs with supplied badge/status/action fixtures. Each expected flag was written and each acceptance script produced its quest-accept effect. That disproves a missing-writer blocker in this version; it does not prove semantic recognition, live timing or an older uploaded export works. See `offer-writer-tests.json` for every tested quest and writer.

## Deliberately retained under the hood

Output-field contracts in actual generation tasks; strict reward/ownership rules; identity resolution; hostility; travel authorization; evidence and knowledge boundaries; and actual trigger scripts. These guide the correct runtime consumer. Repetition across separate AI tasks can be necessary because each task receives its own instructions. The cleanup did not replace detailed guidance with generic prose.

## Validation and delivery

The complete export and all eighteen section maps are synchronized. All AI task and leaf sizes, image prompt sizes, relevant catalogue/description limits, world size and preservation constraints were checked locally. The file includes the corrected 4,469-character NPC portrait prompt. No live Studio import, playtest or existing-save migration was performed.
