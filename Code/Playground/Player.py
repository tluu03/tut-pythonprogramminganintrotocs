from Stats import *
from Inventory import *

class Player:
    def __init__(self, name, stats, inventory, race):
        self.name = name
        self.stats = stats
        self.inventory = inventory
        self.race = race
