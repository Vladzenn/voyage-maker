"""Narrow playtest patch, built on the freshly downloaded Alpha draft."""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import project

HERE = Path(__file__).resolve().parent
TMP = ROOT / 'tmp/playtest-phantom-2026-11-06'
TALENT = 'Quickened Chorus'
ORIGIN = 'Otherworld Rebirth'


def trait(name, description, narrative, skill=None, resources=()):
    return dict(name=name, description=description, traitNarrativeEffects=narrative,
                attributes=[], skills=[dict(skill=skill, modifier=1)] if skill else [],
                resources=list(resources), startingItems=[], abilities=[], unlockedBy=[],
                excludedBy=[], requirements=[])


def tc(name, has=True):
    return dict(type='player-traits', operator='contains' if has else 'notContains', value=name)


def te(name, add=True):
    return dict(type='player-traits', operator='add' if add else 'remove', value=name, target='satisfyingPlayers')


def meter(n):
    return dict(type='player-resource', operator='set', resource='Resonance', value=n, target='satisfyingPlayers')


def rule(name, conditions, effects):
    return dict(name=name, recurring=True, phase='planning', scope='player', conditions=conditions, effects=effects)


def patch(w):
    # Preserve the complete downloaded draft, including its order and native normalization.
    before = copy.deepcopy(w)
    past = [
        ('Work and Trade', 'Workshop Apprentice', 'Magitech', 'You spent years fitting ordinary mechanisms, sorting parts and learning which tolerances matter.'),
        ('Work and Trade', 'Apothecary Assistant', 'Alchemy', 'You washed vessels, weighed ingredients and learned to distinguish a useful preparation from a ruined batch.'),
        ('Work and Trade', 'Inn Kitchen Hand', 'Cooking', 'You kept meals moving through crowded services and learned to make a modest pantry feed one more guest.'),
        ('Work and Trade', 'Former Market Trader', 'Trade', 'You once made your living weighing stock, bargaining and knowing which promises a customer would remember.'),
        ('Work and Trade', 'Former Estate Steward', 'Etiquette', 'You managed household arrangements, visiting guests and the delicate business of explaining what a budget cannot cover.'),
        ('Travel and Water', 'Former Sailor', 'survival', 'You served aboard a working vessel, learning watches, weather signs and the limits of tired hands.'),
        ('Travel and Water', 'Riverhand', 'Fishing', 'You worked river banks and small boats, reading current and handling lines without tangling everyone else’s gear.'),
        ('Travel and Water', 'Caravan Hand', 'Animal Handling', 'You cared for pack animals, checked harness and learned when a stubborn beast had a sensible objection.'),
        ('Travel and Water', 'Former Courier', 'acrobatics', 'You carried messages through busy streets and awkward shortcuts, learning where haste is useful and where it breaks an ankle.'),
        ('Care and Community', 'Herbalist Apprentice', 'Medicine', 'You learned basic field dressings and useful local plants under someone who checked your work.'),
        ('Care and Community', 'Temple Volunteer', 'Insight', 'You helped visitors through ordinary grief, celebration and practical trouble without having an answer for everything.'),
        ('Care and Community', 'Village Mediator', 'persuasion', 'Neighbors once asked you to sit between incompatible accounts and find a concession both could live with.'),
        ('Study and Experiment', 'Archive Assistant', 'investigation', 'You sorted damaged records, chased references and learned that a confident citation can still be wrong.'),
        ('Study and Experiment', 'Former Research Assistant', 'spellcraft', 'You kept experiment notes and repeated small controlled trials, often finding the overlooked detail in another person’s theory.'),
        ('Study and Experiment', 'Wardkeeper’s Apprentice', 'Enchantment Magic', 'You helped maintain modest household enchantments and learned to inspect a worn working before trying to improve it.'),
        ('Performance and Public Life', 'Traveling Performer', 'performance', 'You played for unfamiliar audiences and learned to recover when a joke, cue or entrance went wrong.'),
        ('Performance and Public Life', 'Former Stagehand', 'athletics', 'You hauled scenery, steadied ladders and learned the precise weight of someone else’s grand artistic vision.'),
        ('Performance and Public Life', 'Former Civic Clerk', 'Trade', 'You handled fees, appointments and mismatched records, learning to make an account understandable to the person paying it.'),
    ]
    cat = w['traitCategories']['Past Experience']
    for group, name, skill, text in past:
        w['traits'][name] = trait(name, text + f' Start with +1 {w["skills"][skill].get("name", skill)}.',
                                 text + ' This earlier experience supplies only its listed familiarity, not a present job, license, equipment or personal connection.', skill)
        cat['traits'].append(name)
        sub = next((s for s in cat['subcategories'] if s['name'] == group), None)
        if sub is None:
            sub = dict(name=group, traits=[]); cat['subcategories'].append(sub)
        sub['traits'].append(name)
    impressions = {
        'Unbothered Bearing': 'Loose shoulders, an easy pace and an unhurried expression can make you seem chilled and difficult to fluster.',
        'Sleepy Composure': 'Heavy-lidded eyes and a leisurely manner can suggest someone who refuses to spend energy on a needless fuss.',
        'Relaxed Charm': 'A casual smile and comfortable manner can make ordinary conversation feel easy.',
        'World-Weary Look': 'A patient stare and a faintly tired manner can suggest that you have heard this particular speech before.',
        'Bookish Air': 'A thoughtful manner and attention to detail can make you look more at home with a question than a spectacle.',
        'Restless Energy': 'Quick gestures and a habit of looking toward the next activity can make you seem eager to get moving.',
        'Earnest Awkwardness': 'Careful words and imperfect timing can give an impression of sincere effort rather than practiced polish.',
        'Playfully Cheeky': 'An amused glance and a lightly irreverent manner can suggest that you are already finding the funny side.',
        'Gentle Reserve': 'A soft voice and considered gestures can make you seem considerate without being eager to reveal everything.',
        'Distant Elegance': 'An composed posture and measured expression can seem refined or aloof, depending on the observer.',
        'Scruffy Practicality': 'Lived-in presentation and an unfussy manner can suggest someone more interested in getting things done than looking immaculate.',
        'Focused Intensity': 'A steady gaze and close attention can make even an ordinary task look as though it has your full concentration.',
    }
    impressions['Distant Elegance'] = impressions['Distant Elegance'].replace('An composed', 'A composed')
    for name, text in impressions.items():
        w['traits'][name] = trait(name, text, text + ' This is an optional visible first impression, not prescribed feelings, competence, clothing, attraction or another character’s guaranteed reaction.')
        w['traitCategories']['First Impression']['traits'].append(name)

    w['traits'][ORIGIN] = trait(ORIGIN,
        'An isekai origin: you lived in another world and awakened here in your selected present body, with memories of that earlier life. Start with +1 Insight. This origin also opens the Rebirth storyline; your chosen opening still determines where play begins.',
        'Your earlier world and life are the player’s to define. Present ancestry describes the body you awakened in, not a childhood automatically spent in this world. Preserve the chosen opening and any explicitly established time since arrival. Your origin is private until actually disclosed or discovered; it grants no public hero status, automatic mastery or invented death scene.', 'Insight')
    origins = w['traitCategories']['Origin & Upbringing']; origins['traits'].append(ORIGIN)
    origins['subcategories'].append(dict(name='Otherworldly Origins', traits=[ORIGIN]))
    origins['description'] = 'Optionally choose one formative community or Otherworld Rebirth. Each adds +1 to a useful skill; the selected opening sets your current circumstances.'
    init = rule('rb_otherworld_origin', [tc(ORIGIN), tc('Summoned one', False)], [te('Summoned one')])
    init['script'] = "if(storage.rbCampaign!==true){storage.rbCampaign=true;if(storage.rbPhase===undefined)storage.rbPhase=0;if(storage.rbOriginTick===undefined)storage.rbOriginTick=Number(check({type:'game-tick'}))||0;}"
    w['triggerDefinitions'][init['name']] = init
    start = w['storyStarts']['🌅 Rebirth: A Morning in Brookmeadow']
    start['description'] = 'An isekai beginning in Brookmeadow, in the Glowhaven countryside. After a life in another world, you awaken here in your selected body with your old memories intact. Two locals rescued you from the shore and offered shelter. What you tell them is up to you.'
    start['storyStart'] = start['storyStart'].replace('The player is the person found unconscious on the nearby shore.', 'This is an isekai awakening after a life in another world, not an infant birth or a childhood raised in Glowhaven. The player is the person found unconscious on the nearby shore.')
    start['storyStart'] = start['storyStart'].replace('You wake up in a body that isn’t yours.', 'You remember a life in another world. Now you wake in a different body, beneath a ceiling you have never seen.')
    bg = w['aiInstructions']['generateCharacterBackground']
    bg['Formation, Work and Forward Direction'] = (
        'Use a few relevant influences from the selected family, community, work or training; no exhaustive childhood or compulsory tragedy. Preserve cultural naming and explicitly established ties. Explain useful practice without granting mastery, equipment or a current appointment. Leave the player’s future choices open.\n\n'
        'For Otherworld Rebirth or the Rebirth opening, explicitly establish an isekai origin: an earlier life in another world, memories retained and awakening in the selected present body. Upbringing and past experiences normally describe that previous life; any adaptation here needs explicitly established elapsed time. Do not invent a childhood or family in this world, a death scene, Earth origin or publicly known hero identity. Other openings retain their actual premise and location. Otherworld Rebirth is not mandatory for ordinary natives.')
    opening = w['aiInstructions']['generateInitialStart']['Selected Opening and Special Context']
    w['aiInstructions']['generateInitialStart']['Selected Opening and Special Context'] = opening + '\n\nRebirth: explicitly show remembered life in another world and awakening in the chosen present body, not being born or raised here. For Otherworld Rebirth with another selected opening, preserve that opening and established adaptation rather than replaying the cottage rescue. NPCs do not know this private origin without evidence.'
    clock = w['triggerDefinitions']['rb_clock']['script']
    assert clock.count('tick - originTick >= 200') == 1
    w['triggerDefinitions']['rb_clock']['script'] = clock.replace('tick - originTick >= 200', 'tick - originTick >= 100')
    w['triggerDefinitions']['rb_visitors_depart']['conditions'][1]['value'] = 101

    w['nameFilterSettings']['Fenwick'] = dict(replacements=['Matsumoto', 'Ishida', 'Morita', 'Shibata', 'Takeda', 'Hasegawa', 'Numata', 'Fujita'])
    w['progressionSettings']['startingCharacterLevelUpRequirement'] = 550
    titles = ['Trailfoot', 'Curious Wanderer', 'Wayfarer', 'Pathfinder', 'Trailblazer', 'Taleweaver', 'Farstrider', 'Marvelmaker', 'Realmroamer', 'Horizon Seeker', 'Worldwalker', 'Walking Folktale', 'Mythmaker', 'Ascendant', 'Northern Star', 'A Story Without End']
    w['progressionSettings']['milestoneTitles'] = [dict(levelGranted=1 if i == 0 else i * 10, title=title) for i, title in enumerate(titles)]
    assert w['progressionSettings']['abilityPointsPerGrant'] == before['progressionSettings']['abilityPointsPerGrant'] == 1
    labels = ['Bitter Enmity', 'No Friend of Mine', 'At Daggers Drawn', 'Rather Unfriendly',
              'A Touch Frosty', 'Neither Here nor There', 'Pleasant Enough', 'Quite Friendly',
              'Rather Dear', 'Near and Dear', 'A Place in My Heart']
    assert len(w['relationshipStages']) == len(labels)
    for stage, label in zip(w['relationshipStages'], labels):
        stage['name'] = label

    # Background civilians lose combat levels; preserve their original HP multipliers.
    civilian_types = {'Resident', 'Merchant', 'Artisan', 'Performer', 'Researcher', 'Guild Staff', 'Healer', 'Court Official', 'Noble'}
    trained = re.compile(r'\b(guard|soldier|paladin|shinobi|samurai|ronin|rōnin|warrior|fighter|duelist|adventurer|mercenary|assassin|bandit|hunter|warden|marshal|captain|emperor|empress|king|queen|princess|bodyguard|swordsman|swordswoman|combat instructor|combatant)\b', re.I)
    tier_hp = dict(trivial=.15, weak=.5, average=1)
    level_rows = []
    for name, npc in w['npcs'].items():
        identity = npc.get('basicInfo', '').split('\n\n')[0][:350]
        if npc.get('type') not in civilian_types or npc.get('tier') not in tier_hp or trained.search(identity):
            continue
        level = npc.get('level', 1)
        if level <= 6:
            continue
        base = (w['otherSettings']['npcMinHealth'] + w['otherSettings']['npcHealthPerLevel'] * level) * tier_hp[npc['tier']]
        old_multi = npc.get('healthMultiplier', 1)
        new_level = min(level, 8, (level + 5) // 6)
        npc['level'] = new_level
        after_hp = (w['otherSettings']['npcMinHealth'] + w['otherSettings']['npcHealthPerLevel'] * new_level) * tier_hp[npc['tier']] * old_multi
        level_rows.append(dict(npc=name, beforeLevel=level, afterLevel=new_level, tier=npc['tier'], beforeNeutralHP=round(base * old_multi, 2), afterNeutralHP=round(after_hp, 2)))
    w['aiInstructions']['generateNewNPC']['Affinity and Competence Selection'] = (
        'NEW casters draw affinity counts independently: one 65%, two 25%, three 10%. Use actual available randomness; never claim an unperformed roll. Choices: Arcane, Metal, Gravity, Enchantment, Space, Fire, Lightning, Earth, Wind, Water, Healing, Nature, Light, Summoning, Soul, Divination, Void, Illusion, Ice, Sound. Never Time. Spellcraft and Magitech are skills.\n\n'
        'Affinity eases learning, not mastery. Describe actual training separately. Space needs Gravity study; Time needs exceptional reserved instruction. Body casting is learned, focuses usually store no reserve, and bodily augmentation is Enchantment. Noncasters remain valid.\n\n'
        'Ordinary noncombatant workers generally use levels 1–6; exceptional civilian specialists 7–8. Age and craft seniority are not combat levels. Guards, fighters, faculty and exceptional authored people retain their established bands. Preserve existing records; do not scale them to the player, invent an apex shopkeeper or exceed levels 1–100.')

    w['traits'][TALENT] = trait(TALENT,
        'Your elemental combinations find their chorus sooner. Reduce maximum Resonance from 20 to 16; a full sixteen points readies the same surge. Earn each point through a real elemental reaction.',
        'Your personal Resonance capacity and charging threshold are 16 instead of 20. Readiness still requires genuinely earned charge. This does not grant starting charge, passive recovery, cheaper spells, an extra reaction or stronger surge damage.', resources=[dict(resource='Resonance', modifier=-4)])
    cat = w['traitCategories']['Special Talent']; cat['traits'].append(TALENT)
    next(s for s in cat['subcategories'] if s['name'] == 'Arcane Peculiarities')['traits'].append(TALENT)
    rules = w['triggerDefinitions']; receipt = 'Gathered Resonance'; ready = 'Resonant'
    rules['mx_resonance_earn_15']['conditions'].append(tc(TALENT, False))
    rules['mx_resonance_earn_20']['conditions'].append(tc(TALENT, False))
    rules['mx_resonance_mirror_20']['conditions'].append(tc(TALENT, False))
    t = rule('mx_resonance_quickened_earn', [tc(TALENT), tc('Resonance: 15'), tc(receipt)],
             [te(receipt, False), te('Resonance: 15', False), te(ready), meter(16), dict(type='story', instruction='Your earned Resonance reaches its personal full chorus. The next landed damaging technique can release it; do not empower an already resolved action.')])
    rules[t['name']] = t
    for n in range(16, 20):
        t = rule(f'mx_resonance_quickened_convert_{n}', [tc(TALENT), tc(f'Resonance: {n}')],
                 [te(f'Resonance: {n}', False), te(ready), te(receipt, False), meter(16)])
        rules[t['name']] = t
    t = rule('mx_resonance_quickened_full', [tc(TALENT), tc(ready), tc(receipt)], [te(receipt, False), meter(16)])
    rules[t['name']] = t
    t = rule('mx_resonance_quickened_mirror', [tc(TALENT), tc(ready), tc(receipt, False), dict(type='player-resource', resource='Resonance', operator='notEquals', value=16)], [meter(16)])
    rules[t['name']] = t
    for n in range(1, 20):
        w['traits'][f'Resonance: {n}']['description'] = f'You have gathered {n} points of Resonance through elemental reactions. Your full chorus is 20 points, or 16 with Quickened Chorus.'
    w['traits'][ready]['traitNarrativeEffects'] = w['traits'][ready]['traitNarrativeEffects'].replace('Exactly 20 earned Resonance.', 'Your personal full chorus is earned: normally 20 Resonance, or 16 with Quickened Chorus.')
    usage = w['resourceSettings']['Resonance']['usageInstructions']
    w['resourceSettings']['Resonance']['usageInstructions'] = usage.replace('from 0 to 20.', 'from 0 to your personal maximum: 20 normally, 16 with Quickened Chorus.').replace('No currently authored item lowers the threshold.', 'Quickened Chorus lowers both capacity and charging threshold by 4; it supplies no charge. No currently authored item changes that threshold.')
    key = 'Reaction Resolution and Resonance'
    w['aiInstructions']['generateActionInfo'][key] += '\nQuickened Chorus has a native 16-point maximum and readies its surge at 16 genuinely earned points. Other characters retain 20. Use the supplied readiness state; the talent itself never fills the meter.'
    resources = {}
    for name, data in w['resourceSettings'].items():
        if name == 'Resonance':
            continue
        resources[name] = data
        if name == 'Stamina':
            resources['Resonance'] = w['resourceSettings']['Resonance']
    w['resourceSettings'] = resources
    return w, level_rows


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--apply', action='store_true'); args = parser.parse_args()
    if args.apply and (HERE / 'review.json').exists():
        reviewed = project.load(HERE / 'review.json')
        actual = hashlib.sha256(project.WORLD.read_bytes()).hexdigest()
        if actual not in {reviewed['baseRawSHA256'], reviewed['afterRawSHA256']}:
            raise ValueError('Newer canonical work exists; read a fresh Studio draft and reconcile. No overwrite performed.')
    baseline_path = TMP / 'local-before.json'
    if not baseline_path.exists():
        baseline_path.write_bytes(project.WORLD.read_bytes())
    live = project.load(TMP / 'live-world.json')
    candidate, levels = patch(copy.deepcopy(live))
    project.validate(candidate)
    out = ROOT / 'output/playtest-phantom-2026-11-06'; out.mkdir(parents=True, exist_ok=True)
    project.write_json(out / 'world.json', candidate)
    envelope = dict(world=copy.deepcopy(project.load(TMP / 'live-envelope.json')['data']['world']))
    envelope['world']['initialGameState'] = candidate
    project.write_json(TMP / 'candidate-envelope.json', envelope)
    project.write_json(HERE / 'level-review.json', dict(policy='Eligible background civilian levels above six are reduced to ceil(old level / 6), capped at eight. Levels already at six or below and actual trained roles are preserved. Original HP multipliers, tiers and ability descriptions are unchanged; native HP and damage follow the new level.', rows=levels))
    if args.apply:
        project.write_json(project.WORLD, candidate)
    print(json.dumps(dict(applied=args.apply, newPastExperiences=18, newFirstImpressions=12, civilianLevelRecords=len(levels), resonanceTalent=TALENT, resonanceCap=16, otherworldOrigin=ORIGIN, rawSHA256=hashlib.sha256((out/'world.json').read_bytes()).hexdigest())))


if __name__ == '__main__':
    main()
