# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.itembag = []
        self.curroom = current_room.name

    def addItem(self, item):
        self.itembag.append(item)