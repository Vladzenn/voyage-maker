// Authoring-time proof against the exact pre-task Git commit. Does not edit world.
const fs=require('fs'),path=require('path'),cp=require('child_process'),crypto=require('crypto'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),file=path.join(__dirname,'manifest.json');
const m=JSON.parse(fs.readFileSync(file,'utf8'));
const before=JSON.parse(cp.execFileSync('git',['show',m.baseCommit+':world-draft/WorldAlpha - World.json'],{cwd:root,encoding:'utf8',maxBuffer:30*1024*1024}));
const after=JSON.parse(fs.readFileSync(path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(v)).digest('hex');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const sortedHash=v=>hash(sort(v));
const preStudioSha256=sortedHash(before);
// Reconstruct the newly supplied merge BASE from its three exact source edits,
// then prove our patch against that base. Production retains those exact edits.
const incoming=JSON.parse(fs.readFileSync(path.join(__dirname,'studio-merge.json'),'utf8'));
for(const r of incoming.changes){let owner=before;for(const k of r.path.slice(0,-1))owner=owner[k];const key=r.path.at(-1);
 assert(r.path[0]==='gameplayMusicSettings','Only the reviewed incoming music delta belongs here');
 if(r.kind!=='added')assert(equal(owner[key],r.before),'Exact original Studio merge field');
 if(r.kind==='removed')delete owner[key];else owner[key]=structuredClone(r.after);
}
const allowed=new Set(['skills','traits','traitCategories','itemTypes','itemSettings','triggerDefinitions','parties','worldLore','aiInstructions','imagePromptConfiguration']);
for(const k of Object.keys(before))if(!allowed.has(k))assert(equal(before[k],after[k]),'Unrelated section changed: '+k);
function oldExact(section,exceptions=[]){for(const [k,v]of Object.entries(before[section]))if(!exceptions.includes(k))assert(equal(v,after[section][k]),section+'/'+k+' changed unexpectedly')}
oldExact('skills');oldExact('itemTypes');oldExact('worldLore');
oldExact('traits',['Fisher','Portrait Frame — Hip-up','Portrait Style — Fantasy RPG illustration','Portrait Style — Dramatic gacha illustration','Portrait Style — Elegant linework']);
oldExact('traitCategories',['Starting Equipment','Portrait Framing','Portrait Style']);
oldExact('triggerDefinitions',['ghx_local_commissions']);
for(const k of Object.keys(after.triggerDefinitions))if(!(k in before.triggerDefinitions))assert(k.startsWith('fsh_')||m.repairedLocalOffers.includes(k),'Unexpected trigger '+k);
const bp=structuredClone(before.parties),ap=structuredClone(after.parties);
for(const k of m.quests){assert(!(k in bp[''].quests),'Quest key collision '+k);delete ap[''].quests[k]}
assert(equal(bp,ap),'Existing quests/arcs/party data changed');
for(const [task,leaves]of Object.entries(before.aiInstructions))for(const [key,v]of Object.entries(leaves)){
 const editable=(task==='generateCharacterBackground'&&['Appearance Construction and Support','Appearance Depth and Visual Continuity'].includes(key))||(task==='generateActionInfo'&&key==='Exact Skill Routing');
 if(!editable)assert(equal(v,after.aiInstructions[task][key]),'Unrelated AI leaf changed '+task+'/'+key);
}
for(const key of Object.keys(before.imagePromptConfiguration))if(key!=='npcs')assert(equal(before.imagePromptConfiguration[key],after.imagePromptConfiguration[key]),'Other image route changed');
const bItems=structuredClone(before.itemSettings),aItems=structuredClone(after.itemSettings);
for(const tier of Object.values(aItems.tiers))tier.bonusPolicy.allowedBonuses=tier.bonusPolicy.allowedBonuses.filter(x=>!(x.type==='skill'&&x.variable==='Fishing'));
assert(equal(bItems,aItems),'Other equipment economy settings changed');
const changes=[];
function walk(a,b,p){if(equal(a,b))return;if(a&&b&&typeof a==='object'&&typeof b==='object'&&!Array.isArray(a)&&!Array.isArray(b)){
 for(const k of new Set([...Object.keys(a),...Object.keys(b)])){if(!(k in a))changes.push({path:[...p,k],kind:'added'});else if(!(k in b))changes.push({path:[...p,k],kind:'removed'});else walk(a[k],b[k],[...p,k])}
}else changes.push({path:p,kind:'changed'})}
walk(before,after,[]);
m.changes=changes;m.beforeSha256=hash(before);m.afterSha256=hash(after);
m.unchangedTopLevel=Object.fromEntries(Object.entries(before).filter(([k,v])=>equal(v,after[k])).map(([k,v])=>[k,hash(v)]));
m.newTriggerKeys=Object.keys(after.triggerDefinitions).filter(k=>!(k in before.triggerDefinitions));
m.source='Latest Studio export 366606e8-3528-434f-80b6-fef091104a73, reconstructed exactly from pre-task commit plus the separately recorded three music edits. No older candidate snapshot.';
fs.writeFileSync(file,JSON.stringify(m,null,2)+'\n');
// A separate exact, reversible patch for historical TEST views only. Existing
// preservation fingerprint files are never edited. Full before/after hashes
// ensure an unrelated mutation cannot disappear behind this projection.
const get=(o,p)=>p.reduce((v,k)=>v?.[k],o);
const rows=changes.map(c=>({...c,...(c.kind!=='added'?{before:get(before,c.path)}:{}),...(c.kind!=='removed'?{afterSha256:sortedHash(get(after,c.path))}:{})}));
fs.writeFileSync(path.join(__dirname,'historical-test-projection.json'),JSON.stringify({purpose:'Exact Fishing patch and three separately verified incoming music edits for old preservation assertions only; all behavior tests execute current data.',baseCommit:m.baseCommit,preStudioSha256,beforeSha256:sortedHash(before),afterSha256:sortedHash(after),rows},null,2)+'\n');
fs.writeFileSync(path.join(root,'output/fishing-2026-11-04/Reviewable Changes.json'),JSON.stringify({baseCommit:m.baseCommit,changes,preserved:['NPCs and portraits','all location/area images and coordinates','regions and realm maps','Spider content','existing quests and arcs','music and voices','starting currency and progression']},null,2)+'\n');
console.log(JSON.stringify({status:'reviewed',changedLeaves:changes.length,newTriggers:m.newTriggerKeys.length,unchangedSections:Object.keys(m.unchangedTopLevel).length}));
