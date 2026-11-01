if(!solo||c.entrant!==names[0]||!['live','away'].includes(c.phase)){skip=true;}
else{
 const m=current(),n=opponent(m),p=playerHealth(),h=n?health(n):undefined;
 if(!m||m.resultTick!==undefined){skip=true;}
 else if(typeof p==='number'&&p<=0&&typeof h==='number'&&h<=0){setPhase('review');say('The simultaneous fall requires a no-contest/referee review. Do not award victory or continue the fight.');}
 else if(typeof p==='number'&&p<=0){finish(n,'actual player incapacity');}
 else{finish(RESULT_WINNER==='player'?'@':n,RESULT_REASON);}
 mirror();
}

