"""Finite local contracts. Narrative particulars belong here, not in global AI rules."""

ENTRY_GUIDANCE = (
    'ENTRY BRONZE AND FINITE GUILD FIELDWORK\n'
    'Newly licensed work uses one active weak/trivial hostile initially, normally level 1–3; '
    'follow the stated type/count and New NPC creation profile. Introductory foes never exceed 6. '
    'NPC allies do not raise the band. No hidden alpha, surprise pack, lethal continuous damage, '
    'free follow-up hit or elite upgrade. Use juvenile/beginner variants where specified. '
    'A survey or delivery need not include combat. At the actual work site, show the approach and an escape, then wait for the player. '
    'Notices spawn nothing in the guild hall. Level-7 and level-15 postings advertise stronger bounded jobs. '
    'No forced twist, extra hunt or respawn.')


def update_encounter_guidance(text):
    # Preserve the general combat and dangerous-dungeon paragraphs exactly.
    head = text.split('ENTRY BRONZE CONTRACTS')[0].split('ENTRY BRONZE AND FINITE GUILD FIELDWORK')[0]
    tail = text.split('OTHER DANGER', 1)[1].split('\nFINITE GUILD FIELDWORK:')[0]
    return head+ENTRY_GUIDANCE+'\n\nOTHER DANGER'+tail

# Native npcTypes fields only. Level/damage calibration belongs to generated individuals.
CREATURES = [
    ('Cellar Rat', -30, [], [],
     'A large ordinary brown rat with a blunt nose, torn ears and flour dust caught in its whiskers. It bites when cornered, then scurries behind cover; it has no venom, armor or magical disease. Usually a level 1 nuisance. Scratching, droppings and gnawed sacks reveal its route. Traps, a food lure or a clear escape can work as well as a blow.'),
    ('Stray Dog', -25, [], [],
     'A lean, rough-coated domestic dog with muddy paws and an uneven leather collar. A hungry stray may defend stolen food, bark and make a short snap before retreating. Beginner individuals are level 1–2, not wolves or trained warhounds. Flattened ears and a stiff posture warn of a bite; food, space and patient handling may avoid one. No automatic rabies, bleeding effect or alpha pack.'),
    ('Flour Beetle', -30, [], [],
     'A knee-high oval beetle with cream-brown wing cases, six stubby legs and flour clinging to its feelers. Its shell is thin. It drags dry food toward a dark gap, lifting its front legs before an awkward shove. Level 1–2 specimens are slow nuisances with no damage resistance. Turning a sack, blocking a gap or baiting a basket can contain one without destroying the grain.'),
    ('Runaway Cleaning Broom', -25, [], [],
     'A household broom animated by a worn cleaning enchantment, with copper binding wire and an erratically glowing maker’s mark. It whacks whatever it mistakes for dirt and needs time to turn its long handle. Usually level 2. Pinning the bristles or safely interrupting its accessible binding can stop it. It has no hidden master, inexhaustible spell arsenal or resistance merely because it is a construct.'),
    ('Orchard Crab', -25, [], [],
     'A broad freshwater crab about the size of a cooking pot, its mottled olive shell often carrying fallen blossom petals. It wedges itself into irrigation sluices and raises one conspicuous claw before pinching. Young specimens are level 2–3 and have no armored damage resistance. A baited pot, a lifted sluice or a cautious approach from behind offers alternatives to a fight.'),
    ('Soot Moth', -25, [], [],
     'A hand-sized moth with charcoal wings, amber eye-spots and a fluffy white collar stained by lamp soot. It feeds on warm lamp residue and leaves dusty wing prints on glass. Level 2–3 nuisances flutter into faces or shed a brief obscuring puff; they cannot poison lungs, blind permanently or ignite a building. A shaded decoy lamp and a soft net can move them safely.'),
    ('Timberjaw Gnawer', -15, [], [],
     'A stocky, rabbit-sized mana rodent with broad orange incisors, a squared muzzle and a tail fringed with wood fibers. It gnaws damp supports and stamps before lunging at a nearby boot. Common troublesome adults are level 5–8. Fresh paired tooth marks and a trail of damp shavings expose the nest; sound bracing, barriers and bait interrupt its approach. No instant beam collapse or buried swarm is inherent to the species.'),
    ('Lantern Wasp', -15, ['water'], [],
     'A fist-sized wasp with a translucent amber abdomen and folded wings patterned like paper ribs. Its nest resembles a little hanging lantern. A bright pulse and rising buzz precede a single close sting. Local nuisance adults are level 6–8. Their venom produces a painful welt rather than continuous lethal damage; covering the light or dampening an abandoned nest can make relocation possible.'),
    ('Cinderback Lizard', -15, ['water'], ['fire'],
     'A squat red-brown lizard with four splayed feet and a row of warm coal-colored scales across its shoulders. Often level 7–9 around forges, it warms its back visibly before expelling a short ember puff, then must cool. It cannot breathe a dragon’s stream of flame. A clear cool route, a shielded coal lure or shutting off its heat source changes its behavior.'),
    ('Scrap Imp', -10, [], [],
     'A small nonhumanoid fiend with an angular brass-colored face, batlike ears, backward-bending legs and a forked tail used to carry washers. Often level 7–10, it steals useful offcuts and makes crude mechanical toys. It can speak and bargain, lie or become spiteful; these are individual choices. It throws loose scrap or makes a short clawing rush, without teleporting away an entire inventory.'),
    ('Reed Ambusher', -10, ['lightning'], [],
     'A flat olive amphibian with four finned limbs, a wide shovel jaw and a fringe of reed-like whiskers. It lies in shallow water and pushes a visible V-shaped ripple ahead of a short bankward leap. Usually level 8–11. It must return to water between committed lunges. High dry footing, a disturbed mud trail and bait are useful; concealment is camouflage rather than true invisibility.'),
    ('Burrback Hedgebeast', -10, ['fire'], [],
     'A goat-sized grazer with short brown fur, a broad snout and tough seed-like burrs woven through its back. Local adults are usually level 8–11. It bowls through low fences, lowers its head before charging and leaves hooked burrs along its trail. Its prickles scratch at contact but do not launch endless binding roots. Fruit lures, open lanes and repaired fencing can redirect it.'),
    ('Glass-Eye Basilisk', 0, ['sound'], [],
     'A six-legged gray reptile with green glassy brow plates and milky eyes that brighten before a fixed stare. Local adults are level 13–16. Its sustained gaze causes a brief creeping stiffness; looking away or breaking sight interrupts it. There is no instant permanent petrification. It moves poorly on loose rubble and cannot gaze through walls, shields or closed shutters.'),
    ('Hollow Lantern', 0, ['light', 'sound'], ['dark'],
     'A salt-corroded rescue lantern floating inside a loose hoop of pale spirit-light, with a wavering human-sized shadow beneath it and no actual body. Usually level 13–16. It repeats a damaged signal and releases a bounded pulse of cold light when approached. Its direction and bell rhythm reveal the place to which it is bound. This is a local haunting, not an all-knowing dead soul or an automatic possession.'),
    ('Ashcoil Salamander', 0, ['water', 'ice'], ['fire'],
     'A long charcoal-black salamander with six small feet, a coiling tail and orange seams between its broad scales. Furnace-fed adults are level 14–17. Its throat glows before a close heat jet, followed by a cooling pause. It hunts warm mineral deposits rather than metal objects in an inventory. Damp channels, furnace shutters and vent pressure offer counterplay; no unavoidable room-wide inferno.'),
    ('Mireglass Stalker', 0, ['sound'], [],
     'A low wetland hunter with four narrow legs, a split paddle tail and translucent green plates over a dark amphibian body. Typically level 14–18. Reflections break up its outline, but mud prints, ripples and shifting reeds remain visible. It makes short lunges rather than teleporting and loses its camouflage on dry ground. It has neither perfect invisibility nor an unavoidable opening critical strike.'),
    ('Canal Watcher', 0, ['lightning'], [],
     'A waist-high municipal maintenance construct with a round ceramic torso, three iron feet, a water-level float and two jointed gate tools. Malfunctioning working models are around level 14–17. A clacking gauge precedes each heavy tool sweep. A cracked float or obstructed intake may explain its faulty safety order. It has reachable controls, limited movement and no blanket construct immunities.'),
    ('Thunderfin Ray', 0, ['earth'], ['lightning'],
     'A blue-gray mana ray that skims wet sand and shallow water on broad winglike fins, with three amber nodules along its spine and a narrow ribbon tail. Local adults are level 15–18. The nodules glow and its fins spread before a bounded electric discharge. Dry high ground and spacing matter; it cannot electrocute an entire coastline or discharge every action without recovery.'),
]


def job(title, client, location, area, creature, band, level, rank, marks, xp,
        statement, goal, scene, lane='combat'):
    return dict(title='Guild: '+title, client=client, location=location,
                area=location+' - '+area, creature=creature, band=band,
                recommendedLevel=level, rank=rank, marks=marks, xp=xp,
                statement=statement, goal=goal, scene=scene, lane=lane)


JOBS = [
    job('Rats in the Cellar', 'Noriko Hanesawa', 'Roseberry Inn', 'Cellar',
        'Cellar Rat', 1, 1, 1, 30, 200,
        'Something has gnawed through the inn’s flour sacks. Noriko Hanesawa offers 30 marks to clear the cellar and stop the damage before supper preparations.',
        'Clear the rats damaging Roseberry Inn’s cellar stores and close their visible entry gap, leaving the food storage usable.',
        'Noriko Hanesawa has balanced a flour sack on a chair and is refusing to sacrifice another loaf. Two ordinary rats occupy the cellar, separated by shelving; begin with one exposed and the other hiding. Their trail leads to a loose board beside the steps. Fighting, traps or a food lure can clear them; the gap needs a simple physical repair. Let this be a short, satisfying first job. No rat king, disease outbreak or second nest.'),
    job('The Washbasin Is Occupied', 'Daichi Kamado', 'The Golden Ladle', 'Kitchen Passage',
        'Puddle Slime', 1, 1, 1, 30, 200,
        'Daichi Kamado’s kitchen basin has acquired an unwelcome wobbling occupant. He offers 30 marks for a working basin and an uninterrupted lunch service.',
        'Remove or defeat the Puddle Slime in The Golden Ladle’s washbasin and restore the basin to safe use.',
        'One level 1–2 Puddle Slime keeps sliding back into the basin through a leaking pipe joint. Daichi Kamado argues with it as if it were a lazy kitchen assistant. A bucket, a lure or careful fighting can remove it; closing the small leak prevents another immediate slip back. Splashing dishes makes a mess, not an acid attack. The actual removal and usable basin finish the work.'),
    job('The Watchdog Nobody Hired', 'Kaito Minato', 'Whitecrest Harbor', 'Cargo Pier',
        'Stray Dog', 1, 2, 1, 35, 240,
        'A stray dog is defending a bundle of stolen provisions behind the cargo sheds. Kaito Minato offers 35 marks to recover the supplies and let the porters work safely.',
        'Recover the cargo-pier provisions and end the stray dog’s obstruction without leaving it threatening the workers.',
        'One hungry level 1–2 dog has decided a dropped sausage bundle is its property. It barks before snapping and backs toward the shed when crowded. Food, calm handling, a barrier or a fight can settle it. Kaito Minato wants the pier safe; he has not ordered a killing or promised free adoption. The dog does not lead to a wolf pack. Keep any voluntary care or ownership decision separate from the paid job.'),
    job('Something in the Flour', 'Haruho Taneda', 'Brookmeadow', 'Mill Lane',
        'Flour Beetle', 1, 2, 1, 35, 240,
        'Flour sacks are moving by themselves in Brookmeadow’s mill yard. Haruho Taneda offers 35 marks to stop the theft without ruining the remaining grain.',
        'Remove the Flour Beetle taking grain in Brookmeadow’s Mill Lane and leave the remaining sacks secure.',
        'One level 1–2 Flour Beetle is hauling a sack far too large for it, inch by determined inch. Haruho Taneda is more offended by the waste than frightened. It pauses to rearrange the load, exposing its soft underside. Trap, lure or defeat it. A tipped sack and a tied store cover are enough environmental business; the beetle is not a secret armored boss.'),
    job('Swept Off Your Feet', 'Reiji Takatori', "Rune and Raven's", 'Back Stock',
        'Runaway Cleaning Broom', 1, 2, 1, 35, 240,
        'A cleaning broom at Rune and Raven’s has begun treating customers’ boots as stubborn dirt. Reiji Takatori offers 35 marks to stop it before another customer complains.',
        'Safely stop the runaway cleaning broom in Rune and Raven’s back stock and leave it contained or repaired.',
        'One level 2 broom has chased Reiji Takatori onto a stock stool. Its loose binding charm is plainly accessible near the bristles. Pinning it, distracting it with dirt, disabling the binding or defeating it are all credible. A cracked handle may lower its resale value but does not secretly cancel the agreed fee. No advanced Enchantment skill is mandatory to wrestle a broom into a cupboard.'),
    job('A Claw in the Channel', 'Takumi Hatano', 'Glowhaven Farmlands', 'Irrigation Run',
        'Orchard Crab', 1, 3, 1, 40, 280,
        'A large crab has wedged itself into an irrigation sluice. Takumi Hatano offers 40 marks to restore the water before the lower beds dry out.',
        'Remove the Orchard Crab blocking the agreed irrigation sluice and restore water to the lower beds.',
        'A single level 2–3 crab grips the sluice frame. Takumi Hatano holds a basket with an obvious hole in it and insists it was a perfectly good plan. The crab raises its claw before a pinch. Bait, a sound container, a lifted gate or careful fighting works. Water should flow again once the obstruction and lodged twigs are removed; do not add an upstream monster.'),
    job('A Very Unhelpful Night-Light', 'Shizuru Sumida', 'The Wandering Quill', 'Stock Alcove',
        'Soot Moth', 1, 3, 1, 40, 280,
        'Sooty wing prints are appearing across The Wandering Quill’s clean paper. Shizuru Sumida offers 40 marks to remove the moths and protect the stock.',
        'Clear the Soot Moths from The Wandering Quill’s stock alcove and remove the lamp residue drawing them to the paper.',
        'Two level 2–3 moths circle one warm lamp; only one is an active nuisance initially. Shizuru Sumida has covered the costly paper with cheap practice sheets. Their amber wing prints collect nearest a freshly polished lamp: sweet resin in the polish, not cursed ink, attracts them. A shaded decoy, netting or careful blows can clear them. Cleaning that lamp gives the job a small satisfying explanation, not another quest.'),
    job('Something Chewed the Joists', 'Makoto Sashihara', "The Carpenter's Measure", 'Timber Yard',
        'Timberjaw Gnawer', 7, 7, 1, 60, 450,
        'Fresh timber keeps failing Makoto Sashihara’s checks before it reaches the workbench. He offers 60 marks to find and stop whatever is chewing the stored joists.',
        'Stop the Timberjaw Gnawer damaging the stored joists and help Makoto Sashihara separate sound timber from the gnawed pieces.',
        'One level 5–8 gnawer nests beneath the damp rack. Paired tooth marks lead to it. A propped timber stack makes reckless heavy attacks a poor choice, but Makoto Sashihara can show a safe brace when asked. Capture, drive off or defeat the creature, then identify the visibly damaged pieces. No hidden infestation or engineering examination follows.'),
    job('Lanterns With a Temper', 'Rinpei Komatsu', 'Four Sages Bazaar', 'North Arcade',
        'Lantern Wasp', 7, 7, 1, 65, 480,
        'Rinpei Komatsu’s newest hanging lantern has started buzzing at customers. He offers 65 marks to remove its occupants without scattering them through the arcade.',
        'Clear the Lantern Wasps from the occupied bazaar lantern and leave the immediate stall frontage safe.',
        'Two level 6–8 wasps have occupied a hollow display lantern; only one emerges at first. Close the neighboring screens or move the display before provoking both. Rinpei Komatsu claims the buzzing is excellent advertising until a customer refuses to approach. Covering its light, relocating the nest or a controlled fight works. A painful sting is one resolved attack, not an automatic continuing poison clock.'),
    job('Warm Feet, Cold Delivery', 'Kazuo Kurogaki', 'Blackstone Smithy', 'Forge Floor',
        'Cinderback Lizard', 7, 8, 1, 70, 520,
        'A Cinderback Lizard has settled on the forge delivery route. Kazuo Kurogaki offers 70 marks to clear it without letting its ember puffs reach the waiting packing straw.',
        'Remove the Cinderback Lizard from Blackstone Smithy’s delivery route and make the packed goods safe to move.',
        'One level 7–9 lizard sprawls across a warm stone near the forge door. Its glowing shoulder scales telegraph each short ember puff. Moving the straw and opening a cool route are useful preparation. Lure it, contain it or fight with the forge’s actual cover. Kazuo Kurogaki provides ordinary tongs when asked, not a free enchanted weapon. The job ends with a clear route and secure packing.'),
    job('The Spare Parts Bargain', 'Seiji Haguruma', 'The Compassmaker', 'Parts Cabinet',
        'Scrap Imp', 7, 9, 1, 75, 560,
        'Washers, springs and a very particular gear have vanished from Seiji Haguruma’s cabinet. He offers 75 marks for their recovery and an end to the intrusions.',
        'Recover or replace Seiji Haguruma’s stolen working parts on terms he accepts, and settle the Scrap Imp’s repeated intrusions.',
        'One level 7–10 Scrap Imp has assembled an almost-working clock beneath the bench. It sincerely offers to trade the stolen gear for another stolen gear. Seiji Haguruma may accept a properly agreed supply of useless offcuts if the necessary working parts come back; the player cannot give his stock away for him. Bargain, trap or defeat the imp. Its ridiculous hobby does not excuse the theft or compel friendship.', lane='other'),
    job('A Ripple Under the Ford', 'Shiori Kawase', 'Pinewater River', 'Brookmeadow Ford',
        'Reed Ambusher', 7, 10, 1, 80, 600,
        'Something has been snapping at the crossing ropes at Brookmeadow Ford. Shiori Kawase offers 80 marks to make the marked crossing usable again.',
        'Remove the Reed Ambusher threatening the marked ford crossing and restore a safe line for the crossing crew.',
        'One level 8–11 ambusher waits beside the shallow rope anchor, with ripples exposing its position. Shiori Kawase refuses to send another porter across until it is dealt with. Work from a dry bank, draw it into the open or fight during its recovery after a leap. A frayed rope needs retying, not a second expedition. The accepted notice makes this stronger creature explicit; ordinary nearby travelers do not acquire its difficulty.'),
    job('Prickles in the Orchard', 'Takumi Hatano', 'Glowhaven Farmlands', 'South Fields',
        'Burrback Hedgebeast', 7, 11, 1, 90, 650,
        'A Burrback Hedgebeast keeps flattening the orchard fence on its evening visits. Takumi Hatano offers 90 marks to stop the raids and secure the damaged stretch.',
        'End the Burrback Hedgebeast’s raids on the agreed orchard beds and leave the damaged fence secure.',
        'One level 8–11 grazer follows the smell of split fruit through a broken fence. Its lowered head and scraping forefoot warn of a charge. Moving the windfalls can draw it away; a sound barrier, relocation or defeat also works. Takumi Hatano can supply fence slats from his actual repair pile. This is a stubborn animal causing costly damage, with no obligation to discover a secret ecological catastrophe.'),
    job('Do Not Meet Its Eyes', 'Osamu Iseki', 'Greywatch Keep', 'Overgrown Yard',
        'Glass-Eye Basilisk', 15, 15, 2, 110, 850,
        'Osamu Iseki spotted an unfamiliar reptile beside Greywatch’s old yard wall. A commissioned inspection offers 110 marks to clear the marked approach before local workers enter.',
        'Clear the Glass-Eye Basilisk from the marked Greywatch yard approach so the commissioned inspection can proceed safely.',
        'One level 13–16 basilisk occupies a sunny rubble shelf. Osamu Iseki is a retired mason and witness, not Greywatch’s owner or a commander. The job concerns this approach only. Brightening eyes precede a sustained stiffening stare; broken sight interrupts it. Shielding, noisy distraction, containment or combat can succeed. The animal has not turned missing workers into statues, and no deeper keep clearance is required.'),
    job('The Lantern That Would Not Land', 'Kaito Minato', 'Pinewake Coast', 'Pine Headland',
        'Hollow Lantern', 15, 15, 2, 120, 900,
        'A wandering light is drawing boats toward Pinewake’s wrong channel. Kaito Minato relays a 120-mark commission to end the dangerous signal.',
        'End the Hollow Lantern’s misleading coastal signal, leaving the Pinewake approach safe for the affected boats.',
        'One level 13–16 haunting repeats an old rescue rhythm. Its turns point toward a real snag beneath the water: the alarm is damaged, not maliciously luring people for a sea god. The player can correct the local binding and establish a reliable warning, quiet it or defeat it. Natsume Isobe may share a sketch if actually present; do not summon her as a required witness. Resolving this one signal completes the job without a second hidden culprit.', lane='other'),
    job('Too Hot for the Furnace', 'Kazuo Kurogaki', 'Blackstone Smithy', 'Forge Floor',
        'Ashcoil Salamander', 15, 16, 2, 130, 950,
        'An Ashcoil Salamander has moved into a furnace vent and the working heat is rising. Kazuo Kurogaki offers 130 marks to remove it before the next firing.',
        'Remove the Ashcoil Salamander from the agreed furnace vent and restore a safe working draft.',
        'One level 14–17 salamander feeds on deposits in the vent. Kazuo Kurogaki shuts down the working forge before the attempt; do not attack customers with a live furnace hazard. Opening a cool exit, managing the shutters or a prepared fight can remove it. Its orange throat telegraphs the heat jet. A cooling and draft check ends the work; no rare-metal delivery or mandatory magical engineering project is added.'),
    job('Tracks That Disappear', 'Shiori Kawase', 'Pinewater Woods', 'River Edge',
        'Mireglass Stalker', 15, 16, 2, 135, 1000,
        'A supply crew keeps losing its route to a hunter it can barely see. Shiori Kawase relays 135 marks to clear the marked river-edge approach.',
        'Remove the Mireglass Stalker threatening the marked supply approach and establish that the crew can use the route.',
        'One level 14–18 stalker has a visible trail in mud despite its broken outline. The player can study that trail and choose dry footing before committing. Drive it away from the working approach, contain it or defeat it. Keep the creature’s actual retreat and injuries. No invisible pack appears behind the party, and clearing this stretch does not require making the whole forest harmless.'),
    job('The Gate That Guarded Nothing', 'Takumi Hatano', 'Glowhaven Farmlands', 'Irrigation Run',
        'Canal Watcher', 15, 17, 1, 140, 1050,
        'A maintenance construct is barring an irrigation gate that workers must open. Takumi Hatano offers 140 marks for a functioning gate and a safe work path; the notice warns of heavy moving tools.',
        'Stop the malfunctioning Canal Watcher obstructing the agreed irrigation gate and restore safe access to the controls.',
        'One level 14–17 construct has a cracked float stuck at flood level. Its response is dangerous even though the fault is mundane. A safely braced gate, freed float, accessible shutdown or controlled defeat can settle it; no specialist spell is compulsory. Takumi Hatano wants water control restored, not a collectible golem. Repair is a real alternative to combat and grants neither ownership nor free Magitech skill.', lane='other'),
    job('Blue Sparks at Low Tide', 'Kaito Minato', 'Crescent Shores', 'Sheltered Cove',
        'Thunderfin Ray', 15, 18, 1, 150, 1100,
        'A Thunderfin Ray is keeping a small fishing crew from its beached gear. Kaito Minato relays a 150-mark job to clear the cove approach, with an explicit warning about electric discharges.',
        'Clear the Thunderfin Ray from the crew’s cove approach and make their beached gear safely recoverable.',
        'One level 15–18 ray skims the shallows around bait spilled from a torn basket. Its amber nodules glow before it discharges. Dry rock, spacing and moving the bait are useful; relocation or a prepared fight can succeed. The crew’s ordinary gear is entrusted property, not bonus loot. One secured approach completes the job; it does not turn into a hunt for a legendary storm beast.'),
]


LEGACY_BRIEFS = {
    'Guild: A Parcel for the Bazaar':
        'Rinpei Komatsu needs a box of fragile trinket clasps before his next customer fitting. The address leads to his actual stall at Four Sages Bazaar. Give the delivery a small practical obstacle: a busy arcade and the awkward parcel, not an armed ambush. Rinpei Komatsu talks while inspecting the clasps and may ask the carrier to hold one edge of his display. Keep his received-delivery record and the existing guild verification as the ending. An intact delivery and honest handling matter more than a flawless performance.\nBronze; posted fee 40 marks. Existing work-proof and settlement logic own completion and payment. No compulsory combat, second commission or automatic relationship reward.',
    'Guild: Westwood Trail Notes':
        'The guild needs a useful account of an ordinary public trail in West Glowhaven Woods, not a heroic monster census. An old route marker has sagged toward a muddy deer track; footprints and the actual path make the mistake discoverable. Let the player inspect footing, record a fallen branch or clear finding and make understandable notes. A spoken dictation or simple sketch can be useful; no scholarly essay is required. Distant wildlife need not attack. Return the route notes for the existing verification and finish there.\nBronze; posted fee 50 marks. Preserve the existing proof, completion and reward owners. Do not move this survey into an unrelated dangerous lair.',
    'Guild: Boars at the Watercourse':
        'At Pinewater River’s agreed working bank, stage one Young Stonehide Boar with soft undeveloped mineral patches. It has been raiding spilled feed and now blocks the workers’ approach. A stamping forefoot precedes a short committed charge, followed by a clear turn to recover. Moving the feed, a lure, a barrier or defeating it can make the bank usable. The workers need access, not an animal extermination tally. Use one level 2–3 weak beginner individual; no adult armored boar, pack or hidden alpha.\nBronze; posted fee 55 marks and 450 experience. Keep the existing completed-work verification, payment and service-credit owners. A later repeat needs a genuine new agreed job after the existing gap; the same cleared animal never respawns for another reward.',
    'Guild: The Courier at the Wrong Turn':
        'Follow the torn route ribbon into Pinewater Woods. The missing courier is alive beside a tipped load, embarrassed about trusting an old marker and unable to shift the cart with a strained ankle. Shoe marks and scraped bark give ordinary evidence; let observation matter. Unloading, a lever, assistance or suitable learned magic can help. Do not demand Healing magic, a fight or an automatic recruitment. The courier remains a working person with their own destination. Resolve the actual predicament, then use the existing guild settlement.\nBronze; posted fee 60 marks. Retain completion checks and rewards. Any incidental animal follows beginner limits; no kidnapping ring or compulsory missing second courier.',
    'Guild: A Cart Full of Glass':
        'A cart of household fittings is ready at Caravan Outpost. The nervous driver keeps tightening one rope while ignoring the loose packing underneath. Agree the actual existing local destination before departure. A bad rut and shifting load create the main decision: take the slower firm route, repack or carefully support the cart through. Do not add random bandits merely because this is an escort. A small breakage can be discussed honestly without inventing an all-or-nothing fail condition. Complete the agreed delivery and existing guild settlement.\nBronze; posted fee 50 marks and the existing experience reward. Keep the present repeat cooldown and proof/payment owners. Future work needs a fresh load and agreement, not the old cart reset.',
    'Guild: After the Harbor Squall':
        'At Whitecrest Harbor, marked cargo is caught against a damaged mooring while a working crew argues about which line to cut. Kaito Minato can identify the berth and actual handlers when present. Present the taut rope, unstable crate and incoming swell so the player can plan a pull, brace or safe release. Recovered cargo belongs to its actual owner. No sea monster, surprise smuggling ring or mandatory underwater spell is needed. Once the marked load is safely recovered, the existing guild settlement ends the job.\nBronze; posted fee 45 marks and the existing experience reward. Keep the verification, payment, service credit and fresh-instance repeat rules unchanged.',
}
