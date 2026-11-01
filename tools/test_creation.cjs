// Data and effect fixtures, not an implementation of Voyage's model or UI.
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const w=JSON.parse(fs.readFileSync(process.argv[2]||path.join(root,'world-draft','WorldAlpha - World.json'),'utf8'));
const m=JSON.parse(fs.readFileSync(path.join(__dirname,'phantom','manifest.json'),'utf8'));
let checks=0;const ck=(v,n)=>{checks++;assert.ok(v,n)};
function make(names){
 const out={attributes:Object.fromEntries(w.attributeSettings.attributeNames.map(k=>[k,w.attributeSettings.startingAttributeValue])),skills:{},resources:Object.fromEntries(Object.entries(w.resourceSettings).map(([k,v])=>[k,v.maxValue])),abilities:new Set(),items:{}};
 for(const name of names){const t=w.traits[name];ck(!!t,'Actual chosen trait '+name);
  for(const b of t.attributes)out.attributes[b.attribute]+=b.modifier;
  for(const b of t.skills)out.skills[b.skill]=(out.skills[b.skill]||0)+b.modifier;
  for(const b of t.resources)out.resources[b.resource]+=b.modifier;
  for(const a of t.abilities)out.abilities.add(a);
  for(const i of t.startingItems)out.items[i.item]=(out.items[i.item]||0)+i.quantity;
 }
 for(const k in out.attributes)out.attributes[k]=Math.min(out.attributes[k],w.attributeSettings.maxStartingAttribute);
 return out;
}
const physical=make(['Human','Primary Force','Secondary Finesse','Physical Foundations','Force Training','Finesse Training','Blacksmith Apprentice','Iron Lotus Constitution','Tonfa Starter Kit']);
ck(physical.attributes.force>15&&physical.attributes.finesse>13,'Physical Foundations has actual attribute impact');
ck(!Object.keys(physical.skills).some(k=>k.endsWith(' Magic')),'No affinity/study selection remains a valid noncaster');
ck(physical.resources.Health===145&&physical.resources.Mana===70,'Talent has real benefit and real trade-off');
ck(physical.items['Ironwood Tonfa Pair']===1,'One actual selected kit grant');
ck(!physical.items['Guild Badge: Bronze'],'No licence from prior work or talent');
const mage=make(['Fae','Primary Intuition','Secondary Passion','Ice Studies','Cautious','Observant','Paper Lantern Body']);
ck(mage.resources.Health===70&&mage.resources.Mana===150&&mage.resources.Stamina===90,'Fragile talent uses current resource baselines');
ck(mage.attributes.intuition===20,'Real creation ceiling handles combined bonuses');
ck(mage.skills['Ice Magic']===3&&mage.abilities.size===2,'Study grants only its actual two techniques');
const skip=make(['Physical Foundations']);
ck(skip.attributes.force===11&&skip.attributes.finesse===11&&!skip.abilities.size,'Physical alternative grants no spells');
ck(w.traitCategories['Special Talent'].maxSelections===1,'One optional special talent');
ck(w.traitCategories['Natural Magical Affinity'].description.includes('zero'),'Empty affinity choice explicitly supported');
ck(w.traitCategories['Starting Magical Study'].traits[0]==='Physical Foundations','Physical option comes first');
ck(w.traitCategories['Profession & Useful Skills'].maxSelections===1,'Profession remains one background');
ck(w.traitCategories['Starting Equipment'].maxSelections===1,'Extra kits do not stack');
for(const name of m.talents){
 const t=w.traits[name];const p=make([name]);
 ck(!t.startingItems.length,'No undeclared gear from talent '+name);
 ck(p.resources.Health>0&&p.resources.Mana>0&&p.resources.Stamina>0,'No starting resource deficit '+name);
 for(const a of t.abilities)ck(w.abilities[a].requirements.some(r=>r.type==='trait'&&r.variable===name&&r.amount===1),'Technique has a complete requirement for the actual chosen gift');
}
for(const name of m.newKits){
 const t=w.traits[name];ck(t.startingItems.length>0,'Actual item kit '+name);
 ck(!t.skills.length&&!t.attributes.length&&!t.abilities.length,'Kit is equipment, not mastery '+name);
 for(const i of t.startingItems)ck(!!w.itemTypes[i.item]&&i.quantity===1,'Real single starter item '+name);
}
for(const name of ['Portrait Style','Portrait Framing','Portrait Camera','Portrait Background']){
 const c=w.traitCategories[name];ck(c.maxSelections===1,'Single portrait dimension '+name);
 ck(c.subcategories[0].name==='Default','Defaults visibly grouped '+name);
 const seen=new Set();for(const g of c.subcategories)for(const t of g.traits){ck(!seen.has(t),'No duplicate subcategory choice '+t);seen.add(t)}
}
ck(!w.traits['Hair Style — Bald'].startingItems.length,'Bald option is visual');
ck(w.traitCategories['Accessories & Outer Layers'].maxSelections<=4,'Bounded accessory selections');
for(const [name,cue] of [['Fighting','combat'],['Dead','dead'],['Travelling','travel']]){
 ck(!w.gameplayMusicSettings.tracks[name].matchTags.length,'No topic-word match for '+name);
 ck(w.gameplayMusicSettings.tracks[name].cues.includes(cue),'Keep real engine cue for '+name);
}
// Certification is the sole Bronze award; spending its real records prevents a repeat.
const badge=w.triggerDefinitions.gh_guild_exam_certify;
const bag={'Guild Exam Docket':1,'Guild Judgment Pass':1,'Guild Practical Pass':1};
const hasRecords=()=>badge.conditions.filter(c=>c.type==='player-item').every(c=>(bag[c.item]||0)>c.value);
ck(hasRecords(),'Applicant has all real pass records');
for(const e of badge.effects){
 if(e.type==='item-remove')bag[e.item]=(bag[e.item]||0)-e.quantity;
 if(e.type==='item-add')bag[e.item]=(bag[e.item]||0)+e.quantity;
}
ck(bag['Guild Badge: Bronze']===1&&!hasRecords(),'One certification award, no repeat from spent papers');
ck(!w.itemTypes['Bronze Guild Badge'],'No competing authored badge');
ck(w.itemTypes['Guild Badge: Bronze'].category==='Document'&&!!w.itemTypes['Guild Badge: Bronze'].imageUrl,'Canonical badge retains correct category and art');
ck(!w.parties[''].quests['Guild: Adventurer Licensure'].onCompleteEffects.some(e=>e.type==='item-add'&&/badge/i.test(e.item)),'Quest completion does not also grant a badge');
ck(w.aiInstructions.ItemGenerationAndUsage['Keys, Credentials and Information Items'].includes('must not add another badge'),'Inventory generation reserves the typed grant');
console.log(JSON.stringify({status:'passed',checks,scope:'Creation arithmetic, references and native effect fixtures; no live UI, image generation or semantic judgment.'}));
