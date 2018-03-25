import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, attack, defence, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackl = attack - 10
        self.attackh = attack + 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.attackl, self.attackh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS " + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ". ", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC " + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ". ", spell.name, "(cost: ",
                  str(spell.cost) + ") damage: ", str(spell.dmg), str(spell.description))
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ITEMS " + bcolors.ENDC)
        for items in self.items:
            print("    " + str(i) + ". ", items["item"].name +  ": ", items["item"].description, "(x " + str(items["quantity"]), ")")
            i += 1

    def get_status(self):
        print("                   ________________________              __________")
        print(bcolors.BOLD + + self.name + "     " +
              self.hp +"/", self.maxhp + "|" + bcolors.OKGREEN + "████████                " + bcolors.ENDC +
              "|        " +
              self.mp + "/", self.maxmp + "|" + bcolors.OKBLUE + "█████     " + bcolors.ENDC + "|")
