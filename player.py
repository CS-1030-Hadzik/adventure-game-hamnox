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
        self.health = 100

    def stay_still(self):
        self.health -= 10
        print(f"You lost some health. Current health: {self.health}")
        if self.health <= 0:
            print("You have lost all your health. Game over!")
            self.quit()

    def print_health(self):
        print(f"Health: {self.health}")

    def has_won(self):
        return self.has_treasure and self.has_herbs
    
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