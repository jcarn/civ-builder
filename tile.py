class Tile():

    def __init__(self, value, loc):
        self.value = value
        self.is_owned = False
        self.loc = loc

    def border_tiles(self):
        border = []

    def __str__(self):
        return ("Value: " + str(self.value) + " Is owned: " + str(self.is_owned) + "Loc: " + str(self.loc))




