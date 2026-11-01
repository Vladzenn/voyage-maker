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

Minor patch titles use a randomly chosen, unrelated animal emoji plus `Minor Patch n`. No descriptive subtitle in the title; thematic headings may appear in the body. The latest published minor release is **🐙 Minor Patch 3**, so the next new minor release is **Minor Patch 4**. An import hotfix to the same release is not automatically a new numbered patch.

## Champions of the Crucible — planning decisions, 1 November 2026

Plan before implementation. First format: individual championship bouts, regulated nonlethal even in Permadeath, full Health/Mana/Stamina treatment between bouts, finite summons allowed, no outside interference. Leaving the venue withdraws the entrant from that edition. About thirty-two new named fighters. A hundred completed game turns between editions replaces the proposed narrated-day cooldown. Opponent selection should preserve existing NPC levels rather than resize the cast.

New Nature/Soul plant-undead dungeon targets approximately levels 35–50. Its discovery uses the actual Evertree Portal Room plus a championship trophy and Silver Web Portal Key; no spider-queen victory was requested. Preserve the existing Spider Realm and anomaly behavior. The Sepulchral Conservatory premise and named caretaker remain creative proposals.

Oni lore direction: predominantly Edo-inspired countryside/towns, samurai, shinobi, independent factions, Shogun and yokai, with some more-developed Arcane/Soul magitech. No modern metropolis or carved-face mountain. This update prepares lore and modest ancestry details, not the Oni map/realm or spirit portal expansion. The detailed plan separates supported mechanics, observed reference configuration and live-test uncertainties.

## Champions of the Crucible — implementation decisions

The user authorized the full package in one release. Use a persistent opt-in world activity rather than a native character-creation Game Mode. First controlled championships and exhibitions support one human; NPC companions remain outside combat. Do not silently enroll a multiplayer party. A changed human roster pauses review; prize ownership keeps the registered human name.

Latest medical steering supersedes the stricter planning requirement: care/rest is appropriate and optional. Do not invent injuries when unharmed, confuse low Mana with wounds, or gate readiness on exact maximum resource values. Normal narrative/resource updates handle accepted player care; this is not a verified heal-to-max API. Results are recorded before treatment, and later recovery cannot turn a loss into victory.

Semantic action/story recognition handles actual commitments and sporting decisions. The bracket's stored state owns entrant selection, eliminations, current match, result, 100-tick break and one prize dispatch. There is no championship quest, invented spawn effect or per-bout native permadeath switch. Native knockout/medical timing and semantic recognition require Voyage testing. NPC-only brackets are abstract recorded results rather than fake offscreen combat.

The Sepulchral Conservatory has two tending wings in either order before its gated heart, a safe return refuge, optional investigation and finite creature-type encounter guidance. Both physical circuits must actually be settled; lost keepsake seals do not undo repairs. Threnvoss is the level-50 named caretaker. Actual defeat or genuine release shares one trophy owner. Portal discovery requires the championship trophy plus Silver Web Portal Key at Evertree, with no spider-queen-victory prerequisite and no change to the Spider Realm.

Public notes are a thematic major announcement. Forty-three one-pass portraits and four dungeon environments accompany the native JSON; no unavailable hosted URL is fabricated. Preserve artwork mismatches in the review manifest and obtain a new request before re-generating under the one-pass portrait rule. Sources and the original AGENTS.md remain unchanged.

The author clarified the announcement-length distinction: **minor patches are simple; major releases are more wordy and visually inviting**. Major notes should explain the playable experience through descriptive sections and useful detail, rather than using the same brief checklist as a minor patch. The guide now suggests roughly 400–700 words for a substantial major release, scaled to actual content. Preserve the existing rules against spoilers, internal machinery, padding and unverified claims. The Crucible announcement was expanded; no world mechanics changed in this follow-up.

The author also requested a little unlock information in the major notes. Include the Conservatory entrance requirement in natural terms: carry a Crucible championship trophy and Silver Web Portal Key to the Evertree Portal Room. This is an explicit exception to withholding that hidden condition; later dungeon discoveries remain unspoiled.

2 November public-copy refinement: the author's edited announcement favors a mysterious rumor over an explicit unlock checklist. Refer to a champion's prize and a key from a silken descent beneath the Evertree, without inventing a blessing or favor mechanic. Keep the expanded fighter-roster point and the Oni preparation for the next major update. Retain the author's removal of the closing solo/team-format paragraph from this announcement; this editorial choice does not change runtime capabilities or the mechanics guide.
