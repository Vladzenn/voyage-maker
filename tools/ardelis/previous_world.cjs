// Exact reversible view for historical fixtures, never a permissive hash bypass.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previous(world){
 if(!world.realms?.Ardelis)return world;
 const r=JSON.parse(fs.readFileSync(path.join(__dirname,'review.json'),'utf8'));
 assert.strictEqual(hash(world),r.afterHash,'Only the exact reviewed Ardelis candidate may enter historical fixtures');
 const out=structuredClone(world);
 for(const row of r.rows){let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
  if(row.kind==='removed')p[k]=structuredClone(row.before);
  else{assert.strictEqual(hash(p[k]),row.afterHash,'Exact Ardelis delta '+row.path.join('/'));if(row.kind==='added')delete p[k];else p[k]=structuredClone(row.before);}
 }
 assert.strictEqual(hash(out),r.baseHash,'Reconstruct the exact approved Rebirth world');return out;
};
