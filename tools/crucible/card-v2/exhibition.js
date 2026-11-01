if(!solo||!here||active()){skip=true;}else{
 const raw=[].concat(check({type:'action-text'})||[]).join(' ').toLowerCase(),recent=String(check({type:'story-text'})||'').toLowerCase();
 const pool=roster.filter(available),mentioned=pool.filter(x=>raw.includes(x.name.toLowerCase())||raw.includes(x.name.split(' ')[0].toLowerCase())),contextual=pool.filter(x=>recent.includes(x.name.toLowerCase()));
 const choice=mentioned.length===1?mentioned[0]:!mentioned.length&&contextual.length===1?contextual[0]:null;
 if(!choice){say('Identify the actual willing practice partner before arranging the friendly bout. Do not replace an ambiguous partner with an unrelated fighter.');}
 else{c.exhibition=true;c.entrant=names[0];c.title='Friendly exhibition';c.outcome='practice arranged';c.index=0;c.used=[choice.name];c.roster=[choice.name];c.card=[{id:'EX'+tick,opponent:choice.name,level:choice.level,arena:rings[tick%rings.length],label:'Friendly exhibition'}];c.phase='waiting';mirror();say('A consensual nonlethal exhibition is arranged. It gives no championship purse or trophy and does not alter the title cooldown.');callNext();}
}
