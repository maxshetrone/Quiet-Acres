# main.py

import time
from engine.game_loop import start_game
from engine.commands import process_command
from data.locations import locations
from systems.save_load import save_game, load_game
from systems.farming import grow_crops
from engine.inventory import Inventory

# initialize game state
current_location = "farm"
inventory = Inventory()
field = []
last_autosave = time.time()

def game_callback(command):
    global current_location, last_autosave, animals, buildings

    # autosave check
    now = time.time()
    if now - last_autosave >= 300:  # 300 seconds = 5 minutes
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
    )

    return response

if __name__ == "__main__":
    start_game()