const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'..');
const worldPath=process.argv[2] || path.join(root,'world-draft','WorldAlpha - World.json');
const world=JSON.parse(fs.readFileSync(worldPath,'utf8'));
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'item-regression-manifest.json'),'utf8'));let checks=0;
function ck(ok,label){checks++;if(!ok)throw new Error(label)}
const numeric=(a,op,b)=>({equals:a===b,notEquals:a!==b,greaterThan:a>b,lessThan:a<b,greaterThanOrEqual:a>=b,lessThanOrEqual:a<=b}[op]);
function player(name,items={},traits=[],skills={}){
 return {name,items:{...items},traits:new Set(traits),abilities:new Set(),skills:{...skills},abilityPoints:3,
  resources:{Health:100,Mana:100,Stamina:60},maximum:{Health:100,Mana:100,Stamina:60}};
}
// Fixture semantics are supplied explicitly. This tests effects, references and ownership,
// not whether Voyage's model will understand a live study scene.
function qualifies(rule,p,semanticByName){return rule.conditions.every(c=>{
 if(c.type==='player-item')return numeric(p.items[c.item]||0,c.operator,c.value);
 if(c.type==='player-traits')return c.operator==='contains'?p.traits.has(c.value):!p.traits.has(c.value);
 if(c.type==='skill-value')return numeric(p.skills[c.skill]||0,c.operator,c.value);
 if(c.type==='story'||c.type==='action')return semanticByName[p.name]===true;
 throw Error('Unexpected fixture condition '+c.type);
})}
function fire(rule,players,semanticByName){
 const recipients=players.filter(p=>qualifies(rule,p,semanticByName));
 for(const p of recipients)for(const e of rule.effects){
  if(e.type==='story')continue;
  ck(e.target==='satisfyingPlayers','All new individual changes target qualifying players');
  if(e.type==='player-traits')p.traits.add(e.value);
  else if(e.type==='player-abilities')p.abilities.add(e.value);
  else if(e.type==='item-remove'){ck((p.items[e.item]||0)>=e.quantity,'Real inventory before consume');p.items[e.item]-=e.quantity}
  else if(e.type==='player-resource'){
   const delta=e.operator==='add'?e.value:-e.value;
   p.resources[e.resource]=Math.max(0,Math.min(p.maximum[e.resource],p.resources[e.resource]+delta));
  }else throw Error('Unexpected fixture effect '+e.type);
 }
 return recipients;
}
for(const row of manifest.scrolls){
 const rule=world.triggerDefinitions[row.trigger];
 const skills={[row.skill]:5,'Gravity Magic':25};
 let a=player('Alice',{[row.item]:2},[],skills),b=player('Bob',{[row.item]:1},[],{...skills,[row.skill]:100});
 fire(rule,[a,b],{Alice:true,Bob:false});
 ck(a.abilities.has(row.ability)&&a.traits.has(row.trait),'Successful research teaches '+row.ability);
 ck(a.items[row.item]===1,'One of two scrolls consumed '+row.ability);
 ck(a.abilityPoints===3,'No ability point charged '+row.ability);
 ck(a.skills[row.skill]===skills[row.skill],'No discipline rank awarded '+row.ability);
 ck(!b.abilities.size&&!b.traits.size&&b.items[row.item]===1,'Other reader unchanged '+row.ability);
 ck(fire(rule,[a,b],{Alice:true,Bob:false}).length===0,'Known formula blocks duplicate '+row.ability);
 ck(a.items[row.item]===1,'Duplicate scroll retained '+row.ability);
 a=player('Alice',{[row.item]:1},[],skills);
 fire(rule,[a],{Alice:false});
 ck(a.items[row.item]===1&&!a.abilities.size&&!a.traits.size,'Failed or unfinished study retains scroll '+row.ability);
 a=player('Alice',{},[],skills);fire(rule,[a],{Alice:true});
 ck(!a.abilities.size&&!a.traits.size,'Unheld catalogue scroll teaches nothing '+row.ability);
 a=player('Alice',{},[],skills);b=player('Bob',{[row.item]:1},[],skills);
 fire(rule,[a,b],{Alice:true,Bob:false});
 ck(!a.abilities.size&&!b.abilities.size&&b.items[row.item]===1,'One person cannot consume another holder copy '+row.ability);
 a=player('Alice',{[row.item]:1},[],skills);b=player('Bob',{[row.item]:1},[],skills);
 fire(rule,[a,b],{Alice:true,Bob:true});
 ck(a.abilities.has(row.ability)&&b.abilities.has(row.ability),'Two real readers each learn '+row.ability);
 ck(a.items[row.item]===0&&b.items[row.item]===0,'Two real readers each pay own scroll '+row.ability);
 if(row.skill==='Space Magic'){
  a=player('Alice',{[row.item]:1},[],{'Gravity Magic':24,'Space Magic':5});fire(rule,[a],{Alice:true});
  ck(a.items[row.item]===1&&!a.abilities.size,'Space foundation retained');
 }
}
for(const row of manifest.fixedDoses){
 const rule=world.triggerDefinitions[row.trigger];
 let a=player('Alice',{[row.item]:2}),b=player('Bob',{[row.item]:1});
 a.resources={Health:50,Mana:40,Stamina:20};
 const before={...a.resources};fire(rule,[a,b],{Alice:true,Bob:false});
 ck(a.items[row.item]===1,'Single dose consumption '+row.item);
 for(const [resource,value] of Object.entries(row.resources))ck(a.resources[resource]===Math.max(0,Math.min(a.maximum[resource],before[resource]+value)),'Exact resource effect '+row.item+'/'+resource);
 ck(b.items[row.item]===1&&b.resources.Health===100&&b.resources.Mana===100&&b.resources.Stamina===60,'No bystander medicine '+row.item);
 a=player('Alice',{[row.item]:1});fire(rule,[a],{Alice:true});
 for(const [resource,value] of Object.entries(row.resources))if(value>0)ck(a.resources[resource]===a.maximum[resource],'Recovery capped at actual maximum '+row.item+'/'+resource);
 a=player('Alice',{[row.item]:1});fire(rule,[a],{Alice:false});ck(a.items[row.item]===1,'Reading medicine label consumes nothing '+row.item);
 a=player('Alice');fire(rule,[a],{Alice:true});ck(a.resources.Health===100&&a.resources.Mana===100,'Absent medicine gives nothing '+row.item);
}
const board=world.triggerDefinitions.gh_guild_board;
const levels=[1,3,5,9,10,15,20,35,60,100];
function runBoard({rank=1,level=1,otherLevel=null,text='',cursor=0,statuses={},storage={}}={}){
 const effects=[],store={q20_board_cursor:cursor,...storage};
 const actorLevels={Alice:level,...(otherLevel===null?{}:{Bob:otherLevel})};
 const badge=['Bronze','Silver','Gold','Platinum'][rank-1];
 function check(c){
  if(c.type==='game-tick')return 100;
  if(c.type==='player-level')return actorLevels;
  if(c.type==='player-item')return {Alice:c.item==='Guild Badge: '+badge?1:0,Bob:0};
  if(c.type==='action-text')return [text];
  if(c.type==='quest-status')return statuses[c.questId]||'hidden';
  throw Error(c.type);
 }
 vm.runInNewContext(board.script,{check,effects,storage:store},{timeout:100});
 ck(effects.length<=10,'Board effect budget');
 return {effects,storage:store};
}
const recommended={
 'Guild: A Parcel for the Bazaar':1,'Guild: Westwood Trail Notes':1,'Guild: Boars at the Watercourse':1,
 'Guild: The Courier at the Wrong Turn':3,'Guild: A Cart Full of Glass':1,'Guild: After the Harbor Squall':1,
 'Guild: A Door That Keeps Its Promise':1,'Guild: Keep the Fair Moving':1,'The Road: An Empty Harness':5,
 'Salvage: What the Tide Left':10,'Separate Pay: The Same Commission':10,'Guild: Bitter Roots, Sharp Teeth':15,
 'Guild: Broken Halo Recovery':20,'Guild: Beneath the Broken Dial':25,
 'Guild: Redvein Safety Survey':25,'Guild: Inverted Crown Instruments':40
};
const expansionManifest=path.join(__dirname,'adventurers','manifest.json');
if(fs.existsSync(expansionManifest))for(const job of JSON.parse(fs.readFileSync(expansionManifest,'utf8')).guildJobs||[])recommended[job.title]=job.recommendedLevel;
const fieldworkManifest=path.join(__dirname,'fieldwork','manifest.json');
if(fs.existsSync(fieldworkManifest))for(const job of JSON.parse(fs.readFileSync(fieldworkManifest,'utf8')).jobs)recommended[job.title]=job.recommendedLevel;
for(const level of levels)for(let cursor=0;cursor<20;cursor+=2){
 const result=runBoard({level,rank:4,cursor});
 for(const e of result.effects)if(e.type==='quest-init')ck(recommended[e.value]<=level+(level<10?2:5),'Routine offer respects level '+level+'/'+e.value);
}
const mixed=runBoard({level:1,otherLevel:100,rank:4});
ck(mixed.effects.filter(e=>e.type==='quest-init').every(e=>recommended[e.value]<=3),'Veteran does not drag novice into high-level job');
const requested=runBoard({level:1,rank:4,text:'Please show Guild: Inverted Crown Instruments'});
ck(requested.effects.some(e=>e.type==='quest-init'&&e.value==='Guild: Inverted Crown Instruments'),'Explicit harder request can open posting');
ck(!requested.effects.some(e=>e.type==='quest-accept'),'Opening harder request does not accept it');
ck(requested.effects.some(e=>e.type==='story'&&e.instruction.includes('explain its actual danger')),'Harder requested job gets warning');
ck(!runBoard({rank:0}).effects.some(e=>e.type==='quest-init'),'Unlicensed player gets no licensed job');
for(const [title,slug] of Object.entries({'Salvage: What the Tide Left':'salvage_1','The Road: An Empty Harness':'road_1','Separate Pay: The Same Commission':'camp_1','Guild: Boars at the Watercourse':'contract_cull','Guild: The Courier at the Wrong Turn':'contract_search','Guild: A Cart Full of Glass':'contract_escort','Guild: After the Harbor Squall':'contract_storm','Guild: Bitter Roots, Sharp Teeth':'contract_reagent','Guild: A Door That Keeps Its Promise':'contract_repair','Guild: Keep the Fair Moving':'contract_steward','Guild: Beneath the Broken Dial':'contract_ruin'})){
 const result=runBoard({level:100,rank:4,text:'Show '+title});
 ck(result.storage['q20_offered_'+slug]===true,'Existing offer-flag writer preserved '+title);
}
let compiled=0;
for(const [name,tr] of Object.entries(world.triggerDefinitions))if(tr.script){new vm.Script(tr.script,{filename:name+'.js'});compiled++}
const digest=crypto.createHash('sha256').update(fs.readFileSync(worldPath)).digest('hex');
const result={status:'passed',checks,compiledScripts:compiled,candidateSHA256:digest,
 fixtureScope:'Local mocked condition/effect routing and compiled real scripts; not Voyage runtime or AI recognition.',
 scrolls:30,medicines:12,boardLevels:levels,livePlaytest:false};

console.log(JSON.stringify(result));
