import json
import os

save_file = "save.json"

def save_game(inventory, field, current_location, animals, buildings):
    data = {
        "money": inventory.money,
        "items": inventory.items,
        "field": field,
        "animals": animals,
        "buildings": buildings,
        "current_location": current_location
    }

    buildings = data["buildings"]

    with open(save_file, "w") as f:
        json.dump(data, f, indent=4)

    print("Game saved!")

def load_game():
    if not os.path.exists(save_file):
        print("No save file found.")
        return None

    with open(save_file, "r") as f:
        data = json.load(f)

    print("Game loaded!")
    return data