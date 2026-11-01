# Approved world and workflow decisions

These notes carry context between desktop and web chats. They supplement the actual JSON and creation guides; newer explicit user instructions take precedence.

## World identity

Glowhaven is a mostly human, autonomous, magic-heavy city around the **Evertree**. Its four academies have nuanced civic duties, not one-word personality cultures. Morning classes are mandatory; students have varied lives outside them. All authored academy students are adults in a four-year program. Faculty are trained, capable adults even when lazy, unpleasant or weak by their peers' standards.

The Great Sage governs; Archons are exceptionally powerful representatives and Conclave members; headmasters run their schools. Preserve canonical office holders and full names. Existing nations, realms and maps constrain generation. Ordinary new household rooms can be areas inside existing locations.

Drakenspire is a snowy dragonkin-majority alpine city with a higher fortress, sacred dragon skeleton and clan-based elective Jarl. It is allied with Glowhaven. Dragon worship and ancestors matter. Rovakthuun is the elusive gray lightning dragon; Orrum is an isolated named yeti, not a generic repeatable type.

Asterveil is predominantly wilderness with four regional biomes, a small fae settlement and expedition work. It remains midgame. Fae appearances vary broadly; most dragonkin are humanoid with human faces, horns, slit pupils, scales and thick tails.

## Magic and combat

All disciplines can be learned; affinity eases learning rather than restricting it. Affinity and starting studies are separate creation choices. One affinity is most common (65%), two 25%, three 10% for generated characters unless explicitly directed otherwise.

Logic: Arcane, Metal, Gravity, Enchantment, Space. Passion: Fire, Lightning, Earth, Wind, Water. Empathy: Healing, Nature, Light, Summoning, Soul. Intuition: Divination, Void, Illusion, Ice, Sound. Force and Finesse support physical delivery. No separate Endurance attribute. Magitech includes the former Artifice scope.

Spell invention requires Spellcraft; ordinary casting uses the discipline. Simple invention can be a quick experiment; difficult spells require research. Time is configured but reserved, absent from affinity and normal creation. Space has a Gravity foundation and difficult private travel. Public court-issued portal keys are separate permissions. Light is not Healing; Nature heals plants; Soul includes spell-specific necromancy.

Ordinary physical attacks and routine defense remain useful without spending Stamina. Demanding techniques spend it. Bonuses, cooldowns and other mechanics must use supported fields. Temporary conjuration does not generate endless permanent crafting supplies.

## Fixed events and consequences

The Evertree base is the Glowhaven portal hub. Authorized court keys regulate outbound public travel. All cross-realm returns go there. The level-20+ anomaly is a once-only surprise crossing into the Spider Realm, independent of briefing/exam completion. Its boss, Vhalessra, and authored mechanics stay unchanged unless requested. The boss trophy can enable the Ryūka Marufuji bazaar confrontation. Those are events, not reasons to turn every normal quest into a trigger machine.

Crime and Prison is a narrow system: deliberate evil killing of nonhostiles or destruction of multiple buildings can lead to a wanted poster after three turns. Torture alone, theft, accidents, self-defense and hostile combat do not trigger this automatic loop. Poster possession controls enforcement; discarding it stops this loop by user choice. Arrest needs an actual outcome. Automatic custody is solo-only. Actual prisoners have the fifteen-turn release loop; lawful visitors do not. The prison is a separate realm; Wraith Island is a Glowhaven location.

## Character and art authoring

Use given name then family name, including Japanese-inspired names. Named references in factual NPC records use full canonical names to prevent duplicates. Nonhumanoids can have different naming conventions. Cards are native NPC JSON by default and use the established format. No pronoun profile field, no redundant Faction profile bullet, no Structured Profile heading; role in faction stays. Equipment is a Basic Info paragraph, weapons first only when present. Appearance includes hair and eye colors. Concealment and knowledge is consistently present.

Do not add phantom sections or engine-state notes to public character prose. Give people ordinary pleasures, real flaws, relationships and independent wants. Not everyone is a hidden genius or secretly kind. Romance, appreciation, work and party membership are different.

Portraits are colorful crisp 2D anime illustrations, default waist/hip up, no text, with appropriate setting backgrounds. Major characters get suitable flair; minor characters retain polished art. Player portrait customization is flexible. Follow the actual portrait guide. Save PNGs under the exact NPC name. Existing uploaded media URLs are preserved during merges.

Reference cast: Ragnar Leonhart is the adapted gravity veteran, level 67, with his horse only in lore. Adoha Aonuma carries a magitech voice amplifier. Karia Morino's revised portrait is the less literal adaptation. Preserve the user's latest voices; descriptive voiceTag text may fall back to a stock voice and must not be called a verified celebrity voice.

## Guild, quests and public prose

International guild with a court-permitted Glowhaven branch. Bronze, Silver, Gold, Platinum; examination for licensure, genuine assessments for promotion. Posted rewards are paid in full. The guild's commission is background economics, not an extra deduction. Rank is not level, automatic enrollment, recruitment or portal permission.

Use native completion for simple ordinary quests; explicit stages only where evidence, permissions or real choices need them. One completion owner and one reward owner. Existing offer flags may have dynamic writers in gh_guild_board; test those rather than declaring them missing from a text search. First thesis is once per playthrough, not repeated paperwork.

Inventory descriptions, locations and dialogue must read naturally. Technical flags, save instructions, authored/generation notes and hidden conditions belong in internal fields and development notes. Short public patch notes are copyable Markdown and describe player benefits; do not expose Easter-egg conditions.

## Adventurers of Glowhaven — approved implementation

The sixteen-person cast, three native arcs, additional finite work and all sixteen portraits are implemented. Snow-spirit conflict permits force or negotiation. The Hydra Head researcher is an adult fourth-year, talented in research and weak in combat; the Stillwind Pearl exists but does not validate her original theory. Copper Laurels are comic opportunists, not compulsory lethal enemies. The two adventuring companies are factions, not automatic player-party membership.

Use the revised power anchors: academy faculty and headmasters generally 28–32, Archons 50–55, court elites 40–45 and Karia Morino 42. **Ilyra Stillglass remains level 100 and Ragnar Leonhart 67**, explicitly exempted by the user. Legendary creatures, Orrum and the Spider Realm are not subject to this ordinary cast rebalance. Level bands do not make every trained adult a famous prodigy.

Rentals and modest purchases should leave natural keys/deeds in actual inventory. Six fixed arrangements have native payment/key grants; arbitrary household keys still require supported item generation. No automatic offscreen rent deductions, eviction clock or passive income is implied. Losing a key does not erase legal ownership.

Public leads reveal circumstances rather than accepting quests or exposing secrets. Returning clients can acknowledge an actual outcome without becoming repeatable reward sources. Native arcs remain distinct from simple authored quests and exact event triggers; do not fabricate authored quest arcId fields.

The user approved an honor-based `quest done: Exact Quest Name` repair action for an accepted journal quest that fails recognition. It may settle ordinary rewards without independent proof. It is OOC, exact-name based and not NPC dialogue.

Ironman is optional and solo. The main world's native death flag remains false for ordinary modes; Ironman's instructions and an ending trigger reinforce final lethal outcomes. For native permanent death use the separate full-world Solo Ironman export, where the global flag is true. Do not claim a game-mode record can override that flag, or that AI instructions are a guaranteed native toggle.

Touring routines move existing Ragnar Leonhart, Adoha Aonuma and Karia Morino through actual addresses and pause for presence, party travel, combat, incapacitation and real commitments. Adoha's Asterveil visits remain in the settlement. Personal travel authorization does not confer portal permissions on the player. Orivelle's existing circuit is preserved.

## Character creation minor patch — 1 November 2026

Player affinities are optional: zero to three. No affinity is a valid choice, distinct from a learned discipline. Physical Foundations supplies +1 Force and +1 Finesse among the starting-study choices. The existing weighted affinity-count rule for newly authored NPCs is unchanged.

Ancestry and optional temperament have actual modest attribute/skill/resource benefits without forcing behavior. Starting attribute ceiling is 20 so selected bonuses have room; normal attribute awards remain two points every three levels, as supplied by the user. Do not reinstate the rejected slower five-level proposal or infer a newly approved normal spending ceiling.

Special Talent is optional with one choice. The user approved stronger gifts having trade-offs. Their actual modifiers, vulnerabilities and granted techniques own effects; they do not grant unlisted affinities, automatic success, unlimited recovery, chosen-god status or Space/Time access. Added cosmetic outfit/accessory/portrait choices do not grant equipment or stats. Waist/hip-up remains the default, with explicitly selected alternate player framing respected.

The accompanying instruction sets starting/base maximum Stamina to 100; the export's 80% rest fraction is preserved. Marika Hoshino stays at the user's level 30. No blanket NPC nerf was authorized for this patch. Ordinary working adventurer generation is generally 20–30; authored exceptional people retain their actual levels.

Preserve all supplied hosted images, voices, coordinates and music. The user removed non-badge item artwork; do not restore it from older exports. Artwork backfill for existing catalogue items remains unverified. The ambiguous needsMediaGeneration toggle is not permission to bulk-enable it.

The public announcement must not disclose this release's Stamina adjustment, alternate framing/camera additions, Default grouping or emoji compatibility work. Those belong in private development notes. Mention Bald, broader creation choices, talents, equipment and minor balance changes as requested.

Studio's 1 November rejection confirms that ability trait requirements still require a numeric `amount`, even though the engine ignores that value for a trait check. Author `amount: 1`. Estimated item prices must be nonnegative whole numbers inside their configured tier range. Portable validation and regression tests now enforce these constraints; do not lower tier boundaries to accommodate an incorrectly priced item.
