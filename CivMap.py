from Tile import Tile

class CivMap():

    def __init__(self, size):
        super(CivMap, self).__init__()
        self.tile_map = [[Tile(0, (x, y)) for y in range(size[1])] for x in range(size[0])]
        self.updated_tiles = sum(self.tile_map, [])


    def __str__(self):
        stringMap = ""
        for row in self.tile_map:
            for val in row:
                stringMap += "X" if val.is_owned else "0"
            stringMap += "\n"
        return stringMap

    def tile_at(self, loc):
        return self.tile_map[loc[0]][loc[1]]

    def width(self):
        return len(self.tile_map)

    def height(self):
        return len(self.tile_map[0])

    