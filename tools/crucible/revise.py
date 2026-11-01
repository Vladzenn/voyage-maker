"""Overlay the approved v2 tournament card on an explicit current Studio export."""
import argparse,copy,hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--source',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
w=json.loads(a.source.read_text(encoding='utf-8-sig'));before=copy.deepcopy(w)
m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'))
assert all(k in w['triggerDefinitions'] for k in ['cc1_register','cc1_grove_inner_gate'])
roster=[dict(x,level=w['npcs'][x['name']]['level']) for x in m['roster']]
def write(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def c(t,v,op='equals',**kw):return dict(type=t,operator=op,value=v,**kw)
def js(*files,replacements=None):
 s='\n'.join((HERE/'card-v2'/f'{f}.js').read_text(encoding='utf-8') for f in files)
 s=s.replace('ROSTER',json.dumps(roster,ensure_ascii=False,separators=(',',':'))).replace('RINGS',json.dumps(m['rings'],ensure_ascii=False,separators=(',',':')))
 for key,value in (replacements or {}).items():s=s.replace(key,json.dumps(value,ensure_ascii=False))
 return '\n'.join(x.strip() for x in s.splitlines() if x.strip() and not x.lstrip().startswith('//'))
def emit(key,conds,files=(),phase=None,scope=None,replacements=None,script=None):
 body=script if script is not None else js('base',*files,replacements=replacements)
 if script is None and key!='cc1_initialize':
  base=js('base');body=base+'\nif(c.v!==2){skip=true;}else{\n'+body[len(base)+1:]+'\n}'
 t=dict(name=key,recurring=True,conditions=conds,effects=[],script=body)
 if phase:t['phase']=phase
 if scope:t['scope']=scope
 assert len(json.dumps(t,ensure_ascii=False,separators=(',',':')).encode('utf-16-le'))//2<=10000,(key,'trigger size')
 w['triggerDefinitions'][key]=t
at=c('party-location','The Eternal Crucible');phase=lambda s:c('read-string',s,'regex',key='cc1_phase');action=lambda q:dict(type='action',query=q)
emit('cc1_initialize',[c('game-tick',0,'greaterThan')],['initialize'],phase='planning')
emit('cc1_register',[at,phase('^(idle|closed)$'),action('The player explicitly registers now for the announced Crucible individual championship after learning its actual scheduled card, rules and prize. Asking, spectating, discussing a future entry or accepting a friendly spar is false.')],['register'],scope='player')
emit('cc1_ready',[at,phase('^waiting$'),action('The registered fighter explicitly agrees to START their currently called Crucible bout now. Conversation, spectating or movement alone does not start it. Care is optional; no full-resource requirement.')],['finish','ready'],scope='player')
emit('cc1_observe',[phase('^(waiting|live)$')],['finish','observe'],phase='planning')
for suffix,winner,reason,q in [
 ('loss','opponent','official player surrender or stoppage','The latest actual scene settles the registered player\'s exact currently STARTED Crucible bout as their loss: surrender, referee/medical stoppage, ring-out or disqualification. A previous bout, spectator fight, hypothetical, merely sitting in the stands between bouts or another contestant losing is false.'),
 ('win','player','official opponent surrender or stoppage','The latest actual scene settles the registered player\'s exact currently STARTED Crucible bout as their win: the announced opponent actually yields or loses under the rules. A boast, recap, watched NPC fight, dead summon, pre-start incapacity or an unresolved scene is false.')]:
 emit('cc1_result_'+suffix,[phase('^live$'),dict(type='story',query=q)],['finish','result'],scope='player',replacements={'RESULT_WINNER':winner,'RESULT_REASON':reason})
emit('cc1_withdraw',[phase('^(waiting|live)$'),action('The registered fighter explicitly FORFEITS or cancels their championship/exhibition ENTRY. This must be an actual decision to stop competing. Mere movement, spectating, a question or another person leaving is false.')],['finish','withdraw'],scope='player')
for key,file,conds in [
 ('cc1_care','care',[at,phase('^(waiting|closed)$'),c('read-boolean',True,key='cc1_care'),dict(type='story',query='After the recorded Crucible bout or stoppage the entrant actually accepts appropriate care, a check-up or recovery rest. An offer/refusal alone, another person\'s treatment or an old scene is false. Unharmed people need no invented wounds.')]),
 ('cc1_claim_prize','claim',[at,phase('^(waiting|closed)$'),c('read-boolean',True,key='cc1_due'),action('The actual recorded champion explicitly collects their owed uncollected Crucible prize now. A boast, another person\'s award, buying a trophy, a practice win or an already paid edition is false.')])]:
 # These two existing owner-scoped dispatches remain the same implementation.
 original=(HERE/f'{file}.js').read_text(encoding='utf-8')
 emit(key,conds,scope='player',script=js('base')+'\nif(c.v!==2){skip=true;}else{\n'+original+'\n}')
emit('cc1_status',[c('action-text','^[Cc]rucible status[.!]?$','regex')],['status'])
emit('cc1_exhibition',[at,phase('^(idle|closed)$'),action('The player and an actually available named willing fighter explicitly agree to a friendly nonlethal Crucible match now. Talking about a possible match, watching, coercing someone, or championship registration is false.')],['exhibition'],scope='player')
w['triggerDefinitions'].pop('cc1_review',None)

# One route script, run before narration and again as a position-only state backstop.
g=[c('party-realm','The Sepulchral Conservatory')]
emit('cc1_grove_inner_gate',g,phase='planning',script=js('guard'))
emit('cc1_grove_inner_gate_state',g,phase='state',script='const statePass=true;\n'+js('guard'))

new_hidden='CRUCIBLE ACTIVITY: Follow the entrant\'s announced opponents. Start only the called bout after explicit agreement and actual capacity. A real started bout ends through knockout, surrender, ring-out or referee ruling. Both down eliminates both and brings appropriate care. An unavailable pre-start opponent is replaced or the card is cancelled, never counted as a combat win. Withdrawal means an explicit forfeit of the entry; ordinary movement and spectating do not change its status. Other matches, conversation and recovery are narrative. Care is optional and unharmed people need no invented injury or full bars. Finite summons are legal; outside attacks, buffs and healing are banned. Preserve recorded results and one prize owner. Discussing fighting does not start a match.'
loc=w['locations']['The Eternal Crucible'];loc['hiddenInfo']=re.sub(r'CRUCIBLE ACTIVITY:.*?Discussing fighting does not start a match\.',lambda _:new_hidden,loc['hiddenInfo'],count=1,flags=re.S)
assert new_hidden in loc['hiddenInfo']
w['aiInstructions']['generateStory']['Crucible Activity']='Crucible: register, agree to start the called bout, resolve that actual fight, then next bout or finish. Conversation, spectating and recovery remain narrative. Withdrawal requires explicitly forfeiting the entry; movement alone is not withdrawal. A started fight can end through surrender, knockout, ring-out or referee ruling. Both down eliminates both and brings appropriate care. Unavailable pre-start opponents are replaced or the card cancelled, never a combat win. No invented injuries, full-bar gate, extra final or duplicate prize. Finite summons are legal; outside interference is not.'
w['aiInstructions']['generateActionInfo']['Crucible Intent']='Crucible: explicit readiness starts the called bout; explicit forfeiting cancels entry. Movement/spectating alone does neither. A real started fight has real surrender, knockout and referee outcomes. Both down eliminates both; no full-bar gate. Conservatory: an unreleased inner lattice stops heart/boss entry at the actual safe area; an attack through it cannot succeed.'
w['aiInstructions']['generateNPCIntents']['Crucible Sporting Intent']='Only an actually started Crucible bout authorizes its entrants and finite legal summons to fight. Waiting in stands, clinic or lounge is not combat or outside interference. Stop immediately on surrender, incapacity, ring-out or referee ruling; no queued extra attack after a result. No compulsory injury or lethal intent. Simultaneous knockout eliminates both from title contention and medics offer appropriate care. Other NPC matches may be narrated without rewriting the registered entrant\'s card.'
key='The Crucible — Cups and Competitor Life';text=w['worldLore'][key]['text'];text=text.split('\n\nChampionship format:')[0]
w['worldLore'][key]['text']=text+'\n\nChampionship format: Officials announce scheduled opponents and arenas. Entrants can watch, rest or socialize until ready for a called bout. An unavailable opponent is replaced or the remaining card cancelled; no unplayed combat win is awarded. A simultaneous knockout eliminates both from title contention. Voluntary withdrawal means explicitly forfeiting the entry. Mere movement is not withdrawal; an actual started fight can still end through a referee\'s ruling.'

# Preserve incoming authored records and media exactly; update the baseline to this Studio export.
m['controllerVersion']=2;m['mergeSourceSHA256']=hashlib.sha256(a.source.read_bytes()).hexdigest();m['sourceAttachment']='eefdd39e-e77a-4b8e-b870-5216d4c9022a'
m['roster']=roster;m['triggers']=[k for k in w['triggerDefinitions'] if k.startswith('cc1_')]
m['preserved']['npcs']={k:digest(v) for k,v in before['npcs'].items()};m['preserved']['originalItems']={k:digest(v) for k,v in before['itemTypes'].items()};m['preserved']['originalAbilities']={k:digest(v) for k,v in before['abilities'].items()}
m['preserved']['spider']={s:{k:digest(before[s][k]) for k in old} for s,old in m['preserved']['spider'].items()}
allowed={'triggerDefinitions','aiInstructions','locations','worldLore'}
for key in before:
 if key not in allowed:assert w[key]==before[key],key
for key,value in before['locations'].items():
 if key!='The Eternal Crucible':assert value==w['locations'][key],key
assert {k:v for k,v in loc.items() if k!='hiddenInfo'}=={k:v for k,v in before['locations']['The Eternal Crucible'].items() if k!='hiddenInfo'}
for key,value in before['triggerDefinitions'].items():
 if not key.startswith('cc1_'):assert value==w['triggerDefinitions'][key],key
write(a.output,w);write(HERE/'manifest.json',m)
write(HERE/'revision-preservation.json',{'sourceAttachment':m['sourceAttachment'],'sourceSHA256':m['mergeSourceSHA256'],'controllerVersion':2,'unchangedSections':{k:digest(before[k]) for k in sorted(set(before)-allowed)},'unchangedLocations':{k:digest(v if k!='The Eternal Crucible' else {a:b for a,b in v.items() if a!='hiddenInfo'}) for k,v in before['locations'].items()},'allNPCsItemsAbilitiesUnchanged':True,'userMapAndCoordinatesPreserved':True,'changedTriggers':[k for k in w['triggerDefinitions'] if before['triggerDefinitions'].get(k)!=w['triggerDefinitions'][k]],'removedTriggers':['cc1_review']})
print(json.dumps({'candidate':str(a.output),'controller':2,'triggers':len(w['triggerDefinitions']),'cards':len(w['npcs']),'preservedUserMap':True}))
