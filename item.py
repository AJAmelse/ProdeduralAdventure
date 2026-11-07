import random
from time import time


class Item:
    def __init__(self, difficulty):
        random.seed(time())
        self.damage = 0
        self.armor = 0
        self.durability = 1
        self.difficulty = difficulty
        self.broken = False

    def generate(self, difficulty):
        self.damage = 0
        self.armor = 0


class Weapon(Item):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.generate()

    def generate(self):
        self.damage = int(1 + abs(self.difficulty + random.randint(-5, 5)))
        self.durability = int(10 + self.difficulty * random.randint(1, 4))

    def attack(self):
        if not self.broken:
            self.durability -= 1
            if self.durability <= 0:
                self.broken = True
            return self.damage
        print("Weapon is broken!")
        return 0


class Armor(Item):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.generate()

    def generate(self):
        self.armor = int(1 + abs(self.difficulty + random.randint(-5, 5)))
