from unittest import TestCase
from roman import roman


class TestRoman(TestCase):

    def test_roman(self):
        self.assertEquals(roman(0), "")
