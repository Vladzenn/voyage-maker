// Hints select catches; only the declared semantic condition establishes that
// suitable, reachable, fish-bearing water actually exists in the current scene.
const area=String(check({type:'party-area'})||''),location=String(check({type:'party-location'})||'');
const realm=String(check({type:'party-realm'})||''),region=String(check({type:'party-region'})||'');
const realmCode=(__REALMS__)[realm]||'*';
function waterType(text){
 if(/estuar|brackish|river mouth|tidal marsh/i.test(text))return 'e';
 if(/offshore|deepwater|open sea|open ocean/i.test(text))return 'd';
 if(/river|brook|stream|freshwater|lake|tarn|pond|creek|canal|snowmelt/i.test(text))return 'r';
 if(/harbou?r/i.test(text))return 'h';
 if(/\bsea\b|ocean|saltwater|coast|beach|reef|cove/i.test(text))return 's';
 return '';
}
const hints=__HINTS__;
const habitat=hints[area]||waterType(area+' '+location)||waterType(String(check({type:'action-text'})||''))||waterType(region)||(['d','a','k'].includes(realmCode)?'r':'u');
const zone=habitat==='r'||(habitat==='u'&&!/Harbor|Coast|Isles|Shoals|Reach|Bluffs|Marshes/.test(region))?'inland':'coast';
const weather=realm==='Glowhaven'?(storage.fshWeather?.[zone]?.kind||(zone==='inland'?'clear':'overcast')):'neutral';
