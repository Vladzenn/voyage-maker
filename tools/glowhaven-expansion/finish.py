"""Local ecology, two openings and one bounded offstage roaming event."""
import copy

LORE={
 'Glowhaven — City and Country':'Glowhaven’s territory includes a great walled city, settled countryside, western wooded hills and eastern coastal waters. The city’s visible districts are neighboring parts of one community, not separate countries. The Evertree district holds the court and the single public inter-realm portal hub at Evertree Base. Brookmeadow remains a farming village in the southeastern countryside. The western caravan stop and Pinewater routes serve local travel. Field expeditions beyond Glowhaven go outside this whole territory, not merely across a district boundary.',
 'Whitecrest — Boats and Passage':'Small local boats connect usable landings when weather, tide and the vessel permit. A traveler can arrange a crossing, hire a boat with its operator or buy a suitable small craft. Destination, fare, ownership and a safe return are agreed before departure. Boats do not appear for free merely because someone reaches water. Long or dangerous trips need a seaworthy arrangement and actual preparation. The Gilded Albatross takes independent salvage and agreed voyages; its captain and crew keep their own duties. A charter does not recruit the whole crew into a permanent adventuring party.',
 'The Albatross Company':'Reina Kazehara’s independent company lives from agreed voyages, salvage and exploration work. Mio Tatsunami serves as first mate; Daigo Umetsu keeps the deck work sound; Nanae Kogure feeds the household aboard; Sōji Hamada weighs its obligations; Iris Mornay handles difficult underwater work. Their talents and disagreements do not disappear when a passenger boards. Cargo has real owners, a discovery can create a disputed claim, and a profitable trip can still cost a friendship. Negotiated shares concern the company; a posted player reward is the full agreed payment.',
 'Avelune and Starlark Abbey':'Starlark Abbey is devoted to Avelune, Lady of Returning Light. Her worshippers tend lamps at departures and returns, honor people who guide others home, and keep a lamp burning for an absent household member. The star above a small lantern is a familiar local devotional image. Chizuru Hoshikawa leads the abbey’s household, which maintains a chapel, hospice, kitchen garden and guest wing. Belief, charity and institutional pride can disagree in ordinary life. Hospitality does not compel conversion; neither a cure nor an unanswered prayer settles every religious claim. The abbey is one faith among Glowhaven’s many, not the state’s compulsory church.',
 'Stillback — The Patient Island':'Mauruun is an immense, usually peaceful animal whose shell resembles part of Stillback’s shore. It rests, grazes and protects a sheltered shelf without seeking fights with ordinary visitors. Observation, careful relief of an injury and adjusting human traffic can accomplish more than a weapon. Its shell is living anatomy; naturally loose material differs from cutting a plate off. It is powerful enough to punish an attack, not an automatically hostile obstacle or a prize mount.',
 'Bluecoil — A Sleeping Danger':'Nerathyl usually sleeps at the inner ledge of Bluecoil Rest. The outer mooring offers a place to watch its breathing and the movement of its coils. It is an animal-like sea serpent, not a dragon in disguise or a guardian offering an examination. Noise, pain and close interference can wake it. Its fixed resting place is distinct from Ghorvath’s roaming deepwater approaches; one creature’s signs do not announce the other.',
 'Ghorvath — Eastern Deepwater':'The great kraken Ghorvath uses a few deep approaches around the eastern wrecks and shoals. Broad suckered marks, displaced debris and an unnatural rolling swell are reasons to observe or leave, not a requirement that every fishing trip becomes a boss fight. It is a persistent individual, not an endlessly replaced population. Prepared hunters can deliberately seek it; sheltered beginner crossings do not sail into its reach without warning.',
 'Glowhaven — Rural Work and Quiet Places':'The country has working mills, fields, guest houses, woodlots, a river estuary and old infrastructure still useful to ordinary people. Some work is simply repairing a shutter, finding a missing tool or getting a cart past an animal. Other investigations uncover a real disagreement or an unfamiliar creature. Quiet overlooks can remain quiet. A place does not need a resident quest giver, secret shrine or large monster to justify existing.',
 'Glowhaven — Coastwise Exploration':'Fisheries, lighthouse supplies, reef gathering, wreck surveys and salvage support very different kinds of work. Close landings and settled paths are suitable for modest experience; the outer wrecks, exposed nests and deepwater channels show greater danger before a traveler commits. Sea travel rewards navigation, rope work, observation, craft, ordinary medicine and martial protection as well as magic. Swimming, breathing and a way back remain practical requirements. Healing magic, a coat or a flattering tale does not make a person able to breathe underwater.'
}

HABITATS={
 'Wrenhill Windmill':('Flour Beetle, Sailcloth Moth','A bounded store or machinery problem can occur during actual inspection; stop the machinery before handling a jam. Routine business and the siblings’ own work continue.'),
 'Greenrush Estuary':('Tideglass Shrimp, Reedlace Sprite, Tangletooth Otter, Brinecap Slime','Shallow-land jobs favor levels 2–8, a single active hostile initially, clear warning and practical alternatives. Deeper optional work can reach 12–18 after actual preparation. Do not turn passive wildlife into attacking packs.'),
 'Gullwatch Reefs':('Hookbeak Gull, Kelpclaw Crab, Shoalglass Ray, Salt-Crest Wyvern','The sheltered pools support levels 3–8 and noncombat collection. Exposed high nests are a separate deliberately approached level 24–30 hazard. Mark that difference through tracks, circling and local advice before danger.'),
 'Splinterwake Wreck':('Barnacle Brute, Undertow Eel, Mooring Mimic','Use finite groups of one to three fitting creatures, with room to observe or retreat. The level-55 authored kraken is a separate optional deepwater danger; never replace it with a fresh generated duplicate. Check actual Ghorvath placement and state before involving it.'),
 'Moonarch Isle':('Inkpot Cuttlefish, Shoalglass Ray, Undertow Eel','The arch is a ruin, not an automatic portal. Low water, stable footing and recorded marks make useful investigation. Sheltered landing encounters can be modest; the flooded undercroft needs preparation.'),
 'Stillback Isle':('Tideglass Shrimp, Inkpot Cuttlefish, Hookbeak Gull','Mauruun is the unique resident, not a generated hostile turtle. Quiet arrival does not provoke it. Any finite small wildlife problem must leave its passive baseline intact.'),
 'Bluecoil Rest':('Kelpclaw Crab, Tideglass Shrimp','Nerathyl is the unique fixed sleeping serpent. Begin with its established current condition; never reset it after actual events. Show its formidable level-45 danger before a close approach. No free surprise strike or automatic awakening from observation at the distant mooring.'),
 'The Gilded Albatross':('Sailcloth Moth, Mooring Mimic','Aboard is a working household. Pests or salvage complications occur through real causes and can be addressed without spawning a fight every visit. Crew are not automatically recruited.'),
 'Old Southwatch':('Burdock Lurker, Chalkback Ram','The keeper and the ruin have ordinary uses. Any finite wildlife issue belongs to the surrounding path, not an obligatory ambush in his home.'),
 'Thistlebank Alchemy Cottage':('Sailcloth Moth, Burdock Lurker','The garden and workroom support small experiments, trade and household life. Do not add another dangerous unstable-potion conspiracy merely because an alchemist is present.')
}

def add(w):
    w['factions']['The Albatross Company']={'name':'The Albatross Company','factionType':'minor','initialKnown':False,'basicInfo':'An independent sailing and salvage company led by Reina Kazehara aboard the Gilded Albatross. The crew takes agreed voyages, recovery work and exploration while guarding its freedom to refuse a patron.','hiddenInfo':'Reina’s personal repair guarantee makes attractive work tempting. Sōji wants defensible ownership and a sound balance; Nanae will not solve a budget problem by feeding bad stores to the crew. Their disagreements require specific events, not automatic loyalty or betrayal.'}
    w['factions']['Starlark Abbey']={'name':'Starlark Abbey','factionType':'minor','initialKnown':False,'basicInfo':'A religious household devoted to Avelune, Lady of Returning Light. Its chapel, hospice, garden and guest rooms serve worshippers and travelers in the southern countryside.','hiddenInfo':'Chizuru protects the institution’s dignity; Lucette prioritizes actual patients; Tamae wants the household to run; Eiji is still finding his place. They can disagree without secretly being an evil cult.'}
    for k,v in LORE.items():w['worldLore'][k]={'text':v}
    for place,(types,notes) in HABITATS.items():
        loc=w['locations'][place]
        loc['hiddenInfo']='Local opportunities and ecology: '+types+'. '+notes+' Use the actual scene, relevant NPC types and the party’s real experience. These are possible situations, not an instruction to generate all of them at arrival. Authored people and the three named creatures retain their own power. Travel encounters remain separate from exploration within the location.'
    # One offstage schedule, no per-location spawn triggers or duplicate monster NPCs.
    w['triggerDefinitions']['ghx_kraken_roam']={'name':'ghx_kraken_roam','conditions':[{'type':'game-tick','operator':'greaterThan','value':0}],'effects':[],'recurring':True,'phase':'planning','script':"const npc='Ghorvath',tick=Number(check({type:'game-tick'}))||0,h=check({type:'npc-health',npc});if((typeof h==='number'&&h<=0)||check({type:'quest-status',questId:'Guild: Ghorvath at the Deepwater Edge'})==='completed')storage.ghxKrakenDefeated=true;if(storage.ghxKrakenDefeated||check({type:'npc-in-scene',npc})===true||check({type:'npc-in-combat',npc})===true||check({type:'npc-in-party',npc})===true){skip=true;}else{const slot=Math.floor(tick/24),route=[['Splinterwake Wreck','Splinterwake Wreck - Deepwater Edge'],['Moonarch Isle','Moonarch Isle - Offshore Drop']];if(storage.ghxKrakenSlot===slot){skip=true;}else{const [location,area]=route[slot%route.length];effects.push({type:'npc-placement',npc,operation:'moveTo',location,area});storage.ghxKrakenSlot=slot;}}"}
    w['locations']['Moonarch Isle']['areas']['Moonarch Isle - Offshore Drop']={'description':'Beyond the sheltered landing, the bottom drops into dark water. Heavy swell and broad marks on driftwood warn of deepwater animals.','paths':['Moonarch Isle - Pebble Landing']}
    w['locations']['Moonarch Isle']['areas']['Moonarch Isle - Pebble Landing']['paths'].append('Moonarch Isle - Offshore Drop')
    # Keep the creature away from beginner landings: the outer anchorage is a warned approach to the wreck.
    starts={
     '⛵ Aboard the Gilded Albatross':{'name':'⛵ Aboard the Gilded Albatross','description':'Begin aboard the Gilded Albatross off Glowhaven’s eastern coast. A butterfly-winged captain, an eager dragonkin first mate and a crew with unfinished business offer a foothold in coastal adventure.','locations':['The Gilded Albatross'],'locationAreas':['The Gilded Albatross - Main Deck'],'startingQuests':[],'startingItems':[{'item':'Mark','quantity':1000}],'startingPartyNPCs':[],'isDefault':False,'questGenerationGuidance':'Keep the ship a working household. The actual background can make the player a visitor, passenger or agreed worker; do not impose employment, payment, membership or permanent recruitment. A local voyage, salvage lead or shore visit can be discussed, not automatically accepted. Lower-experience characters receive a suitable modest role; the kraken and serpent are warned optional dangers.','storyStart':'''[Opening aboard the anchored Gilded Albatross. Reina Kazehara and Mio Tatsunami are working near the main deck; use their actual records. The player’s real background determines their reason for being aboard. Do not grant a free ship, crew, key, job or paid fare. Stop before the player answers or agrees to sail.]

A line snaps taut above the deck, and a bright voice announces that the knot is definitely right this time.

Daigo Umetsu inspects it in silence. Mio Tatsunami tries not to look as though the silence has become a personal challenge. A few teal scales catch the light along her wrist.

“It’s the knot you showed me.”

“It is,” Daigo says. “On the wrong line.”

Reina Kazehara laughs from the quarterdeck, great butterfly wings bright behind her navy coat. “Excellent! Half the mystery solved. Find the other half before it takes the awning with it.”

From the galley comes Nanae’s opinion of anyone who expects lunch to survive another wet sack. Reina calls back that lunch is a sacred obligation, then steps down to examine the chart spread beside the rail. One route follows the sheltered landings. Another turns toward a wreck marked with a heavy warning.

“We’re taking work ashore before we commit to another recovery,” she tells Mio. “Ask what we can carry before you promise what we can find.”

Mio opens her mouth, sees Daigo looking at the line, and goes back to the knot.

The captain notices the visitor without calling the deck to attention. “Come clear of the rigging. If you’re looking for passage, work, or simply the way back to shore, we can discuss it. Which is it?”'''},
     '🕯️ Starlark Abbey: A Light for the Road':{'name':'🕯️ Starlark Abbey: A Light for the Road','description':'Begin at Starlark Abbey in Glowhaven’s southern countryside. Lamps, travelers, an overworked hospice and a household with different ideas about service offer a quieter beginning.','locations':['Starlark Abbey'],'locationAreas':['Starlark Abbey - Pilgrim Court'],'startingQuests':[],'startingItems':[{'item':'Mark','quantity':1000}],'startingPartyNPCs':[],'isDefault':False,'questGenerationGuidance':'Use the player’s chosen local, visiting, religious or secular background. The abbey worships Avelune but does not force conversion or invent divine favor. A room, help with ordinary work, care or onward travel can be discussed; ownership and jobs need actual agreement. No compulsory confession, trauma, injury or hidden cult.','storyStart':'''[Opening at Starlark Abbey’s Pilgrim Court. Tamae Shibano is arranging arrivals; Eiji Kuramochi tends the garden, while Chizuru Hoshikawa and Lucette Bellanger have their own household disagreement. Preserve the actual player background and stop before their reply.]

A little brass lantern hangs beneath the abbey’s star, its flame sheltered from the wind off the river. Eiji Kuramochi is carrying a tray of seedlings through the court with the concentration of someone who has already dropped one.

“The chapel lamps need tending,” Chizuru Hoshikawa says from the doorway.

Lucette Bellanger appears beside her with a basin and a folded towel. “And the west bed needs clean water. I have three patients who will appreciate it more than the lamps.”

“They can both be done.”

“Good. Which are you doing?”

Eiji looks urgently at the seedlings. Tamae Shibano takes the tray before he can attempt to solve the disagreement by carrying four things at once.

“One errand at a time. And nobody sends the guest-wing key to the kitchen again.”

Chizuru lifts the water jar herself. Lucette’s expression softens by a fraction, and both women continue their argument toward the hospice.

Beyond the gate, the country road follows the river toward fields and the distant city. A bell moves once in the wind. Tamae checks a small row of numbered keys and looks toward the new arrival.

“A bed, a visit, or someone you came to see? We can usually manage one. If it’s all three, tell me before I finish arranging the rooms.”'''}
    }
    # Insert these before the flexible Random start and preserve every existing ID.
    out={}
    for k,v in w['storyStarts'].items():
        if 'Random' in k:out.update(starts)
        out[k]=v
    if not all(k in out for k in starts):out.update(starts)
    w['storyStarts']=out
    return {'newStarts':list(starts),'loreEntries':list(LORE),'roamingTriggers':['ghx_kraken_roam']}
