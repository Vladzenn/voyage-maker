// The build replaces ROUTES with exact supported location/area pairs.
const routes = ROUTES;
const dayRaw = Number(check({type:'day'}));
const day = Number.isFinite(dayRaw) && dayRaw >= 1 ? Math.floor(dayRaw) : 1;
const time = String(check({type:'time-of-day'}) || '').toLowerCase();
const late = /afternoon|evening|night|dusk/.test(time);
for (const [npc, stops] of Object.entries(routes)) {
  const hp = check({type:'npc-health',npc});
  if (typeof hp !== 'number' || hp <= 0 || storage['ad34_hold_'+npc] === true ||
      check({type:'npc-in-party',npc}) === true ||
      check({type:'npc-in-combat',npc}) === true ||
      check({type:'npc-in-scene',npc}) === true) continue;
  const index = ((day - 1) * 2 + (late ? 1 : 0)) % stops.length;
  const [location,area] = stops[index];
  if (check({type:'npc-location',npc}) === location && check({type:'npc-area',npc}) === area) continue;
  // At most one move per traveler in a phase; never a player teleport or a new NPC.
  effects.push({type:'npc-placement',npc,operation:'moveTo',location,area});
}
