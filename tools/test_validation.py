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
