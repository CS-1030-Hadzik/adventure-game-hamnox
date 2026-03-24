
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
    
    def quit(self):
        self.location = "quit"

# welcome player
def welcome_player():
    # Ask for the player's name.
    name = input("What is your name adventurer? ")
    player = Player(name, [])

    # Welcome with personalized message.
    player.greet()
    return player








def explore_start(player: Player):
    starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
Two paths lie ahead, leading deeper into the unknown...
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
(Type 1, 2, 3, i for inventory, q to quit)
"""
    print(starting_area)
    while True:
        decision = input("What would you like to do?: ").lower() # Normalize the answer.
        print("")

        if decision == "i":
            player.print_inventory()
            continue
        elif decision == "q":
            player.quit()
            break
        elif decision in ["1", "2", "3"]:
            if decision == "1":
                if not player.has_lantern:
                    print(f"Brave choice, {player.name}! You grab a lantern and venture forward into the dark woods.")
                    player.add_item("lantern")
                else:
                    print(f"You venture forward into the dark woods.")
                player.go("woods")
                break
            elif decision == "2":
                if not player.has_map:
                    print(f"Clever choice {player1.name}! You grab a map and venture forward into the mountain pass.")
                    player.add_item("map")
                else:
                    print(f"You venture forward into the mountain pass.")
                player.go("mountain")
                break
            else:
                print(player.name + ", you decide to wait. Perhaps courage will find you later.") # concatenation example
                continue
        else:
            print("Confused, you stand still, unsure of what to do.")


def explore_woods(player: Player):
    woods_area = """
You are in the woods. According to the legends, there is hidden valley in these woods.
    1. Search for the hidden valley.
    2. Go back.
(Type 1, 2, i for inventory, q to quit)
"""
    print(woods_area)
    while True:
        decision = input("What would you like to do?: ").lower() # Normalize the answer.
        print("")

        if decision == "i":
            player.print_inventory()
            continue
        elif decision == "q":
            player.quit()
            break
        if decision == "2":
            print(f"Back to the start you go!") 
            player1.go("start")
            break
        elif decision == "1" and player1.has_map:
            print(f"With the help of the map, you find the hidden valley. It is filled with luscious plant life.")
            if not player1.has_herbs:
                player1.add_item("rare herbs")
            player1.go("valley")
            break
        elif decision == "1":
            print("You cannot find the valley :(")
        else:
            print("Confused, you stand still, unsure of what to do.")


def explore_mountain(player: Player):
    mountain_area = """
You are in the mountain pass. There seems to be a cave over yonder.
    1. Explore the cave.
    2. Head back.
(Type 1, 2, i for inventory, q to quit)
""" 
    print(mountain_area)
    while True:
        decision = input("What would you like to do?: ").lower() # Normalize the answer.
        print("")
        if decision == "i":
            player.print_inventory()
            continue
        elif decision == "q":
            player.quit()
            break
        if decision == "2":
            print(f"You go back.")
            player1.go("start")
            break
        elif decision == "1":
            print(f"You venture towards the cave.")
            player1.go("cave")
            break
        else:
            print("Confused, you stand still, unsure of what to do.")
    

def explore_cave(player: Player):
    cave_area = """
You are in the entrance to the cave. It is dark and damp.
    1. Explore deeper into the cave.
    2. Head back.
(Type 1, 2, i for inventory, q to quit)
""" 
    print(cave_area)
    while True:
        decision = input("What would you like to do?: ").lower() # Normalize the answer.
        print("")
        if decision == "i":
            player.print_inventory()
            continue
        elif decision == "q":
            player.quit()
            break
        if decision == "2":
            print(f"You go back.")
            player1.go("mountain")
            break
        elif decision == "1" and player1.has_lantern:
            print("""You venture further into the cave.
The light from your lantern reveals a hidden treasure chest!
You open it and find a trove of gold and jewels. You head back to the start of the cave.
""")
            if not player1.has_treasure:
                player1.add_item("treasure")
            else:
                print("You already checked there, no point in going again.")
            player1.go("cave")
            break
        elif decision == "1":
            print("It's too dark! You cannot see anything.")
        else:
            print("Confused, you stand still, unsure of what to do.")

def explore_valley(player: Player):
    valley_area = """You are in the valley now. It is beautiful here.
        1. Head back
    (Type 1, i for inventory, q to quit)
    """
    print(valley_area)

    while True:
        decision = input("What would you like to do?: ").lower() # Normalize the answer.
        print("")
        if decision == "i":
            player.print_inventory()
            continue
        elif decision == "q":
            player.quit()
            break
        elif decision == "1":
            print(f"You go back.")
            player1.go("woods")
            break
        else:
            print("Confused, you stand still, unsure of what to do.")

player1 = welcome_player()
prev_location = ""

while True:
    # do not redescribe location
    # if prev_location != player.location:
    #     prev_location = player.location

    if player1.location == "quit":
        print("Thanks for playing!")
        break
    elif player1.location == "start":
         explore_start(player1)

## TODO dark woods, pass, cave, valley
    elif player1.location == "woods":
        explore_woods(player1)

    elif player1.location == "mountain":
        explore_mountain(player1)

    elif player1.location == "cave":
        explore_cave(player1)

    elif player1.location == "valley":
        explore_valley(player1)

    else:
        print(f"You seem to be lost, {player1.name}.")



