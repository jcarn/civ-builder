from Civilization import Civilization
from CivMap import CivMap
from random import randint
import pygame, sys
from pygame.locals import *

def run():
    h, w = 15, 30
    game_map = CivMap((w, h))
    civ = Civilization("America", game_map, (randint(0,w - 1), randint(0,h - 1)))

    
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("Civ Builder")
    pygame.key.set_repeat(0, 100)
    clock = pygame.time.Clock()
    paused = False
    frames = 0

    #game loop
    while True:
        #check for all types of events
        for event in pygame.event.get():
            if event.type == QUIT:
                print(str(frames))
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_TAB:
                    for i in range(20): civ.expand()

        #arbitrary expansion constant, replace soon
        for i in range(round(len(civ.owned_tiles) / 10)): civ.expand() 
        frames += 1
        draw_map(display_surface, game_map)
        clock.tick(FPS)
        pygame.display.update()

def draw_map(display_surface, game_map):
    MARGIN = 20
    side_l = round(min((WIDTH - 2 * MARGIN) / (game_map.width()),(HEIGHT - 2 * MARGIN) / (game_map.height())))
    
    def draw_tile(tile):
        x = MARGIN + (tile.loc[0] * (side_l))
        y = MARGIN + (tile.loc[1] * (side_l))
        pygame.draw.rect(display_surface, GREEN if tile.is_owned else RED, (x, y, side_l, side_l))

    #draw all tiles that have been changed, then remove them from the changed list
    for tile in game_map.updated_tiles:
            draw_tile(tile)
            game_map.updated_tiles.remove(tile)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 960
HEIGHT = 540

FPS = 10

pygame.init()
run()