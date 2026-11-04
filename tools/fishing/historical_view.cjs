// Read-only test projection. No baseline update, runtime change or file writes.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previousFishingView(world){
 world=require('../rebirth/previous_world.cjs')(world);
 if(!world.skills?.Fishing)return world;
 const d=JSON.parse(fs.readFileSync(path.join(__dirname,'historical-test-projection.json'),'utf8'));
 assert.strictEqual(hash(world),d.afterSha256,'Only the exact reviewed Fishing patch may enter the historical test view');
 const out=structuredClone(world);
 for(const r of d.rows){let owner=out;for(const k of r.path.slice(0,-1))owner=owner[k];const key=r.path.at(-1);
  if(r.kind==='removed'){assert(!(key in owner),'Removed field still absent');owner[key]=structuredClone(r.before)}
  else{assert.strictEqual(hash(owner[key]),r.afterSha256,'Exact Fishing field '+r.path.join('/'));if(r.kind==='added')delete owner[key];else owner[key]=structuredClone(r.before)}
 }
 assert.strictEqual(hash(out),d.beforeSha256,'Projection must reproduce the exact pre-task world, not mask unrelated changes');
 // The author supplied these three music edits during this task. Runtime data
 // keeps them; only old preservation assertions need their exact earlier view.
 const incoming=JSON.parse(fs.readFileSync(path.join(__dirname,'studio-merge.json'),'utf8'));
 for(const r of incoming.changes){let owner=out;for(const k of r.path.slice(0,-1))owner=owner[k];const key=r.path.at(-1);
  if(r.kind==='removed'){assert(!(key in owner),'Source-removed music still absent');owner[key]=structuredClone(r.before)}
  else{assert.strictEqual(hash(owner[key]),hash(r.after),'Exact incoming music edit');if(r.kind==='added')delete owner[key];else owner[key]=structuredClone(r.before)}
 }
 assert.strictEqual(hash(out),d.preStudioSha256,'Historical-only view must equal the exact pre-task Git world');
 return out;
};
