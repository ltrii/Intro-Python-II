from room import Room
from item import Item
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#OUTSIDE
room['outside'].n_to = 'foyer'

#FOYER
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'

#OVERLOOK
room['overlook'].s_to = 'foyer'

#NARROW
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'

#TREASURE
room['treasure'].s_to = 'narrow'

room['outside'].add_item = Item('Stick', 'A small wooden stick.')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print('Welcome to the Game! \n')

playername = input("Please choose a name: ")

curplayer = Player(playername)

run = 1

while run == 1:
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    print("Current Player: " + curplayer.name + "\n")
    print(room[curplayer.curroom].name)
    print(room[curplayer.curroom].description + "\n")
    print(room[curplayer.curroom].get_items_str())
    print(room[curplayer.curroom].get_exits())

    choice = input('Make a choice ==> ')

    if choice == 'n':
        move = room[curplayer.curroom].get_room_in_direction('n')
        if move == None:
            print('You can not move in that direction')
        else:
            curplayer.curroom = move

    if choice == 'e':
        move = room[curplayer.curroom].get_room_in_direction('e')
        if move == None:
            print('You can not move in that direction')
            input("Press anything to continue..")
        else:
            curplayer.curroom = move

    if choice == 's':
        move = room[curplayer.curroom].get_room_in_direction('s')
        if move == None:
            print('You can not move in that direction')
        else:
            curplayer.curroom = move

    if choice == 'w':
        move = room[curplayer.curroom].get_room_in_direction('w')
        if move == None:
            print('You can not move in that direction')
            input("Press anything to continue..")
        else:
            curplayer.curroom = move

    if choice == 'q':
        quit()


