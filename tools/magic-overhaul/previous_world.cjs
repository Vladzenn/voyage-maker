// Exact inverse of this update for historical preservation fixtures only.
// Current mechanics are exercised separately by test_magic_overhaul.cjs.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
module.exports=function previous(w){
    if(!w.triggerDefinitions?.mx_scroll_catalogue)return w;
    const r=JSON.parse(fs.readFileSync(path.join(__dirname,'review.json'),'utf8'));
    assert.strictEqual(hash(w),r.afterHash,'Only the exact reviewed Magic Overhaul enters historical fixtures');
    const out=structuredClone(w);
    for(const row of r.rows){
        let p=out;for(const k of row.path.slice(0,-1))p=p[k];const k=row.path.at(-1);
        if(row.kind==='removed')p[k]=structuredClone(row.before);
        else{
            assert.strictEqual(hash(p[k]),row.afterHash,'Exact Magic Overhaul delta '+row.path.join('/'));
            if(row.kind==='added')delete p[k];else p[k]=structuredClone(row.before);
        }
    }
    assert.strictEqual(hash(out),r.baseHash,'Reconstruct exact pre-Magic canonical world');
    return out;
};
