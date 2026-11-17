"""Layered work rule (owner 2026-11-17): the skill and the reference name every layer."""
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'skills' / 'framecut'
LAYERS = ['Assembly', 'Rough cut', 'Fine cut', 'Picture lock', 'Sound', 'Colour', 'Captions', 'QC']


class LayersTest(unittest.TestCase):
    def test_reference_lists_all_layers(self):
        text = (SKILL / 'references' / 'layered-work.md').read_text(encoding='utf-8')
        for layer in LAYERS:
            self.assertIn(f'| {layer} |', text)
        self.assertIn('Exception', text)

    def test_skill_points_to_reference(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('Work in layers (mandatory)', text)
        self.assertIn('references/layered-work.md', text)

    def test_checkpoint_has_layer(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('the current `layer`', text)


if __name__ == '__main__':
    unittest.main()
