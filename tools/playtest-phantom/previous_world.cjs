// Exact reviewed inverse for older preservation suites; not gameplay code.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previous(w){
    const r=JSON.parse(fs.readFileSync(path.join(__dirname,'review.json'),'utf8'));
    const prior=JSON.parse(fs.readFileSync(path.join(__dirname,'../npc-conversations/review.json'),'utf8'));
    if([r.baseHash,prior.baseHash].includes(hash(w)))return w;
    assert.strictEqual(hash(w),r.afterHash,'Only the exact reviewed playtest patch enters historical fixtures');
    const out=structuredClone(w);
    for(const row of r.rows){
        let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
        if(row.kind!=='removed')assert.strictEqual(hash(p[k]),row.afterHash,'Exact playtest delta '+row.path.join('/'));
        if(row.kind==='added')delete p[k];else p[k]=structuredClone(row.before);
    }
    assert.strictEqual(hash(out),r.baseHash,'Exact pre-playtest world restored');return out;
};
