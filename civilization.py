import random
from civ_map import CivMap
import civ_utility
from tile import Tile

class Civilization():

    #init function. game_map is a required param, all the others can be randomly genned
    def __init__(self, game_map, name = None, start_location = None, color = None):
        self.name = name if name != None else CivUtility.get_random_name()
        self.game_map = game_map
        self.owned_tiles = [game_map.tile_at(start_location)]
        self.new_tiles = [self.owned_tiles[0]]
        self.edge_tiles = []

        #governs behavior of civilization
        self.FULL = 100
        self.expansion = round(self.FULL / 2)
        self.construction = self.FULL - self.expansion
        game_map.tile_at((start_location[0],start_location[1])).is_owned = True

    def expand(self):
        #choose expansion
        self.edge_tiles += list(self.getEdgeTiles())
        edge_tile = random.choice(self.edge_tiles)
        #expand
        edge_tile.is_owned = True
        self.owned_tiles.append(edge_tile)
        self.new_tiles.append(edge_tile)

    #move functionality to tile
    def getEdgeTiles(self):
        edges = []
        game_map = self.game_map
        for tile in self.new_tiles:
            self.new_tiles.remove(tile)
            game_map.updated_tiles.append(tile)
            loc = tile.loc
            if (loc[0] + 1 < game_map.width()) and (not game_map.tile_at((loc[0] + 1,loc[1])).is_owned): edges.append(game_map.tile_at((loc[0] + 1,loc[1])))
            if (loc[0] - 1 >= 0) and (not game_map.tile_at((loc[0] - 1,loc[1])).is_owned): edges.append(game_map.tile_at((loc[0] - 1,loc[1])))
            if (loc[1] + 1 < game_map.height()) and (not game_map.tile_at((loc[0], loc[1] + 1)).is_owned): edges.append(game_map.tile_at((loc[0],loc[1] + 1)))
            if (loc[1] - 1 >= 0) and (not game_map.tile_at((loc[0],loc[1] - 1)).is_owned): edges.append(game_map.tile_at((loc[0],loc[1] - 1)))
        return edges

