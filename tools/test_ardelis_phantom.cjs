// Run the shipped scripts with deterministic RNG and supplied semantic answers.
// Semantic interpretation, NPC movement and narrator behavior still need live testing.
const fs=require('fs'),path=require('path'),assert=require('assert'),crypto=require('crypto'),vm=require('vm');
const root=path.resolve(__dirname,'..'),read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const w=read(process.argv[2]||path.join(root,'world-draft/WorldAlpha - World.json'));
const r=read(path.join(__dirname,'ardelis-phantom/review.json'));
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
let checks=0;const ck=(b,m)=>{checks++;assert.ok(b,m)};
ck(hash(w)===r.afterHash,'Exact reviewed output');
const base=structuredClone(w);
for(const row of r.rows){let p=base;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
 if(row.kind==='removed')p[k]=structuredClone(row.before);
 else{ck(hash(p[k])===row.afterHash,'Reviewed change '+row.path.join('/'));if(row.kind==='added')delete p[k];else p[k]=structuredClone(row.before);}}
ck(hash(base)===r.baseHash,'All non-patch content reconstructs the author export exactly');
const intended=new Set(['itemTypes','locations','npcs','storyStarts','triggerDefinitions','worldLore']);
ck(r.rows.every(x=>intended.has(x.path[0])),'Focused section scope');
for(const s of Object.keys(base).filter(s=>!intended.has(s)))ck(hash(w[s])===hash(base[s]),'Untouched '+s);
for(const [k,v]of Object.entries(base.npcs))if(k!=='Akihisa Sakimori')ck(hash(w.npcs[k])===hash(v),'Preserved complete NPC '+k);
for(const [k,v]of Object.entries(base.locations)){
 const now=w.locations[k==='residential area'?'Crownwater Row':k];
 for(const f of ['region','x','y','radius','images'])ck(hash(now[f]??null)===hash(v[f]??null),'Exact incoming pin/art '+k+'/'+f);
}
ck(hash(w.regions)===hash(base.regions),'All incoming region maps and Elsewhere pins exact');
ck(hash(w.combatSettings)===hash(base.combatSettings),'Incoming damage presentation exact');
for(const [k,v]of Object.entries(base.triggerDefinitions))if(!/^fsh_(cast_|bait_miss|rare_)/.test(k))ck(hash(w.triggerDefinitions[k])===hash(v),'Unchanged controller '+k);
const items=Object.keys(w.itemTypes).filter(k=>!base.itemTypes[k]);
ck(items.length===7&&r.fish.every(k=>items.includes(k)),'Six fish and one ownership key only');
ck(JSON.stringify(w.itemTypes).length<=250000,'Native item collection budget');
const starts=Object.keys(w.storyStarts),oldStarts=Object.keys(base.storyStarts);
ck(starts.filter(k=>!r.starts.includes(k)).join('|')===oldStarts.join('|'),'Existing start order preserved');
ck(starts.indexOf(r.starts[0])===starts.indexOf('🎭 Ardelis: An Orselle Invitation')+1,'New Ardelis starts grouped together');
for(const k of r.starts){const s=w.storyStarts[k];ck(s.name===k&&typeof s.storyStart==='string'&&s.storyStart.trim().length>0,'Named native opening '+k);
 ck(s.startingItems.filter(x=>x.item==='Mark').length===1&&s.startingItems.find(x=>x.item==='Mark').quantity===1000,'No extra money '+k);
 ck(s.startingPartyNPCs.length===0&&s.startingQuests.length===0,'No forced companions or commissions '+k);
 ck(s.locations.every(x=>w.regions[w.locations[x].region].realm==='Ardelis'),'Begin in Ardelis '+k);
 ck(s.locationAreas.every(x=>Object.hasOwn(w.locations[s.locations[0]].areas,x)),'Real starting area '+k);
 ck(/no Rebirth quest/i.test(s.questGenerationGuidance)&&s.questGenerationGuidance.includes('keyless'),'Accessible native transit guidance '+k);
}
const home=w.storyStarts['🏠 Ardelis: A Door of Your Own'];
ck(home.startingItems.filter(x=>x.item==='Key and Deed to 14 Crownwater Row').length===1,'Home key and deed issued once');
ck(!w.locations['residential area']&&w.locations['Crownwater Row'].x===base.locations['residential area'].x,'Finish exact new residential pin');
// No changes to the established travel/anomaly implementation.
for(const k of ['ar_portal_to','ar_portal_from','ar_issue_key'])ck(hash(w.triggerDefinitions[k])===hash(base.triggerDefinitions[k]),'Original route preserved '+k);
const key=w.triggerDefinitions.ar_local_key_issue;
ck(key.scope==='player'&&key.conditions.find(x=>x.type==='player-item').value===0,'Per-player no-duplicate issue guard');
ck(!key.conditions.some(x=>['read-boolean','quest-status','player-level'].includes(x.type)),'No campaign/rank dependency');
function issue(location,players){const emitted=[];
 const recipients=players.filter(p=>key.conditions.every(c=>c.type==='action'?p.semantic:c.type==='party-location'?location===c.value:c.type==='player-item'?p.key===c.value:false));
 for(const e of key.effects)if(e.type==='item-add'){
  const targets=e.target==='satisfyingPlayers'?recipients:e.target==='allPlayers'?players:[];
  for(const p of targets){p.key+=e.quantity;emitted.push(p.name);}
 }return emitted;}
const people=[{name:'Local',key:0,semantic:true},{name:'Visitor',key:0,semantic:false},{name:'Holder',key:1,semantic:true}];
ck(issue('Southbank Homes',people).length===0,'No remote key issue');
ck(issue('Caelrath Portal Hall',people).join()==='Local','Only actual eligible requester receives key');
ck(issue('Caelrath Portal Hall',people).length===0,'Repeat cannot duplicate held key');
ck(!w.triggerDefinitions.ar_portal_from.conditions.some(x=>x.type==='player-item'),'Native may cross to Glowhaven without any key');

function script(id,{realm='Ardelis',area='The High Reservoir - Fishing Bank',location='The High Reservoir',region='Crownwater Terraces',tick=10,storage={},random=()=>0,traits=[]}={}){
 const m=Object.create(Math);m.random=random;
 const raw={'party-realm':realm,'party-area':area,'party-location':location,'party-region':region,'action-text':['I cast my line into the water.'],'game-tick':tick,'player-traits':{Angler:traits}};
 const box={storage,effects:structuredClone(w.triggerDefinitions[id].effects),check:c=>{assert.ok(c.type in raw,c.type);return raw[c.type]},skip:false,Math:m};
 vm.runInNewContext(w.triggerDefinitions[id].script,box,{timeout:200});return box;
}
const rows=JSON.parse(w.triggerDefinitions.fsh_cast_lure.script.match(/^const fish=(.*);\n/)[1]);
ck(rows.length===57&&rows.filter(x=>x[6]==='i').length===6,'57 fish, six Ardelis rows');
ck(hash(rows.slice(0,51))===hash(JSON.parse(base.triggerDefinitions.fsh_cast_lure.script.match(/^const fish=(.*);\n/)[1])),'Previous catch rows unchanged');
for(const id of ['fsh_cast_lure','fsh_cast_bait']){
 ck(hash(JSON.parse(w.triggerDefinitions[id].script.match(/^const fish=(.*);\n/)[1]))===hash(rows),'Identical bait/lure catalogue');
 for(const habitat of ['r','h','s','d']){
  const place={r:['The High Reservoir','The High Reservoir - Fishing Bank'],h:['Caelrath Harbor','Caelrath Harbor - Harbor Quay'],s:['Crownlight Lighthouse','Crownlight Lighthouse - Coastal Beach'],d:['Open Sea','Open Sea - Offshore Deck']}[habitat];
  const pool=rows.filter(f=>(f[6]==='*'||f[6]==='i')&&f[1].includes(habitat));
  const weights=pool.map(f=>f[2]*(f[6]==='i'?1.5:1)*(id.endsWith('bait')&&(f[2]<=9||/Loach|Bream|Tench|Eel|Goby/.test(f[0]))?1.6:1));
  for(const f of pool.filter(f=>f[6]==='i')){
   const index=pool.indexOf(f),roll=(weights.slice(0,index).reduce((a,b)=>a+b,0)+weights[index]/2)/weights.reduce((a,b)=>a+b,0);
   const x=script(id,{location:place[0],area:place[1],random:()=>roll});
   ck(!x.skip,'Eligible actual cast runs '+id+'/'+f[0]);
   ck(x.effects.filter(e=>e.type==='item-remove').length===(id.endsWith('bait')?1:0),'Spend one bait only when selected');
   if(f[2]===2){ck(x.storage.fshHook?.fish==='Bellglass Carp'&&!x.effects.some(e=>e.type==='item-add'),'Rare fish hooked, not granted');
    for(const mode of ['land','miss','release','cleanup']){
     const y=script('fsh_rare_'+mode,{location:place[0],area:place[1],tick:mode==='cleanup'?17:11,storage:structuredClone(x.storage),traits:['Rare Fish on the Line']});
     ck(!y.skip,'New rare species recognized by '+mode);
     ck(y.effects.filter(e=>e.type==='item-add').length===(mode==='land'?1:0),'Only successful landing grants carp '+mode);
    }
   }else ck(x.effects.filter(e=>e.type==='item-add'&&e.item===f[0]&&e.quantity===1).length===1,'Land exact regional fish '+f[0]);
  }
 }
}
for(const realm of ['Glowhaven','Drakenspire Mountains','Asterveil Sky Archipelago','Akitsuhara','Future Realm']){
 const x=script('fsh_cast_lure',{realm,area:'Freshwater Lake - Bank',location:'Freshwater Lake',region:'Local Country',random:()=>.61});
 ck(!x.skip&&!x.effects.some(e=>e.type==='item-add'&&r.fish.includes(e.item))&&x.storage.fshHook?.fish!=='Bellglass Carp','No Ardelis fish leakage '+realm);
}
const state={};script('fsh_cast_lure',{storage:state});ck(script('fsh_cast_lure',{storage:state}).skip,'Existing same-turn catch guard retained');
console.log(JSON.stringify({status:'passed',checks,scope:'Exact author-export preservation; emitted fishing scripts; native start and transit structure. Semantic answers supplied, not live playtesting.'}));
