if(!solo||c.entrant!==names[0]||!here||c.phase!=='review'){skip=true;}else{
 const m=current(),n=opponent(m),p=playerHealth(),h=n?health(n):undefined;
 if(typeof p==='number'&&p<=0&&!(typeof h==='number'&&h<=0)){finish(n,'confirmed incapacity on review');}
 else if(typeof h==='number'&&h<=0&&!(typeof p==='number'&&p<=0)){finish('@','confirmed opponent incapacity on review');}
 else if(m&&m.resultTick===undefined&&(typeof h!=='number'||h>0)&&(typeof p!=='number'||p>0)){
  m.attempts=m.attempts||[];m.attempts.push({attempt:m.attempt||1,reason:'no-contest after inconclusive stoppage',tick});m.attempt=(m.attempt||1)+1;
  if(m.attempt>2){withdraw('edition withdrawn after an unresolved repeat stoppage');say('The official closes the unresolved title entry instead of generating endless replays. No championship prize is awarded.');}
  else{setPhase('between');say('The official records the interrupted attempt as a no-contest and offers one replay after appropriate care. The existing bracket and arena remain; no result or prize is invented. Wait for readiness.');}
 }else{say('The bout remains stopped for actual medical care. Once the fighters are fit, request a review or withdraw. Do not force a wounded actor into a rematch or declare an automatic champion.');}
 mirror();
}

