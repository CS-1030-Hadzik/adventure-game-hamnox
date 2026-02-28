
"""
Adventure Game
Author: Mel Heisey
Version: 0.3
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
        self.has_treasure = False
        self.has_herbs = False
    
    def greet(self):
        print(f"Welcome, {self.name}! Your journey begins now.")

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            if item == "map":
                self.has_map = True
            elif item == "lantern":
                self.has_lantern = True
            elif item == "treasure":
                self.has_treasure = True
            elif item == "rare herbs":
                self.has_herbs = True
            print(f"You picked up {"" if item == "rare herbs" else "a "}{item}!")

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
    # Describe the starting area.
    starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
Two paths lie ahead, leading deeper into the unknown...
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
(Type 1, 2, 3, i for inventory, q to quit)
"""
    woods_area = """
You are in the woods. According to the legends, there is hidden valley in these woods.
    1. Search for the hidden valley.
    2. Go back.
(Type 0, i for inventory, q to quit)
"""
    mountain_area = """
You are in the mountain pass. There seems to be a cave over yonder.
    1. Explore the cave.
    2. Head back.
(Type 1, 2, i for inventory, q to quit)
"""
    cave_area = """You are in the cave now. It is eerie in here.
    0. Head back.
(Type 0, i for inventory, q to quit)
"""
    valley_area = """You are in the valley now. It is beautiful here.
    0. Head back
(Type 0, i for inventory, q to quit)
"""

    if location == "start":
        print(starting_area)
        return
    elif location == "woods":
        print(woods_area)
        return
    elif location == "mountain":
        print(mountain_area)
        return
    elif location == "cave":
        print(cave_area)
    elif location == "valley":
        print(valley_area)
    else:
        print(f"You seem to be lost, {player.name}. Type 'q' to quit.")
    #TODO make this a dictionary



player = welcome_player()
prev_location = ""

while True:
    # do not redescribe location
    if prev_location != player.location:
        describe_area(player.location)
        prev_location = player.location
    decision = input("What would you like to do?: ").lower() # Normalize the answer.
    print("")
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
        if decision == "2":
            print(f"Back to the start you go!") 
            player.go("start")
        elif decision == "1" and player.has_map:
            print(f"With the help of the map, you find the hidden valley. It is filled with luscious plant life.")
            if not player.has_herbs:
                player.add_item("rare herbs")
            player.go("valley")
        elif decision == "1":
            print("You cannot find the valley :(")
        else:
            print("Confused, you stand still, unsure of what to do.")
        continue
    elif player.location == "mountain":
        if decision == "2":
            print(f"You go back.")
            player.go("start")
        elif decision == "1" and player.has_lantern:
            print(f"With the help of the lantern, you find your way into the cave.")
            if not player.has_treasure:
                player.add_item("treasure")
            player.go("cave")
        elif decision == "1":
            print("It's too dark!")
        else:
            print("Confused, you stand still, unsure of what to do.")
        continue
    elif player.location in ["cave", "valley"]:
        if decision == "0":
            print(f"You go back.")
            player.go("start")
        else:
            print("Confused, you stand still, unsure of what to do.")


