"""Apply the approved finite-contract expansion to the current canonical world once.

Never rerun an older world builder. Existing quests change only on the explicit
six-title allowlist; effects, checks and objectives are preserved byte-for-value.
"""
import copy
import hashlib
import json
import pathlib
import re

from content import CREATURES, JOBS, LEGACY_BRIEFS, update_encounter_guidance

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
WORLD = ROOT / 'world-draft/WorldAlpha - World.json'
OUTPUT = ROOT / 'output/fieldwork-2026-11-02/The Schools of Magic, Arise! - Beginner Contracts and Fieldwork.json'


def load(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def units(value):
    return len(value.encode('utf-16-le'))//2


w = load(WORLD)
before = copy.deepcopy(w)
quests = w['parties']['']['quests']
assert len(JOBS) == 19 and len(CREATURES) == 18 and len(LEGACY_BRIEFS) == 6
assert not any(j['title'] in quests for j in JOBS), 'Already applied; inspect the current world instead of rebuilding.'
assert not any(c[0] in w['npcTypes'] for c in CREATURES)

for name, bonus, vulnerable, resistant, description in CREATURES:
    w['npcTypes'][name] = dict(name=name, description=description,
                             vulnerabilities=vulnerable, resistances=resistant,
                             immunities=[], successBonus=bonus)

# A small service space, not another map location. Every old image and path is retained.
inn = w['locations']['Roseberry Inn']['areas']
cellar = 'Roseberry Inn - Cellar'
door = 'Roseberry Inn - Kitchen Passage'
assert cellar not in inn
inn[cellar] = dict(description='Broad wooden steps lead into a low, cool cellar smelling of flour and apple skins. Sack shelves, a work stool and spare boards flank a clear central aisle; a small ground-level vent lets in a strip of daylight.', paths=[door])
inn[door]['paths'].append(cellar)

profiles = {
    1: 'BEGINNER WORK: use the stated finite nuisance, normally level 1–3, weak/trivial, with only one active hostile initially. A second rat or moth is separated, not a free pack attack. Apply the individual beginner profile in New NPC guidance. No hidden alpha, lethal continuous damage, opening critical burst or mandatory second hunt.',
    7: 'PRACTICED BRONZE: one stated creature, or the explicit separated pair. Use its described local band, capped at two levels above the least experienced participating human unless a harder job was explicitly requested and warned about. Weak individuals, telegraphed attacks and useful cover; no surprise elite upgrade.',
    15: 'EXPERIENCED FIELDWORK: one stated creature in its described level band, normally 13–18 and average tier. Preserve readable threats and practical alternatives. The posted risk belongs to this accepted commission, not every nearby passerby or a novice’s unrelated job.',
}
for j in JOBS:
    assert j['client'] in w['npcs'] and j['location'] in w['locations']
    assert j['area'] in w['locations'][j['location']]['areas']
    assert j['creature'] in w['npcTypes']
    badge = 'Bronze' if j['rank'] == 1 else 'Silver'
    brief = (j['scene']+'\n\nSite: '+j['area']+'. '+profiles[j['band']]+
             '\n'+badge+' badge or higher; posted fee '+str(j['marks'])+' marks. Optional, finite work: agree terms before accepting. The native completion condition and effects alone settle this job, paying the fee, experience and one Guild Service Credit once. Do not duplicate those grants or add a return report beyond the stated objective. Killing is not required when a safe, effective alternative achieves the same work. No instant capture, automatic success, free spell or recruitment. Respect the actual outcome and resolved individuals.')
    quests[j['title']] = dict(
        name=j['title'], questSource=j['client'], questLocation=j['location'],
        detailType='detailed', status='hidden',
        questStatement=badge+' contract. '+j['statement'], mainObjective=j['goal'],
        questDesignBrief=brief, conclusive=True,
        completionCondition=dict(type='story', query=(
            'For the accepted contract "'+j['title']+'", the actual events have achieved this outcome: '+j['goal']+
            ' Count an effective nonlethal or negotiated solution when it achieves that outcome. The real work must be done; a plan, arrival, boast, unrelated creature or old result from another contract is insufficient. Once achieved, preserve the outcome after travel. No extra report or another job is required.')),
        onCompleteEffects=[
            dict(type='item-add', item='Mark', quantity=j['marks'], target='allPlayers'),
            dict(type='player-experience', operator='add', value=j['xp'], target='allPlayers'),
            dict(type='item-add', item='Guild Service Credit', quantity=1, target='allPlayers'),
            dict(type='story', instruction='Conclude '+j['title']+' with the actual method and consequences. The typed effects settle the agreed payment and service credit once. Show the client’s specific reaction if they are present; otherwise preserve the result without teleporting them here. Return entrusted property, keep resolved creatures resolved and leave any further work optional.'),
        ])

for title, brief in LEGACY_BRIEFS.items():
    quests[title]['questDesignBrief'] = brief
quests['Guild: Boars at the Watercourse']['questStatement'] = (
    'A young boar is blocking a working bank at Pinewater River. The crew needs safe access to its watercourse. '
    'Posted reward: 55 marks. A short, local Bronze job suitable for a newly licensed adventurer.')

board = w['triggerDefinitions']['gh_guild_board']
old_jobs = json.loads(re.search(r'const jobs=(\[.*?\]);', board['script'], re.S).group(1))
new_jobs = [dict(title=j['title'], rank=j['rank'], recommendedLevel=j['recommendedLevel'],
                band=j['band'], lane=j['lane']) for j in JOBS]
combat_legacy = {'Guild: Boars at the Watercourse', 'Guild: Teeth in the Spare Crate',
                 'Guild: Bitter Roots, Sharp Teeth'}
for j in old_jobs:
    j['lane'] = 'combat' if j['title'] in combat_legacy else 'other'
    level = j['recommendedLevel']
    j['band'] = 15 if level >= 15 else 7 if level >= 7 else 1
table = json.dumps(new_jobs+old_jobs, ensure_ascii=False, separators=(',', ':'))
board['script'] = (HERE/'board.js').read_text(encoding='utf-8').replace('JOBS', table)
assert units(json.dumps(board, ensure_ascii=False, separators=(',', ':'))) <= 10000

# Type descriptions do not set native level/tier/health fields. Give their creation owner
# one compact calibration instead of repeating the entire implementation in every brief.
power_key = 'Power Anchors and Professional Breadth'
w['aiInstructions']['generateNewNPC'][power_key] = (
    'POWER BY ROLE\nUse actual role, training and place, not the player’s level or highest nearby NPC. '
    'Untrained adults: 8–20; practiced workers/guards: 15–28; ordinary adventurers: 20–30; professors/headmasters: 28–32; '
    'exceptional specialists/court elites: 40–45; Archons: 50–55. Headmaster is a job, not a power promotion. '
    'Ilyra Stillglass at 100, Ragnar Leonhart at 67 and established legendary creatures are authored exceptions. '
    'No random level-70 professional, 87 shopkeeper or hidden demigod. Office, age, wealth, species and portrait flair do not confer mastery; '
    'a lazy graduate knows magic, a scholar may fight poorly, an elderly worker need not be elite. Tier and real bonuses matter; avoid stacked multipliers. '
    'Preserve authored levels, the Spider Realm and knowingly chosen dangerous places. Warn about major mismatches.\n'
    'GUILD FIELDWORK\nCreate the accepted job’s actual type and count. Beginner nuisances: explicit level 1–3, weak/trivial tier, '
    'damageModifier -50, damageReductionModifier 0, healthMultiplier 0.7; retain the type’s successBonus. '
    'Practiced Bronze jobs around level 7: stated local band, weak tier, damageModifier -20, damageReductionModifier 0, healthMultiplier 0.85. '
    'Routine new foes stay within the stated band and at most two levels above the least experienced human; powerful NPC companions do not raise it. '
    'Explicit warned harder jobs retain their posted band. Experienced level-15 work normally uses its stated 13–18 band, average tier and unstacked modifiers. '
    'Persist individuals; these are creation profiles, never extra narrated damage or per-turn rescaling. Do not apply them to authored actors or the Spider Realm.')
ai = w['aiInstructions']['generateNewNPC']
assert units(json.dumps(ai, ensure_ascii=False, separators=(',', ':'))) <= 20000
key = 'Combat, Power and Telegraphing'
w['aiInstructions']['generateEncounters'][key] = update_encounter_guidance(w['aiInstructions']['generateEncounters'][key])

# Exact allowlist: no licenses, starts, old completion/reward checks, NPCs, items,
# regions, dangerous dungeon records, travel restrictions or unrelated quests change.
allowed = {'npcTypes', 'parties', 'triggerDefinitions', 'aiInstructions', 'locations'}
assert all(w[k] == before[k] for k in before if k not in allowed)
assert w['parties'][''].keys() == before['parties'][''].keys()
assert {k:v for k,v in w['parties'][''].items() if k!='quests'} == {k:v for k,v in before['parties'][''].items() if k!='quests'}
for title, q in before['parties']['']['quests'].items():
    changed = {k for k in set(q)|set(quests[title]) if q.get(k)!=quests[title].get(k)}
    expected = {'questDesignBrief'} if title in LEGACY_BRIEFS else set()
    if title == 'Guild: Boars at the Watercourse': expected.add('questStatement')
    assert changed == expected, (title, changed)
for key in before['triggerDefinitions']:
    if key != 'gh_guild_board': assert w['triggerDefinitions'][key] == before['triggerDefinitions'][key], key
for key in before['locations']:
    if key != 'Roseberry Inn': assert w['locations'][key] == before['locations'][key], key
for key, value in before['npcTypes'].items(): assert w['npcTypes'][key] == value, key

manifest = dict(date='2026-11-02', baselineSHA256=hashlib.sha256(WORLD.read_bytes()).hexdigest(),
                types=[c[0] for c in CREATURES], jobs=JOBS, revisedBriefs=list(LEGACY_BRIEFS),
                output=str(OUTPUT.relative_to(ROOT)), addedArea=cellar,
                preserved=dict(originalQuests={k:digest({f:v for f,v in q.items() if f not in (
                    {'questDesignBrief', 'questStatement'} if k=='Guild: Boars at the Watercourse' else
                    {'questDesignBrief'} if k in LEGACY_BRIEFS else set())}) for k,q in before['parties']['']['quests'].items()},
                    otherTriggers={k:digest(v) for k,v in before['triggerDefinitions'].items() if k!='gh_guild_board'},
                    untouchedSections={k:digest(v) for k,v in before.items() if k not in allowed},
                    originalTypes={k:digest(v) for k,v in before['npcTypes'].items()}))

# Refresh only fingerprints for the explicit additions; keep every protected Spider,
# media and old quest/effect fingerprint in the new report and existing tests.
pres_path = ROOT/'tools/crucible/revision-preservation.json'
pres = load(pres_path)
refresh = {}
for key in ['npcTypes', 'parties']:
    assert pres['unchangedSections'][key] == digest(before[key])
    refresh[key] = dict(before=digest(before[key]), after=digest(w[key]))
    pres['unchangedSections'][key] = digest(w[key])
assert pres['unchangedLocations']['Roseberry Inn'] == digest(before['locations']['Roseberry Inn'])
refresh['Roseberry Inn'] = dict(before=digest(before['locations']['Roseberry Inn']), after=digest(w['locations']['Roseberry Inn']))
pres['unchangedLocations']['Roseberry Inn'] = digest(w['locations']['Roseberry Inn'])
pres['approvedFieldworkRevision'] = dict(date='2026-11-02', changes=refresh,
    scope='18 appended types, 19 native quests, six brief-only edits plus corrected boar notice, one connected inn cellar. Existing quest checks/effects and all Spider fingerprints unchanged.')

write(WORLD, w)
write(OUTPUT, w)
alias = ROOT/'world-draft/The Schools of Magic, Arise! Full World Update 5 - Champions of the Crucible - Revised.json'
write(alias, w)
write(HERE/'manifest.json', manifest)
write(pres_path, pres)
print(json.dumps(dict(addedTypes=18, addedQuests=19, revisedBriefs=6,
                     rootTriggers=len(w['triggerDefinitions']), newNPCUnits=sum(units(k)+units(v) for k,v in ai.items()),
                     boardUnits=units(json.dumps(board,ensure_ascii=False,separators=(',',':'))), output=str(OUTPUT))))
