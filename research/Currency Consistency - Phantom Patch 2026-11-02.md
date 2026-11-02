# Currency consistency — phantom patch

**Use the Revised download:** `output/currency-phantom-2026-11-02/The Schools of Magic, Arise! - Currency Consistency - Revised.json`. The first download below is superseded. Review identified three wording problems: compressed original safeguards, automatic reinterpretation of another coin name at the same numeric amount, and a blanket statement against conjured spendable money. The revision restores the original trade/property and debt/contract paragraphs verbatim, appends only short currency clarifications, and requires an established or newly agreed Mark price without an assumed conversion. It removes the conjuration sentence. Exactly three AI fields differ from the initial patch; all other source-preservation guarantees remain.

Source: supplied Studio full export `5fea7ef8-f456-4593-aeca-1f19c890d924`, SHA-256 `8b8472de77ccdd886e5787eda93fa64e7a17bc6ff6e7e9f0408d4b900e3bddc1`. Applied to the canonical world and synchronized section files. Full delivery: `output/currency-phantom-2026-11-02/The Schools of Magic, Arise! - Currency Consistency.json`.

## Finding and scope

The author requested preventive hardening after the “Identify the bug” review. The shared screenshot does not identify the world and is not evidence of a reproduced Glowhaven failure. Native `itemSettings.currencyName` was already `Mark`, with exactly one Currency-category item. No authored metal-denomination exchange table was found. The ambiguity was in narrative guidance: gold/silver wording could drift into a second currency.

Silver marks now refer to the same one-unit Mark everywhere. Metals, jewelry, bullion, collectible coins, equipment names, guild ranks and silver-thread portal keys retain their identities and are not spendable denominations. Barter and genuine sales remain available. Correct an accidental money denomination before payment without inventing rates, surcharges or refusing the existing Mark item. Genuinely unclear amounts or metal-object offers require clarification.

Five existing AI tasks received focused rules: story, action interpretation, dialogue, item handling and memory. The revised story trade entry retains the original paragraph verbatim and adds a short currency sentence within its existing 30,000-unit task cap. Item-handling rules retain the original contract safeguards, one holding, actual terms, payment direction and one payout owner. Public Mark description and the existing currency lore entry use natural prose. No new native setting, currency alias item, trigger, balance adjustment, reward or quest controller was introduced.

The latest source changes Pebbletown x/y and the ordering of an existing diplomacy lore entry; both coordinate values and the supplied lore order are preserved. All non-target source fields, including images, coordinates, music, voices, quest/triggers, starting funds, price anchors, item values and the entire Spider content, remain exact. See `tools/currency/patch-report.json` for the seven changed paths. Reproduce from an explicit current source using `tools/currency/patch.py --source <export>`; do not run against an old export to rebuild later user changes.

## References

- [Item Settings](https://wiki.unofficial.voyage/mechanics/itemSettings): native currency name and starting items.
- [Item types](https://wiki.unofficial.voyage/world/itemTypes): categories, item identity and runtime generated items.
- Local read-only `sources/Luxcellia.json`, `ItemGenerationAndUsage / Currency Discipline`: dedicated denomination rule, aliases, valuables and dialogue consistency. Its four-denomination coin set was not imported.

This is AI-guidance hardening around an already configured native currency, not a deterministic ban on every possible generated coin. No live saved-game migration or playtest is claimed.

## Validation and manual checks

Local structural/size/reference validation and existing item-mechanics fixtures pass. The patch report verifies preservation against the supplied export. The existing fixtures test actual mechanics; they do not prove semantic compliance by the live narrator.

The fieldwork preservation fixture now permits only the two exact approved description texts, then restores their old text in a clone before checking the unchanged historical section hash. It does not bless a new whole-section baseline. Negative probes confirm that an unrelated Evertree lore edit and an unauthorized Mark combat bonus still fail.

The Crucible preservation fixture uses the same exact Mark-description allowance and a separate before/after record for the supplied Pebbletown coordinates. Its combat, bracket and reward scripts are unchanged; all other fields still have to match their historical hashes.

Test in Voyage:

1. Buy multiple goods for an agreed total in marks: actual goods and the correct net Mark reduction once; insufficient funds do not create unagreed debt.
2. An NPC accidentally says “ten silver”: confirm the ordinary agreed price as ten marks, accept Mark payment, no invented exchange or repeated charge.
3. A gold bar, silver jewelry or collectible coin is appraised, then sold or bartered by real agreement. Appraisal alone grants no money; no fixed metal-to-mark exchange is fabricated.
4. Silver/Gold guild badges and the Silver Web Portal Key remain documents/keys, not currency or money sources.
5. A wallet total and Mark inventory describe one purse. Summaries preserve the net amount and do not revive spent cash or promised rewards.
6. Finish a paid quest, report again and revisit the counter: its fixed reward remains paid once through its existing owner.
7. Handle an advance, deposit, refund and change without reversing who owes whom or counting returned change as new income.
8. Elvish/French dialogue still prices goods in marks and does not introduce écus, francs or gold denominations.
9. Test an existing save separately. Already fabricated duplicate coin items require case-specific review; this export does not silently convert or delete live inventory.

This phantom update does not advance public Minor Patch numbering. A short optional public line is provided separately.

