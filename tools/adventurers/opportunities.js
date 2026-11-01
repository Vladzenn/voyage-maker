const entries = OPPORTUNITIES;
const tick = Number(check({type:'game-tick'}));
const location = check({type:'party-location'});
const sceneCombat = check({type:'npc-in-combat',npc:'anySceneNPC'});
const fighting = sceneCombat === true || (sceneCombat && typeof sceneCombat === 'object' && Object.values(sceneCombat).some(Boolean));
const actions = check({type:'action-text'});
const input = (Array.isArray(actions) ? actions : [actions]).join(' ');
const arrival = storage.ad34_last_place !== location;
storage.ad34_last_place = location;
// Nothing here asks the AI a question. Cooldown and cleared-job filters run in JS.
if (fighting || tick < 3 || tick - Number(storage.ad34_last_public_tick ?? -100) < 9 ||
    /quest done:|\b(attack|cast|fight|sleep|rest|kiss|rent|buy|purchase|leave|portal|return home)\b/i.test(input) ||
    !(arrival || /\b(look around|news|rumou?r|listen|notice|explore|anything happening|what.*do here)\b/i.test(input))) {
  skip = true;
} else {
  const levels = Object.values(check({type:'player-level'}) || {}).filter(x=>typeof x==='number' && x>0);
  const level = levels.length ? Math.min(...levels) : 1;
  const choices = entries.filter(e => e.location === location && !storage['ad34_public_'+e.id] &&
    level >= (e.level || 1) && (!e.quest || check({type:'quest-status',questId:e.quest}) === 'hidden'));
  if (!choices.length) skip = true;
  else {
    const e = choices[Number(storage.ad34_public_cursor || 0) % choices.length];
    effects.push({type:'story',instruction:e.text+' Present one brief public circumstance at this actual location only if the scene has room. No acceptance, journal entry, revealed private motive or completed job follows from overhearing it. If the player ignores it, continue their chosen activity.'});
    storage['ad34_public_'+e.id] = true;
    storage.ad34_public_cursor = Number(storage.ad34_public_cursor || 0) + 1;
    storage.ad34_last_public_tick = tick;
  }
}
