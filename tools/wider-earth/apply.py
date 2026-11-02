"""Apply the approved lore handoff to an explicit, current Studio export.

No mechanics, NPC rewrites or destinations are generated. The supplied export
remains the source of every non-lore field, including the author's XP edit.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
WORLD = ROOT/'world-draft/WorldAlpha - World.json'


def load(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def digest(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def units(s):
    return len(s.encode('utf-16-le'))//2


p = argparse.ArgumentParser()
p.add_argument('--source', type=pathlib.Path, required=True)
p.add_argument('--proposal', type=pathlib.Path, required=True)
p.add_argument('--output', type=pathlib.Path, required=True)
a = p.parse_args()
current = load(WORLD)
w = load(a.source)
baseline = copy.deepcopy(w)
text = a.proposal.read_text(encoding='utf-8-sig')
section = text.split('## Proposed in-world lorebook entries', 1)[1].split('## Implementation reconciliation', 1)[0]
draft = {m.group(1): m.group(2).strip() for m in re.finditer(
    r'^### ([^\n]+)\n(.*?)(?=^### |\Z)', section, re.M | re.S)}
assert len(draft) == 32, (len(draft), list(draft))
assert 'Earth and the Wider World' not in w['worldLore'], 'Already implemented; inspect the current export.'
assert all(isinstance(v, dict) and set(v) == {'text'} for v in w['worldLore'].values())

lore = w['worldLore']
new_headings = [
    'Earth and the Wider World', 'Continents, Nations and Peoples',
    'Maps, Distance and Foreign Knowledge', 'Oceans, Ships and Naval Power',
    'Glowhaven Among the Centers of Magic', 'Histories of Kingdoms and Cities',
    'Elves — Lifespan, Maturity and Appearance', 'Elves — Mana and the Recognition of Age',
    'Valcéranne — Land and Kingdom', 'Valcéranne — Long Memory and Public Change',
    'Valcéranne — Study, Art and Foreign Life', 'Dwarves — Homelands, Work and Migration',
    'Dwarvish Language and Speech', 'Dunbrae — The Maritime Commonwealth',
    'Dunbrae — Ports, Ships and the Interior', 'Dunbrae — Company and Public Life',
    'Yunhai — Land and Peoples', 'Yunhai — Cities, Provinces and Learning',
    'Yunhai — Foreign Scholars and Exchange', 'Celestials, Gods and Religious Traditions',
    'Faith, Testimony and Local Knowledge', 'Lives Across Borders',
]
for title in new_headings:
    assert title not in lore
    lore[title] = {'text': draft[title]}
lore['Earth and the Wider World']['text'] = lore['Earth and the Wider World']['text'].replace(
    'It revolves around the Sun.',
    'It revolves around the Sun, with a circumference of roughly forty thousand kilometers. '
    'Its continents have their own shapes and histories. Ordinary cosmic and physical principles operate alongside magic.')

# Reconcile overlapping subjects in their existing entries rather than appending
# several versions of the same founding, portal or language account.
lore['The Founding of Glowhaven']['text'] = (
    draft['Glowhaven — Founders and Independence']+
    '\n\nThe academies preserve different interpretations of the founders’ legacies. '
    'The shared monument is a civic meeting point rather than proof of every retelling of the planting.')

old_diplomacy = 'Diplomacy and the Wider Kingdom'
new_diplomacy = 'Diplomacy and Foreign Relations'
assert old_diplomacy in lore and new_diplomacy not in lore
lore[old_diplomacy]['text'] = (
    draft['Glowhaven — Foreign Relations']+
    '\n\nThe Great Sage can send elite personnel abroad when credibility, discretion and protection matter together. '
    'Visiting scholars, sailors, merchants and foreign residents bring other customs; foreign origin does not make every visitor a diplomat.')
# Rename in place: keep the existing entry position and all other entry order.
w['worldLore'] = {new_diplomacy if k == old_diplomacy else k: v for k, v in lore.items()}
lore = w['worldLore']

lore['Noble Houses and Civic Development']['text'] = lore['Noble Houses and Civic Development']['text'].replace(
    'service to the city and kingdom', 'service to Glowhaven')
lore['Noble Houses and Civic Development']['text'] += (
    '\n\nGlowhaven’s own institutions recognize its civic honors and grants. Private family, commercial or marital ties '
    'abroad can remain important without giving Ardelis jurisdiction over Glowhaven.')
lore['The Four Academies and Civic Service']['text'] = lore['The Four Academies and Civic Service']['text'].replace(
    'public institutions serving the city and wider kingdom',
    'public institutions serving independent Glowhaven and undertaking separately agreed international work')

lore['Elvish Language']['text'] = (
    'Elvish is represented as French in story text and dialogue. Render spoken Elvish in French; do not invent a replacement language. '
    'A speaker may also know Glowhaven’s common language, and listeners understand only languages their actual background supports.\n\n'+
    draft['Elvish Language and Foreign Communities'])
ancestry = lore['Playable Peoples — Expanded Ancestries']['text']
ancestry = ancestry.replace(
    'Elven adult appearance does not follow human aging.',
    'Elves live roughly a thousand years, physically mature at about the human rate and retain a youthful adult appearance. '
    'Changes in mana can indicate age to a knowledgeable observer; age does not itself confer skill. '
    'Cultural expectations of seniority differ from physical maturity and do not reclassify existing adults.')
lore['Playable Peoples — Expanded Ancestries']['text'] = ancestry

lore['Known Routes and Distant Lands']['text'] += (
    '\n\nThese familiar maps cover only a small part of Earth. Ardelis, Valcéranne, Dunbrae and Yunhai are among its wider countries. '
    'Their existence and foreign connections do not establish a new operating portal or an already available itinerary; '
    'most long journeys still depend on ships, roads and prepared travel.')
portal_intro = (
    'Permanent portals require immense magical power, costly construction and specialist knowledge. '
    'The Evertree sustains Glowhaven’s distant hub connections, an exceptional achievement. '
    'Glowhaven’s mages established the Drakenspire endpoint with its power; that receiving room is not evidence '
    'of independently equivalent Drakenspire portal-making technology. Most world travel and freight still use ordinary routes.\n\n')
lore['Evertree Portals and Distant Regions']['text'] = portal_intro+lore['Evertree Portals and Distant Regions']['text']
lore['The Evertree']['text'] += (
    '\n\nThe Evertree also sustains Glowhaven’s exceptionally demanding permanent portal connections. '
    'The hub’s practical importance extends beyond its benefits to local learning; it does not make ordinary personal mana inexhaustible.')
lore['Magic Learning and Affinity']['text'] += '\n\n'+draft['Magical Principles and Cultural Traditions']

# Retain the four focused Oni entries and their existing useful details. The
# proposal extends ordinary life and clarifies rumors without creating a route.
lore['Oni — Country, Houses and Public Life']['text'] = (
    draft['The Oni Homeland — Country and Public Life']+
    '\n\nHousehold loyalty, public office and independent organizations give people different obligations. '
    'Rural work and trade remain as important to daily life as martial service.')
lore['Oni — Samurai and Shinobi Traditions']['text'] += (
    '\n\nA samurai’s learned duties can include household administration and public service. '
    'A shinobi’s methods reflect an actual organization and training rather than inherited supernatural competence.')
lore['Oni — Arcane and Soul Magitech']['text'] += (
    '\n\nThese workshops support local livelihoods and foreign exchange while retaining their own working traditions. '
    'A foreign visitor can admire a particular mechanism without finding modern machinery in every household.')
lore['Oni — Yokai and the Unquiet Countryside']['text'] = (
    'The oni countryside has unfamiliar yokai, local spirits and territorial supernatural creatures. Some are dangerous predators, '
    'some intelligent neighbors and others bound to a place or custom. A horn, frightening appearance or spiritual nature alone proves no crime. '
    'Local accounts mix useful observation, custom and exaggeration. Travelers tell of a mysterious torii exuding Soul magic, '
    'but those accounts establish neither a reliable passage through it nor agreement about its significance.')

for title in ['Ardelis — Crown, Country and Provinces', 'Ardelis — Celestial Worship',
              'Ardelis — Glowhaven and the Former Connection']:
    lore[title] = {'text': draft[title]}

# A narrator convention, not a claim about a new Gaelic translation rule or voice asset.
lore['Dwarvish — Dialogue Convention'] = {'text': (
    'NARRATOR LANGUAGE CONVENTION. Portray Dwarvish-influenced common speech with readable Scottish-accented English '
    'and selected Scots words or constructions such as aye, wee, ken, dinnae and cannae. Vary the strength by speaker, '
    'upbringing and company; avoid making every line a phonetic puzzle or every dwarf sound identical. '
    'Dwarves raised abroad may share their home city’s speech. This is a writing convention, not a new voice tag '
    'or an instruction to translate Dwarvish into Scottish Gaelic. Keep public cultural descriptions natural.')}

private_title = 'Author Background — Primordial Origins'
lore[private_title] = {'text': (
    'AUTHOR/NARRATOR ONLY — NEVER DISCLOSE DURING PLAY. This background is unknown to every being in the world, '
    'including mortals, celestials, gods, oracles and ancient inhabitants. It is not a discoverable secret. '
    'No NPC, book, research, history, inscription, cult, divine revelation, memory, Divination or other in-game source '
    'can know or reveal it. The narrator must not disclose it directly, hint it as a solvable mystery or turn it into a quest.\n\n'
    'After the Big Bang, nigh-infinite primordial eldritch beings came into existence. Incomprehensible to mortal minds, '
    'they made galaxies, stars and initially empty planets, including matter, elements and the physical laws governing their works. '
    'There are trillions of planets and stars; Earth is one of the relatively few inhabited worlds.\n\n'
    'Primordial speech is part of their reality-shaping magic. A single breath can carry thousands of years of information. '
    'It is not a surviving ancient language that scholars can decode. A group made Earth as experiment and diversion. '
    'One sacrificed himself out of curiosity to produce life, not established altruism, martyrdom, cosmic duty or a struggle against evil. '
    'His act created Earth’s abundance of creatures and suffused it with lingering primordial power. The accessible fraction is called mana.\n\n'
    'This origin changes none of the established distinctions between usable mana, the soul’s sustaining reserve, ordinary animals, '
    'mana beasts and intentional casting. In-world creation accounts remain beliefs and claims; even beings claiming to have created '
    'the world do not gain knowledge of these beginnings. Their own origins and convictions are not explained here. '
    'The Evertree’s founding and Asterveil’s ruins remain separate, unexplained mysteries. '
    'Use this account only for private consistency; never place its truth into narration, dialogue, records or discoveries.')}

# Keep existing entries in position; arrange only the new tail by the proposal's
# topic order, with the clearly labeled narrator conventions/background last.
existing_order = [new_diplomacy if k == old_diplomacy else k for k in baseline['worldLore']]
new_order = [k for k in draft if k in lore and k not in existing_order]
new_order += ['Dwarvish — Dialogue Convention', private_title]
assert set(existing_order+new_order) == set(lore)
w['worldLore'] = {k:lore[k] for k in existing_order+new_order}
lore = w['worldLore']

# Lore-only scope relative to the supplied Studio file, not an older snapshot.
assert all(w[k] == baseline[k] for k in baseline if k != 'worldLore')
assert all(units(v['text']) <= 5000 for v in lore.values())
assert not any(re.search(r'city and wider kingdom|service to the city and kingdom|participate in a wider kingdom', v['text'], re.I)
               for v in lore.values())
assert not any('primordial' in v['text'].lower() for k, v in lore.items() if k != private_title)
for k in ['The Silken Brood', 'The Silken Descent', 'Silken Descent Routes and Map Scale',
          'Field Tests and the Anomalous Passage', 'Dungeon Enemy Groups']:
    assert lore[k] == baseline['worldLore'][k], k

changed = [k for k in lore if k in baseline['worldLore'] and lore[k] != baseline['worldLore'][k]]
added = [k for k in lore if k not in baseline['worldLore']]
removed = [k for k in baseline['worldLore'] if k not in lore]
report = dict(
    date='2026-11-02', baselineCommit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip(),
    sourceSHA256=hashlib.sha256(a.source.read_bytes()).hexdigest(), proposalSHA256=hashlib.sha256(a.proposal.read_bytes()).hexdigest(),
    sourceAttachment=a.source.parent.name, addedLoreEntries=added, revisedLoreEntries=changed,
    renamedLoreEntries={old_diplomacy:new_diplomacy}, removedLoreKeys=removed,
    incomingEdits=[dict(path='progressionSettings.extraRequiredXPPerCharacterLevel',
                        before=current['progressionSettings']['extraRequiredXPPerCharacterLevel'],
                        after=baseline['progressionSettings']['extraRequiredXPPerCharacterLevel'])],
    preservedSourceSections={k:digest(v) for k,v in baseline.items() if k!='worldLore'},
    preservedLoreEntries={k:digest(v) for k,v in baseline['worldLore'].items() if k not in changed and k not in removed},
    privateOriginEntry=private_title, newPlayableDestinations=False, newMechanics=False,
    publicPatchLine='Lore expanded.', liveStudioValidation=False,
)

# Update only active fingerprints for the author-supplied XP change and approved
# lore section, retaining every other historical/protected fingerprint.
refresh = {}
for path, prefix, keys in [
    (ROOT/'tools/crucible/revision-preservation.json', ['unchangedSections'], ['progressionSettings']),
    (ROOT/'tools/fieldwork/manifest.json', ['preserved','untouchedSections'], ['progressionSettings','worldLore']),
]:
    f=load(path);target=f
    for key in prefix:target=target[key]
    for key in keys:
        assert target[key] == digest(current[key]), (path,key)
        target[key]=digest(w[key])
        refresh.setdefault(path.relative_to(ROOT).as_posix(), {})[key]=dict(before=digest(current[key]),after=digest(w[key]))
    f['approvedWiderEarthLoreMerge']=dict(date='2026-11-02', proof='tools/wider-earth/merge-report.json', fields=keys)
    write(path,f)
report['approvedFingerprintRefresh']=refresh
write(WORLD,w)
write(a.output,w)
write(ROOT/'world-draft/The Schools of Magic, Arise! Full World Update 5 - Champions of the Crucible - Revised.json',w)
write(ROOT/'output/fieldwork-2026-11-02/The Schools of Magic, Arise! - Beginner Contracts and Fieldwork.json',w)
report['candidateSHA256']=hashlib.sha256(WORLD.read_bytes()).hexdigest()
write(HERE/'merge-report.json',report)
print(json.dumps(dict(added=len(added), revised=len(changed), renamed=1,
                     totalLore=len(lore), maxEntryUnits=max(units(v['text']) for v in lore.values()),
                     preservedXPIncrement=w['progressionSettings']['extraRequiredXPPerCharacterLevel'], output=str(a.output))))
