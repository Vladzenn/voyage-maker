const care=m=>{c.care[c.edition+':'+m.id+':'+m.startedTick]={owner:c.entrant,edition:c.edition};const h=health(m.opponent);if(check({type:'npc-location',npc:m.opponent})===venue&&typeof h==='number'&&typeof m.opponentStartHealth==='number'&&h<m.opponentStartHealth)effects.push({type:'npc-health',npc:m.opponent,operator:'set',value:m.opponentStartHealth});};
const close=(outcome,reason)=>{
 c.phase='closed';c.outcome=outcome;c.closedTick=tick;storage.gh_lore_tournament_active=false;
 if(!c.exhibition){c.nextTick=tick+100;c.history.push({v:2,edition:c.edition,title:c.title,entrant:c.entrant,outcome,reason,closedTick:tick,card:JSON.parse(JSON.stringify(c.card))});c.history=c.history.slice(-8);}
 mirror();
};
const finish=(winner,reason)=>{
 const m=current();if(c.phase!=='live'||!m||typeof m.startedTick!=='number'||m.result)return;
 m.result={winner,reason,tick};care(m);storage.gh_lore_tournament_active=false;
 if(c.exhibition){close(winner==='player'?'exhibition win':winner==='draw'?'exhibition draw':'exhibition loss',reason);say('The friendly bout is stopped and its actual result stands: '+reason+'. Offer appropriate optional care or rest, including after simultaneous falls. No championship prize or title cooldown is created.');return;}
 if(winner!=='player'){close(reason==='voluntary withdrawal'?'withdrawn':'eliminated',reason);say('This championship run is closed: '+reason+'. A simultaneous knockout eliminates both contestants under the announced rules. Offer relevant care immediately; recovery never reverses the result. No trophy is owed. The rest of the tournament continues elsewhere; do not announce a champion who has not actually been established.');return;}
 if(c.index===c.card.length-1){c.prizes[c.edition]={owner:c.entrant,title:c.title,marks:c.purse};close('champion',reason);say(c.entrant+' has won the final of '+c.title+'. The announced '+c.purse+' marks and one championship trophy are owed for actual collection, not already granted. No further final belongs to this edition. Offer optional care, rest or company without inventing injuries.');}
 else{c.index++;c.phase='waiting';mirror();say('The actual bout is won and recorded. Offer appropriate optional care or rest; an unharmed fighter can proceed without treatment and no exact resource percentage is required.');callNext();}
};
const withdraw=reason=>{
 const m=current();if(c.phase==='live'&&m&&typeof m.startedTick==='number'&&!m.result){finish('opponent',reason);return;}
 if(!active())return;close('withdrawn',reason);say('The entry is withdrawn from this edition. No unstarted match is recorded as a combat result and no trophy is owed. Moving between areas within the venue would not withdraw an entry.');
};
