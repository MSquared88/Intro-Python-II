# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item="stuff"):
        self.name = name
        self.description = description 
        self.item = item

    def __str__(self):
        return f"\nYou are in the {self.name}. {self.description}\n"
    def wrong_way(self):
        print(f"The way is blocked. Try to go somewhere else.\n \n {self.description}\n")