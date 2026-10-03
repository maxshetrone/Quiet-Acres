# fishing.py

import random
from data.fish import fish_data

 # fishing system
def fish(inventory, current_location):
    # must be at a riverbank
    if current_location != "riverbank":
        print("You can only fish at the riverbank")
        return

    rod = None
    for item in inventory.items:
        if "fishing_rod" in item:
            rod = item
            break
    if rod is None:
        print("You need a fishing rod to fish.")
        return
    
    bonus = 0
    if rod == "copper_fishing_rod":
        bonus = 10
    elif rod == "iron_fishing_rod":
        bonus = 20
    elif rod == "gold_fishing_rod":
        bonus = 35

    # random chance to catch a fish
    catch_chance = random.randint(1, 100)

    if catch_chance <= 25:
        print("You didn't catch anything")
        return

    # pick a random fish
    fish_name = random.choice(list(fish_data.keys()))
    inventory.add_item(fish_name)

    print(f"You caught a {fish_name}!")