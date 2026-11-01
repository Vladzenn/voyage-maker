if(c.v!==3){
 const wasActive=['ready','waiting','live','between','review','away'].includes(c.phase);
 c.prizes=c.prizes||{};c.care=c.care||{};c.history=Array.isArray(c.history)?c.history:[];c.v=3;
 if(wasActive){c.history.push({edition:c.edition,title:c.title,outcome:'cancelled on bracket revision',closedTick:tick});c.phase='closed';c.outcome='cancelled';c.nextTick=Math.max(c.nextTick||0,tick);c.upgradeNotice=true;}
 else c.phase=c.phase==='idle'?'idle':'closed';
 c.card=[];c.index=0;c.rounds=[];for(const k of ['matches','match','awayTick','champion'])delete c[k];
}
if(c.upgradeNotice&&here){delete c.upgradeNotice;say('An unfinished older championship entry is closed while the officials replace its schedule. Earned uncollected prizes remain owed; no result or new waiting penalty is invented.');}
mirror();
