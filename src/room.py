# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items is None:
            self.contains = []
        else:
            self.contains = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None    
    def __str__(self):
        roomstr = f"{self.name}\n\n"
        roomstr += f"   {self.description}\n\n"
        roomstr += f"Possible directions: {self.get_exits()}\n"
        return roomstr

    def get_items_str(self):
        return ', '.join([str(i) for i in self.contains])
    
    def print_contents(self):
        for i in self.contains:
            print(i.name)

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.e_to is not None:
            exits.append('e')
        if self.s_to is not None:
            exits.append('s')
        if self.w_to is not None:
            exits.append('w')
        return ", ".join(exits)

    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def add_item(self, item):
        self.contains.append(item)