if(active()){
 if(!solo||c.entrant!==names[0]){skip=true;}
 else if(c.phase==='live'){
  const m=current();if(!m||typeof m.startedTick!=='number'){close('cancelled','missing actual start');say('An inconsistent unstarted bout is closed without a victory or trophy.');}
  else if(!inRing(m)){m.requiresRuling=true;}
  else if(!m.requiresRuling&&!m.result&&tick>m.startedTick){const p=playerHealth(),h=health(m.opponent),pd=typeof p==='number'&&p<=0,nd=typeof h==='number'&&h<=0;if(pd&&nd)finish('draw','simultaneous knockout');else if(pd)finish('opponent','actual player incapacity in the ring');else if(nd)finish('player','actual opponent incapacity in the ring');}
 }
}
mirror();
