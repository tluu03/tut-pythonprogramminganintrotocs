from Player import *
from Stats import *

def main():
    name = input("You wake up in a cavern, dazed and confused. A shadowy figure asks you: 'What is your name, young traveller?'")
    race = input("Where do you derive your lineage?")
    inventory = []
    stats = None

    # TODO: Add method tolower method to input race
    if race == "human":
        stats = Stats(1, 10, 100, 10, 0)
    elif race == "orc":
        stats = Stats(1, 15, 100, 10, 0)
    elif race == "elf":
        stats = Stats(1, 8, 100, 12, 0)

    player = Player(name, stats, inventory, race)

    print("Your name is: ", player.name)

    print("Your attack is ", stats.attack)
        
    
    
