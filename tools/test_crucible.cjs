// Actual emitted scripts with explicit semantic fixtures. Not a live Voyage playtest.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const root=path.resolve(__dirname,'..'),w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft','WorldAlpha - World.json'),'utf8'));
const manifest=JSON.parse(fs.readFileSync(path.join(root,'tools','crucible','manifest.json'),'utf8'));
let checks=0;function ck(v,s){checks++;assert.ok(v,s)}
function cmp(a,op,b){if(op==='regex')return new RegExp(b).test(a);return {equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b}[op]}
function harness(level=20){
 const s={tick:1,location:'The Eternal Crucible',area:'The Eternal Crucible - Competitor Passage',players:{Player:level},hp:{Player:100},items:{Player:{}},storage:{},npcs:{},said:[],grants:[],action:['I register for the championship.']};
 for(const [name,n] of Object.entries(w.npcs))s.npcs[name]={hp:100,location:n.currentLocation,area:n.currentArea,combat:false,party:false};
 function raw(c){
  if(c.type==='game-tick')return s.tick;
  if(c.type==='party-location')return s.location;
  if(c.type==='party-area')return s.area;
  if(c.type==='party-realm')return w.regions[w.locations[s.location].region].realm;
  if(c.type==='player-level')return s.players;
  if(c.type==='player-resource')return Object.fromEntries(Object.keys(s.players).map(n=>[n,c.resource==='Health'?s.hp[n]:100]));
  if(c.type==='action-text')return s.action;
  if(c.type==='story-text')return s.story||'';
  if(c.type==='player-item')return Object.fromEntries(Object.keys(s.players).map(n=>[n,s.items[n]?.[c.item]||0]));
  if(c.type.startsWith('read-'))return s.storage[c.key]??(c.type==='read-boolean'?false:c.type==='read-string'?'':0);
  if(c.type==='npc-health')return s.npcs[c.npc]?.hp;
  if(c.type==='npc-relationship')return s.npcs[c.npc]?.relationship??-75;
  if(c.type==='npc-in-party')return s.npcs[c.npc]?.party??false;
  if(c.type==='npc-in-combat')return s.npcs[c.npc]?.combat??false;
  if(c.type==='npc-in-scene')return s.npcs[c.npc]?.location===s.location&&s.npcs[c.npc]?.area===s.area;
  if(c.type==='npc-location')return s.npcs[c.npc]?.location;
  if(c.type==='npc-area')return s.npcs[c.npc]?.area;
  throw Error('Unimplemented check '+JSON.stringify(c));
 }
 function check(c){const a=raw(c);if(!c.operator)return a;if(c.type.startsWith('player-'))return Object.values(a).some(x=>cmp(x,c.operator,c.value));return cmp(a,c.operator,c.value)}
 function qualifies(t,semantic){
  if(t.scope==='player'){
   const cs=t.conditions.filter(c=>c.type.startsWith('player-'));
   if(cs.length&&!Object.keys(s.players).some(n=>cs.every(c=>cmp(raw(c)[n],c.operator,c.value))))return false;
  }
  return t.conditions.every(c=>{
   if(['story','action'].includes(c.type))return semantic===true;
   if(c.type==='player-item')return Object.values(s.items).some(b=>cmp(b[c.item]||0,c.operator,c.value));
   if(c.type==='quest-status')return cmp('hidden',c.operator,c.value);
   return check(c);
 })}
 function run(name,semantic=true){
  const t=w.triggerDefinitions[name];ck(!!t,'Actual trigger exists '+name);if(!qualifies(t,semantic))return false;
  const ctx={check,storage:s.storage,effects:structuredClone(t.effects),skip:false};
  vm.runInNewContext(t.script||'',ctx,{timeout:500});if(ctx.skip)return false;
  for(const e of ctx.effects){
   if(e.type==='story')s.said.push(e.instruction);
   else if(e.type==='party-area')s.area=e.value;
   else if(e.type==='party-location'){s.location=e.value;s.area=Object.keys(w.locations[e.value].areas)[0]}
   else if(e.type==='npc-placement'){
    if(e.npc==='allPartyNPCs'){for(const n of Object.values(s.npcs))if(n.party){n.location=e.location;n.area=e.area}continue;}
    ck(!!s.npcs[e.npc],'Move real NPC');s.npcs[e.npc].location=e.location;s.npcs[e.npc].area=e.area;
   }else if(e.type==='item-add'){
    for(const n of Object.keys(s.players)){s.items[n]??={};s.items[n][e.item]=(s.items[n][e.item]||0)+e.quantity;s.grants.push({n,item:e.item,quantity:e.quantity});}
   }else if(e.type==='write-boolean')s.storage[e.key]=e.value;
   else if(e.type==='npc-health'){s.npcs[e.npc].hp=e.operator==='set'?e.value:s.npcs[e.npc].hp+e.value;}
   else if(e.type==='npc-relationship'){s.npcs[e.npc].relationship=e.value;}
   else if(['known-entity','location-hidden','quest-init'].includes(e.type)){}
   else throw Error('Unsupported emitted effect '+e.type);
  }
  return true;
 }
 const c=()=>s.storage.cc1;
 const clock=()=>run('cc1_initialize');
 const enter=()=>{clock();run('cc1_register');};
 const win=()=>{s.action=['I am ready to begin my called bout.'];run('cc1_ready');const m=c().v>=2?c().card[c().index]:c().matches.find(x=>x.id===c().match),op=c().v>=2?m.opponent:m.players.find(x=>x!=='@');s.tick++;s.npcs[op].hp=0;run('cc1_observe');return op};
 return {s,run,c,clock,enter,win};
}

// VERSION DISPATCH: retain v1 fixtures as historical diagnostics; current code uses the card suite.
if(w.triggerDefinitions.cc1_initialize.script.includes('v:3')){
 require('./test_crucible_v3.cjs')({w,manifest,harness,ck,getChecks:()=>checks});
}else if(w.triggerDefinitions.cc1_initialize.script.includes('v:2')){
 require('./test_crucible_v2.cjs')({w,manifest,harness,ck,getChecks:()=>checks});
}else{
for(const name of manifest.triggers){const t=w.triggerDefinitions[name];ck(t.conditions.length<=5&&t.effects.length<=10,'Native trigger caps '+name);if(t.script)new vm.Script(t.script)}
for(const level of [1,2,5,10,15,20,30,40,60,100,150]){
 const h=harness(level);h.enter();ck(h.c().phase==='ready','An available suitable or announced lower field can register at '+level);
 const count=h.c().roster.length;ck([4,8].includes(count),'Valid field size');
 ck(new Set(h.c().roster).size===count,'No duplicate entrants');
 ck(h.c().roster.slice(1).every(n=>w.npcs[n].level<=level+(level<=10?2:Math.max(4,Math.ceil(level*.3)))),'No involuntary over-level padding');
 const saved=JSON.stringify(h.c().matches);h.run('cc1_register');ck(JSON.stringify(h.c().matches)===saved,'Repeated registration cannot reroll');
 const rounds=Math.log2(count);for(let i=0;i<rounds;i++){h.win();if(i<rounds-1)ck(h.c().phase==='between','Winning a nonfinal waits for readiness');}
 ck(h.c().phase==='closed'&&h.c().outcome==='champion','Final closes exactly once at '+level);
 ck(Object.keys(h.c().prizes).length===1,'One pending prize');
 const results=h.c().matches.map(m=>m.winner);ck(results.every(Boolean),'All NPC branches settled');
 const tick=h.s.tick;h.run('cc1_result_win');ck(h.c().closedTick===tick,'No second final from repeated victory');
 h.run('cc1_claim_prize');ck(h.s.items.Player['Crucible Championship Trophy']===1,'Actual trophy awarded');
 h.run('cc1_claim_prize');ck(h.s.items.Player['Crucible Championship Trophy']===1,'No duplicate payout');
 h.s.tick=tick+99;h.run('cc1_register');ck(h.c().phase==='closed','Cooldown holds at +99');
 h.s.tick=tick+100;h.run('cc1_register');ck(h.c().phase==='ready'&&h.c().edition===2,'New edition at +100');
}
{
 const h=harness();h.enter();h.run('cc1_ready');h.s.hp.Player=0;h.run('cc1_result_win');
 ck(h.c().outcome==='eliminated'&&h.c().phase==='closed','Player incapacity outranks semantic victory');ck(!Object.keys(h.c().prizes).length,'Loss earns no prize');
}
{
 const h=harness();h.enter();h.run('cc1_ready');const m=h.c().matches.find(x=>x.id===h.c().match),op=m.players[1];h.s.tick++;h.s.hp.Player=0;h.s.npcs[op].hp=0;h.run('cc1_observe');
 ck(h.c().phase==='review'&&!m.winner,'Double knockout has no automatic winner');
 h.s.hp.Player=100;h.s.npcs[op].hp=100;h.run('cc1_review');ck(h.c().phase==='between'&&m.attempt===2,'One consented replay preserves bracket');
}
{
 const h=harness();h.enter();h.s.location='Four Sages Bazaar';h.run('cc1_observe');
 ck(h.c().phase==='closed'&&h.c().outcome==='withdrawn','Leaving between bouts closes entry');ck(!Object.keys(h.c().prizes).length,'Withdrawal earns no prize');
}
{
 const h=harness();h.enter();h.run('cc1_ready');h.s.location='Four Sages Bazaar';h.run('cc1_observe');ck(h.c().phase==='away','Unclear live departure gets a brief reconciliation window');
 h.s.tick+=2;h.run('cc1_observe');ck(h.c().phase==='closed','Missed semantic departure cannot strand bracket');
}
{
 const h=harness();h.enter();h.win();ck(h.s.hp.Player===100,'Unharmed winner stays unharmed');
 const before=h.s.grants.length;h.run('cc1_ready');ck(h.c().phase==='live','Unharmed fighter can skip treatment');ck(h.s.grants.length===before,'No invented medicine or free stock');
}
{
 const h=harness();h.enter();while(h.c().phase!=='closed')h.win();const old=structuredClone(h.c().prizes);h.s.tick=h.c().nextTick;h.run('cc1_register');
 ck(JSON.stringify(h.c().prizes)===JSON.stringify(old),'New edition preserves uncollected old prize');
 const snap=JSON.parse(JSON.stringify(h.s.storage));h.s.storage=snap;h.clock();ck(h.c().phase==='ready','Reload preserves current bracket');
}
{
 const h=harness();h.s.action=['I agree to a friendly match with Kōta Mibu.'];h.clock();h.run('cc1_exhibition');h.win();ck(!Object.keys(h.c().prizes).length&&h.c().nextTick===0,'Friendly win gives no championship and no cooldown');
}
{
 const h=harness();h.s.action=['I accept a friendly match.'];h.clock();h.run('cc1_exhibition');ck(h.c().phase==='idle','An ambiguous practice agreement never selects an unrelated opponent');
}
{
 const h=harness();h.s.players.Second=20;h.s.hp.Second=100;h.s.items.Second={};h.clock();h.run('cc1_register');
 ck(h.c().phase==='idle'&&!h.c().matches,'Multiplayer is not silently treated as one entrant');
}
{
 const h=harness();h.enter();h.run('cc1_ready');h.run('cc1_result_win',false);ck(h.c().phase==='live','No semantic match means no invented result');
 const n=h.c().matches.find(x=>x.id===h.c().match).players[1];delete h.s.npcs[n];h.s.tick++;h.run('cc1_observe');ck(h.c().phase==='live','Missing NPC value is not zero Health');
}
{
 const h=harness();h.enter();h.run('cc1_ready');h.s.players.Second=20;h.s.hp.Second=100;h.s.items.Second={};h.run('cc1_observe');
 ck(h.c().phase==='review'&&h.c().entrant==='Player','Joining human pauses rather than transferring entry');
 const saved=JSON.stringify(h.c().matches);h.run('cc1_result_win');ck(JSON.stringify(h.c().matches)===saved,'Multiplayer cannot settle paused solo entry');
}
{
 const h=harness();h.enter();while(h.c().phase!=='closed')h.win();const old=JSON.stringify(h.c().prizes);
 h.s.players={Different:20};h.s.hp={Different:100};h.s.items.Different={};h.run('cc1_claim_prize');
 ck(JSON.stringify(h.c().prizes)===old,'Another human cannot claim an earlier entrant prize');
 ck(!h.s.items.Different['Crucible Championship Trophy'],'No transferred trophy');
}
{
 const h=harness();h.s.location='Evertree Base';h.s.area='Evertree Base - Portal Room';h.s.items.Player={'Crucible Championship Trophy':1};
 h.run('cc1_grove_discover');ck(!h.s.storage.cc1_grove_open,'Trophy alone cannot open route');
 h.s.items.Player['Silver Web Portal Key']=1;h.s.storage.ghPortalTransitTick=h.s.tick;h.run('cc1_grove_discover');
 ck(!h.s.storage.cc1_grove_open,'Discovery defers on another actual portal transit tick');
 h.s.tick++;h.run('cc1_grove_discover');ck(h.s.storage.cc1_grove_open,'Eligible holder reveals route without crossing');
 ck(h.s.location==='Evertree Base','Discovery does not force travel');
 const companion='Kōta Mibu';h.s.npcs[companion].party=true;h.run('cc1_grove_enter');
 ck(h.s.location==='Sepulchral Portal House'&&h.s.area.endsWith('Return Arch'),'Committed crossing changes actual address');
 ck(h.s.npcs[companion].location===h.s.location,'NPC companions follow crossing');
 h.run('cc1_grove_key');h.run('cc1_grove_key');ck(h.s.items.Player['Sepulchral Portal Key']===1,'First arrival grants one key');
 h.run('cc1_grove_return');ck(h.s.location==='Sepulchral Portal House','Same-tick lock prevents bouncing');
 h.s.tick++;h.run('cc1_grove_return');ck(h.s.location==='Evertree Base'&&h.s.area==='Evertree Base - Portal Room','Return goes to exact hub');
 ck(h.s.npcs[companion].location==='Evertree Base','Return moves actual NPC companions');
}
{
 const h=harness();h.s.location='Evertree Base';h.s.area='Evertree Base - Portal Room';h.s.players.Second=20;h.s.items.Player={'Crucible Championship Trophy':1};h.s.items.Second={'Silver Web Portal Key':1};
 h.run('cc1_grove_discover');ck(!h.s.storage.cc1_grove_open,'Different item holders do not satisfy player-scoped conjunction');
}
{
 const h=harness();h.s.location='Sepulchral Conservatory';h.s.area='Sepulchral Conservatory - Grafting Heart';h.s.npcs['Kōta Mibu'].party=true;h.run('cc1_grove_inner_gate');
 ck(h.s.area.endsWith('Ossuary Greenhouse')&&!h.s.storage.cc1_grove_heart_seen,'Early heart click leaves party outside');
 ck(h.s.npcs['Kōta Mibu'].area===h.s.area,'Locked heart correction moves actual companions');
 h.s.area='Sepulchral Conservatory - Tending Gallery';h.run('cc1_grove_root',false);ck(!h.s.storage.cc1_grove_root,'Seeing a valve is not completing it');
 h.run('cc1_grove_root');delete h.s.items.Player['Rootwake Seal'];h.s.area='Sepulchral Conservatory - Ossuary Greenhouse';h.run('cc1_grove_mourning');
 h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_inner_gate');ck(h.s.storage.cc1_grove_heart_seen,'Both physical circuits open heart despite losing a seal');
 h.s.area='Sepulchral Conservatory - Entry Rotunda';ck(!h.s.storage.cc1_grove_resolved,'Backtracking does not declare victory');
 h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_release',false);ck(!h.s.storage.cc1_grove_resolved,'Failed semantic release gives no trophy');
 h.run('cc1_grove_release');h.s.npcs.Threnvoss.hp=0;h.run('cc1_grove_defeat');h.run('cc1_grove_release');
 ck(h.s.items.Player['Heartwood Remembrance']===1,'Release and defeat share one trophy owner');
 ck(h.s.npcs.Threnvoss.relationship===0,'Genuine release ends default hostility without forced friendship');
}
const digest=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
function sort(v){if(Array.isArray(v))return v.map(sort);if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])]));return v}
for(const [name,hash] of Object.entries(manifest.preserved.npcs))ck(digest(w.npcs[name])===hash,'Keep supplied NPC '+name);
for(const [name,hash] of Object.entries(manifest.preserved.originalItems))ck(digest(w.itemTypes[name])===hash,'Keep preceding item '+name);
for(const [name,hash] of Object.entries(manifest.preserved.originalAbilities))ck(digest(w.abilities[name])===hash,'Keep preceding ability '+name);
for(const [section,entries] of Object.entries(manifest.preserved.spider))for(const [name,hash] of Object.entries(entries))ck(digest(w[section][name])===hash,'Protected Spider configuration '+name);
console.log(JSON.stringify({status:'passed',checks,newNPCs:manifest.npcs.length,newAbilities:manifest.abilities.length,scope:'Actual emitted controller scripts with explicit semantic fixtures. No live Voyage, semantic recognition, native knockout or media-generation guarantee.'}));
}
