if(!solo||c.entrant!==names[0]||!here||c.phase!=='waiting'){skip=true;}
else{
 const m=current(),p=playerHealth();
 if(!m||m.result||typeof m.startedTick==='number'){close('cancelled','invalid schedule');say('The officials close an inconsistent schedule without inventing a fight or trophy.');}
 else if(typeof p!=='number'||p<=0){say('The entrant cannot begin while actually incapacitated or their condition is unconfirmed. Offer appropriate assessment/care; retain the entry and wait. Full Health, Mana or Stamina is not required.');}
 else if(!available({name:m.opponent})){
  const pool=roster.filter(x=>available(x)&&!(c.used||[]).includes(x.name)&&x.level<=(c.entryLevel||levels[c.entrant])+(c.gap||4));
  pool.sort((a,b)=>Math.abs(a.level-(c.entryLevel||levels[c.entrant]))-Math.abs(b.level-(c.entryLevel||levels[c.entrant])));pool.length=Math.min(pool.length,7);
  if(!pool.length){close('cancelled','no available substitute');say('The remaining scheduled bout cannot be held safely and no suitable unused substitute is available. This edition is cancelled without an unearned win or trophy; keep previously earned prizes. Offer ordinary company and a later championship.');}
  else{const old=m.opponent,replacement=pool[Math.floor(rnd()*pool.length)];m.replacements=m.replacements||[];m.replacements.push({opponent:old,tick,reason:'unavailable before opening'});m.opponent=replacement.name;m.level=replacement.level;c.used.push(replacement.name);c.roster=c.card.map(x=>x.opponent);say(old+' is unavailable before the opening. Announce '+replacement.name+' as the substitute, explain their actual level/style and wait for fresh readiness. No match has started and no win is recorded.');callNext();}
 }
 else{m.startedTick=tick;m.startHealth=p;m.opponentStartHealth=health(m.opponent);c.phase='live';storage.gh_lore_tournament_active=true;mirror();effects.push({type:'party-area',operator:'set',value:m.arena},{type:'npc-placement',npc:m.opponent,operation:'moveTo',location:venue,area:m.arena},{type:'known-entity',entity:m.opponent,operator:'set',value:true});say('The official now opens only '+m.label+': '+c.entrant+' versus '+m.opponent+' at '+m.arena+'. This is actual nonlethal subdual, not an invitation or a free opening attack. Respect the exact participants, finite legal summons, real costs, surrender, ring boundaries and referee stops. Outside companions do not attack/heal/buff. Double knockout eliminates both from this title run. Preserve actual resources; optional care is never a full-bar gate.');}
}
