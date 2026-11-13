"""Caption size floor (2026-11-13 test: a 9:16 reel shipped with captions at 3.2% of the height, unreadable on a phone)."""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'skills/framecut/assets/framecut'))
from fc_captions import ass_document


def style_size(ass):
    return int(re.search(r'^Style: Caption,[^,]*,(\d+),', ass, re.M).group(1))


class CaptionSizeFloor(unittest.TestCase):
    def doc(self, size, w=1080, h=1920):
        seq = {'fps': {'num': 25, 'den': 1}, 'captions': {'enabled': True, 'size': size}}
        delivery = {'width': w, 'height': h}
        return ass_document({}, seq, delivery, {'groups': []})

    def test_vertical_captions_never_go_below_the_floor(self):
        ass, layout = self.doc(.032)
        self.assertEqual(style_size(ass), round(1920 * .045))
        self.assertIn('caption_size_raised', [x['code'] for x in layout])

    def test_landscape_floor_is_lower(self):
        ass, _ = self.doc(.03, 1920, 1080)
        self.assertEqual(style_size(ass), round(1080 * .04))

    def test_a_larger_size_is_kept_without_a_warning(self):
        ass, layout = self.doc(.06)
        self.assertEqual(style_size(ass), round(1920 * .06))
        self.assertEqual(layout, [])


if __name__ == '__main__':
    unittest.main()
