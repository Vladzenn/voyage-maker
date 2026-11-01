if(!solo||c.entrant!==names[0]){if(['live','ready','between','away'].includes(c.phase)){setPhase('review');say('The registered individual bout is paused because the human-player roster or identity changed. Preserve the entrant and results; do not give another person their place, treatment or prize. Restore the original solo entrant or explicitly withdraw/review the entry.');}}
else if(c.phase==='live'){
 const m=current(),n=opponent(m),p=playerHealth(),h=n?health(n):undefined;
 if(m&&tick>m.startedTick&&check({type:'npc-in-combat',npc:n})===true)m.seenCombat=true;
 const pd=typeof p==='number'&&p<=0,nd=typeof h==='number'&&h<=0;
 if(m&&tick>m.startedTick&&(pd||nd)){
  if(pd&&nd){setPhase('review');say('Both actual competitors are down. The bout is stopped for medical care and referee review, not a player victory. Preserve the actual nonlethal outcome; offer care without continuing attacks.');}
  else finish(pd?n:'@',pd?'actual player incapacity':'actual opponent incapacity');
 }else if(!here){c.awayTick=tick;setPhase('away');}
}else if(['ready','between','review'].includes(c.phase)&&!here){withdraw('withdrawal from the venue');}
else if(c.phase==='away'&&tick>c.awayTick+1){withdraw('departure after the bout was interrupted');}
mirror();

