// Exact prose-only correction view for existing historical fixtures.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=w=>{
 const r=JSON.parse(fs.readFileSync(path.join(__dirname,'residential-correction.json'),'utf8'));
 if(hash(w)===r.baseHash)return w;
 assert.strictEqual(hash(w),r.afterHash,'Only the exact reviewed residential correction enters old fixtures');
 const out=structuredClone(w);
 for(const row of r.rows){let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
  assert.strictEqual(hash(p[k]),row.afterHash,'Exact residential prose delta');p[k]=row.before;}
 assert.strictEqual(hash(out),r.baseHash,'Reconstruct exact prior phantom patch');return out;
};
