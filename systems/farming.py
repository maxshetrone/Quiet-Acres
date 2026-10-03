# farming.py

from data.crops import crops

# plant the crop(s)
def plant_crop(seed_name, field, inventory):
    # check if seed exists in crop definitions
    if seed_name not in crops:
        print("That seed cannot be planted.")
        return

    # check if plater has the seed
    if seed_name not in inventory.items:
        print("You do not have this seed.")
        return

    # remove seed from inventory
    inventory.remove_item(seed_name)

    # get crop info
    crop_info = crops[seed_name]
    crop_name = crop_info["name"]
    growth_time = crop_info["growth_time"]

    # add crop to field
    field.append({
        "seed": seed_name,
        "crop": crop_name,
        "growth_time": growth_time,
        "age": 0
    })

    print(f"You planted a {crop_name}. It will take {growth_time} turns to grow.")

# check the field
def check_field(field):
    if not field:
        print("Your field is empty.")
        return

    print("\n--- Field Stats ---")
    for crop in field:
        name = crop["crop"]
        age = crop["age"]
        total = crop["growth_time"]

        if age >= total:
            print(f"{name}: Ready to harvest!")
        else:
            print(f"{name}: {age}/{total} turns grown")

# harvest the crop(s)
def harvest_crop(field, inventory):
    if not field:
        print("There is nothing to harvest.")
        return

    harvested_any = False
    new_field = []

    for crop in field:
        if crop["age"] >= crop["growth_time"]:
            inventory.add_item(crop["crop"])
            print(f"You harvested a {crop['crop']}!")
            harvested_any = True
        else:
            new_field.append(crop)

    # update field
    field[:] = new_field

    if not harvested_any:
        print("Nothing is ready to harvest yet.")

# grow the crop(s)
def grow_crops(field):
    for crop in field:
        crop["age"] += 1

        # clamp age so it never exceeds growth_time
        if crop["age"] > crop["growth_time"]:
            crop["age"] = crop["growth_time"]

        # notify player when crop finishes growing
        if crop["age"] == crop["growth_time"]:
            print(f"Your {crop['crop']} has finished growing!")