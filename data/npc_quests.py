# npc_quests.py

# quests
npc_quests = {
    "rowan": {
        "quest_1" :{
            "quest_id": "rowan_wood_delivery",
            "description": "Bring Rowan 10 wood for his shop.",
            "requires": {"wood": 10},
            "reward": {"money": 50},
            "unlock_after": None,
        },
        "quest_2": {
            "quest_id": "rowan_seed_supply",
            "description": "Bring Rowan 5 tomatoes so he can make new seed stock.",\
            "requires": {"tomato": 5},
            "reward": {"money": 90},
            "unlock_after": "rowan_wood_delivery"
        },
        "quest_3": {
            "quest_id": "rowan_special_order",
            "description": "Bring Rowan 2 iron_ore for a special customer order.",
            "requires": {"iron_ore": 2},
            "reward": {"money": 80},
            "unlock_after": "rowan_seed_supply"
        }
    },

    "faye": {
        "quest_1": {
            "quest_id": "faye_flower_help",
            "description": "Bring Faye 3 sunflowers.",
            "requires": {"sunflower": 3},
            "reward": {"money": 60},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "faye_garden_growth",
            "description": "Bring Faye 5 green beans.",
            "requires": {"green bean": 5},
            "reward": {"money": 100},
            "unlock_after": "faye_flower_help"
        },
        "quest_3": {
            "quest_id": "faye_rare_seed",
            "description": "Bring Faye 1 golden_fish for her rare seed ritual.",
            "requires": {"golden_fish": 1},
            "reward": {"item": "rare_seed"},
            "unlock_after": "faye_garden_growth"
        }
    },

    "elias": {
        "quest_1": {
            "quest_id": "elias_big_catch",
            "description": "Bring Elias 1 catfish.",
            "requires": {"catfish": 1},
            "reward": {"money": 100},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "elias_river_help",
            "description": "Bring Elias 4 small_fish to help clean the river.",
            "requires": {"small_fish": 4},
            "reward": {"money": 60},
            "unlock_after": "elias_big_catch"
        },
        "quest_3": {
            "quest_id": "elias_master_fisher",
            "description": "Bring Elias 2 bass.",
            "requires": {"bass": 2},
            "reward": {"item": "copper_fishing_rod"},
            "unlock_after": "elias_river_help"
        }
    },

    "maren": {
        "quest_1": {
            "quest_id": "maren_axe_upgrade",
            "description": "Bring Maren 5 copper_ore.",
            "requires": {"copper_ore": 5},
            "reward": {"item": "copper_axe"},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "maren_tree_help",
            "description": "Bring Maren 15 wood.",
            "requires": {"wood": 15},
            "reward": {"money": 120},
            "unlock_after": "maren_axe_upgrade"
        },
        "quest_3": {
            "quest_id": "maren_forest_guardian",
            "description": "Bring Maren 3 iron_ore.",
            "requires": {"iron_ore": 3},
            "reward": {"item": "forest_charm"},
            "unlock_after": "maren_tree_help"
        }
    },

    "clay": {
        "quest_1": {
            "quest_id": "clay_miner_support",
            "description": "Bring Clay 4 iron_ore.",
            "requires": {"iron_ore": 4},
            "reward": {"money": 120},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "clay_mine_clear",
            "description": "Bring Clay 2 gold_ore.",
            "requires": {"gold_ore": 2},
            "reward": {"money": 200},
            "unlock_after": "clay_miner_support"
        },
        "quest_3": {
            "quest_id": "clay_depths",
            "description": "Bring Clay 1 golden_fish for a deep mine ritual.",
            "requires": {"golden_fish": 1},
            "reward": {"item": "iron_pickaxe"},
            "unlock_after": "clay_mine_clear"
        }
    },

    "luna": {
        "quest_1": {
            "quest_id": "luna_river_clean",
            "description": "Bring Luna 2 small_fish.",
            "requires": {"small_fish": 2},
            "reward": {"money": 40},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "luna_water_blessing",
            "description": "Bring Luna 1 tomato.",
            "requires": {"tomato": 1},
            "reward": {"item": "river_charm"},
            "unlock_after": "luna_river_clean"
        },
        "quest_3": {
            "quest_id": "luna_moon_favor",
            "description": "Bring Luna 1 sunflower.",
            "requires": {"sunflower": 1},
            "reward": {"money": 150},
            "unlock_after": "luna_water_blessing"
        }
    },

    "ivy": {
        "quest_1": {
            "quest_id": "ivy_farm_growth",
            "description": "Bring Ivy 2 tomatoes.",
            "requires": {"tomato": 2},
            "reward": {"item": "copper_hoe"},
            "unlock_after": None
        },
        "quest_2": {
            "quest_id": "ivy_crop_help",
            "description": "Bring Ivy 5 carrots.",
            "requires": {"carrot": 5},
            "reward": {"money": 90},
            "unlock_after": "ivy_farm_growth"
        },
        "quest_3": {
            "quest_id": "ivy_harvest_festival",
            "description": "Bring Ivy 1 golden_fish for the festival.",
            "requires": {"golden_fish": 1},
            "reward": {"item": "festival_banner"},
            "unlock_after": "ivy_crop_help"
        }
    }
}