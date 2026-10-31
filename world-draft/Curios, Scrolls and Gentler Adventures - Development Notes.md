# Curios, Scrolls and Gentler Adventures — development notes

31 October 2026. The latest supplied Crime and Consequence export is the authoritative merge base. Its 213 NPC records, portraits, custom voices, music, map geometry, initial discovery settings and other unmodified data are preserved. The earlier local canonical file was older. A losslessly compressed copy of the incoming bytes is retained beside the build scripts.

Source SHA-256: `a7bd8d7451a3fa4dff8a9c4d54a01a1594ddf234cc141486a512689eae4aaebb`

Release SHA-256: `4c36c415eddab569bbd703d8070e81ada31e9c1085ba7e96e1c8071e72bd6c82`

## Shipped content

300 new items / 360 total: 84 weapons and shields; 54 clothing/armor pieces; 54 accessories; 42 tools, catalysts and materials; 24 consumables; 12 curios; 30 teaching scrolls. New tiers: {"mundane": 55, "artisan": 117, "special": 114, "legendary": 14}. The 30 new abilities bring the library to 510. Their 30 earned Formula traits are absent from creation categories and level-up pools. Twelve medicines have exact typed self-use effects; all thirty scrolls have player-scoped study effects. There are 351 root triggers, including 42 new item rules. No new quests or adventurer arcs were implemented in this item patch.

## Scroll ownership and research

Study conditions first require the actual scroll and absence of its learned formula. Successful research grants the formula trait, adds the exact ability, and removes one actual scroll, in that order. All personal changes target satisfyingPlayers. Rules recur so another genuine reader can learn from their own copy; the per-player trait prevents repeated consumption for the same formula. A deliberately completed study can be recognized in the latest or immediately preceding scene. No speculative onUseEffects or ability-point charge is invented.

Ordinary scroll abilities have no hard school-rank threshold. A real research project can support a difficult discovery at Fire Magic 5, but not an automatic successful master cast. Space retains Gravity Magic 25; there is no Time scroll. Bonus/cooldown and formula prerequisites are native. Spell scope, Mana expenditure, study difficulty and recognition of successful learning remain AI-interpreted. An independently invented related spell remains possible through normal Spellcraft; the scroll is not a monopoly on an entire magical function.

## Consumables and equipment

Native equipment bonuses apply while equipped. Damage +1 means +10 percent outgoing damage; armor +10 means 1 percent reduction. Resource equipment bonuses affect capacity, not potion healing. Materials and readable curios have no equipment bonuses. Dangerous items use visible negative bonuses or a stated Health cost, rather than hidden forced events.

The twelve new self-use restoratives remove one dose and apply exact resource effects, including harmful costs. Other utility uses and treatment of NPCs use normal item/action handling with the stated effect once. Test against duplicate AI inventory/resource updates. No automatic overdose engine was added. Item estimated values use the existing Mark economy and tier ranges.

## Availability

Existing item-generation guidance now favors catalogue identities before near-duplicates. Nine suitable locations carry hidden stock context. Browsing, purchasing and ownership remain separate. Items can enter play through appropriate shops, finds, salvage, commissions and gifts; this is guided generation, not a deterministic global drop table. Fourteen authored Legendary items can appear as exceptional discoveries or credible specialist offerings, while generation of new Legendary definitions remains disabled. No credential, wanted poster, portal key or victory proof was added to ordinary stock.

## Difficulty changes

Generation bands were lowered at 58 locations. Five regional bands were softened: Drakenspire 5-40; Cloudbloom 8-20; Rimeglass 15-30; Mirrorwater 25-40; Amethyst 35-50. Local overrides retain a gradual curve and intentionally dangerous remote sites. Asterveil lore and Crown level wording follow the changed bands.

Six introductory Bronze contracts request one weak/trivial opponent, levels 1-3 initially and capped at 6 later, with individual damageModifier -50 and successBonus -25. Four beginner creature types supply native -25 success defaults. Routine generated foes below level 10 receive reduced-damage guidance, with a milder reduction at levels 10-19. Existing actors never rescale every turn.

The existing guild board now screens its sixteen authored postings by the least experienced human participant. A powerful NPC companion does not increase the threshold. A specifically named harder request can reveal its offer with a warning; the board never accepts it for the player. Existing offer-flag writers, rank checks, recurring-job cooldowns and payouts remain in place. General generated jobs and incidental threats follow informed-risk guidance. These are not invisible level walls or invented per-hit damage caps.

The entire Spider Realm, its regions, locations, NPCs, anomaly, progression and triggers are exactly preserved. All authored NPC records and player stats remain unchanged. No broader combat-engine formula or global difficulty constant was changed. The native bands and type defaults are actual data; generated tier/damage selection still needs live verification.

## Validation actually performed

- 11,937 structural, reference, size-limit and preservation checks passed.
- 1,209 local condition/effect and board-script fixtures passed; 164 trigger scripts compiled.
- Fixtures cover successful/failed study, duplicate formulas, two readers, absent items, Space foundations, one-dose effects, resource maxima, mixed-level parties, explicit harder requests and all eleven existing dynamic offer flags.
- All relevant AI tasks and leaves remain under their checked caps. The compact item section is 152,298 UTF-16 characters, below 250,000.
- No live Studio import or Voyage playtest was performed. Mocked semantic results do not prove the live model recognizes the same events.

## Manual checks

1. Import the full release and run a fresh level-one Bronze character through the survey and boar work. Inspect actual enemy level, tier, health, successBonus and damageModifier; compare landed damage and available retreat. Try a nonmage and a minimally equipped caster.
2. Browse with level-one and mixed-level parties. Confirm routine offers remain suitable, a deliberately requested harder posting gives a warning, and rank alone does not promise safety. Confirm chosen dangerous sites still feel dangerous.
3. Read only a scroll label, fail study, then complete genuine research. Check one consumed copy, the correct Formula trait and actual usable ability. Test an advanced formula at skill 5 and its difficult casting. Try a duplicate and two real readers.
4. Consume a restorative at low and nearly full resources. Confirm one inventory removal and one exact resource change; verify a dangerous dose also charges its Health cost. Check an NPC patient separately.
5. Browse several shops, acquire a cursed accessory, equip and unequip it, and verify its actual bonuses. Check special finds remain scarce and no forged plot credential becomes real.
6. Verify the unchanged surprise Spider Realm flow in a separate run. A rule for ordinary jobs must not intercept that event.

Do not assume importing a World configuration rewrites an already-running adventure or the stats of already-generated enemies. Use a fresh run for the balance comparison and verify any save-update feature separately.

## Technical references

- [Items](https://wiki.unofficial.voyage/world/itemTypes): native item fields and bonus units.
- [Triggers](https://wiki.unofficial.voyage/mechanics/triggerDefinitions): item/ability grants, targeting and script execution.
- [Locations](https://wiki.unofficial.voyage/world/locations): per-location generation ranges.
- [NPCs](https://wiki.unofficial.voyage/world/npcs): tier and individual combat modifiers.

These community references document the authoring structures; the live checks above remain necessary.
