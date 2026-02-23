
"""
Adventure Game
Author: Mel Heisey
Version: 0.2
Description: This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
# Deviations from the example code have been taken where I feel appropriate.



class Player:
    def __init__(self, name, inventory, location = "start"):
        self.name = name # instance attribute
        self.inventory = inventory or []
        self.location = location
        self.health = 100
        self.has_map = False
        self.has_lantern = False
    
    def greet(self):
        print(f"Welcome, {self.name}! Your journey begins now.")

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            if item == "map":
                self.has_map = True
            elif item == "lantern":
                self.has_lantern = True
            print(f"You picked up a {item}!")

    def print_inventory(self):
        print(f"Items: {", ".join(self.inventory)}")
    
    def go(self, location):
        self.location = location

# welcome player
def welcome_player():
    # Ask for the player's name.
    name = input("What is your name adventurer? ")
    player = Player(name, [])

    # Welcome with personalized message.
    player.greet()
    return player



def describe_area(location):
    if location == "start":
        # Describe the starting area.
        starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
Two paths lie ahead, leading deeper into the unknown...
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass
    3. Stay where you are.
(Type 1, 2, 3, i for inventory, q to quit)
"""
        print(starting_area)
        return
    elif location == "woods":
        print("""
You are in the woods. It's eerie here, even with the lantern.
    0. Go back
(Type 0, i for inventory, q to quit)
""")
        return
    elif location == "mountain":
        print("""
You are in the mountain pass. It's hard to tell where you're going, even with the map.
    0. Go back
(Type 0, i for inventory, q to quit)
""")
    else:
        print("You seem to be lost. Type 'q' to quit.")



player = welcome_player()

while True:
    describe_area(player.location)
    decision = input("What would you like to do?: ").lower() # Normalize the answer.
    if decision == "i":
        player.print_inventory()
    elif decision == "q":
        break
    elif player.location == "start":
        if decision == "3":
            print(player.name + ", you decide to wait. Perhaps courage will find you later.") # concatenation example
            continue
        elif decision == "1":
            if not player.has_lantern:
                print(f"Brave choice, {player.name}! You grab a lantern and venture forward into the dark woods.")
                player.add_item("lantern")
            else:
                print(f"You venture forward into the dark woods.")
            player.go("woods")
        elif decision == "2":
            if not player.has_map:
                print(f"Clever choice {player.name}! You grab a map and venture forward into the mountain pass.")
                player.add_item("map")
            else:
                print(f"You venture forward into the mountain pass.")
            player.go("mountain")
        else:
            print("Confused, you stand still, unsure of what to do.")
    elif player.location == "woods":
        if decision == "0":
            player.go("start")
        continue
    elif player.location == "mountain":
        if decision == "0":
            player.go("start")
        continue


