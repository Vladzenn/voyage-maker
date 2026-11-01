if(c.v!==2){
 const old=JSON.parse(JSON.stringify(c)),wasActive=['ready','live','between','review','away'].includes(old.phase);
 c.v=2;c.card=[];c.index=0;c.history=Array.isArray(old.history)?old.history:[];c.prizes=old.prizes||{};c.care=old.care||{};
 if(wasActive){c.history.push({v:1,edition:old.edition,title:old.title,outcome:'cancelled on controller upgrade',closedTick:tick});c.phase='closed';c.outcome='cancelled';c.nextTick=Math.max(old.nextTick||0,tick);c.upgradeNotice=true;}
 else{c.phase=old.phase==='idle'?'idle':'closed';c.nextTick=old.nextTick||0;}
 for(const k of ['matches','match','awayTick'])delete c[k];
}
if(c.upgradeNotice&&here){delete c.upgradeNotice;say('An unfinished older Crucible entry is closed without an invented result or prize as the officials revise the schedule. Previously earned uncollected prizes remain owed to their actual owners. A new suitable solo entry may be arranged.');}
mirror();
