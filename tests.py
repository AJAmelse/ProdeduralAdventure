import unittest
from monster import *

class TestMonster(unittest.TestCase):

    def setUp(self):
        self.monsters = [Skeleton(10)]

    def raise_error_on_negative_difficulty(self):
        with self.assertRaises(ValueError):
            Skeleton(-5)

    def raise_error_on_non_int_difficulty(self):
        values = [True, None, [5], 6.3, "AAAA"]
        for v in values:
            with self.subTest(v=v):
                with self.assertRaises(TypeError):
                    Skeleton("NaN")

    def test_attack(self):
        for m in self.monsters:
            self.assertGreaterEqual(m.attack, 0)
