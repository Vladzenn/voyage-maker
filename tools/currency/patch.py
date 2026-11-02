"""Apply the narrow silver-mark currency clarification to an explicit Studio export."""
import argparse, copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "world-draft/WorldAlpha - World.json"
DELIVERY = ROOT / "output/currency-phantom-2026-11-02/The Schools of Magic, Arise! - Currency Consistency.json"
def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
def units(value):
    return len(compact(value).encode("utf-16-le")) // 2
def sha(value):
    return hashlib.sha256(compact(value).encode("utf-8")).hexdigest()
def paths(a, b, prefix=()):
    if a == b: return []
    if isinstance(a, dict) and isinstance(b, dict):
        result = []
        for k in dict.fromkeys([*a, *b]):
            if k not in a or k not in b: result.append(list((*prefix, k)))
            else: result.extend(paths(a[k], b[k], (*prefix, k)))
        return result
    return [list(prefix)]
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
def order_paths(a, b, prefix=()):
    result = []
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() == b.keys() and list(a) != list(b): result.append(list(prefix))
        for key in a.keys() & b.keys(): result.extend(order_paths(a[key], b[key], (*prefix, key)))
    elif isinstance(a, list) and isinstance(b, list):
        for i, (left, right) in enumerate(zip(a, b)): result.extend(order_paths(left, right, (*prefix, i)))
    return result
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    raw = args.source.read_bytes()
    supplied = json.loads(raw.decode("utf-8-sig"))
    previous = json.loads(CANONICAL.read_text(encoding="utf-8-sig"))
    world = copy.deepcopy(supplied)
    assert world["itemSettings"]["currencyName"] == "Mark"
    assert world["itemTypes"]["Mark"]["category"] == "Currency"
    assert [(k, v["category"]) for k, v in world["itemTypes"].items() if v.get("category") == "Currency"] == [("Mark", "Currency")]
    ai = world["aiInstructions"]
    ai["generateStory"]["Work, Trade and Property"] = "All money uses marks, also called silver marks, everywhere. Mark is the sole currency; gold, silver, copper and platinum are materials or ranks, not denominations. Honor actual terms and settled payments. A quote is not payment, a repair target is not loot, and a viewing key is not ownership. Property retains its real address, owner, agreement and key/deed after acquisition. No rent deductions while away, invented eviction, passive income, unbought tools or automatic household recruitment. New private rooms belong within existing residential locations. Successful services and paid bills stay settled."
    ai["generateDialogue"]["Currency and Settled Prices"] = "Prices, pay, rewards and debts use marks everywhere. 'Silver marks' means the same unit, not another currency. Gold/silver/copper/platinum can name materials or guild ranks; never invent monetary denominations or exchange rates. If you previously called an ordinary agreed price 'silver' or 'gold', clarify that same amount in marks before transfer. Accept actual Mark payment; do not add a conversion fee, reopen settled bills or claim a spoken promise already paid. Appraising or bartering a metal object is a separate agreement."
    ai["generateActionInfo"]["Currency"] = "Money uses Mark only; marks and silver marks are the same unit. Never invent denominations or exchange rates. Clarify genuinely ambiguous money-versus-metal offers before transfer."
    ai["ItemGenerationAndUsage"]["Currency, Debt and Contract Integrity"] = "Mark is the sole currency item in every realm and nation. 'Mark', 'marks', 'silver mark' and 'silver marks' mean the SAME unit; use quantities of the existing Mark item, never new alias stacks. Gold, silver, copper and platinum may describe metals, colors, equipment or guild ranks, not money denominations. Never invent exchange rates or foreign money. Bullion, jewelry and old coins are goods/collectibles: appraise and actually sell or barter them by agreement, not automatic currency conversion. A coin's metal content or a metal-conjuring spell does not create spendable Marks.\n\nQuote prices, wages, rewards, debts and change in marks. Correct a stray 'silver'/'gold' money quote before transfer; when an ordinary price's amount is already agreed, restate that number in marks without an exchange fee or refusing Mark payment. Ask only if the amount or the distinction between money and a metal object is genuinely unclear. Do not alter completed payment.\n\nActual Mark holdings are one purse; a wallet display is not extra money. Barter records both real transfers without fictitious cash. Check funds, quantity and ownership; no negative purse, invented credit, interest or upkeep. Preserve actual advances, deposits, remaining debt and their direction.\n\nTyped quest/trigger payouts own their payment once. Do not add another narration award, objective fee, recap payment or deducted guild cut. A promised fee is not cash; an advance is not the full fee twice. Real damage liability needs evidence, ownership and a credible demand; no offscreen invented bills or erased negotiated settlements."
    ai["summarization"]["State and Property Ledger"] += "\n\n" + "All monetary amounts remain in marks; silver marks is the same unit, not a second stack. Preserve corrected quotes and settled payments. Gold/silver materials, collectibles and guild ranks remain distinct from cash; estimated values and promised rewards are not money received."
    old_lore = world["worldLore"]["Glowhaven Marks and Everyday Prices"]["text"]
    price_paragraph = old_lore.split("\n\n", 1)[1]
    world["worldLore"]["Glowhaven Marks and Everyday Prices"]["text"] = (
        "Silver marks are the common money used throughout Glowhaven and the world's other nations. "
        "A mark, or silver mark, is the same single unit; prices, wages, rewards and debts are counted in marks. "
        "Gold, silver, copper and platinum are also materials and, in the Adventurer's Guild, names of ranks; "
        "they are not separate monetary denominations. Jewelry, bullion and old collectible coins can be sold "
        "for an agreed price in marks. Barter or a favor can replace money when both sides agree. "
        "An appraisal, an unpaid invoice and a promised reward are not payment received.\n\n" + price_paragraph
    )
    world["itemTypes"]["Mark"]["description"] = (
        "A stamped silver coin accepted in Glowhaven and abroad. One coin is one mark, also called a silver mark. "
        "Meals, wages, prices and debts are counted in this same unit."
    )
    allowed = {
        ("aiInstructions", "generateStory", "Work, Trade and Property"),
        ("aiInstructions", "generateDialogue", "Currency and Settled Prices"),
        ("aiInstructions", "generateActionInfo", "Currency"),
        ("aiInstructions", "ItemGenerationAndUsage", "Currency, Debt and Contract Integrity"),
        ("aiInstructions", "summarization", "State and Property Ledger"),
        ("worldLore", "Glowhaven Marks and Everyday Prices", "text"),
        ("itemTypes", "Mark", "description"),
    }
    changed = paths(supplied, world)
    assert {tuple(p) for p in changed} == allowed, changed
    for task in ("generateStory", "generateDialogue", "generateActionInfo", "ItemGenerationAndUsage", "summarization"):
        assert units(ai[task]) <= (30000 if task == "generateStory" else 20000), (task, units(ai[task]))
        for title, value in ai[task].items():
            assert units(value) <= 5000, (task, title, units(value))
    assert world["locations"] == supplied["locations"]
    assert world["itemSettings"] == supplied["itemSettings"]
    assert world["triggerDefinitions"] == supplied["triggerDefinitions"]
    assert world["parties"] == supplied["parties"]
    assert world["storyStarts"] == supplied["storyStarts"]
    for name in world["itemTypes"]:
        if name != "Mark": assert world["itemTypes"][name] == supplied["itemTypes"][name]
    for key in supplied:
        if key not in ("aiInstructions", "itemTypes", "worldLore"): assert world[key] == supplied[key]
    save(CANONICAL, world)
    save(DELIVERY, world)
    save(ROOT / "tools/currency/approved-description-delta.json", {
        "worldLore": {"entry": "Glowhaven Marks and Everyday Prices", "field": "text",
                      "before": supplied["worldLore"]["Glowhaven Marks and Everyday Prices"]["text"],
                      "after": world["worldLore"]["Glowhaven Marks and Everyday Prices"]["text"]},
        "itemTypes": {"entry": "Mark", "field": "description",
                      "before": supplied["itemTypes"]["Mark"]["description"],
                      "after": world["itemTypes"]["Mark"]["description"]},
    })
    report = {
        "sourceAttachment": "5fea7ef8-f456-4593-aeca-1f19c890d924",
        "sourceSHA256": hashlib.sha256(raw).hexdigest(),
        "canonicalBeforeSemanticSHA256": sha(previous),
        "suppliedChangesFromPrevious": paths(previous, supplied),
        "suppliedOrderChangesFromPrevious": order_paths(previous, supplied),
        "patchChangedPaths": changed,
        "newPromptUnits": {task: units(ai[task]) for task in ("generateStory", "generateDialogue", "generateActionInfo", "ItemGenerationAndUsage", "summarization")},
        "allNonTargetFieldsPreservedFromSource": True,
        "pricesStartingFundsRewardsAndMechanicsUnchanged": True,
        "spiderContentPreservedFromSource": True,
        "nativeCurrency": "Mark",
        "newCurrencyItems": [],
        "livePlaytest": False,
        "scope": "AI instructions and natural currency descriptions; no new trigger, conversion, balance change or saved-game migration."
    }
    save(ROOT / "tools/currency/patch-report.json", report)
    print(json.dumps({"delivery": str(DELIVERY), "report": report}, ensure_ascii=False))
if __name__ == "__main__":
    main()

