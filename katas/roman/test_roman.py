from unittest import TestCase
from roman import roman


class TestRoman(TestCase):

    def test_roman(self):
        self.assertEqual(roman(0), None)
