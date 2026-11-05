// Exact inverse of the three AI prose changes, for historical fixtures only.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previous(w){
    w=require('../playtest-phantom/previous_world.cjs')(w);
    const r=JSON.parse(fs.readFileSync(path.join(__dirname,'review.json'),'utf8'));
    if(hash(w)===r.baseHash)return w;
    assert.strictEqual(hash(w),r.afterHash,'Only the exact reviewed NPC conversation patch enters historical fixtures');
    const out=structuredClone(w);
    for(const row of r.rows){
        let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
        assert.strictEqual(hash(p[k]),row.afterHash,'Exact NPC conversation delta '+row.path.join('/'));
        p[k]=row.before;
    }
    assert.strictEqual(hash(out),r.baseHash,'Reconstruct exact pre-conversation world');
    return out;
};
