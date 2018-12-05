from settings import *
from board import Board
from screens import starting_screen, end_screen
import sys


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        starting_screen(self.screen)
        self.run()

    def run(self):
        self.playing = True
        self.screen.fill(WHITE)
        self.bd = Board(self.screen)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == LEFT:
                    self.bd.control('left')
                elif event.key == RIGHT:
                    self.bd.control('right')
                elif event.key == DOWN:
                    self.bd.place_piece(self.bd.get_low())
                elif event.key == Q:
                    self.bd.debug_print()

    def updates(self):
        if self.bd.check_connect4() == 'blue' or self.bd.check_connect4() == 'red':
            sys.exit()

    def draw(self):
        pg.display.update()


g = Game()
while g.running:
    g.new()


pg.quit()
