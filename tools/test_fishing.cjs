// Real emitted scripts; semantic answers and native action outcomes are fixtures.
// This is not an NLP test, a native-engine conformance test or a live playtest.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const root=path.resolve(__dirname,'..');
const w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'fishing/manifest.json'),'utf8'));
let checks=0;function ck(x,label){checks++;assert.ok(x,label)}
const levels=['impossible','critical failure','failure','mixed results','basic success','success','great success','critical success'];
function compare(a,op,b){return {equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b,contains:Array.isArray(a)&&a.includes(b),notContains:Array.isArray(a)&&!a.includes(b),regex:typeof b==='string'&&new RegExp(b).test(String(a))}[op]}
function player(o={}){return {items:{'Angler’s Rod':1,'Angler’s Bait Portion':3},skills:{Fishing:1},traits:[],outcome:'success',semantic:new Set(),...o}}
function fixture(o={}){
 const s={tick:1,realm:'Glowhaven',location:'Pinewater River',area:'Pinewater River - River Bend',region:'Pinewater Vale',text:'I cast my line.',players:{Alice:player()},quests:{},storage:{},rng:()=>0,...o};
 const raw=c=>{
  if(c.type==='game-tick')return s.tick;
  if(c.type==='party-realm')return s.realm;if(c.type==='party-location')return s.location;if(c.type==='party-area')return s.area;if(c.type==='party-region')return s.region;
  if(c.type==='action'||c.type==='action-text')return [s.text];if(c.type==='story'||c.type==='story-text')return '';
  if(c.type==='quest-status')return s.quests[c.questId]||'hidden';
  if(c.type==='player-traits')return Object.fromEntries(Object.entries(s.players).map(([n,p])=>[n,p.traits]));
  if(c.type==='player-item')return Object.fromEntries(Object.entries(s.players).map(([n,p])=>[n,p.items[c.item]||0]));
  if(c.type==='skill-value')return Object.fromEntries(Object.entries(s.players).map(([n,p])=>[n,p.skills[c.skill]||0]));
  if(c.type==='action-success-level')return Object.fromEntries(Object.entries(s.players).map(([n,p])=>[n,p.outcome]));
  throw Error('Unimplemented read '+c.type);
 };
 // Script-side semantic types return RAW TEXT, even with a query/operator.
 const check=c=>{const v=raw(c);if(!c.operator||['action','story'].includes(c.type))return v;return v&&typeof v==='object'&&!Array.isArray(v)?Object.values(v).some(x=>compare(x,c.operator,c.value)):compare(v,c.operator,c.value)};
 function qualifies(c,p,id){
  if(c.type==='action'||c.type==='story')return p.semantic.has(id);
  let value;if(c.type==='player-item')value=p.items[c.item]||0;
  else if(c.type==='player-traits')value=p.traits;
  else if(c.type==='skill-value')value=p.skills[c.skill]||0;
  else if(c.type==='action-success-level')return compare(levels.indexOf(p.outcome),c.operator,levels.indexOf(c.value));
  else value=raw(c);
  if(c.type==='action-text')return value.some(v=>compare(v,c.operator,c.value));
  return compare(value,c.operator,c.value);
 }
 function run(id,{apply=true}={}){
  const t=w.triggerDefinitions[id];const recipients=Object.entries(s.players).filter(([n,p])=>t.conditions.every(c=>qualifies(c,p,id))).map(([n])=>n);
  if(!recipients.length)return [];
  const math=Object.create(Math);math.random=s.rng;
  const box={check,storage:s.storage,effects:structuredClone(t.effects),skip:false,Math:math};
  if(t.script)vm.runInNewContext(t.script,box,{timeout:100});
  if(box.skip)return [];
  const effects=JSON.parse(JSON.stringify(box.effects));ck(effects.length<=10,id+' effect count');
  for(const e of effects){
   if(e.type==='story'){ck(e.instruction.length<=1000,id+' story length');continue}
   if(!apply)continue;
   const names=e.target==='allPlayers'?Object.keys(s.players):recipients;
   for(const n of names){const p=s.players[n];
    if(e.type==='item-add'){ck(!!w.itemTypes[e.item],id+' real fish/item');p.items[e.item]=(p.items[e.item]||0)+(e.quantity||1)}
    else if(e.type==='item-remove'){ck((p.items[e.item]||0)>=(e.quantity||1),id+' spends actual holder inventory');p.items[e.item]-=e.quantity||1}
    else if(e.type==='player-traits'){
     if(e.operator==='add'&&!p.traits.includes(e.value)){p.traits.push(e.value);for(const x of w.traits[e.value].skills)p.skills[x.skill]=(p.skills[x.skill]||0)+x.modifier}
     else if(e.operator==='remove')p.traits=p.traits.filter(v=>v!==e.value);
    }else if(e.type==='quest-init')s.quests[e.value]='available';
    else throw Error('Unexpected fishing effect '+e.type);
   }
  }
  return effects;
 }
 return {s,run,check};
}
function allow(f,...ids){for(const p of Object.values(f.s.players))for(const id of ids)p.semantic.add(id);return f}
function catches(f,n='Alice'){return m.species.reduce((sum,k)=>sum+(f.s.players[n].items[k]||0),0)}
ck(m.species.length===30&&m.gear.length===11&&Object.keys(m.sites).length===18,'Reviewed catalogue size');
for(const [k,t]of Object.entries(w.triggerDefinitions).filter(([k])=>k.startsWith('fsh_')||m.repairedLocalOffers.includes(k))){
 ck(t.conditions.length<=5,'Condition cap '+k);ck(!t.script||!(/check\(\{\s*type\s*:\s*['"](?:action|story)['"]\s*,\s*query/.test(t.script)),'No fake script semantic evaluation '+k);
 ck(!(t.phase==='planning'&&t.conditions.some(c=>['story','action'].includes(c.type))),'Native phase convention '+k);
 ck(JSON.stringify(t).length<=10000,'Compact trigger cap '+k);
 for(const c of t.conditions)if(typeof c.value==='string')ck(c.value.length<=100,'Value cap '+k);
 if(t.script)new vm.Script(t.script);
}
for(const [area,habitat]of Object.entries(m.sites)){ck(!!w.locations[area.split(' - ')[0]]?.areas[area],'Actual fishing ground '+area);ck('rehsd'.includes(habitat),'Known habitat')}
ck(!Object.keys(m.sites).some(x=>/Serpent Ledge|Nest|Crypt|Infirmary|Portal/.test(x)),'Dangerous/indoor rooms are not fishing shortcuts');
let f=fixture();f.run('fsh_weather');const initial=JSON.stringify(f.s.storage.fshWeather);ck(f.s.storage.fshWeather.inland.kind==='clear','Usable initial inland forecast');ck(!f.run('fsh_weather').length&&JSON.stringify(f.s.storage.fshWeather)===initial,'No forecast reroll same turn');
f.s.tick=2;f.run('fsh_weather');ck(JSON.stringify(f.s.storage.fshWeather)===initial,'Weather persists across ordinary turns');
f.s.tick=40;f.run('fsh_weather');for(const z of ['coast','inland'])ck(f.s.storage.fshWeather[z].until>=52&&f.s.storage.fshWeather[z].until<=64,'Bounded next forecast '+z);
f=allow(fixture(),'fsh_cast_lure');f.run('fsh_cast_lure');ck(catches(f)===1&&f.s.players.Alice.items['Angler’s Bait Portion']===3,'One ordinary lure catch, no bait spent');ck(f.s.storage.fshRecords['Pinewater Perch'].best===12,'Measurement in records');ck(!f.run('fsh_cast_lure').length&&catches(f)===1,'Same turn retry cannot duplicate catch');
f=allow(fixture(),'fsh_cast_bait');f.run('fsh_cast_bait');ck(catches(f)===1&&f.s.players.Alice.items['Angler’s Bait Portion']===2,'Successful baited cast consumes exactly one');
f=allow(fixture({players:{Alice:player({outcome:'failure'})}}),'fsh_bait_miss');f.run('fsh_bait_miss');ck(catches(f)===0&&f.s.players.Alice.items['Angler’s Bait Portion']===2,'Failed real baited cast spends bait, no consolation fish');f.run('fsh_bait_miss');ck(f.s.players.Alice.items['Angler’s Bait Portion']===2,'No retry bait double-charge');
f=fixture();f.run('fsh_cast_lure');ck(catches(f)===0,'Discussing fishing does not qualify');
f=allow(fixture({area:'Phoenix Wing Academy - Lecture Hall'}),'fsh_cast_lure','fsh_basics');f.s.players.Alice.skills={};f.run('fsh_cast_lure');f.run('fsh_basics');ck(catches(f)===0&&!f.s.players.Alice.skills.Fishing,'No catch or lesson from an indoor claim');
f=allow(fixture({realm:'Asterveil'}),'fsh_cast_lure');f.run('fsh_cast_lure');ck(catches(f)===0,'Glowhaven system stays local');
f=allow(fixture({players:{Alice:player({skills:{}})}}),'fsh_basics');f.run('fsh_basics');f.run('fsh_basics');ck(f.s.players.Alice.skills.Fishing===1,'First real practice teaches basics once');
f=fixture({players:{Alice:player({items:{}}),Bob:player()}});f.s.players.Alice.semantic.add('fsh_cast_lure');f.run('fsh_cast_lure');ck(catches(f,'Alice')===0&&catches(f,'Bob')===0,'Cannot borrow a spectator’s gear or grant them a catch');
f=fixture({players:{Alice:player(),Bob:player()}});f.s.players.Alice.semantic.add('fsh_cast_bait');f.run('fsh_cast_bait');ck(catches(f,'Alice')===1&&catches(f,'Bob')===0&&f.s.players.Bob.items['Angler’s Bait Portion']===3,'One angler never consumes spectator bait');
f=allow(fixture({players:{Alice:player(),Bob:player()}}),'fsh_cast_lure');f.run('fsh_cast_lure');ck(catches(f,'Alice')===1&&catches(f,'Bob')===1,'Two qualifying anglers each receive their local shoal catch');
function hooked(){const a=allow(fixture({rng:()=>0.99999}),'fsh_cast_lure');a.run('fsh_cast_lure');return a}
f=hooked();ck(catches(f)===0&&f.s.players.Alice.traits.includes('Rare Fish on the Line'),'Rare hook is not an inventory grant');const chosen=f.s.storage.fshHook.fish;f.s.tick++;allow(f,'fsh_rare_land');f.run('fsh_rare_land');ck(f.s.players.Alice.items[chosen]===1&&!f.s.players.Alice.traits.includes('Rare Fish on the Line'),'Actual handling lands the exact saved species');f.run('fsh_rare_land');ck(catches(f)===1,'Landing cannot repeat');f.run('fsh_weather');ck(!f.s.storage.fshHook,'Finished hook state swept when no holders remain');
f=hooked();f.s.tick++;allow(f,'fsh_rare_release');f.run('fsh_rare_release');ck(catches(f)===0&&!f.s.players.Alice.traits.length,'Voluntary release gives no fish');
f=hooked();f.s.tick++;f.s.players.Alice.outcome='mixed results';allow(f,'fsh_rare_miss');f.run('fsh_rare_miss');ck(catches(f)===0&&!f.s.players.Alice.traits.length,'Unsuccessful rare handling has a terminating outcome');
for(const change of [{area:'Whitecrest Harbor - Harbor Office'},{realm:'Drakenspire',area:'Drakenspire - Portal Room'},{tick:8}]){
 f=hooked();Object.assign(f.s,change);f.run('fsh_rare_cleanup');ck(catches(f)===0&&!f.s.players.Alice.traits.length&&!f.s.storage.fshHook,'Leaving/expiry terminates unlanded catch '+JSON.stringify(change));
}
f=hooked();f.s.storage.fshHook.fish='Nonexistent Fish';f.run('fsh_rare_cleanup');ck(!f.s.players.Alice.traits.length,'Corrupt hook fails closed');
f=allow(fixture({area:'The Gilded Albatross - Main Deck',storage:{fshWeather:{coast:{kind:'storm',until:99},inland:{kind:'clear',until:99}}}}),'fsh_cast_bait');f.run('fsh_cast_bait');ck(!catches(f)&&f.s.players.Alice.items['Angler’s Bait Portion']===3,'Warned offshore squall spends no bait or catch');
f.s.tick++;f.s.players.Alice.outcome='failure';allow(f,'fsh_bait_miss');f.run('fsh_bait_miss');ck(f.s.players.Alice.items['Angler’s Bait Portion']===3,'Failed unsafe cast also retains bait');
// Inspecting old records cannot mint fish or money.
f=fixture({text:'I check my fishing records.',storage:{fshRecords:{'Pinewater Perch':{best:20,landings:3}}}});const ledger=f.run('fsh_records');ck(ledger.every(e=>e.type==='story')&&catches(f)===0,'Records are observations, not inventory');
// Weighted sampling exercises every water table with emitted code and real item IDs.
for(const [area,habitat]of Object.entries(m.sites))for(const weather of ['clear','overcast','rain','fog','wind'])for(const roll of [0,.25,.7,.999]){
 f=allow(fixture({area,rng:()=>roll,storage:{fshWeather:{inland:{kind:weather},coast:{kind:weather}}}}),'fsh_cast_lure');f.run('fsh_cast_lure');ck(catches(f)===1||!!f.s.storage.fshHook,'Every supported table yields a fish or rare hook '+area+'/'+weather+'/'+roll);
}
for(const title of m.quests){const q=w.parties[''].quests[title];ck(q.status==='hidden'&&q.completionCondition.type==='story','Optional native fishing quest '+title);ck(q.onCompleteEffects.filter(e=>e.type==='item-add'&&e.item==='Mark').length===1,'One reward owner '+title);ck(!Array.isArray(q.objectives)&&Object.values(q.objectives).every(o=>typeof o.id==='string'&&typeof o.text==='string'&&['hidden','active','completed'].includes(o.status)),'Native keyed objective records '+title)}
// Review proof: unrelated whole sections, including NPCs, map pins/art and realms, stay exact.
for(const [k,h]of Object.entries(m.unchangedTopLevel)){const actual=crypto.createHash('sha256').update(JSON.stringify(w[k])).digest('hex');ck(actual===h,'Unchanged section '+k)}
ck(w.imagePromptConfiguration.npcs.includes('top of the thighs')===false&&w.imagePromptConfiguration.npcs.includes('upper thighs'),'Hip-up runtime wording reaches below waist');
ck(w.traits['Portrait Frame — Hip-up'].description.includes('top of the thighs'),'Selected hip-up crop is explicit');
const prior=require('./fishing/historical_view.cjs')(w);
ck(!prior.skills.Fishing&&prior.npcs.Nerathyl.level===45,'Historical view removes this patch only');
const mutated=structuredClone(w);mutated.npcs.Nerathyl.level=1;
assert.throws(()=>require('./fishing/historical_view.cjs')(mutated),/exact reviewed Fishing patch/);checks++;
console.log(JSON.stringify({status:'passed',checks,species:30,grounds:18,nativeQuests:3,semanticRecognitionTested:false,livePlaytest:false}));
