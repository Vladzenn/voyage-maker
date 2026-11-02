// Exercise the real board script against changing rank, level and quest state.
// Semantic completion is NOT simulated: live model recognition remains a playtest.
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'..');
const w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'fieldwork/manifest.json'),'utf8'));
const currencyDelta=JSON.parse(fs.readFileSync(path.join(__dirname,'currency/approved-description-delta.json'),'utf8'));
const quests=w.parties[''].quests;let checks=0;
const ck=(v,label)=>{checks++;if(!v)throw Error(label)};
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const digest=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
function run({rank=1,level=1,otherLevel=null,cursor=0,text='',statuses={},storage={}}={}){
 const effects=[],state={q20_board_cursor:cursor,...storage};
 const badge=['Bronze','Silver','Gold','Platinum'][rank-1];
 function check(c){
  if(c.type==='game-tick')return 100;
  if(c.type==='player-level')return {Player:level,...(otherLevel===null?{}:{Guest:otherLevel})};
  if(c.type==='player-item')return {Player:c.item==='Guild Badge: '+badge?1:0};
  if(c.type==='quest-status')return statuses[c.questId]||'hidden';
  if(c.type==='action-text')return [text];
  throw Error(c.type);
 }
 vm.runInNewContext(w.triggerDefinitions.gh_guild_board.script,{check,storage:state,effects},{timeout:100});
 return {effects,storage:state,offers:effects.filter(e=>e.type==='quest-init').map(e=>e.value)};
}
const first=run();
ck(first.offers.includes('Guild: Rats in the Cellar'),'First browsing includes simple combat');
ck(first.offers.includes('Guild: A Parcel for the Bazaar'),'First browsing retains a noncombat choice');
ck(!first.effects.some(e=>e.type==='quest-accept'||e.type==='item-add'),'Browsing grants neither acceptance nor rewards');
ck(!run({rank:0}).offers.length,'No licensed postings without a held badge');
const row=Object.fromEntries(m.jobs.map(j=>[j.title,j]));
const rec=Object.fromEntries(m.jobs.map(j=>[j.title,j.recommendedLevel]));
for(const level of [1,3,5,6,7,9,10,14,15,18,30])for(let cursor=0;cursor<50;cursor+=2){
 const r=run({rank:4,level,cursor});
 ck(r.offers.length<=2,'Small board selection');
 ck(new Set(r.offers).size===r.offers.length,'Distinct offers');
 for(const title of r.offers)if(row[title]){
  ck(row[title].band<=level,'Band is unlocked '+title+'/'+level);
  ck(rec[title]<=level+(level<10?2:5),'Routine new job fits human level '+title+'/'+level);
 }
}
for(const [level,band]of [[7,7],[15,15]]){
 const r=run({rank:2,level});
 ck(r.offers.some(t=>row[t]?.band===band),'New work appears immediately at level '+level);
}
ck(run({rank:1,level:15}).offers.some(t=>row[t]?.band===15),'Experienced Bronze holder still has new work');
ck(run({rank:4,level:100,otherLevel:1}).offers.every(t=>!row[t]||row[t].band===1),'Weakest human sets routine band');
const hard=run({level:1,rank:2,text:'Show Do Not Meet Its Eyes'});
ck(hard.offers.includes('Guild: Do Not Meet Its Eyes'),'Deliberate named harder job may be opened');
ck(hard.effects.some(e=>e.type==='story'&&e.instruction.includes('explain its actual danger')),'Harder choice gets warning');
ck(!run({rank:1,level:30,text:'Show Do Not Meet Its Eyes'}).offers.includes('Guild: Do Not Meet Its Eyes'),'Named request does not bypass badge');
const unavailable=Object.fromEntries(m.jobs.map(j=>[j.title,'accepted']));
ck(run({rank:4,level:30,statuses:unavailable}).offers.every(t=>!row[t]),'Accepted work is not reoffered');
const finished=Object.fromEntries(m.jobs.map(j=>[j.title,'completed']));
ck(run({rank:4,level:30,statuses:finished}).offers.every(t=>!row[t]),'Finite completed work is not respawned');
for(const j of m.jobs){
 const q=quests[j.title];
 ck(q.detailType==='detailed'&&q.status==='hidden','Native finite quest '+j.title);
 ck(q.completionCondition?.type==='story'&&typeof q.completionCondition.query==='string','Typed single completion owner '+j.title);
 ck(w.npcs[q.questSource]&&w.locations[q.questLocation].areas[j.area],'Real client and address '+j.title);
 ck(q.onCompleteEffects.filter(e=>e.type==='item-add'&&e.item==='Mark').length===1,'One payment '+j.title);
 ck(q.onCompleteEffects.filter(e=>e.type==='item-add'&&e.item==='Guild Service Credit').length===1,'One service credit '+j.title);
 ck(!Object.keys(w.triggerDefinitions).some(k=>k.startsWith('fw_')),'No per-job trigger state machines');
}
for(const [k,v]of Object.entries(m.preserved.originalQuests)){
 const exclude=k==='Guild: Boars at the Watercourse'?['questDesignBrief','questStatement']:m.revisedBriefs.includes(k)?['questDesignBrief']:[];
 ck(digest(Object.fromEntries(Object.entries(quests[k]).filter(([f])=>!exclude.includes(f))))===v,'Old quest checks/effects/untouched prose '+k);
}
for(const [k,v]of Object.entries(m.preserved.otherTriggers))ck(digest(w.triggerDefinitions[k])===v,'Existing event/settlement '+k);
for(const [k,v]of Object.entries(m.preserved.untouchedSections)){
 // Permit only the two exact approved currency descriptions, not a new section baseline.
 if(currencyDelta[k]&&digest(w[k])!==v){
  const d=currencyDelta[k],section=structuredClone(w[k]);
  ck(section[d.entry]?.[d.field]===d.after,'Exact approved currency description '+k);
  section[d.entry][d.field]=d.before;
  ck(digest(section)===v,'Untouched section except approved currency description '+k);
 }else ck(digest(w[k])===v,'Untouched section '+k);
}
for(const [k,v]of Object.entries(m.preserved.originalTypes))ck(digest(w.npcTypes[k])===v,'Existing creature type '+k);
const cellar=w.locations['Roseberry Inn'].areas[m.addedArea];
ck(cellar.paths.includes('Roseberry Inn - Kitchen Passage')&&w.locations['Roseberry Inn'].areas['Roseberry Inn - Kitchen Passage'].paths.includes(m.addedArea),'Cellar supports normal entry/backtracking');
console.log(JSON.stringify({status:'passed',checks,addedQuests:m.jobs.length,addedTypes:m.types.length,rootTriggers:Object.keys(w.triggerDefinitions).length,livePlaytest:false}));
