"""Authored Oni geography. Coordinates are provisional local positions, not generated map tiles."""
NATION = 'Akitsuhara'
CAPITAL = 'Benitsuru'
SPIRIT = 'The Veiled Beyond'
REGIONS = [
 ('Blackpine March', (1,18), 'Western cedar ridges, hamlets, waterfalls and old roadside shrines. The maintained post road serves everyday journeys; deeper forest hollows have their own occupants.'),
 ('Thundercrag Highlands', (8,30), 'A great terraced quarry and working mine basin below jagged ridges. Stone roads serve inhabited works, while abandoned cuts and high scree are dangerous.'),
 ('Mount Shiun', (10,35), 'The sacred mountain rises behind the capital. Pilgrim lodgings, cedar stairs, pagodas and waterfalls occupy its lower approaches; snow and exposed ridges lie above.'),
 ('Snowcedar Heights', (20,48), 'Snowbound mountains, blue tarns and isolated conifer valleys. A sheltered pass links the few attended refuges. Glacial basins and ruined watchposts demand preparation.'),
 ('Mizuhara Lake Country', (1,20), 'The western castle town and its lakeshore villages share ferries, fish markets and irrigated terraces. The castle is a working seat above a broad landing, not a second national capital.'),
 ('Bamboo Veil Valleys', (1,24), 'Green bamboo valleys connect the western country with Benitsuru. Mills, bridges, paper workshops and small farms stand along bright tributaries; abandoned groves have less welcoming inhabitants.'),
 ('Benitsuru Basin', (1,25), 'The capital beneath the sacred mountain: Shogunal castle, canal wards, shrines, guildhall and dense neighborhoods. Its streets are inhabited civic space, with roads radiating toward both castle towns.'),
 ('Koganedai Terraces', (1,30), 'The eastern castle town stands above gold-leaved terraces, artisan streets, training grounds and timber approaches. House Tsubakiri guards a small imported-device workshop.'),
 ('Mirror-Reed Lowlands', (2,25), 'Wooded low ridges, cedar paths and a narrow river descending beneath an arched bridge. Reeds gather along the northern water margin, but most of this province is forest, rocky slopes and clearings. Small hamlets, dye gardens and roadside shrines serve walkers and pack traffic; the principal crossing is a bridge.'),
 ('Golden Grain Plain', (1,18), 'Working grain fields, paddies, orchards and riverside villages feed the towns. Travelers encounter ordinary farm business as often as trouble; the principal road is maintained.'),
 ('Redleaf River Country', (5,32), 'Maple-red valleys, riverside shrines, guesthouses and broad old bridges. Locals use the main road; wooded side trails and abandoned festival grounds have stranger traffic.'),
 ('Lanternwood Border', (12,45), 'Ancient wooded escarpments, waterfalls and shrines among enormous roots. The Soul Torii occupies a reachable lower approach, while the far cedar hollows shelter dangerous beings.'),
]

# Each line: name | x | y | local encounter band | public place | distinct areas | reusable inhabitants.
# Area descriptions and routes are completed by build.py; every named place has its own scene anchors.
SITES = {
1: '''
Blackpine Posthouse|-10|-20|1-5|A timber posthouse beside the cedar road sells simple meals and dry beds. Couriers warm their hands around bowls while parcels wait on a covered bench.|Road Porch;Common Table;Guest Loft;Parcel Shed|Roadside Sparrow Imp
Cedarfall Hamlet|43|-6|1-8|Cottages cluster beside a working watercourse. Indigo laundry, split firewood and a communal oven make this a place to stop and meet neighbors.|Village Well;Oven Yard;Cottage Lane;Water Steps|
Western Watch Road|37|-15|1-8|A maintained road crosses a stone viaduct above a narrow stream. Watch patrols share it with woodcutters and small carts.|Viaduct;Watch Shelter;Cart Pullout|Bamboo Fox
Old Bell Shrine|30|22|5-15|A modest shrine hangs over a fern-filled gorge. Its bell rope is new, but old plaques have been turned face-in against the weather.|Outer Steps;Bell Court;Fern Descent|Moss-Tongue Kodama
Foxglove Wood|30|8|8-18|Sun reaches long clearings between cedar trunks. Fallen flowers mark animal paths, and a broken charcoal kiln lies beyond the usual gathering ground.|Flower Clearing;Charcoal Kiln;Root Tunnel|Antler-Moss Boar,Bamboo Fox
Blackpine Boundary Stones|-19|36|15-25|Mossy boundary markers follow a disputed ridge. Some stones have been shifted a few feet, enough to put a charcoal wood under another household's claim.|Ridge Path;Shifted Markers;Old Camp|Boundary Tengu
Hollow Cedar Ruins|-4|38|18-30|A burned waystation survives inside a cedar's split roots. Rainwater fills the cooking hearth and something has arranged old cups on the lintel.|Broken Hearth;Root Chamber;Rear Slope|Cinder Umbrella,Paper-Face Lurker
Western Woodcutters' Yard|26|-30|1-8|Logs are counted, seasoned and floated downstream here. The sawyers argue over a newly marked stand while lunch cools on a stump.|Saw Shelter;Log Run;Counting Bench|
''',
2: '''
Thundercrag Quarry|3|17|5-15|Stone terraces step around a pale quarry basin. Haul tracks, hoists and safety shelters keep the working cuts busy; abandoned galleries lie well beyond them.|Receiving Yard;Working Cut;Hoist House;Foreman's Cabin|Scree Crab
Kuroishi Miners' Row|19|-19|3-12|Miners and their households live along a steep lane of patched shutters and flower tubs. A public washhouse stays open after the last shift.|Lane Steps;Washhouse;Meal House|
Basalt Kilns|-2|1|5-15|Low kilns bake roof tiles beside stacks of drying clay. A distorted new firing has left the potters with an expensive heap of crooked rain gutters.|Kiln Yard;Clay Shed;Cooling Walk|Kiln Ashling
Amber-Salt Mine|24|5|12-25|An attended mine extracts small amber inclusions and salts used by alchemists. The good face is narrow and ordinary braces matter more than claims of luck.|Inspection Shed;Salt Face;Brace Junction;Pump Sump|Crystal Centipede
Abandoned Splitshaft|30|22|22-35|A failed mine has two mouths divided by a cracked pillar. One leads to old hauling chambers; the other draws air through a natural cavity.|Twin Mouths;Haul Chamber;Breathing Cavity|Stone-Eating Centipede,Paper-Face Lurker
Scree Lantern Pass|-14|33|18-30|Iron lantern hooks mark a mountain pass. Loose stone hides old steps, and the last sheltered bend carries names carved by passing porters.|Lantern Bend;Loose Stair;Porters' Niche|Scree Crab,Boundary Tengu
Quarry Exchange|-5|-11|1-12|Stone buyers inspect samples under a long awning. Workers can arrange hauling, lodge a wage dispute or find practical mountain equipment.|Sample Tables;Hiring Rail;Weigh House|
Broken Relay Tower|-33|25|25-40|An old signal tower stands beyond the working roads. Cracked mirrors face the wrong valleys; lightning has melted the upper rail.|Mirror Floor;Broken Stair;Roof Platform|Storm-Kite Tengu
''',
3: '''
Shiun Pilgrim Lodge|-6|-32|1-8|Wet sandals line the entrance of a busy pilgrim lodge. Simple sleeping bays, hot millet porridge and a patient drying rack serve people with very different reasons for climbing.|Sandals Porch;Dining Bays;Drying Room;Guest Gallery|
Shiun Thousand Steps|-18|-12|5-15|Cedar stairs climb past small rest shrines and carefully tended drainage cuts. Visitors ring a hand bell at the turns where sightlines disappear.|Lower Rest;Cedar Stair;Water Crossing|Moss-Tongue Kodama
Cloudbell Monastery|2|8|5-20|A mountain monastery keeps prayer halls, a public teaching court and guest rooms. Novices practice forms while visitors debate whether silence is worth missing breakfast.|Teaching Court;Bell Hall;Guest Veranda;Archive Alcove|
Whitefall Shrine|-30|-4|3-12|A waterfall scatters cold mist over the steps of a small shrine. Pilgrims wash their hands below, leaving the upper watercourse undisturbed.|Falls Steps;Offering Shelter;Upper Pool|Whitefall Crane
Summit Cedar Precinct|6|20|20-35|Wind bends the upper cedars around a weathered summit shrine. The mountain view opens beyond a stone railing; the last approach is steep and exposed.|Wind Rail;Inner Court;Storm Shelter|Boundary Tengu
Shiun Herb Slopes|25|-17|10-22|Terraced herb plots give way to wild mountain plants. Woven markers distinguish cultivated roots from protected stands and unstable slopes.|Tended Beds;Gatherers' Path;Rock Shelf|Antler-Moss Boar
Ancestor Archive|12|13|1-15|A stone-backed archive holds family records, repaired shrine registers and accounts of disputed land. Its keeper serves ordinary genealogies as often as great houses.|Reading Bench;Record Stacks;Dry Store|
Frost-Eave Approach|-16|26|25-40|An old ascent curves around frost-streaked rock. An empty hut shelters a cache left for emergencies, and enormous three-toed tracks cross a nearby drift.|Emergency Hut;Drift Crossing;Upper Notch|Snow-Mantle Tengu
''',
4: '''
Snowcedar Refuge|-27|-28|5-20|A low stone refuge has warm sleeping benches, a soup pot and an attended weather board. Its keepers distinguish a difficult crossing from an impossible one.|Heated Hall;Weather Porch;Supply Store|
Blue Mirror Tarn|-6|32|25-40|A glacial lake reflects a torn ring of peaks. Ice shelves crack at the shore while deep blue water remains open farther out.|Shingle Shore;Ice Lip;Observation Ledge|Ice-Reed Serpent
White Antler Basin|-16|-22|30-45|A sheltered basin contains white antler-shaped stone and sparse winter grazing. The quiet is broken by scraping under the snow rather than birdsong.|Antler Stones;Snow Hollow;Raised Moraine|Snowburrow Mukade
Snowcedar Signal Hut|-10|-3|10-25|A staffed signal hut maintains flags and mirror shutters for the pass. Tea tastes of smoke and visitors can leave a message for the next safe caravan.|Flag Deck;Stove Room;Mirror Box|
Rime Bridge|-6|-14|20-35|A narrow bridge crosses a snowmelt cleft. Windblown ice obscures its center, and the handrail needs inspection before loaded parties cross.|Near Abutment;Bridge Span;Far Shelter|Snow-Mantle Tengu
Forgotten Muster Camp|27|30|30-48|A snow-filled camp still has tent rings, stacked shields and a collapsed officer's shelter. Disturbed equipment carries no promise of an unclaimed treasure.|Tent Rings;Shield Store;Officer's Hollow|Hollow War Armor
Sleeping Lake Cavern|6|39|38-55|Cold vapor rolls from a cavern above the tarn. Mineral shelves descend toward a dark pool and the floor bears the smooth tracks of something heavy.|Vapor Mouth;Mineral Walk;Deep Pool|Ice-Reed Serpent,Stone-Eating Centipede
''',
5: '''
Mizuhara Castle|5|28|1-25|A river-facing castle overlooks the western town and lake. House Saionoma conducts audiences in a modest hall while guards train below the granary wall.|Petition Yard;Audience Hall;Granary Walk;Training Court|
Mizuhara Landing|28|23|1-8|Ferries, fishing boats and grain barges crowd a practical lakeside landing. Travelers can hire passage, check a consignment or argue over a missed connection.|Ferry Steps;Cargo Rail;Harbor Office;Net Yard|
Silver Carp Market|-23|28|1-8|Fishmongers and vegetable sellers fill covered stalls. The best bargaining happens before the ice melts; a fish too big for its basket has become the morning attraction.|Fish Aisle;Produce Stalls;Covered Bench|
Three Reeds Inn|-33|-10|1-8|A lakeside inn hangs colorful travel coats beneath its eaves. The kitchen specializes in pepper broth and the host keeps a separate kettle for bad weather.|Welcome Porch;Common Room;Guest Landing;Kitchen Door|
Saionoma Household|14|22|1-20|A residential compound beside the castle has bright screens, a small archery yard and a kitchen famous for feeding more people than its accounts admit.|Receiving Veranda;Archery Yard;Kitchen Garden;Family Walk|
Reedwake Boatworks|40|-28|1-12|Boatwrights steam planks, mend hulls and keep an astonishing collection of borrowed tools. A partly rebuilt ferry waits under a roof weighted against the wind.|Slipway;Steam Shed;Tool Loft|
Western Spear Hall|-7|26|5-25|A practical martial hall teaches spear distance, escort work and fighting in narrow lanes. Loan staves stand beside a repair bench.|Practice Yard;Indoor Floor;Equipment Bench|
Reedshore Hamlet|40|29|1-10|Low cottages face gardens and the lake. Nets dry beside bean poles, and shared landings let neighbors reach one another without walking the whole shore.|Common Landing;Garden Lane;Smoking Shed|
Lakewatch Islet|6|-22|12-25|A small wooded islet holds a disused watch shrine. Boats can land on the sheltered side; the reed channels on the far shore conceal movement.|Sheltered Shore;Watch Shrine;Far Reeds|Reed-Jaw Kappa
''',
6: '''
Bamboo Crossing|-23|25|1-8|A bridge village sits where two bamboo roads meet. Food stalls and pack-animal rails make it an ordinary stopping place between the capital and west.|Bridge End;Food Awning;Pack Rail;Village Steps|
Green Thread Paperworks|-41|17|1-10|A family workshop makes writing paper, fans and sturdy weather slips. Pale sheets hang over water channels, and a ruined batch threatens a household contract.|Pulp Yard;Drying Walk;Cutting Room|Paper-Face Moth
Rainsong Mill|-21|12|1-8|A waterwheel turns under bamboo shade. Farmers queue with sacks while the miller tries to decide whether a new squeak is a bearing or a tenant.|Mill Door;Wheel Walk;Sack Store|Granary Rat
Hidden Reed Training Ground|26|39|10-28|A discreet training yard uses bamboo screens, water channels and raised targets. Students practice observation and quiet movement without turning every passerby into a target.|Screen Yard;Water Lane;Practice Shelter|
Riverglass Baths|14|-1|1-8|A village bathhouse draws warm water through stone-lined channels. A garden waiting court and private washing rooms give weary travelers an unhurried stop.|Garden Court;Changing Walk;Bath Hall|
Abandoned Bamboo Village|-30|37|15-28|Overgrown lanes lead through houses abandoned after repeated floods. A shrine roof survives above an empty storehouse, and someone has swept the doorstep recently.|Flood Lane;Storehouse;Swept Shrine|Cinder Umbrella,Paper-Face Lurker
Moonweave Grove|-9|36|20-32|Tall bamboo creaks in a wind that moves below the leaves. Braided cords mark the old gathering boundary and hollow stalks carry voices strangely far.|Cord Boundary;Hollow Stalks;Wind Pocket|Bamboo Fox,Whisper-Reed Oniwa
Bamboo Charcoal Camp|9|28|5-15|Earth kilns and rough shelters serve seasonal charcoal cutters. The crew keeps one fire small enough to cook on while the others smolder for days.|Cooking Fire;Earth Kilns;Wood Stack|
''',
7: '''
Benitsuru Transit Shrine|1|34|1-12|The authorized Evertree route opens inside a tiled shrine receiving hall. Vermilion beams frame a quiet transit torii; clerks handle permits beside a courtyard full of arriving travelers.|Portal Hall;Permit Desk;Receiving Court;Baggage Veranda|
Benitsuru Castle|-2|47|1-30|A terraced Shogunal castle rises toward Mount Shiun. Petitioners, household officers and military envoys share its outer court, while the lived-in residence stands behind controlled doors.|Petition Court;Council Hall;Garden Veranda;Residence Walk|
Adventurer's Guild - Benitsuru Branch|-13|23|1-15|The international Adventurer's Guild occupies a lively street hall near the transit road. Local notices share a board with foreign expeditions; the exam court is audible through a rear door.|Reception;Request Board;Common Tables;Assessment Court;Records Desk|
Lantern Canal Market|-9|29|1-12|Cloth, food, fans and river cargo fill the capital's canal market. Porters thread between customers while street performers claim the bridges one tune at a time.|Cloth Row;Food Bridge;Canal Steps;Parcel Arcade|
Benitsuru Magistracy|20|23|1-25|A public hearing compound receives complaints, petitions and testimony. Its clerks can explain procedure without promising a favorable ruling.|Public Desk;Hearing Room;Waiting Court;Records Room|
Red Maple Inn|0|3|1-10|A comfortable capital inn has a bright dining room, private rooms and a courtyard where travelers compare journeys. The host knows which stories were different yesterday.|Front Room;Dining Room;Guest Gallery;Courtyard|
Benitsuru Ward Clinic|-30|35|1-15|A public clinic treats ordinary injuries and magical mishaps. Herbal drying racks share space with clean bandages and plain examination screens.|Receiving Bench;Treatment Room;Herb Yard|
Kagetsuna Household|-22|25|1-25|The ruling household's city residence contains working offices, a practice court and a surprisingly unruly garden. Domestic staff keep it functioning through visitors and arguments.|Receiving Room;Garden Path;Practice Court;Service Court|
Eight Petals Theater|15|45|1-12|A small theater stages comic plays, dance and music. Costume repairs happen in the side passage, often while the audience is already arriving.|Ticket Porch;Audience Floor;Stage;Costume Walk|
Benitsuru Craft Quarter|30|31|1-20|Ordinary smiths, lacquerers and joiners share narrow workshop streets. One guarded importer works behind a plain gate; most doors open on familiar hand tools.|Smith Lane;Lacquer Court;Importer's Gate;Public Yard|
Morning Crane Dojo|13|21|3-25|A disciplined sword school teaches measured footwork and control. The owner welcomes earnest beginners but refuses to call expensive equipment a substitute for practice.|Practice Hall;Open Court;Loan Rack|
Canal Ward Homes|-31|23|1-12|Homes, shared wells, sewing rooms and a tiny tea stall fill a working residential ward. Neighbors know who borrows ladders and who returns them.|Shared Well;Home Lane;Tea Corner;Courtyard|
Benitsuru Public School|-38|1|1-12|A medium-sized school teaches letters, arithmetic, local history and basic mana safety. Its public evening lessons draw artisans as well as younger adults.|School Court;Evening Classroom;Supply Room|
South Gate Caravan Yard|41|17|1-15|A broad yard outside the gate serves carts and pack animals. Travelers can arrange escorts, buy road supplies and hear whether the bridges are open.|Gate Rail;Caravan Lines;Road Office;Feed Store|
''',
8: '''
Koganedai Castle|0|22|1-30|House Tsubakiri's hill castle looks across gold-leaved terraces and managed pine. Its outer hall hosts trade talks as often as military audiences.|Audience Court;Trade Hall;Terrace Walk;Guard Yard|
Tsubakiri Residence|22|18|1-30|A wealthy household occupies a garden compound behind the eastern market. Music lessons and family dinners continue beside arguments about foreign equipment.|Garden Room;Practice Veranda;Family Court;East Gate|
Goldleaf Arcade|9|-13|1-12|Lacquer, textiles and polished fittings catch the light beneath a long arcade. Buyers compare workmanship while apprentices carry bowls to nearby shops.|Lacquer Stalls;Cloth Walk;Tea Bench|
Ginkgo Crossbow Works|18|3|8-30|A guarded workshop assembles a limited number of imported magitech crossbows and sword mechanisms. Buyers need patience, money and an actual appointment.|Demonstration Yard;Receiving Desk;Assembly Room;Secure Store|
Koganedai Muster Ground|-14|-8|8-30|A broad practice ground outside town provides targets, lanes and formation space. Regular soldiers train beside a few sponsored equipment trials.|Archery Lane;Formation Field;Trial Shelter|
Terrace Waterworks|-31|21|1-12|Waterwheels, sluice gates and stepped channels distribute mountain water to the town and fields. A jammed gate can become everyone's problem by supper.|Upper Sluice;Wheel House;Lower Channel|
East Wind Archery Hall|27|-21|5-28|An archery school opens onto a long sheltered range. Its master insists that calm breathing matters more than a dramatic release.|Covered Range;Bow Room;Breathing Court|
Koganedai Guesthouse|9|15|1-12|A prosperous guesthouse serves eastern merchants and visiting craftspeople. Its courtyard contains more borrowed umbrellas than paying guests.|Reception;Dining Gallery;Guest Court|
Ginkgo Schoolhouse|1|0|1-10|A plain schoolhouse and public reading room stand under old ginkgo trees. Notices include lessons, repairs and a missing pet that has become a neighborhood joke.|Reading Room;School Yard;Notice Porch|
''',
9: '''
Mirror-Reed Bridge|-8|17|1-12|A red-lacquered timber bridge crosses a clear river between wooded banks. A path-keeper’s shelter and a broad waiting verge serve walkers, pack animals and the occasional small cart. Ferns hide the older footpath beneath the stone approach.|Woodland Approach;Bridge Span;Path-Keeper Shelter|
Reedglass Woodland Hamlet|43|24|1-12|A few timber homes occupy a sunny clearing above the river, linked by stone steps and garden paths. Firewood, cultivated mushrooms and baskets of herbs wait under deep eaves; the common yard hosts meals and loud card games.|Clearing Lane;Common Yard;Wood and Herb Store|
White Heron Grove|23|40|10-24|White birds nest in a stand of pale-barked trees above a shallow river bend. Smooth stones, old roots and pockets of reeds break the bank; the higher path stays within the trees.|Riverbank Path;Nesting Trees;Rooted Pool|Reed-Jaw Kappa,Whitefall Crane
Singing Cedar Hollow|28|2|15-28|A wind funnel carries wavering notes through a wooded hollow between rocky slopes. Strips of old trail cloth catch among cedar branches, and root hollows conceal the source of some replies.|Cedar Descent;Windfall Glade;Root Hollow|Moss-Tongue Kodama,Antler-Moss Boar
Old Bridge Shrine|-20|38|3-15|A small roadside shrine stands where an earlier footbridge met the wooded ridge path. Travelers leave repaired walking sandals and little carved charms beneath its eaves. An upright tanuki in a patched saffron coat is often inspecting something with immense self-importance.|Trail Approach;Charm Shelter;Shrine Steps|Moss-Tongue Kodama
Mossbank Ridgeway|10|-28|5-18|A maintained ridge path winds between moss-covered rocks and cedar trunks. Low stone walls stabilize the steeper bends, and small shelters mark sensible places to rest a load before the road reaches open grain country.|Ridge Approach;Rest Shelter;Southward Bend|Moss-Tongue Kodama
Woodland Dye Workshop|-30|-29|1-10|A timber workshop and drying yard sit beside a clean stream below the trees. Aya Takino steeps bark, roots and gathered leaves into vivid dyes; cloth bundles arrive by pack trail, and the rinsing channel turns a different color with each batch.|Dye Yard;Cloth Racks;Ledger Bench|
''',
10: '''
Hoshina Village|5|21|1-8|A farming village surrounds a grain yard, gardens and a small roadside shrine. The fields support ordinary lives whose disagreements rarely need a sword.|Grain Yard;Garden Lane;Shrine Corner;Well Court|
Golden Sheaf Granary|-30|28|1-10|A public granary keeps measured stores for winter and bad harvests. Its keeper takes damaged sacks personally and gives hungry visitors directions before a lecture.|Loading Porch;Sack Hall;Tally Room|Granary Rat
South River Bridge|25|45|1-12|A broad bridge carries the southern road over the river. A repair crew occupies one lane while travelers debate whether they can fit a wider cart through.|Near Toll Shelter;Repair Span;Far Bank|
Goldfinch Orchard|37|22|1-10|An orchard and honey yard produce fruit, wax and loudly disputed preserves. Visitors can arrange seasonal work or buy a basket for the road.|Fruit Rows;Packing Shed;Bee Yard|Orchard Sootling
Susuki Road|-5|32|3-12|White grass borders a road through broad grain country. The view makes approaching carts easy to see, but a neglected side path leads toward empty fields.|Road Verge;Traveler's Shelter;Grass Path|Bamboo Fox
Low Meadow Paddies|22|7|1-12|Irrigated paddies are divided by raised footpaths and small gates. Water theft and blocked channels can cause more trouble than the creatures hunting frogs.|Raised Walk;Water Gate;Tool Shelter|Paddy Mudling
Saffron Road Hostel|29|-31|1-10|A plain hostel offers stew, a bedroll space and secure pack hooks. Farmhands and wandering adventurers share the common room without agreeing on much.|Common Room;Sleeping Gallery;Pack Yard|
''',
11: '''
Redleaf Bridge|-48|10|3-15|A long bridge joins maple-red riverbanks. Tea sellers wait at each end, and pilgrims stop in its sheltered middle to watch the water.|West Approach;Covered Span;East Approach|Lantern Prowler
Evening Maple Shrine|-1|11|1-12|A lively shrine hosts ordinary petitions, seasonal gatherings and practical lessons in tending a spirit boundary. The keeper has set aside a bell needing only a little local help.|Offering Court;Bell Workshop;Cedar Steps;Guest Veranda|
Redleaf Guest Village|-27|1|1-12|Guesthouses and small gardens line a pilgrim road. Locals know how to dry a soaked travel cloak and exactly which host watered yesterday's soup.|Village Street;Shared Garden;Guest Porch|
Paper Moon Pavilion|12|-12|5-20|An old festival pavilion overlooks a river bend. Performers still use its covered floor, though some of the stored masks have become strangely hard to count.|Covered Floor;Mask Store;River Steps|Cinder Umbrella,Paper-Face Lurker
Foxfire Verge|30|-31|22-38|The maintained road ends at a maple-and-cedar boundary. Ragged cloth strips hang above an abandoned rest bench, and sharp joint-like cracks sometimes answer footsteps.|Last Rest Bench;Cloth Strips;Cedar Track|Lantern Prowler
Broken Kite Camp|24|-14|12-25|A disreputable camp occupies an old roadside enclosure. Cooking smoke, stolen pennants and badly patched tents make its residents easier to find than they believe.|Outer Track;Cooking Yard;Tent Row|
Redleaf Apiculture|-41|-4|1-12|Hives stand beneath flowering trees beside a wax workshop. The keeper sells candles and is quite tired of visitors treating bees as a free spectacle.|Hive Walk;Wax Room;Packing Porch|Orchard Sootling
River Lantern Mooring|28|32|3-18|A small mooring serves shrine cargo and festival boats. Spare lantern frames hang above a dry work area with a kettle that never quite boils evenly.|Cargo Steps;Lantern Shed;Boat Bench|
''',
12: '''
Moonless Torii|22|-4|1-12|A dark stone torii stands among enormous cedar roots above a clear lower trail. A weathered bell hook faces an empty space between its uprights; an ordinary shrine path leads back toward Redleaf.|Gate Steps;Torii Court;Return Trail|
Lanternwood Root Shrine|-26|34|5-18|A small shrine occupies a living root arch. Travelers leave lamps inside deep niches, and the caretaker keeps the lower route clear.|Lamp Court;Root Veranda;Side Hollow|Moss-Tongue Kodama
Ragged Cedar Hollow|31|7|32-45|A tall hollow between ancient trunks is littered with torn cloth and broken animal bones. Snapping sounds move from tree to tree above ordinary sightlines.|Cloth Clearing;High Roots;Hollow Center|Paper-Face Lurker
Old Mask Trail|19|13|28-42|An abandoned trail winds between hanging roots and empty mask niches. Its far turn is hidden by a steep wall of ferns.|Niche Walk;Blind Turn;Fern Escape|Lantern Prowler
Rootfall Ravine|-11|-37|24-38|Water falls through a narrow ravine roofed by roots. The upper path is usable; the lower stones require care and carry fresh claw marks.|Upper Walk;Water Shelf;Lower Stones|Root-Back Nue
Lanternwood Field Shelter|-5|-9|5-18|A small attended shelter marks the last reliable bed and supply stop on the lower forest approach. Its bell sounds toward the road when visibility closes.|Stove Room;Supply Porch;Bell Rail|
Foxglade Spirit Orchard|4|41|18-30|Old fruit trees grow in a cedar clearing where no household claims the harvest. Small wooden bowls sit at the roots, some newly filled.|Orchard Edge;Bowl Trees;Rear Clearing|Bamboo Fox,Orchard Sootling
Hushwater Pool|14|26|20-35|A dark pool lies under an overhanging stone face. Ripples continue after the wind stops; a shallow gravel shelf offers a safe place to observe before approaching.|Gravel Shelf;Stone Overhang;Pool Rim|Reed-Jaw Kappa,Whisper-Reed Oniwa
'''
}

SPIRIT_SITES = '''
Veiled Threshold|-38|-29|1-12|Mist parts around a stone torii on a raised patch of dry ground. The opening shows the cedar court in Akitsuhara, and a line of white stones marks a nearby shelter.|Return Torii;White-Stone Path;Dry Shelter|
Bellroot Refuge|-33|16|5-18|An immense root shelters a little dry platform above the fog. Old bells hang under its arch, and careful guests can rest without stepping into the surrounding pools.|Root Platform;Bell Hooks;Covered Rest|
Pale Lantern Marsh|24|-23|18-30|Blue-white lights drift above a marsh with black reeds and pale flowers. Some lights move against the wind; raised roots offer a real route between pools.|Root Causeway;Lantern Pool;Reed Island|Mist-Lure Wisp,Marsh-Stilt Haunt
The Listening Cedars|-36|40|20-35|Huge cedar silhouettes vanish upward into mist. Unfamiliar voices use recognizable cadences, and the roots hold objects carried here by the water.|Root Entrance;Listening Hollow;High Footpath|Echo-Hide Stalker,Moss-Tongue Kodama
Ashen Festival Road|4|4|20-35|A road of dark stone passes broken festival frames and empty stalls. Tall shapes stand beyond the lanterns, moving when the road turns out of sight.|Old Stalls;Lantern Crossing;Broken Stage|Empty Festival Husk,Cinder Umbrella
Crane-of-the-Hush Crossing|2|26|15-30|A pale stream cuts the fog beneath a broad stone crossing. A great white shape waits in the reeds without revealing whether it guards or simply watches.|Near Bank;Stone Crossing;Reed Pavilion|Whitefall Crane
Hollow Sky Grove|35|33|30-42|A grove of enormous pale trees encloses a patch of sky that never becomes fully clear. Fallen branches reveal dark cavities in the ground, and distant footfalls circle the outer roots.|Outer Roots;Hollow Trees;Sky Clearing|Root-Back Nue,Echo-Hide Stalker
'''

AREA_DETAILS = {
 'Portal Hall':'A vermilion transit torii stands on a dry tiled floor. Paper screens frame the capital courtyard; the fixed return passage leads to Evertree Base - Portal Room. Travelers can wait, arrange permitted transit or leave for the city.',
 'Permit Desk':'An attended counter handles authorized route keys, manifests and visitors. A window looks directly onto the transit floor; waiting passengers can ask about actual permitted routes.',
 'Request Board':'Bronze through Platinum tabs divide local postings and foreign field contracts. A low reading shelf lets visitors compare work without blocking the hall.',
 'Reception':'A bright counter has worn elbow rests, a vase of seasonal flowers and a small stack of disputed expense slips. The clerk handles licensing records, directions and actual requests.',
 'Assessment Court':'A rear court contains padded posts, movable obstacles and a clear demonstration lane. Applicants can demonstrate their actual practical abilities under supervision.',
 'Council Hall':'Maps, petition bundles and plain cushions fill a working hall. Officials attend to current decisions; doors and attendants separate it from private household rooms.',
 'Torii Court':'Moss borders the torii uprights and an old bell hook. The space between the stones is quiet until the restored way bell is sounded here.',
 'Return Torii':'The stable torii opening leads directly back to Moonless Torii - Torii Court in Akitsuhara. Its dry stone approach remains visible through the nearest fog.',
 'Hollow Center':'The cedar trunks leave a high, narrow space where an unnaturally tall body can unfold. Two low root gaps lead back toward the trail.',
 'Bell Workshop':'Bell molds, repair cords and a padded work tray occupy a sheltered bench. A small damaged way bell awaits its missing clapper.',
 'Secure Store':'Locked cases hold actual commissioned mechanisms and carefully counted components. Entry is controlled by the workshop staff.',
 'Assembly Room':'Bench clamps, crystal housings and disassembled bow mechanisms show a few expensive imported devices under repair. No row of mass-produced weapons fills the room.'
}

SITES[7] += '\nHinoki Hollow Onsen|34|-45|1-12|Warm mineral water rises beneath a low cypress bathhouse at the wooded edge of Benitsuru. A covered washing court, small quiet pools and a garden rest veranda offer a break from the capital. A basic bath and clean towel cost 6 marks.|Reception Porch;Washing Court;Stone Pools;Rest Veranda|\n'
