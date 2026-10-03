# helpers.py

import os

# for clearing the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# pause game
def pause():
    input("\nPress Enter to continue...")

# simple divider line for formatting
def divider():
    print("\n" + "-" * 40 + "\n")