"""Merge the approved cast/portrait revisions and minimal bracket onto the current world."""
import argparse,copy,hashlib,json,pathlib,re
from cast_polish import apply
ROOT=pathlib.Path(__file__).resolve().parents[2];HERE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--source',type=pathlib.Path,required=True);p.add_argument('--npcs',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
w=json.loads(a.source.read_text(encoding='utf-8-sig'));before=copy.deepcopy(w);incoming=json.loads(a.npcs.read_text(encoding='utf-8-sig'));incoming=incoming.get('npcs',incoming)
cast_report=apply(w,incoming);m=json.loads((HERE/'manifest.json').read_text(encoding='utf-8'));roster=[dict(x,level=w['npcs'][x['name']]['level']) for x in m['roster']]
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def js(*files,replacements=None):
 s='\n'.join((HERE/'bracket-v3'/f'{f}.js').read_text(encoding='utf-8') for f in files)
 s=s.replace('ROSTER',json.dumps([[x['name'],x['level']] for x in roster],ensure_ascii=False,separators=(',',':'))).replace('RINGS',json.dumps(m['rings'],ensure_ascii=False,separators=(',',':')))
 for k,v in (replacements or {}).items():s=s.replace(k,json.dumps(v,ensure_ascii=False))
 return '\n'.join(x.strip() for x in s.splitlines() if x.strip() and not x.lstrip().startswith('//'))
def emit(key,conditions,files,phase=None,scope=None,replacements=None,raw=None):
 base=js('base');body=raw if raw is not None else js('base',*files,replacements=replacements)
 if key!='cc1_initialize':body=base+'\nif(c.v!==3){skip=true;}else{\n'+body[len(base)+1:]+'\n}'
 t=dict(name=key,recurring=True,conditions=conditions,effects=[],script=body)
 if phase:t['phase']=phase
 if scope:t['scope']=scope
 size=len(json.dumps(t,ensure_ascii=False,separators=(',',':')).encode('utf-16-le'))//2
 assert size<=10000,(key,size)
 w['triggerDefinitions'][key]=t
def cond(t,v,op='equals',**kw):return dict(type=t,operator=op,value=v,**kw)
at=cond('party-location','The Eternal Crucible');phase=lambda v:cond('read-string',v,'regex',key='cc1_phase');action=lambda q:dict(type='action',query=q)
emit('cc1_initialize',[cond('game-tick',0,'greaterThan')],['initialize'],phase='planning')
emit('cc1_register',[at,phase('^(idle|closed)$'),action('The player explicitly registers now for the announced Crucible championship after hearing the rules and prize. A question, future intention, spectating or friendly spar is false.')],['bracket','register'],scope='player')
emit('cc1_ready',[at,phase('^waiting$'),action('The registered fighter explicitly agrees to START the currently called bout now. Conversation, spectating and movement alone are false; full resources are not required.')],['bracket','finish','ready'],scope='player')
emit('cc1_observe',[phase('^(waiting|live)$')],['bracket','finish','observe'],phase='planning')
for suffix,winner,q in [
 ('draw','draw','The referee explicitly rules the exact currently STARTED Crucible bout a simultaneous knockout or double elimination: BOTH registered fighters are eliminated. This can be reported after they are moved for treatment. An unrelated injury, hypothetical, old match, ordinary loss by one fighter or watched match is false.'),
 ('loss','opponent','The latest actual scene has an official ruling that ONLY the registered entrant LOST the exact currently STARTED Crucible bout: surrender, ring-out, disqualification or referee/medical stoppage. Both eliminated/double knockout, mere movement, a hypothetical, another fight, a recap, or unrelated illness/injury elsewhere is false.'),
 ('win','player','The latest actual scene has an official ruling that ONLY the called opponent LOST the exact currently STARTED Crucible bout. The entrant wins because that opponent yields, is defeated in this bout, or loses under its rules. Both eliminated/double knockout, a boast, recap, unrelated incapacity outside the bout, pre-start incapacity or another fight is false.')]:
 emit('cc1_result_'+suffix,[phase('^live$'),dict(type='story',query=q)],['bracket','finish','result'],scope='player',replacements={'RESULT_WINNER':winner,'RESULT_REASON':'official simultaneous knockout' if winner=='draw' else 'official '+('opponent' if winner=='player' else 'entrant')+' surrender or referee ruling'})
emit('cc1_withdraw',[phase('^(waiting|live)$'),action('The registered fighter explicitly FORFEITS or cancels the ENTRY. It is an actual decision to stop competing; ordinary movement, spectating, a question or somebody else leaving is false.')],['bracket','finish','withdraw'],scope='player')
for key,file,conditions in [
 ('cc1_care','care',[at,phase('^(waiting|closed)$'),cond('read-boolean',True,key='cc1_care'),dict(type='story',query='The registered entrant accepts appropriate post-bout care, a check-up or rest now. An offer alone, old scene or another person’s treatment is false. Unharmed people need no invented injury.')]),
 ('cc1_claim_prize','claim',[at,phase('^(waiting|closed)$'),cond('read-boolean',True,key='cc1_due'),action('The actual champion collects the recorded owed uncollected prize now. Another person’s prize, practice win, purchased trophy or an already paid edition is false.')])]:
 emit(key,conditions,[],scope='player',raw=js('base')+'\n'+(HERE/f'{file}.js').read_text(encoding='utf-8'))
emit('cc1_status',[cond('action-text','^[Cc]rucible status[.!]?$','regex')],['status'])
emit('cc1_exhibition',[at,phase('^(idle|closed)$'),action('The player and an available named willing fighter agree to a friendly nonlethal match now. Merely asking, coercion, watching or championship registration is false.')],['exhibition'],scope='player')
guide='Crucible championships use a recorded four- or eight-entrant elimination bracket. Explicit registration and readiness start the entry and called bout. NPC-only bouts receive one abstract official result; established levels remain unchanged and unfit entrants cannot win a new simulated match. Record the eventual champion even after a player loss. Real started bouts end by knockout, surrender, ring-out or referee ruling. Native knockout checks require both participants in the assigned arena; after an interruption use the actual referee ruling, never unrelated injury elsewhere. Mere movement does not forfeit. Voluntary withdrawal requires explicit forfeiting. No invented injuries, full-bar gate, duplicate prizes or extra finals. Finite summons are legal; outside interference is not. Controlled bouts are solo-only; a second human suspends control without cancelling the entry or transferring it.'
w['aiInstructions']['generateStory']['Crucible Activity']=guide
w['aiInstructions']['generateActionInfo']['Crucible Intent']='Explicit readiness opens the called official bout; explicit forfeiting ends entry. Movement alone does neither. A referee’s ruling can settle a real interruption; an unrelated fall in the lounge cannot. Other NPC bracket outcomes are already recorded; describe them faithfully. Multiplayer suspends the controlled activity until solo again. Conservatory: the unreleased lattice still stops early heart entry.'
w['aiInstructions']['generateNPCIntents']['Crucible Sporting Intent']='Only the exact started bout authorizes its fighters and finite legal summons to attack. Stop on the official result; no extra queued attacks. Outside companions cannot attack, buff or heal a contestant. Both down eliminates both. Referee rulings settle interruptions; unrelated injury is not a match result. NPC-only bracket outcomes are abstract official results, not orders to stage unsupervised combat. A second human suspends controlled bouts.'
loc=w['locations']['The Eternal Crucible'];loc['hiddenInfo']=loc['hiddenInfo'].split('CRUCIBLE ACTIVITY:')[0]+'CRUCIBLE ACTIVITY: '+guide
key='The Crucible — Cups and Competitor Life';w['worldLore'][key]['text']=w['worldLore'][key]['text'].split('\n\nChampionship format:')[0]+'\n\nChampionship format: Four or eight entrants compete in single elimination, with semifinals and a final. The announced field keeps its actual strengths. A defeated entrant may watch the rest of the competition and learn who became champion. Officials stop a bout for surrender, incapacity, ring-out or infringement. Both contestants are eliminated after a simultaneous knockout. Competitors can converse, watch or rest between called bouts; withdrawing means explicitly forfeiting the entry.'
m['controllerVersion']=3;m['roster']=roster;m['triggers']=[k for k in w['triggerDefinitions'] if k.startswith('cc1_')];m['npcMergeSource']=str(a.npcs);m['npcMergeSHA256']=hashlib.sha256(a.npcs.read_bytes()).hexdigest()
m['preserved']['npcs']={k:digest(v) for k,v in incoming.items() if k not in m['npcs']}
public={'basicInfo','hiddenInfo','personality','abilities','visualDescription','portraitUrl'}
m['preserved']['revisedNPCIdentity']={k:digest({f:v for f,v in incoming[k].items() if f not in public}) for k in m['npcs']}
allowed={'triggerDefinitions','aiInstructions','locations','worldLore','npcs'}
for k in before:
 if k not in allowed:assert w[k]==before[k],k
for k,v in before['locations'].items():
 if k!='The Eternal Crucible':assert w['locations'][k]==v,k
for k,v in before['triggerDefinitions'].items():
 if not k.startswith('cc1_'):assert w['triggerDefinitions'][k]==v,k
write(a.output,w);write(HERE/'manifest.json',m);write(HERE/'cast-polish-report.json',cast_report)
write(HERE/'revision-preservation.json',{'controllerVersion':3,'unchangedSections':{k:digest(before[k]) for k in set(before)-allowed},'unchangedLocations':{k:digest(v if k!='The Eternal Crucible' else {a:b for a,b in v.items() if a!='hiddenInfo'}) for k,v in before['locations'].items()},'userMapAndCoordinatesPreserved':True,'newPortraitsExplicitlySelected':m['npcs']})
print(json.dumps({'candidate':str(a.output),'controller':3,'castRewritten':len(cast_report['rewritten']),'rootTriggers':len(w['triggerDefinitions'])}))
