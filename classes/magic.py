import random


class Spell:
    def __init__(self, name, cost, dmg, type, description):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        self.description = description

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
