"""Apply the approved small Ardelis patch to the author's full Studio export."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
WORLD = ROOT / 'world-draft/WorldAlpha - World.json'


def dump(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def digest(v):
    return hashlib.sha256(dump(v).encode('utf-8')).hexdigest()


def write(p, value):
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def changes(before, after, path=()):
    rows = []
    if isinstance(before, dict) and isinstance(after, dict):
        for k in before.keys() | after.keys():
            loc = list(path + (k,))
            if k not in before:
                rows.append(dict(path=loc, kind='added', afterHash=digest(after[k])))
            elif k not in after:
                rows.append(dict(path=loc, kind='removed', before=before[k]))
            elif before[k] != after[k]:
                rows.extend(changes(before[k], after[k], path + (k,)))
    elif before != after:
        rows.append(dict(path=list(path), kind='changed', before=before, afterHash=digest(after)))
    return sorted(rows, key=lambda r: r['path'])


# name, habitat, relative weight, weather preference, minimum/maximum cm, price, description
# Non-Glowhaven weather is neutral: these preferences never gate availability.
FISH = [
    ('Crownwater Dace', 'r', 32, 'clear', 8, 22, 3,
     'A silver dace with a violet gill mark, common in Caelrath’s open canals.'),
    ('Violetfin Perch', 'r', 27, 'overcast', 12, 30, 5,
     'A striped reservoir perch with violet fins and firm white flesh.'),
    ('Terrace Trout', 'r', 19, 'rain', 20, 44, 9,
     'A speckled trout from cool terrace channels; quick to dart beneath a sluice.'),
    ('Goldscale Bream', 'reh', 21, 'overcast', 18, 39, 7,
     'A broad golden bream found in lower canals and sheltered brackish harbors.'),
    ('Lanternbelly Smelt', 'hsd', 31, 'clear', 7, 18, 4,
     'A small coastal fish whose translucent belly gleams softly after dusk.'),
    ('Bellglass Carp', 'r', 2, 'fog', 32, 68, 30,
     'A scarce pale carp with translucent scales that briefly ring against a landing net.'),
]

HOME = 'Crownwater Row'
HOME_KEY = 'Key and Deed to 14 Crownwater Row'
KEY_GUIDANCE = (
    'Caelrath Portal Hall has a fixed, keyless crossing to Evertree Base - Portal Room in Glowhaven. '
    'Akihisa Sakimori at the Visitor Desk can verify an established local resident, household member, '
    'institute learner or posted recruit and issue the reusable Ardelis Portal Key for their return. '
    'A routine check of that existing local connection is enough; no Rebirth quest, Vladimir meeting, '
    'guild qualification or invented fee is required. Visitors from Glowhaven still need genuine '
    'bilateral sponsorship. The key does not transport anyone until they choose to cross.'
)


def start(name, description, narrative, location, area, guidance, items=None):
    return dict(name=name, description=description, storyStart=narrative,
                locations=[location], locationAreas=[f'{location} - {area}'], startingQuests=[],
                startingItems=[dict(item='Mark', quantity=1000)] + (items or []),
                startingPartyNPCs=[], isDefault=False,
                questGenerationGuidance=guidance + '\n\n' + KEY_GUIDANCE)


def apply(w):
    # Finish the user's new pin; its exact region, coordinates and radius survive.
    house = w['locations'].pop('residential area')
    house.update(name=HOME, complexityType='complex', detailType='detailed',
        basicInfo='A narrow residential lane follows an upper water terrace. Pale two-storey houses share violet shutters, small walled gardens and a view of the aqueduct. Number 14 has an iron gate, a ground-floor sitting room and a modest upper bedroom. Bakers’ deliveries and neighbors’ washing make this a lived-in street.',
        hiddenInfo='Number 14 is the home established by A Door of Your Own: its selected player already owns it and has the matching key and deed. In a shared start the household may be jointly owned. Other beginnings do not grant ownership. Keep residents’ private homes separate; access to this house is not access to the whole row. The purchase predates the opening, so charge no new purchase price or recurring rent.')
    house['areas'] = {
        f'{HOME} - Lane': dict(description='Pale walls and violet shutters line a narrow paved lane. A shared drain runs beneath the aqueduct parapet; deliveries leave room for people to pass.', paths=[f'{HOME} - Number 14 Sitting Room']),
        f'{HOME} - Number 14 Sitting Room': dict(description='A brass 14 marks the front door. Unpacked boxes stand beside a plain hearth, a sturdy table and a window overlooking the lane. A narrow stair leads up; a rear door opens into a small walled garden.', paths=[f'{HOME} - Lane', f'{HOME} - Number 14 Bedroom', f'{HOME} - Number 14 Garden']),
        f'{HOME} - Number 14 Bedroom': dict(description='The upper room has a bed, empty shelves and a wardrobe with one squeaking hinge. A high window admits morning light and the sound of water passing along the terrace.', paths=[f'{HOME} - Number 14 Sitting Room']),
        f'{HOME} - Number 14 Garden': dict(description='A small enclosed garden has a washing line, an unplanted bed and a rain barrel. The low rear wall looks toward the aqueduct but gives no public passage through the house.', paths=[f'{HOME} - Number 14 Sitting Room']),
    }
    w['locations'][HOME] = house
    w['itemTypes'][HOME_KEY] = dict(name=HOME_KEY, category='Key', bonuses=[],
        description='A front-door key and completed deed for 14 Crownwater Row, Caelrath, Ardelis. The named owner has already bought and taken possession of the house; the papers record the holder’s household, address and ownership.', needsMediaGeneration=True)

    for name, habitat, weight, weather, low, high, price, desc in FISH:
        assert name not in w['itemTypes'], name
        w['itemTypes'][name] = dict(name=name, category='Consumable', tier='mundane', estimatedValue=price,
                                  description=desc, bonuses=[], needsMediaGeneration=True)
    for key in ['fsh_cast_lure', 'fsh_cast_bait']:
        t = w['triggerDefinitions'][key]
        end = t['script'].index(';\n')
        rows = json.loads(t['script'][len('const fish='):end])
        assert len(rows) == 51
        rows.extend([[n, h, wt, we, lo, hi, 'i'] for n, h, wt, we, lo, hi, _, _ in FISH])
        t['script'] = 'const fish=' + json.dumps(rows, ensure_ascii=False, separators=(',', ':')) + t['script'][end:]
    for key in ['fsh_cast_lure', 'fsh_cast_bait', 'fsh_bait_miss']:
        t = w['triggerDefinitions'][key]
        old = '"Akitsuhara":"k"}'
        assert t['script'].count(old) == 1
        t['script'] = t['script'].replace(old, '"Akitsuhara":"k","Ardelis":"i"}')
        t['script'] = t['script'].replace('canal|snowmelt', 'canal|reservoir|aqueduct|snowmelt')
    for key in ['fsh_rare_land', 'fsh_rare_miss', 'fsh_rare_release', 'fsh_rare_cleanup']:
        t = w['triggerDefinitions'][key]
        assert t['script'].count('"Moonbell Koi"]') == 1
        t['script'] = t['script'].replace('"Moonbell Koi"]', '"Moonbell Koi","Bellglass Carp"]')
    w['worldLore']['Angling and Regional Waters']['text'] += (
        '\n\nIn Ardelis, open Caelrath canals and reservoirs hold Crownwater Dace, Violetfin Perch and Terrace Trout. '
        'Goldscale Bream tolerate the lower canals and sheltered brackish harbors; Lanternbelly Smelt school along the coast. '
        'Rare Bellglass Carp favor quiet freshwater. Fishers use public banks or obtain permission; drinking cisterns, '
        'ornamental basins and sealed aqueducts are not public fishing grounds.'
    )

    # One semantic handover, one native item owner, no campaign-wide authorization flag.
    w['triggerDefinitions']['ar_local_key_issue'] = dict(name='ar_local_key_issue', recurring=True, scope='player',
        conditions=[dict(type='party-location', operator='equals', value='Caelrath Portal Hall'),
                    dict(type='player-item', operator='equals', value=0, item='Ardelis Portal Key'),
                    dict(type='action', query='This player actually requests their own Ardelis return-route key from Akihisa Sakimori at the Visitor Desk or Registrar’s Office. Their genuine local residence, household membership, institute place, guard/paladin posting or valid bilateral sponsorship is already established in play, including an Ardelis story-start premise, and can be routinely verified now. A bare claim, forgery, another person’s permission, a hypothetical future request or a request merely for directions is false. No unrelated quest or special patron is needed for a genuine local connection.')],
        effects=[dict(type='item-add', item='Ardelis Portal Key', quantity=1, target='satisfyingPlayers'),
                 dict(type='story', instruction='Akihisa checks the traveler’s established local connection or genuine sponsorship and hands over the one reusable key recorded by the item effect. Explain that this hall’s fixed arch reaches Glowhaven without a key, while this key permits the journey back from Evertree Base. There is no fee, palace clearance, extra item or automatic crossing.')])
    w['itemTypes']['Ardelis Portal Key']['description'] = (
        'Reusable permission for the Evertree–Caelrath route. Transit officers issue it after verifying genuine bilateral sponsorship or an established Ardelis local connection. Caelrath Portal Hall’s fixed crossing to Glowhaven needs no key.'
    )
    w['worldLore']['Ardelis — Passage and Jurisdiction']['text'] = (
        'The Evertree and Caelrath Portal Hall are the fixed endpoints of a restricted bilateral route. '
        'Travelers entering from Glowhaven need an issued Ardelis Portal Key and genuine named sponsorship. '
        'Vladimir can arrange a meeting without joining the party; the two courts provide an independent route. '
        'Ardelis residents, household members, institute learners and posted recruits can instead ask Akihisa Sakimori '
        'at Caelrath’s Visitor Desk for a reusable key after an ordinary check of their established local connection. '
        'The selected Ardelis beginning supplies that connection, not a claim to imperial authority. '
        'No Rebirth investigation, guild exam or fee is needed for this local issue. '
        'The hall’s fixed crossing always reaches Evertree Base - Portal Room in Glowhaven and needs no key. '
        'An Ardelis start gives no key automatically; the local desk is available before departure. '
        'Keys confer passage, not palace access. Local offenses do not use Glowhaven’s Wraith Island automatic custody system.'
    )
    hall = w['locations']['Caelrath Portal Hall']
    hall['basicInfo'] = (
        'A staffed hall connects Caelrath with Evertree Base in Glowhaven. Its fixed arch leads to the Evertree Portal Room without a key. '
        'At the Visitor Desk, Akihisa Sakimori issues reusable Ardelis route keys to travelers with verified sponsorship or an established local home, household, institute place or service posting. The key permits the journey back from Glowhaven.'
    )
    hall['areas']['Caelrath Portal Hall - Visitor Desk']['description'] = (
        'An orderly visitor desk stands beneath a board reading “Glowhaven passage and return keys.” '
        'A transit officer checks local records and genuine invitations. The open waiting court and marked stairs lead to the fixed portal room.'
    )
    w['npcs']['Akihisa Sakimori']['hiddenInfo'] += '\n\nLocal transit: ' + KEY_GUIDANCE

    extra = [
        start('👑 Ardelis: A Place at the Family Table',
            'Begin in Caelrath, capital of Ardelis, as an adult junior noble with a place at the Minazuki table. A family supper, an inconvenient promise and two invitations compete for your attention. Your title opens doors; it does not settle the arguments inside.',
            '''The soup has gone cold while Hidetaka Minazuki finishes a story about a horse nobody else remembers fondly.

“It bit the magistrate,” Ruri says, separating two letters from the supper tray.

“An excellent judge of character.”

The dining-room windows overlook Caelrath’s upper terraces. Behind the glass, water pours beneath a bridge busy with servants, messengers and people who will never be invited to this table. Here a place has been set for you: an adult junior member of the lesser nobility, received under the Minazuki household’s roof. Your own family and your reasons for accepting their hospitality remain yours.

One letter invites the household’s younger relations to a music evening. The other asks for a representative at tomorrow’s hearing over a leased orchard. Neither has your name on the reply yet.

Ruri sets them between the bread and a dish of untouched pears. “I need someone at the hearing who will listen to the growers. My uncle seems to think listening is what happens while he prepares his answer.”

“And I need someone at the evening who won’t insult our host,” Hidetaka says. “We must all make sacrifices.”

A footman reaches for the soup tureen. Ruri stops him with a hand; she has barely eaten. Across the table, Hidetaka breaks the seal on his own correspondence. The two unanswered invitations remain within reach.''',
            'House Minazuki Estate', 'Family Dining Room',
            'The player is an adult junior noble of a lesser house with genuine household ties, not a royal child or automatically a named Minazuki’s close relative. Let their selected background supply family details without rewriting the authored family. Hidetaka and Ruri are occupied with their own interests. Either invitation, both with a workable arrangement, or neither is possible. No task is already accepted, reward promised or conspiracy revealed. No rank, advanced skill, private palace access or new fortune follows from the title.'),
        start('🛡️ Ardelis: Beneath the Starward Banner',
            'Begin in Caelrath, Ardelis, as a newly admitted adult paladin recruit. Your first watch concerns ordinary people on a crowded stair. Veterans disagree about what good service looks like; your own training determines what you can do.',
            '''A practice shield rolls across the Starward Commandery’s court and strikes the boot of a woman in ivory plate.

Serika Tōgane traps it under one heel. “Useful. Now the enemy has a seat.”

The recruit who dropped it goes scarlet. His partner, still wearing her cloak backward, looks desperately at the rack instead. Above them the violet banner lifts in the mountain wind. Beyond the parapet lie Caelrath’s white terraces, its crowded bridges and a palace much too distant to hear a dropped shield.

Today is your first day with the order. Your admission is settled; the person beneath the new posting is the one you created, with that person’s actual training.

Osamu Narusawa arrives carrying two medical rolls. Serika reaches for one. He keeps it.

“The hospice stair this morning,” he says. “A delivery, market traffic and a broken handrail. Someone needs to keep the passage clear.”

“And learn to give an instruction people can hear,” Serika adds.

“Without mistaking volume for judgment.”

From the gate, Akihiro Kanzaki calls Serika to a meeting. She retrieves her spear and points toward the two recruits before going. “You’re all expected back for practice. Bring the shields. Preferably in your hands.”

Osamu lays a roll beside the gate and checks its ties. The recruits begin arguing in whispers about who should speak to the cart drivers. The stair is a short walk away; the chaplain has left room for a question before anyone sets off.''',
            'Starward Commandery', 'Practice Court',
            'Establish an ordinary novice posting with the Starward Oath, distinct from the palace guard, city watch and cult. Do not require a second application or grant unearned levels, affinities, spells, combat skills or plate armor. Serika, Osamu and Akihiro are at their own commandery; the two unnamed fellow recruits are incidental peers, not new canonical principals or forced companions. The first responsibility is a manageable local watch, not a Rebirth mission or compulsory fight. The player can ask questions, raise an objection, request different work or leave. Actual agreement may establish an ordinary quest; do not mark duty done just for hearing it.'),
        start('🏠 Ardelis: A Door of Your Own',
            'Begin in Caelrath, Ardelis, inside the house you have just bought at 14 Crownwater Row. The deed is settled, the boxes are not, and your neighbors already have opinions. Make a home in the imperial capital on your own terms.',
            '''The front door opens properly on the third try. The trick, apparently, is lifting it slightly before turning the key.

Fourteen Crownwater Row is yours. The purchase is complete; the key and deed are already among your belongings. Inside, morning light crosses unopened boxes, a bare table and the clean rectangle where the previous owner’s rug used to lie. Upstairs a wardrobe hinge complains each time the breeze catches it.

Outside, two neighbors are trying to carry a flowering shrub through a gate narrower than its pot.

“Turn it,” the woman says.

“I am turning it.”

“The pot, not yourself.”

A basket of bread rests on the low wall. Nina Suzuhara, the baker making her morning deliveries, is keeping a running count of how many times the shrub has come back out.

“Five,” she says. Then she notices the open door. “Oh, good. Someone lives here now. I’m Nina, from Threadneedle. The previous owner ordered two loaves every fourth morning. You can tell me if that’s a habit worth keeping.”

Water glints beyond the terrace parapet. Far below, a bell sounds in Kingsward, where the Portal Hall handles travel to Glowhaven. Here there is an empty house to arrange, a delivery to consider and a shrub that has once again reached the wrong side of the gate.''',
            HOME, 'Number 14 Sitting Room',
            'The player already owns Number 14. Its exact key and deed are starting inventory, so neither the custom-property handover rule nor the narrator should create another key, sale, charge or rent. Use the selected player’s name when referring to the owner; in a shared household beginning establish co-ownership rather than rival deeds. Nina is visiting on a delivery round and returns to her bakery afterward; do not permanently move her card or recruit the neighbors. The shrub and bread are ordinary optional interactions, not automatic quests. Furnishings are modest; boxes contain ordinary selected personal belongings, not bonus wealth or equipment.',
            [dict(item=HOME_KEY, quantity=1)]),
    ]
    order = {}
    for k, v in w['storyStarts'].items():
        if k.startswith(('🛡️ Ardelis:', '🏘️ Ardelis:', '🔬 Ardelis:', '🎭 Ardelis:')):
            v['questGenerationGuidance'] += '\n\n' + KEY_GUIDANCE
        order[k] = v
        if k == '🎭 Ardelis: An Orselle Invitation':
            order.update({s['name']: s for s in extra})
    assert len(order) == len(w['storyStarts']) + 3
    w['storyStarts'] = order
    return [s['name'] for s in extra]


def main():
    p = argparse.ArgumentParser(); p.add_argument('--base', required=True); args = p.parse_args()
    raw = Path(args.base).read_bytes(); base = json.loads(raw.decode('utf-8-sig'))
    before = json.loads(WORLD.read_text(encoding='utf-8-sig'))
    w = copy.deepcopy(base); names = apply(w)
    review = dict(inputSHA256=hashlib.sha256(raw).hexdigest(), baseHash=digest(base), afterHash=digest(w),
                  starts=names, fish=[f[0] for f in FISH], renamedLocation={'residential area': HOME},
                  noPublicPatchNotes=True, rows=changes(base, w))
    historical = HERE/'historical-review.json'
    if not historical.exists():
        write(historical, dict(baseHash=digest(before), afterHash=digest(w), rows=changes(before, w)))
    else:
        assert json.loads(historical.read_text(encoding='utf-8'))['afterHash'] == digest(w), 'Review changed patch before rebuilding'
    write(HERE/'review.json', review); write(WORLD, w)
    print(json.dumps(dict(fish=len(review['fish']), starts=len(names), changedLeaves=len(review['rows']),
                         itemCharacters=len(json.dumps(w['itemTypes'], ensure_ascii=False, separators=(',', ':')).encode('utf-16-le'))//2)))


if __name__ == '__main__':
    main()
