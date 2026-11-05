// Current-world tests. Semantic decisions are supplied; no live AI/math claims.
const fs=require('fs'),path=require('path'),assert=require('assert'),crypto=require('crypto');
const {fixture,player}=require('./magic-overhaul/runtime_fixture.cjs');
const root=path.resolve(__dirname,'..'),read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const w=read(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'));
const review=read(path.join(__dirname,'magic-overhaul/review.json'));
const rows=read(path.join(__dirname,'magic-overhaul/scroll-catalogue.json'));
const recipes=read(path.join(__dirname,'magic-overhaul/reactions.json'));
const inverse=require('./magic-overhaul/previous_world.cjs');
let checks=0;function ck(b,m){checks++;assert.ok(b,m);}
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
const old=inverse(w);
ck(hash(old)===review.baseHash,'Exact historical inverse, without relaxing fingerprints');
ck(review.hybridApproved===true&&review.livePlaytest===false,'Hybrid approved; fixtures are not live tests');
for(const key of ['npcs','itemTypes','abilities','regions','storyStarts','parties','gameplayMusicSettings','progressionSettings','locationSettings'])ck(hash(w[key])===hash(old[key]),'Preserved '+key);
const changedPins=new Set(['The Pearl and Thistle','Opaline Arcade','Caelrath Amphitheatre',"The King's Lists",'House Orselle Salon']);
for(const [name,loc]of Object.entries(old.locations))if(!changedPins.has(name))ck(hash(loc)===hash(w.locations[name]),'Untouched location '+name);
for(const name of changedPins){
    const a=structuredClone(old.locations[name]),b=structuredClone(w.locations[name]);
    for(const k of ['x','y','region']){delete a[k];delete b[k];}
    ck(hash(a)===hash(b),'Only incoming position/region edits '+name);
}
for(const [name,t]of Object.entries(old.triggerDefinitions)){
    if(name.startsWith('item31_study_')||name.startsWith('rb_scroll_registry_'))continue;
    const before=structuredClone(t),now=structuredClone(w.triggerDefinitions[name]);
    for(const c of before.conditions)if(c.type==='action-success-level'){
        const oldNames=['Critical Failure','Failure','Mixed Results','Basic Success','Success','Great Success','Critical Success'];
        const i=oldNames.findIndex(n=>n.toLowerCase()===c.value.toLowerCase());
        c.value=w.successLevelSettings.tiers[i].name.toLowerCase();
    }
    ck(hash(before)===hash(now),'Other event unchanged '+name);
}
ck(!Object.keys(w.triggerDefinitions).some(k=>/^item31_study_|^rb_scroll_registry_|^rb_study_/.test(k)),'Old 130-scroll handlers retired');
ck(w.triggerDefinitions.mx_scroll_learn.scope==='player','One shared, player-scoped learner');
const baseTiers=old.successLevelSettings.tiers,newTiers=w.successLevelSettings.tiers;
const names=['Spectacular Blunder','Unfortunate Mishap','Imperfect Result','Little Triumph','Splendid Work','Stroke of Brilliance','Storybook Triumph'];
ck(newTiers.map(t=>t.name).join('|')===names.join('|'),'Selected display ladder');
for(let i=0;i<7;i++)for(const k of ['id','minScore','maxScore','imageUrl'])ck(newTiers[i][k]===baseTiers[i][k],'Tier behavior preserved '+i+'/'+k);
ck(w.successLevelSettings.firstSuccessfulTierId===old.successLevelSettings.firstSuccessfulTierId,'First successful ID unchanged');
const labelRefs=[];
function visit(x){if(x&&typeof x==='object'){if(x.type==='action-success-level')labelRefs.push(x.value);for(const v of Object.values(x))visit(v);}}
visit(w);
ck(labelRefs.length===5&&labelRefs.every(v=>names.some(n=>n.toLowerCase()===v.toLowerCase())),'All five native label tests migrated');
ck(w.combatSettings.damageTypes.includes('poison')&&!w.combatSettings.damageTypes.includes('poisoning'),'Canonical poison key');
ck(w.combatSettings.damageTypes.includes('soul')&&w.combatSettings.damageTypes.length===20,'Separate Soul damage');
ck(w.combatSettings.damageTypes.every(k=>w.combatSettings.damageTypePresentation[k]?.emoji),'All damage channels represented');
for(const [name,t]of Object.entries(old.npcTypes)){
    const migrated=JSON.parse(JSON.stringify(t).replace(/"poisoning"/g,'"poison"'));
    ck(hash(migrated)===hash(w.npcTypes[name]),'Defense equivalence '+name);
}
ck(recipes.length===24&&new Set(recipes.map(r=>[r[0],r[1]].sort().join('|'))).size===24,'24 unique unordered recipes');
const coverage={};
for(const [a,b,name,bonus]of recipes){
    ck(a!==b&&w.combatSettings.damageTypes.includes(a)&&w.combatSettings.damageTypes.includes(b),'Registered pair '+name);
    ck(![a,b].some(x=>['soul','piercing','slashing','bludgeoning'].includes(x)),'No physical/Soul reaction '+name);
    for(const k of [a,b])(coverage[k]??=[]).push(bonus);
    ck(w.aiInstructions.generateActionInfo['Elemental Reaction Table'].includes(name),'Shipped table includes '+name);
}
ck(Object.keys(coverage).length===16,'All sixteen reaction channels');
for(const [name,budgets]of Object.entries(coverage))ck(budgets.sort((a,b)=>a-b).join(',')==='0,10,20','Three balanced partner roles '+name);
ck(w.aiInstructions.generateActionInfo['Reaction Resolution and Resonance'].includes('0.90'),'Relative damage weakening, not flat armor/damage subtraction');
ck(!Object.values(w.triggerDefinitions).some(t=>t.conditions.some(c=>c.type==='damage-type')||t.effects.some(e=>['npc-debuff','npc-stat'].includes(e.type))),'No invented hit/debuff clauses');

function studyDecision(approved){return (name,r)=>{
    if(r.name!=='mx_scroll_learn')return false;
    const item=r.conditions.find(c=>c.type==='player-item')?.item;
    return (approved[name]||[]).includes(item);
};}
function teachOne(row,{copies=2,second=true,success=true,gravity=25}={}){
    const item='Teaching Scroll: '+row[0];
    const f=fixture(w,{players:{Alice:player({[item]:copies},[],{'Gravity Magic':gravity}),...(second?{Bob:player({[item]:1},[],{'Gravity Magic':100})}:{})}});
    f.turn();
    f.turn({actions:['I deliberately study '+item],story:'Alice works on '+item+'.'});
    f.turn({actions:['I continue the controlled test.'],story:'The real test resolves.',semantic:studyDecision(success?{Alice:[item]}:{})});
    return f;
}
for(const row of rows){
    const item='Teaching Scroll: '+row[0],formula='Formula: '+row[0];
    let f=teachOne(row),a=f.s.players.Alice,b=f.s.players.Bob;
    ck(a.traits.includes(formula)&&a.abilities.includes(row[0]),'Learns exact formula '+row[0]);
    ck(a.items[item]===1&&a.abilityPoints===3&&a.skills['Gravity Magic']===25,'Consumes once; no point/rank charge '+row[0]);
    ck(b.items[item]===1&&!b.abilities.length&&!b.traits.includes(formula),'Bystander unchanged '+row[0]);
    f.turn({actions:['study it again'],semantic:studyDecision({Alice:[item]})});
    ck(a.items[item]===1,'Known formula duplicate retained '+row[0]);
    f=teachOne(row,{success:false});
    ck(f.s.players.Alice.items[item]===2&&!f.s.players.Alice.abilities.length,'Failed/uncompleted study retains item '+row[0]);
    f=teachOne(row,{copies:0});
    ck(!f.s.players.Alice.abilities.length&&f.s.players.Bob.items[item]===1,'No borrowed ownership '+row[0]);
    if(row[2]){
        f=teachOne(row,{gravity:24});
        ck(!f.s.players.Alice.abilities.length&&f.s.players.Alice.items[item]===2,'Gravity foundation retained '+row[0]);
    }
}
// Different formulas in the same multiplayer turn use different queued gates.
for(const [i,j]of [[0,1],[29,30],[40,70],[110,129]]){
    const a='Teaching Scroll: '+rows[i][0],b='Teaching Scroll: '+rows[j][0];
    const f=fixture(w,{players:{Alice:player({[a]:2},[],{'Gravity Magic':25}),Bob:player({[b]:2},[],{'Gravity Magic':25})}});
    f.turn();f.turn({actions:['Alice studies '+a,'Bob studies '+b],story:'Both work on their own formulas.'});
    const semantic=studyDecision({Alice:[a],Bob:[b]});
    f.turn({semantic});f.turn({semantic});
    ck(f.s.players.Alice.abilities.join('|')===rows[i][0]&&f.s.players.Bob.abilities.join('|')===rows[j][0],'Different-formula readers never cross-grant '+i+'/'+j);
    ck(f.s.players.Alice.items[a]===1&&f.s.players.Bob.items[b]===1,'Different-formula readers each consume one '+i+'/'+j);
    ck(!Object.keys(f.s.rules).some(k=>/^rb_study_|^item31_study_/.test(k)),'No per-scroll dynamic registration');
}
{
    const row=rows[0],item='Teaching Scroll: '+row[0],f=fixture(w,{players:{Alice:player({[item]:1}),Bob:player({[item]:1})}});
    f.turn();f.turn({actions:['Both read '+item]});f.turn({semantic:studyDecision({Alice:[item],Bob:[item]})});
    ck(f.s.players.Alice.items[item]===0&&f.s.players.Bob.items[item]===0,'Two successful holders of one formula both settle independently');
}
{
    const row=rows[0],item='Teaching Scroll: '+row[0],f=fixture(w,{players:{Alice:player({[item]:1})}});
    f.turn();f.turn({actions:['I study '+item]});
    delete f.s.players.Alice.items[item];
    f.turn({semantic:studyDecision({Alice:[item]})});
    ck(!f.s.players.Alice.abilities.length,'Selling/dropping before verification prevents consumption/grant');
}
{
    const f=fixture(w);f.turn();f.turn({actions:['I read a sign.']});
    ck(!f.s.storage.mxScrollReady,'No held formula means no semantic scroll query');
}

const grades=['Quiet Resonance',...Array.from({length:19},(_,i)=>'Resonance: '+(i+1)),'Resonant'];
const grade=p=>grades.findIndex(g=>p.traits.includes(g));
const reactionFor=(...names)=>(name,r)=>r.name==='mx_resonance_gain'&&names.includes(name);
const spendFor=(...names)=>(name,r)=>r.name==='mx_resonance_spend'&&names.includes(name);
for(const snapshotConditions of [false,true])for(const reverse of [false,true]){
    const f=fixture(w,{snapshotConditions,reverse,players:{Alice:player(),Bob:player()}});
    f.turn();
    ck(grade(f.s.players.Alice)===0&&f.s.players.Alice.resources.Resonance===0,'Starts empty '+snapshotConditions);
    for(let i=1;i<=20;i++){
        f.turn({semantic:reactionFor('Alice')});
        f.turn();
        ck(grade(f.s.players.Alice)===i&&f.s.players.Alice.resources.Resonance===i,'One exact earned charge '+i+'/'+snapshotConditions);
        ck(grade(f.s.players.Bob)===0&&f.s.players.Bob.resources.Resonance===0,'No bystander charge '+i);
    }
    f.turn({semantic:()=>false});
    ck(grade(f.s.players.Alice)===20,'Miss/heal/no valid spend retains readiness');
    f.turn({semantic:(name,r)=>name==='Alice'&&['mx_resonance_gain','mx_resonance_spend'].includes(r.name)});
    f.turn();
    ck(grade(f.s.players.Alice)===1&&f.s.players.Alice.resources.Resonance===1,'Burst resets old charge then reaction begins next cycle');
    f.s.players.Alice.resources.Resonance=20;f.s.players.Bob.resources.Resonance=20;
    f.s.players.Alice.level++;f.s.players.Bob.level++;
    f.turn();
    ck(f.s.players.Alice.resources.Resonance===1&&f.s.players.Bob.resources.Resonance===0,'Level-up/native refill cannot create charge or erase earned value');
    f.turn({semantic:spendFor('Alice','Bob')});
    ck(grade(f.s.players.Alice)===1&&grade(f.s.players.Bob)===0,'Semantic false positive cannot spend unready players');
}
// Consecutive reactions, not only every-other-turn fixtures.
{
    const f=fixture(w);f.turn();
    for(let i=0;i<20;i++)f.turn({semantic:reactionFor('Alice')});
    f.turn();
    ck(grade(f.s.players.Alice)===20,'Consecutive turns do not lose earned receipts');
    const before=[...f.s.players.Alice.traits];
    f.turn({semantic:reactionFor('Alice')});f.turn();
    ck(grade(f.s.players.Alice)===20&&f.s.players.Alice.resources.Resonance===20,'Ready charge cannot overflow');
}
{
    const f=fixture(w);f.turn();
    for(let i=0;i<8;i++)f.turn();
    ck(grade(f.s.players.Alice)===0,'Rest/day/idle with no approved reaction earns nothing');
    f.s.players.Bob=player();f.turn();f.turn();
    ck(grade(f.s.players.Bob)===0,'Late-joining player starts empty, not with party charge');
}
const sem=Object.values(w.triggerDefinitions).filter(t=>t.conditions.some(c=>['story','action'].includes(c.type))).length;
ck(sem===429,'Semantic definitions decrease from 456 to 429');
ck(Object.keys(w.triggerDefinitions).length===556,'Expected mechanical counter and universal-gate inventory');
for(const [name,t]of Object.entries(w.triggerDefinitions).filter(([k])=>k.startsWith('mx_'))){
    ck(t.name===name&&t.conditions.length<=5&&t.effects.length<=10,'Native rule shape '+name);
    ck(JSON.stringify(t).length<=10000,'Rule size '+name);
    for(const e of t.effects)if(e.type.startsWith('player-'))ck(e.target==='satisfyingPlayers','Native recipient filtering '+name);
}
console.log(JSON.stringify({status:'passed',checks,scrolls:rows.length,reactions:recipes.length,semanticDefinitions:sem,
    livePlaytest:false,semanticRecognitionTested:false,exactCombatDamageTested:false}));
