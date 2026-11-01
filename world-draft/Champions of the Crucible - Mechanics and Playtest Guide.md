# Champions of the Crucible — mechanics and playtest guide

Implementation edition 1 · 1 November 2026. This describes the shipped configuration and local fixtures, not a successful live Studio import or playtest. It supersedes stricter treatment requirements in the planning document.

## Deliverables and preservation

The full import is **The Schools of Magic, Arise! Full World Update 5 - Champions of the Crucible.json**. The canonical editable copy remains **WorldAlpha - World.json**. This update adds 32 competitors, four arena staff, six crime contacts and Threnvoss: 43 native cards and 43 one-pass portraits. The bundled expansion includes 160 abilities, eight finite shady jobs, one sanctuary investigation, seven guardian types plus a general competitor type, eight arena interiors and one compact three-location realm with twelve areas. There are thirty new root triggers. Three existing triggers receive narrow compatibility edits: the two older official-duel lore recognizers and the touring routine.

Every incoming NPC record, item and ability is fingerprinted in `tools/crucible/manifest.json` and checked unchanged. The protected Spider Realm, its anomaly and existing portal scripts are fingerprinted separately. Existing media, location coordinates, story starts, character creation, music, voices and ordinary difficulty are preserved. New images are local PNG deliverables: upload them in Studio; no hosted artwork URLs were invented.

## Why this is a world activity

There is no new native Game Mode. A character can study, work, adventure, enter a championship, lose and continue ordinary play. The bracket belongs to the party's persistent trigger storage, under `cc1`; conversation, teaching, medical scenes and ordinary combat still use Voyage's normal narration and resolution.

This release supports **one human player** in controlled championships and exhibitions. NPC companions may attend outside the ring. Human multiplayer registration is declined without charging or treating the party as one fighter. If another human joins during an entry, the controller pauses for review, preserving the original entrant. Restore the original solo roster before continuing; it does not silently transfer the entry or its prizes. Human renames need deliberate state migration rather than guessing that a new name is the same person. Team tournaments remain separate future work.

## Registration, divisions and draws

Ask the officials to enter after learning the rules, actual field and announced prize. Hina Wakabayashi handles announcements/registration; Shōgo Mizutani officiates; Nozomi Hayase and Gorō Azuma offer care. Existing coordinator Tomoe Enokida retains her own role and unchanged card.

Registration is a semantic **action** condition: an actual commitment qualifies; asking, spectating, imagining a fight or agreeing to a friendly spar does not. It has no entry fee. A mechanical script then records the edition, entrant, selected people, bracket, arenas, seed and purse once. Repeating registration cannot redraw an active field.

Divisions are Initiates (up to 12), Rising (13–25), Veteran (26–45) and Crown (46+). They are sporting labels, not new level caps. Candidates normally fall within two levels at levels 1–10, and within the greater of four levels or 30% above that. If fewer than three fit candidates remain, the script takes nearby lower-level competitors rather than introducing over-level padding. It announces actual levels. With seven suitable opponents it uses an eight-person field and three player bouts; with three it uses a four-person field and two bouts. Fewer than three means no edition is created.

Authored levels never scale. A level-100 or 150 player can outgrow this pool and receive an announced lower-level field; a separate high-level pool would be better than inflating familiar people. New entrants span levels 1–64. Ragnar Leonhart stays 67. Selected existing visitors join only when actually present, fit and free: Takeru Akabane, Ruri Saegusa, Asuka Tsurugi and Ragnar Leonhart. In-party, in-combat and known-incapacitated NPCs are excluded. The touring script holds a registered visiting competitor in place for the edition.

First Bloom Cup, Highsun Clash, Harvest Crown and Frostglass Championship rotate as cup traditions. They do not pretend the unreliable calendar has advanced to a particular season. The next edition opens at **closing engine tick + 100**. A narrated week or arbitrary date change does not bypass the tick gate. Sparring remains available during that break.

## A real bout and a real ending

After registration the current opponent waits in the lounge. Only an explicit readiness action moves the party and opponent to the recorded arena and opens the match. Readiness itself is not an attack. Arena Floor, Pillar Court, Verdant Ring, Frostglass Platform, Broken Stair Arena and Mirrorwater Garden are different native areas with their own cover, footing and routes. The bracket records a layout for each match; it does not continually reroll it.

Ordinary attacks and spells are resolved through normal Voyage combat. Finite learned summons are legal; outside companions cannot attack, heal or buff. Existing bans on live-bout mana potions and external stored-mana assistance remain. Ordinary control catalysts are legal. Surrender, ring-out, referee stoppage and proven interference can decide a match without needing to drive someone to zero Health.

The controller accepts a recognized actual result for the exact current bout. A player's boast alone is insufficient. In addition, a planning observer reads native Health after the bout has begun. A sole player's incapacity overrides a flattering semantic victory; an incapacitated opponent can settle a win; both down means a stopped bout awaiting review. Missing Health is not zero. An old bout, dead summon, spectator injury or earlier edition cannot qualify as the current result.

The result is recorded before aftermath: winner, loser, reason and tick. A repeated callback cannot finish it again. NPC-only branches use a small level-weighted stored draw and are settled abstractly, without fabricating offscreen damage or simulating other combat engines. They cannot resurrect an eliminated entrant or create another final. A player loss closes that title run; remaining branches yield one NPC champion.

After a recorded nonlethal stop, a native NPC-health effect can restore the opponent to its recorded starting Health if lower. This keeps repeat editions from exhausting the finite pool. It does not reverse their defeat. Whether native knockout/death processing, combat removal and placement cooperate with this timing requires a live test; this fixture does not prove revival support. Do not use it to excuse a genuine lethal attack or claim an NPC's death was harmless.

## Optional care, including an unharmed fighter

A settled bout creates one care entitlement. Medics naturally offer what fits: treatment for injuries, recovery for exertion, a check-up or simply rest. **An unharmed fighter has no fabricated wound.** Someone with full Health but low Mana is not automatically bleeding. Offers, refusals and another person's treatment do not count as the player's accepted care.

The user explicitly relaxed the original full-bar requirement. There is **no exact Health/Mana/Stamina percentage gate**, no compulsory medical scene and no obligation to spend a turn receiving unnecessary care. The player may decline, talk, rest or declare readiness. An actually accepted scene uses the normal resource-update workflow; this release does not invent a maximum-resource read or a typed player heal-to-max effect. Appropriate generous treatment is intended, but exact numeric restoration is not locally guaranteed. Treatment never changes the recorded match result or auto-starts the next bout.

## Departure, stoppage and rewards

Leaving the location between bouts withdraws the entry. Moving to its lounge or infirmary does not. A live departure has a short reconciliation window for a genuine emergency stoppage; if no result resolves it, the next observer after two tick increments closes it as withdrawal. Voluntary surrender/withdrawal can be recognized immediately. An emergency is not a free rematch after a verified loss.

For an inconclusive stop, ask the referee for review. Native one-sided incapacity still governs. If the evidence remains inconclusive and both can continue, one agreed no-contest replay is available, preserving the first stopped attempt and its arena/opponent. Repeated inconclusive stoppages close the entry instead of looping forever. Both still down means treatment/review, not an invented winner.

A championship win creates an owed prize, not an inventory duplicate. Explicitly collecting it grants **one Crucible Championship Trophy** and `80 + min(700, floor(entryLevel × 10))` marks through native effects. The pending award retains its original owner's name across later editions. Another human cannot claim it. Repeated handover callbacks cannot pay again. Exhibitions grant neither championship trophy nor purse and impose no title cooldown.

Prize dispatch is idempotent in the emitted scripts; it is not an external transaction database. A service interruption exactly between persistent mutation and effect application needs manual verification, not an automatic retry that might duplicate currency. Inspect actual inventory and `Crucible status` before using any repair. The existing honor-based quest repair command does not mint a championship trophy: there is no tournament quest to complete.

`Crucible status` is an OOC exact command showing the current recorded edition, phase, opponent/layout, outcome, cooldown and unpaid awards. Normal conversation with the officials remains in character. This command does not select a new field or force a win.

## The Sepulchral Conservatory

Discovery checks the Evertree Portal Room, one qualifying holder's Championship Trophy and existing Silver Web Portal Key. It does not demand spider-queen victory, consume those items or alter the anomaly. The same-tick transit guard defers revelation when an existing portal transition is already happening. A new arch appears without crossing for the player. A deliberate crossing updates the actual location/area and NPC companions; return goes directly to **Evertree Base - Portal Room**. First arrival supplies a Sepulchral Portal Key. Return needs no key, so a lost inventory item does not trap anyone.

This is a compact **35–50 midgame** sanctuary, not another nation. The Portal House is a safe staging point. The conservatory has two guarded tending wings that can be explored in either order. Rootwalk/Tending Gallery use small groups of Gravewood Golems or Rootbound Pallbearers. Memorial Orchard/Ossuary Greenhouse use a Censer-Willow and Ossuary Trellis. Mourning Garden has an optional Hollowseed Swarm problem and a quiet arbor. The Keeper Archive and nameplates distinguish empty frames from conscious spirits.

Real work on the rootwake and mourning circuits opens the inner lattice. Repair, qualified assistance or a clever practical bypass can work; merely visiting cannot. These two physical facts remain completed if their keepsake seals are lost. Early area-click entry is corrected back to the Ossuary Greenhouse with actual NPC companions. The heart is not a reward for possessing a token alone. Backtracking and retreat remain possible.

**Threnvoss**, level 50, begins hostile to interference. The caretaker confuses keeping charges present with keeping them safe. Its roots, visible chest knot, staff and limited bindings give counterplay; two finite Grafted Sentinels can support it. Actual defeat or an achieved dismantlement/release ends its coercive vigil. Flattery or a promise cannot. Both outcomes share one resolution flag and one typed Heartwood Remembrance grant. The ordinary optional investigation quest has native semantic completion and no duplicate trophy.

Enemy groups use npcTypes and scoped encounter guidance. This configuration does **not** fabricate a typed spawn effect. The narrator must register real generated actors before attacks; those instructions cannot guarantee an exact spawn count in every live scene. Cleared routes should remain cleared in narrative state rather than respawning on each visit. Testing direct map/area clicks, unusual spells, revisits and the actual scene NPC roster is necessary.

A genuine release also raises Threnvoss's relationship to neutral if still negative, ending its default hostility without forcing friendship. An already positive relationship is preserved. Combat resolution does not apply that truce automatically.

## Abilities, questionable work and Oni preparation

The catalogue gains 120 spells (six per public discipline), 24 martial/tactical techniques, twelve mixed techniques and four Magitech techniques. They have supported requirements, costs, cooldowns and bounded scope; none automatically grants the entire catalogue to a starting character. Existing 534 abilities remain unchanged. Time gets no public spell batch. No discipline-acquisition system or new creation category was introduced.

Mika Koshimizu, Renjirō Suda and Momo Shiratori offer four Glowhaven situations; Shiori Takase, Genta Shishido and Koharu Mikazuki offer four Drakenspire ones. These are people with livelihoods, relationships and flaws, not automatic mission dispensers. Specific interest in an actual offer can surface a native quest without accepting it. Agreed work can be done, exposed, refused or renegotiated. Their completion conditions own journal closure. Fixed illicit completion payouts are intentionally absent: compensation follows the actual agreement through ordinary inventory updates, so reporting a scheme does not automatically earn the criminal's quoted fee. This is less mechanically exact than championship prizes and needs normal playtesting.

Oni lore establishes Edo-inspired towns/countryside, Shogun, samurai, shinobi, independent households/factions, yokai and selected Arcane/Soul magitech. Existing ancestry modifiers remain unchanged. No Oni realm, torii quest, spirit realm or imported franchise character was added.

## Trigger ownership and budget

Twelve `cc1_` controllers handle initialization, registration, readiness, observation, semantic win/loss, withdrawal, care, prize collection, review, status and exhibition. Ten `cc1_grove_` events handle discovery/travel, first key, two circuits, heart access, shared resolution and quest offer. Eight crime offer events surface finite native quests. There is no separate completion watcher for every ordinary quest.

Pure mechanical filters reject irrelevant places/phases before story/action checks. The portable eligibility probe includes registration, a live bout, between-bout care, a tending wing and the heart, alongside the earlier academy/guild/settlement scenes. Its counts include a conservative allowance for existing arcs and accepted quests. It remains a static approximation: generated quests, runtime dispatch order and Voyage's semantic selection are not reproduced locally. Do not assume thirty new trigger definitions mean thirty AI checks every turn.

## Live verification priorities

1. Import the full world and check current Studio validation, character/AI limits and all new references.
2. Register at low and middle levels; inspect the announced field. Win, lose, surrender, ring out and leave. Confirm actual location, current opponent and journal/inventory independently of narration.
3. Test semantic surrender and referee stoppage while both have positive Health. Test a real knockout and a deliberately contradictory victory sentence. Confirm NPCs actually leave combat and can appear in another edition.
4. Enter a bout unharmed; skip care. Accept real treatment after another bout. Confirm neither creates injuries, duplicate supplies, a readiness lock or an automatic next attack.
5. Test nonlethal intent in ordinary play before using the separate native-Permadeath export. There is no documented per-bout override of the world's global death flag. Regulated nonlethal instructions cannot honestly guarantee engine safety without that live test.
6. Claim a prize, reload, try again and revisit after 99/100 ticks. Check actual marks, one trophy and old unclaimed ownership. Try changing the human-player roster mid-entry.
7. Open the new route after a real championship, cross, backtrack, try early heart clicks, finish the wings in both orders, lose a seal and return through the arch. Verify enemy groups exist before damage, and that return changes actual address immediately.
8. Resolve Threnvoss by combat and by genuine release in separate runs. Check the natural trophy description and one grant. Test the eight optional illicit offers and their alternative outcomes without unsolicited payment or ordinary-crime overreach.

## Sources and evidence

Reference configurations: read-only Luxcellia and Chikara exports under `sources/`, especially ordinary native quest completion, dungeon progression, sporting tone and bounded generated content. They are examples, not proof of current engine support.

- [Voyage trigger reference](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): conditions, effects, scopes, phases, persistent storage and semantic budgets.
- [Voyage NPC type reference](https://wiki.unofficial.voyage/world/npcTypes): reusable creature definitions; authored named people remain separate.
- The project planning document records the official release-note research and supported/observed/untested distinctions used to choose this implementation.

Local fixtures execute the actual emitted scripts with supplied semantic answers. They validate consistency under those answers, not the AI's ability to recognize prose. They do not replace a live playthrough.
