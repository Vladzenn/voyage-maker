# Next patch — observed issues and pending Studio edits

Recorded 1 November 2026. **Status after the Character Creation & Polish patch:** the latest Studio edits are merged, and badge single-owner/anti-alias guidance is implemented. Actual badge behavior and catalogue artwork backfill still need live verification. The original evidence below remains relevant; it is not a claim that the fixes were playtested. Do not restore removed images or older progression/mode labels.

## Duplicate Bronze guild badge — observed

The user's inventory screenshots show two distinct records:

- `Guild Badge: Bronze`: category **Document**, with the intended pregenerated badge image and licence description.
- `Bronze Guild Badge`: category **Relic**, a different description and an estimated value of 15 marks, without an image.

The canonical catalogue defines only `Guild Badge: Bronze`. The typed `gh_guild_exam_certify` reward grants exactly one of it to satisfying players. The alternate `Bronze Guild Badge` is absent from the current catalogue. This supports investigating an additional runtime-generated reward, but the screenshots alone do not establish which task or turn created it.

Next investigation: trace the licensure scene, certification effects, item-update output and relevant reward narration. Establish one owner for the badge grant and reuse its exact existing identity. Check examination and any prelicensed start separately. Preserve the correct badge artwork and rank checks. Do not blindly delete items from an existing save or replace the intended Document with the generated Relic.

Implemented: typed certification remains the sole Bronze award, the quest has no second badge payout, and item generation is explicitly barred from defining/granting a renamed badge for the same ceremony. No old-save item deletion was introduced. Next step remains a fresh playtest trace, not another speculative grant trigger.

Acceptance test: one successful licensure grants one canonical Bronze badge, visible once under its intended category; subsequent dialogue does not produce a renamed copy. Existing badges retain their artwork.

## Missing runtime item artwork — observed; cause unresolved

The pregenerated Bronze badge image displays correctly. The shown Padded Handwraps and alternate runtime badge have no artwork. This demonstrates that missing item artwork was not automatically filled in the observed session; it does not establish that every runtime-generated item lacks images.

The local world has `itemSettings.imageGenerationEnabled: true` and an item-image prompt. User toggling **Needs media generation** in Studio adds per-item `needsMediaGeneration: true`; the original Mark entry omits the field and Studio displays the toggle as off. Do not assume this flag controls artwork: the documentation lists it without sufficient runtime explanation, and `mediaContent` is documented as readable text while `imageUrl` stores artwork.

Next investigation: inspect the toggle's actual tooltip/help, then compare an existing catalogue item, a newly generated item and a readable item in a fresh test. Establish whether image generation is triggered by creation, acquisition, inspection or an explicit generation request, and whether the per-item flag is relevant. Do not bulk-enable it for currency or the entire catalogue without evidence.

Acceptance test: document which item classes generate images and when, retain the guild badge art, and make only supported configuration changes. If existing catalogue artwork cannot be generated automatically, state that limitation clearly.

## User edits to preserve on the next merge

- Merged: guild badge images retained; fifteen other catalogue image URLs removed as supplied.
- Merged: correct **💀 Permadeath Mode** key/name and matching ending trigger. The formerly blank mode label is no longer present.
- Merged: attribute awards every **three levels**, retaining two points per grant. The earlier five-level proposal was not approved.
- Merged: thirty-three new location images, sixteen hosted NPC portraits and Marika Hoshino at level 30. Starting/base maximum Stamina follows the explicit request for 100 while retaining the exported 80% rest fraction.

References: [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings), [Items](https://wiki.unofficial.voyage/world/itemTypes). The behavior above separates user-observed playtest evidence from documented fields and untested explanations.
