"""Small exact event owners around ordinary native quests and free local play."""
import copy, json
from geography import NATION, SPIRIT

def s(text):return {'type':'story','instruction':text}
def c(kind,value,operator='equals',**kw):return {'type':kind,'operator':operator,'value':value,**kw}
def setloc(place,area):return [c('party-location',place,'set'),c('party-area',area,'set'),{'type':'npc-placement','npc':'allPartyNPCs','operation':'moveTo','location':place,'area':area}]

def add_systems(w,catalog):
    added=[]
    def add(name,conditions,effects,script=None,**kw):
        if name in w['triggerDefinitions']:raise ValueError(name)
        tr={'name':name,'conditions':conditions,'effects':effects,'recurring':True,**kw}
        if script:tr['script']=script
        w['triggerDefinitions'][name]=tr;added.append(name);return tr
    # A new route reuses the original anomaly decision unchanged; old routes are not rewritten.
    replacements={'Drakenspire Mountains':NATION,'Drakenspire Highlands':'Benitsuru Basin','Drakenspire Portals':'Benitsuru Transit Shrine','Drakenspire - Portal Room':'Benitsuru Transit Shrine - Portal Hall','Drakenspire Portal Key':'Oni Nation Portal Key','Drakenspire':NATION}
    def replace(value):
        if isinstance(value,str):
            for a,b in replacements.items():value=value.replace(a,b)
            return value
        if isinstance(value,list):return [replace(v) for v in value]
        if isinstance(value,dict):return {k:replace(v) for k,v in value.items()}
        return value
    for suffix in ['to','from']:
        tr=replace(copy.deepcopy(w['triggerDefinitions']['gh_portal_'+suffix+'_drakenspire']))
        tr['name']='oni_portal_'+suffix;w['triggerDefinitions'][tr['name']]=tr;added.append(tr['name'])
        fast=copy.deepcopy(tr);fast['name']='oni_portal_'+suffix+'_direct'
        fast['conditions'][-1]={'type':'action-text','operator':'regex','value':r'^([Ii] )?(enter|cross|use|step through|walk through|go through|return|head|go)'}
        if suffix=='to':
            exact=r'^(?:i )?(?:(?:enter|cross|step through|walk through|go through|head through|travel through) (?:the |this )?(?:(?:portal|arch|gate) (?:to|for) )?(?:akitsuhara|oni nation)(?: (?:portal|arch|gate))?|use (?:my |the )?(?:oni nation|akitsuhara)(?: portal)? key)[.!]?$'
        else:
            exact=r'^(?:i )?(?:(?:enter|cross|step through|walk through|go through) (?:the |this )?(?:return )?(?:portal|arch|gate)(?: (?:back )?to (?:glowhaven|evertree(?: base)?))?|(?:return|head back|go back) to (?:glowhaven|evertree(?: base)?))[.!]?$'
        fast['script']="const oniRaw=check({type:'action-text'});const oniInputs=Array.isArray(oniRaw)?oniRaw:[oniRaw];const oniText=oniInputs.length===1?String(oniInputs[0]).trim().toLowerCase():'';if(!new RegExp("+json.dumps(exact)+").test(oniText)){skip=true;}else{\n"+tr['script']+'\n}'
        w['triggerDefinitions'][fast['name']]=fast;added.append(fast['name'])
    issue=copy.deepcopy(w['triggerDefinitions']['gh_portal_key_issue_asterveil'])
    issue['name']='oni_portal_key_issue';issue['conditions'][0]['value']="^(The Grand Sage's Court|Sage's Spire|Evertree Base|Benitsuru Transit Shrine)$"
    issue['conditions'][1]['item']='Oni Nation Portal Key'
    issue['conditions'][2]['query']='The court or an actually delegated transit officer at this desk approves the traveler for a legitimate journey and actually hands them an Oni Nation Portal Key now. Enrolled study, a real expedition, authorized trade, local official business or credible sponsorship can qualify. Requests, mere status, another person’s key and an unofficial gift are false. Nobu Senda is Akitsuhara’s authorized bilateral transit registrar. A valid permitted request can be handled here without sending the traveler to a distant court first.'
    issue['effects'][0]['item']='Oni Nation Portal Key'
    w['triggerDefinitions'][issue['name']]=issue;added.append(issue['name'])
    w['locations']['Evertree Base']['basicInfo']+=' Its ordinary network also serves Akitsuhara through Benitsuru Transit Shrine.'
    w['locations']['Evertree Base']['areas']['Evertree Base - Portal Room']['description']+=' An additional torii-marked arch serves Akitsuhara. Its Oni Nation Portal Key can be issued by an authorized transit delegate here for a legitimate journey, alongside the existing destination keys.'
    w['locations']['Evertree Base']['hiddenInfo']+=' Akitsuhara uses the same court-authorized network and the same once-only outward anomaly decision. Do not invent a separate academy portal or an automatically free key. The local Spirit Torii in Akitsuhara is outside this public network and returns to its own local gate.'
    add('oni_soul_torii_awaken',[c('party-location','Moonless Torii'),c('player-item',0,'greaterThan',item='Restored Way Bell'),c('read-boolean',False,key='oni_soul_gate_awake'),{'type':'action','query':'The player deliberately sounds the real restored way bell to awaken this torii now. Looking at the hook, discussing a future attempt, claiming an absent bell or ringing an unrelated object is false. Awakening the gate does not choose to cross it.'}],
        [c('write-boolean',True,'set',key='oni_soul_gate_awake'),c('known-entity',True,'set',entity=SPIRIT),c('known-entity',True,'set',entity='Veiled Cedar Reach'),c('known-entity',True,'set',entity='Veiled Threshold'),s('The bell’s double note answers through the empty arch. Fog draws back from a dry stone threshold on the far side, with a clear stable view home. The route is now permanently awake; keep the bell as an ordinary keepsake. Stop before choosing to enter.')],recurring=False)
    lock="const tick=check({type:'game-tick'});if(storage.ghPortalTransitTick===tick){skip=true;}else{storage.ghPortalTransitTick=tick;}"
    add('oni_soul_torii_cross',[c('party-location','Moonless Torii'),c('read-boolean',True,key='oni_soul_gate_awake'),{'type':'action','query':'The active player party chooses to cross the awakened Soul Torii into the mist now. A clear enter or step through qualifies when this open gate is the actual referent. Discussion, an unawakened gate, a future plan or leaving part of a split party behind is false.'}],setloc('Veiled Threshold','Veiled Threshold - Return Torii')+[s('Arrive together on the dry Veiled Threshold. Describe dense fog, huge cedar shapes and the immediately usable home torii. Stop here; do not choose a deeper journey, encounter or return.')],lock)
    add('oni_soul_torii_return',[c('party-location','Veiled Threshold'),{'type':'action','query':'The active party actually enters the fixed return torii now, including a clear bare enter when it refers to this arch. It leads to Moonless Torii in Akitsuhara, not the Evertree. No key or bell is required. Discussion or an unchosen split-party departure is false.'}],setloc('Moonless Torii','Moonless Torii - Torii Court')+[s('The local spirit crossing returns the actual party to Moonless Torii - Torii Court in Akitsuhara. Preserve people, goods and discoveries. This is one completed crossing; do not add an Evertree journey.')],lock)
    add('oni_hagire_roam',[c('game-tick',0,'greaterThan')],[],"""
const npc='Hagire',tick=Number(check({type:'game-tick'}));
const health=check({type:'npc-health',npc});
if(check({type:'read-boolean',key:'oni_hagire_route_safe'})||(typeof health==='number'&&health<=0)||check({type:'npc-in-scene',npc})===true||check({type:'npc-in-combat',npc})===true||check({type:'npc-in-party',npc})===true){skip=true;}else{
 const slot=Math.floor(tick/24),route=[['Ragged Cedar Hollow','Ragged Cedar Hollow - Hollow Center'],['Old Mask Trail','Old Mask Trail - Blind Turn'],['Foxfire Verge','Foxfire Verge - Cloth Strips']];
 if(storage.oniHagireSlot===slot){skip=true;}else{
  const at=route[slot%route.length];effects.push({type:'npc-placement',npc,operation:'moveTo',location:at[0],area:at[1]});storage.oniHagireSlot=slot;
 }
}
""",phase='planning')
    # Occasional public news, never quest acceptance or automatic spawning.
    add('oni_forest_rumor',[c('party-location',"^(Lanternwood Field Shelter|Redleaf Guest Village|Benitsuru Guildhall)$",'regex'),c('read-boolean',False,key='oni_hagire_route_safe'),{'type':'action','query':'The player genuinely asks about local forest danger, missing travelers or a named hunt. A casual arrival, completed unrelated job, combat or private romantic conversation is false.'}],
        [s('Offer one concrete public account of Hagire: hanging cloth and joint cracks near the old cedar trail. Describe a dangerous optional hunt and the actual three haunts, not a creature already attacking this safe place. The listener may ask, investigate or ignore it; do not accept the contract or reveal an unseen private fact.')],"const t=Number(check({type:'game-tick'}));if(t-Number(storage.oniRumorTick??-100)<12){skip=true;}else{storage.oniRumorTick=t;}")
    # The existing multi-part license is reusable; branch-specific copies use the same passes/badge.
    oldq='Guild: Adventurer Licensure';newq='Guild: Benitsuru Licensure'
    q=copy.deepcopy(w['parties']['']['quests'][oldq]);q['name']=newq;q['questSource']='Hiyori Mitsuba';q['questLocation']='Benitsuru Guildhall'
    def rename(v):
        if isinstance(v,str):return v.replace(oldq,newq).replace('Komugi Hanabishi','Hiyori Mitsuba').replace("Adventurer's Guild - Glowhaven Branch",'Benitsuru Guildhall')
        if isinstance(v,list):return [rename(x) for x in v]
        if isinstance(v,dict):return {k:rename(x) for k,x in v.items()}
        return v
    w['parties']['']['quests'][newq]=rename(q)
    for part in ['register','judgment','practical','certify']:
        tr=rename(copy.deepcopy(w['triggerDefinitions']['gh_guild_exam_'+part]));tr['name']='oni_guild_exam_'+part
        if part!='register':
            tr['script']="const original=check({type:'quest-status',questId:"+json.dumps(oldq)+"});if(original==='accepted'||original==='active'){for(const e of effects){if(e.questId==="+json.dumps(newq)+")e.questId="+json.dumps(oldq)+";}}"
        if part=='register':tr['effects'][-1]=s('Record the actual first-time applicant. Hiyori Mitsuba directs them to Mika Fuyuse in the assessment court for a brief judgment question and safe practical demonstration using their real training. Both can be addressed in one coherent assessment when actual play supports it; no repeated forms or extra fee. A genuine existing badge is recognized without another exam.')
        w['triggerDefinitions'][tr['name']]=tr;added.append(tr['name'])
    for rank in ['silver','gold','platinum']:
        for kind in ['review','promote']:
            tr=copy.deepcopy(w['triggerDefinitions']['gh_guild_'+kind+'_'+rank])
            tr['name']='oni_guild_'+kind+'_'+rank
            tr['conditions'][0]['value']='Benitsuru Guildhall'
            w['triggerDefinitions'][tr['name']]=tr;added.append(tr['name'])
    # A single contextual board uses native quest completion, not one controller per contract.
    board=[r for r in catalog if r['rank'] and (r['location'] in w['locations'])]
    data=json.dumps([[r['title'],r['level'],r['rank']] for r in board],ensure_ascii=False,separators=(',',':'))
    script="const jobs="+data+";\n"+"""
const levels=check({type:'player-level'})||{},names=Object.keys(levels),ranks={};
for(const n of names)ranks[n]=0;
for(let rank=1;rank<=4;rank++){
 const held=check({type:'player-item',item:'Guild Badge: '+['','Bronze','Silver','Gold','Platinum'][rank]})||{};
 for(const n of names)if(Number(typeof held==='number'?held:held[n])>0)ranks[n]=rank;
}
const licensed=Object.values(ranks).filter(x=>x>0),rank=licensed.length?Math.min(...licensed):0;
const level=names.length?Math.min(...Object.values(levels).map(Number)):1;
const raw=check({type:'action-text'});const text=(Array.isArray(raw)?raw.join(' '):String(raw||'')).toLowerCase();
const available=jobs.filter(j=>j[2]<=rank&&['hidden','inactive','unstarted',''].includes(String(check({type:'quest-status',questId:j[0]})||'')));
let chosen=available.filter(j=>text.includes(j[0].toLowerCase())||text.includes(j[0].replace(/^Akitsuhara Guild: /,'').toLowerCase()));
const explicit=chosen.length>0;
if(!explicit){
 const suitable=available.filter(j=>j[1]<=level+(level<7?2:5));
 const cursor=Number(storage.oniBoardCursor||0);chosen=suitable.length?[suitable[cursor%suitable.length]]:[];
 if(suitable.length>1)chosen.push(suitable[(cursor+1)%suitable.length]);storage.oniBoardCursor=cursor+2;
}
storage.ghGuildDisplayedOffers=chosen.slice(0,2).map(j=>j[0]);
storage.ghGuildOfferRanks=Object.fromEntries(chosen.slice(0,2).map(j=>[j[0],j[2]]));
for(const j of chosen.slice(0,2))effects.push({type:'quest-init',operator:'set',value:j[0]});
if(!rank)effects.push({type:'story',instruction:'Recognize any genuine international badge; otherwise offer the short local licensure assessment. Browsing is not certification.'});
else if(chosen.length)effects.push({type:'story',instruction:'Show the selected real postings and their stated terms. Browsing is not acceptance. '+(explicit&&chosen.some(j=>j[1]>level+5)?'Explain the actual greater danger and leave this knowingly harder work optional.':'Keep the offer suitable to the least experienced participating human; NPC companions do not inflate it.')});
else effects.push({type:'story',instruction:'No matching unfinished posting remains in this selection. Preserve completed work; discuss suitable ordinary work or another interest without reopening a finished contract.'});
"""
    from guild_patch import BROWSE_GATE_JS
    script=BROWSE_GATE_JS+'\nif(choiceCommit&&choiceOffers.length){skip=true;}else{\n'+script+'\n}'
    add('oni_guild_board',[c('party-location','Benitsuru Guildhall'),{'type':'action','query':'The player actually asks to browse local guild work, foreign expeditions or details of a named posting. Mere arrival, accepting a displayed contract, a completed report or unrelated conversation is false.'}],[],script)
    add('oni_glowhaven_expedition_notice',[c('party-location',"Adventurer's Guild - Glowhaven Branch"),{'type':'action','query':'The player specifically asks for fieldwork or an expedition to Akitsuhara or the Oni nation. Merely mentioning the country, ordinary local browsing or asking about a portal alone is false.'}],
      [c('quest-init','Expedition: The Foreign Grain','set'),s('Komugi Hanabishi can show the actual Akitsuhara irrigation commission. Explain its fieldwork and separate portal permission. This is an offer, not automatic acceptance or travel.')])
    return added

STARTS = [
 ('⚔️ Akitsuhara: Samurai at the Gate','Kagetsuna Household','Receiving Room','Ayame Kagetsuna','An Escort in Plain Clothes',
  'A junior service assignment, a house full of opinions and a commander who wants something useful done before noon.',
  '''The receiving room smells of clean wood and yesterday's rain. Beyond an open screen, someone in the practice court is making the same mistake for the fourth time. The answering correction is considerably louder than the strike.

Ayame Kagetsuna stands beside a low map table, one sleeve tied back, arguing with a courier about a cart.

“It has two wheels. I am reasonably sure the road has room for both.”

“The porter says the load is ceremonial.”

“Then it can be ceremonially moved six inches to the left.”

The courier leaves with the air of a man who intends to quote that exactly. Ayame turns toward you. Her amber eyes travel to the mud by the threshold and then back to your face.

“Good. You're here. We have a short delivery waiting at the south yard. It needs an escort who can solve an argument without making it a duel.”

She folds the corner of the map clear. A bright cord marks the maintained road, ending at a bridge repair. Behind her, a servant carries a tray past two retainers pretending not to listen.

“Ask what is being carried. Ask who owns it. And if the answer is ‘because my cousin said so,’ ask another question.”

Her mouth twitches.

“If you have questions about the assignment, now is an excellent time. If you have a magnificent speech prepared, I recommend saving it for someone who has finished breakfast.”'''),
 ('🥷 Akitsuhara: Behind the Reed Screen','Hidden Reed Training Ground','Screen Yard','Yuzuri Kageura','The Message behind the Message',
  'Begin among independent scouts, where noticing the ordinary detail matters more than an impressive entrance.',
  '''Water ticks from a bamboo spout into a stone basin. Three porters cross the practice yard in succession, each carrying the same kind of wrapped load. None of them looks at the narrow opening between the screens.

Yuzuri Kageura is standing beside that opening with a small ornamental gourd in her hand.

“One changed something,” she says. “Nothing stolen. Nothing dangerous. Tell me what you actually saw.”

On the far side of the yard, a young man starts to vault a rail. A voice from the shade tells him the gate was open. He lands badly enough to regret the flourish.

Yuzuri does not turn.

“This is why we practice before accepting money.”

The last porter pauses beside a water channel. A cord hangs from the load; its loose end is a different length from the others. There may be more to notice, or a perfectly ordinary reason for it.

“You can ask a question. You can look again. You can say you don't know. That last one is useful only if it is true.”

She sets the gourd on the rail, giving it a final protective glance. The yard remains open around you, screens stirring in the breeze, with no one yet deciding how you will proceed.'''),
 ('🍃 Akitsuhara: A Rōnin’s Morning','Red Maple Inn','Front Room','Tōma Sagiri','',
  'A crowded inn, an independent swordsman and a capital that offers more than another master to serve.',
  '''A sandal sits on the table beside a bowl of rice. Tōma Sagiri is repairing its strap with the concentration of a man handling a royal commission.

“Before you ask,” he says, “the food was here first.”

The inn's front room is filling with the ordinary noise of a capital morning. A porter wants an early bowl, two travelers disagree about a ferry fare, and somebody outside is advertising a blade that has apparently never missed. Tōma listens to the last claim and pulls the new strap tight.

“Must be exhausting, carrying something with a reputation like that.”

Chiyo Matsukaze passes the table with a folded fan tucked into her sash.

“If either of you wants paid work, ask before finishing the expensive tea. The south yard has escorts. The guild has a board. I have a loose shutter, but it is unlikely to earn you a song.”

She moves on to the porter. Beyond the open door, bright sleeves and loaded baskets pass along the street. The castle roofs rise above them; the guild road turns away beneath a line of shop awnings.

Tōma sets the sandal down.

“A shutter is an honest opponent. What sort of morning were you hoping for?”'''),
 ('🔔 Akitsuhara: The Bell Workshop','Evening Maple Shrine','Offering Court','Sae Kagurazaka','A Bell for the Mist',
  'Start with shrine life, a small repair and an old path that may answer a clear note.',
  '''A bronze bell lies on a padded tray beneath the shrine eaves. Without its clapper, it looks mildly offended by the morning.

Sae Kagurazaka turns it over, considers the empty mouth and gives it a sympathetic tap.

“Yes. I know. Everyone else gets to make noise.”

Behind her, a visitor is trying to decide which offering shelf is meant for ordinary thanks. Iori Kagurazaka points to the nearest one, then begins explaining the shelf's history until his aunt clears her throat.

“The short answer was excellent,” she tells him.

She turns to you, lifting the little tray clear of a damp patch on the bench.

“We have a clapper to fetch. It slipped below the mooring steps yesterday. Shallow water, awkward angle. A pole would do, or a rope, or a better idea.”

The bell's old cord is soft with wear. At the back of the court, a cedar path climbs toward the lower forest. It is a quiet place today, with a kettle warming and someone sweeping leaves into a pile that the wind keeps revising.

“Once this is sound, I'll show you where it belongs. First, though—would you rather look at the steps yourself, or hear Iori's very complete account of how it fell?”'''),
 ('🌾 Akitsuhara: Bread before Rumors','Hoshina Village','Grain Yard','Mutsumi Hosaka','First Bread in Hoshina',
  'Begin in a working village, with neighbors, an oven and room to choose a life beyond the sword.',
  '''A line of dough bowls occupies the dry side of the grain yard. On the wet side, three people are looking at an oven as if disappointment might repair it.

Mutsumi Hosaka emerges from behind the stack of firewood carrying a paddle that has lost half its handle.

“We have flour, fuel and opinions. Apparently those are not enough.”

A neighbor suggests magic. Another points out that someone tried that last month and the crust reached the far fence. The argument is familiar enough for a passing child to supply the next line before disappearing down the lane.

Mutsumi notices you and wipes one hand on her apron.

“Morning. There's work if you want it. We need the vent cleared, the good wood kept dry and one person willing to ask where the other paddle went.”

Across the yard, a water channel glints between the gardens. Carts are already moving toward the capital road. The village has its own business before any traveler arrives, and plenty of people prepared to explain how it ought to be done.

Mutsumi sets the broken paddle on the wall.

“Or you can tell me what brings you here. I can complain and listen at the same time.”'''),
 ('🧭 Akitsuhara: The Local Board','Benitsuru Guildhall','Reception','Hiyori Mitsuba','',
  'Join the international guild from its lively Akitsuhara branch, or bring your genuine badge and look for local work.',
  '''Someone has pinned a very small drawing of a furious umbrella beside the request board. The person arguing beneath it insists the umbrella was bigger.

“You also wrote ‘certain death’ on a roof repair,” Hiyori Mitsuba says without looking up. “We agreed that meant the ladder needed replacing.”

The man retreats toward the common tables. Hiyori slides a closed ledger aside and gives you her full attention, coral hair catching the daylight from the street.

“Welcome to Benitsuru. Already licensed, applying, or here to ask why that picture has teeth?”

Behind her, the door to the assessment court stands open. A practice spear taps twice against a padded post. Mika Fuyuse's voice follows: one brief correction, then a question about when to withdraw.

“Your genuine badge works here,” Hiyori says. “If you need your first one, the assessment uses what you actually know. No need to become a wizard to carry a spear, or a swordsman to know when a job has gone wrong.”

Bronze and silver tabs divide the nearer notices. Beyond them hang longer field commissions: samples, routes, a weather observation and a journey through the Evertree network. Some work looks modest. Some has enough preparation written into it to deserve the space.

She rests a pen across her fingers.

“What shall we look at first?”'''),
 ('🏔️ Drakenspire: By the Common Hearth','Whitepass Caravan Lodge','Common Hearth','Akemi Fushida','',
  'A mountain beginning among carriers, local work and the immense dragon bones above the city.',
  '''Snow melts from a line of boots beside the hearth. Beyond the lodge windows, roofs step up the mountain toward walls and the enormous pale curve of the sacred dragon's bones.

A carrier is trying to bring a loaded frame through a doorway that was built before anyone anticipated his particular ambitions.

Akemi Fushida watches him turn it sideways.

“That was promising,” she says. “Try taking the crate off before the door.”

The carrier stops. Somewhere behind the frame, a companion begins laughing with the helpless delight of someone who will be retelling this for years.

Akemi sets a bowl near the hearth and turns your way.

“Sit if you want warmth. Ask at the route desk if you want work. If you want to help him, I suggest starting with the straps.”

Across the room, travelers compare the state of the pass. Somebody has brought a fine blade for inspection; somebody else is carrying a goat that regards the entire arrangement with contempt. The lodge is a first foothold in a living mountain town, not an automatic expedition into its worst weather.

Akemi shifts the bowl clear of the struggling load.

“So. What sort of day have you come to find?”'''),
 ('🦋 Asterveil: Notes beneath Glass','Bellwind Conservatory','Living Gallery','Kureha Kazahana','',
  'Begin at an inhabited research hub above the clouds, with a real observation problem and wilderness beyond the maintained walks.',
  '''A leaf turns over beneath the gallery glass. Its underside catches the light in a color that disappears when you lean closer.

Kureha Kazahana has placed two trays beneath it, along with a pencil, a magnifying lens and a cup that contains considerably more pollen than tea.

“The left sample changes at the chime,” she says. “The right one changes when someone opens that door. Yesterday an extremely confident observer decided they were responding to affection.”

The door opens. A breeze crosses the gallery. The right sample obligingly changes.

Kureha looks at it with the satisfaction of a person whose objection has just become visible.

“You don't need an impressive spell. You need to notice which thing happened first.”

Outside, a maintained path bends through the settlement greenery. Farther off, islands carry forests, lakes and snow above the cloud sea. The view promises a much larger field of work than this table, but the table offers somewhere sensible to begin.

She moves the contaminated cup away from the notes.

“We can compare them here, or take a properly arranged short observation walk. Tell me what you want to study—and whether you've already eaten. People make very creative conclusions when they haven't.”''')]

def add_starts(w):
    entries={}
    for name,place,area,npc,quest,description,prose in STARTS:
        fullarea=place+' - '+area
        if fullarea not in w['locations'][place]['areas']:raise ValueError(fullarea)
        opening=f'[Begin at {fullarea}. Present the authored {npc}; use actual records, chosen appearance, training and possessions. This start does not prescribe ancestry, gender, a weapon, powerful mastery, an existing romance or party recruitment. Establish the scene and stop before the player’s meaningful reply or acceptance. Existing starting money is supplied only through startingItems.]\n\n'+prose
        entries[name]={'name':name,'description':description,'storyStart':opening,'locations':[place],'locationAreas':[fullarea],'startingQuests':([quest] if quest else []),'startingItems':[{'item':'Mark','quantity':1000}],'startingPartyNPCs':[],'isDefault':False,'questGenerationGuidance':'Begin with the actual local scene and the player’s chosen interest. Use the established cast, ordinary services and existing optional undertakings before inventing replacements. The first useful action can be practical, social, martial or magical. Respect refusal, actual training, real payment and a completed outcome. Travel to another realm is an explicit choice with actual permission, not an automatic introduction.'}
    out={};inserted=False
    for key,v in w['storyStarts'].items():
        if not inserted and 'First Day of Work:' in key:
            out.update(entries);inserted=True
        out[key]=v
    if not inserted:raise ValueError('Academy work insertion anchor missing')
    w['storyStarts']=out
    return list(entries)
