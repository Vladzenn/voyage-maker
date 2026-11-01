if(!solo){say('Individual championships currently support a solo human session. Friends may roleplay spectators, but controlled bouts wait until the session is solo; do not register the whole party.');}
else if(active()){skip=true;}
else if(tick<c.nextTick){say('The next championship opens in '+(c.nextTick-tick)+' completed turns. Friendly practice remains available.');}
else{
 const entrant=names[0],level=levels[entrant],gap=level<=10?2:Math.max(4,Math.ceil(level*.3));
 let pool=roster.filter(x=>available(x)&&Math.abs(x.level-level)<=gap);
 if(pool.length<3)pool=roster.filter(x=>available(x)&&x.level<=level+gap).sort((a,b)=>Math.abs(a.level-level)-Math.abs(b.level-level)).slice(0,7);
 if(pool.length<3){say('Too few suitable fit opponents are available for a championship. Offer practice or another visit; no entry or fee is created.');}
 else{
  c.edition++;c.seed=(tick*1949+c.edition*7919+31337)>>>0;c.entrant=entrant;c.entryLevel=level;c.gap=gap;
  const count=pool.length>=7?7:3,selected=[];while(selected.length<count)selected.push(pool.splice(Math.floor(rnd()*pool.length),1)[0]);
  c.title=['First Bloom Cup','Highsun Clash','Harvest Crown','Frostglass Championship'][(c.edition-1)%4]+' — Edition '+c.edition;
  c.division=level<=12?'Initiates':level<=25?'Rising':level<=45?'Veteran':'Crown';c.purse=80+Math.min(700,Math.floor(level*10));c.card=[];c.index=0;c.exhibition=false;c.outcome='competing';c.phase='waiting';c.registeredTick=tick;c.champion=null;
  c.used=selected.map(x=>x.name);c.roster=c.used.slice();c.rounds=[];let slots=['@',...c.used],r=0;
  while(slots.length>1){const round=[];for(let i=0;i<slots.length;i+=2){const m={id:'E'+c.edition+'R'+r+'M'+i/2,done:false};if(!r)m.players=[slots[i],slots[i+1]];else m.parents=[slots[i],slots[i+1]];round.push(m);}c.rounds.push(round);slots=round.map(x=>x.id);r++;}
  schedule();mirror();say('Registration accepted for '+c.title+', '+c.division+': '+(count+1)+' entrants in a recorded elimination bracket. Field: '+entrant+', '+c.used.join(', ')+'. No entry fee; '+c.purse+' marks and a trophy for the champion. Actual levels stand. NPC-only bouts receive one abstract official result, checked for current availability, not simulated attacks. Announce subdual, surrender/referee stops, both eliminated on double knockout, finite summons and no outside assistance. No live-bout mana potions or reserves. Only an explicit forfeit voluntarily withdraws the entry.');callNext();
 }
}
