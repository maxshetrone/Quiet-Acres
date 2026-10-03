# buildings.py

buildings_data = {
    "coop": {
        "description": "A small coop for chickens.",
        "requires": {
            "wood": 20,
            "stone": 10,
            "nails": 5
        }
    },
    "barn": {
        "description": "A sturdy barn for cows.",
        "requires": {
            "wood": 40,
            "stone": 20,
            "iron_ore": 5,
            "nails": 10
        }
    },
    "silo": {
        "description": "Stores hay and grain for animals.",
        "requires": {
            "wood": 25,
            "stone": 15
        }
    },
    "well": {
        "description": "Provides free water for crops.",
        "requires": {
            "stone": 30,
            "iron_ore": 3
        }
    },
    "pet_house": {
        "description": "A cozy home for your pets.",
        "requires": {
            "wood": 15,
            "planks": 5,
            "nails": 4
        }
    },
    "workshop": {
        "description": "Allows advanced crafting.",
        "requires": {
            "wood": 50,
            "stone": 25,
            "iron_ore": 10
        }
    }
}