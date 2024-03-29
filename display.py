from settings import *

pg.init()
pg.font.init()


class Button:

    font = pg.font.SysFont('Impact', 30)

    def __init__(self, screen, msg, x, y, width, height, inactivec, activec):
        self.screen = screen
        self.msg = msg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactivec = inactivec
        self.activec = activec

        self.rect = (x, y, width, height)

    def display(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        text_surf, text_size = self.text_objects()
        if self.x < mouse[0] < self.x + self.width \
                and self.y < mouse[1] < self.y + self.height:
            pg.draw.rect(self.screen, self.activec, self.rect)
            if click[0] == 1:
                return True
        else:
            pg.draw.rect(self.screen, self.inactivec, self.rect)
        text_pos = (((self.width - text_size[0]) / 2) + self.x, ((self.height - text_size[1]) / 2) + self.y)
        self.screen.blit(text_surf, text_pos)

    def text_objects(self):
        text_surface = self.font.render(self.msg, True, BLACK)
        return text_surface, (text_surface.get_width(), text_surface.get_height())


class Title:

    font = pg.font.SysFont('Sitka', 100, bold=True)

    def __init__(self, screen, msg):
        self.screen = screen
        self.msg = msg

        self.surf = Title.font.render(msg, False, BLACK)
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        self.x = (WIDTH - self.width) / 2
        self.y = 150

    def display(self):
        self.screen.blit(self.surf, (self.x, self.y))
