# Next patch — observed issues and pending Studio edits

Recorded 1 November 2026. **Investigation backlog only; no world changes applied.** Use the user's next Studio export as the merge base. Do not silently restore removed images or the older progression/mode labels from the local canonical world.

## Duplicate Bronze guild badge — observed

The user's inventory screenshots show two distinct records:

- `Guild Badge: Bronze`: category **Document**, with the intended pregenerated badge image and licence description.
- `Bronze Guild Badge`: category **Relic**, a different description and an estimated value of 15 marks, without an image.

The canonical catalogue defines only `Guild Badge: Bronze`. The typed `gh_guild_exam_certify` reward grants exactly one of it to satisfying players. The alternate `Bronze Guild Badge` is absent from the current catalogue. This supports investigating an additional runtime-generated reward, but the screenshots alone do not establish which task or turn created it.

Next investigation: trace the licensure scene, certification effects, item-update output and relevant reward narration. Establish one owner for the badge grant and reuse its exact existing identity. Check examination and any prelicensed start separately. Preserve the correct badge artwork and rank checks. Do not blindly delete items from an existing save or replace the intended Document with the generated Relic.

Acceptance test: one successful licensure grants one canonical Bronze badge, visible once under its intended category; subsequent dialogue does not produce a renamed copy. Existing badges retain their artwork.

## Missing runtime item artwork — observed; cause unresolved

The pregenerated Bronze badge image displays correctly. The shown Padded Handwraps and alternate runtime badge have no artwork. This demonstrates that missing item artwork was not automatically filled in the observed session; it does not establish that every runtime-generated item lacks images.

The local world has `itemSettings.imageGenerationEnabled: true` and an item-image prompt. User toggling **Needs media generation** in Studio adds per-item `needsMediaGeneration: true`; the original Mark entry omits the field and Studio displays the toggle as off. Do not assume this flag controls artwork: the documentation lists it without sufficient runtime explanation, and `mediaContent` is documented as readable text while `imageUrl` stores artwork.

Next investigation: inspect the toggle's actual tooltip/help, then compare an existing catalogue item, a newly generated item and a readable item in a fresh test. Establish whether image generation is triggered by creation, acquisition, inspection or an explicit generation request, and whether the per-item flag is relevant. Do not bulk-enable it for currency or the entire catalogue without evidence.

Acceptance test: document which item classes generate images and when, retain the guild badge art, and make only supported configuration changes. If existing catalogue artwork cannot be generated automatically, state that limitation clearly.

## User edits to preserve on the next merge

- Keep guild badge images; the user intends to remove other catalogue item images in Studio. This image removal is not yet applied locally.
- Rename Ironman to **Permadeath**. The reviewed export had a blank mode label (`💀  Mode`); both its key and `name` should be `💀 Permadeath Mode`. The reviewed export has not been merged locally.
- The user is changing attribute awards to an interval of **three levels**. Preserve the actual grant amount, cap and other progression settings in the next export rather than assuming the earlier five-level proposal was approved. No progression change has been applied locally.

References: [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings), [Items](https://wiki.unofficial.voyage/world/itemTypes). The behavior above separates user-observed playtest evidence from documented fields and untested explanations.
