// Exact scope proof for the universal-fishing follow-up, not a broad approval.
const fs=require('fs'),path=require('path'),cp=require('child_process'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),base='a1315e6';
const before=JSON.parse(cp.execFileSync('git',['show',base+':world-draft/WorldAlpha - World.json'],{cwd:root,encoding:'utf8',maxBuffer:30*1024*1024}));
const after=JSON.parse(fs.readFileSync(path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'manifest.json'),'utf8'));
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b),changes=[];
function walk(a,b,p){if(equal(a,b))return;if(a&&b&&typeof a==='object'&&typeof b==='object'&&!Array.isArray(a)&&!Array.isArray(b)){
 for(const k of new Set([...Object.keys(a),...Object.keys(b)])){if(!(k in a))changes.push({path:[...p,k],kind:'added'});else if(!(k in b))changes.push({path:[...p,k],kind:'removed'});else walk(a[k],b[k],[...p,k])}
}else changes.push({path:p,kind:'changed'})}
walk(before,after,[]);
const triggerKeys=['fsh_basics','fsh_cast_lure','fsh_cast_bait','fsh_bait_miss','fsh_rare_land','fsh_rare_miss','fsh_rare_release','fsh_rare_cleanup'];
for(const {path:p,kind}of changes){const [section,key,field]=p;
 const allowed=section==='itemTypes'&&kind==='added'&&p.length===2&&m.regionalFishAdded.includes(key)
 ||section==='triggerDefinitions'&&triggerKeys.includes(key)&&['conditions','script'].includes(field)
 ||section==='parties'&&p[1]===''&&p[2]==='quests'&&m.quests.includes(p[3])&&['description','questStatement'].includes(p[4])
 ||section==='worldLore'&&['Angling around Glowhaven','Angling and Regional Waters'].includes(key)
 ||section==='aiInstructions'&&key==='ItemGenerationAndUsage'&&field==='Fishing Stock and Catches';
 assert(allowed,'Unrelated universal-fishing change: '+p.join('/'));
}
for(const name of m.quests){const b=structuredClone(before.parties[''].quests[name]);b.questStatement=b.description;delete b.description;assert.deepStrictEqual(after.parties[''].quests[name],b,'Only supported statement field rename: '+name)}
assert(Object.keys(after.triggerDefinitions).length===Object.keys(before.triggerDefinitions).length,'No new controllers');
assert(m.regionalFishAdded.length===21&&m.regionalFishAdded.every(n=>!(n in before.itemTypes)&&n in after.itemTypes),'Exactly 21 new species');
const report={baseCommit:base,status:'reviewed',changedLeaves:changes.length,changes,preserved:['NPCs and portraits','all locations/areas and maps','Spider Realm data and triggers','weather controller','old species and tackle','all non-fishing quests and rewards','music, progression and character creation'],livePlaytest:false};
fs.writeFileSync(path.join(__dirname,'universal-review.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,changedLeaves:changes.length,newSpecies:21,newControllers:0}));
