# game_loop.py

import sys
import time
from systems.save_load import load_game, save_game
from utils.helpers import clear
from systems.farming import grow_crops
from data.locations import locations
from engine.commands import process_command
from engine.inventory import Inventory

# main loop
def start_game():
    clear()
    print("--- Welcome to Quiet Acres! ---")
    print("Pick a option:")
    print("1. Start a new game.")
    print("2. Load a saved game.")
    print("3. Quit the game.")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        start_new_game()
    elif choice == "2":
        data = load_game()
        if data is None:
            time.sleep(1)
            start_game()
            return
        start_loaded_game(data)
    elif choice == "3":
        print("Thanks for playing!")
        time.sleep(1)
        sys.exit()
    else:
        print("Invalid choice.")
        time.sleep(1)
        start_game()

def start_new_game():
    clear()
    print("[Press ` to return to main menu] [Type 'help' for a list of commands].\n")
    last_autosave = time.time()

    # variables needed
    current_location = "farm"
    inventory = Inventory()
    field = []  # will store planted crops
    animals = {
        "chicken": [],
        "cow": []
    }
    buildings = {
        "coop": 0,
        "barn": 0,
        "silo": 0,
        "well": 0,
        "pet_house": 0,
        "workshop": 0
    }

    # add base items
    inventory.add_item("basic_axe")
    inventory.add_item("basic_hoe")
    inventory.add_item("basic_fishing_rod")
    inventory.add_item("basic_pickaxe")
    print("----------------------------------------")

    print(locations[current_location])

    while True:
        command = input("\nWhat do you want to do? ")

        # grow crops every turn
        grow_crops(field)

        if command == "`":
            start_game()
            return
        
         # autosave check
        current_time = time.time()
        if current_time - last_autosave >= 300:  # 300 seconds = 5 minutes
            save_game(inventory, field, current_location, animals, buildings)
            print("[Autosaved]")
            last_autosave = current_time
        
        current_location = process_command(command, current_location, locations, inventory, field, animals, buildings)

def start_loaded_game(data):
    clear()
    print("[Press ` to return to main menu] [Type 'help' for a list of commands].\n")
    last_autosave = time.time()

    buildings = {
        "coop": 0,
        "barn": 0,
        "silo": 0,
        "well": 0,
        "pet_house": 0,
        "workshop": 0
    }
    animals = {
        "chicken": [],
        "cow": []
    }


    inventory = Inventory()
    inventory.money = data["money"]
    inventory.items = data["items"]

    field = data["field"]
    current_location = data["current_location"]

    print(locations[current_location])

    while True:
        command = input("\nWhat do you want to do? ")

        if command == "`":
            start_game()
            return

        grow_crops(field)

         # autosave check
        current_time = time.time()
        if current_time - last_autosave >= 300:  # 300 seconds = 5 minutes
            save_game(inventory, field, current_location, animals, buildings)
            print("[Autosaved]")
            last_autosave = current_time

        current_location = process_command(command, current_location, locations, inventory, field, animals, buildings)