from settings import *
import sys
from display import Button, Title

pg.init()
clock = pg.time.Clock()


def starting_screen(screen):
    intro = True
    ctitle = Title(screen, 'Connect 4')
    startb = Button(screen, 'Start', CENTER[0] - 250, CENTER[1], 200, 150, BLUE, LBLUE)
    quitb = Button(screen, 'Quit', CENTER[0] + 50, CENTER[1], 200, 150, RED, LRED)
    screen.fill(WHITE)
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        ctitle.display()
        if startb.display():
            intro = False
        if quitb.display():
            sys.exit()
        pg.display.update()
        clock.tick(15)


# for some reason doesnt work
def end_screen(screen):
    rtitle = Title(screen, 'Restart?')
    restartb = Button(screen, 'Restart', CENTER[0] - 250, CENTER[1], 200, 150, BLUE, LBLUE)
    quitb = Button(screen, 'Quit', CENTER[0] + 50, CENTER[1], 200, 150, RED, LRED)
    end = True
    screen.fill(WHITE)
    while end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        rtitle.display()
        if restartb:
            end = False
            pg.time.delay(100)
        if quitb:
            end = False
        pg.display.update()
        clock.tick(15)




