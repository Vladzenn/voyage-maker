# Character creation and polish — development notes

Implemented 1 November 2026 from the user's supplied Studio export `b44dcd0f-0fe6-49d9-9b55-34301190d203`. Source SHA-256 and preservation fingerprints are in `tools/phantom/manifest.json`. The public announcement intentionally omits the requested internal details. This file is author-facing.

## Source and scope

The supplied export is the merge base. It contains thirty-three added location images, all sixteen new Adventurers portraits uploaded to genuine hosted URLs, Marika Hoshino at level 30, the correct Permadeath mode/trigger rename, a three-level attribute-award interval, and the removal of fifteen non-badge item images. Those edits are retained. All NPC records and all location/map records are preserved exactly from that source, including Spider Realm images; no Spider progression, enemy, encounter or reward changes were made.

The export actually had 80 starting/max Stamina and a rest fraction of 0.8. The user's accompanying instruction explicitly requested 100, so initial and base maximum are 100; their 0.8 rest fraction remains. The old prose claiming full recovery on every rest was corrected to the actual 80% fraction. The existing actual-new-day full recovery rule remains. Attribute awards stay at two points every three levels and the normal spending ceiling is unchanged.

## Creation implementation

- Natural affinity explicitly permits zero to three selections. A skipped choice means no chosen innate affinity; it is not an invitation for biography generation to invent one. Native categories allow zero selections, so no incompatible “None plus three affinities” trait was added.
- **Physical Foundations** is first in Starting Magical Study and grants exactly +1 Force and +1 Finesse, without a spell or affinity. That category still permits up to two choices, including a physical/magical combination.
- Thirty-six professions were added to the preceding twelve. Each supplies a +2 main skill and +1 support skill; existing professions gain a comparable supporting benefit. Prior work does not grant employment, licence, premises, free tools or a current teaching subject.
- Each of the eight ancestry choices now has +1 attribute, +2 skill and a modest resource-capacity bonus. Each of the twenty optional temperament traits has +1 attribute and +1 skill. They retain individual anatomy and player agency rather than forcing moral alignment or actions.
- The starting attribute ceiling is 20, allowing the new ancestry, temperament and talent contributions to matter alongside the selected aptitudes. This is a creation ceiling, not a change to later spending cadence or a new damage multiplier. All attribute-to-damage and attribute-to-damage-reduction maps remain as supplied.
- **Special Talent** is optional with one selection total. Forty-eight original choices are grouped by instinct/ingenuity, martial gifts, arcane peculiarities and blessings/burdens. Twenty-four grant a distinctive finite technique. Strong capacity gifts have actual resource penalties; elemental protection gifts have actual vulnerabilities. Native trait modifiers, grants and damage profiles own the mechanics. Ability descriptions own their committed costs; no extra resource or unsupported effect fields were invented.
- Talent techniques require the corresponding trait for later availability. They do not unlock merely from a modest general skill. A selected gift may supply its explicitly listed discipline, without silently adding an affinity or mastery of other disciplines. No Space or Time starting gift is included, and talents are not added to the repeatable milestone pool.

Luxcellia's Divine Blessing/Cheat Skills categories informed the grouped optional menu and visible identity of a gift. Their intentionally overpowered bonuses, sovereignty, free shops, universal knowledge and automatic success were not imported. Our gifts have explicit moderate grants, costs and limits. See `Phantom Patch - Creation Guide.md` for the actual mechanical list.

## Appearance and equipment

Added explicit Bald; thirty-two outfits; thirty-two accessories/outer layers in a separate optional category; additional framing/camera choices; and twenty-eight backgrounds. The usual waist/hip-up framing and natural camera are grouped as Default. More unusual choices are visibly grouped separately. Portrait selections remain mechanically empty. A selected close-up or full-body player composition overrides default framing without changing the manual NPC portrait process. The player handoff and shared image prompt agree; no residual full-body blacklist cancels an explicit player choice.

Forty actual items include additional thrown weapons, flexible weapons, guard implements, polearms, casting tools and a few ordinary/whimsical goods. Sixteen further starter kits reuse these actual definitions. The equipment category still allows one kit. New weapons use the existing Force/Finesse/Guarded methods; no weapon-family skill, free mastery, extra attack or unsupported equipment field is introduced.

## Music

The official community reference distinguishes native scene cues from mood/scene `matchTags`, and supports explicit pin/clear effects. The existing Fighting family had both the combat cue and broad tags such as attack, strike and battle. It now uses the combat cue alone. Dead and Travelling similarly use their corresponding native cues. Generic words likely to match ordinary conversation, an empty resource pool or floating-island scenery were removed from several other mood families. MashMode and every audio URL/variant are preserved. A short Story instruction keeps mood/context about the actual present scene rather than a discussed subject.

This reduces obvious false matches without building another trigger system or taking over the single pinned-track slot. No new music trigger was added. It cannot guarantee perfect engine context/mood classification; verify calm combat discussion, a real fight, aftermath, a memory of death, a road journey and Asterveil conversation in play.

## Badge duplication and artwork

There remains exactly one typed Bronze issuance owner, `gh_guild_exam_certify`. It consumes the real applicant's pass records and grants the existing Document `Guild Badge: Bronze`. The licensure quest has no separate item payout. The inventory-generation instruction and ceremony instruction explicitly reserve all four exact badge identities for their typed effects, and prohibit creating an alternate `Bronze Guild Badge` Relic from the handover. This addresses the likely duplicate-reward path while retaining ordinary item generation. No alias was added to the catalogue, and no generic cleanup deletes possessions from old saves. The actual source of the playtest duplicate still needs a fresh licensure trace; static tests cannot prove model compliance.

Runtime image backfill for existing catalogue items is **not confirmed**. The global artwork switch is already true. The user-provided tooltip for the per-item flag was only “Controls whether needs media generation applies to this item.” The browser helper failed before page access with a Windows sandbox lock/access error. Neither proves that `needsMediaGeneration` controls artwork rather than another media workflow. Consequently no bulk flag changes, fake image URLs or image-generation triggers were introduced. The user's badge-only artwork choice is preserved. This issue remains open rather than being announced as fixed.

## Levels and menu compatibility

The supplied named-NPC medians are Glowhaven **27** across 229 positive authored levels, Luxcellia **22** across 372, and Chikara **18** across 110 positive levels. These are role-mixed figures; missing/zero levels were excluded. They do not justify a global nerf. Ordinary working adventurers have a generation anchor around 20–30, with explicitly exceptional veterans preserved. No further cast level changes were made beyond retaining the user's Marika edit. Ilyra Stillglass remains 100; Ragnar Leonhart 67.

No replacement characters or unpaired surrogate code points were found. Several newer emoji were replaced in story-start titles with more widely supported alternatives. Exact keys, name fields and their references were updated together, including first-day triggers and creation gates. This improves compatibility but is not a claim to have tested every font or device.

## Validation and remaining tests

The generic validator now checks trait arrays, references, category memberships, game-mode key/name agreement and current trait/category size caps. `test_creation.cjs` checks contrasting starting builds, real benefits/trade-offs, finite kit grants, badge effect ownership and cue configuration. Existing item and Adventurers fixtures still apply. The release audit verifies source NPCs, maps, media, preceding items/abilities and unrelated event logic. These are local/CI checks, not live Studio validation, image generation or semantic playtests.

Before release, use a fresh licensure run to inspect the inventory update output; try both a noncasting and gifted caster build; inspect the optional menu groups and deliberate portrait choices; verify real music transitions; and check that ordinary item acquisition does not silently redefine a catalogue object. Artwork generation requires a separate actual engine test. Existing saves may retain generated duplicate items, older portraits or prior trait state.

Technical references: [Traits](https://wiki.unofficial.voyage/mechanics/traits), [Trait Categories](https://wiki.unofficial.voyage/mechanics/traitCategories), [Music](https://wiki.unofficial.voyage/other/gameplayMusicSettings), [Items](https://wiki.unofficial.voyage/world/itemTypes), [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings), [Quests](https://wiki.unofficial.voyage/world/quests). Source reference worlds remain unchanged.

## Studio import hotfix — 1 November 2026

The user's actual Studio rejection identified twenty-four trait requirements without numeric `amount`, plus two Special-tier prices outside the permitted 300–3000 mark range. The earlier local validator checked references but not these required values. Every new talent requirement now has `amount: 1`; the Rain-Counting Brooch and Polite Kettle Bell each cost 300 marks. The tier policy and item effects remain unchanged.

The [ability reference](https://wiki.unofficial.voyage/mechanics/abilities) lists `amount` in the requirement shape, even though it is ignored for trait gates. The [item reference](https://wiki.unofficial.voyage/world/itemTypes) requires an estimated price to be a nonnegative whole number inside its tier range. These constraints now apply to all configured ability/trait requirements and item prices in portable validation. `tools/test_validation.py` reconstructs the exact twenty-six rejected entries and exercises missing/invalid numeric values, bounds and reference types. Builders are fixed as well as the canonical export. A fresh Studio import is still required to verify acceptance; local success is not live validation.
