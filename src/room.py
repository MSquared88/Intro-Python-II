# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item="stuff"):
        self.name = name
        self.description = description 
        self.item = item  

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def get_room_by_direction(self,direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        else: 
            return None

    def __str__(self):
        return f"\n{self.name}\n{self.description}\n"
    def wrong_way(self):
        print(f"\nThe way is blocked. Try to go somewhere else.\n\n{self.description}\n")