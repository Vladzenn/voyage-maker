const raw = check({type:'action-text'});
const inputs = Array.isArray(raw) ? raw : [raw];
const seen = [];
for (const input of inputs) {
  // Match only the whole out-of-character command, never a quotation inside prose.
  const match = /^\s*quest done:\s*([^\r\n]+?)\s*$/i.exec(String(input || ''));
  if (!match) continue;
  const title = match[1];
  if (seen.includes(title)) continue;
  seen.push(title);
  const status = check({type:'quest-status',questId:title});
  if (status !== 'accepted') {
    effects.push({type:'story',instruction:'Out of character only: the quest-repair command found no accepted quest with the exact supplied name. Give one short correction note without quoting internal flags. Do not change a quest, item, reward or NPC memory, and continue the current scene.'});
  } else {
    effects.push({type:'quest-complete',questId:title});
    effects.push({type:'story',instruction:'The player used the out-of-character journal repair for '+title+'. Let its normal completion effects settle once. Continue the existing scene; NPCs did not hear a command and no fictional deed, forged evidence or extra payment is retroactively invented.'});
  }
  if (effects.length >= 8) break;
}
if (!effects.length) skip = true;
