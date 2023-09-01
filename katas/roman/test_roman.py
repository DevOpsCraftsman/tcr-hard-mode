from unittest import TestCase
from roman import roman


class TestRoman(TestCase):

    def test_canary(self):
        self.assertTrue(True)

    def test_I_1(self):
        self.assertEqual(roman(""), None)
