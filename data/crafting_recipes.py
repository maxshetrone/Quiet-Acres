# crafting_recipes.py

# crafting recipes
crafting_recipes = {
    "copper_fishing_rod": {
        "requires": {
            "basic_fishing_rod": 1,
            "wood": 15,
            "copper_ore": 8
        }
    },
    "iron_fishing_rod": {
        "requires": {
            "copper_fishing_rod": 1,
            "wood": 18,
            "iron_ore": 9
        }
    },
    "gold_fishing_rod": {
        "requires": {
            "iron_fishing_rod": 1,
            "wood": 20,
            "gold_ore": 7
        }
    },
    # hoe recipes
    "copper_hoe": {
        "requires": {
            "basic_hoe": 1,
            "wood": 14,
            "copper_ore": 5
        }
    },
    "iron_hoe": {
        "requires": {
            "copper_hoe": 1,
            "wood": 16,
            "iron_ore": 9
        }
    },
    "gold_hoe": {
        "requires": {
            "iron_hoe": 1,
            "wood": 18,
            "gold_ore": 7
        }
    },
    # axe recipes
    "copper_axe": {
        "requires": {
            "basic_axe": 1,
            "wood": 16,
            "copper_ore": 8
        }
    },
    "iron_axe": {
        "requires": {
            "copper_axe": 1,
            "wood": 20,
            "iron_ore": 9
        }
    },
    "gold_axe": {
        "requires": {
            "iron_axe": 1,
            "wood": 24,
            "gold_ore": 7
        }
    },
    # pickaxe recipes
    "copper_pickaxe": {
        "requires": {
            "basic_pickaxe": 1,
            "wood": 14,
            "copper_ore": 8
        }
    },
    "iron_pickaxe": {
        "requires": {
            "copper_pickaxe": 1,
            "wood": 16,
            "iron_ore": 9
        }
    },
    "gold_pickaxe": {
        "requires": {
            "iron_pickaxe": 1,
            "wood": 18,
            "gold_ore": 7
        }
    },
    # building recipes
    "nails": {
        "requires": {
            "iron_ore": 2
        }
    },
    "planks": {
        "requires": {
            "wood": 3
        }
    },
    "bricks": {
        "requires": {"stone": 3}
    },
    "steel": {
        "requires": {"iron_ore": 4}
    }
}