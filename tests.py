import unittest
from monster import *
from item

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
                    Skeleton(v)

    def test_attack(self):
        for m in self.monsters:
            self.assertGreaterEqual(m.attack(), 0)

    def test_damage(self):
        for m in self.monsters:
            self.assertEqual(m.damage(1), 1)

    def test_reward(self):
        for m in self.monsters:
            self.assertGreaterEqual(m.reward(), 1)

class TestItems(unittest.TestCase):
    def setUp(self):
        items = [Weapon()]
