#!/usr/bin/env python3
"""Portable authoring, validation and conservative Git synchronization helpers."""
import argparse
import hashlib
import json
import math
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORLD = ROOT / 'world-draft/WorldAlpha - World.json'
INDEX = ROOT / 'docs/asset-index.json'
MEDIA_DIRS = ['npc portraits', 'location images', 'maps', 'map-variations']
MEDIA_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.mp3', '.wav', '.ogg', '.m4a', '.pdf'}
SECTIONS = {
    'Abilities': 'abilities', 'Author Seeds': 'authorSeeds', 'Factions': 'factions',
    'Game Modes': 'gameModes', 'Items': 'itemTypes', 'Location Archetypes': 'locationArchetypes',
    'Locations': 'locations', 'NPC Types': 'npcTypes', 'NPCs': 'npcs', 'Realms': 'realms',
    'Regions': 'regions', 'Resources': 'resourceSettings', 'Skills': 'skills',
    'Story Overview': 'storySettings', 'Story Starts': 'storyStarts', 'Tips': 'tipSettings',
    'Trait Categories': 'traitCategories', 'Traits': 'traits', 'Triggers': 'triggerDefinitions',
    'World Lore': 'worldLore',
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write_json(path, data):
    text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    if not path.exists() or path.read_text(encoding='utf-8-sig') != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8', newline='\n')


def units(value):
    return len(value.encode('utf-16-le')) // 2


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def sync(check=False):
    w = load(WORLD)
    sections = {name: w[key] for name, key in SECTIONS.items()}
    sections['AI'] = {key: w[key] for key in ['imagePromptConfiguration', 'aiInstructions']}
    sections['Quests'] = w['parties']['']['quests']
    sections['Quest Triggers'] = w['parties']['']['questTriggers']
    sections['Arcs'] = w['parties'][''].get('arcs', {})
    stale = []
    for name, data in sections.items():
        path = WORLD.parent / ('WorldAlpha - ' + name + '.json')
        if not path.exists() or load(path) != data:
            stale.append(name)
            if not check:
                write_json(path, data)
    if check and stale:
        raise ValueError('Stale section exports: ' + ', '.join(stale))
    print(f'Section exports: {len(sections)} checked; {len(stale)} ' + ('stale' if check else 'updated'))


def validate(world=None):
    w = load(WORLD) if world is None else world
    errors, checks = [], 0

    def ck(ok, label):
        nonlocal checks
        checks += 1
        if not ok:
            errors.append(label)

    def number(value):
        return type(value) in (int, float) and math.isfinite(value)

    def requirement(req, trail):
        if not isinstance(req, dict):
            ck(False, f'Requirement object: {trail}')
            return
        kind = req.get('type')
        targets = {'trait': w['traits'], 'skill': w['skills'],
                   'attribute': w['attributeSettings']['attributeNames'],
                   'resource': w['resourceSettings']}
        ck(kind in [*targets, 'characterLevel'], f'Requirement type: {trail}')
        # Studio requires amount even for trait gates, where its value is ignored.
        ck(number(req.get('amount')), f'Requirement numeric amount: {trail}')
        if kind in targets:
            ck(isinstance(req.get('variable'), str) and req['variable'] in targets[kind],
               f'Requirement reference: {trail}')

    for section in ['npcs', 'itemTypes', 'abilities', 'traits', 'triggerDefinitions', 'storyStarts', 'gameModes', 'traitCategories']:
        for key, value in w[section].items():
            ck(key == value.get('name'), f'{section}/{key}: key/name mismatch')
        ck(len({key.casefold().strip() for key in w[section]}) == len(w[section]),
           f'{section}: case-insensitive duplicate name')

    for key, region in w['regions'].items():
        ck(region['realm'] in w['realms'], f'Region realm: {key}')
    for key, location in w['locations'].items():
        ck(location['region'] in w['regions'], f'Location region: {key}')
    for key, npc in w['npcs'].items():
        location = npc.get('currentLocation')
        if location:
            ck(location in w['locations'], f'NPC location: {key}/{location}')
        ck('known' not in npc, f'Deprecated known field: {key}')

    refs = {'resource': w['resourceSettings'], 'skill': w['skills'],
            'attribute': w['attributeSettings']['attributeNames'], 'stat': ['damage', 'armor']}
    ck(units(compact(w['traits'])) <= 1750000, 'Trait collection exceeds 1,750,000 characters')
    ck(units(compact(w['traitCategories'])) <= 100000, 'Trait categories exceed 100,000 characters')
    for name, trait in w['traits'].items():
        ck(units(trait.get('description', '') + trait.get('traitNarrativeEffects', '')) <= 6000,
           f'Trait text cap: {name}')
        ck(len(trait.get('requirements', [])) <= 10, f'Trait requirement count: {name}')
        for field in ['attributes', 'skills', 'resources', 'startingItems', 'abilities', 'unlockedBy', 'excludedBy', 'requirements']:
            ck(isinstance(trait.get(field), list), f'Trait required array: {name}/{field}')
        for field, target, key in [('attributes', refs['attribute'], 'attribute'), ('skills', w['skills'], 'skill'), ('resources', w['resourceSettings'], 'resource'), ('startingItems', w['itemTypes'], 'item')]:
            for entry in trait.get(field, []):
                ck(entry.get(key) in target, f'Trait reference: {name}/{field}/{entry.get(key)}')
        for ability in trait.get('abilities', []):
            ck(ability in w['abilities'], f'Trait ability reference: {name}/{ability}')
        for field in ['unlockedBy', 'excludedBy']:
            for key in trait.get(field, []):
                ck(key in w['traits'] or key in w['storyStarts'], f'Trait gate reference: {name}/{key}')
        for index, req in enumerate(trait.get('requirements', [])):
            requirement(req, f'traits/{name}/{index}')
    for name, category in w['traitCategories'].items():
        ck(0 <= category.get('maxSelections', -1) <= 40, f'Creation selection limit: {name}')
        ck(isinstance(category.get('traits'), list), f'Category required traits: {name}')
        for group in [category] + category.get('subcategories', []):
            for key in group.get('traits', []):
                ck(key in w['traits'], f'Category trait reference: {name}/{key}')
    for key, item in w['itemTypes'].items():
        ck(item['category'] in w['itemSettings']['itemCategories'], f'Item category: {key}')
        ck(units(item['description']) <= 4000, f'Item description cap: {key}')
        tier = item.get('tier')
        if tier is not None:
            ck(tier in w['itemSettings']['tiers'], f'Item tier reference: {key}/{tier}')
        if 'estimatedValue' in item:
            value = item['estimatedValue']
            valid_value = number(value) and value >= 0 and value == int(value)
            ck(valid_value, f'Item estimatedValue must be a nonnegative whole number: {key}')
            bounds = w['itemSettings']['tiers'].get(tier, {}).get('valueRange')
            if bounds and valid_value:
                ck(bounds['min'] <= value <= bounds['max'],
                   f'Item estimatedValue outside {tier} range {bounds["min"]}–{bounds["max"]}: {key} ({value})')
        for bonus in item.get('bonuses', []):
            ck(bonus.get('variable') in refs.get(bonus.get('type'), []), f'Item bonus reference: {key}')
    ck(units(compact(w['itemTypes'])) <= 250000, 'Item collection exceeds 250,000 characters')
    ck(len(w['abilities']) <= 1500, 'Ability count exceeds 1,500')
    for key, ability in w['abilities'].items():
        ck(units(ability['description']) <= 2000, f'Ability description cap: {key}')
        ck(isinstance(ability.get('requirements'), list), f'Ability required requirements array: {key}')
        ck(len(ability.get('requirements', [])) <= 10, f'Ability requirement count: {key}')
        for index, req in enumerate(ability.get('requirements', [])):
            requirement(req, f'abilities/{key}/{index}')

    for name, tr in w['triggerDefinitions'].items():
        ck(len(tr.get('conditions', [])) <= 5 and len(tr.get('effects', [])) <= 10,
           f'Trigger condition/effect count: {name}')
        ck(units(compact(tr)) <= 10000, f'Trigger character cap: {name}')
        for c in tr.get('conditions', []):
            if c['type'] in ['story', 'action']:
                ck(units(c['query']) <= 1000, f'Trigger semantic query cap: {name}')
            if c['type'] == 'player-item':
                ck(c['item'] in w['itemTypes'], f'Condition item reference: {name}')
            if c['type'] == 'skill-value':
                ck(c['skill'] in w['skills'], f'Condition skill reference: {name}')
        for e in tr.get('effects', []):
            for kind, field, collection in [('item-add', 'item', 'itemTypes'),
                                           ('item-remove', 'item', 'itemTypes'),
                                           ('player-abilities', 'value', 'abilities'),
                                           ('player-traits', 'value', 'traits'),
                                           ('player-resource', 'resource', 'resourceSettings')]:
                if e['type'] == kind:
                    ck(e[field] in w[collection], f'Effect reference: {name}/{kind}')

    for party in w['parties'].values():
        for name, quest in party.get('quests', {}).items():
            # Quest objects, including nested objectives, may contain typed conditions.
            def visit(value, trail):
                if isinstance(value, dict):
                    if 'completionCondition' in value:
                        c = value['completionCondition']
                        ck(isinstance(c, dict) and (
                            c.get('type') == 'story' and isinstance(c.get('query'), str) or
                            c.get('type') == 'narrative-event-completed' and isinstance(c.get('eventId'), str)
                        ), f'Typed quest completion condition: {trail}')
                    for k, v in value.items():
                        visit(v, trail + '/' + k)
                elif isinstance(value, list):
                    for i, v in enumerate(value):
                        visit(v, trail + '/' + str(i))
            visit(quest, name)

    for task, notes in w['aiInstructions'].items():
        cap = {'generateStory': 30000, 'generateNPCIntents': 40000,
               'generateNPCDetails': 28964, 'generateNPCUpdates': 24000}.get(task, 20000)
        ck(units(compact(notes)) <= cap, f'AI task character cap: {task}')
        for key, text in notes.items():
            ck(units(compact(text)) <= (8000 if task == 'generateNPCIntents' else 5000),
               f'AI leaf character cap: {task}/{key}')
    for key, text in w['imagePromptConfiguration'].items():
        ck(units(text) <= 5000, f'Image prompt character cap: {key}')
    ck(sum(units(v) for v in w['imagePromptConfiguration'].values()) <= 15000, 'Image prompt total cap')
    for key in ['worldBackground', 'questGenerationGuidance']:
        ck(units(w['storySettings'].get(key, '')) <= 5000, f'Story settings character cap: {key}')
    ck(units(compact(w)) <= 12500000, 'Whole world character cap')
    if errors:
        raise ValueError(f'{len(errors)} validation errors:\n' + '\n'.join(errors[:50]))
    print(f'Structural validation passed: {checks} checks (not live Studio validation)')


def git(*args, capture=False, check=True):
    return subprocess.run(['git', *args], cwd=ROOT, check=check, text=True,
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.PIPE if capture else None)


def start():
    if git('status', '--porcelain', capture=True).stdout.strip():
        raise ValueError('Local changes exist. Keep them; commit or review before pulling.')
    git('fetch', 'origin')
    git('pull', '--ff-only')
    print('Desktop checkout is current. No local work was discarded.')


def asset_changes():
    index = load(INDEX) if INDEX.exists() else {'assets': {}}
    changed = []
    for folder in MEDIA_DIRS:
        for path in (WORLD.parent / folder).rglob('*'):
            if not path.is_file() or path.suffix.lower() not in MEDIA_EXTS:
                continue
            relative = path.relative_to(ROOT).as_posix()
            old = index['assets'].get(relative)
            stat = path.stat()
            if old and old['size'] == stat.st_size and old.get('mtimeNs') == stat.st_mtime_ns:
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if old and old['sha256'] == digest:
                continue
            if stat.st_size > 95 * 1024 * 1024:
                raise ValueError(f'New media exceeds 95 MiB; choose storage deliberately: {relative}')
            changed.append(relative)
            index['assets'][relative] = {'size': stat.st_size, 'sha256': digest, 'mtimeNs': stat.st_mtime_ns}
    # Missing legacy files in cloud checkouts are deliberately retained in the index.
    return changed, index


def publish(message):
    branch = git('branch', '--show-current', capture=True).stdout.strip()
    if not branch:
        raise ValueError('Detached checkout: use the cloud branch/PR workflow instead.')
    git('fetch', 'origin')
    upstream = git('rev-parse', '--abbrev-ref', '@{upstream}', capture=True, check=False)
    if upstream.returncode == 0:
        result = git('merge-base', '--is-ancestor', '@{upstream}', 'HEAD', check=False)
        if result.returncode:
            raise ValueError('Remote changes need review before publishing. No push or reset performed.')
    sync()
    validate()
    subprocess.run([sys.executable, str(ROOT / 'tools/test_validation.py')], cwd=ROOT, check=True)
    if (ROOT / 'tools/test_voyage_portraits.py').exists():
        subprocess.run([sys.executable, str(ROOT / 'tools/test_voyage_portraits.py')], cwd=ROOT, check=True)
    subprocess.run(['node', str(ROOT / 'tools/test_item_mechanics.cjs')], cwd=ROOT, check=True)
    if (ROOT / 'tools/test_adventurers.cjs').exists():
        subprocess.run(['node', str(ROOT / 'tools/test_adventurers.cjs')], cwd=ROOT, check=True)
    if (ROOT / 'tools/test_creation.cjs').exists():
        subprocess.run(['node', str(ROOT / 'tools/test_creation.cjs')], cwd=ROOT, check=True)
    if (ROOT / 'tools/test_crucible.cjs').exists():
        subprocess.run(['node', str(ROOT / 'tools/test_crucible.cjs')], cwd=ROOT, check=True)
    changed, index = asset_changes()
    if changed:
        write_json(INDEX, index)
    git('add', '--all')
    for path in changed:
        git('add', '--force', '--', path)
    if git('diff', '--cached', '--quiet', check=False).returncode:
        git('commit', '-m', message)
    git('push', '--set-upstream', 'origin', branch)
    print(f'Published {branch}; included {len(changed)} new or changed media files.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('validate')
    commands.add_parser('start')
    commands.add_parser('sync').add_argument('--check', action='store_true')
    commands.add_parser('publish').add_argument('-m', '--message', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'validate': validate()
        elif args.command == 'sync': sync(args.check)
        elif args.command == 'start': start()
        elif args.command == 'publish': publish(args.message)
    except (ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
