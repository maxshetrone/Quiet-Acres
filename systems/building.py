# building.py

from data.buildings import buildings_data

def build_structure(structure_name, buildings, inventory):
    # check if structure exists
    if structure_name not in buildings_data:
        print("You can't build that")
        return

    # already built
    if structure_name in buildings:
        print(f"You already built the {structure_name}.")
        return

    requirements = buildings_data[structure_name]["requires"]

    # check materials
    for item, amount in requirements.items():
        if item not in inventory.items or inventory.items[item] < amount:
            print(f"You need {amount}x {item} to build the {structure_name}.")
            return

    # remove materials
    for item, amount in requirements.items():
        inventory.remove_item(item, amount)

    # add building
    buildings.append(structure_name)

    print(f"You built the {structure_name}!")