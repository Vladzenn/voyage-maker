"""A reviewed repertoire of distinct actions, using native ability fields only."""

SPELLS={
 'Arcane':[
 ('Chalkstar Needle','Send a narrow raw-mana dart through one exposed gap; precise aim matters more than impact.'),
 ('Lantern Cage','Arrange three small force panes around an object to catch a falling load; the open sides remain open.'),
 ('Cathedral of Lines','Build a waist-high interlocking force lattice that divides one approach and gives allies cover; it has real breakable surfaces.'),
 ('Borrowed Orbit','Keep one small carried tool circling within arm\'s reach, then send it along a chosen short path; this grants no extra attack.'),
 ('Crown of Interception','Prepare several bounded force facets to intercept one approaching volley; gaps, strength and the actual result still matter.'),
 ('The Last Clear Equation','Unmake one understood hostile construct by attacking a structural junction; powerful unfamiliar magic requires investigation and can resist.')],
 'Fire':[
 ('Cinder March','Move behind a brief low ember screen without treating it as solid cover or invisibility.'),
 ('Kettlewick Touch','Warm a small existing object to a controlled useful temperature; living tissue and dangerous materials demand caution.'),
 ('Emberglass Fan','Send a broad short fan of sparks that threatens an exposed approach without a room-filling explosion.'),
 ('Heat Haze Waltz','Create a localized shimmer that makes a distant outline harder to judge, while leaving nearby sight intact.'),
 ('Furnace Gate','Hold a narrow stationary curtain of heat across an actual doorway; it does not block sight, air or an unrelated route.'),
 ('Sunfall Crucible','Concentrate a major heat release into one declared bounded area after a visible preparation; allies and combustible surroundings remain at risk.')],
 'Water':[
 ('Blue Ribbon Snare','Loop a small quantity of water around an ankle or tool and pull against its resistance; this is not a guaranteed restraint.'),
 ('Raincup Filter','Separate ordinary grit from a cupful of existing water; this does not guarantee removal of poison or disease.'),
 ('Dancer Beneath the Rain','Draw existing surface water beneath a short moving path to interfere with footing or help a deliberate slide.'),
 ('Riverglass Rampart','Raise a compact moving water barrier that can divert a modest projectile; it is not solid ice.'),
 ('The Turning Flood','Redirect a substantial existing current around an obstacle, keeping its volume and dangerous pressure real.'),
 ('Palace of Falling Rain','Suspend and release a large prepared mass of water in a controlled descending pattern; no ice, blood control or permanent conjured reservoir is created.')],
 'Earth':[
 ('Pebble Choir','Lift a handful of nearby stones and cast them in one directed burst; resolve one actual attack.'),
 ('Earthen Thumbprint','Press a temporary identifying impression into accessible clay or loose soil without detecting an unseen person.'),
 ('Rampart Step','Raise a broad low earthen step for a defensive angle or safer reach; ceilings and real foundations constrain it.'),
 ('Dunehook','Draw loose sand into a short gripping ridge beneath a target; hard stone floors offer no convenient sand.'),
 ('Bastion Without a Crown','Build several connected earthwork sections with visible gaps and finite durability rather than an invulnerable dome.'),
 ('Faultline Testament','Drive a carefully directed rupture through an understood existing rock seam; unstable structures and nearby people remain a serious consideration.')],
 'Wind':[
 ('Tailwind Courtesy','Give one willing person a brief assisting breeze for a jump or recovery of balance; it grants no flight or extra action.'),
 ('Whistling Thread','Send a small tied signal along a short known open air route, unable to pass sealed barriers.'),
 ('Crosswind Stair','Support one short controlled aerial step between nearby footholds; a failed landing still needs a real recovery route.'),
 ('Bannerbreaker','Push a broad sideways gust through one declared lane to disturb aim, smoke or loose material.'),
 ('Seven Sails Ascending','Maintain sustained personal flight with real concentration, Mana and wind limits; passengers require separate preparation.'),
 ('The Weather Opens','Influence an existing local cloud front over time, shifting a limited patch of rain or wind rather than commanding the entire sky.')],
 'Lightning':[
 ('Bluebell Sting','Release a short directed spark toward an exposed target; it neither guarantees paralysis nor jumps freely through every bystander.'),
 ('Static Petal','Place a faint temporary charge on one touched nonliving object, useful as a visible contact signal.'),
 ('Thunderclap Reversal','Send a brief counter-directed discharge along an actual approaching conductive line; timing and insulation matter.'),
 ('Stormwire Arc','Link two prepared conductive points with a brief controlled arc; announce the path and its danger before committing.'),
 ('Spear of the Stormcourt','Concentrate a powerful long-range discharge into one sighted lane, with real cover and grounding counterplay.'),
 ('Heaven\'s Answering Bell','Draw a major discharge through a prepared storm circuit; setup, weather, conductors and civilian safety constrain it.')],
 'Ice':[
 ('Winter Button','Form a small temporary ice catch around a touched fastening; force or warmth can break it.'),
 ('Frostprint','Chill a small exposed surface so recent warm contact may become easier to inspect; this reveals no exact identity or history.'),
 ('Glasswinter Causeway','Lay a short broad ice path across a shallow obstacle, with finite load, slippery footing and actual anchoring.'),
 ('Blue Chapel Wall','Grow a segmented ice screen with narrow protected viewing gaps; it can melt or shatter.'),
 ('Still Lake Verdict','Remove heat from a bounded existing wet surface over several moments, threatening footing without instantly freezing living blood.'),
 ('The White Cathedral','Build a large temporary chamber of ice ribs and screens, requiring support and sustained control rather than granting an invulnerable palace.')],
 'Light':[
 ('Starling Glint','Throw a bright glint toward one sighted line to distract aim; it is not automatic blindness.'),
 ('Lanternscript','Illuminate an existing etched pattern with a stable narrow light, making detail easier to inspect without revealing hidden truth.'),
 ('Starlight Aperture','Focus a short beam through a prepared gap, trading a narrow firing line for concentration.'),
 ('Sunroom Veil','Fill a small area with even diffuse light that reduces harsh shadows; it grants no healing or protection from every illusion.'),
 ('The Unbroken Beacon','Maintain a clear distant signal through ordinary darkness, with actual line-of-sight and atmospheric limits.'),
 ('Daybreak Lance','Release a tightly focused high-energy light beam into one declared lane after visible preparation; reflective surfaces and real cover matter.')],
 'Metal':[
 ('Iron Orchard Bud','Shape a small temporary metallic hook for a brief task; conjured metal fades and supplies no saleable ore.'),
 ('Smith\'s Quiet Ear','Sense a touched metal piece\'s strain through a controlled vibration; this is inspection, not universal appraisal.'),
 ('Silverreed Guard','Bend accessible metal into a narrow deflecting arc without stealing distant weapons automatically.'),
 ('Chain of Proper Measure','Alter the length and shape of an existing modest chain while preserving its actual mass and material limits.'),
 ('Iron Orchard','Raise several temporary metallic spars as obstacles, leaving visible routes and finite breakable supports.'),
 ('The Patient Transmutation','Refine a prepared quantity of real metallic material through a difficult controlled working; conservation, tools and impurities remain real.')],
 'Nature':[
 ('Briar Button','Conjure a short temporary thorned fastening to catch cloth or hold a small object; strength can break it.'),
 ('Greenhouse Courtesy','Encourage a small living plant to recover from ordinary stress using suitable soil, light and water; this does not heal people.'),
 ('Hedgeknight\'s Welcome','Grow a temporary branching screen along a touched support, useful for cover but vulnerable to cutting and fire.'),
 ('Rootwalk Covenant','Ask accessible existing roots to form a short stable path, requiring real plant matter and suitable footing.'),
 ('The Orchard Takes a Stand','Shape a substantial rooted barrier with several grasping branches; it has limited reach and cannot pursue detached targets indefinitely.'),
 ('Spring After the Ash','Restore a damaged real planting through a sustained difficult working with surviving roots and actual growing resources; it creates no instant inexhaustible harvest.')],
 'Sound':[
 ('Copper Cricket','Produce a short directional chirp from a touched object for a simple signal, not concealed telepathy.'),
 ('Velvet Footfall','Soften a few actual footsteps by controlling their vibration; nearby observers can still see the caster.'),
 ('Mourning Bell Release','Send a bounded resonant pulse that can interrupt fragile concentration; resolve resistance rather than guaranteeing a canceled spell.'),
 ('The Split Chorus','Carry two distinguishable voices along separate short acoustic lanes, without translating unknown languages.'),
 ('Bellwall','Set a sustained resonant boundary that disrupts an approaching vibration or sound-based working; it does not stop every physical projectile.'),
 ('Cathedral Resonance','Excite an understood structural frequency through a prepared major working; material knowledge and collateral risk matter, and buildings do not collapse by declaration.')],
 'Gravity':[
 ('Pocket Moon','Briefly lighten one small held object, not its owner or every item in a pack.'),
 ('Pendulum Courtesy','Apply a short gentle pull to steady a swaying load; the weight must remain within the caster\'s practiced scale.'),
 ('The Bent Step','Alter local downward pull for one short movement, changing a jump or fall without granting permanent flight.'),
 ('Court of Heavy Petals','Increase apparent weight in a small declared patch; targets can resist, brace or leave it.'),
 ('Crownless Meteor','Draw a substantial existing object into one committed descending strike; the object, travel path and possible damage remain real.'),
 ('Orbit of the Unbowed','Maintain several carefully bounded gravitational lanes to redirect movement, with real concentration and no infinite crushing field.')],
 'Void':[
 ('Black Margin Mark','Place a small temporary darkened edge around a touched surface, making a boundary easier to see without opening another realm.'),
 ('Hollow Candle','Dampen one minor nearby magical glow through a brief opposing working; ordinary flame is not automatically erased.'),
 ('The Unspoken Gap','Attack a vulnerable interval in an understood ongoing spell, requiring timing rather than canceling every caster on sight.'),
 ('Umbra Pocket','Create a small localized patch of dimness that obstructs visual detail but is neither invisibility nor a bottomless storage space.'),
 ('Silence Between Stars','Suppress a bounded prepared magical effect temporarily through a sustained contest; stronger workings and physical attacks remain threats.'),
 ('The Empty Throne','Create a brief powerful zone of magical interference with explicit boundaries and a serious concentration cost; it does not erase people, souls or the world.')],
 'Healing':[
 ('Gentle Knot','Treat a modest fresh cut with contact and actual clean care; it neither restores lost limbs nor hides the cause of injury.'),
 ('Steady Hands, Warm Breath','Help one willing patient settle ordinary shock while assessing the real wound; comfort is not mind control.'),
 ('The Red Thread Holds','Stabilize a serious injury while preserving the need for proper treatment and actual recovery.'),
 ('Mercy Under the Shield','Provide a focused restorative working to one reachable ally, with no automatic attack or simultaneous group heal.'),
 ('House of Returning Strength','Perform sustained treatment for several consenting patients in a prepared safe space; supplies, time and individual limits matter.'),
 ('Dawn at the Sickbed','Attempt difficult restoration of severe living tissue damage through a major prepared treatment; this is not resurrection or a universal cure for age.')],
 'Enchantment':[
 ('Borrowed Firmness','Briefly reinforce one touched mundane grip or fastening without making it unbreakable.'),
 ('Needle After Rain','Give a small sewing or repair tool a short-lived steadying charm; this grants no finished item or permanent craftsmanship.'),
 ('The Returning Guard','Prepare a bounded reinforcement on one shield or weapon for a difficult exchange; the item remains an actual damageable object.'),
 ('Courier\'s Long Step','Sustain a modest bodily movement enhancement with real Mana cost; it grants no unlimited attacks or inexhaustible Stamina.'),
 ('The Unwearied Hinge','Place a durable limited-purpose enchantment on a prepared real mechanism through careful work and suitable materials.'),
 ('Covenant of the Living Blade','Perform a major personalized equipment enchantment with an explicit finite function and preparation; bonuses require actual supported inventory changes, not bigger prose.')],
 'Summoning':[
 ('Paperwing Errand','Call one tiny temporary paperlike helper to carry a light object along a short known route; it has no free attack.'),
 ('A Guest at the Lantern','Call a small harmless temporary light-bearing familiar with a clear duration and task, not a permanent NPC companion.'),
 ('Hearthbound Sentinel','Form one short-lived defensive elemental at a prepared point; any actual action requires a registered actor or supported resolved technique.'),
 ('The Second Pair of Hands','Call a small bounded helper for a physical task, sharing real coordination and concentration limits.'),
 ('Parliament of Small Wings','Coordinate several minor helpers for reconnaissance of an accessible area; they cannot reveal thoughts or unseen sealed rooms.'),
 ('The Gatekeeper\'s Guest','Call one formidable prepared ally through a learned bounded bond, with real consent, duration and resources; no automatic recruitment or extra damage follows the arrival.')],
 'Illusion':[
 ('Paper Moon Feint','Place a brief false glint on the caster\'s actual movement to sell one feint; it cannot strike.'),
 ('Borrowed Color','Alter the apparent color of one small visible object for a short time; touch and close inspection can expose the effect.'),
 ('A Seat Still Warm','Project a stationary visible likeness at an actual seat, without physical weight, independent thought or automatic deception.'),
 ('The False Doorway','Overlay a plausible visual passage on one existing surface; it does not open a route or alter the map.'),
 ('Masquerade of Rain','Maintain a complex bounded visual disguise for a consenting group, with sensory limitations and real concentration.'),
 ('Palace of the Unsaid','Construct a large prepared sensory illusion with explicit boundaries; it cannot create possessions, force belief, rewrite memory or inflict unearned physical damage.')],
 'Divination':[
 ('Lantern Question','Study one actual nearby trace for a narrow impression, which may be incomplete and requires interpretation.'),
 ('The Unturned Card','Seek an uncertain hint about a simple immediate choice; this is not guaranteed prediction or control over the result.'),
 ('Footprints in the Quiet','Read lingering impressions at a touched place to guide an investigation, without inventing a complete exact historical recording.'),
 ('The Listening Compass','Follow a prepared sympathetic trace toward a plausible local direction; unknown barriers and false leads remain possible.'),
 ('A Window Not Yet Open','Examine a likely near-future consequence through a major focused reading; alternate choices can change it.'),
 ('The Archive of Echoes','Perform a difficult prepared reading of an old significant event through surviving evidence; uncertainty, consent where relevant and the caster\'s actual knowledge still matter.')],
 'Soul':[
 ('Kindly Passing','Ease a minor disturbed spiritual residue toward quiet without destroying a conscious spirit or healing living flesh.'),
 ('Candle for the Absent','Sense whether a touched prepared object carries a spiritual trace; this reveals no automatic identity or private memory.'),
 ('The Borrowed Marrow','Animate one small set of actual animal remains as a short-lived mindless helper. It contains no conscious deceased soul and creates no free attack.'),
 ('Mourner\'s Threshold','Ward a bounded doorway against an actual possessing or intrusive spirit through a contest, not a universal species ban.'),
 ('Court of Unfinished Names','Speak with a willing identifiable spirit through a prepared ritual; testimony is limited by its actual knowledge and honesty.'),
 ('The Last Chain Opens','Attempt a difficult exorcism or release of a conscious bound spirit through prepared evidence and a sustained contest; no casual resurrection or humanoid soul extraction is granted.')],
 'Space':[
 ('Seam at Arm\'s Length','Fold a very short clear interval to retrieve a small unattended object within sight; ownership, barriers and actual access still matter.'),
 ('Two Steps, One Shadow','Make a short personal displacement between visible clear footholds; the destination must actually fit and be unblocked.'),
 ('The Narrow Elsewhere','Open a brief arm-width passage between two nearby prepared points; it cannot cut a person in half or become infinite storage.'),
 ('Measured Horizon','Establish a short-lived local spatial anchor for a later prepared return; it creates no court portal permission.'),
 ('Bridge of the Known Shore','Attempt prepared long-distance travel to a genuinely learned and suitable destination, with serious cost and barriers respected; apply supported real geography changes.'),
 ('The Cartographer\'s Door','Open a major temporary passage between two researched anchored destinations through extensive preparation; no new realm, unknown nation or public-network authorization is invented.')],
}

PHYSICAL={
 'Force Combat':[
 ('Gatebreak Shoulder','Commit to a close shoulder drive against an actual guard, opening space rather than guaranteeing a knockdown.'),
 ('Anvil Courtesy','Catch a weak committed line with the actual weapon or forearm guard and answer in one short forceful exchange.'),
 ('Stonewheel Entry','Step across a target\'s approach and use leverage to turn them; size, footing and resistance matter.'),
 ('The Heavy Door Closes','Drive one broad weapon line across a narrow approach, threatening entry without hitting everyone automatically.'),
 ('Ironhand Clinch','Secure a close grip and use bodily leverage to restrict one opponent\'s movement; breaking or maintaining it is a real contest.'),
 ('Mastbreaker','Commit to a powerful strike against an exposed structural support after identifying it; strength does not declare a building collapse.'),
 ('The Mountain Answers','Absorb pressure through a prepared braced stance and deliver one decisive counter, with actual timing and footing.'),
 ('Crown of the Last Stand','Hold one threatened close approach through a demanding sequence of controlled strikes and guards; no extra turns or invulnerability are granted.')],
 'Finesse Combat':[
 ('Needle at the Cuff','Attack an exposed weapon-hand line with precise placement, seeking disruption rather than an automatic severing injury.'),
 ('The Empty Sleeve','Sell a small false commitment, then enter the opening with one real attack.'),
 ('Swallow Turns Home','Pivot out of one committed line and return along a shorter angle; a genuine escape path is required.'),
 ('The Quiet Disarm','Use a clear leverage point on a held weapon for a precise disarming attempt; grip, reach and resistance matter.'),
 ('Thread Through the Rain','Cross a threatened short lane using actual cover and timing; projectiles do not all miss by declaration.'),
 ('Ribbon at the Throat','Present a controlled nonlethal threat at close reach after earning the position, allowing surrender rather than deciding it for the target.'),
 ('The Ninth Petal Falls','Exploit a carefully read repeated movement with one precise counter; observation does not grant omniscience.'),
 ('The Duel Without a Shadow','Commit to a demanding sequence of angle changes supporting one decisive exchange; speed grants no extra independent attacks.')],
 'Guarded Combat':[
 ('Lantern Behind the Gate','Put an actual shield or defensive line between a nearby ally and one approaching threat.'),
 ('The Folded Wing','Close a compact guard while withdrawing one short safe step; this does not escape an enclosed grapple automatically.'),
 ('Patient Iron','Meet a committed weapon line with a supported guard and seek a short controlled response.'),
 ('A Chair for the Storm','Use stable footing and a real support to resist displacement, accepting that force can still break the position.'),
 ('Circle of Returning Blades','Maintain a mobile defensive arc while a nearby person retreats; it protects only actual reachable lines.'),
 ('The Unbroken Handrail','Guide an injured willing ally along a real route while defending the most immediate approach.'),
 ('Winter at the Gate','Use an exceptionally disciplined guard to stall a stronger close opponent, without granting immunity or canceling their successful actions.'),
 ('The House Still Stands','Organize one demanding defensive exchange around real cover and willing allies; each actor still receives only actual resolved actions.')],
}

def build(existing):
    out={}
    for school,rows in SPELLS.items():
        for i,(name,text) in enumerate(rows):
            skill=school+' Magic';rank=[3,12,24,38,60,85][i];cost=[4,5,9,12,20,32][i]
            if school=='Space':rank=[15,22,35,45,70,90][i];cost=[10,12,18,22,35,50][i]
            req=[dict(type='skill',variable=skill,amount=rank)]
            if school=='Space':req.append(dict(type='skill',variable='Gravity Magic',amount=20 if i<4 else 40))
            duration=' Sustaining the effect beyond its immediate working requires continued concentration and proportionate Mana; temporary conjured matter fades.' if i in [2,4,5] else ''
            desc=text+f' Costs {cost} Mana on a committed attempt, including failure.'+duration+' Use the actual '+skill+' resolution; no guaranteed success or unlisted free action follows.'
            out[name]=dict(name=name,description=desc,requirements=req,bonus=[2,3,4,5,7,9][i],cooldown=[0,0,1,2,3,5][i])
    for skill,rows in PHYSICAL.items():
        for i,(name,text) in enumerate(rows):
            cost=[3,4,5,6,8,10,13,16][i];rank=[3,10,18,28,40,55,70,90][i]
            out[name]=dict(name=name,description=text+f' Costs {cost} Stamina when committed. Resolve one actual {skill} technique; it does not add an automatic hit or extra turn.',requirements=[dict(type='skill',variable=skill,amount=rank)],bonus=[2,3,4,4,5,6,8,10][i],cooldown=0 if i<3 else 1 if i<6 else 3)
    mixed=[('Emberhook Return','Force Combat','Fire',12,'Use a short heated weapon hook to threaten the line opened by an actual close entry.'),('Rain on the Swordline','Finesse Combat','Water',15,'Guide a small existing water ribbon along a precise cut to obscure its changing angle.'),('Thunder Behind the Buckler','Guarded Combat','Lightning',20,'Prepare a brief conducted discharge through the actual buckler during one earned close exchange.'),('Briar at the Heel','Finesse Combat','Nature',25,'Use a short temporary vine anchor to support a precise turning strike, with real breakable footing.'),('The Heavy Crescent','Force Combat','Gravity',30,'Alter a held weapon\'s apparent weight during one committed powerful arc.'),('Star Beneath the Guard','Guarded Combat','Light',35,'Throw a narrow light feint beside the actual guard to support a measured counter.'),('Winteredge Waltz','Finesse Combat','Ice',40,'Lay a brief frost line from the actual weapon during one controlled movement, threatening footing rather than freezing blood.'),('The Iron Door Answers','Guarded Combat','Metal',45,'Reinforce an actual shield rim for a demanding catch-and-answer exchange.'),('Gale at the Shoulder','Force Combat','Wind',50,'Support a committed physical drive with a short directed gust, without doubling its resolved damage.'),('The Unbound Blade','Finesse Combat','Void',60,'Contest one understood magical protection at the actual point of a precise weapon attempt.'),('Lantern Against the Dead','Guarded Combat','Soul',70,'Hold an actual defensive line against a spiritual intrusion while making one controlled physical counter.'),('The Last Arc of Dawn','Force Combat','Arcane',85,'Channel a major bounded force reinforcement through one committed actual weapon strike.')]
    for name,physical,school,rank,text in mixed:
        out[name]=dict(name=name,description=text+' This is one infused physical resolution using '+physical+', not a second detached spell. Costs '+str(6+rank//8)+' Mana and '+str(4+rank//12)+' Stamina on commitment. Resistance and actual positioning still apply.',requirements=[dict(type='skill',variable=physical,amount=rank),dict(type='skill',variable=school+' Magic',amount=max(5,rank-10))],bonus=min(10,3+rank//15),cooldown=1 if rank<40 else 3)
    for i,(name,text) in enumerate([
      ('Circuit Lantern','Diagnose one accessible faulty mana circuit with real tools; reading a fault does not repair it automatically.'),
      ('The Helpful Little Ratchet','Temporarily bypass one understood nonsecurity mechanical fault using actual spare parts, without generating an item.'),
      ('Pressure Valve Sonata','Safely vent a prepared malfunctioning device through a controlled path; stored energy and bystanders remain real.'),
      ('Heart of the Quiet Engine','Recalibrate a complex prepared mana-powered mechanism through sustained skilled work, using actual components and permissions.')]):
        out[name]=dict(name=name,description=text+f' Costs {3+i*3} Stamina for the committed focused work. Powered testing also needs the device\'s real finite supply; no free ammunition, inventory grant or permanent upgrade is implied.',requirements=[dict(type='skill',variable='Magitech',amount=[5,20,45,75][i])],bonus=[3,4,6,8][i],cooldown=[0,1,2,4][i])
    collisions=set(out)&set(existing)
    assert not collisions,collisions
    assert len(out)==160,len(out)
    return out
