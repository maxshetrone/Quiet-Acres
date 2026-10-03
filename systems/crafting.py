# crafting.py

from data.crafting_recipes import crafting_recipes

# crafting system
def craft(item_name, inventory):
    # check if item is craftable
    if item_name not in crafting_recipes:
        print("You can't craft that.")
        return

    recipe = crafting_recipes[item_name]
    requirements = recipe["requires"]

    # check if player has all required materials
    for req_item, req_amount in requirements.items():
        if req_item not in inventory.items or inventory.items[req_item] < req_amount:
            print(f"You need {req_amount}x {req_item} to craft {item_name}.")
            return

    # remove required items
    for req_item, req_amount in requirements.items():
        inventory.remove_item(req_item, req_amount)

    inventory.add_item(item_name)

    print(f"You crafted a {item_name}!")