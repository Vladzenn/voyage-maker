// Execute emitted scripts with explicit semantic answers; no live AI simulation.
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto'),assert=require('assert');
const root=path.resolve(__dirname,'..'),dir=path.join(__dirname,'glowhaven-expansion');
const w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const p=JSON.parse(fs.readFileSync(path.join(dir,'merge-review.json'),'utf8'));
let checks=0;const ck=(ok,label)=>{checks++;assert.ok(ok,label)};
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
ck(p.newNpcs.length===28&&w.npcs.Nerathyl.level===45&&w.npcs.Mauruun.level===60&&w.npcs.Ghorvath.level===55,'Approved cast and creature levels');
const grid=Object.values(w.regions).filter(r=>r.realm==='Glowhaven');
ck(grid.length===20&&new Set(grid.map(r=>r.x+','+r.y)).size===20,'Twenty unique tiles');
for(const x of [-2,-1,0,1,2])for(const y of [0,-1,-2,-3])ck(grid.some(r=>r.x===x&&r.y===y),'Actual 5x4 tile '+[x,y]);
for(const [name,h]of Object.entries(p.sourceNpcHashes))ck(hash(w.npcs[name])===h,'Existing NPC exact '+name);
for(const [name,h]of Object.entries(p.sourceRegionMediaHashes)){const r=w.regions[name];ck(hash({x:r.x,y:r.y,images:r.images??null,realm:r.realm})===h,'Incoming tile media/grid exact '+name)}
const artJobsFile=path.join(dir,'location-art/jobs.json'),artJobs=fs.existsSync(artJobsFile)?JSON.parse(fs.readFileSync(artJobsFile,'utf8')):[];
const addedArt=new Map(artJobs.filter(j=>p.locationArtwork?.locations.includes(j.location)).map(j=>[j.location,j]));
for(const [name,h]of Object.entries(p.sourceLocationMediaHashes)){const l=w.locations[name];ck(hash({x:l.x,y:l.y,images:addedArt.has(name)?addedArt.get(name).originalImages:(l.images??null)})===h,'Incoming location pin/media exact '+name)}
for(const [name,h]of Object.entries(p.protectedTriggerHashes))ck(hash(w.triggerDefinitions[name])===h,'Old trigger exact '+name);
ck(hash(w.parties[''].arcs)===p.protectedArcsHash,'No extra global arc checks');
for(const [name,l]of Object.entries(w.locations))ck(w.regions[l.region],'Resolved location parent '+name);
ck(w.locations.Brookmeadow.region==='Brookmeadow Vale','Starter village repaired');
const hosted=JSON.parse(fs.readFileSync(path.join(dir,'hosted-portraits.json'),'utf8')),urls=new Set();
for(const name of p.newNpcs){const n=w.npcs[name],r=hosted[name];
 ck(n.name===name&&w.locations[n.currentLocation].areas[n.currentArea],'Real card address '+name);
 ck(w.npcTypes[n.type]&&(!n.faction||w.factions[n.faction]),'Actual type and optional faction '+name);
 ck(n.portraitUrl===r.url&&r.name===name&&path.basename(r.file,'.png')===name,'Exact portrait identity '+name);
 ck(!/\b(?:authored|trigger|save file|generation|off.stage)\b/i.test(n.basicInfo+' '+n.abilities.join(' ')),'Natural public card '+name);
 urls.add(n.portraitUrl);
 const f=path.join(root,r.file);if(fs.existsSync(f))ck(crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex')===r.sha256,'Actual uploaded PNG hash '+name);
}
ck(urls.size===28,'No shared/crossed cast portraits');
const q=w.parties[''].quests,followups=new Map();
for(const title of p.contents.quests){const a=q[title];
 ck(a.status==='hidden'&&a.detailType==='detailed'&&a.completionCondition.type==='story','Native typed quest '+title);
 ck(w.npcs[a.questSource]&&w.locations[a.questLocation],'Canonical client/place '+title);
 ck(a.onCompleteEffects.filter(e=>e.type==='item-add'&&e.item==='Mark').length===1,'One payout owner '+title);
 for(const e of a.onCompleteEffects)if(e.type==='quest-init'){ck(q[e.value],'Real follow-up '+e.value);followups.set(e.value,title);ck(!a.conclusive,'Intermediate stage is not the arc ending '+title)}
 ck(!Object.values(w.triggerDefinitions).some(t=>t.effects.some(e=>['quest-complete','quest-progress'].includes(e.type)&&(e.questId===title||e.value===title))),'No competing completion owner '+title);
}
ck(followups.size===4&&p.contents.localOffers.length===8&&p.contents.guildJobs.length===12,'Complete discovery routes for all 24 new quests');
for(const title of p.academicRevamp.newNativeAssessments){ck(q[title].completionCondition.type==='story','Typed classroom assessment '+title);ck(Object.values(q).some(a=>a.onCompleteEffects?.some(e=>e.type==='quest-init'&&e.value===title)),'Assignment has a native producer '+title)}
for(const school of ['Phoenix Wing','Gryffin Tail','Dragon Hoard','Hydra Head']){const st=Object.values(w.storyStarts).find(s=>s.name.includes(school+': First Day'));ck(st.startingQuests.includes('Find Afternoon Work')&&st.startingQuests.includes('Visit the Glowhaven Guild'),'Suggestion goals retained '+school)}
ck(w.traits['Physical Foundations'].skills.some(s=>s.skill==='Guarded Combat'&&s.modifier===1),'Guarded foundation restored');
ck(w.traits['Self-Taught Spell Experimenter'].skills.some(s=>s.skill==='spellcraft'&&s.modifier===1),'Spellcraft experience selectable');
const cmp=(a,op,b)=>({equals:a===b,greaterThan:a>b,greaterThanOrEqual:a>=b,regex:new RegExp(String(b)).test(String(a))})[op];
function ctx(overrides={}){
 const s={tick:1,location:'Bluecoil Rest',realm:'Glowhaven',health:100,scene:true,combat:false,party:false,storage:{},quests:{},semantic:true,semTitle:null,...overrides};let queries=0;
 function check(c){let v;
  if(c.type==='game-tick')v=s.tick;else if(c.type==='party-location')v=s.location;else if(c.type==='party-realm')v=s.realm;
  else if(c.type==='npc-health')v=s.health;else if(c.type==='npc-in-scene')v=s.scene;else if(c.type==='npc-in-combat')v=s.combat;else if(c.type==='npc-in-party')v=s.party;
  else if(c.type==='read-boolean')v=s.storage[c.key]===true;else if(c.type==='quest-status')v=s.quests[c.questId]||'hidden';else if(c.type==='action-text')v=s.text||'';
  else if(c.type==='story')v=s.story||'';else if(c.type==='action')v=[s.text||''];
  else throw Error('Unimplemented '+c.type);
  return c.operator?cmp(v,c.operator,c.value):v;
 }
 function run(id){const t=w.triggerDefinitions[id];if(!t.conditions.every(c=>{if(c.type==='story'||c.type==='action'){queries++;return s.semTitle?c.query.includes(s.semTitle):s.semantic}return check(c)}))return [];
  const box={check,storage:s.storage,effects:structuredClone(t.effects),skip:false};if(t.script)vm.runInNewContext(t.script,box,{timeout:150});
  if(box.skip)return [];for(const e of box.effects)if(e.type==='write-boolean')s.storage[e.key]=e.value;return Array.from(box.effects);
 }
 return {s,run,queries:()=>queries};
}
const variants=w.npcs.Nerathyl.portraits;ck(Object.keys(variants).length===2&&w.npcs.Nerathyl.portraitUrl===variants.Asleep&&variants.Awake!==variants.Asleep,'Two native portrait states, sleeping default');
let h=ctx();ck(h.run('ghx_serpent_wakes').some(e=>e.type==='npc-portrait'&&e.value==='Awake'),'Actual wake switches awake');
ck(!h.run('ghx_serpent_wakes').length,'No repeated wake switch');
ck(h.run('ghx_serpent_sleeps').some(e=>e.type==='npc-portrait'&&e.value==='Asleep'),'Actual resettling switches asleep');
ck(!ctx({semantic:false}).run('ghx_serpent_wakes').length,'Observation/intent does not wake');
ck(!ctx({health:0}).run('ghx_serpent_wakes').length,'No waking dead serpent');
ck(!ctx({scene:false}).run('ghx_serpent_wakes').length,'No distant portrait switch');
h=ctx({storage:{ghxSerpentAwake:true},semantic:false});ck(!h.run('ghx_serpent_sleeps').length&&h.s.storage.ghxSerpentAwake,'Return visit does not reset awake state');
for(const tick of [1,24,48,120]){h=ctx({tick,scene:false});const e=h.run('ghx_kraken_roam');ck(e.length===1&&['Splinterwake Wreck - Deepwater Edge','Moonarch Isle - Offshore Drop'].includes(e[0].area),'Bounded deepwater route '+tick);ck(!h.run('ghx_kraken_roam').length,'No duplicate move within slot')}
for(const guard of [{scene:true},{scene:false,combat:true},{scene:false,party:true},{scene:false,health:0},{scene:false,quests:{'Guild: Ghorvath at the Deepwater Edge':'completed'}}])ck(!ctx(guard).run('ghx_kraken_roam').length,'Kraken scheduling guard '+JSON.stringify(guard));
h=ctx({scene:false,health:0});h.run('ghx_kraken_roam');h.s.health=100;h.s.tick=100;ck(!h.run('ghx_kraken_roam').length,'Defeat latch prevents later resurrection by schedule');
for(const [title,client,place]of p.contents.localOffers){const id=Object.keys(w.triggerDefinitions).find(k=>k.startsWith('ghx_local_commissions')&&w.triggerDefinitions[k].conditions.some(c=>c.questId===title));h=ctx({location:place,semTitle:title});const e=h.run(id);ck(e.some(v=>v.type==='quest-init'&&v.value===title)&&e.filter(v=>v.type==='quest-init').length===1,'Exact local offer '+title);ck(!e.some(v=>['quest-accept','item-add'].includes(v.type)),'Offer is not acceptance/payment '+title);h.s.quests[title]='completed';ck(!h.run(id).some(v=>v.value===title),'No respawn completed personal work '+title)}
ck(!ctx({location:'Starlark Abbey',semantic:false}).run('ghx_local_commissions').length,'No quest spam from arrival/greeting');
ck(!ctx({location:'The Eternal Crucible'}).run('ghx_local_commissions').length,'Local dispatcher not active at unrelated arena');
for(const t of Object.values(w.triggerDefinitions))for(const c of t.conditions)if(typeof c.value==='string')ck(c.value.length<=100,'Studio string condition limit '+t.name);
const offsite=ctx({location:'The Eternal Crucible'});offsite.run('ghx_local_commissions');ck(offsite.queries()===0,'Unrelated location performs zero local-offer semantic checks');
if(p.locationArtwork?.count){
 const art=JSON.parse(fs.readFileSync(path.join(dir,'location-art/hosted.json'),'utf8'));const allUrls=new Set();
 ck(addedArt.size===14,'Exactly one shot for each new location');
 for(const [name,j]of addedArt){const shot=w.locations[name].images.establishingShot,r=art[name];ck(shot.imageUrl===r.url&&r.target==='LOCATION_IMAGE'&&path.basename(r.file,'.png')===name,'Location art exact identity '+name);ck(shot.crop.zoom===100&&shot.crop.focus.x===50&&shot.crop.focus.y===50,'Complete native crop '+name);allUrls.add(r.url)}
 ck(allUrls.size===14,'Fourteen distinct location shots');
}
console.log(JSON.stringify({status:'passed',checks,newNpcs:28,portraits:29,newQuests:28,protectedExistingNpcs:p.existingNpcsExact,livePlaytest:false}));
