if(!solo||!here||['ready','live','between','review','away'].includes(c.phase)){skip=true;}else{
 const raw=check({type:'action-text'}),text=(Array.isArray(raw)?raw:[raw]).join(' ').toLowerCase();
 const pool=roster.filter(x=>check({type:'npc-in-party',npc:x.name})!==true&&!(typeof health(x.name)==='number'&&health(x.name)<=0)&&check({type:'npc-in-combat',npc:x.name})!==true);
 const mentioned=pool.filter(x=>text.includes(x.name.toLowerCase())||text.includes(x.name.split(' ')[0].toLowerCase()));
 const recent=String(check({type:'story-text'})||'').toLowerCase();
 const contextual=pool.filter(x=>recent.includes(x.name.toLowerCase())&&check({type:'npc-location',npc:x.name})===venue);
 const choice=mentioned.length===1?mentioned[0]:mentioned.length===0&&contextual.length===1?contextual[0]:null;
 if(!choice){say('Confirm the full identity of the actual willing practice partner before arranging a match. Do not substitute a different fighter merely because they are close in level. Offer a clear introduction or ask which person the player means.');}
 else{c.exhibition=true;c.entrant=names[0];c.roster=['@',choice.name];c.title='Friendly exhibition';c.outcome='practice arranged';c.matches=[{id:'EX'+tick,players:['@',choice.name],arena:rings[tick%rings.length],attempt:1}];c.match=c.matches[0].id;setPhase('ready');mirror();say('The agreed friendly match is arranged with '+choice.name+' at '+current().arena+'. It gives no championship trophy or purse and does not change championship cooldown. Keep it nonlethal; wait for the player to be ready.');}
}
