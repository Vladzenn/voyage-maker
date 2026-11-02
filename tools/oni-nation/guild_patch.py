"""Targeted live-playtest repair: bind acceptance to one currently displayed contract."""
import json,re,copy

CHOICE_JS=r'''
const choiceRaw=check({type:'action-text'}),choiceText=(Array.isArray(choiceRaw)?choiceRaw.join(' '):String(choiceRaw||'')).toLowerCase();
const choiceOffers=Array.isArray(storage.ghGuildDisplayedOffers)?storage.ghGuildDisplayedOffers:[];
const choiceCommit=/\b(accept|take|choose|agree|yes|okay|alright|deal)\b/.test(choiceText)&&!/\b(don't|do not|won't|will not|decline|reject|no thanks)\b/.test(choiceText);
const choiceStop=new Set('guild akitsuhara a an the of to for and in at on is with without after from its this that one'.split(' '));
const choiceWords=t=>t.toLowerCase().match(/[a-zéōū]+/g)?.filter(t=>t.length>2&&!choiceStop.has(t)).map(t=>t.length>3?t.replace(/s$/,''):t)||[];
const actionWords=new Set(choiceWords(choiceText));
const scores=choiceOffers.map(title=>({title,score:choiceWords(title).filter(t=>actionWords.has(t)).length}));
const best=Math.max(0,...scores.map(x=>x.score)),matches=scores.filter(x=>x.score===best&&best>0);
const chosen=choiceCommit?(matches.length===1?matches[0].title:(!best&&choiceOffers.length===1?choiceOffers[0]:'')):'';
'''
BROWSE_GATE_JS=CHOICE_JS.split('const choiceStop=')[0]

def apply(w):
    changed=[];legacy={}
    for key,tr in w['triggerDefinitions'].items():
        flag=next((c.get('key') for c in tr.get('conditions',[]) if c['type']=='read-boolean' and c.get('key','').startswith('q20_offered_')),None)
        courier=key.startswith('gh_guild_accept_courier_')
        if not courier and (not flag or not key.endswith('_accept')):continue
        title=next((e['value'] for e in tr['effects'] if e['type'] in ['quest-init','quest-accept']),None)
        if not title:continue
        if not any(c['type']=='party-location' and c.get('value')=="Adventurer's Guild - Glowhaven Branch" for c in tr['conditions']):continue
        old=tr.get('script','')
        tr['script']=CHOICE_JS+'\nif(chosen!=='+json.dumps(title)+'){skip=true;}else{\n'+old+'\n}'
        changed.append(key);legacy.setdefault(title,key)
    board=w['triggerDefinitions']['gh_guild_board'];script=board['script']
    match=re.search(r'const jobs=(\[.*?\]);\s*\n',script,re.S)
    if not match:raise ValueError('Existing board catalog not recognized')
    jobs=json.loads(match.group(1));compact=[]
    for j in jobs:
        q=w['parties']['']['quests'][j['title']]
        # Use the actual public terms, never an invented client/price in narration.
        text=q.get('questStatement','')+' '+q.get('questDesignBrief','')
        fees=re.findall(r'(?:PostedReward\s*:\s*|[Pp]osted reward\s*:\s*|[Pp]osted fee\s*:?\s*)(\d+)',text)
        if not fees:
            fees=re.findall(r'(\d+) marks',q.get('questStatement',''))
        fee=int(fees[0]) if fees else 'as posted'
        compact.append([j['title'],j['rank'],j.get('slug',''),j.get('repeatable',False),j.get('recommendedLevel',1),j.get('lane','other'),j.get('band',1),q.get('questSource','the actual client'),q.get('questLocation','the stated site'),fee])
    table='const jobs='+json.dumps(compact,ensure_ascii=False,separators=(',',':'))+'.map(([title,rank,slug,repeatable,recommendedLevel,lane,band,client,place,fee])=>({title,rank,slug,repeatable,recommendedLevel,lane,band,client,place,fee}));\n'
    script=script[:match.start()]+table+script[match.end():]
    script=script.replace('storage.q20_board_cursor=cursor+2;','storage.q20_board_cursor=cursor+2;\n storage.ghGuildDisplayedOffers=picked.map(j=>j.title);\n storage.ghGuildOfferRanks=Object.fromEntries(picked.map(j=>[j.title,j.rank]));')
    old="j.title+' (recommended level '+j.recommendedLevel+'+)'"
    new="j.title+' — '+j.client+'; '+j.place+'; '+j.fee+' marks (recommended level '+j.recommendedLevel+'+)'"
    if old not in script:raise ValueError('Board terms insertion anchor')
    script=script.replace(old,new)
    # An acceptance turn must not rotate the current two choices before they can be resolved.
    script=BROWSE_GATE_JS+'\nif(choiceCommit&&choiceOffers.length){skip=true;}else{\n'+script+'\n}'
    board['script']=script;changed.append('gh_guild_board')
    return {'changedTriggers':changed,'legacyAcceptances':legacy}

def add_native_choice(w,legacy):
    name='oni_guild_native_choice'
    script=CHOICE_JS+"\nconst legacy="+json.dumps(list(legacy),ensure_ascii=False,separators=(',',':'))+r''';
if(!chosen||legacy.includes(chosen)){skip=true;}else{
 const status=check({type:'quest-status',questId:chosen});
 const required=Number((storage.ghGuildOfferRanks||{})[chosen]||1);
 let held=0;for(let i=1;i<=4;i++){const v=check({type:'player-item',item:'Guild Badge: '+['','Bronze','Silver','Gold','Platinum'][i]})||{};if(Object.values(typeof v==='object'?v:{player:v}).some(x=>Number(x)>0))held=Math.max(held,i);}
 if(held<required||!['hidden','planned','available','inactive','unstarted',''].includes(String(status||''))){skip=true;}else{
  effects.push({type:'quest-accept',operator:'set',value:chosen},{type:'story',instruction:'Record acceptance of only '+chosen+'. Preserve that existing contract’s exact client, site, scope and posted reward. Do not replace its people, create a second contract item, accept the other displayed choice or award completion rewards now.'});
 }
}
'''
    w['triggerDefinitions'][name]={'name':name,'phase':'state','recurring':True,'conditions':[{'type':'party-location','operator':'regex','value':"^(Adventurer's Guild - Glowhaven Branch|Adventurer's Guild - Benitsuru Branch)$"},{'type':'action','query':'The player actually accepts one of the currently displayed guild contracts. Browsing, asking for details, exam examples, accepting a different undertaking or an unclear yes to multiple choices is false.'}],'effects':[],'script':script}
    return name
