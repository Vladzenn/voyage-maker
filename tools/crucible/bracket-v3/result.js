if(!solo||c.entrant!==names[0]||c.phase!=='live'){skip=true;}
else{
 const m=current();if(!m||typeof m.startedTick!=='number'||m.result){skip=true;}
 else{
  const p=playerHealth(),h=health(m.opponent),native=inRing(m)&&!m.requiresRuling;
  if(RESULT_WINNER==='draw')finish('draw',RESULT_REASON);
  else if(native&&typeof p==='number'&&p<=0&&typeof h==='number'&&h<=0)finish('draw','simultaneous knockout');
  else if(native&&typeof p==='number'&&p<=0)finish('opponent','actual player incapacity in the ring');
  else finish(RESULT_WINNER,RESULT_REASON);
 }
 mirror();
}
