"""Authored locations, finite illegal work and focused lore for this update."""
VENUE='The Eternal Crucible'
RINGS=[VENUE+' - Arena Floor',VENUE+' - Pillar Court',VENUE+' - Verdant Ring',VENUE+' - Frostglass Platform',VENUE+' - Broken Stair Arena',VENUE+' - Mirrorwater Garden']
AREAS={
 'Competitor Lounge':'Wide benches, battered game boards and a tea counter overlook a narrow practice court. Competitors talk, eat, rehearse, ask advice and occasionally avoid one another. A posted bracket gives the current order without requiring everyone to gather around it.',
 'Infirmary':'Clean screened treatment bays open around a warm rest room. Medics offer care appropriate to the patient: an unharmed fighter may need only water or a quiet seat. Nobody needs to pretend to be injured to rest here.',
 'Practice Gallery':'A roofed practice strip holds training dummies, equipment racks and a marked sparring ring. Willing partners can arrange a friendly match when work and health permit; instruction requires actual willingness and time.',
 'Pillar Court':'Staggered broad stone pillars interrupt long firing lanes. The paths between them are wide enough for a controlled retreat. Chipped cover remains chipped during the bout; a later announced reset prepares another match.',
 'Verdant Ring':'Waist-high planted banks divide two shallow channels crossed by broad dry paths. Vegetation gives real concealment and can be cut or disturbed. The floor has no hidden lethal pits.',
 'Frostglass Platform':'A low central ice platform is surrounded by broad padded side decks and marked stopping lines. Footing, approach angles and controlled displacement matter; leaving its raised center alone is not a ring-out.',
 'Broken Stair Arena':'Three low stone elevations connect through wide shallow steps and open ramps. Elevation gives a useful angle without becoming a lethal fall. The outer marked line defines the competition boundary.',
 'Mirrorwater Garden':'Shallow water reflects the canopy above a scattering of broad dry stepping platforms. Channels and reflections complicate movement and aim. Water conducts only according to the actual resolved effect, not an automatic room-wide shock.',
}

CRIMES=[
 ('A Seal Nobody Checked','Mika Koshimizu','Four Sages Bazaar',12,90,
  'Mika Koshimizu has a profitable repair waiting, but the customer expects a certification she does not possess.',
  'Settle the repair commission through the agreed illicit work, a genuine certified alternative, or an actual exposure of the deception.',
  'The repaired household kettle is real, and the deadline is inconvenient rather than world-ending. Let the player repair without licensing, seek a qualified collaborator, expose Mika Koshimizu, or decline. Payment requires the outcome actually agreed with its payer; an exposed fraud does not pay the illicit fee automatically.'),
 ('The Parcel with Two Owners','Renjirō Suda','Four Sages Bazaar',15,110,
  'Renjirō Suda offers a discreet fee to move a sealed parcel whose ownership is more complicated than he first admits.',
  'Resolve custody of the actual disputed parcel through a completed handover, restitution or a consequential agreement.',
  'The parcel contains confiscated enchanted surveying fittings. Its previous owner and the official depot have different claims. Establish the physical object and what the player actually agrees to move. No item changes ownership merely because Renjirō Suda says it does.'),
 ('A Very Profitable Defeat','Momo Shiratori','The Eternal Crucible',10,140,
  'Momo Shiratori has an offer for someone who can make a real arena loss look convincing.',
  'Resolve the proposed match-fixing arrangement through an actual agreed performance, exposure or refusal with consequential follow-through.',
  'An illicit payoff requires a genuine agreement and actual qualifying loss. Refusing an offer alone is not successful paid work. Reporting credible evidence can conclude an accepted exposure undertaking. The tournament controller owns every result: no forged victory, trophy or altered bracket is created by quest completion.'),
 ('The Recommendation in Violet Ink','Renjirō Suda','Four Sages Bazaar',18,130,
  'A private commission requires a sponsor, and Renjirō Suda knows someone who sells unusually convenient recommendations.',
  'Actually obtain, replace or expose the proposed recommendation and settle the specific accepted commission.',
  'A forged letter may fool a particular clerk if a real check succeeds; it does not create a noble title, court key, guild license or universal permission. Genuine sponsorship and exposing the broker are credible alternatives with separately agreed compensation.'),
 ('Scales Before the Census','Shiori Takase','Coppercrest Exchange',24,180,
  'Shiori Takase wants a parcel of sacred shed scales moved before a clan inventory inspection.',
  'Settle the scale parcel through a completed illicit delivery, authorized purchase, restitution or actual exposure.',
  'These are shed scales, not a living dragon to injure or a newly invented egg supply. Establish who currently owns them. Religion, ownership and a trader\'s profit are separate claims. No Drakenspire arrest automatically becomes a Wraith Island sentence.'),
 ('The Missing Weight','Genta Shishido','Redvein Mine',22,150,
  'Two crystal tallies disagree, and Genta Shishido would prefer a quiet correction to an official investigation.',
  'Resolve the actual missing-crystal discrepancy by a completed deception, restitution, verified exposure or a carried-out settlement.',
  'The error conceals deliberate diverted stock, but Genta Shishido is not secretly running the whole nation. Records, actual goods and testimony can establish a narrow case. Do not announce his guilt before evidence or make altering a page summon unlimited crystals.'),
 ('A Blade Without a Name','Koharu Mikazuki','Hearthmarket Square',27,210,
  'Koharu Mikazuki has a handsome blade to sell quickly and very little interest in its previous owner.',
  'Settle the actual stolen blade through fencing, recovery, restitution or a consequential bargain with the affected people.',
  'The weapon is one existing physical object established during the quest, not a new legendary reward for everyone. The owner has a recognizable repair mark, not an omniscient tracking spell. Keep who paid, retained or recovered it distinct.'),
 ('A Delay Worth Buying','Koharu Mikazuki','Hearthmarket Square',25,170,
  'A trader will pay to delay a rival\'s delivery without making the damage look deliberate.',
  'Carry out or expose the specific delivery interference, or establish a genuine alternative settlement.',
  'The cargo is ordinary valuable winter cloth and metal fittings. Sabotage can harm workers who were not part of the dispute. Offer warning, bargaining or refusal without turning the entire city into a chase. Torture alone, theft and fraud do not expand Glowhaven\'s existing automatic wanted loop.'),
]

ONI_LORE={
 'Oni — Country, Houses and Public Life':
  'Beyond Glowhaven lies an oni homeland of broad cultivated fields, wooded roads and distinct towns under a Shogun. Household loyalties, local officials, martial schools and independent organizations share influence; their rivalries do not make every resident a soldier. Wooden streetscapes, tiled roofs, paper screens, workshops and market gardens shape ordinary life. Travelers can be craftspeople, farmers, couriers, scholars or adventurers. Horned ancestry is not an allegiance or a compulsory temperament.',
 'Oni — Samurai and Shinobi Traditions':
  'Samurai serve through learned martial, administrative or household duties. Shinobi traditions develop reconnaissance, concealment, fieldcraft and specialized magical techniques; they are not a separate species or a power everyone inherits. Some organizations accept commissioned work while others bind themselves to a household or locality. Methods, ethics and politics differ. Their society permits both public honor and discreet pragmatism without making either universal.',
 'Oni — Arcane and Soul Magitech':
  'Oni workshops are especially accomplished at selected Arcane- and Soul-based mechanisms: warded tools, spirit-message relays, articulated assistive devices and compact workshop machinery. Expensive specialized equipment can coexist with hand labor, traditional buildings and open farmland. There are fewer exposed cables than in a modern city; this is no ubiquitous electrical metropolis. A device still needs suitable materials, a finite power source, knowledge and maintenance. Skill does not belong exclusively to ancestry.',
 'Oni — Yokai and the Unquiet Countryside':
  'The oni countryside has unfamiliar yokai, local spirits and territorial supernatural creatures. Some are dangerous predators, some intelligent neighbors and others bound to a place or custom. A horn, frightening appearance or spiritual nature alone proves no crime. Local accounts mix useful observation, custom and exaggeration. A mysterious torii is known in travelers\' stories for exuding Soul magic; its route and significance require an actual future investigation rather than opening a new destination through rumor.',
}

DUNGEON_LORE={
 'The Sepulchral Conservatory':
  'A sealed sanctuary beyond an old Evertree connection, where gardeners tried to grow new vessels for the dead. Living timber, memorial stone and old irrigation channels surround abandoned glasshouses. Some bodies are empty animated frames; others carry identifiable spirits. Their caretaker has continued the work long after the keepers vanished. The portal threshold offers a clear way home, while the inner gardens demand preparation and courage.',
 'The Conservatory — Vessels and Their Names':
  'Nature magic grows and repairs the plant framework. Soul magic binds an instruction, residue or conscious spirit to it. These are different things: breaking a frame does not always release its charge, and not every golem contains a dead person. Memorial plaques and the tending apparatus can distinguish them. A living plant may respond to Nature working, while an actual binding calls for Soul knowledge, careful physical intervention or qualified help.',
}

MONSTERS={
 'Gravewood Golem':dict(description='A broad walking frame of pale timber, riblike branches and an empty stone face-mask. Moss threads its joints and amber lights burn in the grain. Most are mindless instruction-bound vessels, not conscious dead people. Nature and Soul workings are distinct ways to affect frame and binding. Guards the rooted walks in small groups; deliberate flanking and exposed joint bindings provide counterplay.',vulnerabilities=['fire'],resistances=['piercing'],immunities=['poisoning']),
 'Rootbound Pallbearer':dict(description='A four-legged bier of black roots carrying a hollow wooden torso and a little bell. It drags binding strands behind it and tries to hold an intruder for another guardian. Slow turns and the exposed rear bell are readable weaknesses. Its apparent coffin is not automatically occupied by a conscious soul.',vulnerabilities=['fire'],resistances=[],immunities=['poisoning']),
 'Censer-Willow':dict(description='A narrow willow-bodied guardian with hanging seed-pod censers and a crown of long white leaves. It releases visible drifting spiritual haze to obscure an approach, then strikes with flexible branches. Air movement and distance can clear a lane. The haze is not automatic possession, hallucination or unavoidable damage.',vulnerabilities=['fire'],resistances=['nature'],immunities=['poisoning']),
 'Hollowseed Swarm':dict(description='A single coherent encounter of fist-sized seed husks with insectlike root legs and dim blue interiors. They skitter toward warm moving bodies and try to overwhelm one exposed position. Broad barriers, water channels and disrupting the central cluster can limit them. A swarm is not an unlimited number of independent attacks.',vulnerabilities=['fire','water'],resistances=[],immunities=['poisoning']),
 'Ossuary Trellis':dict(description='A wall-clinging lattice of roots and old animal bones, its folded limbs opening like a garden fan. It blocks narrow routes with real hooked growth and reacts to contact or vibration. Cutting its exposed anchors or following a different physical route can avoid a direct contest.',vulnerabilities=['fire'],resistances=['piercing'],immunities=['poisoning']),
 'Grafted Sentinel':dict(description='A tall armored tree-vessel with a polished memorial plate, a heavy root club and a visible amber binding knot behind one shoulder. These finite inner guards act with disciplined physical pressure rather than a limitless supply of spells. A real individual spirit may occupy a particular vessel only when established; otherwise it is an instruction-bound guardian.',vulnerabilities=['fire'],resistances=['piercing','nature'],immunities=['poisoning']),
 'Rootbound Regent':dict(description='An individually named intelligent caretaker built from living timber, funerary bronze and conscious spiritual bindings. It can reason, bargain, lie and defend itself. Its Nature framework and Soul stewardship do not confer universal magic immunity, instant resurrection or the authority to command every dead creature.',vulnerabilities=[],resistances=['nature'],immunities=['poisoning']),
}

GROVE_AREAS={
 'Sepulchral Portal House':{
  'Return Arch':('An intact pale arch opens toward the recognizable Evertree roots. Dry benches and an old inspection table make this threshold a usable staging refuge.','Vestibule'),
  'Vestibule':('Cracked green tiles lead past a gardener\'s coat hooks and a plan of the sanctuary carved in stone. The main conservatory is visible through the outer doors.','Return Arch')},
 'Sepulchral Conservatory':{
  'Entry Rotunda':('A roof of cracked green glass shelters a dry circular platform above slow irrigation water. Two overgrown tending wings lead toward a bronze-latticed inner greenhouse.','Rootwalk,Memorial Orchard'),
  'Rootwalk':('Pale root bridges cross irrigation channels beside silent racks of unfinished wooden bodies. Broad piers offer cover from the guardians beyond.','Entry Rotunda,Tending Gallery'),
  'Tending Gallery':('Pruning tools, repaired joints and strips of binding cloth cover long workbenches. Timber guardians patrol around an exposed rootwake valve.','Rootwalk,Memorial Orchard'),
  'Memorial Orchard':('White-leaved trees carry small bronze nameplates. Some hollow trunks answer a voice; others repeat only an old work instruction.','Entry Rotunda,Tending Gallery,Ossuary Greenhouse'),
  'Ossuary Greenhouse':('Animal bones support climbing vines around a dry stone bed. A clear bell beside a mourning valve marks the second tending circuit.','Memorial Orchard,Grafting Heart'),
  'Grafting Heart':('A vast rooted cradle rises around a bronze-and-timber figure beneath the last intact glass dome. Amber veins connect it to the sanctuary\'s two tending circuits.','Ossuary Greenhouse'),
  'Keeper Archive':('A dry side room holds water-stained journals, diagrams of vessels and carefully labeled names. The records distinguish empty frames from conscious charges.','Memorial Orchard')},
 'Mourning Garden':{
  'Quiet Gate':('A broken garden wall encloses low white flowers and scattered memorial stones. The conservatory\'s roof rises beyond the trees.','Reed Pool'),
  'Reed Pool':('Clear water covers a collapsed path, with stepping stones still visible beneath drifting pale reeds. Small seed husks stir at the edges.','Quiet Gate,Sheltered Arbor'),
  'Sheltered Arbor':('An open-sided wooden shelter offers a dry seat, a surviving gardener\'s sketch and a view back toward the portal house.','Reed Pool')},
}
