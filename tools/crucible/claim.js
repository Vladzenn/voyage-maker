if(!here||!solo){skip=true;}else{
 const id=Object.keys(c.prizes).filter(k=>c.prizes[k].owner===names[0]).sort((a,b)=>Number(a)-Number(b))[0],prize=c.prizes[id];
 if(!prize){skip=true;}else{
  effects.push({type:'item-add',item:'Mark',quantity:prize.marks,target:'satisfyingPlayers'});
  effects.push({type:'item-add',item:'Crucible Championship Trophy',quantity:1,target:'satisfyingPlayers'});
  c.lastPrizeDispatch={edition:Number(id),tick,marks:prize.marks,owner:prize.owner};delete c.prizes[id];mirror();
  say('Complete the real prize handover for '+prize.title+': the typed effects award '+prize.marks+' marks and one Crucible Championship Trophy. Do not generate a second payment or substitute trophy. This does not reopen the final, enroll companions or automatically cross a portal.');
 }
}

