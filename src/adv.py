from room import Room
from item import Item, Key
from player import Player
import os
import time

def get_exits(thisroom):
    hidden = []
    exits = []
    if thisroom.n_to is not None:
        if room[thisroom.n_to].hidden == True:
            hidden.append('N')
        else:
            exits.append('N')
    if thisroom.e_to is not None:
        if room[thisroom.e_to].hidden == True:
            hidden.append('E')
        else:
            exits.append('E')
    if thisroom.s_to is not None:
        if room[thisroom.s_to].hidden == True:
            hidden.append('S')
        else:
            exits.append('S')
    if thisroom.w_to is not None:
        if room[thisroom.w_to].hidden == True:
            hidden.append('W')
        else:
            exits.append('W')
    return " | ".join(exits)

def roomlock(move):
    if room[move].locked == True:
        print('Room is locked')
        time.sleep(1)
        room[move].hidden = False
        for index, item in enumerate(curplayer.itembag):
            if curplayer.itembag[index].name == room[curplayer.curroom].name:
                print('You have a key to open this door! Opening...')
                room[move].locked = False
                time.sleep(2)
                curplayer.curroom = move
            else:
                print('Turning around...')
                time.sleep(2)
    else:
        curplayer.curroom = move

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
earlier adventurers. It appears the only exit is to the south."""),

    'hidden room': Room("Hidden Room", """You walk down a small staircase to a hidden room in the back of the Cave below the overlook. There might be something nice here...""", None, True, True),

    'trail': Room("Trail", """Outdoor trail connecting the Cave opening to a small pond"""),

    'pond': Room("Small Pond", """You may have dropped something here on your initial walk up to the Cave...""")
}

items = {
    'stick':    Item('Stick', 'A small wooden stick.'),
    'sword':    Item('Sword', 'A really sharp stabby thing made of metal'),
    'door-key':   Key('Door-Key', 'A key used for opening a door... Someone told you it would work somewhere in the Cave...?', 'door', 'hidden room')
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
room['outside'].s_to = 'trail'

#TRAIL
room['trail'].n_to = 'outside'
room['trail'].s_to = 'pond'

#POND
room['pond'].n_to = 'trail'

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
room['treasure'].w_to = 'hidden room'

#HIDDEN ROOM
room['hidden room'].e_to = 'treasure'


#ITEM POPULATE
room['outside'].add_item(items['stick'])
room['treasure'].add_item(items['sword'])
room['pond'].add_item(items['door-key'])



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
    if room[curplayer.curroom].contains == []:
        print("There appears to be nothing around" + "\n")
    else:
        print("You see: " + room[curplayer.curroom].get_items_str())
    print("Possible directions: " + get_exits(room[curplayer.curroom]) + "\n")

    choice = input('Make a choice ==> ')
    choiceword = choice.split()

    if len(choice) == 1:
        choice = choice.upper()
        if choice == 'N':
            move = room[curplayer.curroom].get_room_in_direction('n')
            if move == None:
                print('You can not move in that direction')
                input("Press anything to continue..")
            else:
                roomlock(move)
        elif choice == 'E':
            move = room[curplayer.curroom].get_room_in_direction('e')
            if move == None:
                print('You can not move in that direction')
                input("Press anything to continue..")
            else:
                roomlock(move)
        elif choice == 'S':
            move = room[curplayer.curroom].get_room_in_direction('s')
            if move == None:
                print('You can not move in that direction')
                input("Press anything to continue..")
            else:
                roomlock(move)
        elif choice == 'W':
            move = room[curplayer.curroom].get_room_in_direction('w')
            if move == None:
                print('You can not move in that direction')
                input("Press anything to continue..")
            else:
                roomlock(move)
        elif choice == 'Q':
            quit()
        elif choice == 'I':
            print('Current inventory: ')
            print(curplayer.itembag_contents())
            input('Press anything to continue')
        else:
            print('Unrecognized command. Pick a direction or Q to quit.')
            time.sleep(.5)
            print('Resetting...')
            time.sleep(1.5)

    elif len(choiceword) == 2:
        if choiceword[0] == 'get':
            try:
                for index, item in enumerate(room[curplayer.curroom].contains):
                    if(item.lowname == choiceword[1].lower()):
                        curplayer.add_item(items[choiceword[1].lower()])
                        room[curplayer.curroom].contains.remove(items[choiceword[1].lower()])
                        print(f'You picked up a {choiceword[1]}')
                        time.sleep(2)
                        break
                    elif(index == len(room[curplayer.curroom].contains)-1):
                        print("There is no item in this room with that name")
                        time.sleep(2)
                        break
            except AttributeError:
                for index, item in enumerate(room[curplayer.curroom].contains):
                    if(item.lowname == choiceword[1].lower()):
                        curplayer.add_item(items[choiceword[1].lower()])
                        room[curplayer.curroom].contains.remove(items[choiceword[1].lower()])
                        print(f'You picked up a {choiceword[1]}')
                        time.sleep(2)
                        break
                    elif(index == len(room[curplayer.curroom].contains)-1):
                        print("There is no item in this room with that name")
                        time.sleep(2)
                        break
        if choiceword[0] == 'drop':
            for index, item in enumerate(curplayer.itembag):
                if(curplayer.itembag[index] == items[choiceword[1]]):
                    curplayer.itembag.remove(item)
                    room[curplayer.curroom].contains.append(item)
                    print(f'You dropped a {choiceword[1]}')
                    time.sleep(2)
                elif(index == len(curplayer.itembag)-1):
                    print("There is no item in your inventory that matches that name")
                    time.sleep(2)
                    break

