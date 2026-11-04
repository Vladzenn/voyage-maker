"""Regression tests for the actual Studio rejection reported on 1 November 2026."""
import contextlib
import copy
import io
import unittest

import project


class StudioValidationRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = project.load(project.WORLD)
        manifest = project.load(project.ROOT / 'tools/phantom/manifest.json')
        cls.talent_abilities = manifest['newAbilities']

    def setUp(self):
        self.world = copy.deepcopy(type(self).world)

    def validate(self):
        with contextlib.redirect_stdout(io.StringIO()):
            project.validate(self.world)

    def test_fixed_world_passes(self):
        self.validate()

    def test_area_paths_cannot_cross_parent_locations(self):
        locations = self.world['locations']
        parents = [name for name, location in locations.items() if location.get('areas')]
        first, other = parents[:2]
        area_name = next(iter(locations[first]['areas']))
        other_area = next(iter(locations[other]['areas']))
        area = locations[first]['areas'][area_name]
        previous = copy.deepcopy(area.get('paths', []))
        area['paths'] = [other_area]
        with self.assertRaisesRegex(ValueError, 'Area path outside parent location:'):
            self.validate()
        area['paths'] = previous
        self.validate()

    def test_quest_statement_uses_supported_field(self):
        for name in ['A Fisher’s First Lesson', 'Supper before the Tide Turns',
                     'A Color beneath the Scales']:
            with self.subTest(quest=name):
                q = self.world['parties']['']['quests'][name]
                self.assertIsInstance(q['questStatement'], str)
                q['description'] = q.pop('questStatement')
                with self.assertRaisesRegex(ValueError, 'Quest statement field: ' + name):
                    self.validate()
                q['questStatement'] = q.pop('description')
        self.validate()

    def test_quest_objectives_use_native_map(self):
        names = ['A Fisher’s First Lesson', 'Supper before the Tide Turns',
                 'A Color beneath the Scales']
        for name in names:
            with self.subTest(quest=name):
                q = self.world['parties']['']['quests'][name]
                correct = copy.deepcopy(q['objectives'])
                q['objectives'] = [{'description': 'A real fishing task', 'completed': False}]
                with self.assertRaisesRegex(ValueError, 'Quest objectives map: ' + name):
                    self.validate()
                q['objectives'] = correct
        q = self.world['parties']['']['quests'][names[0]]
        key = next(iter(q['objectives']))
        correct = copy.deepcopy(q['objectives'][key])
        for field, value, label in [('id', None, 'id'), ('text', 42, 'text'),
                                    ('status', 'available', 'status')]:
            with self.subTest(field=field):
                q['objectives'][key] = {**correct, field: value}
                with self.assertRaisesRegex(ValueError, 'Quest objective ' + label + ':'):
                    self.validate()
        q['objectives'][key] = correct
        self.validate()

    def test_trigger_string_value_studio_limit(self):
        tr = self.world['triggerDefinitions']['ghx_local_commissions']
        tr['conditions'].append({'type': 'party-location', 'operator': 'regex', 'value': 'x' * 101})
        with self.assertRaisesRegex(ValueError, 'Trigger condition value cap: ghx_local_commissions'):
            self.validate()
        # Quotes occupy two units, leaving room for 49 non-BMP glyphs.
        tr['conditions'][-1]['value'] = '\U0001f30a' * 49
        self.validate()
        tr['conditions'][-1]['value'] += '\U0001f30a'
        with self.assertRaisesRegex(ValueError, 'Trigger condition value cap: ghx_local_commissions'):
            self.validate()

    def test_studio_rejects_previous_fishing_regex(self):
        previous = r'\b([Ff]ish|[Aa]ngling|[Rr]eel|[Ll]ure|[Bb](ait|obber))\w*|\b([Cc]ast|[Ll]ower).*\b(line|rod|hook)\b'
        self.assertEqual(project.units(previous), 99)
        self.assertEqual(project.units(project.compact(previous)), 106)
        for name in ('fsh_basics', 'fsh_cast_lure', 'fsh_cast_bait', 'fsh_bait_miss'):
            condition = self.world['triggerDefinitions'][name]['conditions'][0]
            current = condition['value']
            with self.subTest(trigger=name):
                condition['value'] = previous
                with self.assertRaisesRegex(ValueError, f'Trigger condition value cap: {name}'):
                    self.validate()
                condition['value'] = current
        self.validate()

    def test_original_studio_rejection_is_detected(self):
        for name in self.talent_abilities:
            del self.world['abilities'][name]['requirements'][0]['amount']
        for name, value in [('Rain-Counting Brooch', 260), ('Polite Kettle Bell', 180)]:
            self.world['itemTypes'][name]['estimatedValue'] = value
        with self.assertRaises(ValueError) as caught:
            self.validate()
        message = str(caught.exception)
        self.assertTrue(message.startswith('26 validation errors:'), message)
        for name in self.talent_abilities + ['Rain-Counting Brooch', 'Polite Kettle Bell']:
            self.assertIn(name, message)

    def test_requirement_amount_must_be_finite_number(self):
        req = self.world['abilities'][self.talent_abilities[0]]['requirements'][0]
        for value in [None, True, '1', float('nan'), float('inf')]:
            with self.subTest(value=value):
                req['amount'] = value
                with self.assertRaisesRegex(ValueError, 'Requirement numeric amount:'):
                    self.validate()

    def test_resource_and_level_requirement_forms(self):
        ability = self.world['abilities'][self.talent_abilities[0]]
        ability['requirements'] = [{'type': 'characterLevel', 'amount': 1},
                                   {'type': 'resource', 'variable': 'Mana', 'amount': 1}]
        self.validate()
        ability['requirements'][1]['variable'] = 'Missing Resource'
        with self.assertRaisesRegex(ValueError, 'Requirement reference:'):
            self.validate()
        ability['requirements'] = [{'type': 'ability', 'variable': 'Margin Remembered', 'amount': 1}]
        with self.assertRaisesRegex(ValueError, 'Requirement type:'):
            self.validate()

    def test_item_price_and_tier_bounds(self):
        item = self.world['itemTypes']['Rain-Counting Brooch']
        for value in [299, 3001, -1, 300.5, True, '300']:
            with self.subTest(value=value):
                item['estimatedValue'] = value
                with self.assertRaisesRegex(ValueError, 'Item estimatedValue'):
                    self.validate()
        for value in [300, 3000]:
            item['estimatedValue'] = value
            self.validate()
        item.pop('estimatedValue')  # Unknown prices remain valid.
        self.validate()
        item['tier'] = 'Missing Tier'
        with self.assertRaisesRegex(ValueError, 'Item tier reference:'):
            self.validate()


if __name__ == '__main__':
    unittest.main()
