import pygame as pg

# Game variables
GAME_NAME = 'Connect 4'
VERSION = ' TEST'
TITLE = GAME_NAME + VERSION
WIDTH = 700
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH / 2, HEIGHT / 2)
FPS = 60
DEBUG = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
LBLUE = (0, 0, 245)
LRED = (245, 0, 0)

# Keys
LEFT = pg.K_LEFT
RIGHT = pg.K_RIGHT
DOWN = pg.K_DOWN
Q = pg.K_q
W = pg.K_w


def convert2rez(x, y):
    rezx = x * 100
    rezy = y * 100
    return rezx, rezy
