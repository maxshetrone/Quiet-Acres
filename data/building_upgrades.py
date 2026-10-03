# building_upgrades.py

building_upgrades = {
    "coop": {
        "level_1": {
            "requires": {"wood": 15, "stone": 10, "nails": 5},
            "effect": {"max_chickens": 5}
        },
        "level_2": {
            "requires": {"wood": 25, "stone": 20, "planks": 10},
            "effect": {"max_chickens": 10}
        },
        "level_3": {
            "requires": {"wood": 40, "stone": 30, "steel": 5},
            "effect": {"max_chickens": 15}
        }
    },

    "barn": {
        "level_1": {
            "requires": {"wood": 30, "stone": 20, "nails": 10},
            "effect": {"max_cows": 3}
        },
        "level_2": {
            "requires": {"wood": 50, "stone": 35, "planks": 15},
            "effect": {"max_cows": 6}
        },
        "level_3": {
            "requires": {"wood": 70, "stone": 50, "steel": 10},
            "effect": {"max_cows": 10}
        }
    },

    "silo": {
        "level_1": {
            "requires": {"wood": 20, "stone": 15},
            "effect": {"storage": 50}
        },
        "level_2": {
            "requires": {"wood": 35, "stone": 25, "bricks": 10},
            "effect": {"storage": 100}
        }
    },

    "workshop": {
        "level_1": {
            "requires": {"wood": 40, "stone": 20},
            "effect": {"craft_speed": 1.2}
        },
        "level_2": {
            "requires": {"wood": 60, "stone": 40, "steel": 5},
            "effect": {"craft_speed": 1.5}
        }
    },

    "pet_house": {
        "level_1": {
            "requires": {"wood": 20, "planks": 10},
            "effect": {"pet_affection_gain": 2}
        },
        "level_2": {
            "requires": {"wood": 40, "planks": 20, "bricks": 10},
            "effect": {"pet_affection_gain": 4}
        }
    },

    "well": {
        "level_1": {
            "requires": {"stone": 25, "iron_ore": 5},
            "effect": {"water_bonus": 1}
        },
        "level_2": {
            "requires": {"stone": 40, "iron_ore": 10, "steel": 3},
            "effect": {"water_bonus": 2}
        }
    }
}