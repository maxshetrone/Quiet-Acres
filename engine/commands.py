# commands.py

from dataclasses import field

from engine.movement import move_to
from data.items import items
from data.locations import locations
from data.sell_prices import sell_prices
from systems.shop import open_shop
from systems.shop import sell_crop, sell_all
from systems.fishing import fish
from systems.crafting import craft
from systems.woodcutting import chop_wood
from systems.mining import mine
from systems.dialogue import talk_to_npc
from systems.animals import buy_animal, feed_animal, collect_products, buy_pet
from data.npc_dialogue import npc_dialogue
from systems.quests import start_quest, complete_quest
from systems.building import build_structure
from systems.building_upgrades import upgrade_building
from data.buildings import buildings_data
from data.crafting_recipes import crafting_recipes
from data.fish import fish_data
from systems.farming import plant_crop, check_field, harvest_crop
from systems.save_load import save_game, load_game
from data.npc_quests import npc_quests

def process_command(command, current_location, locations_dict, inventory, field, animals, buildings):
    parts = command.split()

    if len(parts) == 0:
        print("You must type something.")
        return current_location

    # shop command
    if parts[0] == "shop":
        open_shop(inventory)
        return current_location

    # enter shop (general_store)
    if parts[0] == "enter":
        if current_location == "general_store":
            open_shop(inventory)
            return current_location
        else:
            print("There is nothing to enter here.")
            return current_location

    # enter shop (command: "enter store")
    if parts[0] == "enter" and len(parts) > 1:
        if parts[1] == "store" and current_location == "general_store":
            open_shop(inventory)
            return current_location
        else:
            print("You can't enter the store from here.")
            return current_location

    # planting
    if parts[0] == "plant":
        if len(parts) < 2:
            print("Plant what?")
            return current_location

        seed = parts[1]
        plant_crop(seed, field, inventory)
        return current_location

    # check field
    if parts[0] == "check" and len(parts) > 1 and parts[1] == "field":
        check_field(field)
        return current_location

    # harvest crop
    if parts[0] == "harvest":
        harvest_crop(field, inventory)
        return current_location

    # sell one crop
    if parts[0] == "sell":
        if len(parts) < 2:
            print("Sell what?")
            return current_location

        if parts[1] == "all":
            sell_all(inventory)
            return current_location

        crop_name = parts[1]
        sell_crop(crop_name, inventory)
        return current_location

    # fishing
    if parts[0] == "fish":
        fish(inventory, current_location)
        return current_location

    # crafting
    if parts[0] == "craft":
        if len(parts) < 2:
            print("Craft what?")
            return current_location

        item_name = parts[1]
        craft(item_name, inventory)
        return current_location

    # chop wood
    if parts[0] == "chop":
        chop_wood(inventory, current_location)
        return current_location

    # mining
    if parts[0] == "mine":
        mine(inventory, current_location)
        return current_location

    # quest dictionary
    active_quests = {"id": None, "npc": None}
    completed_quests = []

    # accept quest
    if parts[0] == "quest":
        if len(parts) < 2:
            print("Quest from who?")
            return current_location

        npc_name = parts[1]
        start_quest(npc_name, current_location, active_quests, completed_quests)
        return current_location

    # complete quest
    if parts[0] == "complete":
        complete_quest(inventory, active_quests, completed_quests)
        return current_location

    # buy animal
    if parts[0] == "buy" and parts[1] == "animal":
        animal_type = parts[2]
        buy_animal(animal_type, animals, inventory)
        return current_location

    pets_owned = []
    # buy pet
    if parts[0] == "buy" and parts[1] == "pet":
        pet_type = parts[2]
        breed = parts[3]
        buy_pet(pet_type, breed, pets_owned, inventory)
        return current_location

    # feed aniaml
    if parts[0] == "feed":
        animal_type = parts[1]
        feed_animal(animal_type, animals, inventory)
        return current_location

    # collect products
    if parts[0] == "collect":
        animal_type = parts[1]
        collect_products(animal_type, animals, inventory)
        return current_location

    # build structure
    if parts[0] == "build":
        if len(parts) < 2:
            print("Build what?")
            return current_location

        structure_name = parts[1]
        build_structure(structure_name, buildings, inventory)
        return current_location

    # building upgrades
    if parts[0] == "upgrade" and parts[1] == "building":
        structure_name = parts[2]
        upgrade_building(structure_name, buildings, inventory)
        return current_location
    
    # help commands
    if parts[0] == "help":
        # Basic help
        if len(parts) == 1:
            print("\n--- Help Menu ---")
            print("help commands           - Show all commands")
            print("help locations          - Show all locations")
            print("help items              - Show all items")
            print("help selling            - Show all sellable crops")
            print("help fishing            - Show fishing info")
            print("help crafting           - Show all crafting recipes")
            print("help wood               - Show wood gathering info")
            print("help mining             - Show mining info")
            print("help npcs               - Show all NPCs")
            print("help quests             - Show all quests")
            print("help animals            - Show animal info")
            print("help pets               - Show pet info")
            print("help building           - Show building info")
            print("help upgrades           - Show building upgrade info")
            print("upgrade building <name> - Upgrade a farm structure")
            print("build <structure>       - Build a structure")
            print("buy pet <type> <breed>  - Buy a pet")
            print("buy animal <type>       - Buy an animal")
            print("feed <animal>           - Feed an animal")
            print("collect <animal>        - Collect products from an animal")
            print("complete                - Complete active quest")
            print("quest <npc>             - Accept an NPC's next quest")
            print("quest <npc>             - Accept an NPC's quest")
            print("talk <npc>              - Talk to an NPC")
            print("save                    - Save your game")
            print("load                    - Load your game")
            print("plant <seed>            - Plant a seed in your field")
            print("check field             - Check crop growth progress")
            print("mine                    - Mine for ores in the mines")
            print("chop                    - Chop wood in the forest")
            print("craft <item>            - Craft an item using available materials")
            print("harvest                 - Harvest grown crops")
            print("go <location>           - Move to a location")
            print("fish                    - Fish at the riverbank")
            print("enter store             - Enter a building (e.g. general_store)")
            print("buy <item>              - Buy an item inside the shop")
            print("sell <crop>             - Sell one harvested crops")
            print("sell all                - Sell all harvested crops")
            print("exit                    - Leave the shop")
            print("inventory               - Show your inventory")
            print("add <item>              - Add an item (debugging)")
            print(" `                      - Return to main menu")
            return current_location

        # help commands
        if parts[1] == "commands":
            print("\n--- Commands ---")
            print("go <location>   - Move to a location")
            print("inventory       - Show your inventory")
            print("add <item>      - Add an item (testing)")
            print("help            - Show help menu")
            print("help locations  - Show all locations")
            print("help items      - Show all items")
            print("m               - Return to main menu")
            return current_location

        # help locations
        if parts[1] == "locations":
            print("\n--- Available Locations ---")
            for loc in locations_dict.keys():
                print(loc)
            return current_location

        # help items
        if parts[1] == "items":
            print("\n--- Available Items ---")
            for item in items.keys():
                print(item)
            return current_location

        # help selling
        if parts[1] == "selling":
            print("\n--- Sellable Crops ---")
            for crop, price in sell_prices.items():
                print(f"{crop}: {price} coins each")
            return current_location

        # help fishing
        if parts[1] == "fishing":
            print("\n--- Fishing Info ---")
            print("You can fish at the riverbank")
            print("You need a basic_fishing_rod to fish")
            print("Fish you can cactch:")
            for f in fish_data.keys():
                print(f)
            return current_location

        # help crafting
        if parts[1] == "crafting":
            print("\n--- Crafting Info ---")
            for item, recipe in crafting_recipes.items():
                print(f"{item}:")
                for req, amt in recipe["requires"].items():
                    print(f"  - {req}: {amt}")
            return current_location

        # help wood
        if parts[1] == "wood":
            print("You can chop wood in the forest.")
            print("You need an axe to chop wood.")
            print("Better axes give more wood.")
            print("Axes you can craft:")
            print("basic_axe -> copper_axe -> iron_axe -> gold_axe")
            return current_location 

        # help mining
        if parts[1] == "mining":
            print("\n--- Mining Info ---")
            print("You can mine ores in the mines.")
            print("You need a pickaxe to mine ores.")
            print("Better pickaxes give more ore.")
            print("Pickaxe progression:")
            print("basic_pickaxe -> copper_pickaxe -> iron_pickaxe -> gold_pickaxe")
            return current_location

        # help npcs
        if parts[1] == "npcs":
            print("\n--- NPCs ---")
            for npc, info in npc_dialogue.items():
                print(f"{info['name']} - Found at {info['location']}")
            return current_location

        # help quests
        if parts[1] == "quests":
            print("\n--- NPC Quest Chains ---")
            for npc, quests in npc_quests.items():
                print(f"{npc}:")
                for q in quests.values():
                    print(f"  {q['quest_id']} - {q['description']}")

            return current_location

        # help animals
        if parts[1] == "animals":
            print("\n--- Farm Animals ---")
            print("chicken - produces eggs, needs grain")
            print("cow - produces milk, needs hay")
            return current_location

        # help pets
        if parts[1] == "pets":
            print("\n--- Pets ---")
            print("Cats: tabby, black, white, calico, siamese, orange")
            print("Dogs: labrador, golden retriever, beagle, poodle, bulldog, german shepherd")
            return current_location

        # help building
        if parts[1] == "building":
            print("\n--- Building Info ---")
            for name, info in buildings_data.items():
                print(f"{name}: {info['description']}")
                for item, amt in info["requires"].items():
                    print(f"  - {item}: {amt}")

            return current_location
        
    # movement command
    if parts[0] == "go":
        if len(parts) < 2:
            print("Go where?")
            return current_location

        destination = parts[1]
        return move_to(destination, current_location, locations_dict)

    # show the inventory
    if parts[0] == "inventory":
        inventory.show_inventory()
        return current_location

    # add item (for testing)
    if parts[0] == "add":
        if len(parts) < 2:
            print("Add what?")
            return current_location

        item = parts[1]
        inventory.add_item(item)
        return current_location

    # save game
    if parts[0] == "save":
        save_game(inventory, field, current_location)
        return current_location

    # load game
    if parts[0] == "load":
        data = load_game()
        if data is None:
            return current_location

        # restore data
        inventory.money = data["money"]
        inventory.items = data["items"]
        field[:] = data["field"]
        current_location = data["location"]

        print("Your game has been restored.")
        return current_location

    print("I don't understand that command yet.")
    return current_location