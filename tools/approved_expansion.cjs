// Reconstruct the exact pre-expansion view ONLY for old preservation assertions.
// Actual behavior tests continue to execute the current scripts and data.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previousView(world){
 if(!world.realms.Akitsuhara)return world;
 const d=JSON.parse(fs.readFileSync(path.join(__dirname,'oni-nation/approved-delta.json'),'utf8'));
 const out=structuredClone(world);
 for(const row of d.rows){
  let owner=out;for(const p of row.path.slice(0,-1))owner=owner[p];
  const field=row.path.at(-1),value=owner[field];
  if(row.added){
   for(const [k,h]of Object.entries(row.added)){assert.strictEqual(hash(value[k]),h,'Exact approved addition '+row.path.join('/')+'/'+k);delete value[k];}
   for(const [k,v]of Object.entries(row.changed)){assert.strictEqual(hash(value[k]),v.afterSha256,'Exact approved change '+row.path.join('/')+'/'+k);value[k]=structuredClone(v.before);}
   for(const [k,v]of Object.entries(row.removed)){assert.ok(!(k in value),'Removed entry remains removed '+k);value[k]=structuredClone(v);}
  }else{assert.strictEqual(hash(value),row.afterSha256,'Exact approved field '+row.path.join('/'));owner[field]=structuredClone(row.before);}
 }
 return out;
};
