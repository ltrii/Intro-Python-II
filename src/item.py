class Item:
    def __init__(self, name, description):
        self.name = name
        self.lowname = name.lower()
        self.description = description

    def __repr__(self):
        return f'{self.name}'

class Key(Item):
    def __init__(self, name, description, type, unlocks):
        Item.__init__(self, name="Key", description="Used for opening things")
        self.type = type
        self.unlocks = unlocks