// Read-only diagnostics for an external audit. No world edits or semantic claims.
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'../..');
const raw=fs.readFileSync(path.join(root,'world-draft/WorldAlpha - World.json'));
const w=JSON.parse(raw),quests=w.parties[''].quests;
const refs=name=>[
 ...Object.entries(w.triggerDefinitions).filter(([,v])=>JSON.stringify(v).includes(name)).map(([k])=>'trigger:'+k),
 ...Object.entries(w.storyStarts).filter(([,v])=>v.startingQuests?.includes(name)).map(([k])=>'start:'+k),
 ...Object.entries(quests).filter(([,v])=>JSON.stringify(v.onCompleteEffects||[]).includes(name)).map(([k])=>'completion:'+k)
];
const alleged=['The Cost of a Courtyard','One Honest Demonstration','The Ledger and the Soup','A Patient Distance','The Bow That Will Not Settle','The Oven and the Boundary','The Archive Has Two Dates','The Last Dry Platform','The Name on the Parcel','Expedition: The Bamboo Method',"Expedition: A Reed Bell's Answer",'An Unmarked Parcel','The Wrong Water Seal'];
const coverage=alleged.map(name=>({name,status:quests[name]?.status,explicitReferences:refs(name)}));
const category=name=>{const c=w.traitCategories[name],sub=c.subcategories.flatMap(s=>s.traits);return {root:c.traits.length,subcategories:sub.length,rootOnly:c.traits.filter(n=>!sub.includes(n)),undefined:[...new Set([...c.traits,...sub])].filter(n=>!w.traits[n])};};
// Exercise the emitted registry with the documented mutable triggers object.
function study(firstTick,wording){
 const storage={},triggers={},item="Teaching Scroll: The Porter's Invisible Palm";
 const run=(tick,text)=>{
  const check=c=>({'game-tick':tick,'action-text':[text],'story-text':'The scroll diagram is on the table for continued study.','player-traits':{Alice:[]},'player-item':c.item===item?{Alice:1}:{Alice:0}}[c.type]);
  const box={check,storage,triggers,effects:[],skip:false};
  vm.runInNewContext(w.triggerDefinitions.rb_scroll_registry_01.script,box,{timeout:500});
  return {tick,focused:storage.rbScrollFocus?.rb_study_001??null,registered:!!triggers.rb_study_001};
 };
 const rows=[run(firstTick,"I study Teaching Scroll: The Porter's Invisible Palm")];
 for(let t=firstTick+1;t<=firstTick+8;t++)rows.push(run(t,wording));
 return rows;
}
function board(text){
 const storage={ghGuildDisplayedOffers:['Guild: Rats in the Cellar']};
 const check=c=>c.type==='action-text'?[text]:c.type==='game-tick'?80:c.type==='player-level'?{Alice:3}:c.type==='player-item'?{Alice:c.item==='Guild Badge: Bronze'?1:0}:c.type==='quest-status'?'hidden':undefined;
 const box={storage,check,effects:[],skip:false};
 vm.runInNewContext(w.triggerDefinitions.gh_guild_board.script,box,{timeout:500});
 return {text,skipped:box.skip,offered:box.effects.filter(e=>e.type==='quest-init').map(e=>e.value)};
}
const items=['Starward Shield','Violet Weather Cloak','Takamine Travel Case'].map(name=>({name,category:w.itemTypes[name].category,slot:w.itemTypes[name].slot??null,bonuses:w.itemTypes[name].bonuses}));
const report={worldSHA256:crypto.createHash('sha256').update(raw).digest('hex'),readOnly:true,livePlaytest:false,
 counts:{npcs:Object.keys(w.npcs).length,locations:Object.keys(w.locations).length,triggers:Object.keys(w.triggerDefinitions).length},
 creation:{appearance:category('Appearance Builder'),equipment:category('Starting Equipment'),strawberry:w.traits['Strawberry Blond'],toughSkinned:w.traits['Tough Skinned']},
 questActivation:coverage,
 registry:{studyWording:study(10,'I study the diagram.'),continueWording:study(10,'I continue studying the diagram.'),tickZero:study(0,'I continue studying the diagram.')},
 board:[board('Show me the board.'),board('Okay, show me the board.')],
 equipment:items,
 emptyRegions:['Longgrass Meadows','Sunmead Plain'].map(name=>({name,locations:Object.values(w.locations).filter(l=>l.region===name).length})),
 note:'Semantic answers are not simulated. These are static facts and isolated emitted-script observations; they do not establish live engine scheduling or UI behavior.'};
const target=path.join(__dirname,'audit-evidence.json');fs.writeFileSync(target,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({report:target,missingActivation:coverage.filter(r=>r.status==='hidden'&&!r.explicitReferences.length).length,
 scrollStudyFocusAtEnd:report.registry.studyWording.at(-1),scrollContinueFocusAtEnd:report.registry.continueWording.at(-1),tickZeroNext:report.registry.tickZero[1],board:report.board}));
