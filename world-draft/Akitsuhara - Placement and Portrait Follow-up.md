# Akitsuhara — placed locations and completed cast portraits

This follow-up merges the author's location export `43fe08da-66f0-451e-bf62-281d8f699479`. All supplied x/y coordinates, region assignments and existing images are preserved. The country still has twelve map regions; location pins now use the author's placements rather than the original broad estimates. No location or area images were generated in this pass.

## Mirror-Reed correction

The supplied ninth tile shows wooded ridges, a narrow river and bridge, with reeds along its northern water margin. The earlier broad-lake/ferry interpretation was wrong. The region remains **Mirror-Reed Lowlands**, but its seven locations, their areas and encounter habitats now fit the actual woodland terrain.

| Retired premise | Current location |
| --- | --- |
| Mirror-Reed Ferry | Mirror-Reed Bridge |
| Reedglass Fishing Village | Reedglass Woodland Hamlet |
| White Heron Islets | White Heron Grove |
| Singing Reed Marsh | Singing Cedar Hollow |
| Old Ferry Shrine | Old Bridge Shrine |
| Saltwind Causeway | Mossbank Ridgeway |
| Reed Dye Workshop | Woodland Dye Workshop |

Yumi Sawatari becomes a bridge keeper and trail guide; Gorō Fushimi becomes a woodland hamlet headman; Aya Takino works with bark, roots and leaf dyes; Koma claims to be a boundary inspector and knows woodland shortcuts. Their names, appearances, personalities, levels and affinities are retained. Their equipment, local knowledge and motives change only where needed to remove the boating premise.

Two native quests become **Cloth on the Forest Road** and **Missing on the Ridge**. They now concern a pack-cart consignment and a delayed trail party. Their existing recommended difficulty, badge requirement, rewards and native completion ownership remain. All location/area keys, NPC addresses, lore references, board entries and script references are updated together. Retired names are kept in this historical change table, not the live world.

The capital branch is now **Adventurer's Guild - Benitsuru Branch**, matching Glowhaven's naming convention. Its areas, NPC addresses, starts, quests, scripts and developer fixtures use the same canonical ID.

## The author's onsen pin

The draft marker at **Benitsuru Basin (34, -45)** becomes **Hinoki Hollow Onsen**. Its four connected areas are Reception Porch, Washing Court, Stone Pools and Rest Veranda. A maintained side lane connects it with South Gate Caravan Yard. Existing nearby sites are not moved.

**Atsuha Yunokawa**, an adult human proprietor, brings the new cast to **97 NPCs**. She likes old festival songs and a good travel excuse, keeps a spotless bathhouse and makes unwise promises to impressive guests. Her Water affinity came from the recorded weighted affinity draw. A basic bath and clean towel cost six marks; there is no automatic bath-payment or healing controller.

## Portrait completion and review

The 82 previously pending portraits plus Atsuha's portrait are completed. The user also explicitly requested one fresh pass each for **Sana Kuroiwa** and **Shōen Kagetsuna**, then separately approved a covered-outfit replacement for **Misao Shingū** after the first API upload was rejected. The replacement uploaded successfully. Sana's selected portrait has a continuous aligned walking-spear shaft with its head attached. Shōen's selected portrait has clear Earth effects, two properly rooted swept ivory horns and no foreground people.

Each other supporting character received one generation call. The update’s public name is **Steel and Spirits**. The four Mirror-Reed residents were generated after their cards were corrected, so no new portrait needs an obsolete ferry/fishing-village background. Exact NPC keys, filenames, PNG hashes and hosted URLs are recorded. Completed outputs were checkpointed to disk; 56 earlier results were recovered from this chat's generation-event metadata after a crash without repeating their calls. No conversation content or credentials were exported into the repository.

The original PNGs remain unchanged by the labeled review sheets. The complete roster retains varied colors, recognizable jobs, the approved local flowing effects and unusual yōkai anatomy. Some effects are subtle, especially on **Kazuma Ebisawa, Hokuto Mizusawa, Yasuo Natori, Takuro Namiki and Hiroto Sakuma**. Jin Lin's bird-beastfolk traits are less obvious at thumbnail size. Several portraits still have tighter headroom than the guide target; no automatic extra pass is authorized or claimed. The review sheets let the author select any later redo deliberately.

The portrait authoring guide and runtime NPC image instructions now require continuous straight spear/polearm shafts, collinear grips and attached heads. Future briefs also repeat that narrow rule. It does not change weapons or create new abilities.

## Verification and live checks

The regression suite checks every supplied coordinate/region, retired-ID absence, local paths, all seven forest locations, the four corrected residents, the onsen and the shared guild name. Portrait application is restricted to the 83 new supporting URLs and the explicitly selected Shōen replacement. Existing valid portraits elsewhere are preserved.

Official draft validation, final upload totals and delivery hashes are in the release receipts. These do not constitute a live story playtest or a Studio save/publication. Test the renamed guild opening, both rewritten contracts and the onsen's ordinary transactions in Voyage. Existing saves using retired names may require explicit repair; no automatic save migration is claimed.

## Starts and creation follow-up

All 25 selectable descriptions use plain text, and each of the eight foreign descriptions explicitly identifies its starting realm. The Glowhaven adventurer opening is immediately above the Akitsuhara starts. A new narrowly scoped authorization event lets foreign starters obtain a Glowhaven Portal Key from their local transit desk before crossing; it leaves existing fixed returns and post-transit key grants intact.

The optional Past Experience category has 14 histories, including veterans, former adventurers and criminal pasts. Seven more Drakenspire origins cover the three clans and community life. Physical Foundations now grants +1 Force Combat and +1 Finesse Combat as well as its existing +1 Force and +1 Finesse. Clan origins mean ordinary household membership, with the player’s own branch left open.
