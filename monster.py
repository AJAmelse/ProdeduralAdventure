import random
from time import time


class Monster:
    def __init__(self, difficulty_allocation):
        random.seed(time())
        self.alive = True
        self.health = 1
        self.damage = 1
        self.accuracy = 1.0
        if difficulty_allocation < 1:
            raise ValueError("difficulty_allocation must be positive")
        try:
            self.difficulty = int(difficulty_allocation)
        except ValueError:
            raise TypeError("difficulty_allocation must be an integer")

    def attack(self):
        if (random.randint(0, 99) % 100)/100 > self.accuracy:
            return self.damage
        return 0

    def reward(self):
        return self.difficulty * random.randint(1, 5)

    def damage(self, amount):
        if amount < 0:
            raise ValueError("cannot deal negative damage")
        if amount > self.health:
            self.health = 0
        else:
            self.health -= amount
        if self.health == 0:
            self.alive = False
        return self.alive


class Skeleton(Monster):
    def __init__(self, difficulty_allocation):
        super().__init__(difficulty_allocation)
        self.health = 40
        self.damage = 5
        self.accuracy = 0.8

