# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, health, items, starting_room):
        self.name = name
        self.health = health
        self.items = items
        self.current_room = starting_room

    def move(self, direction):
        next_room  =  self.current_room.get_room_by_direction(direction)

        #check if move is valid
        if next_room:
            self.current_room = next_room
            print(self.current_room)
        else:
            return self.current_room.wrong_way()
        

