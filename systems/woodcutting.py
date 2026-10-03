# woodcutting.py

import random

# woodcutting system
def chop_wood(inventory, current_location):
    # must be in a forest
    if current_location != "forest":
        print("You can only chop wood in the forest.")
        return

    # must have a axe
    axe = None
    for item in inventory.items:
        if "axe" in item:
            axe = item
            break

    if axe is None:
        print("You need an axe to chop wood.")
        return

    # axe bonuses
    bonus = 0
    if axe == "copper_axe":
        bonus = 2
    elif axe == "iron_axe":
        bonus = 4
    elif axe == "gold_axe":
        bonus = 7

    # random wood amount
    wood_amount = random.randint(1, 3) + bonus

    inventory.add_item("wood", wood_amount)
    print(f"You chopped {wood_amount} wood using your {axe}.")