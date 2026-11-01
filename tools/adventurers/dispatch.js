const jobs = JOBS;
const location = check({type:'party-location'});
const actions = check({type:'action-text'});
const text = (Array.isArray(actions) ? actions : [actions]).join(' ');
const levels = Object.values(check({type:'player-level'}) || {}).filter(x=>typeof x==='number' && x>0);
const minLevel = levels.length ? Math.min(...levels) : 1;
storage.ad34_solo = levels.length === 1;
storage.ad34_offer_target = '';
const propertyWords = /\b(rent|lease|purchase|buy|bought|rented|own|ownership|deed|lodging|room|workshop|house|property|key)\b/i.test(text);
storage.ad34_property_interest = propertyWords;
const candidates = jobs.filter(j => j.location === location &&
  check({type:'quest-status',questId:j.title}) === 'hidden' &&
  check({type:'npc-in-scene',npc:j.source}) === true &&
  minLevel + 2 >= j.level);
const explicit = candidates.find(j=>text.toLowerCase().includes(j.title.toLowerCase()));
const addressed = candidates.find(j=>text.toLowerCase().includes(j.source.toLowerCase()) || text.toLowerCase().includes(j.source.split(' ')[0].toLowerCase()));
const recent = String(check({type:'story-text'}) || '');
const followup = /\b(yes|sure|okay|ok|accept|agree|terms|pay|payment|do that|i will|i'll)\b/i.test(text) &&
  candidates.find(j=>recent.toLowerCase().includes(j.title.toLowerCase()));
if (/\b(job|work|help|request|commission|task|posting|offer|problem|repair)\b/i.test(text) || explicit || followup) {
  const choice = explicit || followup || addressed || (candidates.length === 1 ? candidates[0] : null);
  if (choice) storage.ad34_offer_target = choice.title;
}
// Older Canopy offers share a venue. Expose only the current conversation's job.
const legacy = LEGACY;
storage.ad34_legacy_offer = '';
if (location === 'Asterveil Canopy') {
  const available = legacy.filter(j=>check({type:'npc-in-scene',npc:j.source}) === true &&
    !['accepted','completed'].includes(check({type:'quest-status',questId:j.title})));
  const named = available.find(j=>text.toLowerCase().includes(j.title.toLowerCase())) ||
    available.find(j=>recent.toLowerCase().includes(j.title.toLowerCase()));
  const relevant = available.find(j=>new RegExp(j.words,'i').test(text));
  const chosen = named || relevant || (/\b(job|work|help|request|offer)\b/i.test(text) && available.length ? available[0] : null);
  if (chosen) storage.ad34_legacy_offer = chosen.title;
}
