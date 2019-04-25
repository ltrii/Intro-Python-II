class Item:
    def __init__(self, name, description):
        self.name = name
        self.lowname = name.lower()
        self.description = description

    def __repr__(self):
        return f'{self.name}'