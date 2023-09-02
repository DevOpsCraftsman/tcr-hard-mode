from unittest import TestCase
from roman import roman


class TestRoman(TestCase):

    def test_roman(self):
        self.assertEqual(roman(0), "")
        self.assertEqual(roman(1), "I")
        self.assertEqual(roman(2), "II")
