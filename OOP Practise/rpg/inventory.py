class Inventory:
    def __init__(self):
        self.slots = []
    
    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __iter__(self):
        # for item in self.slots:
        #     yield item
        yield from self.slots
