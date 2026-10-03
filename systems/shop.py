# shop.py

from data.shop_items import shop_items
from data.sell_prices import sell_prices

# open the shop and handle buying items
def open_shop(inventory):
    print("\n--- General Store ---")
    print(f"Money: {inventory.money} coins.")
    print("Items for sale:")
    for item, price in shop_items.items():
        print(f"{item} - {price} coins")

    print("\nType: buy <item>")
    print("Type: exit to leave the shop")

    # main shop loop
    while True:
        command = input("\nShop command: ").split()

        if len(command) == 0:
            print("Please type something.")
            continue

        # exit shop
        if command[0] == "exit":
            print("You left the shop.")
            return

        # buy item
        if command[0] == "buy":
            if len(command) < 2:
                print("Buy what?")
                continue

            item_name = command[1]

            if item_name not in shop_items:
                print("That item isn't sold here.")
                continue

            price = shop_items[item_name]

            if inventory.money < price:
                print("You don't have enough money.")
                continue

            # purchase successful
            inventory.money -= price
            inventory.add_item(item_name)
            print(f"You bought {item_name} for {price} coins.")
            #print(f"Money left: {inventory.money} coins")
            continue

        print("Unknown shop command.")

# sell the crops
def sell_crop(crop_name, inventory):
    # check if crop is sellable
    if crop_name not in sell_prices:
        print("You can't sell that.")
        return

    # check if the player has any of the crop to sell
    if crop_name not in inventory.items:
        print(f"You don't have any {crop_name} to sell.")
        return

    # remove one crop
    inventory.remove_item(crop_name)

    # add money
    price = sell_prices[crop_name]
    inventory.money += price

    print(f"You sold 1 {crop_name} for {price} coins.")
    print(f"Money: {inventory.money} coins.")

# sell all crops
def sell_all(inventory):
    sold_any = False

    for crop_name in list(inventory.items.keys()):
        if crop_name in sell_prices:
            amount = inventory.items[crop_name]
            price = sell_prices[crop_name]

            # add money
            inventory.money += amount * price

            print(f"You sold {amount}x {crop_name} for {price * amount} coins.")

            # remove from inventory
            inventory.remove_item(crop_name, amount)

            sold_any = True

    if not sold_any:
        print("You have no crops to sell.")
    else:
        print(f"Total money: {inventory.money} coins.")