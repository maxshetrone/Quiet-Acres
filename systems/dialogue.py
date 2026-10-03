# dialogue.py

from data.npc_dialogue import npc_dialogue
import random

# dialogue system for NPCs
def talk_to_npc(npc_name, current_location):
    # check if NPC exists
    if npc_name not in npc_dialogue:
        print("That person doesn't exist.")
        return

    npc = npc_dialogue[npc_name]

    # check if player is at the NPC's location
    if npc["location"] != current_location:
        print(f"{npc['name']} isn't here.")
        return

    line = random.choice(npc["lines"])

    print(f"{npc['name']}: \"{line}\"")