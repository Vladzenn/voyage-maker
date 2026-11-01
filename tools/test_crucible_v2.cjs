const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
module.exports=({w,manifest,harness,ck,getChecks})=>{
 const root=path.resolve(__dirname,'..'),pres=JSON.parse(fs.readFileSync(path.join(root,'tools/crucible/revision-preservation.json'),'utf8'));
 const digest=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
 function sort(v){if(Array.isArray(v))return v.map(sort);if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])]));return v}
 const ready=h=>{h.s.action=['I am ready to begin my called bout.'];h.run('cc1_ready')};
 const bout=h=>h.c().card[h.c().index];
 const champion=h=>{h.enter();while(h.c().phase!=='closed')h.win();};
 for(const key of manifest.triggers){const t=w.triggerDefinitions[key];ck(!!t&&t.conditions.length<=5&&t.effects.length<=10,'Native trigger caps '+key);if(t.script)new vm.Script(t.script)}
 ck(!w.triggerDefinitions.cc1_review,'No review/replay controller remains');
 for(const level of [1,2,5,10,15,20,30,40,60,100,150]){
  const h=harness(level);h.enter();ck(h.c().v===2&&h.c().phase==='waiting','Card entry '+level);
  ck([2,3].includes(h.c().card.length),'Two or three actual scheduled bouts');
  ck(!h.c().matches,'No NPC bracket tree');
  ck(new Set(h.c().card.map(x=>x.opponent)).size===h.c().card.length,'Distinct opponents');
  ck(h.c().card.every(x=>x.level<=level+(level<=10?2:Math.max(4,Math.ceil(level*.3)))),'No oversized involuntary field');
  const draw=JSON.stringify(h.c().card);h.run('cc1_register');ck(JSON.stringify(h.c().card)===draw,'Repeated entry cannot redraw');
  const n=h.c().card.length;
  for(let i=0;i<n;i++){const m=bout(h);h.win();ck(m.result?.winner==='player','Actual started player bout is recorded');if(i<n-1)ck(h.c().phase==='waiting','No automatic next attack');}
  ck(h.c().phase==='closed'&&h.c().outcome==='champion','One closed title run');
  ck(Object.keys(h.c().prizes).length===1,'One owed prize');
  h.run('cc1_result_win');h.run('cc1_claim_prize');h.run('cc1_claim_prize');
  ck(h.s.items.Player['Crucible Championship Trophy']===1,'One trophy only');ck(h.s.items.Player.Mark===h.c().purse,'One native purse only');
  h.s.tick=h.c().nextTick-1;h.run('cc1_register');ck(h.c().phase==='closed','Hundred-turn break holds');
  h.s.tick++;h.run('cc1_register');ck(h.c().edition===2&&h.c().phase==='waiting','Next edition opens at boundary');
 }
 {
  const h=harness();h.enter();const m=bout(h),old=m.opponent;h.s.npcs[old].hp=0;ready(h);
  ck(h.c().phase==='waiting'&&typeof m.startedTick!=='number'&&!m.result,'Pre-start incapacity gives no victory');
  ck(m.opponent!==old&&m.replacements[0].opponent===old,'Suitable unused substitute announced');
  ck(!h.s.items.Player['Crucible Championship Trophy'],'No unearned trophy');ready(h);ck(h.c().phase==='live','Substitute requires fresh readiness');
 }
 {
  const h=harness();h.enter();for(const n of Object.values(h.s.npcs))n.hp=0;ready(h);
  ck(h.c().phase==='closed'&&h.c().outcome==='cancelled','Exhausted roster closes finitely');ck(!Object.keys(h.c().prizes).length,'No cancellation award');
 }
 {
  const h=harness();h.enter();h.s.hp.Player=0;ready(h);ck(h.c().phase==='waiting'&&!bout(h).startedTick,'Incapacitated entrant cannot start');
  h.s.hp.Player=35;ready(h);ck(h.c().phase==='live'&&bout(h).startHealth===35&&h.s.hp.Player===35,'Participation never requires full bars');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.tick++;h.s.hp.Player=0;h.s.npcs[m.opponent].hp=0;h.run('cc1_observe');
  ck(h.c().phase==='closed'&&h.c().outcome==='eliminated'&&m.result.winner==='draw','Double knockout closes without review loop');
  ck(Object.keys(h.c().care).length===1,'Double knockout owns an actual care entitlement');ck(!Object.keys(h.c().prizes).length,'Double knockout has no title prize');
  h.run('cc1_care');ck(!Object.keys(h.c().care).length,'Care can be accepted after stopped double fall');
 }
 {
  const h=harness();h.enter();ready(h);h.s.hp.Player=0;h.run('cc1_result_win');ck(h.c().outcome==='eliminated','Native incapacity beats a false semantic win');
 }
 {
  const h=harness();h.enter();const m=bout(h);h.c().phase='live';h.clock();h.run('cc1_result_win');ck(!m.result,'Result script rejects a missing start');h.run('cc1_observe');ck(h.c().outcome==='cancelled','Missing-start state closes without victory');
 }
 for(const afterWin of [false,true]){
  const h=harness();h.enter();if(afterWin)h.win();const m=bout(h),saved=JSON.stringify(h.c().card);h.s.area='The Eternal Crucible - Grand Stands';h.s.tick++;
  h.s.action=['I leave to the benches to watch until my turn.'];h.run('cc1_observe');h.run('cc1_withdraw',false);h.run('cc1_ready',false);
  ck(h.c().phase==='waiting'&&bout(h)===m&&JSON.stringify(h.c().card)===saved,'Ordinary waiting/spectating preserves entry without movement parsing');
 }
 {
  const h=harness();h.enter();h.s.action=['I withdraw from the championship and go to the benches.'];h.run('cc1_withdraw');ck(h.c().outcome==='withdrawn','Explicit entry cancellation still works with benches mentioned');
 }
 for(const live of [false,true]){
  const h=harness();h.enter();if(live)ready(h);h.s.location='Four Sages Bazaar';h.run('cc1_observe');
  ck(h.c().phase===(live?'live':'waiting'),'Movement alone is not a forfeit');
  if(live){h.run('cc1_result_loss');ck(h.c().outcome==='eliminated','An actual referee ruling can settle a started fight after departure');}
  else{h.run('cc1_withdraw');ck(h.c().outcome==='withdrawn','An explicit entry forfeit closes from any location');}
  h.s.location='The Eternal Crucible';h.s.tick++;h.run('cc1_observe');ck(h.c().phase==='closed','Returning does not reopen a settled run');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);for(const n of h.c().card)if(n.opponent!==m.opponent)h.s.npcs[n.opponent].hp=0;
  h.s.tick++;h.run('cc1_observe');ck(h.c().phase==='live'&&!m.result,'Offscreen NPC incapacity never settles player bout');
  h.run('cc1_result_loss');ck(h.c().outcome==='eliminated'&&!h.c().champion,'No unfit offscreen NPC champion is computed');
 }
 {
  const h=harness();h.enter();ready(h);const m=bout(h);h.s.area='The Eternal Crucible - Grand Stands';h.run('cc1_result_win',true);ck(!m.result,'Spectator-area prose cannot award a semantic victory');
  h.run('cc1_result_loss',true);ck(h.c().outcome==='eliminated','A real ring-out/referee loss may settle outside the ring');
 }
 {
  const h=harness();h.enter();h.win();const granted=h.s.grants.length;ready(h);ck(h.c().phase==='live'&&h.s.hp.Player===100,'Unharmed winner can skip care');
  h.run('cc1_care');ck(h.s.grants.length===granted,'No live-bout care or free supplies');
 }
 {
  const h=harness();champion(h);const old=JSON.stringify(h.c().prizes);h.s.players={Different:20};h.s.hp={Different:100};h.s.items.Different={};h.run('cc1_claim_prize');ck(JSON.stringify(h.c().prizes)===old,'Prize cannot transfer to another identity');
 }
 {
  const h=harness();h.clock();h.s.players.Second=20;h.s.hp.Second=100;h.s.items.Second={};h.run('cc1_register');ck(h.c().phase==='idle','Multiplayer never enters as one fighter');
 }
 {
  const h=harness();h.enter();ready(h);h.s.players.Second=20;h.run('cc1_observe');ck(h.c().outcome==='cancelled'&&!Object.keys(h.c().prizes).length,'Roster change closes entry without transferred win');
 }
 {
  const h=harness();h.clock();h.s.action=['I agree to a friendly match with Kōta Mibu.'];h.run('cc1_exhibition');h.win();ck(h.c().outcome==='exhibition win'&&h.c().nextTick===0&&!Object.keys(h.c().prizes).length,'Exhibition is isolated from title prizes/cooldown');
 }
 {
  const h=harness();h.clock();h.s.action=['I agree to a friendly match.'];h.run('cc1_exhibition');ck(h.c().phase==='idle','Ambiguous practice partner never becomes a random opponent');
 }
 {
  const h=harness();h.s.storage.cc1={v:1,phase:'review',edition:4,nextTick:0,history:[],care:{},prizes:{3:{owner:'Player',title:'Old cup',marks:100}},matches:[{}]};h.clock();
  ck(h.c().v===2&&h.c().outcome==='cancelled'&&!h.c().matches,'Legacy unfinished bracket migrates without fabricated result');ck(h.c().prizes[3].owner==='Player','Earned pending legacy award survives');
 }
 {
  const h=harness();h.s.location='Sepulchral Conservatory';h.s.area='Sepulchral Conservatory - Entry Rotunda';h.s.npcs['Kōta Mibu'].party=true;h.s.action=['I go to the Grafting Heart.'];h.run('cc1_grove_inner_gate');
  ck(h.s.area.endsWith('Entry Rotunda')&&!h.s.storage.cc1_grove_heart_seen,'Proposed premature move keeps actual safe area');
  h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_inner_gate_state');ck(h.s.area.endsWith('Entry Rotunda'),'State backstop restores the actual last safe area');
  ck(h.s.npcs['Kōta Mibu'].area===h.s.area,'Companions receive guard correction');
  h.s.area='Sepulchral Conservatory - Tending Gallery';h.run('cc1_grove_root',false);ck(!h.s.storage.cc1_grove_root,'Visit is not circuit completion');h.run('cc1_grove_root');delete h.s.items.Player['Rootwake Seal'];
  h.s.area='Sepulchral Conservatory - Ossuary Greenhouse';h.run('cc1_grove_mourning');h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_inner_gate');h.run('cc1_grove_inner_gate_state');ck(h.s.storage.cc1_grove_heart_seen,'Both circuits allow heart despite lost keepsake');
  h.run('cc1_grove_release',false);ck(!h.s.storage.cc1_grove_resolved,'No false release');h.run('cc1_grove_release');h.s.npcs.Threnvoss.hp=0;h.run('cc1_grove_defeat');ck(h.s.items.Player['Heartwood Remembrance']===1,'One dungeon trophy across outcomes');
 }
 {
  const h=harness();h.s.location='Evertree Base';h.s.area='Evertree Base - Portal Room';h.s.items.Player={'Crucible Championship Trophy':1};h.run('cc1_grove_discover');ck(!h.s.storage.cc1_grove_open,'Both unlock items required');
  h.s.items.Player['Silver Web Portal Key']=1;h.s.storage.ghPortalTransitTick=h.s.tick;h.run('cc1_grove_discover');ck(!h.s.storage.cc1_grove_open,'Existing portal event keeps transit priority');h.s.tick++;h.run('cc1_grove_discover');h.run('cc1_grove_enter');ck(h.s.location==='Sepulchral Portal House','Real outbound portal address');
  h.run('cc1_grove_key');h.run('cc1_grove_key');ck(h.s.items.Player['Sepulchral Portal Key']===1,'One arrival key');h.s.tick++;h.run('cc1_grove_return');ck(h.s.location==='Evertree Base'&&h.s.area==='Evertree Base - Portal Room','Return reaches exact hub');
 }
 ck(w.triggerDefinitions.cc1_grove_inner_gate.phase==='planning'&&w.triggerDefinitions.cc1_grove_inner_gate_state.phase==='state','Two documented route passes');
 {
  const h=harness();h.s.location='Sepulchral Portal House';h.s.area='Sepulchral Portal House - Return Arch';h.s.action=['I go to Threnvoss.'];h.run('cc1_grove_inner_gate');ck(h.s.location==='Sepulchral Portal House','A direct request from the entrance cannot skip to the heart');
  h.s.location='Sepulchral Conservatory';h.s.area='Sepulchral Conservatory - Grafting Heart';h.run('cc1_grove_inner_gate_state');ck(h.s.location==='Sepulchral Portal House'&&h.s.area.endsWith('Return Arch'),'Actual jump restores the remembered entrance address');
 }
 for(const [key,value] of Object.entries(manifest.preserved.npcs))ck(digest(w.npcs[key])===value,'Preserve incoming NPC '+key);
 for(const [key,value] of Object.entries(manifest.preserved.originalItems))ck(digest(w.itemTypes[key])===value,'Preserve incoming item '+key);
 for(const [key,value] of Object.entries(manifest.preserved.originalAbilities))ck(digest(w.abilities[key])===value,'Preserve incoming ability '+key);
 for(const [section,values] of Object.entries(manifest.preserved.spider))for(const [key,value] of Object.entries(values))ck(digest(w[section][key])===value,'Preserve Spider '+key);
 for(const [key,value] of Object.entries(pres.unchangedSections))ck(digest(w[key])===value,'Preserve entire incoming section '+key);
 for(const [key,value] of Object.entries(pres.unchangedLocations))ck(digest(key==='The Eternal Crucible'?Object.fromEntries(Object.entries(w.locations[key]).filter(([k])=>k!=='hiddenInfo')):w.locations[key])===value,'Preserve location media/coordinates '+key);
 console.log(JSON.stringify({status:'passed',controller:2,checks:getChecks(),scope:'Actual emitted card scripts, supplied semantic answers, regression reproductions and incoming-data fingerprints; no live Voyage or semantic-recognition guarantee.'}));
};
