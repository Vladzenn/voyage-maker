// Real emitted scripts and native effects; semantic answers are supplied fixtures.
const fs=require('fs'),path=require('path'),assert=require('assert'),vm=require('vm');
const root=path.resolve(__dirname,'..'),w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const r=JSON.parse(fs.readFileSync(path.join(__dirname,'ardelis/review.json'),'utf8'));
const source=JSON.parse(fs.readFileSync(path.join(__dirname,'ardelis/source.json'),'utf8'));
let checks=0;const ck=(x,m)=>{checks++;assert.ok(x,m)};
const before=require('./ardelis/previous_world.cjs')(w);
ck(JSON.stringify(Object.keys(w.storyStarts).filter(k=>k in before.storyStarts))===JSON.stringify(Object.keys(before.storyStarts)),'Existing starts retain relative order');
ck(r.contents.npcs.length>=100,'Complete capital cast');ck(r.contents.majorNPCs.length===23,'Includes three major paladins');
ck(r.contents.locations.length===84,'Named inhabited and expedition sites');
for(const [name,loc]of Object.entries(before.locations))if(name!=='Evertree Base')ck(JSON.stringify(w.locations[name])===JSON.stringify(loc),'Old location exact: '+name);
for(const [name,t]of Object.entries(before.triggerDefinitions))ck(JSON.stringify(w.triggerDefinitions[name])===JSON.stringify(t),'Old trigger exact: '+name);
for(const [name,n]of Object.entries(before.npcs))if(name!=="Valkazathoth'dmir")ck(JSON.stringify(w.npcs[name])===JSON.stringify(n),'Old NPC exact: '+name);
const pins=JSON.parse(fs.readFileSync(path.join(__dirname,'ardelis/placements.json'),'utf8'));
for(const pin of pins.filter(p=>p.source!=='NEW')){const old=source.locations[pin.source],now=w.locations[pin.name];ck(now.x===old.x&&now.y===old.y,'Preserve source pin '+pin.source);}
for(const name of r.contents.regions){const reg=w.regions[name];const old=Object.values(source.regions).find(x=>x.x===reg.x&&x.y===reg.y);ck(JSON.stringify(reg.images)===JSON.stringify(old.images),'Map URL and crop exact '+name);}
for(const name of r.contents.npcs){const n=w.npcs[name];ck(w.locations[n.currentLocation]?.areas[n.currentArea],'Placed '+name);ck(['average','strong','boss'].includes(n.tier),'Native tier '+name);ck(!/works as (?:has|keeps|plays|is)\b/i.test(n.basicInfo),'No malformed job sentence '+name);}
const compare=(a,op,b)=>({equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b})[op];
function fixture(extra={}){
 const s={tick:100,location:'Evertree Base',area:'Evertree Base - Portal Room',players:{Alice:10},items:{},quests:{},storage:{gh_spider_entered:true},actions:['enter the Ardelis portal'],...extra};
 function check(c){let v;if(c.type==='game-tick')v=s.tick;else if(c.type==='party-location')v=s.location;else if(c.type==='party-area')v=s.area;else if(c.type==='player-level')v=s.players;else if(c.type==='npc-in-party')v={Companion:true};else if(c.type==='action-text')v=s.actions;else if(c.type==='read-boolean')v=s.storage[c.key]===true;else if(c.type==='quest-status')v=s.quests[c.questId]||'planned';else if(c.type==='player-item')v=s.items[c.item]||0;else throw Error('Unmocked native check '+c.type);return Object.hasOwn(c,'operator')?compare(v,c.operator,c.value):v;}
 function fire(name,semantic=false){const t=w.triggerDefinitions[name];if(!t.conditions.every(c=>['action','story'].includes(c.type)?semantic:check(c)))return false;
  const box={check,storage:s.storage,effects:structuredClone(t.effects),skip:false};if(t.script)vm.runInNewContext(t.script,box,{timeout:500});if(box.skip)return false;
  s.last=box.effects;for(const e of box.effects){if(e.type==='party-location')s.location=e.value;else if(e.type==='party-area')s.area=e.value;else if(e.type==='write-boolean')s.storage[e.key]=e.value;else if(e.type==='item-add')s.items[e.item]=(s.items[e.item]||0)+e.quantity;else if(e.type==='quest-init')s.quests[e.value]='available';}return true;
 }return {s,fire};
}
let f=fixture();ck(!f.fire('ar_portal_to',true),'No outbound transit without genuine key');
f=fixture({items:{'Ardelis Portal Key':1}});ck(!f.fire('ar_portal_to',false),'Discussion is not crossing');ck(f.fire('ar_portal_to',true),'Committed crossing');ck(f.s.location==='Caelrath Portal Hall'&&f.s.area==='Caelrath Portal Hall - Portal Room','Exact arrival');ck(!f.fire('ar_portal_from',true),'Shared lock stops same-turn bounce');f.s.tick++;f.s.items={};ck(f.fire('ar_portal_from',true),'Return works without any key');ck(f.s.area==='Evertree Base - Portal Room','Exact return floor');
f=fixture({items:{'Ardelis Portal Key':1},players:{Alice:20},storage:{}});ck(f.fire('ar_portal_to',true),'Normal level-20 anomaly eligibility');ck(f.s.location==='Silken Portal Room','Existing surprise branch');ck(f.s.storage.ghSpiderIncident.intendedDestination==='Ardelis','Intended route retained');
f=fixture();ck(!f.fire('ar_issue_key',true),'No authorization, no issued key');f.s.storage.arTransitAuthorized=true;ck(!f.fire('ar_issue_key',false),'Mere eligibility is not actual handover');ck(f.fire('ar_issue_key',true),'Verified actual recipient');ck(!f.fire('ar_issue_key',true),'No duplicate key');
f=fixture({location:'Caelrath Palace',area:'Caelrath Palace - Warded Crossing',actions:['I enter the Resonance Cradle']});ck(f.fire('ar_cradle_guard'),'Early directed jump blocked');ck(f.s.area==='Caelrath Palace - Warded Crossing','Retains safe side');f.s.area='Caelrath Palace - Resonance Cradle';ck(f.fire('ar_cradle_backstop'),'Direct pin jump corrected');f.s.storage.arLowerReady=true;ck(!f.fire('ar_cradle_backstop'),'Earned passage stays open');
f=fixture({location:'Caelrath Palace',area:'Caelrath Palace - Resonance Cradle'});ck(!f.fire('ar_diadem_recovery',false),'Arrival alone no relic');ck(f.fire('ar_diadem_recovery',true),'Actual safe recovery');ck(!f.fire('ar_diadem_recovery',true),'Relic once only');ck(f.s.items["Thaurivex's Broken Diadem"]===1,'One recovery award');
f=fixture({location:"Adventurer's Guild - Caelrath Branch",items:{'Guild Badge: Bronze':1},players:{Alice:1},actions:['Could you show me some suitable work?']});
ck(!f.fire('ar_guild_board',false),'Board greeting or exam sample does not offer live work');ck(f.fire('ar_guild_board',true),'Natural actual work request');ck(f.s.last.filter(e=>e.type==='quest-init').length===1,'One board offer');ck(f.s.last.find(e=>e.type==='quest-init').value==='Guild: A Cellar That Rustles','Beginner gets a safe ordinary job');ck(!f.fire('ar_guild_board',true),'No second offer same tick');f.s.tick++;f.s.actions=['I want Guild: Something in the Culvert'];ck(f.fire('ar_guild_board',true),'Explicit eligible harder title is a choice');ck(f.s.last.find(e=>e.type==='quest-init').value==='Guild: Something in the Culvert','Honor actual named job');
const qs=w.parties[''].quests;
for(const name of r.contents.quests){const q=qs[name];ck(!Object.hasOwn(q,'description'),'Native statement '+name);ck(q.completionCondition?.type==='story'||name==='Guild: Caelrath Licensure','Typed completion '+name);ck(!Array.isArray(q.objectives),'Native objective map '+name);}
for(const name of r.contents.quests.filter(n=>n.startsWith('Guild:')&&n!=='Guild: Caelrath Licensure')){const q=qs[name];ck(q.onCompleteEffects.filter(e=>e.type==='item-add'&&e.item==='Mark').length===1,'Single reward owner '+name);ck(q.onCompleteEffects.filter(e=>e.item==='Guild Service Credit').length===1,'One service credit '+name);}
ck(qs['Ardelis: Passage under Seal'].completionCondition.query.includes('without prior Ardelis entry'),'No permission circularity');
ck(!w.triggerDefinitions.ar_portal_from.conditions.some(c=>c.type==='player-item'),'No wording-sensitive return key requirement');
ck(w.npcs['Noelle Ashford'].basicInfo.includes('hand caster'),'Noelle hand-caster card');
ck(w.npcs["Valkazathoth'dmir"].level===100&&w.npcs["Valkazathoth'dmir"].immunities.includes('psychic'),'Wizard power and immunity preserved');
console.log(JSON.stringify({status:'passed',checks,scope:'Exact preservation plus real emitted scripts with supplied semantic answers. Not live playtesting.'}));
