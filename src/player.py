# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, health, inventory, starting_room):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.current_room = starting_room

    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\nName:{self.name}\n"
        display_string += f"\nHealth:{self.health}\n"
        display_string += f"\nIventory:{self.inventory}"
        return display_string

    def move(self, direction):
        next_room  =  self.current_room.get_room_by_direction(direction)

        #check if move is valid
        if next_room:
            self.current_room = next_room
            print(self.current_room)
        else:
            return self.current_room.wrong_way()
        

