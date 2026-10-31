# Alpha 15 — Guild, Court Cast and Inventory Cleanup

This export merges the new guild, the court cast and the ordinary Spider Realm encounter refactor into the latest export you supplied. It preserves the prison-region map image and all 28 prison-location coordinate edits from that export. All other existing hosted images, map positions and surviving NPC records are preserved.

## Court cast

| Character | Work | Affinity | Character hook |
|---|---|---|---|
| Sae Takasago | Principal registrar; petitions and passage permits | Enchantment, Arcane | Dry, exact and quietly invested in the cases she cannot simply approve. Turns a carved desk duck toward the wall during ridiculous meetings. |
| Tadashi Morishige | Public works and treasury controller | Earth | A practical dwarf who inspects actual drains and walls. His harshest scrutiny goes to the ambitious architecture he secretly loves. |
| Tomoe Hoshizaki | Senior magistrate | Sound | A measured judge who can revise a judgment, finds sentiment irritating because it reaches her, and considers Phoenix Wright exhausting but worth hearing. |
| Phoenix Wright | Independent defense attorney; Phoenix Wing Academy graduate | Arcane | Recognizable face, blue coat and red tie; earnest faith, nervous improvisation, theatrical objections and actual evidence. |
| Ayame Kazehara | Court elite; mobile interception | Wind | White uniform, ivory mask and one double-ended twinblade. A disciplined fighter with a private love of ballroom dancing. |
| Gōtarō Iwamine | Court elite; protective escort | Earth, Metal | A dragonkin with a sword and shield, warm literal humor and an imposing white-and-ivory silhouette. |
| Shion Kurobane | Court elite; capture and restraint | Gravity | A whip fighter with dry humor, exact control and unexpectedly awkward Elvish practice. |
| Seiran Yukitsugu | Court elite; counterspells and containment | Void, Illusion, Divination | A reserved half-elf grimoire caster who understands intricate magic better than urgent personal judgments. |

All eight received one portrait-generation pass with major-character staging. The four operatives wear full-face ivory masks and white uniforms. Their names are not automatically known to everyone who sees a mask. The entries use the existing character format; appearance remains in visualDescription, with equipment and the existing profile bullets in basicInfo. Existing court and magistrate areas are used rather than adding redundant locations.

## Adventurer’s Guild

- Added an international major faction, permitted to operate its Glowhaven branch by the court. Martial, magical and mixed adventurers are welcome. Academy staff can commission work without controlling the guild.
- Added Komugi Hanabishi, a bright, cheeky receptionist with peach hair, blue eyes, Enchantment training and an affectionate sketchbook of unsettling monsters. She is a receptionist, not every assessor or specialist.
- Added **Adventurer’s Guild - Glowhaven Branch**, temporarily at x=-44, y=44 in Glowhaven, with seven connected areas: Reception Counter, Request Board, Common Hall, Appraisal Bench, Briefing Room, Training Yard and Staff Office. Move its pin in Studio as intended; the temporary position does not make remote wilderness part of its lore.
- Added an authored **Adventurer: Guild Counter** start. It grants no automatic badge, exam success, equipment, money, party or portal key. Random stays last.
- Added personal exam records and typed Bronze-badge issuance after both a genuine judgment review and practical assessment. Martial methods are valid; no universal spell requirement.
- Added Bronze → Silver → Gold → Platinum badges. Higher badges qualify for lower-rank work. Working review thresholds are 5 service credits for Silver, 10 further credits for Gold and 20 further credits for Platinum. These thresholds are an authoring choice, not a user-declared law. Eligibility offers a review; a real accepted assessment and badge exchange are still required.
- Added five first contracts: Bazaar parcel (Bronze, 40 marks), Westwood trail notes (Bronze, 50), Broken Halo recovery (Silver, 140), Redvein safety survey (Gold, 360), Inverted Crown instruments (Platinum, 900). Work and verified settlement are distinct. Posted rewards are paid in full once; no player commission deduction or repeated commission dialogue.
- Court-issued portal permissions remain separate. Guild membership, rank and accepting a foreign job do not supply a key.

Five authored contracts are the initial board, not enough repeatable work to exhaust the entire promotion ladder. Additional authored or generated guild commissions must use the documented badge and completion pattern, including a service credit, instead of counting unrelated quests. Automatic adherence by generated quests still needs playtesting.

## Ordinary dungeon enemies

Removed the fifteen ordinary prewritten spider/arachne NPCs. Their existing npcTypes remain. Six area-entry hooks now request finite groups through normal NPC generation and reuse actual runtime identities, wounds and defeats. The queen **Vhalessra Veyrath**, and the unique retainers **Khessik Threadwarden** and **Orruk Cindershell**, remain authored. The queen remains level 45; navigation gates, backtracking, return portals and the one-time victory award are retained.

The documented trigger interface does **not** expose a general direct “spawn this npcType” effect. These hooks use supported story effects to request encounter generation. Local tests prove request gating and persistence of the request record, not that the live engine will instantiate exactly the requested pack. If generation fails, the hook does not keep retrying and multiplying enemies. Counts, native identities and scene timing require an in-game test.

## Natural inventory text and the bazaar Easter egg

**Matron’s Anchor Sigil** now reads:

> A palm-sized fragment of silver-black metal threaded with hardened silk. Its broken lattice still holds a faint warmth from the arachne matron’s shattered web-anchor—an unsettling keepsake of the Silken Descent.

The inventory entry no longer carries authoring instructions. The existing one-time victory grant still controls its legitimate award. Ryūka Marufuji’s bazaar confrontation checks the actual carried item and its place/once gate; the extra boss-resolution flag requirement was removed. Losing the trophy can prevent this Easter egg. The event neither replaces a lost trophy nor retrospectively marks the boss defeated. New guild badge and document descriptions were also written as player-facing objects.

## Reference decisions

Inspected LuxcelliaUpdated.json’s Adventurer’s Guild faction, central branch services, rank-card items, guild_ladder, guild_rank_register, guild_rank_plain, guild_rank_record and guild_rank_on_start. Adapted its inventory credential, recorded work, optional assessment and actual badge exchange patterns to the requested four-metal ladder. Did not import its F-to-S ranks, registration fee, unique cast or special guildmaster lore.

Current community documentation: [triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions), [NPC types](https://wiki.unofficial.voyage/world/npcTypes), [factions](https://wiki.unofficial.voyage/world/factions). These establish the supported item effects, selector behavior and faction/type distinction; the ordinary encounter request remains an AI-mediated technique. Phoenix Wright’s visual and behavioral basis was checked against [Capcom’s character introduction](https://news.capcomusa.com/official_capcom_blog/blog/2019/03/06/ace-attorney-files-meet-phoenix-wright-rookie-attorney).

## Artwork and validation

Generated nine individual NPC portraits (eight court characters and Komugi Hanabishi) plus one guild interior. No guild-area images were generated. Each PNG uses its full NPC or location name. All ten are local files awaiting manual Studio upload; no local paths were inserted into hosted-image fields. Some portraits have tighter headroom than the guide target, and Phoenix uses a raised argument finger rather than the full outstretched point. Those are recorded one-pass results, not silently rerolled images.

Passed 8,145 local structural, reference, size and preservation checks and 174 script checks/fixtures. All configured scripts compile. Semantic outcomes and personal recipients are supplied test inputs; movement, inventory and quest effects are simulated. No Studio import, live image upload, combat balance or AI-generated encounter playtest was performed. The full JSON is intended for a fresh imported game; old saves are not migrated.
