"""Authored fishing content. No runtime schema extensions or external dependencies."""

# name, habitats, selection weight, favored weather, length cm, price, description
FISH = [
 ('Pinewater Perch','r',30,'clear',12,30,3,'An olive-backed river fish with copper bars and a stubbornly raised dorsal fin. Good pan-fried with herbs.'),
 ('Brookmeadow Roach','r',32,'overcast',8,22,2,'A silver river fish with orange fins. Brookmeadow cooks flour the smaller ones and fry them crisp.'),
 ('Millpond Crucian','r',25,'rain',12,32,3,'A deep-bodied bronze fish that feeds near quiet banks. Its muddy-looking scales hide delicate flesh.'),
 ('Willowback Trout','r',20,'overcast',18,42,5,'A spotted trout with a green sheen along its back. It favors cool running water and makes excellent supper.'),
 ('Button-Eyed Minnow','r',35,'clear',4,10,1,'A tiny schooling fish with round dark eyes. More impressive as a living flash of silver than as a meal.'),
 ('Rainbell Loach','re',23,'rain',8,20,3,'A whiskered bottom-feeder that makes a faint clicking sound when wet stones touch its scales.'),
 ('Reedstripe Mullet','eh',28,'overcast',15,38,3,'A striped estuary fish that noses through soft sediment. Usually smoked or cooked in a strong broth.'),
 ('Brackish Bream','e',27,'rain',16,35,4,'A pale bream with a faint green edge to each scale. Its feeding grounds move with the river mouth.'),
 ('Mud-Sleeve Goby','eh',33,'overcast',5,16,1,'A mottled little fish with oversized pectoral fins, forever looking as though it has lost its sleeves.'),
 ('Greenrush Flounder','es',23,'fog',15,37,4,'A flat fish with leaflike mottling. It lies almost invisible against sand and is prized for a simple butter fry.'),
 ('Harbor Herring','hs',35,'overcast',14,27,2,'A bright-sided schooling fish, familiar to harbor cooks, gulls and anyone who has carried an unsealed basket.'),
 ('Lantern Sardine','hs',35,'clear',8,18,2,'A small oily fish with a gold spot beside each gill. Its lantern name comes from reflected light.'),
 ('Dockside Smelt','h',30,'rain',7,17,2,'A translucent harbor fish with a clean cucumber scent. Best eaten fresh and cooked thoroughly.'),
 ('Copper-Gill Mackerel','hsd',28,'wind',22,43,4,'A strong swimmer with blue markings and copper-red gill covers. Its meat is rich and oily.'),
 ('Whitecrest Whiting','hs',28,'clear',18,36,3,'A pale coastal fish with a long soft body. Fishmongers like its mild flesh and lack of fuss.'),
 ('Pebble Sole','s',24,'clear',12,29,4,'A compact flatfish patterned like a handful of shore pebbles. It favors quiet sandy pockets.'),
 ('Ribbon Garfish','sd',22,'wind',30,65,5,'A narrow green-backed fish with a needlelike snout. Its bones turn a startling blue-green when cooked.'),
 ('Crescent Sea Bass','hsd',19,'overcast',25,62,6,'A thick coastal hunter with a crescent mark behind the eye. A fine meal, if landed before it finds cover.'),
 ('Silver-Tail Pollock','sd',25,'overcast',25,55,4,'A useful sea fish with a sharply forked silver tail. Often salted aboard working boats.'),
 ('Sandburrow Gurnard','s',22,'clear',18,38,4,'A broad-headed fish with fanlike fins. Its ungainly appearance has never troubled a good cook.'),
 ('Glassvein Char','r',8,'clear',22,48,9,'A cool-water char whose fine scales show branching silver lines. The pattern fades after preservation.'),
 ('Bottle-Green Tench','re',9,'rain',25,52,7,'A smooth, heavy fish with a bottle-green back and tiny red eyes. It tests patience more than strength.'),
 ('Amberfin Eel','re',7,'rain',35,85,9,'A gold-finned eel that slips through flooded roots. Its shed slime is useful in ordinary waterproofing mixtures.'),
 ('Pearlspot Wrasse','s',9,'clear',15,32,8,'A colorful reef fish with pearly spots. Some collectors prefer a careful sketch and its release to a sale.'),
 ('Blueglass Needlefish','sd',8,'wind',35,78,10,'A nearly transparent blue fish that vanishes against open water. Its reflective scales interest pigment makers.'),
 ('Velvet Skate','sd',7,'fog',35,80,11,'A soft gray skate with dark velvet patches on its wings. Handle gently and keep clear of the tail.'),
 ('Stormstripe Bonito','d',8,'wind',40,90,12,'A powerful striped sea fish that hunts beneath wind-ruffled water. Fresh slices are a ship cook’s luxury.'),
 ('Moonmirror Dace','re',2,'fog',18,34,24,'A scarce silver dace whose scales reflect a second, slightly displaced moon. The effect is beautiful and brief.'),
 ('Lanternjaw Angler','d',2,'fog',35,70,30,'A deepwater fish with a blue lure over its jaws. An intact lure is a curious alchemical specimen, not a ready-made lamp.'),
 ('Crownfin Sailfish','d',2,'wind',95,180,38,'A rare open-water fish with a sweeping golden dorsal crest. Its first run can empty a careless angler’s spool.'),
]

# Actual nested area IDs, never whole islands/buildings merely near water.
SITES = {
 'Pinewater River - Brookmeadow Ford': 'r',
 'Pinewater River - River Bend': 'r',
 'Saltmere - Village Landing': 'h',
 'Saltmere - Shoreline Green': 's',
 'Whitecrest Harbor - Harbor Quay': 'h',
 'Whitecrest Harbor - Passenger Landing': 'h',
 'Driftstone Isle - Island Landing': 's',
 'Driftstone Isle - Rocky Shore': 's',
 'Pinewake Coast - Pineward Beach': 's',
 'Pinewake Coast - Tide Pools': 's',
 'The Gilded Albatross - Main Deck': 'd',
 'Moonarch Isle - Pebble Landing': 's',
 'Moonarch Isle - Offshore Drop': 'd',
 'Stillback Isle - Quiet Landing': 's',
 'Greenrush Estuary - Skiff Landing': 'e',
 'Greenrush Estuary - Reedwalk': 'e',
 'Gullwatch Reefs - Boat Shelf': 's',
 'Gullwatch Reefs - Tide Pools': 's',
}

GEAR = [
 ('Angler’s Rod','Tool','mundane',12,'tool',None,'A springy ash rod with a small reel, hook, float and reusable plain spinner. Suitable for river, shore or boat fishing; bait is optional. Dry the fittings after salt water.'),
 ('Angler’s Bait Portion','Consumable','mundane',1,None,None,'One wrapped portion of worms, grubs and prepared paste. Enough to bait a single cast. It attracts bottom-feeding fish and gives patient fish more reason to bite.'),
 ('Painted Willow Lure','Tool','mundane',18,'tool',('Fishing',1),'A hand-painted reusable lure with a leaf-shaped blade. It catches the light with a gentle wobble.'),
 ('Tideglass Spinner','Tool','artisan',65,'tool',('Fishing',3),'An articulated blue-glass spinner balanced for coastal water. Small replaceable links keep it moving without a violent splash.'),
 ('Rainbell Float','Tool','mundane',14,'tool',('Perception',1),'A striped cork float with a tiny brass bell. Useful for noticing a quiet bite when rain dims the surface.'),
 ('Angler’s Finger Guards','Armor','mundane',16,'hands',('Fishing',1),'Soft leather guards protect the fingers handling line. They leave the fingertips free to feel a change in tension.'),
 ('Reed-Woven Creel','Tool','mundane',10,None,None,'A ventilated basket for carrying a modest catch. Wet reeds keep fish cool for a short walk; it is no substitute for preservation.'),
 ('Saltproof Line Spool','Tool','mundane',8,None,None,'A spare length of treated braided line, neatly wound and waxed against salt. Useful for an actual replacement or repair.'),
 ('Angler’s Field Ledger','Document','mundane',6,None,None,'Blank waterproofed pages for sketches, lengths, weather notes and fishing grounds, with a small ruler printed along the cover.'),
 ('Pocket Fish Measure','Tool','mundane',5,None,None,'A folding marked rule and a soft sling for measuring a catch without laying it on hot stone.'),
 ('Smoke-Salt Packet','Tool','mundane',4,None,None,'A small packet of curing salt and aromatic wood shavings. Enough for a little catch, with proper preparation and drying.'),
]

# Ordinary shared catches remain available even when a realm has no profile.
# Existing Glowhaven species retain their authored identity and values.
# Same fish fields as FISH, followed by a compact realm-pool code.
EXTRA_FISH = [
 ('Common Silverfin','rehsdu',65,'overcast',8,24,2,'A small silver-scaled fish found in many ordinary waters. Its mild flesh suits a simple supper.','*'),
 ('Pebblefin Darter','rs',24,'clear',6,16,2,'A quick little fish with mottled fins, often found between clean stones in shallows.','*'),
 ('Rushfin Mudfish','re',24,'rain',12,30,3,'A blunt-headed fish with russet fins. It hides among roots and feeds where the bottom is soft.','*'),
 ('Pale Water Eel','rehs',9,'rain',28,70,7,'A pale-bellied eel that tolerates a change in salinity. It is best handled carefully and cooked thoroughly.','*'),
 ('Tidemark Runner','ehsd',22,'wind',18,42,4,'A lean blue-backed fish whose sides carry a dark line like a water stain. Useful fresh or salted.','*'),
 ('Wandering Prismfin','rehsdu',2,'fog',15,32,23,'A scarce adaptable fish whose fins separate reflected light into faint bands of color. Its beauty survives best in the water.','*'),
 ('Glassmere Char','r',26,'clear',20,48,6,'A cold-water char with copper spots and a slate-blue back. Mountain cooks roast it with hardy herbs.','d'),
 ('Rimefin Whitefish','r',30,'overcast',18,42,4,'A pale alpine fish with translucent fins. It gathers in the deeper water beneath cold lake surfaces.','d'),
 ('Copperwhisker Sculpin','r',22,'rain',7,20,3,'A broad-headed stream fish with copper-colored barbels and a knack for wedging beneath stones.','d'),
 ('Snowmelt Grayling','r',20,'clear',20,45,6,'A mountain fish with a tall, blue-violet dorsal fin. It favors clean running meltwater.','d'),
 ('Amberheart Burbot','r',2,'fog',38,80,28,'A rare alpine burbot with a warm amber gleam beneath its throat. The gleam fades naturally; it is no stored mana crystal.','d'),
 ('Cloudscale Carp','r',28,'overcast',20,48,5,'A sky-island carp with irregular white patches over blue-gray scales. It feeds patiently in still fresh water.','a'),
 ('Petalwash Loach','r',25,'rain',8,22,4,'A small loach whose pink-edged scales resemble damp petals. It noses through the silt beneath flowering banks.','a'),
 ('Rainthread Minnow','r',32,'rain',5,13,2,'A tiny fish with long threadlike fin tips, flashing silver as rain dimples the surface above it.','a'),
 ('Violetfin Gourami','r',14,'clear',12,28,8,'A violet-finned fish that builds delicate bubble nests among sheltered reeds. Naturalists sketch the nests before disturbing them.','a'),
 ('Horizon Koi','r',2,'fog',30,65,27,'A rare koi whose blue-gold flank seems to carry a distant horizon. It swims through water and has no gift for flight.','a'),
 ('Sakura Ayu','r',28,'clear',12,27,4,'A slender river fish with a cherry-pink flush beside its gills. Grilled whole, it has a clean herbal fragrance.','k'),
 ('Goldleaf Carp','r',26,'overcast',22,52,5,'A sturdy carp with leaf-shaped gold markings. The color belongs to its scales, not to precious metal.','k'),
 ('Bamboo Loach','r',27,'rain',9,23,3,'A striped loach that shelters among submerged roots and the shadows of bamboo banks.','k'),
 ('Redleaf Salmon','r',16,'rain',30,68,8,'A strong river fish with red-brown flanks and a silver belly. Its rich flesh is often salted for journeys.','k'),
 ('Moonbell Koi','r',2,'fog',28,62,26,'A rare pale koi with dark crescent markings. As it turns beneath still water, its scales make a faint bell-like shimmer.','k'),
]

REALM_CODES = {'Glowhaven':'g','Drakenspire Mountains':'d',
               'Asterveil Sky Archipelago':'a','Akitsuhara':'k'}

def runtime_fish():
    return [[r[0],r[1],r[2],r[3],r[4],r[5],'g'] for r in FISH]+[
        [r[0],r[1],r[2],r[3],r[4],r[5],r[8]] for r in EXTRA_FISH]
