import time
from engine.commands import process_command
from data.locations import locations
from systems.save_load import save_game
from systems.farming import grow_crops
from engine.inventory import Inventory

# initialize game state
current_location = "farm"
inventory = Inventory()
field = []
animals = {"chicken": [], "cow": []}
buildings = {"coop": 0, "barn": 0, "silo": 0, "well": 0, "pet_house": 0, "workshop": 0}
last_autosave = time.time()

def game_callback(command):
    global current_location, last_autosave, animals, buildings

    # autosave check
    now = time.time()
    if now - last_autosave >= 300:
        save_game(inventory, field, current_location, animals, buildings)
        last_autosave = now

    # grow crops
    grow_crops(field)

    # process command
    response = process_command(
        command,
        current_location,
        locations,
        inventory,
        field,
        animals,
        buildings
    )

    return response
