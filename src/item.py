class Item:
    def __init__(self, name, description, points):
        self.name = name
        self.description = description 
        self.points = points
    
    def __str__(self):
        return f"\n{self.name}"
    
    def look(self): 
        return f"{self.description}"