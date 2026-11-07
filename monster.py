import random
from time import time


class Monster:
    def __init__(self, difficulty_allocation):
        random.seed(time())
        self.alive = True
        self.health = 1
        self.damage = 1
        self.accuracy = 1.0
        self.difficulty = difficulty_allocation

    def attack(self):
        if (random.randint(0, 99) % 100)/100 > self.accuracy:
            return self.damage
        return 0

    def reward(self):
        return self.difficulty * random.randint(1, 5)


class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.damage = 5
        self.accuracy = 0.8
        self.difficulty = 1

