from unittest import TestCase
from roman import roman


class TestRoman(TestCase):

    def test_canary(self):
        self.assertTrue(True)
        self.assertEqual(roman(""), None)
