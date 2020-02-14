from room import Room
from player import Player
from item import Item

#declare items

items = {
     "The Eye of Agammoto": Item("The Eye of Agammoto", "The The Eye of Agammoto can maniputale time", 50),
     "The Sword of a Thousand Truths": Item("The Sword of a Thousand Truths", "A sword made by Hatori Hanzo", 100),
     "Torch": Item("Torch", "Lets you see in dark places", 10)
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons", [items["Torch"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["The Sword of a Thousand Truths"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! You see something shiny in the corner. The only exit is to the south.""", [items["The Eye of Agammoto"]]),
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


player1 = Player("Roger Wilco", 100, [], room['outside'])



ui_display = ""
ui_display += "\n----------------\n"
ui_display += "\nActions: [look]  [i]nventory  [q]uit [h]elp\n"
ui_display += "\nMovement: [n]orth  [s]outh  [e]ast  [w]est  \n"


directions = ("n", "s", "e", "w")

def err_msg():
    print(f"\nThat is not a valid input\n")
    print(player1.current_room)

# start game
print(
    f"\nYou have entered Matthew's Adventure. Only the strong will survive. {player1.current_room}\n\n{ui_display}")
# REPL
while True:

    user_input = input("~~>").split()

    # * Waits for user_input input and decides what to do.

    #one command logic
    if len(user_input) == 1:
        if user_input[0] == "i":
            print(player1)

        elif user_input[0] == "look":
            print(player1.current_room, '\n')

        # If the user_input enters a cardinal direction, attempt to move to the room there.
        elif user_input[0] in directions:
            player1.move(user_input[0])

        # If the user_input enters "q", quit the game.
        elif user_input[0] == "q":
            print("\nThanks for playing!!\n")
            break
        
        elif user_input[0] == "h":
            print(ui_display)
        else:
            err_msg()
            continue    


    elif len(user_input) == 2:
        #action verb logic
        if user_input[1] in items:
            player1.action(user_input[0], items[user_input[1]])
        else:
            err_msg()
            continue    

    else:
        err_msg()
        continue    






