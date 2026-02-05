
"""
Adventure Game
Author: Mel Heisey
Version: 0.1
Description: This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
# Deviations from the example code have been taken where I feel appropriate.
inventory = []

# welcome player
def welcome_player():
    # Ask for the player's name.
    name = input("What is your name adventurer? ")

    # Welcome with personalized message.
    print(f"Welcome, {name}! Your journey begins now.")
    return name


def describe_area():
    # Describe the starting area.
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    Two paths lie ahead, leading deeper into the unknown...
        1. Take the left path into the dark woods.
        2. Take the right path toward the mountain pass
        3. Stay where you are.
        Type 'i' to view your inventory.
    """
    print(starting_area)

def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")

def print_inventory():
    print(f"Items: {", ".join(inventory)}")

def first_decision():
    decision = input("What would you like to do? (1, 2, 3, or i): ").lower() # Normalize the answer.
    if decision == "1":
        print(f"Brave choice, {player_name}! You grab a lantern and venture forward into the dark woods.")
        add_to_inventory("lantern")
        print("")
        return 1
    elif decision == "2":
        print(f"Clever choice {player_name}! You grab a map and venture forward into the mountains.")
        add_to_inventory("map")
        print("")
        return 2
    elif decision == "3":
        print(player_name + ", you decide to wait. Perhaps courage will find you later.") # concatenation example
        print("")
    else:
        handle_other_moves(decision)
    return 0

def handle_other_moves(move):
    if move == "i":
        print_inventory()
    # TODO: handle quit
    else:
        print("Confused, you stand still, unsure of what to do.")



# Welcome and introduction messsage.
print("""Welcome to the Adventure Game!
Your journey begins here...
""")

player_name = welcome_player()
describe_area()

# Ask the player for their first decision.
location = 0
while location == 0:
    location = first_decision()

# Allow player to check inventory
next_action = input("What would you like to do? (i): ").lower()
if next_action == "i":
    print_inventory()


# TODO: separate error and inventory handling
# TODO: location continuations


