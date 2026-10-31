# Dragonkin Appearance Guide

Confirmed by the author, 2026-10-28. This supplements the existing NPC Portrait Creation Format and Location and Area Image Creation Guide. It defines species anatomy; it does not replace their art direction, portrait framing, pose selection or output rules.

## Canonical anatomy

Dragonkin are mostly humanoid people with human faces. Their draconic features include horns, scales along the sides of their faces, scales on the backs of their hands and arms, thick dragon tails, and vertical slit pupils. Their palms retain a human appearance. Colors and the amount of visible scaling vary between individuals.

For these people, keep the human facial structure clear. A reptilian muzzle, elongated snout or fully draconic head is not a substitute for the described face. Distinguish a dragonkin person from an actual dragon. Preserve each individual's hair, eye color, skin/scales palette, horn shape, body build and age from their card. A small adult body remains adult; a thick tail can be proportionate to that body.

The author's description does not establish wings, claws, digitigrade feet, universal breath weapons, innate flight, elemental affinities tied to scale color, a lifespan, or ancestry rules. Do not add those as universal facts. They can be decided separately or established for a particular approved individual.

## Portrait use

Use polished 2D fantasy-anime rendering under the main portrait guide. Put the actual diagnostic anatomy into the individual brief: human face, horn shape, side-face scaling, vertical slit pupils, thick tail, and dorsal hand/arm scales with human-looking palms when visible. A pose/crop need not expose both palms or every scale patch; preserve the anatomy of what is shown. Do not force a full-body crop just to display the whole tail.

Keep the person's approved identity, clothing, personality, equipment and actual location. The species description does not assign a martial personality, noble status, cold immunity or a casting style. Portraits and future map/environment images retain the shared world style, with Drakenspire's architecture and proposed environment palette detailed in Drakenspire - Map Art Brief.md.

For small background figures in Drakenspire images, use suitable humanoid silhouettes with horns and proportionate thick tails where readable. Background people remain secondary; do not turn each into a prominent named character or force every person in a mixed population to be dragonkin.

## Voyage data route

Keep the canonical species definition in relevant world lore and the Dragonkin NPC type description. During first-pass NPC creation, put the specific individual's visible anatomy into their `visualDescription`; retain narrated appearance in `basicInfo` as well. This also applies when their selected NPC type is a profession rather than the Dragonkin category.

The community reference says portrait generation uses `visualDescription` when populated and otherwise falls back to `basicInfo`. A label such as Dragonkin alone leaves too much visual interpretation to the model. Lore/type descriptions alone are not verified to be injected directly into every portrait request. This is why the character-specific appearance record matters. [Community NPC reference](https://wiki.unofficial.voyage/world/npcs).

The NPC-creation instruction now conditionally supplies the anatomy for actual dragonkin. Global `imagePromptConfiguration` is unchanged: the dragonkin definition must not be attached as an unconditional instruction to human, elf, animal or other portraits. The community reference describes those image settings as category-wide additions. [Community image-prompt reference](https://wiki.unofficial.voyage/ai/imagePromptConfiguration).

This route is a practical authoring measure, not an anatomy validator or a guarantee of generated-image compliance. No portrait has been generated or live-tested in this pass. Existing image URLs are preserved. The two authored dragonkin descriptions are aligned with the new anatomy without regenerating their portraits.


## 2026-10-28 — Lifespan, regional variation and Drakenspire

Dragonkin are roughly human-height and can live up to about two hundred years. Scale color is hereditary and cosmetic; it does not assign affinity, status, personality or morality. The amount of visible scaling also varies between individuals. Drakenspire's broadly European-inspired human features and the established desert populations' broadly Middle Eastern-inspired human features are regional variation within one species, not different biological races with different capacities. Keep each approved person's design rather than replacing it with a uniform regional face. Nahlah Qamar retains her established desert homeland.

Local Drakenspire clothing commonly uses wool, fur and thick practical layers. The city has a snowy alpine fortress above a lively lower shelf; its national map brief gives the environment context. Do not infer cold immunity, a martial occupation or a universal elemental affinity from living there.

The first-pass NPC appearance instruction conditionally includes the anatomy and these basic biological limits. The Dragonkin type and species lore supply the fuller definition. This is an authoring aid, not a guarantee that every generated portrait will comply; global image prompts remain unchanged. No portraits were generated in this expansion.
