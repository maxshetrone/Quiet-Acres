# animals.py

from data.animals import farm_animals, pets

def buy_animal(animal_type, animals, inventory):
    if animal_type not in farm_animals:
        print("You can't buy that animal.")
        return

    prices = {
        "chicken": 50,
        "cow": 125
    }

    if inventory.money < prices[animal_type]:
        print(f"You need {prices[animal_type]} coins to buy a {animal_type}.")
        return

    inventory.money -= prices[animal_type]

    animals[animal_type].append({
        "name": animal_type,
        "happiness": 0,
        "fed": False
    })

    print(f"You bought a {animal_type}!")

def feed_animal(animal_type, animals, inventory):
    if animal_type not in animals or len(animals[animal_type]) == 0:
        print(f"Youd don't own any {animal_type}s.")
        return

    feed_item = farm_animals[animal_type]["feed_required"]

    if feed_item not in inventory.items:
        print(f"You need {feed_item} to feed your {animal_type}.")
        return

    inventory.remove_item(feed_item)

    for animal in animals[animal_type]:
        animal["fed"] = True
        animal["happiness"] += farm_animals[animal_type]["happiness_gain"]

    print(f"You fed all your {animal_type}s!")

def collect_products(animal_type, animals, inventory):
    if animal_type not in animals or len(animals[animal_type]) == 0:
        print(f"Youd don't own any {animal_type}s.")
        return

    product = farm_animals[animal_type]["product"]
    total = 0

    for animal in animals[animal_type]:
        if animal["fed"]:
            inventory.add_item(product)
            total += 1
            animal["fed"] = False

    if total == 0:
        print(f"No {product} ready yet.")
    else:
        print(f"You collected {total} {product}(s)!")

# buy pets
def buy_pet(pet_type, breed, pets_owned, inventory):
    if pet_type not in pets:
        print("You can't buy that pet.")
        return

    if breed not in pets[pet_type]["breeds"]:
        print("That breed doesn't exist")
        return

    price = pets[pet_type]["price"]

    if inventory.money < price:
        print(f"You need {price} coins to buy a {breed} {pet_type}.")
        return

    inventory.money -= price

    pets_owned.append({
        "type": pet_type,
        "breed": breed,
        "affection": 0
    })

    print(f"You adopted a {breed} {pet_type}!")