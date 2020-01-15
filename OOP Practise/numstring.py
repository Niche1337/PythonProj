import logging

# logging.info("You wont see this")
# logging.warning("OH NO")

logging.basicConfig(filename="numstring.log", level=logging.DEBUG)

class NumString:
    def __init__(self, value):
        self.value = str(value)#

    
    def __str__(self):
        #import pdb; pdb.set_trace()
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        logging.info(float(self.value))
        return float(self.value)

    def __add__(self, other):
        if "." in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value