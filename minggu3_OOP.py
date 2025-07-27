class doll : 
    def __init__(self,inside,outside,character,colors):
        self.inside = inside
        self.outside = outside
        self.character = character
        self.colors = colors

    def sold(self):
        print(f"{self.character} dolls with {self.colors} colored are sold")

    def sell(self):
        print(f"{self.character} dolls with {self.colors} colored are sell")