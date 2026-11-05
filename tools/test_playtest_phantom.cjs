// Current emitted rules and native-field fixtures; no AI behavior guarantees.
const fs=require('fs'),path=require('path'),assert=require('assert'),vm=require('vm');
const {fixture,player}=require('./magic-overhaul/runtime_fixture.cjs');
const root=path.resolve(__dirname,'..'),read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const w=read(path.join(root,'world-draft/WorldAlpha - World.json'));
const before=require('./playtest-phantom/previous_world.cjs')(w);
let checks=0;function ck(b,m){checks++;assert.ok(b,m);}
const talent='Quickened Chorus',origin='Otherworld Rebirth';
const react=(name,rule)=>rule.name==='mx_resonance_gain';
for(const options of [{},{reverse:true},{snapshotConditions:true},{reverse:true,snapshotConditions:true}]){
    const f=fixture(w,{...options,players:{Alice:player({},[talent]),Bob:player()}});
    f.turn();
    ck(f.s.players.Alice.resources.Resonance===0,'Talent does not grant charge');
    for(let i=0;i<16;i++)f.turn({semantic:react});
    f.turn();f.turn();
    ck(f.s.players.Alice.traits.includes('Resonant'),'Sixteen genuine reactions ready the talent');
    ck(f.s.players.Alice.resources.Resonance===16,'Talent meter uses actual sixteen-point maximum');
    ck(!f.s.players.Bob.traits.includes('Resonant')&&f.s.players.Bob.resources.Resonance===16,'Untalented party member still needs twenty');
    ck(!f.s.players.Alice.traits.some(t=>/^Resonance:/.test(t)),'Early readiness removes intermediate grade');
    for(let i=0;i<4;i++)f.turn({semantic:(n,r)=>n==='Bob'&&react(n,r)});
    f.turn();f.turn();
    ck(f.s.players.Bob.traits.includes('Resonant')&&f.s.players.Bob.resources.Resonance===20,'Normal twenty-point readiness preserved');
    f.turn({semantic:(n,r)=>n==='Alice'&&r.name==='mx_resonance_spend'});
    f.turn();f.turn();
    ck(f.s.players.Alice.resources.Resonance===0&&!f.s.players.Alice.traits.includes('Resonant'),'Own burst consumes own readiness');
    ck(f.s.players.Bob.traits.includes('Resonant'),'Other player retains readiness');
}
for(let n=16;n<20;n++){
    const marker=w.triggerDefinitions.mx_resonance_init.conditions[0].value;
    const f=fixture(w,{players:{Alice:player({},[talent,marker,`Resonance: ${n}`])}});
    f.turn();f.turn();
    ck(f.s.players.Alice.traits.includes('Resonant')&&f.s.players.Alice.resources.Resonance===16,'Lowering an already earned capacity preserves readiness '+n);
}
{
    const f=fixture(w,{players:{Alice:player({},[talent])}});f.turn();
    f.s.players.Alice.resources.Resonance=16;f.turn();f.turn();
    ck(f.s.players.Alice.resources.Resonance===0&&!f.s.players.Alice.traits.includes('Resonant'),'Refill alone cannot manufacture earned charge');
}
{
    const ow=structuredClone(w),r=structuredClone(w.triggerDefinitions.rb_otherworld_origin);
    r.name='mx_origin_fixture';ow.triggerDefinitions={mx_origin_fixture:r};
    const f=fixture(ow,{players:{Alice:player({},[origin]),Bob:player()}});f.s.tick=12;f.turn();
    ck(f.s.players.Alice.traits.includes('Summoned one'),'Origin grants campaign marker');
    ck(!f.s.players.Bob.traits.includes('Summoned one'),'Unrelated player is not a bearer');
    ck(f.s.storage.rbCampaign===true&&f.s.storage.rbOriginTick===12,'First bearer initializes the campaign at actual tick');
    f.s.storage.rbPhase=5;f.s.players.Charlie=player({},[origin]);f.turn();
    ck(f.s.storage.rbPhase===5&&f.s.storage.rbOriginTick===12,'Late origin does not restart an existing campaign');
}
for(const [tick,combat,town,expected]of [[99,false,true,false],[100,false,true,true],[110,true,true,false],[110,false,false,false]]){
    const storage={rbCampaign:true,rbOriginTick:0};
    const check=c=>({'game-tick':tick,'player-traits':{Alice:['Summoned one']},'player-level':{Alice:1},'npc-in-combat':combat,'party-location':town?'Brookmeadow':'Pinewater River','party-realm':'Glowhaven','quest-status':'hidden'}[c.type]);
    vm.runInNewContext(w.triggerDefinitions.rb_clock.script,{storage,check},{timeout:100});
    ck(storage.rbTownReady===expected,'Actual clock: tick/combat/place '+[tick,combat,town]);
}
const levels=read(path.join(__dirname,'playtest-phantom/level-review.json')).rows;
const changed=new Set(levels.map(r=>r.npc));
for(const [name,npc]of Object.entries(w.npcs)){
    const old=before.npcs[name];
    if(!changed.has(name)){assert.deepStrictEqual(npc,old);checks++;continue;}
    const a=structuredClone(npc),b=structuredClone(old);delete a.level;delete b.level;
    assert.deepStrictEqual(a,b);checks++;
    ck(npc.level<old.level,'Background level only decreases '+name);
}
for(const name of ['Haruho Taneda','Mihana Orihara'])ck(w.npcs[name].level===3&&levels.find(r=>r.npc===name).afterNeutralHP===102,'Ordinary worker level and native health '+name);
for(const name of ['Ilyra Stillglass','Ragnar Leonhart',"Valkazathoth'dmir",'Noelle Ashford'])ck(!changed.has(name),'Protected established combatant '+name);
ck(w.traitCategories['Past Experience'].traits.length===before.traitCategories['Past Experience'].traits.length+18,'Eighteen past experiences');
ck(w.traitCategories['First Impression'].traits.includes('Unbothered Bearing'),'Chilled first impression');
ck(w.progressionSettings.startingCharacterLevelUpRequirement===550,'Starting XP five hundred fifty');
ck(w.progressionSettings.abilityPointEveryLevels===1&&w.progressionSettings.abilityPointsPerGrant===1,'False alarm leaves ability point grants unchanged');
ck(w.progressionSettings.milestoneTitles.at(-1).title==='A Story Without End','Full milestone ladder through 150');
for(let i=0;i<before.relationshipStages.length;i++){
    ck(w.relationshipStages[i].minScore===before.relationshipStages[i].minScore&&w.relationshipStages[i].maxScore===before.relationshipStages[i].maxScore,'Relationship bounds unchanged '+i);
}
const resources=Object.keys(w.resourceSettings),ri=resources.indexOf('Resonance');
ck(ri===resources.indexOf('Stamina')+1&&ri<resources.indexOf('Infamy')&&ri<resources.indexOf('Renown'),'Requested resource order');
ck(w.nameFilterSettings.Fenwick.replacements.length===8,'Fenwick filter');
console.log(JSON.stringify({status:'passed',checks,levelRecords:levels.length,livePlaytest:false,scope:'Actual emitted native rules; supplied semantic judgments, not live AI or Studio UI.'}));
