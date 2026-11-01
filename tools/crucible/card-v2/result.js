if(!solo||c.entrant!==names[0]||c.phase!=='live'||(RESULT_WINNER==='player'&&!here)){skip=true;}
else{
 const m=current(),p=playerHealth(),h=m?health(m.opponent):undefined;
 if(!m||typeof m.startedTick!=='number'||m.result){skip=true;}
 else if(typeof p==='number'&&p<=0&&typeof h==='number'&&h<=0)finish('draw','simultaneous knockout');
 else if(typeof p==='number'&&p<=0)finish('opponent','actual player incapacity');
 else if(RESULT_WINNER==='opponent')finish('opponent',RESULT_REASON);
 else if(typeof h==='number'&&h<=0)finish('player','actual opponent incapacity');
 else if(RESULT_WINNER==='player'&&check({type:'party-area'})!==m.arena){skip=true;}
 else finish(RESULT_WINNER,RESULT_REASON);
 mirror();
}
