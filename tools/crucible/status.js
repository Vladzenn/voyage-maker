const m=current();
say('Give a brief out-of-character Crucible status: '+(c.title||'no entered edition')+'; state '+c.phase+'; outcome '+(c.outcome||'none')+'. '+(m?'Current pairing: '+m.players.map(n=>n==='@'?c.entrant:n).join(' versus ')+'; arena '+m.arena+'. ':'')+'Next championship eligibility in '+Math.max(0,(c.nextTick||0)-tick)+' completed turns. Uncollected prizes: '+Object.keys(c.prizes).length+'. Explain naturally; no script/storage jargon in NPC speech. Do not alter the result or award anything.');

