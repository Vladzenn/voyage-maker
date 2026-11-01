"""Build this update from its saved, user-current baseline, never an old release."""
import copy
import hashlib
import json
import pathlib
import re
from cast import build_cast
from content import ARCS, QUESTS, MONSTERS
from housing import PROPERTIES
from polish import apply as polish

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
TEMP = ROOT / 'tmp/adventurers'
BASE = TEMP / 'baseline.json'
load = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
dump = lambda p, x: p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
w = load(BASE)
original = copy.deepcopy(w)
party = w['parties']['']
manifest = {'baselineSHA256': hashlib.sha256(BASE.read_bytes()).hexdigest(), 'npcs': [], 'quests': [],
            'arcs': list(ARCS), 'triggers': [], 'items': [], 'traits': [], 'types': list(MONSTERS),
            'properties': PROPERTIES, 'guildJobs': []}


def trigger(name, conditions, effects=None, script=None, recurring=False, phase=None, scope=None):
    assert name not in w['triggerDefinitions'], name
    value = dict(name=name, conditions=conditions, effects=effects or [], recurring=recurring)
    if script is not None: value['script'] = script
    if phase: value['phase'] = phase
    if scope: value['scope'] = scope
    w['triggerDefinitions'][name] = value
    manifest['triggers'].append(name)


def item(name, category, description, tier='mundane', value=1):
    assert name not in w['itemTypes'], name
    w['itemTypes'][name] = dict(name=name, category=category, description=description,
                              tier=tier, estimatedValue=value, bonuses=[])
    manifest['items'].append(name)


def story(text): return dict(type='story', instruction=text)
def condition(typ, value, operator='equals', **extra): return dict(type=typ, operator=operator, value=value, **extra)
def at(location): return condition('party-location', location)


cast, portrait_briefs = build_cast(w)
cast['Ysolenne']['type'] = 'Snow Spirit'
cast['Masaru Hasebe']['currentArea'] = 'Prison Work Yard - Workshop'
for name in ['Daigo Kisaragi','Chisato Akamine','Tomoe Inukai','Gaku Shindō']:
    cast[name]['faction'] = 'Bellwether Company'
w['npcs'].update(cast)
manifest['npcs'] = list(cast)
for name, (public, hidden) in {
 'Bellwether Company': (
  'A small licensed adventuring company led by Daigo Kisaragi, with Chisato Akamine, Tomoe Inukai and Gaku Shindō. They take escorts, mountain recovery and practical field commissions, sharing costs and disagreeing openly about what a job is worth. Their current Coldglass investigation has exposed a gap in their magical expertise. Each keeps a life and ambitions beyond the company.',
  'Their Silver credentials are real. Company membership is not a separate guild rank or a right to command strangers. They can hire help or cooperate without automatically recruiting the player. Daigo Kisaragi\'s wish to look dependable conflicts with Chisato Akamine\'s insistence on admitting the investigative gap. Their mutual loyalty does not eliminate consent, payment or disagreement.'),
 'Copper Laurels': (
  'Jōta Kamezaki, Beni Tsunoda, Riko Kanehara and Sōta Tobisawa travel under an extravagant copper-laurel badge. They have completed real work and are known for loud claims about their own importance. Their private company mark is not a new rank in the international Adventurer\'s Guild.',
  'They have begun extorting invented recovery fees and claiming other expeditioners\' loot. Keep the four actual authored individuals; never generate copies as generic bandits. Resolved theft needs an actual success and inventory change. They are selfish comic opportunists with limited courage and real relationships, not an omnipotent syndicate or innocent misunderstood heroes. Exposure, defeat, restitution, bargaining or internal fracture can change their conduct.')
}.items():
    w['factions'][name] = dict(name=name, factionType='minor', initialKnown=False, basicInfo=public, hiddenInfo=hidden)

# Introduce actual homes/work rooms as areas, preserving all existing map coordinates and images.
for p in PROPERTIES:
    loc = w['locations'][p['location']]
    door = p['location'] + ' - ' + p['door']
    assert door in loc['areas'], door
    room = p['location'] + ' - ' + p['title']
    p['area'] = room
    descriptions = {
        'roseberry':'A compact private attic room with a bed, washstand, locking chest and writing table under the eaves.',
        'whitepass':'A warm private room with a sturdy bed, gear hooks and a shuttered mountain window above the lodge drying loft.',
        'canopy':'A private guest bough with an adjustable sleeping nook, sheltered work shelf and space for ordinary luggage.',
        'willowbend':'A small courtyard cottage containing a kitchen, sleeping room, storage loft and narrow garden.',
        'workshop':'A modest bench workshop with a workroom, front counter and lockable materials cupboard. Specialist tools and materials are separate property.',
        'snowmelt':'A compact landing flat with a sleeping alcove, tiny hearth kitchen, work table and sheltered gear cupboard.'}
    loc['areas'][room] = dict(description=descriptions[p['id']], paths=[door])
    loc['areas'][door].setdefault('paths', []).append(room)
    loc['basicInfo'] += '\n\n' + p['title'] + ' is available by agreement: ' + str(p['price']) + ' marks for ' + ('the quoted paid stay' if p['rent'] else 'the property purchase') + '. Ask ' + p['owner'] + ' to inspect it and confirm the actual terms before paying.'
    loc['hiddenInfo'] = loc.get('hiddenInfo', '') + '\n\nPROPERTY TERMS: ' + p['title'] + ' has a fixed opening quote of ' + str(p['price']) + ' marks. Its native transaction supplies the key/deed and removes that price once when the owner agrees and the player explicitly commits. Do not also charge or grant it through item generation. A quote, viewing or gift of a key does not silently transfer ownership. Rentals cover the agreed stay, have no background rent drain and need a fresh agreement for an extension; purchases are permanent modest property with no automatic income or free specialist stock. Unavailable sold property is not offered to a second unrelated buyer. Ordinary room access stays local.'
    item(p['key'], 'Key' if p['rent'] else 'Document', p['description'])
    query = ('The player explicitly commits now to ' + ('rent ' if p['rent'] else 'purchase ') + p['title'] + ' from ' + p['owner'] +
             ' for exactly ' + str(p['price']) + ' marks after the owner has agreed. The room/property is actually available, the funds are the player\'s to spend and payment is being tendered for this transaction. Merely asking, inspecting, haggling, planning, discussing somebody else\'s purchase or a completed earlier transaction is false.')
    trigger('ad34_property_' + p['id'], [at(p['location']), condition('player-item', p['price'], 'greaterThanOrEqual', item='Mark'),
        condition('player-item', 0, item=p['key']), dict(type='action', query=query)],
        [dict(type='item-remove', item='Mark', quantity=p['price'], target='satisfyingPlayers'),
         dict(type='item-add', item=p['key'], quantity=1, target='satisfyingPlayers'),
         story('Conclude the agreed handover of '+p['title']+'. The proprietor passes the actual key and any purchase papers to the paying player. The tag/papers identify that person and the actual agreement. Preserve their room and property; no second payment, new companion, free stock or extra house is created.')],
        recurring=p['rent'], scope='player')

item('Stillwind Pearl', 'Relic', 'A pale, hollow-luster pearl formed within a sky nautilus\'s current-sensing chamber. Fine bands in its surface briefly repeat the air-and-mana pattern of the place where it formed. A fresh specimen loses that clear pattern over a few hours, leaving a beautiful and scientifically interesting shell-like bead. It supplies no endless power.', 'special', 900)
w['npcTypes'].update({name: dict(name=name, **value) for name, value in MONSTERS.items()})
party['arcs'].update(copy.deepcopy(ARCS))

private_jobs = []
for title, source, offer, work, level, rank, fee, premise, objective, obstacle in QUESTS:
    assert title not in party['quests'] and source in w['npcs'] and work in w['locations']
    brief = (obstacle + '\nThis is optional finite work. Establish the actual terms before commitment; hearing a public lead is not accepting. '
             'Run a relevant obstacle, show the decisive deed using its actual people, object and place, and let a finished objective stay finished. '
             'Use the native completion condition as the sole completion owner. Do not create a monitoring trigger or repeat the payout in narration. '
             'Respect ordinary difficulty for the least experienced human; NPC companions do not raise that band. '
             + ('The posted fee is '+str(fee)+' marks per participating player, settled by completion effects once; the guild takes no additional cut. Actual guild work gives one service credit. Foreign travel still needs court permission.' if rank else
                'This is a private undertaking, not licensed guild service. Any fixed payment below settles once; no guild credit, automatic training or unagreed gift is added.'))
    effects = []
    if fee: effects.append(dict(type='item-add', item='Mark', quantity=fee, target='allPlayers'))
    if rank: effects.append(dict(type='item-add', item='Guild Service Credit', quantity=1, target='allPlayers'))
    effects.append(story('Let the actual result of '+title+' stand. Return entrusted property as agreed and preserve who took part, any settled payment and the actual relationships. The completed task creates no new debt or compulsory follow-up.'))
    party['quests'][title] = dict(name=title, questSource=source, questLocation=work, detailType='detailed', status='hidden',
        questStatement=premise, mainObjective=objective, questDesignBrief=brief, conclusive=True,
        completionCondition=dict(type='story', query='For "'+title+'", the accepted undertaking\'s actual events establish this final objective: '+objective+' A sincere imperfect result qualifies when its stated objective allows it. Plans, promises, another person\'s unrelated work or the mere offer are false. Preserve a verified outcome after travel; no extra report beyond the stated scope is required.'),
        onCompleteEffects=effects)
    manifest['quests'].append(title)
    if rank:
        manifest['guildJobs'].append(dict(title=title, rank=rank, slug='', repeatable=False, recommendedLevel=level))
    else:
        private_jobs.append(dict(title=title, source=source, location=offer, level=level))
        trigger('ad34_offer_' + str(len(private_jobs)), [at(offer), condition('read-string', title, key='ad34_offer_target'),
                 condition('quest-status','hidden',questId=title), condition('npc-in-scene',True,npc=source),
                 dict(type='story',query='The player has actually encountered the specific offer "'+title+' from '+source+', with its real problem and scope explained, and has asked about helping or requested its terms. An overheard hint, merely arriving, an unrelated conversation or an imagined future offer is false.')],
                [dict(type='quest-init',operator='set',value=title)])

board = w['triggerDefinitions']['gh_guild_board']['script']
match = re.search(r'const jobs=(\[.*?\]);', board, re.S)
assert match, 'Guild board table changed; inspect rather than guessing.'
jobs = json.loads(match.group(1)) + manifest['guildJobs']
w['triggerDefinitions']['gh_guild_board']['script'] = board[:match.start(1)] + json.dumps(jobs, ensure_ascii=False, separators=(',',':')) + board[match.end(1):]

legacy_ids = ['q20_air_1_accept','q20_hunt_1_accept','q20_av_bloom_accept','q20_av_carrier_accept',
              'q20_av_shed_accept','q20_av_dive_accept','q20_av_sketch_accept','q20_av_rivals_accept']
legacy_words = ['crossing|route|tether|road made','hunt|predator|shape.*wake','bloom|rehearsal|celebration',
                'roots|voice|hum','manta|shed|comb','orrery|drown|ring','shade|green|pigment','rival|teams|clean sample']
legacy = []
for name, words in zip(legacy_ids, legacy_words):
    tr = w['triggerDefinitions'][name]
    title = next(c['questId'] for c in tr['conditions'] if c['type']=='quest-status')
    legacy.append(dict(title=title,source=party['quests'][title]['questSource'],words=words))
    tr['conditions'].insert(-1, condition('read-string',title,key='ad34_legacy_offer'))
    tr['phase'] = 'state'  # the planning dispatcher supplies this turn's relevance gate
dispatch = (HERE / 'dispatch.js').read_text(encoding='utf-8').replace('JOBS', json.dumps(private_jobs, ensure_ascii=False)).replace('LEGACY',json.dumps(legacy,ensure_ascii=False))
manifest['modifiedExistingTriggers'] = ['gh_guild_board',*legacy_ids,'gh_lore_tournament_start','gh_portal_key_issue_drakenspire','gh_portal_key_issue_asterveil']
w['triggerDefinitions']['gh_lore_tournament_start']['conditions'].insert(0,condition('party-location','^(The Eternal Crucible|.*Academy)$','regex'))
for name in ['gh_portal_key_issue_drakenspire','gh_portal_key_issue_asterveil']:
    w['triggerDefinitions'][name]['conditions'].insert(0,condition('party-location',"^(The Grand Sage's Court|Sage's Spire|Evertree Base)$",'regex'))
trigger('ad34_scene_dispatch', [condition('game-tick',0,'greaterThanOrEqual')], script=dispatch, recurring=True, phase='planning')
trigger('ad34_quest_repair', [condition('game-tick',0,'greaterThanOrEqual')], script=(HERE/'quest_repair.js').read_text(encoding='utf-8'), recurring=True, phase='planning')

route_pairs = {
 'Ragnar Leonhart': [('The Eternal Crucible','Arena Floor'),('Crooked Tankard','Hearth Corner'),('The Cinder Pit','Fighting Floor'),('Whitepass Caravan Lodge','Common Hearth'),('Cloudbloom Landing','Crossing Quay'),('Asterveil Canopy','Guest Terrace'),('The Eternal Crucible','Competitor Passage'),('Roseberry Inn','Common Room')],
 'Adoha Aonuma': [('Four Sages Bazaar','Four Sages Fountain'),('The Jade Cup Teahouse','Tea Room'),('Snowbell Playhouse','Stage and Wings'),('The Copper Ram',"Musicians' Corner"),('Asterveil Canopy','Guest Terrace'),('Asterveil Canopy','Guest Boughs'),('Roseberry Inn','Common Room'),('Four Sages Bazaar','North Arcade')],
 'Karia Morino': [("Adventurer's Guild - Glowhaven Branch",'Training Yard'),('Crooked Tankard','Taproom'),('Whitepass Caravan Lodge','Route Desk'),('The Copper Ram','Taproom'),('Rimeglass Refuge','Common Shelter'),('Reedglass Anchorage','Arrival Deck'),('Heatherwatch Shelf','Common Room'),('Asterveil Canopy','Guest Terrace')]
}
routes = {name: [[loc,loc+' - '+area] for loc,area in stops] for name,stops in route_pairs.items()}
for name, stops in routes.items():
    for loc,area in stops: assert area in w['locations'][loc]['areas'], area
    w['npcs'][name]['hiddenInfo'] += '\n\nTravel habits: '+', then '.join(loc for loc,_ in stops)+'. These are touring preferences, not promised appointments. Actual conversation, agreed work, party travel, injury and combat take precedence. Their personal standing court travel permission gives no key or permission to the player.'
    slug = name.split(' ')[0].lower()
    trigger('ad34_hold_'+slug, [condition('npc-in-scene',True,npc=name),condition('npc-health',0,'greaterThan',npc=name),condition('read-boolean',False,key='ad34_hold_'+name),
        dict(type='story',query='In the latest actual scene, '+name+' has explicitly agreed to remain at the present place for a specific continuing commitment, or has actually become confined or injured so they cannot resume independent travel. Mere friendliness, a suggested invitation, ordinary rest or a hypothetical injury is false.')],
        [dict(type='write-boolean',key='ad34_hold_'+name,operator='set',value=True)],recurring=True)
    trigger('ad34_resume_'+slug,[condition('read-boolean',True,key='ad34_hold_'+name),condition('npc-health',0,'greaterThan',npc=name),
        dict(type='story',query='The actual specific commitment or confinement that paused '+name+'\'s independent tour has now genuinely ended, or the person has explicitly agreed to resume independent travel. A promise to release them later or an unrelated past event is false.')],
        [dict(type='write-boolean',key='ad34_hold_'+name,operator='set',value=False)],recurring=True)
trigger('ad34_touring_cast', [condition('game-tick',0,'greaterThanOrEqual')],
        script=(HERE/'tour.js').read_text(encoding='utf-8').replace('ROUTES',json.dumps(routes,ensure_ascii=False)), recurring=True,phase='planning')
manifest['routes'] = routes

public_rows = [
 ('Phoenix Wing Academy','A Formula Worth Selling','Ranka Kagari is trying to arrange a small recovery-formula trial; somebody at the faculty table is asking why two dosage sheets disagree.'),
 ('Gryffin Tail Academy','One Standard, Two Students','Two students compare reassessment notices with different requirements for what appears to be the same exercise.'),
 ('Dragon Hoard Academy',"The Shield's Late Return",'A student complains that a loaned shield has not come back to Mai Kajiwara\'s repair queue.'),
 ('Hydra Head Academy','What the Scent Becomes','People near Kaoruko Hanazono\'s workroom are arguing about a fragrance batch that changed after leaving the bench.'),
 ("Rune and Raven's",'The Wrong Kind of Light','A customer asks Rui Takatori why a purchased light does not behave like the demonstration.'),
 ('Whitecrest Harbor','A Crate Without a Signature','At the cargo pier, a delivery is waiting because nobody has matched it to an actual accepting party.'),
 ('Glowhaven Farmlands','Water Owed Downstream','Growers downstream are comparing the water reaching their irrigation runs with what their neighbors expected.'),
 ('Four Sages Bazaar','A Fair Measure','Two traders are checking the same weight on different scales, drawing a small but interested audience.'),
 ('The Everlight Public Library','Margins in Two Hands','A reader has noticed two different hands making incompatible notes in a much-consulted text.'),
 ('The Eternal Crucible','Before the First Bell','A practice entrant has been told to arrive early, and is trying to find out which part of the preparation actually matters.'),
 ('Snowbell Playhouse','The Premiere Was Yesterday','A tired performer at Snowbell Playhouse is comparing the advertised opening date with the rehearsal everyone actually attended.'),
 ('The Cinder Pit','The Cinder Pit Rematch','A previous bout is still being argued about at the booking desk, and somebody wants a properly arranged rematch.'),
 ('Snowmelt Residential Steps','Room for One More Bench','Neighbors are measuring a shared landing and disagreeing about whether another bench would help or block the way.'),
 ('Woolridge Pastures','Tracks Beside the Fold','A herder has marked unfamiliar tracks near the winter fold and wants a sound explanation before moving the animals.'),
 ('Asterveil Canopy','First Bloom, Last Rehearsal','A celebration rehearsal and the first flowering work both need the same stretch of shared Canopy space.'),
 ('Rimeglass Crown','What the Manta Leaves','Expeditioners compare a shed comb fragment with the immense filter feeders seen riding the mountain\'s lee currents.'),
 ('Bellwind Conservatory','Cuts Among the Pollen','A conservatory worker is examining a damaged pollen screen while two colleagues disagree about how it happened.'),
 ('Prison Records Office','A Date in the Ledger','An authorized records visitor asks why two dates in the same case file do not agree. This is public counter business, not access to the secure archive.')]
opportunities = [dict(id='q'+str(i),location=loc,quest=q,text=text,level=1) for i,(loc,q,text) in enumerate(public_rows)]
opportunities.extend([
 dict(id='winter',location='Whitepass Caravan Lodge',quest='',level=25,text='Daigo Kisaragi\'s Bellwether Company has returned with frost samples and no confident reading of them. They need help tracing the unnatural cold from Coldglass Galleries; their martial experience has stopped being enough.'),
 dict(id='thesis',location='Asterveil Canopy',quest='',level=25,text='Suzuha Midorise is looking for help finding the Stillwind Pearl after her guild posting attracted no volunteers. She has measurements, stubborn hope and very little ability to defend herself in the wild.'),
 dict(id='laurels',location='Tetherroot Chain',quest='',level=25,text='An expeditioner is complaining that the Copper Laurels demanded a recovery fee for a prize they never helped recover. Another traveler has heard the same boast at a different crossing.')])
for e in opportunities:
    assert e['location'] in w['locations']
    if e['quest']: assert e['quest'] in party['quests']
trigger('ad34_public_opportunities',[condition('game-tick',3,'greaterThanOrEqual')],
    script=(HERE/'opportunities.js').read_text(encoding='utf-8').replace('OPPORTUNITIES',json.dumps(opportunities,ensure_ascii=False,separators=(',',':'))),recurring=True)
manifest['opportunities'] = opportunities
trigger('ad34_returning_clients',[condition('game-tick',3,'greaterThanOrEqual')],script='''
const contacts=[
 ['Guild: Boars at the Watercourse',"Adventurer's Guild - Glowhaven Branch",'Komugi Hanabishi'],
 ['The Wrong Kind of Light',"Rune and Raven's",'Rui Takatori'],
 ['Tracks Beside the Fold','Woolridge Pastures','Haruto Aonuma']
];
const tick=Number(check({type:'game-tick'})), place=check({type:'party-location'});
const input=String(check({type:'action-text'})||'');
const combat=check({type:'npc-in-combat',npc:'anySceneNPC'});
if(tick-Number(storage.ad34_last_public_tick ?? -100)<9 || /attack|cast|fight|rest|sleep|kiss|quest done:/i.test(input) ||
   (combat && typeof combat==='object' && Object.values(combat).some(Boolean))) skip=true;
else {
 const row=contacts.find(([q,l,n])=>l===place && check({type:'quest-status',questId:q})==='completed' &&
   check({type:'npc-in-scene',npc:n})===true && !storage['ad34_client_return_'+q]);
 if(!row)skip=true;
 else {
  const [quest,location,npc]=row;
  effects.push({type:'story',instruction:npc+' can give one small returning-client acknowledgment appropriate to the actual known outcome of '+quest+'. Use only established deeds and people; if the record does not establish a particular result, keep it a courteous familiar greeting. Then resume ordinary business. No new errand, repeated payment, debt, romance or automatic reputation gain.'});
  storage['ad34_client_return_'+quest]=true;storage.ad34_last_public_tick=tick;
 }
}
''',recurring=True)

# Actual locations support repeated personal contact without extra map pins.
for npc in cast.values():
    loc = w['locations'][npc['currentLocation']]
    loc['hiddenInfo'] = loc.get('hiddenInfo','') + '\n\nAuthored contact: '+npc['name']+' is initially based at '+npc['currentArea']+'. Use that existing individual when their role is relevant; introduce manageable groups and preserve actual subsequent travel or absence.'
w['locations']['Coldglass Galleries']['hiddenInfo'] += '\n\nThe Bellwether investigation and Ysolenne\'s cold-fed nodes belong to The Woman Beyond the Frost. Examine the Mirror Gallery, Split Crossing and Meltwater Chamber through real traversal and clues. Terrain, lesser winter manifestations and the spirit\'s choices create resistance. Do not auto-resolve the investigation, reveal her entire motive on arrival or relocate Orrum into the cavern for convenience.'
w['locations']['Asterveil Canopy']['basicInfo'] = w['locations']['Asterveil Canopy']['basicInfo'].replace(', precisely where the planning map marks a red X','')
w['locations']["Adventurer's Guild - Glowhaven Branch"]['areas']["Adventurer's Guild - Glowhaven Branch - Briefing Room"]['description'] += ' Before an unfamiliar job, visitors can ask for practical route advice: known hazards, transport, supplies and an honest account of uncertain information. Marika Hoshino or Iona Hayashida can contribute when actually present or available by arrangement. A consultation grants no key, credential, automatic escort or mastery.'
for loc, species in [('Coldglass Galleries','Frostglass Leech'),('Lanternamber Caverns','Frostglass Leech'),('Tetherroot Chain','Bracewing Cicada'),('Cloudbloom Landing','Cloudveil Nautilus'),('Mirrorwater Basin','Cloudveil Nautilus'),('Glassreed Labyrinth','Needleback Prowler'),('Caravan Outpost','Vaultjaw Marten')]:
    w['locations'][loc]['hiddenInfo'] += '\n\nAdditional local creature possibility: '+species+'. Use an actual appropriate individual only in a fitting occupied habitat or current problem. Safe services remain safe; this is not a mandatory spawn. Follow this location\'s level band and the least experienced human\'s ordinary-work risk, with warning before a deliberate harder undertaking.'

# Specific generation policies: they bound generated/refined gear, not authored catalogue records.
for tier, values in {'mundane':(1,2,1,5,1,2,20,12,6),'artisan':(2,3,2,10,2,3,40,24,10),
                     'special':(3,4,3,15,3,5,70,40,16),'legendary':(4,5,4,20,4,8,100,60,24)}.items():
    initial, refined, damage, armor, attribute, skill, health, mana, stamina = values
    allowed = [dict(type='stat',variable='damage',min=0,max=damage),dict(type='stat',variable='armor',min=0,max=armor)]
    allowed += [dict(type='attribute',variable=a,min=1,max=attribute) for a in w['attributeSettings']['attributeNames']]
    allowed += [dict(type='skill',variable=s,min=1,max=skill) for s in w['skills'] if s != 'Time Magic']
    allowed += [dict(type='resource',variable=r,min=1,max=n) for r,n in [('Health',health),('Mana',mana),('Stamina',stamina)]]
    w['itemSettings']['tiers'][tier]['bonusPolicy'] = dict(initialMaximumPicks=initial,refinedMaximumPicks=refined,allowedBonuses=allowed)
    w['itemSettings']['tiers'][tier]['description'] = (
        {'mundane':'Ordinary reliable goods; simple material advantages rather than elaborate powers.',
         'artisan':'Skilled craftsmanship, fine fit and dependable materials; specialist work need not be magical.',
         'special':'A meaningful bounded magical property or exceptional specialist construction.',
         'legendary':'Creator-placed exceptional artifacts with specific histories and limits; not routine generated stock.'}[tier]
        + ' New equipment has at most '+str(initial)+' bonus picks; actual refinement has at most '+str(refined)+'. Follow the permitted per-pick ranges. Maintenance adds no bonus pick; non-equippable goods have no equipment bonuses.')

loadouts = {
 'Spear and Rope Kit':['Ashwood Spear','Survey Rope Coil'],
 'Bow Starter Kit':['Yew Hunting Bow','Supple Archery Gloves'],
 'Crossbow Starter Kit':["Stockman's Crossbow"],
 'Greatsword Starter Kit':["Traveler's Greatsword"],
 'Axe Starter Kit':["Woodcutter's Fighting Axe",'Plain Work Gloves'],
 'Mace and Buckler Kit':['Plain Flanged Mace','Ironbound Round Shield'],
 'Polearm Starter Kit':["Gatekeeper's Halberd"],
 'Twinblade Starter Kit':['Balanced Twinblade'],
 'Flexible Weapon Kit':['Braided Fighting Whip','Working Dagger'],
 'War Fan Starter Kit':['Steel-Ribbed War Fan'],
 'Scythe Starter Kit':['Long-Haft War Scythe'],
 'Paired Blades Starter Kit':['Matched Street Blades']}
if 'Survey Rope Coil' not in w['itemTypes']:
    loadouts['Spear and Rope Kit']=['Ashwood Spear']
for name, items in loadouts.items():
    for it in items: assert it in w['itemTypes'], it
    desc='Begin with '+', '.join(items)+'. Ordinary usable equipment; choosing it grants no combat skill or magical discipline.'
    w['traits'][name] = dict(name=name,description=desc,traitNarrativeEffects=desc+' Supply the listed items once at creation, with no second narrative grant, debt, employment or expert training.',
        attributes=[],skills=[],resources=[],startingItems=[dict(item=it,quantity=1) for it in items],abilities=[],unlockedBy=[],excludedBy=[],requirements=[])
    w['traitCategories']['Starting Equipment']['traits'].append(name)
    manifest['traits'].append(name)

trigger('ad34_custom_property_key', [condition('read-boolean',True,key='ad34_property_interest'),
    dict(type='story',query='In the latest actual scene, this player has completed a genuine rental, property purchase or grant of their own private room outside the six named fixed property offers. The owner has agreed, any actual price has been paid once, and no individualized key or deed has already been recorded for this handover. An offer, viewing, future plan, mere claim, remembered ownership or another person\'s purchase is false.')],
    [story('Finish the actual property handover with one clearly tagged key or the appropriate deed. Its ordinary inventory description identifies the real place, recipient, arrangement and any agreed term. Preserve the established payment and ownership; the key gives no stats, master access, new room, stock or second property. If the key was already received, do not duplicate it.')],recurring=True,scope='player')

ironman = dict(name='💀 Ironman Mode',description='Optional solo challenge: one life, no ordinary knockout return. The same world and normal enemy scaling, with final consequences for a genuine lethal defeat. Recommended for experienced players.',difficulty='medium',
 instructions='''## One life, chosen openly
This is an optional solo challenge. Do not impose it on a normal or multiplayer game. Preserve the world, selected start and established difficulty; permanent death is not a reason to invent stronger enemies, bad luck or compulsory misery.

## Lethal outcomes
For an actual lethal defeat, no routine knockout recovery or spontaneous resurrection follows. End the run with a brief meaningful epilogue about the people, promises and places the character affected. An actual nonlethal spar, consensual practice, ordinary sleep or an explicit nonlethal capture is not a death. Zero Mana or Stamina is never itself death. Do not invent a lethal result contrary to Combat Results.

## Fair warning and agency
Let people assess visible danger, prepare, hire help, avoid an offer or retreat when physically possible. Keep existing surprise events and their real rules. Do not turn every setback into death or prescribe the player's courage, sacrifice or final words. Companions retain their motives and can aid a real withdrawal; no automatic abandonment or suicidal loyalty.

## Scope
While active in an actual solo run, these final-outcome instructions take precedence over ordinary knockout narration. Do not apply them to other players or another mode. An irreversible fictional outcome does not authorize changing a supplied mechanical result.''',
 npcIntentInstructions='Use the actual abilities and action budget. Allies act usefully while the player fights, and an agreed retreat is coordinated rather than treated as cowardice. Enemies do not gain free moves or knowledge. Noncombatants and exhausted people have limits. No supplied miss becomes a hit for dramatic finality.',
 askTheNarratorPrompt='One life. Ask about visible danger, your actual condition and possible exits. I will not reveal hidden facts or change a resolved result. This challenge is intended for solo play.')
w['gameModes'][ironman['name']] = ironman
w['death']['instructions'] += '\nIRONMAN EXCEPTION: In an actual solo run currently using Ironman Mode, a genuinely lethal defeat receives a final epilogue instead of routine knockout recovery. Nonlethal training or capture is not automatically death. Normal modes retain their established recovery rules.'
trigger('ad34_ironman_final_outcome',[condition('read-boolean',True,key='ad34_solo'),condition('player-resource',0,'lessThanOrEqual',resource='Health'),
    dict(type='story',query='The current solo run is explicitly using Ironman Mode and its player has actually suffered a genuinely lethal defeat now. An ordinary nonlethal spar, training knockout, sleep, capture, empty Mana or Stamina, a hypothetical threat or another mode is false.')],
    [dict(type='lose-game',endScope='players'),story('Give this solo Ironman character a meaningful final epilogue grounded in their actual choices. Do not revive them, invent final words, award a victory or erase other people\'s existing lives.')],scope='player')

polish(w, original, manifest)
def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
media=[]
def urls(value, trail):
    if isinstance(value,dict):
        for k,v in value.items():urls(v,trail+[k])
    elif isinstance(value,list):
        for k,v in enumerate(value):urls(v,trail+[k])
    elif isinstance(value,str) and value.startswith('https://'):
        media.append(dict(path=trail,value=value))
urls(original,[])
manifest['preservation']={
 'media':media,
 'locationFields':{k:{f:v[f] for f in ['x','y','radius','region','imageUrl','hidden','initialKnown'] if f in v} for k,v in original['locations'].items()},
 'realmsHash':digest(original['realms']), 'regionsHash':digest(original['regions']),
 'questHashes':{k:digest(v) for k,v in original['parties']['']['quests'].items()},
 'itemHashes':{k:digest(v) for k,v in original['itemTypes'].items()},
 'triggerHashes':{k:digest(v) for k,v in original['triggerDefinitions'].items() if k not in manifest['modifiedExistingTriggers']},
 'protectedNPCs':{k:digest(original['npcs'][k]) for k in ['Ilyra Stillglass','Orrum','Rovakthuun','Orivelle']},
 'spiderLocations':{k:digest(v) for k,v in original['locations'].items() if original['regions'][v['region']]['realm']=='The Silken Descent'},
 'spiderNPCs':{k:digest(v) for k,v in original['npcs'].items() if v.get('currentLocation') in original['locations'] if original['regions'][original['locations'][v['currentLocation']]['region']]['realm']=='The Silken Descent'},
 'voices':{k:v.get('voiceTag') for k,v in original['npcs'].items()},
}
dump(TEMP/'manifest.json',manifest)
dump(TEMP/'candidate.json',w)
dump(HERE/'manifest.json',manifest)
print(json.dumps({'newNPCs':len(cast),'arcs':len(ARCS),'newQuests':len(QUESTS),'newTypes':len(MONSTERS),
 'publicSituations':len(opportunities),'newLoadouts':len(loadouts),'properties':len(PROPERTIES),'newTriggers':len(manifest['triggers'])},ensure_ascii=False))
