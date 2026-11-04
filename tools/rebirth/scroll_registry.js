// Candidate formulas use the same native settlement shape. Scripts select
// eligibility only. The engine, not check(), judges the declared story query.
const catalogue = __CATALOGUE__;
const tick = Number(check({type:'game-tick'})) || 0;
const normalize = text => text.toLowerCase().replace(/[’‘]/g, "'");
const input = normalize(JSON.stringify(check({type:'action-text'}) || ''));
const story = normalize(String(check({type:'story-text'}) || ''));
const research = /stud|scroll|formula|research|decipher|practice|practise|experiment|rehears|understand|test|unroll|read/.test(input)
    || (/try again|continue/.test(input) && /scroll|formula|study|research|diagram|ink|working/.test(story));
const recent = research ? input + ' ' + story : '';
const readerTraits = check({type:'player-traits'}) || {};
const continuation = /try again|continue|rehears|practice|practise|experiment|test/.test(input)
    && /scroll|formula|study|research|diagram|ink|working/.test(story)
    && !input.includes('teaching scroll:');
storage.rbScrollFocus = storage.rbScrollFocus || {};
if (research || catalogue.some(row => storage.rbScrollFocus[row.id] !== undefined)) {
for (const row of catalogue) {
    const quantities = check({type:'player-item', item:row.item});
    const held = quantities && typeof quantities === 'object' && Object.entries(quantities).some(([name,n]) => Number(n) > 0 && !readerTraits[name]?.includes(row.trait));
    const focused = storage.rbScrollFocus[row.id];
    if (held && research && (recent.includes(row.ability.toLowerCase()) || (focused && continuation && tick - focused < 8))) {
        if (!focused && Object.keys(storage.rbScrollFocus).length >= 8) continue;
        storage.rbScrollFocus[row.id] = tick;
        const active = Object.keys(storage.rbScrollFocus).length;
        const semanticCount = Object.values(triggers).filter(t => t.conditions.some(c => c.type === 'story' || c.type === 'action')).length;
        if (!triggers[row.id] && active <= 8 && semanticCount < 475) {
            triggers[row.id] = {
                name:row.id, scope:'player', recurring:true,
                conditions:[
                    {type:'player-item', item:row.item, operator:'greaterThan', value:0},
                    {type:'player-traits', operator:'notContains', value:row.trait},
                    ...(row.space ? [{type:'skill-value', skill:'Gravity Magic', operator:'greaterThanOrEqual', value:25}] : []),
                    {type:'story', query:'This player has just completed successful deliberate study of their genuine held ' + row.item + ', has understood its ' + row.difficulty + ' working and carried out a successful controlled test. ' + (row.difficulty === 'masterwork' ? 'Several substantive research sessions and a safe prepared test are necessary. ' : row.difficulty === 'advanced' ? 'Resolve a real difficulty through focused research before the successful test. ' : 'A focused careful exercise can suffice. ') + 'A plan, a label, an unrelated spell, a failed test, another player learning or a formula already known is false. Confirm the exact reader, this formula and the still-held scroll. Substantial research may compensate for low discipline proficiency; study grants no discipline ranks.'}
                ],
                effects:[
                    {type:'player-traits', operator:'add', value:row.trait, target:'satisfyingPlayers'},
                    {type:'player-abilities', operator:'add', value:row.ability, target:'satisfyingPlayers'},
                    {type:'item-remove', item:row.item, quantity:1, target:'satisfyingPlayers'},
                    {type:'story', instruction:'The successful reader learns ' + row.ability + ' as the ink fades from one copy. These effects already settle learning and consumption. Preserve the other readers and unused copies. Casting is a later action using the real discipline and Mana.'}
                ]
            };
        }
    } else if (!held || !focused || tick - focused >= 8) {
        delete triggers[row.id];
        delete storage.rbScrollFocus[row.id];
    }
}
}
