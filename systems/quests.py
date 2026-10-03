# quests.py

from data.npc_quests import npc_quests
from data.npc_dialogue import npc_dialogue

def get_next_available_quest(npc_name, completed_quests):
    quests = npc_quests[npc_name]

    for key, quest in quests.items():
        unlock = quest["unlock_after"]

        if unlock is None:
            if quest["quest_id"] not in completed_quests:
                return quest

        else:
            if unlock in completed_quests:
                if quest["quest_id"] not in completed_quests:
                    return quest

    return None

# start quest
def start_quest(npc_name, current_location, active_quest, completed_quests):
    # only one active quest allowed
    if active_quest["id"] is not None:
        print("You already have an active quest. Complete it first.")
        return

    # check NPC exists
    if npc_name not in npc_quests:
        print("This NPC has no quests.")
        return

    npc = npc_dialogue[npc_name]

    # check location
    if npc["location"] != current_location:
        print(f"{npc['name']} isn't here.")
        return

    # find next quest in chain
    quest = get_next_available_quest(npc_name, completed_quests)

    if quest is None:
        print(f"{npc['name']} has no more quests for you.")
        return

    active_quest["id"] = quest["quest_id"]
    active_quest["npc"] = npc_name 

    print(f"Quest accepted: {quest['description']}")

def complete_quest(inventory, active_quest, completed_quests):
    quest_id = active_quest["id"]

    if quest_id is None:
        print("You don't have an active quest.")
        return

    # find quest data
    quest_data = None
    for npc_name, quests in npc_quests.items():
        for q in quests.values():
            if q["quest_id"] == quest_id:
                quest_data = q
                break

    if quest_data is None:
        print("Quest not found.")
        return

    # check requirments
    for item, amount in quest_data["requires"].items():
        if item not in inventory.items or inventory.items[item] < amount:
            print("You don't have the required items yet.")
            return

    # remove required items
    for item, amount in quest_data["requires"].items():
        inventory.remove_item(item, amount)

    # give reward
    reward = quest_data["reward"]

    if "money" in reward:
        inventory.money += reward["money"]
        print(f"You earned {reward['money']} coins!")

    if "items" in reward:
        inventory.add_item(reward["item"])
        print(f"You received a {reward['item']}!")

    # mark quest completed
    completed_quests.append(quest_id)

    # clear active quest
    active_quest["id"] = None
    active_quest["npc"] = None
    
    print("Quest completed!")