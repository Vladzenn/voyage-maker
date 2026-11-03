// Local deterministic fixtures. Semantic answers are supplied, not tested as LLM behavior.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const world=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft','WorldAlpha - World.json'),'utf8'));
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'adventurers','manifest.json'),'utf8'));
// The user renamed this existing event in Studio; preserve the new identity.
manifest.triggers=manifest.triggers.map(k=>k==='ad34_ironman_final_outcome'&&world.triggerDefinitions.ad34_permadeath_final_outcome?'ad34_permadeath_final_outcome':k);
let checks=0;
function ck(ok,msg){checks++;assert.ok(ok,msg)}
function compare(a,op,b){return ({equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b,contains:Array.isArray(a)?a.includes(b):String(a).includes(b),notContains:Array.isArray(a)?!a.includes(b):!String(a).includes(b),regex:new RegExp(String(b)).test(String(a))})[op]}
function context(overrides={}){
 const ctx={tick:20,day:1,time:'Morning',location:'Four Sages Bazaar',area:'Four Sages Bazaar - Four Sages Fountain',
  realm:'Glowhaven',region:'Glowhaven',players:{Alice:{level:5,Health:100,items:{Mark:100},traits:[]}},
  npcStates:{},scene:[],party:[],combat:[],actions:['look around'],story:'',quests:{},storage:{},...overrides};
 ctx.region=world.locations[ctx.location]?.region || ctx.region;
 ctx.realm=world.regions[ctx.region]?.realm || ctx.realm;
 function check(c){
  let raw;
  const players=Object.entries(ctx.players);
  switch(c.type){
   case 'game-tick':raw=ctx.tick;break;case 'day':raw=ctx.day;break;case 'time-of-day':raw=ctx.time;break;
   case 'party-location':raw=ctx.location;break;case 'party-area':raw=ctx.area;break;
   case 'party-region':raw=ctx.region;break;case 'party-realm':raw=ctx.realm;break;
   case 'action-text':case 'action':raw=ctx.actions;break;case 'story-text':case 'story':raw=ctx.story;break;
   case 'player-level':raw=Object.fromEntries(players.map(([k,p])=>[k,p.level]));break;
   case 'player-resource':raw=Object.fromEntries(players.map(([k,p])=>[k,p[c.resource]??0]));break;
   case 'player-traits':raw=Object.fromEntries(players.map(([k,p])=>[k,p.traits]));break;
   case 'player-item':raw=Object.fromEntries(players.map(([k,p])=>[k,p.items[c.item]||0]));break;
   case 'skill-value':raw=Object.fromEntries(players.map(([k,p])=>[k,p.skills?.[c.skill]||0]));break;
   case 'action-success-level':raw=Object.fromEntries(players.map(([k,p])=>[k,p.outcome||'success']));break;
   case 'quest-status':raw=ctx.quests[c.questId]||'hidden';break;
   case 'quests-completed':raw=Object.keys(ctx.quests).filter(k=>ctx.quests[k]==='completed');break;
   case 'story-start':raw=ctx.start||'';break;case 'known-entity':raw=(ctx.known||[]).includes(c.entity);break;
   case 'narrative-event-status':raw='inactive';break;
   case 'read-boolean':raw=typeof ctx.storage[c.key]==='boolean'?ctx.storage[c.key]:false;break;
   case 'read-number':raw=typeof ctx.storage[c.key]==='number'?ctx.storage[c.key]:0;break;
   case 'read-string':raw=typeof ctx.storage[c.key]==='string'?ctx.storage[c.key]:'';break;
   case 'read-array':raw=Array.isArray(ctx.storage[c.key])?ctx.storage[c.key]:[];break;
   default:
    if(!c.type.startsWith('npc-'))throw Error('Unimplemented fixture read '+c.type);
    const one=npc=>{
     const n=ctx.npcStates[npc]||world.npcs[npc]||{};
     switch(c.type){
      case 'npc-health':return n.fixtureHealth??(n.level?100:undefined);
      case 'npc-health-percent':return n.fixtureHealth===0?0:100;
      case 'npc-in-scene':return ctx.scene.includes(npc);
      case 'npc-in-party':return ctx.party.includes(npc);
      case 'npc-in-combat':return ctx.combat.includes(npc);
      case 'npc-location':return n.currentLocation;
      case 'npc-area':return n.currentArea;
      case 'npc-region':return world.locations[n.currentLocation]?.region;
      case 'npc-realm':return world.regions[world.locations[n.currentLocation]?.region]?.realm;
      case 'npc-relationship':return 0;
      case 'npc-relationship-stage':return 'Neutral';
      case 'npc-type':return n.type;
      default:throw Error('Unimplemented NPC fixture '+c.type);
     }
    };
    raw=c.npc==='anySceneNPC'?Object.fromEntries(ctx.scene.map(n=>[n,one(n)])):
        c.npc==='anyPartyNPC'?Object.fromEntries(ctx.party.map(n=>[n,one(n)])):one(c.npc);
  }
  if(!c.operator)return raw;
  if(c.type==='action-success-level'){const ranks=['impossible','critical failure','failure','mixed results','basic success','success','great success','critical success'];return Object.values(raw).some(v=>compare(ranks.indexOf(v),c.operator,ranks.indexOf(c.value)))}
  if(c.type==='action-text')return ctx.actions.some(x=>compare(x,c.operator,c.value));
  if(raw && typeof raw==='object'&&!Array.isArray(raw))return Object.values(raw).some(v=>compare(v,c.operator,c.value));
  return compare(raw,c.operator,c.value);
 }
 return {ctx,check};
}
function run(name,overrides={}){
 const {ctx,check}=context(overrides),tr=world.triggerDefinitions[name];
 const sandbox={check,storage:ctx.storage,effects:[],skip:false,triggers:{},console:{log(){},warn(){},error(){}}};
 vm.runInNewContext(tr.script,sandbox,{timeout:100});
 ck(sandbox.effects.length<=10,name+' respects effect budget');
 return {...sandbox,ctx};
}

// Tours move the same actual NPCs, never the party; all blocking conditions hold.
for(let day=1;day<=8;day++)for(const time of ['Morning','Evening']){
 const out=run('ad34_touring_cast',{day,time});
 for(const e of out.effects){
  ck(e.type==='npc-placement'&&e.operation==='moveTo','Tour changes only NPC placement');
  ck(world.locations[e.location]?.areas[e.area],'Real tour address');
  if(e.npc==='Adoha Aonuma'&&world.regions[world.locations[e.location].region].realm==='Asterveil')ck(e.location==='Asterveil Canopy','Adoha stays inside the settlement');
 }
}
for(const name of Object.keys(manifest.routes))for(const block of ['scene','party','combat','dead','held']){
 const opts={day:3};
 if(block==='dead')opts.npcStates={[name]:{...world.npcs[name],fixtureHealth:0}};
 else if(block==='held')opts.storage={['ad34_hold_'+name]:true};else opts[block]=[name];
 ck(!run('ad34_touring_cast',opts).effects.some(e=>e.npc===name),'Tour pause '+name+'/'+block);
}

// The repair looks up actual runtime quest keys/names, including unknown generated titles.
const title='A Generated Quest Not in the Export';
let out=run('ad34_quest_repair',{actions:['quest done: '+title],quests:{[title]:'accepted'}});
ck(out.effects.some(e=>e.type==='quest-complete'&&e.questId===title),'Accepted runtime quest completes');
ck(!out.effects.some(e=>['item-add','player-resource','quest-accept','quest-init'].includes(e.type)),'Repair does not pay or accept independently');
for(const status of ['hidden','available','planned','completed','rejected','abandoned']){
 out=run('ad34_quest_repair',{actions:['quest done: '+title],quests:{[title]:status}});
 ck(!out.effects.some(e=>e.type==='quest-complete'),'Repair refuses '+status);
}
for(const input of ['I say "quest done: '+title+'"','quest done: '+title+'\nand attack','I want to finish a quest','quest done:']){
 ck(!run('ad34_quest_repair',{actions:[input],quests:{[title]:'accepted'}}).effects.length,'No incidental command match');
}
out=run('ad34_quest_repair',{actions:['quest done: '+title,'quest done: '+title],quests:{[title]:'accepted'}});
ck(out.effects.filter(e=>e.type==='quest-complete').length===1,'Duplicate commands settle once');

// Public opportunities are sparse, public and do not change quest acceptance.
out=run('ad34_public_opportunities');
ck(out.effects.length===1&&out.effects[0].type==='story','One public lead only');
ck(!out.effects.some(e=>e.type.startsWith('quest-')),'Public lead never enters or accepts a quest');
let again=run('ad34_public_opportunities',{tick:21,storage:out.storage,actions:['listen for news']});
ck(!again.effects.length,'Shared cooldown suppresses flood');
for(const actions of [['attack the guard'],['rest'],['buy bread'],['kiss my partner'],['enter the portal']]){
 ck(!run('ad34_public_opportunities',{actions}).effects.length,'No public interruption during '+actions);
}
ck(!run('ad34_public_opportunities',{scene:['Renpei Sugita'],combat:['Renpei Sugita']}).effects.length,'No public lead during real combat');
out=run('ad34_public_opportunities',{quests:{'A Fair Measure':'completed'}});
ck(!out.effects.length,'Solved public situation not repeated');

// New offers have a dynamic writer; only one private job is eligible at once.
for(const title of manifest.quests){
 const q=world.parties[''].quests[title];
 ck(q.completionCondition.type==='story'&&q.completionCondition.query.includes(q.mainObjective),'Concrete final objective repeated '+title);
 ck(!manifest.triggers.some(k=>(world.triggerDefinitions[k].effects||[]).some(e=>e.type==='quest-complete'&&e.questId===title)),'Native completion sole owner '+title);
 if(manifest.guildJobs.some(j=>j.title===title))continue;
 const offer=manifest.triggers.map(k=>world.triggerDefinitions[k]).find(t=>t.effects.some(e=>e.type==='quest-init'&&e.value===title));
 const loc=offer.conditions.find(c=>c.type==='party-location').value;
 out=run('ad34_scene_dispatch',{location:loc,players:{Alice:{level:50,Health:100,items:{Mark:100},traits:[]}},scene:[q.questSource],actions:['Ask '+q.questSource+' about work']});
 ck(out.storage.ad34_offer_target===title,'Offer flag has actual writer '+title);
 out=run('ad34_scene_dispatch',{location:loc,players:{Alice:{level:50,Health:100,items:{Mark:100},traits:[]}},scene:[q.questSource],actions:['Yes, I will do that.'],story:'The current offer is '+title+'.'});
 ck(out.storage.ad34_offer_target===title,'Natural follow-up keeps specific private offer '+title);
}
const legacyTriggers=manifest.modifiedExistingTriggers.filter(k=>k.startsWith('q20_'));
for(const name of legacyTriggers){
 const tr=world.triggerDefinitions[name],title=tr.conditions.find(c=>c.type==='quest-status').questId;
 const source=world.parties[''].quests[title].questSource;
 out=run('ad34_scene_dispatch',{location:'Asterveil Canopy',scene:[source],actions:['Yes, I will do that.'],story:'The current offer is '+title+'.'});
 ck(out.storage.ad34_legacy_offer===title,'Natural yes has a real conversation gate '+title);
 ck(tr.phase==='state'&&tr.conditions.some(c=>c.key==='ad34_legacy_offer'&&c.value===title),'Typed gate follows planning dispatcher '+title);
}

// Returning clients acknowledge one actual result, never repeat rewards or another job.
out=run('ad34_returning_clients',{location:"Adventurer's Guild - Glowhaven Branch",scene:['Komugi Hanabishi'],quests:{'Guild: Boars at the Watercourse':'completed'}});
ck(out.effects.length===1&&out.effects[0].type==='story','Completed work can receive one client acknowledgment');
ck(!out.effects.some(e=>e.type.startsWith('quest-')||e.type==='item-add'),'Acknowledgment creates no work or payment');
again=run('ad34_returning_clients',{tick:40,location:"Adventurer's Guild - Glowhaven Branch",scene:['Komugi Hanabishi'],quests:{'Guild: Boars at the Watercourse':'completed'},storage:out.storage});
ck(!again.effects.length,'Same completed work is acknowledged once');
for(const status of ['hidden','available','accepted']){
 ck(!run('ad34_returning_clients',{location:"Adventurer's Guild - Glowhaven Branch",scene:['Komugi Hanabishi'],quests:{'Guild: Boars at the Watercourse':status}}).effects.length,'Client greeting requires completion '+status);
}
ck(!run('ad34_returning_clients',{location:"Adventurer's Guild - Glowhaven Branch",scene:['Komugi Hanabishi'],quests:{'Guild: Boars at the Watercourse':'completed'},storage:{ad34_last_public_tick:19}}).effects.length,'Client and public opportunities share pacing');

for(const p of manifest.properties){
 const tr=world.triggerDefinitions['ad34_property_'+p.id];
 ck(tr.scope==='player','Property is payer-scoped');
 ck(tr.effects.filter(e=>e.type==='item-remove'&&e.item==='Mark'&&e.quantity===p.price&&e.target==='satisfyingPlayers').length===1,'Exact one payment '+p.id);
 ck(tr.effects.filter(e=>e.type==='item-add'&&e.item===p.key&&e.quantity===1&&e.target==='satisfyingPlayers').length===1,'One actual key '+p.id);
 ck(tr.conditions.some(c=>c.type==='player-item'&&c.item===p.key&&c.value===0),'No duplicate key '+p.id);
 ck(!world.itemTypes[p.key].bonuses.length,'Property memory item has no stat bonus');
 ck(world.locations[p.location].areas[p.area],'Property is an area in an existing location');
 const low=context({players:{Alice:{level:5,Health:100,items:{Mark:p.price-1},traits:[]}}});
 ck(!low.check(tr.conditions.find(c=>c.type==='player-item'&&c.item==='Mark')),'Cannot buy without actual funds');
}
for(const [tier,t] of Object.entries(world.itemSettings.tiers)){
 ck(t.bonusPolicy.refinedMaximumPicks>=t.bonusPolicy.initialMaximumPicks,'Refinement policy '+tier);
 ck(t.bonusPolicy.allowedBonuses.length<=100,'Bounded policy list '+tier);
 ck(!t.bonusPolicy.allowedBonuses.some(b=>['Time Magic','Renown','Infamy'].includes(b.variable)),'No forbidden generated bonus '+tier);
 for(const b of t.bonusPolicy.allowedBonuses)ck(b.min<=b.max,'Ordered per-pick range');
}
ck(world.npcs['Ilyra Stillglass'].level===100,'Ilyra stays 100');
ck(world.npcs['Ragnar Leonhart'].level===67,'Ragnar stays 67');
for(const n of Object.values(world.npcs).filter(n=>n.type==='Headmaster'))ck(n.level>=28&&n.level<=32,'Administrative office not level 70');
ck(world.death.permadeath===false,'Normal world still supports ordinary recovery');

// Static eligibility probe, not an engine trace. Scripts may further gate some candidates.
const scenarios=[
 ['Academy first day',{location:'Phoenix Wing Academy',scene:['Haruki Saitō']}],
 ['Guild browsing',{location:"Adventurer's Guild - Glowhaven Branch",scene:['Komugi Hanabishi'],actions:['browse guild work']}],
 ['Bazaar quiet',{location:'Four Sages Bazaar'}],
 ['Lodge arrival',{location:'Whitepass Caravan Lodge',realm:'Drakenspire',region:'Drakenspire Highlands',scene:['Daigo Kisaragi']}],
 ['Canopy fieldwork',{location:'Asterveil Canopy',realm:'Asterveil',region:'Cloudbloom Reaches',scene:['Suzuha Midorise']}],
 ['Canopy specific offer',{location:'Asterveil Canopy',realm:'Asterveil',region:'Cloudbloom Reaches',scene:['Sakuya Tomonari','Suzuha Midorise'],actions:['Yes, I accept A Road Made of Air: The Far End'],story:'A Road Made of Air: The Far End is the current offer.'}],
 ['Prison visit',{location:'Prison Visiting Hall',realm:'Wraith Island Prison',region:'Wraith Island Prison'}],
 ['Bronze job active',{location:'Pinewater River',quests:{'Guild: Boars at the Watercourse':'accepted'}}]
];
const budget=[];
if(world.realms.Akitsuhara)scenarios.push(
 ['Benitsuru guild browsing',{location:"Adventurer's Guild - Benitsuru Branch",realm:'Akitsuhara',region:'Benitsuru Basin',scene:['Hiyori Mitsuba'],actions:['browse local work']}],
 ['Evertree travel desk',{location:'Evertree Base',area:'Evertree Base - Portal Room',actions:['ask for a journey to Akitsuhara']}],
 ['Moonless Torii awakened',{location:'Moonless Torii',realm:'Akitsuhara',region:'Lanternwood Border',storage:{oni_soul_gate_awake:true}}],
 ['Veiled threshold',{location:'Veiled Threshold',realm:'The Veiled Beyond',region:'Veiled Cedar Reach'}]
);
if(world.triggerDefinitions.cc1_register)scenarios.push(
 ['Crucible registration',{location:'The Eternal Crucible',area:'The Eternal Crucible - Competitor Lounge',scene:['Hina Wakabayashi'],storage:{cc1_phase:'idle'}}],
 ['Crucible live bout',{location:'The Eternal Crucible',area:'The Eternal Crucible - Pillar Court',scene:['Kōta Mibu','Shōgo Mizutani'],storage:{cc1_phase:'live',cc1_active:true}}],
 ['Crucible between bouts',{location:'The Eternal Crucible',area:'The Eternal Crucible - Infirmary',scene:['Nozomi Hayase'],storage:{cc1_phase:'waiting',cc1_active:true,cc1_care:true}}],
 ['Conservatory tending wing',{location:'Sepulchral Conservatory',area:'Sepulchral Conservatory - Tending Gallery',realm:'The Sepulchral Conservatory',region:'Sepulchral Gardens'}],
 ['Conservatory heart',{location:'Sepulchral Conservatory',area:'Sepulchral Conservatory - Grafting Heart',realm:'The Sepulchral Conservatory',region:'Sepulchral Gardens',scene:['Threnvoss'],storage:{cc1_grove_root:true,cc1_grove_mourning:true,cc1_grove_heart_seen:true}}]
);
if(world.skills.Fishing){
 const angler={level:5,Health:100,items:{Mark:100,'Angler’s Rod':1,'Angler’s Bait Portion':3},traits:[],skills:{Fishing:0},outcome:'success'};
 scenarios.push(
  ['River angler',{location:'Pinewater River',area:'Pinewater River - River Bend',actions:['I fish with my line.'],players:{Alice:angler}}],
  ['Estuary angler',{location:'Greenrush Estuary',area:'Greenrush Estuary - Reedwalk',actions:['I fish with bait.'],players:{Alice:angler}}],
  ['Reef angler',{location:'Gullwatch Reefs',area:'Gullwatch Reefs - Boat Shelf',actions:['I cast my line.'],players:{Alice:angler}}],
  ['Ship angler',{location:'The Gilded Albatross',area:'The Gilded Albatross - Main Deck',actions:['I fish over the rail.'],players:{Alice:angler}}],
  ['Foreign lake angler',{location:'Glassmere Basin',area:'Glassmere Basin - Shore Stones',actions:['I fish with bait.'],players:{Alice:angler}}],
  ['Future realm angler',{location:'Future Lake',area:'Future Lake - Shore',region:'Future Region',realm:'Future Realm',actions:['I cast my line.'],players:{Alice:angler}}],
  ['Crucible with fishing tackle',{location:'The Eternal Crucible',area:'The Eternal Crucible - Pillar Court',actions:['I cast Firebolt.'],scene:['Kōta Mibu','Shōgo Mizutani'],storage:{cc1_phase:'live',cc1_active:true},players:{Alice:angler}}]
 );
}
for(const [name,opts] of scenarios){
 const routed=run('ad34_scene_dispatch',opts);
 const {ctx,check}=context({...opts,storage:routed.storage});let eligible=0;const names=[];
 for(const [key,t] of Object.entries(world.triggerDefinitions)){
  const semantic=(t.conditions||[]).filter(c=>c.type==='story'||c.type==='action');
  if(!semantic.length)continue;
  if(t.conditions.filter(c=>!['story','action'].includes(c.type)).every(c=>check(c))){eligible+=semantic.length;names.push(key)}
 }
 const active=Object.values(ctx.quests).filter(s=>s==='accepted').length;
 // Arc surfacing and detailed quest completion add generated checks outside root triggers.
 const withGenerated=eligible+Object.keys(world.parties[''].arcs).length+active;
 budget.push({scene:name,authoredChecks:eligible,withGenerated,documentedBudget:15+5*active,triggers:names});
 if(withGenerated>15+5*active)console.error(JSON.stringify(budget[budget.length-1],null,2));
 ck(withGenerated<=15+5*active,'Eligibility budget in '+name);
}
console.log(JSON.stringify({status:'passed',checks,budget,scope:'Mocked script reads, effects and static eligibility; no live semantic judging or Voyage playtest.'},null,2));
