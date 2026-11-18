import unittest
from clamp import clamp

class ClampTests(unittest.TestCase):
    def test_below_lower(self):
        self.assertEqual(clamp(-2, 0, 10), 0)

    def test_in_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_above_upper(self):
        self.assertEqual(clamp(12, 0, 10), 10)
