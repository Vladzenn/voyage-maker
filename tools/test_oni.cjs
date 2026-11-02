// Real emitted scripts, supplied semantic answers. This does not simulate Voyage's AI.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'oni-nation/manifest.json'),'utf8'));
let checks=0;const ck=(v,label)=>{checks++;assert.ok(v,label)};
const previous=require('./approved_expansion.cjs')(w);
ck(previous.npcs['Ilyra Stillglass'].level===100,'Sage power preserved');
const compare=(a,op,b)=>({equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b,regex:new RegExp(String(b)).test(String(a))})[op];
function context(overrides={}){
 const q={tick:50,location:"Adventurer's Guild - Glowhaven Branch",area:"Adventurer's Guild - Glowhaven Branch - Reception Counter",actions:['show available work'],level:1,badge:1,items:{},quests:{},storage:{},health:100,inScene:false,inCombat:false,inParty:false,semantic:true,...overrides};
 function check(c){let v;
  if(c.type==='game-tick')v=q.tick;
  else if(c.type==='party-location')v=q.location;
  else if(c.type==='party-area')v=q.area;
  else if(c.type==='action-text')v=c.operator?q.actions.join(' '):q.actions;
  else if(c.type==='player-level')v={Player:q.level};
  else if(c.type==='player-item'){
   const n=Object.prototype.hasOwnProperty.call(q.items,c.item)?q.items[c.item]:(c.item==='Guild Badge: '+['','Bronze','Silver','Gold','Platinum'][q.badge]?1:0);
   return c.operator?compare(n,c.operator,c.value):{Player:n};
  }else if(c.type==='quest-status')v=q.quests[c.questId]||'hidden';
  else if(c.type==='read-boolean')v=q.storage[c.key]===true;
  else if(c.type==='read-number')v=Number(q.storage[c.key]||0);
  else if(c.type==='npc-in-scene')v=q.inScene;
  else if(c.type==='npc-in-combat')v=q.inCombat;
  else if(c.type==='npc-in-party')v=c.npc==='anyPartyNPC'?{}:q.inParty;
  else if(c.type==='npc-health')v=q.health;
  else if(c.type==='story'||c.type==='action')return q.semantic;
  else throw Error('Fixture read '+c.type);
  return c.operator?compare(v,c.operator,c.value):v;
 }
 function run(name){const t=w.triggerDefinitions[name];assert.ok(t,'Missing '+name);
  if(!t.conditions.every(check))return [];
  const box={check,storage:q.storage,effects:structuredClone(t.effects),skip:false};
  if(t.script)vm.runInNewContext(t.script,box,{timeout:150});
  return box.skip?[]:Array.from(box.effects);
 }
 return {q,check,run};
}

// Preserve all twelve supplied region images and grid coordinates.
const coords=[[-1,0],[0,0],[1,0],[2,0],[-1,-1],[0,-1],[1,-1],[2,-1],[-1,-2],[0,-2],[1,-2],[2,-2]];
for(let i=1;i<=12;i++){
 const key=m.regions['Region '+i],r=w.regions[key];
 ck(r.realm==='Akitsuhara','Country region '+i);
 ck(r.x===coords[i-1][0]&&r.y===coords[i-1][1],'Incoming grid '+i);
 ck(JSON.stringify(r.images)===JSON.stringify(m.sourceRegionImages['Region '+i]),'Incoming map image/crop '+i);
}
ck(m.npcs.length>=80&&m.npcs.length<=100,'Requested launch cast');
ck(m.npcs.filter(n=>['Hagire','Koma','Suzu-no-Ura','Oroha'].includes(n)).length===4,'Small named yokai population');
for(const name of m.npcs){const n=w.npcs[name];ck(w.locations[n.currentLocation]?.areas[n.currentArea],'Actual NPC address '+name);ck(w.npcTypes[n.type],'Actual NPC type '+name);ck(!n.basicInfo.includes('works as has'),'No malformed role template '+name);}
ck(w.npcs.Hagire.level===42&&w.npcs.Hagire.initialRelationship<=-80,'Hostile midgame roaming monster');

// New starts are local and grouped before all academy faculty openings.
const starts=Object.keys(w.storyStarts),work=starts.findIndex(k=>k.includes('First Day of Work:'));
for(const name of m.storyStarts){const st=w.storyStarts[name];ck(st.name===name&&starts.indexOf(name)>4&&starts.indexOf(name)<work,'Start order/name '+name);ck(w.locations[st.locations[0]].areas[st.locationAreas[0]],'Start address '+name);
 if(name.includes('Akitsuhara:'))ck(w.regions[w.locations[st.locations[0]].region].realm==='Akitsuhara','Starts inside nation '+name);
}
for(const st of Object.values(w.storyStarts))ck(st.startingItems.filter(i=>i.item==='Mark').reduce((n,i)=>n+i.quantity,0)===1000,'One authored 1000-mark start '+st.name);
ck(!w.itemSettings.startingItems.some(i=>i.item==='Mark'),'No shared extra 18 marks');
ck(w.traitCategories['Special Talent'].maxSelections===2,'Approved talent capacity');
const professions=w.traitCategories['Profession & Useful Skills'];
ck(professions.traits.length>=90&&professions.subcategories.length>=10,'Expanded useful professions and categories');
ck(new Set(professions.subcategories.flatMap(g=>g.traits)).size===professions.traits.length,'Complete profession grouping');
const origins=w.traitCategories['Origin & Upbringing'];
ck(origins.maxSelections===1&&origins.traits.length>=26,'Expanded optional origins retain a single choice');
for(const name of origins.traits.slice(12)){
 const t=w.traits[name];ck(t.skills.length===1&&t.skills[0].modifier===1,'Modest formative skill '+name);
 ck(!t.startingItems.length&&!t.abilities.length&&!t.attributes.length,'Origin grants no estate, ability or title '+name);
}
ck(w.traits['Physical Foundations'].description.length>250&&!/grants no|no spell|no affinity|no combat/.test(w.traits['Physical Foundations'].description),'Positive Physical Foundations description');
const talentNames=w.traitCategories['Special Talent'].traits;
for(let i=0;i<talentNames.length;i++)for(let j=i+1;j<talentNames.length;j++){
 const pools=Object.fromEntries(['Health','Mana','Stamina'].map(r=>[r,w.resourceSettings[r].maxValue]));
 for(const n of [talentNames[i],talentNames[j]])for(const x of w.traits[n].resources)pools[x.resource]+=x.modifier;
 ck(Object.values(pools).every(v=>v>0),'Two talents retain positive initial resources '+talentNames[i]+' / '+talentNames[j]);
}

// Native area paths are local; the recorded road plan is connected in setting text.
for(const realm of ['Akitsuhara','The Veiled Beyond']){
 const locs=m.locations.filter(n=>w.regions[w.locations[n].region].realm===realm);
 const neighbors=n=>m.roads.filter(pair=>pair.includes(n)).map(([a,b])=>a===n?b:a);
 const seen=new Set([locs[0]]),queue=[locs[0]];
 while(queue.length)for(const to of neighbors(queue.shift())){ck(locs.includes(to),'Same-realm road '+to);if(!seen.has(to)){seen.add(to);queue.push(to);}}
 ck(seen.size===locs.length,'Connected ordinary road plan '+realm);
 for(const name of locs){
  const a=w.locations[name].areas,ids=Object.keys(a),visited=new Set([ids[0]]),pending=[ids[0]];
  while(pending.length)for(const to of a[pending.shift()].paths){ck(ids.includes(to),'Supported local area path '+to);if(!visited.has(to)){visited.add(to);pending.push(to);}}
  ck(visited.size===ids.length,'Connected interior '+name);
  for(const [id,v] of Object.entries(a))for(const to of v.paths)ck(a[to].paths.includes(id),'Interior backtracking '+id);
  for(const to of neighbors(name))ck(w.locations[name].basicInfo.includes(to),'Road destination present in actual setting '+name+' / '+to);
 }
}

// Reproduce the user's multiple-acceptance incident with all legacy offer flags already true.
let h=context();let e=h.run('gh_guild_board');
for(const x of e)if(x.type==='quest-available')h.q.quests[x.value]='available';
h.q.quests['Guild: A Parcel for the Bazaar']='available';
ck(h.q.storage.ghGuildDisplayedOffers.includes('Guild: Rats in the Cellar'),'Displayed actual rat contract');
ck(h.q.storage.ghGuildDisplayedOffers.includes('Guild: A Parcel for the Bazaar'),'Displayed parcel alternative');
const terms=e.filter(e=>e.type==='story').map(e=>e.instruction).join(' ');
ck(terms.includes('Noriko Hanesawa')&&terms.includes('Roseberry Inn')&&terms.includes('30 marks'),'Actual rat client/site/fee emitted');
ck(!e.some(e=>e.type==='quest-accept'),'Browsing accepts no contract');
for(const title of Object.keys(m.guildPlaytestFix.legacyAcceptances)){
 const tr=w.triggerDefinitions[m.guildPlaytestFix.legacyAcceptances[title]];
 for(const c of tr.conditions)if(c.type==='read-boolean')h.q.storage[c.key]=true;
}
h.q.actions=["The rats it is, then! I'll take it, pretty lady!"];
e=h.run('gh_guild_board');ck(!e.length,'Acceptance does not rotate or overwrite displayed choices');
let accepted=[];
for(const name of Object.values(m.guildPlaytestFix.legacyAcceptances))accepted.push(...h.run(name).filter(e=>e.type==='quest-accept'));
accepted.push(...h.run('oni_guild_native_choice').filter(e=>e.type==='quest-accept'));
ck(accepted.length===1&&accepted[0].value==='Guild: Rats in the Cellar','Only chosen rats accepted, no parcel/harness/washbasin');
for(const input of ['Yes.',"I don't take the rats.",'Tell me about the rats.']){
 h.q.actions=[input];accepted=[];for(const name of Object.values(m.guildPlaytestFix.legacyAcceptances))accepted.push(...h.run(name).filter(e=>e.type==='quest-accept'));accepted.push(...h.run('oni_guild_native_choice').filter(e=>e.type==='quest-accept'));
 ck(!accepted.length,'Ambiguous/refused/information-only input does not accept '+input);
}
h.q.storage.ghGuildDisplayedOffers=['Guild: A Parcel for the Bazaar'];h.q.actions=['Yes, I accept.'];
e=h.run(m.guildPlaytestFix.legacyAcceptances['Guild: A Parcel for the Bazaar']);
ck(e.filter(e=>e.type==='quest-accept').length===1,'Unambiguous yes to one real offer remains valid');
ck(w.storySettings.questGenerationGuidance.includes('ASSESSMENT SAMPLES'),'Generator separates samples from real contracts');
ck(w.parties[''].quests['Guild: Adventurer Licensure'].questDesignBrief.includes('not a live request'),'Exam uses a sample rather than a live repair job');

// Normal and once-only surprise travel use native movement and the established shared lock.
h=context({location:'Evertree Base',area:'Evertree Base - Portal Room',level:5,actions:['I enter the Akitsuhara portal'],items:{'Oni Nation Portal Key':1}});
e=h.run('oni_portal_to_direct');ck(e.some(e=>e.type==='party-location'&&e.value==='Benitsuru Transit Shrine'),'Normal outward exact position');
ck(!h.run('oni_portal_to').length,'Same tick semantic router cannot double cross');
h=context({location:'Evertree Base',area:'Evertree Base - Portal Room',level:20,actions:['I enter the Akitsuhara portal'],items:{'Oni Nation Portal Key':1}});
e=h.run('oni_portal_to_direct');ck(e.some(e=>e.type==='party-location'&&e.value==='Silken Portal Room'),'Same original level-20 surprise decision on new network route');
h.q.tick++;h.q.storage.gh_spider_entered=true;e=h.run('oni_portal_to_direct');ck(e.some(e=>e.type==='party-location'&&e.value==='Benitsuru Transit Shrine'),'Anomaly cannot recur');
h=context({location:'Benitsuru Transit Shrine',area:'Benitsuru Transit Shrine - Permit Desk',actions:['I enter the return portal']});
e=h.run('oni_portal_from_direct');ck(e.some(e=>e.type==='party-area'&&e.value==='Evertree Base - Portal Room'),'Fixed Evertree return from local staging');
h=context({location:'Moonless Torii',items:{'Restored Way Bell':1}});e=h.run('oni_soul_torii_awaken');
ck(e.some(e=>e.type==='write-boolean'&&e.key==='oni_soul_gate_awake')&&!e.some(e=>e.type==='party-location'),'Awakening permanent flag without forced entry');
h.q.items={};h.q.storage.oni_soul_gate_awake=true;e=h.run('oni_soul_torii_cross');ck(e.some(e=>e.type==='party-location'&&e.value==='Veiled Threshold'),'Opened spirit route works after bell is lost');
h=context({location:'Veiled Threshold'});e=h.run('oni_soul_torii_return');ck(e.some(e=>e.type==='party-area'&&e.value==='Moonless Torii - Torii Court'),'Local spirit return is not Evertree');
for(const overrides of [{health:0},{inScene:true},{inCombat:true},{inParty:true},{storage:{oni_hagire_route_safe:true}}]){h=context(overrides);ck(!h.run('oni_hagire_roam').length,'No roaming over an actual resolved/engaged state');}
h=context({tick:72});e=h.run('oni_hagire_roam');ck(e.length===1&&e[0].type==='npc-placement','One bounded offstage roam');
ck(!h.run('oni_hagire_roam').length,'No repeated move in same roaming interval');

console.log(JSON.stringify({status:'passed',checks,npcs:m.npcs.length,newQuests:m.quests.length+1,majorPortraits:m.majorNpcs.length,scope:'Local data and emitted-script regressions with supplied semantic answers; not live Voyage validation or playtesting.'}));
