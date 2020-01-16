from room import Room
from player import Player
from item import Item

#declare items

items = {
     "eye": Item("The Eye of Agammoto", "The The Eye of Agammoto can maniputale time", 50),
     "sword": Item("The Sword of a Thousand Truths", "A sword made by Hatori Hanzo", 100),
     "torch": Item("Torch", "Lets you see in dark places", 10)
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),

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

#place items in rooms


room['outside'].items.append(items["torch"])
room['outside'].items.append(items["eye"])


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


player1 = Player("Roger Wilco", 100, [], room['outside'])

ui_display = ""
ui_display += "\n----------------\n"
ui_display += "\nActions: [l] Look [i] inventory  [q] Quit\n"
ui_display += "\nMovement: [n] Move North  [s] Move South  [e] Move East  [w] Move West  \n"
ui_display += "~~>"

directions = ("n", "s", "e", "w")
# start game
print(
    f"\nYou have entered Matthew's Adventure. Only the strong will survive. {player1.current_room}")
# Write a loop that:
while True:

    # * Waits for user_input input and decides what to do.
    user_input = input(ui_display)

    # If the user_input enters "q", quit the game.
    if user_input == "q":
        print("\nThanks for playing!!\n")
        exit()
    if user_input == "i":
        print(player1)

    elif user_input == "l":
        print(player1.current_room, '\n')

    # If the user_input enters a cardinal direction, attempt to move to the room there.
    elif user_input in directions:
        player1.move(user_input)

    # else user_input gives invalid input print a error message.
    else:
        print(f"\n{user_input} is not a valid input\n")
        print(player1.current_room)
        continue

# Print an error message if the movement isn't allowed.


