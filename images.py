import pygame as pg

BOARD = pg.image.load('img/connect4_board.png')
RED_PIECE = pg.image.load('img/connect4_red.png')
BLUE_PIECE = pg.image.load('img/connect4_blue.png')
BLANK = pg.image.load('img/square_white.png')
WIN = {'red': pg.image.load('img/win_red.png'),
       'blue': pg.image.load('img/win_blue.png')}
RESTART = {'red': pg.image.load('img/restart_red.png'),
           'blue': pg.image.load('img/restart_blue.png')}