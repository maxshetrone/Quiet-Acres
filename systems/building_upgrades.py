# building_upgrades.py

from data.building_upgrades import building_upgrades

def upgrade_building(structure_name, buildings, inventory):
    # check if building exists
    if structure_name not in building_upgrades:
        print("This building cannot be upgraded")
        return

    # check if building is built
    if structure_name not in buildings:
        print(f"You haven't built the {structure_name} yet.")
        return

    # determine current level
    current_level = buildings[structure_name]

    # determine next level
    next_level = f"level_{current_level + 1}"

    if next_level not in building_upgrades[structure_name]:
        print(f"The {structure_name} is already fully upgraded.")
        return

    upgrade_info = building_upgrades[structure_name][next_level]

    # check materials
    for item, amount in upgrade_info["requires"].items():
        if item not in inventory.items or inventory.items[item] < amount:
            print(f"You need {amount}x {item} to upgrade the {structure_name}.")
            return

    # remove materials
    for item, amount in upgrade_info["requires"].items():
        inventory.remove_item(item, amount)

    # apply upgrade
    buildings[structure_name] += 1

    print(f"{structure_name} upgraded to level {buildings[structure_name]}!")