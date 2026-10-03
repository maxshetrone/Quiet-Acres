# mining.py

import random

# mining system
def mine(inventory, current_location):
    # must be in the mines
    if current_location != "mines":
        print("You can only mine in the mines.")
        return

    # must have a pickaxe
    pickaxe = None
    for item in inventory.items:
        if "pickaxe" in item:
            pickaxe = item
            break

    if pickaxe is None:
        print("You need a pickaxe to mine.")
        return

    # bonuses
    bonus = 0
    if pickaxe == "copper_pickaxe":
        bonus = 1
    elif pickaxe == "iron_pickaxe":
        bonus = 2
    elif pickaxe == "gold_pickaxe":
        bonus = 4

    # random ore type
    ore_types = ["copper_ore", "iron_ore", "gold_ore"]
    ore = random.choice(ore_types)

    ore_amount = random.randint(1, 2) + bonus

    inventory.add_item(ore, ore_amount)
    print(f"You mined {ore_amount}x {ore} using your {pickaxe}.")