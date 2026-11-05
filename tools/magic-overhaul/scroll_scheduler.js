// Selection is lexical/contextual; successful learning is judged only by the
// single declared player-scoped semantic condition, never by this script.
const rows = storage.mxScrollCatalogue;
if (!Array.isArray(rows)) { skip = true; }
else {
    const tick = Number(check({type:'game-tick'})) || 0;
    const norm = s => String(s || '').normalize('NFKC').toLowerCase().replace(/[’‘]/g, "'");
    const input = norm(JSON.stringify(check({type:'action-text'}) || []));
    const story = norm(check({type:'story-text'}));
    const traits = check({type:'player-traits'}) || {};
    const studying = /scroll|formula|stud|read|decipher|research|unroll|pore|rehears|experiment|practi[cs]|try again|continu|test|diagram|working/.test(input);
    const held = rows.filter(row => {
        const quantities = check({type:'player-item',item:'Teaching Scroll: '+row[0]}) || {};
        return Object.entries(quantities).some(([p,n]) => Number(n)>0 && !(traits[p] || []).includes('Formula: '+row[0]));
    });
    let queue = Array.isArray(storage.mxScrollQueue) ? storage.mxScrollQueue : [];
    queue = queue.filter(q => tick-q.touched<=8 && held.some(r=>r[0]===q.name));
    const mention = row => input.includes(norm(row[0])) || (studying && story.includes(norm(row[0])));
    for (const row of held) {
        if (!mention(row) && !(studying && held.length===1) && !(studying && queue.length===1 && queue[0].name===row[0])) continue;
        let q = queue.find(q=>q.name===row[0]);
        if (q) q.touched=tick;
        else queue.push({name:row[0],touched:tick,served:-1});
    }
    storage.mxScrollQueue = queue;
    if (!queue.length) storage.mxScrollReady = false;
    else {
        // Round-robin formulas, not arbitrary player IDs. Everyone learning the
        // selected formula is independently filtered by native scope/ownership.
        queue.sort((a,b)=>a.served-b.served || a.touched-b.touched);
        const q=queue[0], row=rows.find(r=>r[0]===q.name);
        const item='Teaching Scroll: '+row[0], formula='Formula: '+row[0];
        const difficulty=row[1]==='m'
            ? 'Several substantive research sessions, correction and a successful safe final test are required.'
            : row[1]==='a'
            ? 'Identify and solve a genuine difficulty, understand the formula and complete a successful controlled test.'
            : 'A genuinely focused exercise and successful controlled test can suffice.';
        const query='This player actually completed deliberate first-time study of their own held '+item+'. '+difficulty+' Verify the exact reader and formula from actual recent play, including a completed study awaiting this queued verification within the last eight turns. Mere possession, shopping, quotation, intent, opening a label, unread copying, a failed test, another person learning or an already known formula is false. Substantial research may compensate for low school proficiency; it grants no ranks. The reader still holds an unused copy.';
        const conditions=[
            {type:'read-boolean',key:'mxScrollReady',operator:'equals',value:true},
            {type:'player-item',item,operator:'greaterThan',value:0},
            {type:'player-traits',operator:'notContains',value:formula},
            ...(row[2] ? [{type:'skill-value',skill:'Gravity Magic',operator:'greaterThanOrEqual',value:25}] : []),
            {type:'story',query}
        ];
        const effects=[
            {type:'player-traits',operator:'add',value:formula,target:'satisfyingPlayers'},
            {type:'player-abilities',operator:'add',value:row[0],target:'satisfyingPlayers'},
            {type:'item-remove',item,quantity:1,target:'satisfyingPlayers'},
            {type:'story',instruction:'The successful reader learns '+row[0]+' as one scroll fades. Learning and consumption are already supplied once. Preserve other readers and unused duplicates; no ability point, rank, affinity, Mana or automatic cast is granted.'}
        ];
        const script='const tick=Number(check({type:"game-tick"}))||0; storage.mxScrollVerified=storage.mxScrollVerified||{}; storage.mxScrollVerified['+JSON.stringify(row[0])+']=tick;';
        triggers.mx_scroll_learn={name:'mx_scroll_learn',scope:'player',recurring:true,phase:'state',conditions,effects,script};
        storage.mxScrollReady=true;
        q.served=tick;
    }
}
