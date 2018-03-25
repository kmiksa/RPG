from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("NAME               HP                                    MP")


print("\n\n")

# Create Black Magic
fire = Spell('Fire', 10, 50, 'black', 'just fire')
wind = Spell('Wind', 13, 55, 'black', 'make some blow')
blizzard = Spell('Blizzard', 12, 54, 'black', 'strike this fucker with a blizzard')
light = Spell('Light', 20, 100, 'black', 'power of light')
quake = Spell('Quake', 14, 60, 'black', 'u know')

# Create White Magic
cure = Spell("Cure", 12, 120, "white", ' will cure ur ass')
kubinio = Spell("Kubinio", 18, 200, "white", 'will cure ur ass even more')

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
bigpotion = Item("Big Potion", "potion", "Heals for 100HP", 100)
superpotion = Item("Super Potion", "potion", "Heals for 500HP ", 500)
elixer = Item("Elixer", "elixer", "Restores fully HP/MP of one player", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores every party member HP/MP", 9999)

granade = Item("Granade", "attack", "Deals 500 damage", 500)

player_spells = [fire, wind, blizzard, light, cure, kubinio]
player_items = [{"item": potion, "quantity": 10}, {"item": bigpotion, "quantity": 3},
                {"item": superpotion, "quantity": 2}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": granade, "quantity": 4}]

# Initiate Fighters
player = Person("Kuba", 450, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick", 450, 65, 60, 34, player_spells, player_items)
player3 = Person("LP", 450, 65, 60, 34, player_spells, player_items)
enemy = Person("Bill", 550, 65, 40, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENNEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("-------------------------")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1  # używam tego ponieważ Python zaczyna liczyć od 0
    # a więc, żeby użytkownik mógł wybrać dobrą wartosc musze zmniejszyc
    # ja o 1 indeks.

    if index == 0:  # Attack
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough mp\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for",
                  str(magic_dmg),  "HP. " + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals,",
                  str(magic_dmg), "points of damage" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]
        if(player.items[item_choice]["quantity"] > 0):
            player.items[item_choice]["quantity"] -= 1
        else:
            player.items[item_choice]["quantity"] = 0


        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue
        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name +
                  " heals for", str(item.prop), "HP", bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp3
            print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals" +
                  str(item.prop) + "points of damage" + bcolors.ENDC)

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("enemy attacked for:", enemy_dmg)

    print("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) +
          "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) +
          "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) +
          "/" + str(player.get_max_hp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp == 0:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False
