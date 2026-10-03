# inventory.py

# inventory system
class Inventory:
    def __init__(self):
        self.items = {} # example: {"carrot_seed": 5}
        self.money = 250 # starting amount of money

    # add an item to the inventory
    def add_item(self, item_name, amount=1):
        if item_name in self.items:
            self.items[item_name] += amount
        else:
            self.items[item_name] = amount

        print(f"Added {amount}x {item_name} to your inventory.")

    # remove an item from the inventory
    def remove_item(self, item_name, amount=1):
        if item_name not in self.items:
            print(f"You don't have any {item_name}.")
            return False

        if self.items[item_name] < amount:
            print(f"You don't have enough {item_name}.")
            return False

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        print(f"Removed {amount}x {item_name} from your inventory.")
        return True

    # show whats in the inventory
    def show_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
            return

        print("\n--- Your Inventory ---")
        print(f"Money: {self.money} coins")
        for item, amount in self.items.items():
            print(f"{item}: {amount}")