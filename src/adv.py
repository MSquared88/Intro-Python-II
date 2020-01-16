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


p1 = Player("Roger Wilco", 100, [], room['outside'])

directions = ["n", "s", "e", "w"]


# start game
print(
    f"\nYou have entered Matthew's Adventure. Only the strong will survive.\n \n{p1.current_room}")
# Write a loop that:
while True:

    # * Waits for user_input input and decides what to do.
    user_input = input(
        "[l] Look [n] Move North  [s] Move South   [e] Move East  [w] Move West  [q] Quit\n ~~>")

    # If the user_input enters "q", quit the game.
    if user_input == "q":
        print("\nThanks for playing!!\n")
        exit()

    elif user_input == "l":
        print(p1.current_room, '\n')

    # If the user_input enters a cardinal direction, attempt to move to the room there.
    elif user_input in directions:
        p1.move(user_input)
    # else user_input gives invalid input print a error message.
    else:
        print(f"\n{user_input} is not a valid input\n")
        print(p1.current_room)
        continue

# Print an error message if the movement isn't allowed.


