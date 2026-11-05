"""Generate the author-facing map handoff from the actual placement ledger."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VISUAL = {
    'Empyrean Archives': 'Northern raised complex with violet domes; interpreted as the principal archive.',
    'Crownwater Aqueduct': 'Upper connecting aqueducts and stepped water channels.',
    'The High Reservoir': 'Upper water basin and its controlled spillways.',
    'Caelrath Amphitheatre': 'Western open circular performance structure.',
    "The King's Lists": 'Rectangular western exercise or tournament field.',
    'Skyglass Observatory': 'Northeastern isolated spires and celestial fittings.',
    'Amethyst Intake Works': 'Northeastern exposed violet crystal formation.',
    'Windward Mills': 'Southwestern cultivated terraces and visible windmills.',
    'Eastwater Locks': 'Eastern tiered water passages between the inhabited shelves.',
    'Starwatch Isle': 'Small offshore or harbor-edge tower site; its precise pin needs author review.',
}

def main():
    rows = json.loads((HERE / 'placements.json').read_text(encoding='utf-8'))
    world = json.loads((ROOT / 'output/ardelis-2026-11-05/The Schools of Magic, Arise! - Ardelis.json').read_text(encoding='utf-8'))
    source = json.loads((HERE / 'source.json').read_text(encoding='utf-8'))
    regions = {k: v for k, v in world['regions'].items() if v.get('realm') == 'Ardelis'}
    lines = [
        '# Ardelis map and landmark handoff', '',
        'Caelrath occupies the supplied **four-column, three-row** map. Region coordinates use the existing Studio grid; local x/y values are separate offsets within each region. These are authoring notes, not player-facing lore.', '',
        'All twelve original tile images, crops and grid coordinates are retained. The eighteen supplied location pins retain their exact local x/y positions. The other sixty-six pins are provisional placements within the appropriate tile, not pixel-perfect recognition of individual roofs. Move those in Studio as needed.', '',
        '## Grid, north to south', '',
        '| Row | West (-2) | West-center (-1) | East-center (0) | East (1) |',
        '|---|---|---|---|---|',
    ]
    for y in (1, 0, -1):
        cells = [next(k for k, r in regions.items() if (r['x'], r['y']) == (x, y)) for x in (-2, -1, 0, 1)]
        lines.append('| ' + str(y) + ' | ' + ' | '.join(cells) + ' |')
    lines += ['', '## Preserved author pins and completed names', '', '| Supplied name | Final site | Region | Local x/y |', '|---|---|---|---|']
    for row in rows:
        if row['source'] != 'NEW':
            lines.append(f"| {row['source']} | {row['name']} | {row['region']} | {row['x']}, {row['y']} |")
    lines += ['', '## Previously unmarked visible features', '',
              'These assignments interpret recognizable shapes in the supplied map. Function and name are authored choices; the image itself does not establish who owns a building or what happens inside it.', '',
              '| Feature interpretation | Assigned site | Region |', '|---|---|---|']
    for name, note in VISUAL.items():
        matches = [r for r in rows if r['name'] == name]
        if not matches:
            raise ValueError('Landmark no longer exists: ' + name)
        lines.append(f"| {note} | {name} | {matches[0]['region']} |")
    lines += ['', '## Added civic coverage', '',
              'The remaining new establishments give the city usable services and residents: guild, lodging, boutiques, workshops, food, schools, tenements, religious services, household entrances and harbor trades. They occupy existing city fabric; they do not assert that every small illustrated roof was independently identified.', '',
              'The palace descent is inside the palace location. The sewer entrance is in Eastwater Ward and does not create an underground shortcut to the palace. Connected rooms remain areas rather than extra overland pins.', '',
              '## Complete placement list', '']
    for region in sorted(regions, key=lambda k: (-regions[k]['y'], regions[k]['x'])):
        lines += ['### ' + region, '', '| Site | Local x/y | Provenance |', '|---|---|---|']
        for row in rows:
            if row['region'] == region:
                provenance = 'Preserved author pin' if row['source'] != 'NEW' else ('Visible-feature interpretation; approximate pin' if row['name'] in VISUAL else 'Added service or playable site; approximate pin')
                lines.append(f"| {row['name']} | {row['x']}, {row['y']} | {provenance} |")
        lines.append('')
    target = ROOT / 'world-draft/Ardelis - Map and Landmark Handoff.md'
    target.write_text('\n'.join(lines), encoding='utf-8')
    with (HERE / 'placements.csv').open('w', encoding='utf-8-sig', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=['source', 'name', 'sourceRegion', 'region', 'x', 'y', 'placement'])
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({'sites': len(rows), 'preservedPins': sum(r['source'] != 'NEW' for r in rows), 'guide': str(target)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
