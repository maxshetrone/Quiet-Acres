# movement.py

# moving function
def move_to(location, current_location, locations):
    if location in locations:
        print(f"\nYou walk to the {location.replace('_', ' ')}.")
        print(locations[location])
        return location
    else:
        print("\nThat location doesn't exist.")
        return current_location