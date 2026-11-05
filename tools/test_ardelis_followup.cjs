// Exercise the actual emitted follow-up scripts. Semantic results are fixtures,
// never a claim to have tested Voyage's narrator or combat generation.
const fs=require('fs'),path=require('path'),assert=require('assert'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'..'),dir=path.join(__dirname,'ardelis-followup');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const w=require('./ardelis-phantom/previous_world.cjs')(read(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json')));
const review=read(path.join(dir,'review.json')),base=require('./ardelis-followup/previous_world.cjs')(w);
let checks=0;const ck=(b,m)=>{checks++;assert.ok(b,m);};
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
ck(Object.keys(review.names).length===108,'Approved complete naming migration');
for(const [old,name]of Object.entries(review.names)){
 ck(!w.npcs[old]&&!!w.npcs[name],'Exact new NPC key '+name);
 ck(w.npcs[name].name===name&&w.npcs[name].properName===name,'Canonical identity '+name);
 ck(!JSON.stringify(w).includes(old),'No obsolete full-name reference '+old);
}
for(const name of ['Noelle Ashford','Mireille Orselle','Sibylle Opal','Madelon Vire','Edmée Mott','Isaline Orselle'])ck(!!w.npcs[name],'Preserve approved foreign/Elven identity '+name);
const merge=read(path.join(dir,'section-merge.json'));
for(const s of ['locations','regions'])ck(hash(w[s])===merge[s].normalizedSectionHash,'Author corrected complete '+s+' exact');
for(const s of ['regions','locations'])for(const [n,v]of Object.entries(base[s])){
 const realm=s==='regions'?v.realm:base.regions[v.region]?.realm;
 if(realm==='The Silken Descent')ck(hash(w[s][n])===hash(v),'Spider geography exact '+n);
}
for(const [n,t]of Object.entries(base.triggerDefinitions))if(/spider|silken/i.test(n))ck(hash(w.triggerDefinitions[n])===hash(t),'Spider event exact '+n);
ck(hash(w.triggerDefinitions.ar_diadem_recovery)===hash(base.triggerDefinitions.ar_diadem_recovery),'Party diadem behavior unchanged');
const cmp=(a,op,b)=>op==='contains'?Array.isArray(a)&&a.includes(b):op==='notContains'?!(Array.isArray(a)&&a.includes(b)):op==='regex'?new RegExp(b).test(a):({equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b})[op];
function fixture(extra={}){
 const s={tick:500,realm:'Glowhaven',location:'Four Sages Bazaar',area:'Four Sages Bazaar - Market Circle',traits:{Alice:['Summoned one','Traced Shore Record']},levels:{Alice:20},quests:{},hp:{'Kazunari Shiba':100},fighting:false,actions:[],...extra,storage:{rbCampaign:true,rbPhase:5,...extra.storage}};
 const check=c=>{
  let v;
  if(c.type==='game-tick')v=s.tick;
  else if(c.type==='party-realm')v=s.realm;else if(c.type==='party-location')v=s.location;else if(c.type==='party-area')v=s.area;
  else if(c.type==='player-traits')v=s.traits;else if(c.type==='player-level')v=s.levels;
  else if(c.type==='npc-in-combat')v=s.fighting;else if(c.type==='npc-health')v=s.hp[c.npc]??100;
  else if(c.type==='npc-in-scene')v=true;
  else if(c.type==='read-number')v=Number(s.storage[c.key]||0);else if(c.type==='read-boolean')v=s.storage[c.key]===true;
  else if(c.type==='quest-status')v=s.quests[c.questId]||'planned';
  else if(c.type==='action-text')v=s.actions;else throw Error('Unmocked check '+c.type);
  if(!c.operator)return v;
  return ['player-traits','player-level'].includes(c.type)?Object.values(v).some(x=>cmp(x,c.operator,c.value)):cmp(v,c.operator,c.value);
 };
 function fire(name,semantic=false){
  const t=w.triggerDefinitions[name];if(!t.conditions.every(c=>['story','action'].includes(c.type)?semantic:check(c)))return false;
  const box={storage:s.storage,check,effects:structuredClone(t.effects),skip:false};if(t.script)vm.runInNewContext(t.script,box,{timeout:500});
  if(box.skip)return false;
  s.effects=box.effects;
  for(const e of box.effects){if(e.type.startsWith('write-'))s.storage[e.key]=e.value;else if(e.type==='quest-init')s.quests[e.value]='available';}
  return true;
 }
 return {s,fire};
}
let f=fixture({storage:{rbPhase:1}});
ck(!f.fire('rb_peaceful_departure',false)&&f.s.storage.rbPhase===1,'A promise or imagined departure is insufficient');
ck(f.fire('rb_peaceful_departure',true)&&f.s.storage.rbPhase===3,'Actual peaceful resolution progresses directly');
ck(!f.s.effects.some(e=>e.npc==="Valkazathoth'dmir"),'No forced wizard appearance');
ck(!f.fire('rb_intervention',true),'Concluded inquiry cannot force later intervention');
f=fixture({storage:{rbPhase:1},hp:{'Kazunari Shiba':0}});ck(!f.fire('rb_peaceful_departure',true),'Casualty uses its existing branch');
for(const [name,flag,quest]of [['rb_offer_carrier_once','rbCarrierLead','The Carrier behind the Ledger'],['rb_offer_audience_once','rbAudienceLead','At the Wandering Door']]){
 f=fixture();ck(!f.fire(name),'No lead, no offer');f.s.storage[flag]=true;ck(f.fire(name),'Real lead offers a planned quest');ck(!f.fire(name),'Repeated lead does not repeat an available offer');
 for(const state of ['available','accepted','completed','rejected','abandoned','expired']){f.s.quests[quest]=state;ck(!f.fire(name),'Do not reset '+state+' '+quest);}
}
for(const name of ['A Name in the Shore Ledger','The Carrier behind the Ledger']){
 const nonOffers=a=>a.filter(e=>!['quest-init','write-boolean'].includes(e.type));
 ck(hash(nonOffers(w.parties[''].quests[name].onCompleteEffects))===hash(nonOffers(base.parties[''].quests[name].onCompleteEffects)),'Original completion rewards unchanged '+name);
}
f=fixture();f.fire('rb_clock');ck(f.s.storage.rbHuntByName.Alice.next===600&&!f.s.storage.rbHuntDue,'First repeat eligibility waits 100 turns');
f.s.tick=599;f.fire('rb_clock');ck(!f.s.storage.rbHuntDue,'No early attempt');f.s.tick=600;f.fire('rb_clock');ck(f.s.storage.rbHuntDue,'Attempt becomes eligible at 100');
ck(!f.fire('rb_pursuit_attempt',false)&&!f.s.storage.rbHuntActive,'Unsuitable scene postpones without consuming attempt');
ck(f.fire('rb_pursuit_attempt',true)&&f.s.storage.rbHuntActive,'Suitable actual encounter starts once');
ck(f.s.storage.rbHuntCase.target==='Alice'&&f.s.storage.rbHuntCase.attempt===1,'Case records the correct bearer');
ck(f.s.effects.length===1&&f.s.effects[0].type==='story','Setup gives no automatic damage, reward or capture');
ck(f.s.effects[0].instruction.includes('Exactly one opposing individual'),'Early finite opposition');
ck(!f.fire('rb_pursuit_attempt',true),'Active encounter cannot be duplicated');
f.s.tick=900;f.fire('rb_clock');ck(!f.s.storage.rbHuntDue,'Long active encounter never stacks another wave');
ck(!f.fire('rb_pursuit_resolved',false)&&f.s.storage.rbHuntActive,'Intent to escape is not resolution');
f.s.tick=950;ck(f.fire('rb_pursuit_resolved',true)&&!f.s.storage.rbHuntActive,'Actual resolution closes the active case');
ck(f.s.storage.rbHuntByName.Alice.next===1050&&f.s.storage.rbHuntLastResolvedTick===950,'Cooldown starts at resolution, not encounter start');
f.s.tick=1049;f.fire('rb_clock');ck(!f.s.storage.rbHuntDue,'No shortened quiet interval');f.s.tick=1050;f.fire('rb_clock');ck(f.s.storage.rbHuntDue,'Eligible again after actual quiet interval');
function due(extra={}){const x=fixture(extra);x.fire('rb_clock');x.s.tick+=100;x.fire('rb_clock');return x;}
for(const extra of [{traits:{Alice:['Summoned one']}},{traits:{Alice:['Traced Shore Record']}},{levels:{Alice:14}},{storage:{rbPhase:4}},{fighting:{Enemy:true}},{realm:'Wraith Island Prison'},{realm:"Vladimir's Elsewhere"},{realm:'The Silken Descent'}])ck(!due(extra).s.storage.rbHuntDue,'Exclude unqualified or inaccessible case '+JSON.stringify(extra));
for(const location of ['Phoenix Wing Academy','The Eternal Crucible','Caelrath Palace','Caelrath Portal Hall','Caelrath Institute of Magic',"The Grand Sage's Court",'Evertree Base','Shadowspire'])ck(!due({location}).s.storage.rbHuntDue,'No interruption at protected venue '+location);
f=due({traits:{Alice:['Summoned one','Traced Shore Record'],Spectator:[]},levels:{Alice:18,Spectator:100}});
ck(f.s.storage.rbHuntCandidate.name==='Alice'&&f.s.storage.rbHuntCandidate.primaryMax===20,'Unrelated powerful spectator does not inflate the target band');
f.s.traits.Alice=[];ck(!f.fire('rb_pursuit_attempt',true),'A departed/unqualified bearer invalidates a stale dispatch');
f=due();f.s.levels.Alice=14;ck(!f.fire('rb_pursuit_attempt',true),'Recheck minimum level at dispatch');
f=due();f.s.storage.arReceivingConcluded=true;ck(!f.fire('rb_pursuit_attempt',true),'Recheck terminal outcome at dispatch');
for(const ended of [{storage:{rbPhase:5,arReceivingConcluded:true}},{quests:{'Rebirth: What the Crown Received':'completed'}}])ck(!due(ended).s.storage.rbHuntDue,'Either actual ending marker stops new attempts');
f=due({levels:{Alice:100}});f.s.storage.rbHuntByName.Alice.attempts=2;f.fire('rb_clock');ck(f.s.storage.rbHuntCandidate.primaryMax===45&&f.s.storage.rbHuntCandidate.supportLevel===35&&f.s.storage.rbHuntCandidate.count===2,'Desperate team has finite caps');
ck(f.fire('rb_pursuit_attempt',true)&&f.s.effects[0].instruction.includes('Primary opponent native level 45-45')&&f.s.effects[0].instruction.includes('At most one support opponent, level 35'),'Actual high-level dispatch retains bounded opposition');
f.s.storage.arReceivingConcluded=true;f.fire('rb_clock');ck(!f.s.storage.rbHuntDue&&f.s.storage.rbHuntActive,'Ending does not erase an already active fight');
ck(!/completed game turns|native story interpretation|live playtest/i.test(w.worldLore['Ardelis — Mana Traces and Recurring Pursuit'].text),'Runtime lore contains no implementation/test briefing');
console.log(JSON.stringify({status:'passed',checks,scope:'Exact merge preservation and emitted-script behavior with supplied semantic answers; generated combat stats and live scheduling remain untested.'}));
