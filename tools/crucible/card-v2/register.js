if(!solo){say('Controlled individual championships currently take one human entrant; NPC companions may attend outside the ring. Do not register the human party as one fighter.');}
else if(active()){skip=true;}
else if(tick<c.nextTick){say('Another championship opens in '+(c.nextTick-tick)+' completed turns. Conversation, spectating and willing friendly matches remain available.');}
else{
 const entrant=names[0],level=levels[entrant],gap=level<=10?2:Math.max(4,Math.ceil(level*.3));
 let pool=roster.filter(x=>x.name!==entrant&&available(x)&&Math.abs(x.level-level)<=gap);
 if(pool.length<2)pool=roster.filter(x=>x.name!==entrant&&available(x)&&x.level<=level+gap).sort((a,b)=>Math.abs(a.level-level)-Math.abs(b.level-level)).slice(0,7);
 if(pool.length<2){say('There are too few fit, willing, available opponents for a suitable title card. No entry or payment is created. Offer ordinary practice or a later visit.');}
 else{
  c.edition++;c.seed=(tick*1949+c.edition*7919+31337)>>>0;c.entrant=entrant;c.entryLevel=level;c.gap=gap;
  const count=pool.length>=3?3:2,selected=[];while(selected.length<count)selected.push(pool.splice(Math.floor(rnd()*pool.length),1)[0]);
  c.title=['First Bloom Cup','Highsun Clash','Harvest Crown','Frostglass Championship'][(c.edition-1)%4]+' — Edition '+c.edition;
  c.division=level<=12?'Initiates':level<=25?'Rising':level<=45?'Veteran':'Crown';c.purse=80+Math.min(700,Math.floor(level*10));c.index=0;c.exhibition=false;c.outcome='competing';c.phase='waiting';c.registeredTick=tick;
  c.used=selected.map(x=>x.name);c.roster=c.used.slice();
  c.card=selected.map((x,i)=>({id:'E'+c.edition+'B'+(i+1),opponent:x.name,level:x.level,arena:rings[(i+c.edition)%rings.length],label:i===count-1?'Final':i===count-2?'Semifinal':'Opening bout'}));
  mirror();say('Registration is accepted for '+c.title+', '+c.division+' division: '+count+' scheduled player bouts, no entry fee, '+c.purse+' marks and a trophy for winning the final. Announce this fixed card: '+c.card.map(x=>x.label+' — '+x.opponent+' (level '+x.level+'), '+x.arena).join('; ')+'. Actual NPC levels stand. Explain nonlethal subdual, surrender/referee stops, both eliminated on simultaneous knockout, finite summons, no outside assistance or live-bout mana potions/reserves. Only explicit forfeiting ends an entry voluntarily; ordinary movement is not a result.');callNext();
 }
}
