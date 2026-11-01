if(!solo){say('Official individual championship registration currently supports one human player in this adventure, with NPC companions welcome outside the ring. In multiplayer, ordinary consensual sparring and the venue remain available; do not register or charge the entire party as one fighter.');skip=false;}
else if(['ready','live','between','review','away'].includes(c.phase)){skip=true;}
else if(tick<c.nextTick){say('The next championship is not ready yet: '+(c.nextTick-tick)+' completed turns remain before another edition. Sparring, conversation and optional instruction remain available.');}
else{
 const level=levels[names[0]],gap=level<=10?2:Math.max(4,Math.ceil(level*.3));
 const available=roster.filter(x=>check({type:'npc-in-party',npc:x.name})!==true&&check({type:'npc-in-combat',npc:x.name})!==true&&!(typeof health(x.name)==='number'&&health(x.name)<=0));
 let pool=available.filter(x=>Math.abs(x.level-level)<=gap);
 if(pool.length<3)pool=available.filter(x=>x.level<=level+gap).sort((a,b)=>Math.abs(a.level-level)-Math.abs(b.level-level)).slice(0,7);
 if(pool.length<3){say('There are not enough fit, available competitors for a fair card. Offer ordinary sparring or a later registration without charging or inventing replacements.');}
 else{
  c.edition++;c.seed=(tick*1949+c.edition*7919+31337)>>>0;
  const target=pool.length>=7?7:3;
  const selected=[];while(pool.length&&selected.length<target){selected.push(pool.splice(Math.floor(rnd()*pool.length),1)[0]);}
  // Choose the field size from the original available band, not its shrinking remainder.
  const size=selected.length>=7?8:4;selected.length=size-1;
  c.title=['First Bloom Cup','Highsun Clash','Harvest Crown','Frostglass Championship'][(c.edition-1)%4]+' — Edition '+c.edition;
  c.division=level<=12?'Initiates':level<=25?'Rising':level<=45?'Veteran':'Crown';
  c.entrant=names[0];c.roster=['@',...selected.map(x=>x.name)];c.matches=[];c.exhibition=false;c.outcome='entered';c.champion=null;c.registeredTick=tick;c.purse=80+Math.min(700,Math.floor(level*10));
  let ids=[];for(let i=0;i<size;i+=2){const id='R1M'+(i/2);ids.push(id);c.matches.push({id,players:c.roster.slice(i,i+2),arena:rings[(i/2+c.edition)%rings.length],attempt:1});}
  let round=2;while(ids.length>1){const next=[];for(let i=0;i<ids.length;i+=2){const id='R'+round+'M'+i/2;next.push(id);c.matches.push({id,parents:ids.slice(i,i+2),players:[],arena:rings[(round+c.edition)%rings.length],attempt:1});}ids=next;round++;}
  c.match='R1M0';setPhase('ready');mirror();
  const m=current();effects.push({type:'known-entity',entity:opponent(m),operator:'set',value:true});
  effects.push({type:'npc-placement',npc:opponent(m),operation:'moveTo',location:venue,area:'The Eternal Crucible - Competitor Lounge'});
  say('Registration is accepted for '+c.title+', '+c.division+' division. This is a '+size+'-entrant individual bracket, '+Math.log2(size)+' player bouts to win, no entry fee, and a '+c.purse+'-mark championship purse plus trophy. Announce the actual selected field: '+selected.map(x=>x.name+' (level '+x.level+')').join(', ')+'. Preserve authored power levels. First opponent: '+opponent(m)+'; arena: '+m.arena+'. Explain nonlethal subdual, surrender, referee stops, legal finite summons, no outside assistance and no live-bout mana potions/reserve batteries. Ordinary catalysts are legal. Introduce at most two people at once; offer the lounge and wait for readiness.');
 }
}

