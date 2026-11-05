// Actual emitted bracket scripts. Semantic decisions are supplied fixtures, not AI claims.
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const currencyDelta=JSON.parse(fs.readFileSync(path.join(__dirname,'currency/approved-description-delta.json'),'utf8'));
const studioCoordinates=JSON.parse(fs.readFileSync(path.join(__dirname,'currency/approved-studio-coordinates.json'),'utf8'));
module.exports=({w,manifest,harness,ck,getChecks})=>{
 const bout=h=>h.c().card[h.c().index],ready=h=>h.run('cc1_ready');
 const nodes=h=>h.c().rounds.flat(),title=h=>{h.enter();let limit=5;while(h.c().phase!=='closed'&&limit--)h.win();ck(h.c().outcome==='champion','Championship closes');};
 for(const key of manifest.triggers){const t=w.triggerDefinitions[key];ck(!!t&&t.conditions.length<=5&&t.effects.length<=10,'Supported trigger '+key);if(t.script)new vm.Script(t.script);ck(JSON.stringify(t).length<=10000,'Trigger UTF16 cap '+key);}
 for(const level of [1,2,5,10,15,20,30,40,60,100,150]){
  const h=harness(level);h.enter();ck(h.c().v===3&&h.c().phase==='waiting','Register level '+level);
  ck([3,7].includes(h.c().roster.length),'Four/eight entrant field');ck(new Set(h.c().roster).size===h.c().roster.length,'No duplicate entrant');
  ck(h.c().roster.every(n=>w.npcs[n].level<=level+(level<=10?2:Math.max(4,Math.ceil(level*.3)))),'No forced oversized fighter');
  const original=JSON.stringify(h.c().rounds);h.run('cc1_register');ck(JSON.stringify(h.c().rounds)===original,'No registration reroll');
  const rounds=h.c().rounds.length;for(let i=0;i<rounds;i++){const m=bout(h);h.win();ck(m.result?.winner==='player','Recorded real player bout');if(i<rounds-1)ck(h.c().phase==='waiting','Fresh readiness between bouts');}
  ck(h.c().phase==='closed'&&h.c().champion==='Player','Final has one champion');ck(nodes(h).every(n=>n.done),'Every bracket match settled');
  ck(h.c().history.at(-1).champion==='Player','History records champion');
  h.run('cc1_claim_prize');h.run('cc1_claim_prize');ck(h.s.items.Player['Crucible Championship Trophy']===1,'Exactly one trophy');ck(h.s.items.Player.Mark===h.c().purse,'Exactly one purse');
  h.s.tick=h.c().nextTick-1;h.run('cc1_register');ck(h.c().phase==='closed','Cooldown before boundary');h.s.tick++;h.run('cc1_register');ck(h.c().edition===2,'New edition at hundred turns');
 }
 {
  const h=harness();h.enter();const m=bout(h),old=m.opponent;h.s.npcs[old].hp=0;ready(h);ck(h.c().phase==='waiting'&&!m.startedTick&&!m.result,'No pre-start win');ck(m.opponent!==old,'Substitute announced');ready(h);ck(h.c().phase==='live','Fresh substitute readiness');h.s.tick++;h.s.npcs[m.opponent].hp=0;h.run('cc1_observe');ck(nodes(h).find(n=>n.id===m.node).winner==='@','Substitute result reaches real bracket node');
 }
 {
  const h=harness();h.enter();Object.values(h.s.npcs).forEach(n=>n.hp=0);ready(h);ck(h.c().outcome==='cancelled'&&!Object.keys(h.c().prizes).length,'No-fit field closes without prize');
 }
 {
  const h=harness();h.enter();h.s.hp.Player=0;ready(h);ck(h.c().phase==='waiting','Zero-health player blocked');h.s.hp.Player=35;ready(h);ck(h.c().phase==='live'&&h.s.hp.Player===35,'No full-bar gate or free heal');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.tick++;h.s.hp.Player=0;h.s.npcs[m.opponent].hp=0;h.run('cc1_observe');ck(m.result.winner==='draw'&&h.c().outcome==='eliminated','Double KO closes');ck(Object.keys(h.c().care).length===1,'Double KO care entitlement');ck(h.c().champion!==m.opponent,'Downed eliminated opponent cannot become champion');ck(!Object.keys(h.c().prizes).length,'No double-KO trophy');
 }
 for(const who of ['player','opponent']){
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.area='The Eternal Crucible - Competitor Lounge';h.s.tick++;
  if(who==='player')h.s.hp.Player=0;else h.s.npcs[m.opponent].hp=0;
  h.run('cc1_observe');ck(h.c().phase==='live'&&!m.result&&m.requiresRuling,'Lounge incapacity is not match result: '+who);
  h.s.area=m.arena;h.s.tick++;h.run('cc1_observe');ck(!m.result,'Returning cannot launder unrelated incapacity');
  h.run('cc1_result_win',false);h.run('cc1_result_loss',false);ck(!m.result,'No semantic ruling means no fabricated result');
  h.run('cc1_result_loss',true);ck(h.c().outcome==='eliminated','An actual official ruling closes an interrupted bout');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.area='The Eternal Crucible - Infirmary';h.s.hp.Player=0;h.s.npcs[m.opponent].hp=100;h.s.tick++;h.run('cc1_observe');h.run('cc1_result_draw',true);ck(m.result.winner==='draw'&&h.c().outcome==='eliminated','Official double elimination survives medical movement and recovery');ck(h.c().champion!==m.opponent,'Recovered double-KO opponent remains eliminated');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.npcs[m.opponent].area='The Eternal Crucible - Infirmary';h.s.npcs[m.opponent].hp=0;h.s.tick++;h.run('cc1_observe');ck(!m.result&&m.requiresRuling,'Opponent must be in assigned ring for automatic KO');
 }
 {
  const h=harness();h.enter();ready(h);h.s.hp.Player=0;h.run('cc1_result_win');ck(h.c().outcome==='eliminated','In-ring native incapacity defeats false semantic win');
 }
 {
  const h=harness();h.enter();const m=bout(h);h.c().phase='live';h.clock();h.run('cc1_result_win');ck(!m.result,'Unstarted bout has no result');h.run('cc1_observe');ck(h.c().outcome==='cancelled','Missing start closes finitely');
 }
 for(const live of [false,true]){
  const h=harness();h.enter();if(live)ready(h);const entry=JSON.stringify(h.c().rounds);h.s.area='The Eternal Crucible - Grand Stands';h.s.tick++;h.run('cc1_observe');h.run('cc1_withdraw',false);h.run('cc1_ready',false);ck(h.c().phase===(live?'live':'waiting'),'Movement/spectating alone does not withdraw');ck(JSON.stringify(h.c().rounds)===entry,'No movement result tree');h.s.location='Four Sages Bazaar';h.run('cc1_observe');ck(h.c().phase===(live?'live':'waiting'),'Venue departure alone does not forfeit');h.run('cc1_withdraw');ck(h.c().outcome==='withdrawn','Explicit forfeit works');
 }
 {
  const h=harness();h.enter();ready(h);h.s.players.Spectator=20;h.s.hp.Spectator=100;h.run('cc1_observe');h.run('cc1_result_win');ck(h.c().phase==='live'&&!bout(h).result&&h.c().entrant==='Player','Second human suspends without cancelling or transferring');delete h.s.players.Spectator;h.run('cc1_result_loss');ck(h.c().outcome==='eliminated','Original solo owner can resume');
 }
 {
  const h=harness();h.clock();h.s.players.Second=20;h.run('cc1_register');ck(h.c().phase==='idle','No new multiplayer championship');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);const barred=h.c().roster.find(n=>n!==m.opponent);h.s.npcs[barred].hp=0;h.run('cc1_result_loss');ck(h.c().phase==='closed'&&h.c().champion&&h.c().champion!==barred,'Loss still records fit NPC champion');ck(nodes(h).every(n=>n.done),'NPC bracket settles once');const saved=JSON.stringify(h.c().rounds);h.run('cc1_observe');h.run('cc1_result_loss');ck(JSON.stringify(h.c().rounds)===saved,'Settled NPC matches never reroll');
 }
 {
  const h=harness();h.enter();ready(h);const op=bout(h).opponent;Object.entries(h.s.npcs).forEach(([n,v])=>{if(n!==op)v.hp=0});h.s.npcs[op].combat=true;h.run('cc1_result_loss');ck(h.c().champion===op,'Winner of the actual stopped fight remains eligible before the native combat flag clears');
 }
 {
  const h=harness();h.enter();ready(h);Object.entries(h.s.npcs).forEach(([n,v])=>{if(n!==bout(h).opponent)v.hp=0});h.s.npcs[bout(h).opponent].hp=0;h.s.hp.Player=0;h.s.tick++;h.run('cc1_observe');ck(h.c().phase==='closed'&&!h.c().champion,'All unfit yields no fake champion');
 }
 {
  const h=harness();title(h);const old=JSON.stringify(h.c().prizes);h.s.players={Different:20};h.run('cc1_claim_prize');ck(JSON.stringify(h.c().prizes)===old,'Prize never transfers identity');
 }
 {
  const h=harness();h.clock();h.s.action=['I agree to a friendly match with Kōta Mibu.'];h.run('cc1_exhibition');h.win();ck(h.c().outcome==='exhibition win'&&h.c().nextTick===0&&!Object.keys(h.c().prizes).length,'Exhibition isolated');
 }
 {
  const h=harness();h.s.storage.cc1={v:2,phase:'live',edition:2,history:[],care:{},prizes:{1:{owner:'Player',marks:100,title:'Old cup'}},card:[{}]};h.clock();ck(h.c().v===3&&h.c().outcome==='cancelled','Old unfinished card closes honestly');ck(h.c().prizes[1].marks===100,'Old earned prize retained');
 }
 // The dungeon route and return were not changed in this revision.
 {
  const h=harness();h.s.location='Sepulchral Conservatory';h.s.area='Sepulchral Conservatory - Entry Rotunda';h.s.action=['I go to the Grafting Heart.'];h.run('cc1_grove_inner_gate');ck(h.s.area.endsWith('Entry Rotunda'),'Early heart route stopped');h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_inner_gate_state');ck(h.s.area.endsWith('Entry Rotunda'),'Heart state backstop');
 }
 const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v,digest=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
 // Only historical identity fingerprints use the exact inverse; bouts above use current rules/NPCs.
 const prePlaytestNPCs=require('./playtest-phantom/previous_world.cjs')(w).npcs;
 for(const [k,v] of Object.entries(manifest.preserved.npcs))ck(digest(prePlaytestNPCs[k])===v,'Preserve unrelated NPC '+k);
 const edited=new Set(['basicInfo','hiddenInfo','personality','abilities','visualDescription','portraitUrl']);
 for(const [k,v] of Object.entries(manifest.preserved.revisedNPCIdentity))ck(digest(Object.fromEntries(Object.entries(prePlaytestNPCs[k]).filter(([f])=>!edited.has(f))))===v,'Preserve revised NPC identity/stats '+k);
 const approvedPrevious=require('./approved_expansion.cjs')(w);
 for(const s of ['originalItems','originalAbilities'])for(const [k,v] of Object.entries(manifest.preserved[s])){
  let value=approvedPrevious[s==='originalItems'?'itemTypes':'abilities'][k];
  const d=currencyDelta.itemTypes;
  if(s==='originalItems'&&k===d.entry&&digest(value)!==v){
   ck(value[d.field]===d.after,'Exact approved Mark description');
   value={...value,[d.field]:d.before};
  }
  ck(digest(value)===v,'Preserve '+s+' '+k);
 }
 for(const [s,values] of Object.entries(manifest.preserved.spider))for(const [k,v] of Object.entries(values))ck(digest(w[s][k])===v,'Preserve Spider '+k);
 const pres=JSON.parse(fs.readFileSync(path.join(__dirname,'crucible/revision-preservation.json'),'utf8'));
 for(const [k,v] of Object.entries(pres.unchangedSections)){
  let value=approvedPrevious[k];
  const d=currencyDelta[k];
  if(d&&digest(value)!==v){
   ck(value[d.entry]?.[d.field]===d.after,'Exact approved currency field '+k);
   value=structuredClone(value);value[d.entry][d.field]=d.before;
  }
  ck(digest(value)===v,'Preserve section '+k);
 }
 for(const [k,v] of Object.entries(pres.unchangedLocations)){
  let value=k==='The Eternal Crucible'?Object.fromEntries(Object.entries(approvedPrevious.locations[k]).filter(([f])=>f!=='hiddenInfo')):approvedPrevious.locations[k];
  const d=studioCoordinates[k];
  if(d&&digest(value)!==v){
   ck(value.x===d.after.x&&value.y===d.after.y,'Exact incoming Studio coordinates '+k);
   value={...value,...d.before};
  }
  ck(digest(value)===v,'Preserve location '+k);
 }
 console.log(JSON.stringify({status:'passed',controller:3,checks:getChecks(),scope:'Emitted bracket scripts and preservation fingerprints; semantic answers supplied, no live engine guarantee.'}));
};
