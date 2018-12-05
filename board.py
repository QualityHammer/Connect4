from settings import *
from images import *


class Board:

    bd = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, screen):
        self.screen = screen
        self.posx = 0
        self.turn = 'blue'

        self.display_board()
        self.switch_turn()

    def display_board(self):
        for x in range(0, 7):
            for y in range(1, 7):
                self.screen.blit(BOARD, convert2rez(x, y))

    def switch_turn(self):
        self.x = 0
        self.y = 0
        if self.turn == 'blue':
            self.turn = 'red'
        else:
            self.turn = 'blue'
        self.display_piece()

    def display_piece(self, x=None, y=None):
        if self.turn == 'blue':
            if x is not None and y is not None:
                self.screen.blit(BLUE_PIECE, convert2rez(x, y + 1))
            else:
                self.screen.blit(BLUE_PIECE, convert2rez(self.posx, 0))
        else:
            if x is not None and y is not None:
                self.screen.blit(RED_PIECE, convert2rez(x, y + 1))
            else:
                self.screen.blit(RED_PIECE, convert2rez(self.posx, 0))

    def blank(self, x):
        self.screen.blit(BLANK, convert2rez(x, 0))

    def control(self, direction):
        if direction == 'left':
            if self.posx != 0:
                self.blank(self.posx)
                self.posx -= 1
                self.display_piece()
        else:
            if self.posx != 6:
                self.blank(self.posx)
                self.posx += 1
                self.display_piece()

    def place_piece(self, y):
        self.blank(self.posx)
        self.display_piece(self.posx, y)
        if self.turn == 'blue':
            self.bd[y][self.posx] = 1
        else:
            self.bd[y][self.posx] = 2
        self.switch_turn()

    def get_low(self):
        for i in reversed(range(6)):
            if self.bd[i][self.posx] == 0:
                return i
            else:
                continue
        return False

    def board2string(self, direction):
        board_string = ''
        if direction == 'horizontal':
            for row in self.bd:
                for spot in row:
                    board_string += str(spot)
        elif direction == 'vertical':
            for i in range(0, 7):
                for row in self.bd:
                    board_string += str(row[i])
        elif direction == 'ldiagonal':
            for i in range(1, 7):
                for row in self.bd:
                    try:
                        board_string += str(row[i - 3])
                    except IndexError:
                        continue
        elif direction == 'rdiagonal':
            for i in range(1, 7):
                for row in self.bd:
                    try:
                        board_string += str(row[i + 3])
                    except IndexError:
                        continue
        return board_string

    def check_connect4(self):
        horiz = self.board2string('horizontal')
        vert = self.board2string('vertical')
        ldia = self.board2string('ldiagonal')
        rdia = self.board2string('rdiagonal')

        if '1111' in horiz or '1111' in vert or '1111' in ldia or '1111' in rdia:
            return 'red'
        elif '2222' in horiz or '2222' in vert or '2222' in ldia or '2222' in rdia:
            return 'blue'

    def debug_print(self):
        print()
        for row in self.bd:
            print(row)
        print()
