import random

class Character:
    def __init__(self, name="", **kwargs):
        if not name:
            raise ValueError("'name' is required")

        self.name = name

        #allows for extra key value pairs on the class when callled
        for key, value in kwargs.items():
            setattr(self, key, value)
