
"""
Adventure Game
Author: Mel Heisey
Version: 0.1
Description: This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
# Deviations from the example code have been taken where I feel appropriate.

# Welcome and introduction messsage.
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# Ask for the player's name.
player_name = input("What is your name adventurer? ")

# Interpolate strings to create a personalized message.
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area.
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision.
decision = input("Do you wish to take the path? (yes or no): ").lower() # Normalize the answer.

# TODO: replace with a while loop.
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")