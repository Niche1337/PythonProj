import random

class Die:
    def __init__(self, sides=2, value=0):
        """Takes a param to decide how many sides a die will have"""
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    ##equals
    def __eq__(self, other):
        return int(self) == other
    ##not equals
    def __ne__(self,other):
        return int(self) != other
    ##greather than
    def __gt__(self, other):
        return int(self) > other
    ##less then
    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)




class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)

