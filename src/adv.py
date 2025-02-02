from room import Room
from player import Player

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
new_player = Player(name="Louis", current_room="outside")

# Write a loop that:
#
# * Prints the current room name
print(room[player.current_room])
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
move = input("Which direction do you want to move? ( n, s, e, or w)")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
if (validMove(move)):
    movePlayer(new_player)
else:
    printInvalidMoveError()
#
# If the user enters "q", quit the game.
quit_game = input("Do you want to quit the game? (Pres q)")

def main():
    pass

def move_direction(dir):
    pass

def print_current_room_name(room):
    print(room.)

def game_loop():
    game_state = 'ready'

    while game_state != 'q':
        

