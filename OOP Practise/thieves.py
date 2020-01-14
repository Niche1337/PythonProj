import random

from attributes import Agile, Sneaky
from characters import Character

class Thief(Agile, Sneaky, Character):
    sneaky = True

    def pickPocket(self):
            return bool(random.randint(0,1)) and self.sneaky
        



