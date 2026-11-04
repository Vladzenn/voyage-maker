"""Build a text-only, data-grounded Glowhaven map brief; never reads old artwork."""
from __future__ import annotations
import csv
import hashlib
import json
import pathlib
import shutil
from xml.sax.saxutils import escape

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle,
)
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
WORLD = ROOT / 'world-draft/WorldAlpha - World.json'
OUT = ROOT / 'output/pdf'
SHARED = ROOT / 'world-draft/authoring/plans'
PDF_NAME = 'Glowhaven - Fresh Map Brief.pdf'
MD_NAME = 'Glowhaven - Fresh Map Brief.md'
TEAL = colors.HexColor('#145A63')
INK = colors.HexColor('#172E3A')
MUTED = colors.HexColor('#526773')
LIGHT = colors.HexColor('#EDF4F4')
GOLD = colors.HexColor('#B88C47')


def norm(text):
    return (str(text).replace('\u2011', '-').replace('\u2013', '-')
            .replace('\u2014', ' - ').replace('\u00a0', ' '))


OVERVIEW = [
    ('Purpose', 'Create a fresh illustrated regional map of Glowhaven using this document as the complete spatial and architectural reference. No previous map image is supplied, quoted, embedded or required. Keep the existing places and their relative anchors, while designing new coherent buildings, streets, landforms and visual treatment.'),
    ('The place', 'Glowhaven is an independent, prosperous center of magical education and craft. One great walled city shares its territory with modest villages, working farms, western wooded hills, river country, eastern coastal settlements and offshore islands. It is a lived-in country, with many ordinary homes and workplaces between the named institutions.'),
    ('The central landmark', 'The Evertree rises from the ground beside the northern civic precinct, behind the court approaches. Its living trunk and canopy are the main magical silhouette. The court, Sage\'s Spire and rootward grounds form a close group, but they are not interchangeable buildings. The portal hub is beneath the rootward structures; distant realms do not occupy extra land on this map.'),
    ('Composition', 'Use a horizontal 5:4 canvas corresponding to five columns and four rows of square regions. North is up. The city occupies much of the upper-left and upper-middle landscape. Working harbor and shoreline open toward the eastern sea; the bottom half becomes increasingly rural. The whole map is one continuous landscape, not twenty unrelated illustrations.'),
    ('What makes it large', 'The city must read as a major settlement containing dense blocks of ordinary roofs, several different residential textures, workshops, institutions and multiple campuses. Rural houses are the same physical size as comparable city houses. Fields, woodland, meadows, water and distance provide scale. Do not make a cottage huge simply to make it recognizable at first glance.'),
    ('How to use the catalogue', 'All 82 current location records are included. A location can represent a neighborhood, street, river corridor, village, ship or building complex. Its internal areas are parts of that site, not additional freestanding landmarks. Some small addresses will become distinguishable only after the master is cropped and refined.'),
]

SCALE = [
    ('View', 'A high oblique aerial view with a consistent ground-plane registration. Roofs dominate, but enough wall faces remain to distinguish buildings. Avoid a foreground panorama in which the southern cottage appears larger than a northern city block. A shallow camera, huge sky band or strong foreground enlargement defeats the requested scale.'),
    ('Ordinary buildings', 'Proposed master-scale budget: a typical house or shop is about 0.10-0.22% of total canvas width. On a hypothetical 5000-pixel-wide composite, that is approximately 5-11 pixels. This is an art-direction example, not a promised native generation size or a real-world measurement.'),
    ('Institutions', 'A public hall may be about 0.4-0.8% of master width; a multi-building academy precinct about 2-3%; the great arena about 1.5-2.2%. These are aggregate footprints, not a rule to enlarge every roof within a campus. Retain enough space between nearby landmarks.'),
    ('The tree', 'A proposed Evertree canopy width of roughly 4-6% of the master keeps it exceptional without swallowing the city. Its crown and height are above-ground mass; its exact anchor refers to the ground-level base, not the top of the canopy. Its final size should be judged against the adjacent court and city, rather than fixed by pixels alone.'),
    ('Rural restraint', 'Most countryside is landscape. A village is a small group of normal-sized roofs; an outpost is a yard and a few structures. Towers, ruins, mills and the abbey are limited accents. Large meadows and woods are intentional. Do not fill empty space with new stone circles, castles, ruins or identical decorative cabins.'),
    ('Road character', 'City paving ends at the appropriate gates. Country routes become narrow dirt or cart tracks, with lesser paths fading into working land. Bridges reach both banks. Keep the main avenue readable, but avoid a broad paved highway cutting through all the southern plains.'),
    ('Detail', 'Build small structures from coherent footprints, roof planes, walls and access. Do not simulate detail with noise, random greebles, melted roofs or sharpening halos. In later close crops, invent credible construction from the written role instead of reproducing blurry master-image marks.'),
    ('Interpretation', 'Coordinates, names, area membership and described functions are data facts. Unspecified roof pitches, stone colors, timber details and minor yard arrangements are proposed visual interpretations. They may vary consistently across the new design. Do not treat those proposed finishes as newly established world lore.'),
]

TOPOLOGY = [
    'City structure: connect West City Gate, East City Gate and Main City Gate with one coherent wall circuit. The exact wall outline and secondary street plan may be newly designed around the supplied anchors. Do not duplicate the city or place a separate wall around every neighborhood.',
    'Civic route: the Main City Gate leads along the Grand Approach to Four Sages Bazaar; the Grand Ascent then climbs toward the palace forecourt. The source positions form a diagonal axis on the page. "North" in a broad street description need not mean a perfectly vertical drawn road.',
    'Western setting: wooded ridges, an old keep, a modest hot spring and lowland water country surround the western and northwestern approaches. The mountains and forests are not densely packed with settlements. Distant northern high ground is a permissible background interpretation, not a new traversable region.',
    'Water system: keep Pinewater as a continuous valley river corridor and give the southern settlements workable crossings. Connect the lower water country plausibly toward Greenrush Estuary on the eastern edge. Tributaries are preferable to a channel forced through buildings or climbing a bluff. The source does not specify every bend or a complete drainage survey.',
    'Coast: Whitecrest Harbor, Pebblewick and Crescent Shores form different sections of the same settled eastern coast. Beaconrest Lighthouse is offshore. Clovermead remains boat-accessed across northern water; do not add a mainland road connection to it.',
    'Islands: Saltmere, Driftstone Isle and the smaller isolated Wraith Island are distinct. Reefs, Moonarch Isle, Stillback Isle and the wreck add a few secondary offshore shapes. Preserve visible water gaps. Do not turn all coastal sites into one giant island or a chain of causeways.',
    'Southern country: Longgrass Meadows and Sunmead Plain have no named location records. Keep them as substantial open grassland and pasture with only modest unnamed rural texture. Brookmeadow remains a small southeastern farming settlement; the not-yet-implemented port is not part of this brief.',
]

PROMPT = '''Create one fresh, continuous illustrated regional map of Glowhaven from this brief. Use a horizontal 5:4 composition with north up. The twenty named regions form five columns and four rows; their boundaries are invisible in the finished artwork. Follow the percentage anchors in the catalogue for named locations and preserve the broad relationships between coast, islands, city, hills, rivers, villages and open country.

Glowhaven is a great walled magical city in a larger working landscape. Fill the city with dense, human-scale roof groups and varied residential, civic and craft districts. Place the rooted Evertree behind the northern court precinct as the principal magical landmark. Keep the court, its office tower and residential manor distinct. Arrange the main gate, great avenue, founders' market and palace stair as one connected civic route. Include the four separate academy campuses, with red, cyan, violet and gold identifying details, plus the great arena and working harbor.

Buildings must be tiny relative to the complete territory. A rural house is not larger than a comparable city house. Most minor shops need only a logical frontage within a city block at this stage. Do not enlarge every named location into a showcase monument. Keep modest villages, fields, thin dirt roads, western woods and broad southern meadows. Use the eastern sea for genuinely separated inhabited islands, a small prison island, a lighthouse rock, low reefs, a broken-arch isle, a wreck and an anchored sailing ship.

Use richly colored 2D fantasy environment illustration with controlled painterly light, deliberate contours, clear roof planes and consistent aerial perspective. Choose a fresh architectural interpretation within the written world facts. Build terrain as connected ridges, valleys, banks and grouped tree masses. Keep water quiet enough to read the coast. Show a world with practical work and ordinary life, not a display of equally enormous castles. Do not add random ruins or giant decorative statues to fill empty ground.

This is a master composition for later cropped refinement. Design legible silhouettes and believable tiny footprints now; do not make low-resolution texture sacred. Small roofs, yards and structural details can be reconstructed intelligently in later close crops. Preserve the placement, scale, access and identity of each site when refining it.

Deliver clean map artwork only. Do not print this document's names, numbers, coordinate grid, labels, pins, borders, UI, captions or legend. Do not draw indoor rooms as exterior destinations. Other realms and Shadowspire's private realm are not extra islands in Glowhaven. The reef and turtle habitats can be shown without fixing their residents into the background; any optional creature sighting must remain small and secondary. The kraken is mobile, not a new fixed fortress or island. Read the regional catalogue before deciding the final composition.'''

FLAGS = [
    ('Positions are graphic anchors', 'The current world uses regionSize 100 and local coordinates from -50 to +50. Positive y is north. The master percentages below retain the whole 5-by-4 grid; they are not rescaled to the occupied pin cluster. They locate ground-level anchors and do not prescribe physical building size.'),
    ('Names that sound similar', 'Pebbletown is southwest of the city; Pebblewick is the small eastern coastal town; Brookmeadow is far southeast. Clovermead is a northern farming settlement reached by boat. They are four different settlements. West and East Greyfield are the adjoining poor settlement outside the southern city walls.'),
    ('Cross-border sites', 'Seabreeze Inn is in the Crescent Coast region but belongs to Pebblewick across the region boundary. Stargarden Manor is near the boundary beside the civic district. Thistlebank Alchemy Cottage is exactly on a tile edge, Hermit\'s hut is on a southern tile edge, and Longgrass Crossroads is almost on a northern edge. These are not duplicate sites or reasons to interrupt paths.'),
    ('Broad descriptions versus pins', 'The Winding Lowlands is described as remote rural water country, but its current anchor is in the northwest region. Follow that anchor for this brief; keep the settlement tiny. The current Shadowspire pin is at the northeastern side of Greenfield Farmlands, not in the far southern corner. No old map composition overrides these current values.'),
    ('Linear and areal places', 'The Grand Approach, Grand Ascent, Merchant\'s Row, Pinewater River, beaches, farms, woods and neighborhoods extend away from their pins. Design a continuous route or area that includes the anchor, rather than shrinking an entire river or district into a circular marker.'),
    ('Separate realms', 'Wraith Island is the coastal landing and approach visible here; the prison interior has its own playable realm. Evertree portals go to distant regions rather than creating another academy portal on the landscape. Shadowspire\'s private realm lies beyond a cellar gate, not behind the tower as eight more exterior castles.'),
    ('Living creatures', 'Nerathyl sleeps at the fixed Bluecoil reef; Mauruun is the passive giant turtle associated with Stillback; Ghorvath is a roaming kraken. Their habitats and deepwater routes matter. A static background is not proof of their current life, defeat or position, so optional sightings must not create duplicate bosses.'),
]

REFINEMENT = [
    ('First image', 'Generate the complete landscape once. Check coast continuity, the three wall gates, the civic axis, all four campuses, major island separation, open southern country and the tiny building scale before spending effort on individual windows.'),
    ('Split from one master', 'For square region crops, split five across and four down. Core bounds are A-E = 0-20, 20-40, 40-60, 60-80 and 80-100% across; rows 1-4 = 0-25, 25-50, 50-75 and 75-100% down. Use the original master for every crop rather than recursively cropping previous crops.'),
    ('Supply context', 'When refining one part, provide the accepted whole master, the target crop and this PDF\'s matching region entry. Include adjacent edge context. An overlap around 10-15% of a tile\'s width is a starting production choice; explicitly record core and overlap bounds.'),
    ('Rebuild detail', 'Reconstruct tiny buildings from their purpose, placement and footprint. Sharpen coherent roofs, entrances, bridges, courtyards and terrain forms. Do not turn blurred pixels into sacred architectural facts, move ground anchors, enlarge rural buildings, add unsolicited landmarks or change the camera.'),
    ('Seams', 'Match roads, riverbanks, wall segments, coastlines and lighting across every shared strip. Generative refinement cannot guarantee pixel-identical edges. Align and blend in Photoshop using masks or soft erasing, preserving the intended shared geography.'),
    ('Final pass', 'Check the assembled result at whole-map scale and at native crop scale. Tiny shops may remain subtle; they should not be inflated to make their identity readable in a thumbnail. High resolution means credible extra structure, not arbitrary texture or an automatically upscaled image.'),
]


def read_data():
    raw = WORLD.read_bytes()
    world = json.loads(raw.decode('utf-8-sig'))
    region_size = world['locationSettings']['regionSize']
    regions = {k: v for k, v in world['regions'].items() if v.get('realm') == 'Glowhaven'}
    xs = sorted({r['x'] for r in regions.values()})
    ys = sorted({r['y'] for r in regions.values()}, reverse=True)
    assert len(regions) == 20 and len(xs) == 5 and len(ys) == 4
    assert set((r['x'], r['y']) for r in regions.values()) == {(x, y) for x in xs for y in ys}
    descriptions = {}
    for line in (HERE / 'landmarks.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        name, role, visual, note = line.split('|')
        assert name not in descriptions
        descriptions[name] = dict(role=role, visual=visual, note=note)
    records = []
    for name, region in sorted(regions.items(), key=lambda kv: (-kv[1]['y'], kv[1]['x'])):
        col, row = xs.index(region['x']), ys.index(region['y'])
        tile = chr(65 + col) + str(row + 1)
        local = [(k, v) for k, v in world['locations'].items() if v.get('region') == name]
        sites = []
        for key, loc in sorted(local, key=lambda kv: (-kv[1]['y'], kv[1]['x'])):
            assert key in descriptions, 'Missing visual interpretation: ' + key
            x = 100 * (col + .5 + loc['x'] / region_size) / len(xs)
            y = 100 * (row + .5 - loc['y'] / region_size) / len(ys)
            assert 0 <= x <= 100 and 0 <= y <= 100
            site = dict(name=key, tile=tile, region=name, localX=loc['x'], localY=loc['y'],
                        masterX=x, masterY=y, **descriptions[key])
            site['parts'] = [k.removeprefix(key + ' - ') for k in loc.get('areas', {})]
            sites.append(site)
        records.append(dict(name=name, tile=tile, regionX=region['x'], regionY=region['y'],
                            description=region.get('basicInfo', ''), sites=sites,
                            bounds=[20*col, 25*row, 20*(col+1), 25*(row+1)]))
    all_sites = [s for r in records for s in r['sites']]
    assert len(all_sites) == 82
    assert set(descriptions) == {s['name'] for s in all_sites}, 'Unused or missing landmark descriptions'
    for i, site in enumerate(all_sites, 1):
        site['id'] = f'GH{i:02d}'
    return records, all_sites, hashlib.sha256(raw).hexdigest()


def local_position(site):
    x, y = site['localX'], site['localY']
    ew = 'western' if x < -16.7 else 'eastern' if x > 16.7 else 'central'
    ns = 'northern' if y > 16.7 else 'southern' if y < -16.7 else 'middle'
    if ns == 'middle' and ew == 'central':
        return 'near the center of this region'
    if ns == 'middle':
        return 'on the ' + ew + ' side of this region'
    if ew == 'central':
        return 'on the ' + ns + ' side of this region'
    return 'in the ' + ns.replace('ern', '') + ew + ' part of this region'


def markdown(regions, sites, sha):
    lines = ['# Glowhaven: fresh map brief', '', 'Standalone text-only art direction | 5 November 2026', '']
    for title, text in OVERVIEW:
        lines += ['## ' + title, '', text, '']
    lines += ['## Scale and architecture', '']
    for title, text in SCALE:
        lines += ['### ' + title, '', text, '']
    lines += ['## Topology and connections', '']
    lines += [f'- {text}' for text in TOPOLOGY] + ['']
    lines += ['## Coordinate convention', '',
              'Source regionSize = 100; positive local x is east and positive local y is north. Master coordinates are percentages from the LEFT and TOP. X = 100 * (column + 0.5 + localX / 100) / 5. Y = 100 * (row + 0.5 - localY / 100) / 4. Columns and rows are zero-based for these formulas. Coordinates are graphic anchors, not architectural footprints or a physical distance claim.', '',
              '## Standalone generation prompt', '', PROMPT, '', '## Complete regional catalogue', '']
    for r in regions:
        lines += [f"## {r['tile']} - {r['name']}", '', r['description'], '',
                  f"Master bounds: left {r['bounds'][0]}%, top {r['bounds'][1]}%, right {r['bounds'][2]}%, bottom {r['bounds'][3]}%.", '']
        if not r['sites']:
            lines += ['No named location is currently configured here. Preserve open landscape and modest unnamed rural texture; do not invent a new town, castle or dungeon to fill the tile.', '']
        for s in r['sites']:
            lines += [f"### {s['id']} - {s['name']}", '',
                      f"{s['role']}; {local_position(s)}. Local pin ({s['localX']}, {s['localY']}); master anchor ({s['masterX']:.1f}% across, {s['masterY']:.1f}% down).", '',
                      s['visual'], '', s['note'], '',
                      'Location parts, grouped under this site: ' + '; '.join(s['parts']) + '.', '']
    for heading, items in [('Position and interpretation notes', FLAGS), ('Master-to-crop workflow', REFINEMENT)]:
        lines += ['## ' + heading, '']
        for title, text in items:
            lines += ['### ' + title, '', text, '']
    lines += ['## Source and scope', '',
              'Current canonical world, Rebirth revision, read on 5 November 2026. This is a map-authoring brief only. No world records, coordinates, images or gameplay were changed. The original map artwork was not opened, embedded or linked. The document covers the Glowhaven realm only, excluding separate realms.', '',
              'Source SHA-256: ' + sha, '',
              'Coordinate reference: https://wiki.unofficial.voyage/world/locations (x and y fields; checked 5 November 2026).', '']
    return norm('\n'.join(lines))


class BriefDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == 'Section':
            text = flowable.getPlainText()
            key = 'section-' + str(len(self._sections))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, 0, False)
            self._sections.append((text, self.page))


def make_pdf(path, regions, sites, sha):
    font_dir = pathlib.Path('C:/Windows/Fonts')
    fonts = [('Brief', 'segoeui.ttf'), ('BriefBold', 'segoeuib.ttf'), ('BriefItalic', 'segoeuii.ttf')]
    if not all((font_dir / filename).is_file() for _, filename in fonts):
        font_dir = pathlib.Path(reportlab.__file__).resolve().parent / 'fonts'
        fonts = [('Brief', 'Vera.ttf'), ('BriefBold', 'VeraBd.ttf'), ('BriefItalic', 'VeraIt.ttf')]
    for name, filename in fonts:
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily('Brief', normal='Brief', bold='BriefBold', italic='BriefItalic', boldItalic='BriefBold')
    styles = {
        'body': ParagraphStyle('Body', fontName='Brief', fontSize=9.3, leading=13.1, textColor=INK, spaceAfter=6),
        'small': ParagraphStyle('Small', fontName='Brief', fontSize=8, leading=11, textColor=MUTED, spaceAfter=5),
        'title': ParagraphStyle('Title', fontName='BriefBold', fontSize=31, leading=36, textColor=INK, spaceAfter=12),
        'section': ParagraphStyle('Section', fontName='BriefBold', fontSize=18, leading=23, textColor=TEAL, spaceBefore=13, spaceAfter=9, keepWithNext=True),
        'sub': ParagraphStyle('Sub', fontName='BriefBold', fontSize=11.3, leading=15, textColor=INK, spaceBefore=8, spaceAfter=5, keepWithNext=True),
        'meta': ParagraphStyle('Meta', fontName='BriefBold', fontSize=8, leading=11, textColor=TEAL, spaceAfter=5),
        'table': ParagraphStyle('Table', fontName='Brief', fontSize=8.2, leading=11, textColor=INK),
    }
    width, height = A4
    margin = 18*mm
    doc = BriefDoc(str(path), pagesize=A4, leftMargin=margin, rightMargin=margin,
                   topMargin=18*mm, bottomMargin=17*mm, title='Glowhaven - Fresh Map Brief',
                   author='Voyage Maker', subject='Text-only spatial and architectural brief for a fresh regional map')
    doc._sections = []
    frame = Frame(margin, 17*mm, width-2*margin, height-35*mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def decorate(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(TEAL)
        canvas.setLineWidth(.6)
        canvas.line(margin, height-12*mm, width-margin, height-12*mm)
        canvas.setFillColor(MUTED)
        canvas.setFont('Brief', 7.5)
        canvas.drawString(margin, height-10*mm, 'GLOWHAVEN  /  FRESH MAP BRIEF')
        canvas.drawRightString(width-margin, 9*mm, str(document.page))
        canvas.drawString(margin, 9*mm, '5 NOVEMBER 2026  |  TEXT-ONLY GEOGRAPHY AND ARCHITECTURE')
        canvas.restoreState()

    doc.addPageTemplates(PageTemplate(id='normal', frames=[frame], onPage=decorate))
    story = []

    def para(text, style='body'):
        return Paragraph(escape(norm(text)).replace('\n', '<br/>'), styles[style])

    def section(title):
        story.append(para(title, 'section'))

    def item(title, text):
        story.extend([para(title, 'sub'), para(text)])

    story += [Spacer(1, 9*mm), para('GLOWHAVEN', 'title'), para('A fresh map, from the world data', 'section'),
              para('20 regions  /  82 named locations  /  one continuous 5:4 landscape', 'meta'), Spacer(1, 3*mm)]
    for title, text in OVERVIEW:
        item(title, text)
    story.append(PageBreak())
    section('Scale comes before detail')
    for title, text in SCALE:
        item(title, text)
    story.append(PageBreak())
    section('The region grid and essential connections')
    story.append(para('Grid labels belong to this brief only. The finished artwork has no visible tile lines or labels. Each column is 20% of the canvas width; each row is 25% of its height.'))
    grid = []
    for row in range(4):
        cells = []
        for r in regions[row*5:(row+1)*5]:
            cells.append(para(r['tile'] + '\n' + r['name'], 'table'))
        grid.append(cells)
    t = Table(grid, colWidths=[(width-2*margin)/5]*5)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#BFD2D5')),
                          ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                          ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
    story += [t, Spacer(1, 9)]
    for text in TOPOLOGY:
        story.append(para(text))
    story.append(para('Position key: master anchors are measured from LEFT and TOP. Local pins retain the source values: positive x is east; positive y is north. A pin anchors a place; it is not its complete footprint.', 'small'))
    story.append(PageBreak())
    section('Copy-ready generation instruction')
    story.append(para('Give the other image-generation chat this whole PDF. The following instruction summarizes the intended first image; the catalogue supplies its detailed content.', 'small'))
    for paragraph in PROMPT.split('\n\n'):
        story.append(para(paragraph))
    story.append(PageBreak())
    section('Complete regional catalogue')
    story.append(para('Read the location identity and scale notes together. "Parts" lists the actual authored areas for recognition; these are grouped rooms, yards or terrain stretches, not separate map buildings. Exterior descriptions translate current functions into drawable forms. Finishes absent from the source are design suggestions.'))
    for r in regions:
        section(r['tile'] + '  |  ' + r['name'])
        b = r['bounds']
        story.append(para(f"Master window: x {b[0]}-{b[2]}%, y {b[1]}-{b[3]}%  |  {len(r['sites'])} named locations", 'meta'))
        story.append(para(r['description']))
        if not r['sites']:
            story.append(para('No named location is configured here. Keep substantial open landscape with modest unnamed rural texture. This is intentional space, not a request for new towns, castles or dungeon landmarks.'))
        for s in r['sites']:
            elements = [para(s['id'] + '  ' + s['name'], 'sub'),
                        para(f"{s['role']}  |  Master ({s['masterX']:.1f}% across, {s['masterY']:.1f}% down)  |  Local ({s['localX']}, {s['localY']})", 'meta'),
                        para('Position: ' + local_position(s) + '.'),
                        para(s['visual']), para(s['note'])]
            parts = '; '.join(s['parts'])
            elements.append(para('Parts of this one site: ' + parts + '.', 'small'))
            # A whole entry can move to the next page instead of breaking name from its description.
            story.append(KeepTogether(elements))
    story.append(PageBreak())
    section('Position notes and interpretation boundaries')
    for title, text in FLAGS:
        item(title, text)
    story.append(PageBreak())
    section('From the master to detailed crops')
    for title, text in REFINEMENT:
        item(title, text)
    story.append(PageBreak())
    section('Complete position index')
    story.append(para('The index is a numeric cross-check, not a request for printed labels. Percentages use the entire 5:4 master. Values are rounded to one decimal place for reading; the companion CSV retains full precision.', 'small'))
    rows = [[para(x, 'table') for x in ['ID / tile', 'Canonical location', 'Across / down']]]
    for s in sites:
        rows.append([para(s['id'] + ' / ' + s['tile'], 'table'), para(s['name'], 'table'), para(f"{s['masterX']:.1f}% / {s['masterY']:.1f}%", 'table')])
    table = Table(rows, colWidths=[64, 311, width-2*margin-375], repeatRows=1, hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LINEBELOW',(0,0),(-1,0),.6,TEAL),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#D9E2E5')),
                               ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
                               ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    story.append(table)
    section('Source and scope')
    story.append(para('Compiled from the current canonical world on 5 November 2026, following the Rebirth implementation. Only the twenty regions whose realm is Glowhaven and their eighty-two location records are catalogued. Source functions, surface descriptions and area membership guide the text. No old map raster, map URL, screenshot, other-world layout or character portrait is embedded. No gameplay or location record was changed.'))
    story.append(para('Coordinates were checked against the Unofficial Voyage Wiki, Locations, x/y fields: https://wiki.unofficial.voyage/world/locations . The source uses regionSize 100 and north-positive y; this document converts them to left/top master percentages. Building-size budgets are separate illustrative art direction, not engine travel dimensions.', 'small'))
    story.append(para('Source SHA-256: ' + sha, 'small'))
    doc.build(story)
    return doc._sections


def main():
    regions, sites, sha = read_data()
    OUT.mkdir(parents=True, exist_ok=True)
    SHARED.mkdir(parents=True, exist_ok=True)
    pdf = OUT / PDF_NAME
    sections = make_pdf(pdf, regions, sites, sha)
    text = markdown(regions, sites, sha)
    (SHARED / MD_NAME).write_text(text, encoding='utf-8', newline='\n')
    shutil.copyfile(pdf, SHARED / PDF_NAME)
    csv_path = SHARED / 'Glowhaven - Fresh Map Positions.csv'
    with csv_path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['ID', 'Tile', 'Region', 'Location', 'Local X', 'Local Y', 'Across percent', 'Down percent', 'Drawing group'])
        for s in sites:
            writer.writerow([s['id'],s['tile'],s['region'],s['name'],s['localX'],s['localY'],s['masterX'],s['masterY'],s['role']])
    reader = PdfReader(pdf)
    extracted = '\n'.join(page.extract_text() or '' for page in reader.pages)
    missing = [s['name'] for s in sites if s['name'] not in extracted]
    assert not missing, 'Missing locations in PDF: ' + ', '.join(missing)
    assert all(r['name'] in extracted for r in regions)
    assert '/Subtype /Image' not in str(reader.trailer), 'Unexpected image content'
    image_count = sum(len(list(page.images)) for page in reader.pages)
    assert image_count == 0, 'This brief must contain no source artwork'
    assert hashlib.sha256(WORLD.read_bytes()).hexdigest() == sha, 'World changed while building the brief'
    audit = dict(sourceSHA256=sha, regionCount=len(regions), locationCount=len(sites),
                 grid=dict(columns=5,rows=4,aspect='5:4',origin='top left',north='up'),
                 pdfPages=len(reader.pages), embeddedImages=image_count, missingNames=missing,
                 worldChanged=False, artworkOpened=False, sections=sections,
                 sites=sites)
    (HERE / 'review.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in audit.items() if k not in ['sites','sections']},ensure_ascii=False))
    print(str(pdf))


if __name__ == '__main__':
    main()
