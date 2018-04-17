from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

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
enemy_spells = [wind, cure, wind]
player_items = [{"item": potion, "quantity": 10}, {"item": bigpotion, "quantity": 3},
                {"item": superpotion, "quantity": 2}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": granade, "quantity": 4}]

# Initiate Fighters
player1 = Person("Kuba", 1450, 165, 60, 34, player_spells, player_items)
player2 = Person("Nick", 1450, 165, 60, 34, player_spells, player_items)
player3 = Person("LPck", 1450, 165, 60, 34, player_spells, player_items)

# Initiate Enemies
enemy1 = Person("Thor", 500, 160, 200, 30, enemy_spells, [])
enemy2 = Person("Bill", 1550, 165, 240, 25, enemy_spells, [])
enemy3 = Person("Orko", 500, 123, 145, 34, enemy_spells, [])


players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENNEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("-------------------------")

    print("\n\n")

    print("NAME             HP                                      MP")
    for player in players:
        player.get_status()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:
        player.choose_action()
        choice = input("    Choose action:")
        index = int(choice) - 1  # używam tego ponieważ Python zaczyna liczyć od 0
        # a więc, żeby użytkownik mógł wybrać dobrą wartosc musze zmniejszyc
        # ja o 1 indeks.

        # Attack
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name + " for:", dmg,
                  " points of damage.")
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

        # Magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou don't have enough mp\n"
                      + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            # White Magic
            if spell.type == "white":
                player.heal(magic_dmg)
                print("\n" + spell.name + " heals for",
                      str(magic_dmg),  "HP. ")
            # Black Magic
            elif spell.type == "black":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print("\n" + spell.name + " deals,",
                      str(magic_dmg), "points of damage to " +
                      enemies[enemy].name)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

        # Items
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

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

                if item.name == "Mega Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp3
                print(bcolors.OKGREEN + "\n" + item.name +
                      "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals" +
                      str(item.prop) + "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 3:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    # Player lost
    elif defeated_players == 3:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False
    print("\n")
    # Enemies attack
    for enemy in enemies:
        # Chose attack
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " +
                  players[target].name.replace(" ", ""), " for:", enemy_dmg)
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(spell.name + " heals " + enemy.name, " for",
                      str(magic_dmg),  "HP. ")
            # Black Magic
            elif spell.type == "black":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)

                print("\n" + enemy.name.replace(" ", ""), "'s", spell.name + " deals,",
                      str(magic_dmg), "points of damage to " +
                      players[target].name)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]
            #print("Enemy choose ", spell, "damage is", magic_dmg)
