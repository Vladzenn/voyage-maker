"""Build Rebirth from the explicitly approved world, with a reversible review."""
import argparse
import copy
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import project

BASE_SHA = 'a84f4a5e898d6bd85f35b96b354523fe36a0afaeea556b8c827f261d22613200'
START = '🌅 Rebirth: A Morning in Brookmeadow'
VLAD = "Valkazathoth'dmir"
POCKET = "Vladimir's Elsewhere"
REGION = 'The Lantern Circuit'
KEY = 'Shadowspire Guest Key'


def js(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def condition(kind, value, operator='equals', **extra):
    return dict(type=kind, operator=operator, value=value, **extra)


def effect(kind, value, operator='set', **extra):
    return dict(type=kind, operator=operator, value=value, **extra)


def tell(text):
    return dict(type='story', instruction=text)


def trait(name, description, **extra):
    return dict(name=name, description=description, traitNarrativeEffects=description,
                attributes=[], skills=[], resources=[], startingItems=[], abilities=[],
                unlockedBy=[], excludedBy=[], requirements=[], **extra)


def rule(w, name, conditions, effects=(), script=None, recurring=False, scope='party', phase=None):
    value = dict(name=name, conditions=conditions, effects=list(effects), recurring=recurring, scope=scope)
    if script is not None:
        value['script'] = script
    if phase:
        value['phase'] = phase
    w['triggerDefinitions'][name] = value


def quest(w, name, source, location, statement, objective, query, brief, effects=(), reward=0):
    completion = list(effects)
    if reward:
        completion += [dict(type='item-add', item='Mark', quantity=reward, target='allPlayers')]
    w['parties']['']['quests'][name] = dict(
        name=name, status='hidden', detailType='detailed', conclusive=True,
        questSource=source, questLocation=location, questStatement=statement,
        objectives={'task':dict(id='task', text=objective, status='active')},
        completionCondition=dict(type='story', query=query), questDesignBrief=brief,
        onCompleteEffects=completion)


def create_ancestry(w):
    name = 'Beastfae'
    record = trait(name, 'A rare people with fully animal-shaped faces and upright bodies. Choose a furred, scaled or feathered form, adult stature, colors and clothing. Individuals belong to many communities. Starting benefits: +1 Empathy, +2 Survival and +10 Health capacity.')
    record.update(attributes=[dict(attribute='empathy', modifier=1)], skills=[dict(skill='survival', modifier=2)], resources=[dict(resource='Health', modifier=10)])
    record['traitNarrativeEffects'] = 'Preserve the chosen animal face, body covering, hands, feet and tail in portraits and play. Beastfae are a distinct rare ancestry, with no compulsory occupation, personality or magical affinity. The native bonuses apply once.'
    w['traits'][name] = record
    cat = w['traitCategories']['Species & Ancestry']['traits']
    cat.insert(cat.index('Mixed Ancestry'), name)
    groups = {
        'Fae': [
            ('Wings', 'Butterfly-winged|Moth-winged|Dragonfly-winged|Feather-winged|Luna-moth winged|Glasswing|Swallowtail|Damselfly-winged|Lacewing|Cicada-winged|Beetle-winged|Bat-winged'),
            ('Woodland', 'Bark-scaled|Leaf-mantled|Moss-backed|Lichen-marked|Briar-spined|Reed-crested|Shell-plated|Stone-patched'),
            ('Horns and Hooves', 'Satyr|Antlered|Ram-horned|Ibex-horned|Pronghorn|Doe-eared|Hare-eared|Cloven-hoofed'),
            ('Subtler Forms', 'Wingless|Round-eared|Long-eared|Feather-crested')],
        'Beastfolk': [
            ('Ears and Tails', 'Cat|Dog|Wolf|Fox|Rabbit|Bear|Rat|Lynx|Coyote|Raccoon|Otter|Badger'),
            ('Horns and Small Mammals', 'Ram|Deer|Goat|Elk|Bison|Gazelle|Squirrel|Mouse'),
            ('Feather Accents', 'Bird|Crow|Owl|Hawk|Heron|Parrot|Sparrow|Gull'),
            ('Scale Accents', 'Reptile|Gecko|Iguana|Monitor|Skink|Chameleon|Crocodile|Turtle')],
        'Beastfae': [
            ('Canids and Broad Builds', 'Wolf|Fox|Dog|Coyote|Hyena|Jackal|Cat|Lynx|Tiger|Lion|Leopard|Cheetah|Bear|Panda|Raccoon|Badger'),
            ('Small and River Mammals', 'Rabbit|Hare|Mouse|Rat|Squirrel|Porcupine|Otter|Ferret|Marten|Red panda|Beaver|Capybara'),
            ('Hoofed Forms', 'Goat|Ram|Deer|Elk|Bison|Horse|Boar|Gazelle'),
            ('Scaled Forms', 'Gecko|Monitor lizard|Iguana|Chameleon|Skink|Crocodile|Tortoise|Bearded dragon'),
            ('Beaked Forms', 'Raven|Owl|Hawk|Heron')]
    }
    for ancestry, sections in groups.items():
        category_name = ancestry + ' Form'
        keys = []
        for group, names in sections:
            for form in names.split('|'):
                name = f'{ancestry} Form — {form}'
                if ancestry == 'Beastfolk':
                    body = f'A mostly human adult face and upright body with coherent {form.lower()} features, such as ears, feather or scale accents, horns or a tail appropriate to the form.'
                elif ancestry == 'Beastfae':
                    body = f'A fully {form.lower()}-shaped adult face and covered upright body, with fur, scales or feathers, a muzzle, snout or beak and hands and feet appropriate to the animal. Clothing fits this anatomy.'
                else:
                    body = f'An adult fae with coherent {form.lower()} features and individually chosen stature. '
                    body += {'Wings':'Use the named wing structure and a person-like adult face.', 'Woodland':'Living woodland textures form part of the body.', 'Horns and Hooves':'Preserve the selected ears, horn or hoof anatomy.', 'Subtler Forms':'Use the chosen subtle face, ear, crest or wingless silhouette.'}[group]
                if name not in w['traits']:
                    w['traits'][name] = trait(name, body)
                    w['traits'][name]['unlockedBy'] = [ancestry] + (['Mixed Ancestry'] if ancestry != 'Beastfae' else [])
                    w['traits'][name]['traitNarrativeEffects'] = body + ' The preset is optional and cosmetic. Preserve adult proportions at the chosen height. No powers, stat bonuses or compulsory temperament follow from this form.'
                keys.append(name)
        w['traitCategories'][category_name] = dict(name=category_name, description=f'Optional — choose one {ancestry} form or skip and describe your own coherent body. Presets vary in anatomy and can use your chosen colors, clothes and adult stature.', maxSelections=1, traits=keys)
    categories = w['traitCategories']
    ordered = {}
    for name, value in categories.items():
        if name in ['Fae Form','Beastfolk Form','Beastfae Form','Fae Stature']:
            continue
        ordered[name] = value
        if name == 'Species & Ancestry':
            for added in ['Fae Form','Fae Stature','Beastfolk Form','Beastfae Form']:
                ordered[added] = categories[added]
    w['traitCategories'] = ordered
    w['worldLore']['Beastfae — Faces, Bodies and Communities'] = {'text':'Beastfae are a rare distinct ancestry whose faces and upright bodies carry extensive animal anatomy. A wolf-faced neighbor may have a complete muzzle and fur coat; a reptilian person can have a scaled head, hands and tail. Their tools, clothes and furniture accommodate those bodies. Communities contain different forms and each person chooses their work, loyalties, affinities and manner. Appearance alone supplies no family history or relationship to the Fae and Beastfolk.'}
    return {ancestry:sum(len(names.split('|')) for _, names in rows) for ancestry, rows in groups.items()}


def create_scrolls(w):
    rows = []
    for line in (HERE / 'scrolls.txt').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        discipline, title, working = line.split('|', 2)
        skill = discipline + ' Magic'
        position = len(rows) % 5
        rare = position == 4 and discipline in ['Arcane','Void','Divination','Space','Soul']
        difficulty = 'masterwork' if rare else 'advanced' if position >= 3 else 'practical'
        mana = [6,8,10,18,30][position]
        item_name = 'Teaching Scroll: ' + title
        formula = 'Formula: ' + title
        assert title not in w['abilities'], title
        w['abilities'][title] = dict(name=title, description=working + f' Uses {skill}; costs {mana} Mana on a committed attempt. Actual reach, resistance and skill determine the result.', requirements=[dict(type='trait', variable=formula, amount=1)], bonus=[1,2,3,5,7][position], cooldown=[1,1,2,3,5][position])
        if discipline == 'Space':
            w['abilities'][title]['requirements'].append(dict(type='skill', variable='Gravity Magic', amount=25))
        w['traits'][formula] = trait(formula, f'You have deciphered {title}, a {skill} working. You remember its method; practice and the conditions of casting still matter.')
        w['traits'][formula]['requirements'] = [dict(type='characterLevel',amount=151)]
        w['itemTypes'][item_name] = dict(name=item_name, category='Document', description=f'A {difficulty} {discipline} formula on folded vellum. Its diagrams teach {title}. The ink fades when the reader masters the working.', bonuses=[], tier='special' if rare else 'artisan' if position >= 2 else 'mundane')
        rows.append(dict(id=f'rb_study_{len(rows)+1:03}', item=item_name, trait=formula, ability=title, difficulty=difficulty, space=discipline == 'Space'))
    assert len(rows) == 100
    template = (HERE / 'scroll_registry.js').read_text(encoding='utf-8')
    for index in range(0, len(rows), 10):
        rule(w, f'rb_scroll_registry_{index//10+1:02}', [], script=template.replace('__CATALOGUE__',js(rows[index:index+10])), recurring=True, phase='planning')
    w['worldLore']['Working Formulas and Fading Ink'] = {'text':'Teaching scrolls circulate through actual booksellers, workshops, teachers and field discoveries. Practical formulas serve kitchens, mills, gardens and repair benches. Advanced formulas ask for research and controlled tests; masterworks can occupy several sessions. Most use an ink that fades as a reader masters the working. A failed exercise leaves the diagrams usable, and someone who already knows a formula has no need to exhaust another copy. The reading begins by identifying which working is being studied. Research can compensate for limited familiarity, but it supplies no instant discipline mastery. Space remains dependent on a foundation in Gravity; Time has no public teaching catalogue.'}
    return rows


def create_cast(w):
    entries = [
        (VLAD,'male','Human',100,'Shadowspire','Shadowspire - Upper Study','A tall ageless human man with long charcoal-black hair loosely tied back, warm amber eyes, a tired handsome face and a narrow silver streak at one temple. He wears a deep plum traveling coat with irregular brass fastenings and an old ink-blue scarf.',
         'Vladimir lives beyond Shadowspire’s wandering paths. He receives few guests and has a talent for making a brief, mild question feel difficult to avoid. When conversation turns to his collections, his dignity becomes surprisingly fragile.',
         'A plain ash staff, a ring of mismatched brass keys, an old notebook and a bag of carefully sorted river pebbles.',
         'Protect his independence and find out what his former court is doing with his old work.',
         'He is immortal, a former Ardelis court mage and the author of the diagram now being misused. Psychic damage, telepathy, mind reading, mental compulsion and mind control cannot affect him. His immunity reveals nothing about other people. His power rivals a great Glowhaven founder; strangers do not know that. He follows actual intercepted correspondence and observations. He knows only the facts he has established. The player’s memories remain private until disclosed.',
         ['Fatherly and attentive during serious business; childish, indignant and absurdly proud in private.','Listens to the whole account, then asks one exact question.','Declines lessons, escorts, supplies and rescue requests. He never joins a traveling party, even at high trust.','Speaking Style: Quiet, economical and courteous in public; elaborate offended complaints about trivial hobbies in private.'],
         ['Arcane Geometry: Highly advanced mana constructs and prepared wards.','Folded Paths: Deliberate Space workings protect his own home.','Quiet Mind: Immune to psychic damage and mental intrusion.','Immortal: Does not age; his long life has left him astonishingly knowledgeable and very particular about his home.'], 'Arcane, Space, Enchantment'),
        ('Mihana Orihara','female','Human',17,'Brookmeadow','Brookmeadow - Mihana’s Cottage','An adult woman of thirty-seven with chestnut hair in a loose knot, dark green eyes, a broad expressive face and strong hands. She wears a faded coral work dress, blue waist apron and copper earrings.',
         'Mihana Orihara paints and repairs lamp shades for the village and nearby markets. She takes in neighbors during a bad night and becomes cross when they mistake that kindness for an endless invitation. Her kitchen table is usually half workshop.',
         'A shutter lantern, paintbrush roll, work knife and basket of unfinished lamp covers.',
         'Finish a commission and put her spare room back in order before market day.',
         'In the Rebirth opening she helped carry the rescued person from the shore with Kenta Matsuba. That rescue is not assumed in other beginnings. She knows where and when they were found and nothing about reincarnation unless told. She refuses to sell a guest’s private account. She overcommits to helping people and then resents being taken for granted.',
         ['Warm hands, blunt limits and an excellent memory for favors.','Counts paid work aloud while cooking and tells visitors to move a bowl rather than apologizing for the clutter.','Gets curt when someone volunteers her time without asking.','Speaking Style: Practical, dry and affectionate only when she means it.'],
         ['Lamplighter’s Touch: Modest Fire control for existing wicks.','Steady Paint: Experienced decorative handwork and careful repairs.'], 'Fire'),
        ('Reika Kurose','female','Human',29,"The Grand Sage's Court","The Grand Sage's Court - Administrative Wing",'An adult human woman of forty-three with cropped dark auburn hair, gray eyes, freckles and a slightly crooked nose. She wears a navy riding coat, a saffron neckcloth and unpolished practical boots.',
         'Reika Kurose investigates disputes involving visitors, hired labor and the movement of restricted goods. She prefers a witness who admits what they missed to a beautifully complete account. Outside work she repairs toy boats with stubbornly little success.',
         'A short sword, a sealed interview folio, a measuring cord and a chipped little wooden sailboat.',
         'Prove who is hiring dangerous intermediaries without turning every foreign visitor into a suspect.',
         'She initially knows nothing of the summoning. She can follow invoices, named witnesses and actual recovered components. A generic construct regulator does not identify a manufacturer or employer. She respects a refusal to disclose private memories and can pursue the relay independently of Vladimir.',
         ['Patient with frightened witnesses and sharp with officials who demand convenient conclusions.','Asks what someone saw before asking what they think it means.','Becomes terse when a colleague treats suspicion as proof.','Speaking Style: Plain questions, short summaries, occasional bleak jokes.'],
         ['Trace Comparison: Competent Divination and investigation of accessible residue.','Guarded Swordwork: Practical defense and an orderly withdrawal.'], 'Divination, Light'),
        ('Kazunari Shiba','male','Human',32,'','', 'An adult human man of fifty with black hair silvering at the sides, pale brown eyes and a scar through one eyebrow. His slate travel coat carries a restrained gold celestial clasp over ordinary mail.',
         'Kazunari Shiba is an experienced Ardelis delegation officer. He can be formal to the point of stiffness, but takes real care over the condition of his people’s equipment and remembers the names of stable hands.',
         'A service saber, a traveling ledger, a celestial seal and a patched pair of riding gloves.',
         'Complete a politically delicate inquiry and return with something his superiors can actually use.',
         'He is asking about a failed magical transit while presenting a real diplomatic visit. At first he has regional time and place clues, no target identity or face. He recognizes Vladimir from the former court. He will back away from an intrusive inquiry when confronted. His ledger does not contain a convenient confession of the whole program.',
         ['Disciplined, proud and uncomfortably aware that obedience does not remove responsibility.','Checks an order’s wording before accepting a subordinate’s interpretation.','Uses procedural language to avoid admitting a moral hesitation.','Speaking Style: Measured titles and clipped field instructions.'],
         ['Service Saber: Reliable martial training with limited Light support.','Field Ward: A modest practiced defensive working.'], 'Light, Enchantment'),
        ('The Ash-Cloaked Courier','unknown','Unconfirmed',22,'','', 'A human-sized figure in ash-gray travel cloth, with dark hair visible beneath a hood, amber eyes, an unusually pale face and hands covered by close-fitting gloves.',
         'An ash-cloaked traveler stands unusually still when nobody is speaking. Their boots are muddy but the cuffs carry no wear. Their voice is low and careful.',
         'A short hooked blade and a plain cloth satchel.',
         'Carry out a limited interception assignment.',
         'An advanced magitech proxy with only a local description, meeting route and capture instruction. It has no identifying maker’s marks, royal stamp, dispatch or reporting channel. It cannot reveal an employer it was never told. Genuine secured capture burns out its command regulator; threats, a failed grapple, ordinary unconsciousness and capture of the player do not. Its remains can establish construction but not Ardelis’s involvement.',
         ['Repeats one borrowed courtesy when improvisation fails.','Holds conversation only long enough to judge distance.','Falls back to the actual interception order rather than inventing a motive.','Speaking Style: Low, precise, with a pause in the wrong place.'],
         ['Hooked Guard: Close pressure and restraint attempts with real contested outcomes.','Regulator Burnout: Secured custody destroys the command regulator.'], 'Arcane'),
        ('The Reed-Cloaked Courier','unknown','Unconfirmed',21,'','', 'A lean human-sized figure with a moss-green cloak, black hair, clear gray eyes and long gloved hands. Their high collar hides most of the neck.',
         'A green-cloaked traveler moves with a measured, almost practiced casualness. Their hands keep returning to the same position at the waist.',
         'A weighted cord and a narrow defensive wand.',
         'Block an escape route during the assigned interception.',
         'A second proxy with the same narrow knowledge and absence of reporting channels as the ash-cloaked one. It knows its partner’s local instructions, not the royal program. Secured capture triggers its own regulator burnout. It remains a separate individual for damage, capture and remains.',
         ['Appears polite until interrupted, then becomes abruptly literal.','Watches a nearby exit rather than a speaker’s face.','Attempts its assigned restraint; allies can resist, flee or intervene.','Speaking Style: Unnaturally even.'],
         ['Cord Sweep: A single contested entangling attempt.','Regulator Burnout: Secured custody destroys this proxy’s own regulator.'], 'Arcane'),
        ('The Brass Usher','unknown','Construct',16, 'Shifting Gallery','Shifting Gallery - Return Lantern', 'A person-sized porcelain and brass attendant with a round cream faceplate, two green glass eyes and a tidy ocher coat painted with little blue swallows.',
         'The Brass Usher keeps Vladimir’s guests from losing the return lantern. It takes considerable pride in remembering a visitor’s preferred cup and no pride at all in its owner’s sense of direction.',
         'A copper lantern, a cloth polishing roll and a tray with one chipped cup.',
         'Keep the rooms usable while defending its own tiny collection of chipped crockery.',
         'It knows its household duties and what guests actually tell it. It has no automatic access to Vladimir’s mind or surveillance. It can disagree with him over household arrangements. Its fittings are workshop craft, not evidence that it made or knows the hired couriers.',
         ['Painstaking, hospitable and quietly judgmental about muddy boots.','Gives a useful direction before asking an irrelevant question about cups.','Calls attention to the marked return route and moves small hazards aside.','Speaking Style: Precise, warm and gently pedantic.'],
         ['Household Maintenance: Skilled care for its own household mechanisms.','Lantern Guide: Explains the marked walking routes without teleporting a guest.'], 'Enchantment')
    ]
    names = []
    for name, gender, species, level, location, area, appearance, public, equipment, motive, secret, personality, abilities, affinity in entries:
        kind = 'Magitech Proxy' if name == 'The Brass Usher' else 'Resident' if name in ['Mihana Orihara','The Ash-Cloaked Courier','The Reed-Cloaked Courier'] else 'Court Official' if name in ['Reika Kurose','Kazunari Shiba'] else 'Researcher'
        w['npcs'][name] = dict(name=name, properName=name, type=kind, currentLocation=location, currentArea=area, detailType='detailed', gender=gender, tier='strong' if level>=30 else 'average', level=level, healthMultiplier=1, successBonus=0, damageModifier=0, damageReductionModifier=0, initialKnown=False, initialRelationship=-75 if 'Courier' in name else 0, visualDescription=appearance,
             basicInfo=public+'\n\n'+appearance+'\n\nEquipment: '+equipment+f'\n\n- Gender: {gender}\n- Species: {species}\n- Magic affinity: {affinity}',
             hiddenInfo='Private motive: '+motive+'\n\nConcealment and knowledge: '+secret+'\n\nHow it surfaces: Observable behavior, real work and earned conversations reveal individual facts.', personality=personality, abilities=abilities)
        if name in ['Mihana Orihara','Reika Kurose']:
            w['npcs'][name]['faction'] = 'Glowhaven'
        if name == VLAD:
            w['npcs'][name]['immunities'] = ['psychic']
        ages = {VLAD:'Immortal; apparent age around forty', 'Mihana Orihara':'37', 'Reika Kurose':'43', 'Kazunari Shiba':'50'}
        if name in ages:
            w['npcs'][name]['basicInfo'] += '\n- Age: '+ages[name]
        pressures = {
            VLAD:'A guest takes his hospitality as a claim on his time or mocks a collection he cares about.',
            'Mihana Orihara':'A promised commission goes unpaid while another favor fills her worktable.',
            'Reika Kurose':'A witness is pressured to make a more convenient accusation.',
            'Kazunari Shiba':'A superior demands an answer that his actual evidence cannot support.',
            'The Brass Usher':'A careless repair would erase the personality of an old household object.'}
        if name in pressures:
            w['npcs'][name]['hiddenInfo'] += '\n\nPressure point: '+pressures[name]
        if name == 'Mihana Orihara':
            w['npcs'][name]['hiddenInfo'] += '\n\nRelationships: Kenta Matsuba helped with the shore rescue. She likes his music and distrusts his promises about punctuality. Haruho Taneda arranges some of her deliveries.'
        if name == 'Reika Kurose':
            w['npcs'][name]['hiddenInfo'] += '\n\nRelationships: She respects the Great Sage’s jurisdiction. She can disagree with Kazunari Shiba without treating his whole country as the enemy.'
        names.append(name)
    w['npcTypes']['Magitech Proxy'] = dict(name='Magitech Proxy', description='A fabricated autonomous body of fitted ceramic and brass. Its specific design determines its voice, senses, task, weaknesses and power. A construct knows only what it has been given or learned. A household attendant and a disguised interceptor can share materials without sharing purpose.', vulnerabilities=[], resistances=[], immunities=[])
    return names


def create_places(w):
    cottage = 'Brookmeadow - Mihana’s Cottage'
    w['locations']['Brookmeadow']['areas'][cottage] = dict(description='A small cottage off Mill Lane. Sand remains beneath the spare bed; a bowl and a rack of painted lamp covers crowd the kitchen table. A screen separates the sleeping space from paid work. Staying beyond a short recovery needs an actual agreement with Mihana.', paths=['Brookmeadow - Mill Lane'])
    w['locations']['Brookmeadow']['areas']['Brookmeadow - Mill Lane']['paths'].append(cottage)
    shadow = w['locations']['Shadowspire']
    shadow['basicInfo'] = 'A secluded tower rises beyond woodland paths that seem to lead a stranger back the way they came. A small outer clearing offers a safe view of its old brass-bound door. Invited guests can enter a lived-in stair hall, an upper study and the cellar below.'
    shadow['hiddenInfo'] = f'Vladimir, whose full name is {VLAD}, owns the tower. Ownership and the Ardelis history become known through actual contact. The exterior ward folds an uninvited approach back toward the clearing. An actual {KEY} quiets the ward for the permitted party; guests walk normally. The cellar alone contains the private portal. Losing a key leaves a way out and an opportunity to ask Vladimir for a replacement. The tower grants no automatic audience, lesson, treasure or party recruitment.'
    areas = shadow['areas']
    areas['Shadowspire - Outer Clearing']['description'] = 'A small clearing offers a view of the tower’s brass-bound door. A stone bench gives a visitor somewhere to wait. A guest’s key turns quietly toward the threshold; an uninvited walker finds the path bending back toward the trees.'
    areas['Shadowspire - Outer Clearing']['paths'].append('Shadowspire - Threshold Hall')
    for name, description, paths in [
        ('Threshold Hall','A brass ward ring crosses the stone threshold. Cloak pegs, a guest bench and a chipped umbrella stand sit below a curved stair. The open exterior door remains the ordinary way out.',['Shadowspire - Outer Clearing','Shadowspire - Upper Study','Shadowspire - Cellar Gate']),
        ('Upper Study','Round windows overlook the woods. A brass observation instrument stands beside tea, maps and letters under paperweights. Vladimir chooses which private papers a guest may see.',['Shadowspire - Threshold Hall']),
        ('Cellar Gate','Below the stair, a hinged brass doorway holds a bright impossible landscape. A copper lantern marks this exact endpoint. Crossing is voluntary; the return from the far lantern leads here.',['Shadowspire - Threshold Hall'])]:
        areas['Shadowspire - '+name] = dict(description=description, paths=paths)
    w['realms'][POCKET] = dict(name=POCKET, initialKnown=False, basicInfo='Vladimir’s private collection of impossible rooms and living gardens. Moving arcades connect stable destinations. Brass lanterns mark the walking route to the arrival gallery and its one fixed gate back to Shadowspire’s cellar.')
    w['regions'][REGION] = dict(name=REGION, realm=POCKET, x=0, y=0, initialKnown=False, npcLevelRange=dict(min=10,max=30), basicInfo='A compact circuit of gardens, workshops and peculiar recreation rooms. Corridors shift around dependable room thresholds, marked stairs and copper lanterns. The household keeps return routes clear.')
    places = [
        ('Shifting Gallery','Repeated cream arches ride on exposed tracks. A brass return lantern marks the arrival threshold; the private gate opens only to Shadowspire’s Cellar Gate. A sliding passage changes its view while named destinations keep their marked routes.', ['Return Lantern','Sliding Junction','Balcony of Doors']),
        ('Glassroot Gardens','Transparent roots frame lilac light above small pools, antlered hares and little rays swimming through air. Clipped paths protect the animals and leave room for quiet visitors.', ['Garden Gate','Root Walk','Stillwater Pools']),
        ('Inverted Court','Water rises into an overhead basin. Steps climb onto a wall while handrails and marked footing show where a person can actually walk. Curious guests can test one safe surface at a time.', ['Safe Landing','Wall Stair','Uphill Fountain']),
        ('Porcelain Workshops','Copper lamps illuminate fitted ceramic frames, repair benches and labeled trays of hands. Some projects work; others wait beside Vladimir’s abandoned notes.', ['Service Door','Repair Benches','Frame Alcoves']),
        ('The Little Kingdom','A clockwork valley fills a vast table. Tiny carriages halt at miniature bridges and painted villages. Games and repairs can occupy an afternoon without becoming a royal duty.', ['Model Valley','Games Table','Kite Balcony']),
        ('Tilt Court','An airy ringball court tilts between padded landings and brass hoops. Practice constructs wait for agreement on a game. No championship, reward or compulsory contest is assumed.', ['Players’ Bench','Tilting Floor','Hoop Gallery']),
        ('The Rainward Orchard','Rain travels sideways across one orchard row and falls normally in the next. Covered benches, a potting shed and walking rails make the experiment hospitable. Real fruit belongs to its grower.', ['Covered Bench','Crossrain Rows','Potting Shed']),
        ('The Cabinet of Evenings','Different windows hold different skies. Chairs, records of old observations and a narrow viewing balcony invite a guest to linger. The scenes show the instrument’s work, not perfect knowledge of every place.', ['Window Hall','Tea Nook','Viewing Balcony'])]
    for index,(name,description,labels) in enumerate(places):
        area_keys = [f'{name} - {label}' for label in labels]
        a = {key:dict(description=f'{label}. '+description, paths=[other for other in area_keys if other!=key]) for label,key in zip(labels,area_keys)}
        w['locations'][name] = dict(name=name, basicInfo=description, hiddenInfo='Copper lantern signs mark the walk back to Shifting Gallery. Moving corridors change scenery and optional shortcuts; they never remove the exit, relocate belongings, change known addresses or settle a quest. This is Vladimir’s home; ask before taking or altering property.', region=REGION, x=(index%4)*18-27, y=(index//4)*26-13, radius=2, initialKnown=False, complexityType='complex', detailType='detailed', npcLevelRange=dict(min=10,max=30), areas=a)
    for name,_,_ in places[1:]:
        gate = next(iter(w['locations'][name]['areas'].values()))
        gate['description'] += ' A copper-lantern passage provides the ordinary walking route back to Shifting Gallery.'
    # A small investigation site is an area, preserving the existing pin and map.
    w['locations']['Pinewater River']['areas']['Pinewater River - Disused Pump House'] = dict(description='A disused stone pump house stands above a short culvert. Its original gear is rusted. Recently handled packing straw, an unusually clean mounting plate and a replaced padlock suggest new occupants. The river paths remain available to anyone who chooses to leave.', paths=['Pinewater River - Brookmeadow Ford'])
    w['locations']['Pinewater River']['areas']['Pinewater River - Brookmeadow Ford']['paths'].append('Pinewater River - Disused Pump House')
    return [name for name,_,_ in places]


def create_story(w):
    w['traits']['Summoned one'] = trait('Summoned one', 'You woke in another body with the memories of your previous life intact. So far, you alone know what happened to you.')
    w['traits']['Summoned one']['requirements'] = [dict(type='characterLevel',amount=151)]
    w['traits']['Summoned one']['traitNarrativeEffects'] = 'Private origin. Preserve the player’s actual past-life memories and chosen present body. NPCs know only what they observe or learn. The origin itself grants no publicly known identity, automatic mastery or allegiance.'
    w['traits']['Traced Shore Record'] = trait('Traced Shore Record','A real shore report has connected your rescued identity and whereabouts to the people asking questions. It says nothing by itself about your memories or where you came from.')
    w['traits']['Traced Shore Record']['requirements'] = [dict(type='characterLevel',amount=151)]
    w['itemTypes'][KEY] = dict(name=KEY, category='Tool', description='A small brass key whose tooth turns gently toward Shadowspire’s door. Vladimir gave it as permission to visit his home. The copper lantern below his stairs marks the gate back from his private rooms.', bonuses=[])
    w['itemTypes']['Relay Dispatch Copy'] = dict(name='Relay Dispatch Copy', category='Document', description='A copy of the pump-house dispatch and its corroborating delivery record. The dates and recipient connect the hidden apparatus to an Ardelis field office. A final entry reserves a second receiving station beyond Glowhaven.', bonuses=[])
    start = dict(name=START, description='Begin in Brookmeadow, in the Glowhaven countryside. You wake in an unfamiliar body with your old memories intact. The people who carried you from the shore have offered a bed and a bowl of broth. What you tell them is up to you.',
        storyStart='[Use Mihana Orihara and Kenta Matsuba at Brookmeadow - Mihana’s Cottage. The player is the person found unconscious on the nearby shore. Preserve the selected ancestry, anatomy and appearance, their old memories and their right to define the old life. Neither rescuer knows about reincarnation. The public world knows no summoned hero. End before the player answers, acts or agrees to work. The opening does not begin the Ardelis inquiry.]\n\nYou wake up in a body that isn’t yours.\n\nThe face in the washbasin is unfamiliar. Your last life is still there, clear enough to remember the small things. A different ceiling hangs above the bed. Outside the window, a cart wheel bumps over a stone and somebody tells its driver to slow down.\n\nA woman takes a bowl from the stove. There is sand beneath the chair beside you. Painted lamp covers hang above a table crowded with brushes.\n\n“We found you on the shore,” she says. “Kenta ran for me. You’ve been here since dawn.”\n\nAt the open door, a young man with a turquoise shirt and muddy boots shifts a basket against his hip.\n\n“I’ll tell Haruho I’ll be late,” he says. Then, to her, “Actually late. I mean it this time.”\n\n“Might make a useful change.”\n\nHe gives a small, chastened grin and waits by the door. The woman brings the broth within reach. Her hands smell faintly of lamp oil and orange peel.\n\n“Mihana,” she says, touching her own chest. “This is Brookmeadow. When you feel up to it, tell me what to call you.”',
        locations=['Brookmeadow'], locationAreas=['Brookmeadow - Mihana’s Cottage'], startingQuests=[], startingItems=[dict(item='Mark',quantity=1000)], startingPartyNPCs=[], isDefault=False,
        questGenerationGuidance='Let ordinary life establish itself. Mihana has paid craftwork and limits; Kenta has his own obligations. Work in the village and the city guild are optional directions. Existing registration and contract rules apply. Respect the player’s silence or disclosure about their memories and retain their actual relationships across travel. Later chapters follow their own eligibility and evidence.')
    w['storyStarts'] = {START:start, **w['storyStarts']}
    base = [condition('story-start',START), condition('game-tick',0)]
    rule(w,'rb_origin',base,[effect('player-traits','Summoned one','add',target='satisfyingPlayers'),effect('write-boolean',True,key='rbCampaign'),effect('write-number',0,key='rbPhase'),effect('write-number',0,key='rbOriginTick')],scope='player')
    rule(w,'rb_clock',[condition('read-boolean',True,key='rbCampaign')],script=(HERE/'clock.js').read_text(encoding='utf-8'),recurring=True)
    towns = condition('read-boolean',True,key='rbTownReady')
    phase = lambda number:condition('read-number',number,key='rbPhase')
    place = lambda npc, location, area:dict(type='npc-placement',npc=npc,operation='moveTo',location=location,area=area)
    intro = 'The Sage’s Visitors'
    ledger = 'A Name in the Shore Ledger'
    inquiry = 'The Carrier behind the Ledger'
    relay = 'The Pump House That Hummed'
    close = 'A Second Receiving Station'
    audience = 'At the Wandering Door'
    foothold = 'Rumor: A Living to Be Made'
    quest(w,foothold,'Mihana Orihara','Brookmeadow','Mihana says the mill yard sometimes needs hands. There is also an Adventurer’s Guild in the city, if that kind of work appeals. Other ways of making a life are worth asking about.','Find one real local opportunity or establish a practical place in the wider world.',
          'The participant actually learns the terms of a workable opportunity, agrees a real lodging arrangement, begins paid work or establishes a recurring local contact with an achievable next step. Hearing a name alone is insufficient; taking any particular job or joining the guild is unnecessary.',
          'This journal suggestion is optional. Mihana can give directions to Haruho’s real mill work or the actual Glowhaven guild. Registration and licensure remain separate. No automatic accepted contract, assigned profession, property, badge or portal key. Work, study, lodging and relationships can each provide a foothold.',
          [effect('player-experience',60,'add',target='allPlayers')])
    w['storyStarts'][START]['startingQuests']=[foothold]
    # Native quests own their results. Event scripts only stage interruptions.
    quest(w,intro,'Kazunari Shiba','Brookmeadow','An Ardelis delegation says it has business with the Great Sage. Its questions have reached the village shore records.','Learn what the visitors are asking and decide how to respond.',
          'The participant actually hears the delegation’s inquiry, obtains a credible witnessed account or examines an authentic inquiry record, understands that the visitors sought shore traffic records and has made a real response, including a considered refusal. Guessing a secret summoning motive is insufficient.',
          'A diplomatic visit is real. Initially the delegation has no name or face for the missing subject. Its questions concern a date and broad coastal area. Keep Mihana and Kenta’s lives and limits. The player may observe, refuse, question or leave. An ordinary witness cannot disclose memories they never heard. Vladimir’s intervention is his own response to an intrusive inquiry.',
          [dict(type='quest-init',operator='set',value=ledger)])
    quest(w,ledger,'Reika Kurose','Brookmeadow','A copied shore entry may have passed beyond the village. Reika wants to establish who handled it before making an accusation.','Trace the copied entry and decide what to protect or disclose.',
          'The participant actually establishes a real step in the copied shore record’s custody through an examined record or a credible witness, and makes an informed choice about what to disclose or protect. A genuine effort that proves the lead false qualifies. Merely assuming the visitors know the player’s identity does not.',
          'Use Haruho’s real work and Reika’s investigation. A shore entry can identify the rescued person but does not prove reincarnation. Preserve a destroyed copy, protected witness or false lead as an actual outcome. Completion does not establish that the enemy received the information. The separate lead condition requires that actual disclosure.',
          [dict(type='quest-init',operator='set',value=inquiry)])
    quest(w,inquiry,'Reika Kurose',"The Grand Sage's Court",'Someone has been paying a local carrier to move unusual components. Reika can follow the work through witnesses and deliveries. Vladimir may have his own observations.','Establish a credible link between the carrier, the visiting delegation and the abandoned pump house.',
          'The participant obtains and checks independent evidence linking an actual intermediary to the Ardelis delegation and the Pinewater pump house. A witnessed meeting with corroboration, authenticated dispatch or checked delivery chain can qualify. Construct parts alone, an untested accusation or a secret never learned cannot.',
          'This route works after a fought ambush, an escape or no attack. The constructs know no employer and have no royal stamp or reporting channel. Reika provides an independent investigation if the player declines Vladimir. A voluntary Shadowspire visit can supply observations from Vladimir’s actual surveillance. Accepting an invitation, surrendering memories and recruiting him are never prerequisites.',
          [effect('write-number',6,key='rbPhase'),dict(type='quest-init',operator='set',value=relay),dict(type='quest-init',operator='set',value=audience)])
    quest(w,audience,'Reika Kurose','Shadowspire','Reika can pass a request for an audience to the reclusive wizard. His outer clearing offers a place to wait for an agreed visit.','Attend the agreed audience at Shadowspire’s outer clearing, or decline the invitation.',
          'The participant actually attends the arranged meeting with Vladimir at Shadowspire’s outer clearing and has an opportunity to ask about the old diagram, or explicitly declines this optional audience after understanding its terms. Merely traveling toward the tower is insufficient.',
          'An accepted request allows Vladimir to choose this meeting on his own terms. A decline completes this optional undertaking and leaves Reika’s relay investigation available. At the clearing he can discuss observations and offer guest access; the player must actually accept the key handover for its native grant. He gives no automatic training, rescue or party membership.')
    quest(w,relay,'Reika Kurose','Pinewater River','The disused pump house has received parts that do not belong to its old machinery. A delivery chain has made it worth investigating.','Investigate the field relay and stop its local use or secure enough evidence for lawful intervention.',
          'The participant actually investigates the Pinewater River - Disused Pump House, secures corroborated dispatch evidence, and either disables the local relay safely or carries out a real handover that brings an authorized response. Observation from outside, an unverified threat or merely accepting the job is insufficient.',
          'Offer reconnaissance, bargaining with a carrier, covert entry, technical work or contacting lawful help. No particular discipline is mandatory. The apparatus is a local relay and field-test component; it cannot mass-summon heroes. Its attendants can withdraw or surrender. Keep civilians out of a forced boss fight. Record what is actually disabled or secured. The native result gives the one evidence copy and next undertaking.',
          [dict(type='item-add',item='Relay Dispatch Copy',quantity=1,target='allPlayers'),dict(type='quest-init',operator='set',value=close)],reward=160)
    quest(w,close,'Reika Kurose',"The Grand Sage's Court",'The relay records name a second receiving station inside Ardelis. Glowhaven can act on the local intrusion, but the next questions lie beyond its jurisdiction.','Bring the checked relay findings to the court or another credible informed authority and establish the next lead.',
          'The participant actually presents the checked relay findings to Reika or the Great Sage’s informed representative, with the evidence or a credible authenticated alternative, and learns that the second receiving station and next summoning preparations are in Ardelis. Owning a copy without a conversation is insufficient.',
          'Conclude the Glowhaven investigation and preserve its actual local consequences. The remaining lead points to future travel in Ardelis. Do not invent an already accessible Ardelis realm, launch the controlled rival’s attack, claim that the foreign program has ended or leave this undertaking perpetually incomplete. The player can continue ordinary play while preparations beyond the border remain unresolved.',
          [effect('write-number',7,key='rbPhase'),effect('write-boolean',True,key='rbLocalConclusion')])
    rule(w,'rb_delegation',[towns,phase(0),condition('player-traits','Summoned one','contains'),dict(type='story',query='This is a calm town scene after the player has established ordinary work, lodging, study or a recurring local relationship. The party is available for a brief public interruption, not in combat, flight, an expedition, a class assessment, a championship bout or urgent rescue. A high level alone is insufficient.')],
         [effect('write-number',1,key='rbPhase'),dict(type='npc-placement',npc='Kazunari Shiba',operation='moveHere'),dict(type='quest-init',operator='set',value=intro),tell('Kazunari Shiba’s small visiting delegation has genuine business with the Great Sage. Let locals notice its questions about shore records. They have a broad time and place, no identified summoned person. Place the exchange within the actual town and leave the player free to respond or ignore it. Introduce no abduction or revelation now.')],scope='player')
    rule(w,'rb_intervention',[phase(1),condition('npc-in-scene',True,npc='Kazunari Shiba'),condition('npc-health',0,'greaterThan',npc='Kazunari Shiba'),dict(type='story',query='Kazunari Shiba’s delegation has actually begun intrusive questioning of locals in a calm Glowhaven town scene. A brief public intervention can occur without overriding a player action, fight or urgent task.')],
         [effect('write-number',2,key='rbPhase'),dict(type='npc-placement',npc=VLAD,operation='moveHere'),tell('Vladimir interrupts on his own business. Shiba recognizes the former court mage and backs off. Vladimir asks why business with the Great Sage requires this questioning. He gives the rescued traveler an ambiguous look, bids them farewell and leaves the conversation. He offers no diagnosis, lesson or invitation here. Let the actual player response stand.')],script="storage.rbInterventionTick=Number(check({type:'game-tick'}))||0;")
    rule(w,'rb_visitors_depart',[phase(2),condition('game-tick',201,'greaterThanOrEqual')],
         [effect('write-number',3,key='rbPhase'),dict(type='npc-placement',npc='Kazunari Shiba',operation='moveAway'),place(VLAD,'Shadowspire','Shadowspire - Upper Study')],script="if(Number(check({type:'game-tick'}))<Number(storage.rbInterventionTick||0)+2)skip=true;",recurring=True)
    rule(w,'rb_delegation_casualty',[phase(1),condition('npc-health',0,'lessThanOrEqual',npc='Kazunari Shiba')],
         [effect('write-number',3,key='rbPhase'),tell('Preserve the delegation officer’s actual fate. Reika can investigate the visiting delegation’s records through witnesses and authentic papers. No living interview or encounter with that officer is invented. Existing crime and custody rules still apply.')])
    rule(w,'rb_personal_lead',[phase(3),condition('read-boolean',False,key='rbLead'),condition('player-traits','Summoned one','contains'),dict(type='story',query='A real human witness or copied shore record has actually given the intermediary a credible identity and whereabouts for this Summoned one. The connection has been corroborated in this playthrough. A private confession to a trusted person, a false report, a protected witness, an unreceived message or a guess does not qualify.')],
         [effect('write-boolean',True,key='rbLead'),effect('player-traits','Traced Shore Record','add',target='satisfyingPlayers')],script="storage.rbLeadTick=Number(check({type:'game-tick'}))||0;",scope='player')
    rule(w,'rb_interception',[phase(3),condition('read-boolean',True,key='rbAmbushReady'),condition('player-traits','Traced Shore Record','contains'),condition('player-level',15,'greaterThanOrEqual'),dict(type='story',query='The identified Summoned one is personally present at the party’s current rural approach and a short interception can begin now. No fight, expedition hazard, championship, compulsory lesson or urgent rescue is underway. The credible lead still describes this person. Ordinary companions can be present; an unrelated player is not substituted as the target.')],
         [effect('write-number',4,key='rbPhase'),dict(type='npc-placement',npc='The Ash-Cloaked Courier',operation='moveHere'),dict(type='npc-placement',npc='The Reed-Cloaked Courier',operation='moveHere'),tell('Two cloaked travelers intercept the identified person. Give a readable warning, real space to resist or escape, and the companions’ freedom to act. Resolve their actual contested capture attempts. They are disguised proxies with limited instructions and no reporting channel. Their hidden employer is not a public introduction. Do not award victory or capture in the scene setup.')],scope='player')
    for index,npc in enumerate(['The Ash-Cloaked Courier','The Reed-Cloaked Courier'],1):
        rule(w,f'rb_captive_shutdown_{index}',[phase(4),condition('npc-in-scene',True,npc=npc),condition('npc-health',0,'greaterThan',npc=npc),dict(type='story',query=f'{npc} has actually been secured alive in effective custody in the interception. They cannot simply resume the fight or flee. A threat, offered surrender, failed grapple, momentary restraint, ordinary knockout or capture of a player is false.')],
             [effect('npc-health',0,npc=npc),tell(f'The secured {npc} goes inert as its command regulator burns out. Preserve the shell for inspection. It has no message, royal stamp, identifying maker’s mark or knowledge of the employer.')])
    rule(w,'rb_interception_aftermath',[phase(4),dict(type='story',query='The cloaked interception has actually ended through defeat, flight, effective escape, a negotiated release or other resolved outcome. No active attack remains in the party’s current scene. Preserve injuries, actual captivity and each participant’s outcome. Merely declaring victory while the attack continues is false.')],
         [effect('write-number',5,key='rbPhase'),dict(type='quest-init',operator='set',value=inquiry),dict(type='quest-init',operator='set',value=audience)],
         script="""if(storage.rbAftermathRoll===undefined)storage.rbAftermathRoll=Math.random();
const near=['Shadowspire','Brookmeadow','Pinewater River'].includes(String(check({type:'party-location'})||''));
const alive=check({type:'npc-health',npc:"Valkazathoth'dmir"});
if(storage.rbAftermathRoll<0.333333&&near&&typeof alive==='number'&&alive>0){
 effects.push({type:'npc-placement',npc:"Valkazathoth'dmir",operation:'moveHere'});
 effects.push({type:'story',instruction:'After the party has resolved its own danger, Vladimir arrives on his own investigation of these roads. He can offer a visit to Shadowspire. He does not undo wounds, free a captive by decree, recruit himself or explain the conspiracy here. The invitation is voluntary.'});
}else effects.push({type:'story',instruction:'A route remains through Reika Kurose’s actual investigation of deliveries and witnesses. She can arrange a request to speak to Vladimir; declining it leaves her independent evidence route open. An escaped attack creates no recovered corpse or automatic component.'});""")
    rule(w,'rb_guest_key',[condition('npc-in-scene',True,npc=VLAD),condition('player-item',0,item=KEY),dict(type='action',query='Vladimir has actually approved this player and any accompanying guests for a visit, and the player accepts his genuine handover of a Shadowspire Guest Key or authorized replacement. Asking about a key, stealing a similar key or merely knowing his name is insufficient.')],
         [dict(type='item-add',item=KEY,quantity=1,target='satisfyingPlayers'),dict(type='known-entity',entity='Shadowspire',operator='set',value=True),tell('Vladimir hands over the brass guest key. It permits the agreed visit and ordinary walking access to his home. The player chooses when to go. He remains independent and offers no automatic training or party membership.')],recurring=True,scope='player')
    rule(w,'rb_arranged_audience',[condition('quest-status','accepted',questId=audience),condition('party-area','Shadowspire - Outer Clearing'),condition('read-boolean',False,key='rbAudiencePlaced')],
         [effect('write-boolean',True,key='rbAudiencePlaced'),place(VLAD,'Shadowspire','Shadowspire - Outer Clearing'),tell('Vladimir comes to the agreed meeting in his own clearing. He can explain what his actual observations establish and listen to questions. The player chooses what to disclose and whether to accept a guest key. The independent court investigation remains available.')],script=f"const health=check({{type:'npc-health',npc:{js(VLAD)}}});if(typeof health==='number'&&health<=0)skip=true;")
    rule(w,'rb_vladimir_independent',[condition('npc-in-party',True,npc=VLAD)],
         [effect('npc-in-party',False,npc=VLAD),tell('Vladimir declines to travel with the party and returns to his own business. Friendship and permission to visit his home still stand.')],recurring=True)
    endpoints = ['Shadowspire - Cellar Gate','Shifting Gallery - Return Lantern']
    rule(w,'rb_private_gate',[condition('party-area','^(Shadowspire - Cellar Gate|Shifting Gallery - Return Lantern)$','regex'),dict(type='action',query='The player deliberately crosses the private brass portal at this actual endpoint. This is a committed transit, not a question, a glance, a remembered journey or a request to use some other portal. For entry from the cellar Vladimir has authorized the travelers and their party carries his real guest key. Returning from the gallery is always available, including after losing that key.')],
         script=f"""const inward=String(check({{type:'party-area'}})||'')==={js(endpoints[0])};
if(inward&&!check({{type:'player-item',item:{js(KEY)},operator:'greaterThan',value:0}})){{skip=true;}}
else{{
 const destination=inward?[{js(POCKET)},{js(REGION)},'Shifting Gallery','Shifting Gallery - Return Lantern']:['Glowhaven','Greenfield Farmlands','Shadowspire','Shadowspire - Cellar Gate'];
 ['party-realm','party-region','party-location','party-area'].forEach((type,i)=>effects.push({{type,operator:'set',value:destination[i]}}));
 storage.rbPocketEntered=true;
 effects.push({{type:'story',instruction:inward?'Cross into the Shifting Gallery at its brass return lantern. Its one gate leads back to the same Shadowspire cellar. The player chooses a marked onward route.':'Return to the copper lantern in Shadowspire’s cellar. The stairs and exterior exit are available. Do not divert this private return to the Evertree.'}});
}}""",recurring=True)
    rule(w,'rb_tower_ward',[condition('party-location','Shadowspire'),condition('party-area','^Shadowspire - (Threshold Hall|Upper Study|Cellar Gate)$','regex')],
         [effect('party-area','Shadowspire - Outer Clearing'),tell('The unquiet threshold path leads back to the safe outer clearing. The ordinary road remains open; an actual guest key quiets this ward.')],script=f"if(check({{type:'player-item',item:{js(KEY)},operator:'greaterThan',value:0}}))skip=true;",recurring=True,phase='planning')
    rule(w,'rb_private_entry_guard',[condition('party-realm',POCKET),condition('read-boolean',False,key='rbPocketEntered')],
         [effect('party-realm','Glowhaven'),effect('party-region','Greenfield Farmlands'),effect('party-location','Shadowspire'),effect('party-area','Shadowspire - Outer Clearing'),tell('The unentered private threshold resolves at Shadowspire’s safe outer clearing. Its actual entrance is the authorized cellar gate.')],recurring=True,phase='planning')
    destinations=['Shifting Gallery','Glassroot Gardens','Inverted Court','Porcelain Workshops','The Little Kingdom','Tilt Court','The Rainward Orchard','The Cabinet of Evenings']
    rule(w,'rb_pocket_orientation',[condition('party-realm',POCKET),condition('read-boolean',True,key='rbPocketEntered')],
         [*[dict(type='known-entity',entity=name,operator='set',value=True) for name in [REGION,*destinations]],tell('Copper-lantern signs identify the household destinations and the ordinary walk back to Shifting Gallery. Its marked arrival lantern is the one gate to Shadowspire’s cellar. The party chooses where to explore.')])
    # The approved narrow eligibility optimization leaves the Spider trigger intact.
    w['triggerDefinitions']['gh_exam_volunteer']['conditions'].insert(0,condition('player-level',20,'greaterThanOrEqual'))
    chapter_names = [intro,ledger,inquiry,relay,close,audience]
    for name,xp in zip(chapter_names,[80,100,180,300,120,0]):
        chapter=w['parties']['']['quests'][name]
        chapter['status']='planned'
        chapter['questDesignBrief']='Rebirth chapter. Its configured event or predecessor offers this undertaking; contact with the source alone is not permission to jump ahead. '+chapter['questDesignBrief']
        if xp:
            chapter['onCompleteEffects'].append(effect('player-experience',xp,'add',target='allPlayers'))
    return [foothold,*chapter_names]


def create_lore_and_tone(w):
    entries = {
        'Ardelis — Delegations and Jurisdiction':'Ardelis and Glowhaven retain diplomatic and commercial ties despite their political separation. A delegation can seek an audience, buy provisions and ask voluntary questions. It has no automatic authority to requisition homes, arrest Glowhaven residents or command the city guard. Local officials can refuse demands while keeping ordinary visitors safe.',
        'Ardelis — Provinces and Ordinary Life':'The kingdom’s provinces supply grain, livestock, timber, ports and workshop labor. Their interests do not always match the court’s war policy. Temple service, provincial loyalties, family work and travel shape ordinary lives. An officer, artisan or worshipper has individual motives; nationality is no proof of complicity in a royal project.',
        'Summoning — Familiar Bonds and Dangerous Invocations':'Familiar summoning is an established discipline with specific bonds and limits. Invoking a person across realities is an exceptional operation requiring prepared diagrams and infrastructure. A recovered diagram is evidence and an object of research, not an ordinary teachable spell. Divination observes uncertain traces; it does not identify every displaced person or read their memories.',
        'Private Pocket Realms and Returning Thresholds':'Some powerful workings maintain enclosed spaces larger or stranger than their exterior. Each has its own stable entrance and constraints. A private gate belongs to its particular endpoints and permissions. Familiarity with a room, a painting or a map does not make it a surveyed Space destination. Moving interior passages can coexist with marked, dependable return routes.',
        'Magitech — Makers, Repairs and Attribution':'Ceramic shells, brass joints and common regulators circulate through workshops and salvage. A component can reveal how a machine works without naming its owner. Attribution needs a real maker’s mark, checked record, witness or distinctive verified method. An attendant’s household craft does not establish responsibility for a similar weapon.',
        'Shadowspire — A House beyond Wandering Paths':'Travelers speak of a woodland tower whose paths return them to familiar trees. Its outer clearing offers a place to wait. Visitors admitted by the owner describe a curved stair, too many keys and an astonishing concern for small household arrangements. Accounts of the interior disagree; ordinary residents have no reason to know its owner’s entire history.'}
    for name,text in entries.items():
        w['worldLore'][name] = dict(text=text)
    w['narratorStyle'] = w['narratorStyle'].replace('Narrate a vivid fantasy-anime ensemble adventure','Narrate a grounded fantasy ensemble adventure').replace('Show an inviting world through','Make the world concrete through')
    w['narratorStyle'] += '\nLet people have work, loyalties and obligations that predate the player. Kindness appears in what someone does or gives up. Danger has practical consequences. Ordinary warmth, silence and earned humor belong beside serious decisions; the current scene and selected mode determine the register.'
    initial = w['aiInstructions']['generateInitialStart']
    initial['Style Principles'] = initial['Style Principles'].replace('specific inviting fantasy-anime opening','specific opening grounded in its people and place')
    w['aiInstructions']['generateStory']['Relevance and Source Scope'] = 'Use current geography, outcomes and character knowledge. Private origins and motives require actual disclosure or evidence. Keep flags and reward recipes out of speech. An active quest owns its scope. New features do not dominate unrelated scenes. Ordinary lives and quiet moments stand on their own.'
    w['aiInstructions']['generateNewNPC']['Beastfae Anatomy'] = 'Beastfae are rare upright people with full animal faces and coherent body covering. Preserve their selected form, clothing fit and actual adult stature. Do not simplify them to human faces with animal ears. Beastfolk remain generally human-faced; Fae remain individually varied.'
    # Keep the already tight global quest-generation field exact.


def create_household_play(w):
    descriptions = {
        'Glassroot Hare':'A small antlered rabbit with pale brown fur, dark eyes and translucent green horn tips. It browses around Glassroot Gardens and bolts from rough handling. Its curiosity is a household animal’s behavior, not permission to take it.',
        'Driftglass Ray':'A small ray-shaped garden animal with translucent blue fins and a pale spotted belly. It drifts through humid air near the pools, settling to drink. Sudden noise sends it beneath the roots.',
        'Counterweight Practice Frame':'A padded brass practice construct with a rounded wooden shield and clearly visible joints. In Tilt Court it follows the agreed game or sparring rules. An inactive frame does not attack a passing visitor.',
        'Relay Watch Frame':'A compact ceramic guard machine with a broad flat head, copper eyes and a grounding spike. One prepared controller gives it a limited patrol. Its location, level and actual order determine danger; merely finding an old frame does not activate it.'}
    for name,description in descriptions.items():
        w['npcTypes'][name] = dict(name=name, description=description, vulnerabilities=[], resistances=[], immunities=[])
    # Ordinary optional undertakings have native completion and a local offer.
    jobs = [
        ('A Carriage Late for Tea','The Little Kingdom','The little model carriage has stopped beneath a painted bridge. The Brass Usher would like the tea delivery running again before Vladimir notices.',
         'Find the jam and restore a safe run for the little model carriage.',
         'The player actually identifies the model carriage’s obstruction and restores one safe supervised run, using a feasible repair, careful cleaning or appropriate practical magic. Promising a repair or replacing the whole model by narration is insufficient.',
         'The fault is a thread caught around a wheel, which has also loosened the stop pin. A careful nonmage can repair it. A magical fix must still address the actual thread and pin. Let curiosity about the model and the Usher’s exacting pride carry the scene. Vladimir’s tiny tea delivery is an optional household problem.',
         'Teaching Scroll: The Clockmaker\'s Testing Spark'),
        ('Rain on the Wrong Roots','The Rainward Orchard','A reversed rain rail is flooding the young pots. The Brass Usher has moved the dry labels, but would welcome a second pair of hands.',
         'Correct the rain rail or safely move the young plants and agree on a lasting practical fix.',
         'The player actually corrects the displaced rain rail or moves the affected pots to suitable shelter and makes a practical lasting arrangement with the Brass Usher. Harming the plants, merely stopping the rain briefly or promising to help is insufficient.',
         'A loose ceramic collar has turned the rail. Observe the runoff, ask before changing Vladimir’s experiment, and let lifting, repair, Nature or other appropriate methods work. The plants are ordinary household property. The odd weather belongs to this experiment and does not change the global weather system.',
         'Teaching Scroll: The Gardener\'s Returning Tendril')]
    for name,location,statement,objective,query,brief,scroll in jobs:
        quest(w,name,'The Brass Usher',location,statement,objective,query,brief,[dict(type='item-add',item=scroll,quantity=1,target='allPlayers')])
    for index,(name,location,*_) in enumerate(jobs,1):
        rule(w,f'rb_household_offer_{index}',[condition('party-realm',POCKET),condition('npc-in-scene',True,npc='The Brass Usher'),condition('quest-status','hidden',questId=name),dict(type='action',query=f'The Brass Usher has actually explained {name}, concerning the problem at {location}, and the player agrees to help with that particular work. A question about the place, a hypothetical offer, someone else’s work or agreement to a different request is false.')],
             [dict(type='quest-init',operator='set',value=name)])
    # Follow the attendant between adjacent household rooms only when invited.
    # Conversation and play remain normal narration rather than more controllers.
    return [row[0] for row in jobs]


def changes(before, after, path=()):
    if isinstance(before,dict) and isinstance(after,dict):
        out=[]
        for key in before.keys() | after.keys():
            if key not in before:out.append(dict(path=[*path,key],kind='added',afterHash=digest(after[key])))
            elif key not in after:out.append(dict(path=[*path,key],kind='removed',before=before[key]))
            else:out.extend(changes(before[key],after[key],(*path,key)))
        return out
    if before!=after:
        return [dict(path=list(path),kind='modified',before=before,afterHash=digest(after))]
    return []


def build(base):
    w=copy.deepcopy(base)
    forms=create_ancestry(w)
    scrolls=create_scrolls(w)
    places=create_places(w)
    npcs=create_cast(w)
    quests=create_story(w)
    quests+=create_household_play(w)
    create_lore_and_tone(w)
    portraits=HERE/'hosted-portraits.json'
    if portraits.exists():
        for name,record in project.load(portraits).items():
            if name not in npcs:
                raise ValueError('Portrait outside the new Rebirth cast: '+name)
            w['npcs'][name]['portraitUrl']=record['url']
    project.validate(w)
    return w,dict(forms=forms,scrolls=scrolls,npcs=npcs,locations=places,quests=quests)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',type=pathlib.Path,default=project.WORLD)
    parser.add_argument('--output',type=pathlib.Path,default=ROOT/'output/rebirth-2026-11-05/The Schools of Magic, Arise! - Rebirth.json')
    args=parser.parse_args()
    raw=args.base.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=BASE_SHA:
        raise ValueError('The merge base differs from the author-approved Universal Fishing world. Review it before rebuilding.')
    base=json.loads(raw.decode('utf-8-sig'))
    w,meta=build(base)
    project.write_json(args.output,w)
    review=dict(baseCommit='48445de',baseFileSHA256=BASE_SHA,baseHash=digest(base),afterHash=digest(w),rows=changes(base,w),contents=meta,livePlaytest=False)
    project.write_json(HERE/'review.json',review)
    project.write_json(args.output.parent/'Baseline - Universal Fishing.json',base)
    print(js(dict(candidate=str(args.output),forms=meta['forms'],scrolls=len(meta['scrolls']),npcs=len(meta['npcs']),locations=len(meta['locations']),quests=len(meta['quests']))))


if __name__=='__main__':
    main()
