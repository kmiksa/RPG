from classes.game import Person, bcolors

magic = ({"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 70},
         {"name": "Blizard", "cost": 10, "dmg": 75})


player = Person(450, 65, 60, 34, magic)
enemy = Person(1000, 65, 40, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENNEMY ATTACKS!" + bcolors.ENDC)
