import random

class Character:
    def __init__(self,name,role):
        self.name = name
        self.role = role

class Place:
    def __init__(self,location):
        self.location = location

class Item:
    def __init__(self,item_name):
        self.item_name = item_name


class Storygenerator:
    def __init__(self):
        self.characters = [Character("Aron","Wizard"),
                           Character("Lily","Mage"),
                           Character("Ara","Soldier")]
        
        self.locations = [Place("Haunted Castle"),
                          Place("Giant Forest"),
                          Place("WW2 Battlefield")]

        self.items = [Item("Staff"),
                      Item("Gloves"),
                      Item("Springfield Rifle")]
        
    def storygenerator(self):
        character = random.choice(self.characters)
        place = random.choice(self.locations)
        item = random.choice(self.items)

        story = (
            f"{character.name} the {character.role} "
            f"entered the {place.location} and found a "
            f"{item.item_name}."
        )
        return story
    
generator = Storygenerator()
print("\n--- Random Story ---")
print(generator.storygenerator())
    
        