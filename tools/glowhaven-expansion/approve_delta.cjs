// Extend historical preservation fingerprints with this explicitly reviewed update.
// Original "before" records remain intact; actual gameplay fixtures use current data.
const fs=require('fs'),path=require('path'),cp=require('child_process'),crypto=require('crypto'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),dest=path.join(root,'tools/oni-nation/approved-delta.json');
const before=JSON.parse(cp.execFileSync('git',['show','HEAD:world-draft/WorldAlpha - World.json'],{cwd:root,maxBuffer:30*1024*1024,encoding:'utf8'}));
const after=JSON.parse(fs.readFileSync(path.join(root,'world-draft/WorldAlpha - World.json'),'utf8'));
const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;
const hash=v=>crypto.createHash('sha256').update(JSON.stringify(sort(v))).digest('hex');
const d=JSON.parse(fs.readFileSync(dest,'utf8')),get=(x,parts)=>parts.reduce((v,k)=>v[k],x),report=[];
const sections=[...d.rows.map(r=>r.path),['aiInstructions']];
for(const parts of sections){
 const a=get(before,parts),b=get(after,parts);if(hash(a)===hash(b)){
  const prior=d.rows.find(r=>JSON.stringify(r.path)===JSON.stringify(parts));
  if(prior?.added)for(const k of Object.keys(prior.added))if(!(k in b))delete prior.added[k];
  continue;
 }
 let row=d.rows.find(r=>JSON.stringify(r.path)===JSON.stringify(parts));
 if(!row){row={path:parts,added:{},changed:{},removed:{}};d.rows.push(row)}
 assert(row.added,'Manual review required for whole-field preservation row '+parts.join('/'));
 for(const k of new Set([...Object.keys(a),...Object.keys(b)])){
  if(k in a&&k in b&&hash(a[k])===hash(b[k]))continue;
  report.push({path:[...parts,k],change:!(k in a)?'added':!(k in b)?'removed':'changed'});
  if(k in row.added){if(k in b)row.added[k]=hash(b[k]);else delete row.added[k];continue}
  if(k in row.changed){if(k in b)row.changed[k].afterSha256=hash(b[k]);else{row.removed[k]=row.changed[k].before;delete row.changed[k]}continue}
  if(k in row.removed){if(k in b){row.changed[k]={before:row.removed[k],afterSha256:hash(b[k])};delete row.removed[k]}continue}
  if(!(k in a))row.added[k]=hash(b[k]);
  else if(!(k in b))row.removed[k]=a[k];
  else row.changed[k]={before:a[k],afterSha256:hash(b[k])};
 }
 // An addition made earlier in this same uncommitted task can be removed by
 // a reviewed simplification. Do not leave its obsolete fingerprint behind.
 for(const k of Object.keys(row.added))if(!(k in b))delete row.added[k];
}
d.purpose='Historical pre-Oni preservation view, extended for author-supplied map pins, approved Glowhaven expansion and scoped portrait/academy/creation updates. See tools/glowhaven-expansion/merge-review.json for exact incoming-export preservation.';
fs.writeFileSync(dest,JSON.stringify(d,null,2)+'\n');
fs.writeFileSync(path.join(__dirname,'approved-field-diff.json'),JSON.stringify({baseCommit:cp.execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim(),rows:report},null,2)+'\n');
console.log(JSON.stringify({approvedRecordChanges:report.length,originalBeforeRecordsPreserved:true}));
