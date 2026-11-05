// These fixtures supply semantic decisions. They test real emitted scripts and
// native effect ownership, not Voyage's language recognition or live scheduling.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const file = process.argv[2] || path.join(root, 'world-draft/WorldAlpha - World.json');
const world = require('./ardelis/previous_world.cjs')(JSON.parse(fs.readFileSync(file, 'utf8')));
const review = JSON.parse(fs.readFileSync(path.join(__dirname, 'rebirth/review.json'), 'utf8'));
const rules = world.triggerDefinitions;
let checks = 0;
function ck(value, message) { checks++; assert.ok(value, message); }
const canonical = value => Array.isArray(value) ? value.map(canonical) : value && typeof value === 'object' ? Object.fromEntries(Object.keys(value).sort().map(k => [k, canonical(value[k])])) : value;
const hash = value => crypto.createHash('sha256').update(JSON.stringify(canonical(value))).digest('hex');
const compare = (a, op, b) => ({equals:a===b, notEquals:a!==b, greaterThan:a>b, greaterThanOrEqual:a>=b, lessThan:a<b, lessThanOrEqual:a<=b, contains:Array.isArray(a)?a.includes(b):String(a).includes(b), notContains:Array.isArray(a)?!a.includes(b):!String(a).includes(b), regex:new RegExp(String(b)).test(String(a))})[op];
function fixture(overrides = {}) {
    const state = {tick:200, location:'Brookmeadow', area:'Brookmeadow - Mill Lane', realm:'Glowhaven', region:'Brookmeadow Vale', start:Object.keys(world.storyStarts)[0], players:{Alice:{level:20, traits:['Summoned one'], items:{}, skills:{}}}, storage:{rbCampaign:true}, scene:[], fighting:[], health:{}, actions:['look around'], story:'', ...overrides};
    function check(c) {
        let raw;
        if (c.type==='game-tick') raw=state.tick;
        else if(c.type==='story-start') raw=state.start;
        else if(c.type==='party-location') raw=state.location;
        else if(c.type==='party-area') raw=state.area;
        else if(c.type==='party-realm') raw=state.realm;
        else if(c.type==='party-region') raw=state.region;
        else if(c.type==='action-text') raw=state.actions;
        else if(c.type==='story-text') raw=state.story;
        else if(c.type==='player-traits') raw=Object.fromEntries(Object.entries(state.players).map(([k,p])=>[k,p.traits]));
        else if(c.type==='player-item') raw=Object.fromEntries(Object.entries(state.players).map(([k,p])=>[k,p.items[c.item]||0]));
        else if(c.type==='player-level') raw=Object.fromEntries(Object.entries(state.players).map(([k,p])=>[k,p.level]));
        else if(c.type==='skill-value') raw=Object.fromEntries(Object.entries(state.players).map(([k,p])=>[k,p.skills[c.skill]||0]));
        else if(c.type==='npc-in-combat') raw=c.npc==='anySceneNPC'?Object.fromEntries(state.scene.map(n=>[n,state.fighting.includes(n)])):state.fighting.includes(c.npc);
        else if(c.type==='npc-in-scene') raw=state.scene.includes(c.npc);
        else if(c.type==='npc-health') raw=state.health[c.npc];
        else if(c.type==='read-boolean') raw=state.storage[c.key]===true;
        else if(c.type==='read-number') raw=Number(state.storage[c.key])||0;
        else throw Error('Unexpected fixture read '+c.type);
        if (!c.operator) return raw;
        if (raw && typeof raw==='object' && !Array.isArray(raw)) return Object.values(raw).some(v=>compare(v,c.operator,c.value));
        return compare(raw,c.operator,c.value);
    }
    return {state,check};
}
function run(name, options = {}, triggers = {}) {
    const {state,check}=fixture(options);
    const sandbox={check, storage:state.storage, triggers, effects:structuredClone(rules[name].effects), skip:false};
    vm.runInNewContext(rules[name].script, sandbox, {timeout:100});
    ck(sandbox.effects.length<=10, name+' respects effect limit');
    return {...sandbox,state};
}

// Preserve the full reviewed base by reversing only the declared changes.
const before=structuredClone(world);
for(const row of review.rows) {
    let object=before;
    for(const k of row.path.slice(0,-1)) object=object[k];
    const k=row.path.at(-1);
    if(row.kind==='added') {ck(hash(object[k])===row.afterHash,'Exact reviewed addition '+row.path.join('/'));delete object[k];}
    else {if(row.kind==='modified')ck(hash(object[k])===row.afterHash,'Exact reviewed edit '+row.path.join('/'));object[k]=row.before;}
}
ck(hash(before)===review.baseHash,'Review reconstructs the exact approved merge base');
for(const section of ['gameplayMusicSettings','progressionSettings','combatSettings','resourceSettings','locationSettings']) ck(hash(world[section])===hash(before[section]), 'Preserved settings '+section);
for(const [name,n] of Object.entries(before.npcs)) ck(hash(n)===hash(world.npcs[name]),'Existing NPC exact '+name);
for(const [name,r] of Object.entries(before.regions)) ck(hash(r)===hash(world.regions[name]),'Existing region/map exact '+name);
for(const [name,l] of Object.entries(before.locations)) ck(hash({x:l.x,y:l.y,images:l.images})===hash({x:world.locations[name].x,y:world.locations[name].y,images:world.locations[name].images}),'Existing pin/art exact '+name);
ck(!Object.keys(world.realms).includes('Ardelis'),'Ardelis map is deferred');
ck(!Object.keys(world.npcs).some(k=>/rival|second arrival/i.test(k)),'Controlled rival deployment is deferred');
ck(Object.keys(world.storyStarts)[0]==='🌅 Rebirth: A Morning in Brookmeadow','Featured start first');
ck(world.storyStarts[Object.keys(world.storyStarts)[0]].startingItems[0].quantity===1000,'Rebirth grants the established starting amount once');
for(const name of ['Summoned one','Traced Shore Record']) {
    ck(!Object.values(world.traitCategories).some(c=>c.traits.includes(name)), name+' absent from creation');
    ck(world.traits[name].requirements.some(r=>r.type==='characterLevel'&&r.amount>world.progressionSettings.maxCharacterLevel), name+' blocked from ordinary level picks');
}
for(const [name,count] of Object.entries(review.contents.forms)) ck(world.traitCategories[name+' Form'].traits.length===count,'Form count '+name);
ck(world.traits['Fae Form — Moth-winged'].unlockedBy.includes('Mixed Ancestry'),'Existing mixed Fae choice preserved');
ck(world.traits['Beastfolk Form — Cat'].unlockedBy.includes('Mixed Ancestry'),'Existing mixed Beastfolk choice preserved');

for(const tick of [0,25,100,199]) ck(!run('rb_clock',{tick}).storage.rbTownReady,'No early delegation at '+tick);
ck(run('rb_clock',{tick:200}).storage.rbTownReady,'200 turns opens only the mechanical window');
ck(!run('rb_clock',{tick:400,location:'Asterveil Canopy'}).storage.rbTownReady,'Foreign expedition delays the window');
ck(!run('rb_clock',{tick:400,scene:['Enemy'],fighting:['Enemy']}).storage.rbTownReady,'Combat delays the window');
ck(!run('rb_clock',{tick:400,players:{Bob:{level:100,traits:[],items:{},skills:{}}}}).storage.rbTownReady,'Unrelated start/player cannot open window');
const target={level:15,traits:['Summoned one','Traced Shore Record'],items:{},skills:{}};
ck(run('rb_clock',{tick:400,storage:{rbLead:true,rbLeadTick:300},players:{Alice:target}}).storage.rbAmbushReady,'Actual traced bearer can qualify');
ck(!run('rb_clock',{tick:330,storage:{rbLead:true,rbLeadTick:300},players:{Alice:target}}).storage.rbAmbushReady,'Lead needs its separate delay');
ck(!run('rb_clock',{tick:400,storage:{rbLead:true,rbLeadTick:300},players:{Alice:{...target,level:1},Bob:{level:100,traits:[],items:{},skills:{}}}}).storage.rbAmbushReady,'Strong spectator does not qualify a weak bearer');
ck(!run('rb_clock',{tick:400,storage:{rbLead:false,rbLeadTick:300},players:{Alice:target}}).storage.rbAmbushReady,'False or protected lead does not create an ambush');
const ambush=rules.rb_interception;
ck(ambush.scope==='player'&&ambush.conditions.some(c=>c.type==='player-traits'&&c.value==='Traced Shore Record'),'Ambush targets actual traced participant');
ck(ambush.conditions.some(c=>c.type==='player-level'&&c.value===15),'Native recipient level check');
ck(rules.rb_origin.conditions.some(c=>c.type==='game-tick'&&c.value===0),'Later joins do not inherit origin');
ck(run('rb_visitors_depart',{tick:202,storage:{rbInterventionTick:202}}).skip,'Intervention cannot instantly remove its cast');
ck(!run('rb_visitors_depart',{tick:205,storage:{rbInterventionTick:202}}).skip,'Visitors can depart after the exchange');
for(let i=1;i<=2;i++) {
    const r=rules['rb_captive_shutdown_'+i],name=i===1?'The Ash-Cloaked Courier':'The Reed-Cloaked Courier';
    ck(r.conditions.some(c=>c.type==='npc-health'&&c.operator==='greaterThan'&&c.value===0),'Capture requires a living target');
    ck(r.effects[0].npc===name&&r.effects[0].type==='npc-health'&&r.effects[0].value===0,'Shutdown affects only that captured proxy');
    ck(!r.effects.some(e=>e.type==='item-add'),'No false evidence drop from a shutdown');
}
const gate='rb_private_gate';
let out=run(gate,{area:'Shadowspire - Cellar Gate'});ck(out.skip,'Cellar entry needs actual key');
out=run(gate,{area:'Shadowspire - Cellar Gate',players:{Alice:{...target,items:{'Shadowspire Guest Key':1}}}});ck(!out.skip&&out.effects.some(e=>e.type==='party-location'&&e.value==='Shifting Gallery'),'Authorized entry reaches fixed gallery');
out=run(gate,{area:'Shifting Gallery - Return Lantern',realm:"Vladimir's Elsewhere"});ck(!out.skip&&out.effects.some(e=>e.type==='party-area'&&e.value==='Shadowspire - Cellar Gate'),'Lost key never blocks fixed return');
ck(!out.effects.some(e=>String(e.value).includes('Evertree')),'Private return stays at Shadowspire');
out=run('rb_tower_ward',{players:{Alice:{...target,items:{'Shadowspire Guest Key':1}},Bob:{...target,items:{}}}});ck(out.skip,'A permitted companion does not need a duplicate guest key');

// Actual registry scripts create native, individually targeted learning rules.
const first=review.contents.scrolls[0],second=review.contents.scrolls[1];
let runtime={},store={};
out=run('rb_scroll_registry_01',{tick:1,storage:store,actions:['look around'],players:{Alice:{...target,items:{[first.item]:1}}}},runtime);
ck(Object.keys(runtime).length===0,'A carried scroll creates no idle learning judgment');
out=run('rb_scroll_registry_01',{tick:2,storage:store,actions:['I study '+first.item],players:{Alice:{...target,items:{[first.item]:1}}}},runtime);
ck(!!runtime[first.id],'Named study installs an exact native rule');
ck(runtime[first.id].scope==='player','Learning keeps native player scope');
out=run('rb_scroll_registry_01',{tick:3,storage:store,actions:['I try again'],story:'The formula remains difficult; its diagram asks for another careful test.',players:{Alice:{...target,items:{[first.item]:1}}}},runtime);
ck(!!runtime[first.id],'Natural continuation retains the selected study');
out=run('rb_scroll_registry_01',{tick:4,storage:store,actions:['I study '+second.item],players:{Alice:{...target,items:{[first.item]:1}},Bob:{...target,items:{[second.item]:1}}}},runtime);
ck(runtime[first.id]&&runtime[second.id],'Different readers can keep separate formula checks');
function learn(rule,player,semantic) {
    const pass=semantic&&rule.conditions.every(c=>{
        if(c.type==='story')return true;
        if(c.type==='player-item')return (player.items[c.item]||0)>0;
        if(c.type==='player-traits')return !player.traits.includes(c.value);
        if(c.type==='skill-value')return (player.skills[c.skill]||0)>=c.value;
        throw Error('Unexpected learning condition '+c.type);
    });
    if(!pass)return false;
    for(const e of rule.effects) {
        if(e.type==='story')continue;
        ck(e.target==='satisfyingPlayers','Exact native reader owns settlement');
        if(e.type==='player-traits')player.traits.push(e.value);
        else if(e.type==='player-abilities')player.abilities.push(e.value);
        else if(e.type==='item-remove')player.items[e.item]-=e.quantity;
    }
    return true;
}
for(const r of review.contents.scrolls) {
    const registry='rb_scroll_registry_'+String(Math.floor(review.contents.scrolls.indexOf(r)/10)+1).padStart(2,'0');
    const a={...target,traits:[],items:{[r.item]:2},skills:{'Gravity Magic':25},abilities:[]};
    const b={...target,traits:[],items:{[r.item]:1},skills:{'Gravity Magic':25},abilities:[]};
    const live={};
    run(registry,{tick:10,storage:{},actions:['I carefully study '+r.item],players:{Alice:a,Bob:b}},live);
    const tr=live[r.id];ck(!!tr,'Real emitted study rule '+r.ability);
    ck(!learn(tr,a,false)&&a.items[r.item]===2,'Failed study retains copy '+r.ability);
    ck(learn(tr,a,true)&&a.items[r.item]===1&&a.abilities.includes(r.ability),'Successful reader settles once '+r.ability);
    ck(!learn(tr,a,true)&&a.items[r.item]===1,'Duplicate completion cannot consume twice '+r.ability);
    ck(b.items[r.item]===1&&!b.abilities.length,'Other holder unchanged '+r.ability);
    ck(learn(tr,b,true)&&b.abilities.includes(r.ability),'Second actual reader can independently learn '+r.ability);
    if(r.space) {const c={...b,traits:[],items:{[r.item]:1},skills:{'Gravity Magic':24},abilities:[]};ck(!learn(tr,c,true),'Space foundation retained');}
}
out=run('rb_scroll_registry_01',{tick:20,storage:store,actions:['walk to the mill'],players:{Alice:{...target,items:{}}}},runtime);
ck(!runtime[first.id],'Loss/trade removes an active study without granting anything');
for(const [name,t] of Object.entries(rules)) if(name.startsWith('rb_')) {
    ck(t.conditions.length<=5&&t.effects.length<=10,'Native limits '+name);
    if(t.script)new vm.Script(t.script);
}
for(const name of review.contents.npcs) {const npc=world.npcs[name];ck(!npc.currentLocation||world.locations[npc.currentLocation]?.areas[npc.currentArea],'Actual new NPC address '+name);}
for(const name of review.contents.locations) {
    const location=world.locations[name];
    for(const [key,area] of Object.entries(location.areas))for(const next of area.paths)ck(next in location.areas,'Paths stay in the actual parent location '+key+' -> '+next);
    ck(name==='Shifting Gallery'||Object.values(location.areas).some(a=>a.description.includes('walking route back to Shifting Gallery')),'Each room has a marked ordinary return '+name);
}
console.log(JSON.stringify({status:'passed',checks,scrolls:review.contents.scrolls.length,forms:review.contents.forms,scope:'Real emitted scripts and supplied semantic answers; no live Voyage playtest.'}));
