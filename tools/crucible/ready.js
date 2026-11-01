if(!solo||c.entrant!==names[0]||!here||!['ready','between'].includes(c.phase)){skip=true;}
else{
 const m=current(),n=opponent(m);
 if(!m||!n||m.resultTick!==undefined){setPhase('review');say('The official pauses to reconcile the current bout order. Do not invent another final.');}
 else if(typeof health(n)==='number'&&health(n)<=0){setPhase('review');say(n+' is not fit to begin this bout. An official must resolve the absence or schedule a no-contest; do not revive or count an unstarted match as a player victory.');}
 else{
  m.startedTick=tick;m.startHealth=playerHealth();m.opponentStartHealth=health(n);m.seenCombat=false;c.awayTick=null;setPhase('live');storage.gh_lore_tournament_active=true;
  effects.push({type:'party-area',operator:'set',value:m.arena});
  effects.push({type:'npc-placement',npc:n,operation:'moveTo',location:venue,area:m.arena});
  effects.push({type:'known-entity',entity:n,operator:'set',value:true});
  const stage=c.exhibition?'friendly exhibition':Number(m.id.match(/^R(\d+)/)[1])===Math.log2(c.roster.length)?'final':Number(m.id.match(/^R(\d+)/)[1])===Math.log2(c.roster.length)-1?'semifinal':'quarterfinal';
  say('The official starts the current '+stage+' only: '+c.entrant+' against '+n+' at '+m.arena+'. This is actual regulated nonlethal subdual, not an invitation or a lethal duel. Resolve real combat attempts with the actual actors. Finite learned summons are legal within actual costs/action limits; outside companions stay out. No automatic opening hit. Stop on actual incapacity, surrender or an official ruling. The player may have skipped treatment deliberately; preserve actual resources without inventing wounds or silently filling bars.');mirror();
 }
}

