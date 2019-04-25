# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room='outside'):
        self.name = name
        self.itembag = []
        self.curroom = current_room

    def add_item(self, item):
        self.itembag.append(item)

    def itembag_contents(self):
        return ' - '.join([str(i) for i in self.itembag])