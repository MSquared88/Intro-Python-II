# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, health, items, room):
        self.name = name
        self.health = health
        self.items = items
        self.room = room
