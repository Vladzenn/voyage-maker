"""Specific reviewed branch repairs plus the explicitly requested paced pursuit."""
import copy,json
import update
w=update.load(update.WORLD);t=w['triggerDefinitions'];q=w['parties']['']['quests']
assert 'rb_peaceful_departure' not in t,'Story changes already applied'
def cond(kind,value,**kw):return dict(type=kind,operator='equals',value=value,**kw)
def flag(key):return dict(type='write-boolean',operator='set',value=True,key=key)
def story(text):return dict(type='story',instruction=text)
# A genuine resolved peaceful departure is an outcome, not forced intervention.
t['rb_peaceful_departure']=dict(name='rb_peaceful_departure',scope='party',recurring=False,
 conditions=[cond('read-number',1,key='rbPhase'),dict(type='npc-health',operator='greaterThan',value=0,npc='Kazunari Shiba'),
 dict(type='story',query="Kazunari Shiba's delegation has genuinely concluded its local inquiry and peacefully withdrawn or departed after an actual diplomatic resolution. The inquiry is no longer continuing in the scene. A proposal, promise to leave, player leaving alone, or merely hiding from the delegation is false. Vladimir need not appear; preserve the real terms and witnesses.")],
 effects=[dict(type='write-number',operator='set',value=3,key='rbPhase'),dict(type='npc-placement',npc='Kazunari Shiba',operation='moveAway'),story("Preserve the peacefully concluded inquiry and the actual diplomatic terms. Do not insert Vladimir into a meeting he did not attend. Reika Kurose's existing records-and-witnesses route remains available; do not grant evidence or identify the summoned person merely because the visitors left.")])
t['rb_intervention']['conditions'][-1]['query']="Kazunari Shiba's delegation is present and currently conducting intrusive questioning in a calm Glowhaven town scene; that inquiry has not already been peacefully concluded or withdrawn. A brief public intervention can occur without overriding a player action, fight or urgent task."
# Shared guarded offer owners avoid assuming native quest-init idempotence.
targets={'The Carrier behind the Ledger':'rbCarrierLead','At the Wandering Door':'rbAudienceLead'}
for key in ['A Name in the Shore Ledger','The Carrier behind the Ledger']:
 q[key]['onCompleteEffects']=[flag(targets[e['value']]) if e.get('type')=='quest-init' and e.get('value') in targets else e for e in q[key]['onCompleteEffects']]
af=t['rb_interception_aftermath']
af['effects']=[flag(targets[e['value']]) if e.get('type')=='quest-init' and e.get('value') in targets else e for e in af['effects']]
af['script']+="\nstorage.rbHuntLastResolvedTick=Number(check({type:'game-tick'}))||0;"
for quest,key in targets.items():
 name='rb_offer_carrier_once' if key=='rbCarrierLead' else 'rb_offer_audience_once'
 t[name]=dict(name=name,scope='party',recurring=True,conditions=[cond('read-boolean',True,key=key),cond('quest-status','planned',questId=quest)],effects=[dict(type='quest-init',operator='set',value=quest)])
# Add a genuine trace alternative; private thoughts or unreceived records remain
# insufficient, and per-reader native effects still mark only qualifying people.
t['rb_personal_lead']['conditions'][-1]['query']="A real witness or copied shore record, or a mana sample actually observed or collected by an agent and delivered for comparison, has given the intermediary a corroborated identity and current whereabouts for this Summoned one. A cast spell somewhere, private confession, false report, protected sample, unreceived message or guess alone is insufficient. The actual traced bearer must be the qualifying person."
clock=(update.HERE/'pursuit-clock.js').read_text(encoding='utf-8')
t['rb_clock']['script']+='\n'+clock
t['rb_pursuit_attempt']=dict(name='rb_pursuit_attempt',scope='party',recurring=True,
 conditions=[cond('read-boolean',True,key='rbHuntDue'),cond('read-boolean',False,key='rbHuntActive'),cond('read-boolean',False,key='arReceivingConcluded'),
 dict(type='story',query="The specifically traced Summoned one is personally present and free for a new retrieval encounter. A recent usable mana trail and a real permitted or covert route let finite agents reach this actual place. No active fight, urgent expedition hazard, championship bout, compulsory lesson, arrest/custody, private protected sanctuary or major scripted scene is underway. No already active pursuit encounter is being duplicated. Concealment, a lost trail or inaccessible route postpones it. Prepare a fair readable approach, not automatic capture.")],
 effects=[],script=(update.HERE/'pursuit-dispatch.js').read_text(encoding='utf-8'))
t['rb_pursuit_resolved']=dict(name='rb_pursuit_resolved',scope='party',recurring=True,
 conditions=[cond('read-boolean',True,key='rbHuntActive'),dict(type='story',query="The actual current Ardelian pursuit encounter recorded for its traced target has genuinely ended: agents were defeated, departed after a real settlement, lost the trail through effective escape or concealment, or completed a capture with no active pursuit fight remaining. Keep actual captivity, injuries and surviving agents. An intention, unrelated fight, merely stepping into another room or declaring victory during ongoing danger is false.")],
 effects=[dict(type='write-boolean',operator='set',value=False,key='rbHuntActive')],
 script="const tick=Number(check({type:'game-tick'}))||0;const c=storage.rbHuntCase;if(!c){skip=true;}else{storage.rbHuntLastResolvedTick=tick;const row=storage.rbHuntByName?.[c.target];if(row)row.next=tick+100;storage.rbLastHuntCase={...c,resolved:tick};storage.rbHuntCase=null;storage.rbHuntDue=false;}")
for name,description in {
 'Ardelian Trace Construct':"A finite human-sized tracking construct sent only for an established Ardelian retrieval attempt. It follows a recent sampled mana signature, not omniscient identity or private thoughts. Use the dispatch's target-based native level band, average tier and modest bonuses; a helper is weaker. It can lose a trail, be deceived, disabled or escaped. A new instance never resurrects a dead named courier. Its warning gestures and finite capture tools allow actual contested action.",
 'Ardelian Retrieval Proxy':"A finite disguised retrieval construct with a ward-net, short restraint tool and a local command regulator. It knows only its supplied trace, route and capture assignment, with no automatic reporting link. Use the actual dispatch level band capped at 45 and no more than one weaker helper; no elite bonus or unlimited spell resistance. Later attempts may use preparation, decoys or coordinated approaches without inventing extra enemies. Ordinary people are not automatically exposed as proxies."}.items():
 w['npcTypes'][name]=dict(name=name,description=description,vulnerabilities=[],resistances=[],immunities=[])
w['worldLore']['Ardelis — Mana Traces and Recurring Pursuit']={'text':(update.HERE/'pursuit-lore.txt').read_text(encoding='utf-8').strip()}
q['Rebirth: What the Crown Received']['questDesignBrief']+=' This concludes the receiving-operation pursuit. Preserve the actual settlement and stop new retrieval teams; any already active danger still needs its real resolution.'
update.write(update.WORLD,w);update.proof(w)
update.write(update.HERE/'story-fixes.json',dict(peacefulDeparture=True,guardedOffers=list(targets),pursuitMinimumTicks=100,primaryCap=45,supportCap=35,maxOpponents=2,unchanged=['portal anomaly','party-wide diadem','native semantic chapter completion']))
print(json.dumps({'storyRepairs':2,'recurringPursuit':True,'minimumInterval':100,'addedTriggers':5,'addedTypes':2}))
