if(!solo||c.entrant!==names[0]||!here||c.phase!=='waiting'){skip=true;}
else{
 const m=current(),p=playerHealth();
 if(!m||m.result||typeof m.startedTick==='number'){close('cancelled','invalid schedule');say('The inconsistent schedule closes without inventing a fight.');}
 else if(typeof p!=='number'||p<=0){say('The entrant cannot start while incapacitated or unassessed. Keep the entry; offer care. Full bars are not required.');}
 else if(!available({name:m.opponent})){
  const pool=roster.filter(x=>available(x)&&!c.used.includes(x.name)&&x.level<=c.entryLevel+c.gap).sort((a,b)=>Math.abs(a.level-c.entryLevel)-Math.abs(b.level-c.entryLevel)).slice(0,7);
  if(!pool.length){close('cancelled','no available substitute');say('No suitable unused replacement is available. Cancel without a free win or trophy.');}
  else{const old=m.opponent,x=pool[Math.floor(rnd()*pool.length)];m.replacements=m.replacements||[];m.replacements.push({opponent:old,tick});m.opponent=x.name;m.level=x.level;c.used.push(x.name);c.roster=c.used.slice();const n=node(m.node);if(n)n.players=n.players.map(p=>p===old?x.name:p);say(old+' is unavailable. Announce substitute '+x.name+' and wait for fresh readiness; no fight has started.');callNext();}
 }
 else{m.startedTick=tick;m.startHealth=p;m.opponentStartHealth=health(m.opponent);c.phase='live';storage.gh_lore_tournament_active=true;mirror();effects.push({type:'party-area',operator:'set',value:m.arena},{type:'npc-placement',npc:m.opponent,operation:'moveTo',location:venue,area:m.arena},{type:'known-entity',entity:m.opponent,operator:'set',value:true});say('Open '+m.label+': '+c.entrant+' versus '+m.opponent+'. Respect subdual, real costs, surrender/referee stops, finite summons and no outside aid. This opening grants no free attack. Unharmed fighters need no invented treatment.');}
}
