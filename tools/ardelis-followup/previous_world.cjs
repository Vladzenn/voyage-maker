// Exact reversible follow-up projection; no relaxed historical fingerprints.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previous(w){
 w=require('../ardelis-phantom/previous_world.cjs')(w);
 if(!w.npcs?.['Kenzō Shirogane'])return w;
 const r=JSON.parse(fs.readFileSync(path.join(__dirname,'review.json'),'utf8'));
 assert.strictEqual(hash(w),r.afterHash,'Only the exact reviewed naming/portrait follow-up enters historical checks');
 const out=structuredClone(w);
 for(const row of r.rows){let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
  if(row.kind==='removed')p[k]=structuredClone(row.before);
  else{assert.strictEqual(hash(p[k]),row.afterHash,'Exact follow-up delta '+row.path.join('/'));if(row.kind==='added')delete p[k];else p[k]=structuredClone(row.before);}}
 assert.strictEqual(hash(out),r.baseHash,'Reconstruct the exact released Ardelis authoring base');return out;
};
