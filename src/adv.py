from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('Flashlight', 'Helps you see in dark places')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Binoculars', 'You can use this to see from far distances'), Item('Apple', 'Can be used to increase your health')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Treasure', 'Contains a ton of gold coins'), Item('Jewelry', 'Valuable and rare, can cost a fortune')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])


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

print("\t===========Welcome to the Classic Adventure Game===========")
print("You are currently here:")

while True:
    print(player)
    print("========================")
    direction = input(
        'Where would you like to go?\n[n] North\t[s] South\t[w] West\t[e] East\t[q] Quit Game:\n')
    if direction in {'n', 's', 'w', 'e'}:
        player.new_direction(direction)
    elif direction == 'q':
        exit('Thank you for playing')
    else:
        print('=====Invalid Command=====')
