import pygame
from .constants import white, black, sq_size, board_x, board_y, b_PAWN, w_PAWN, w_ROOK, b_ROOK, w_KNIGHT, b_KNIGHT, w_BISCHOP, b_BISCHOP, w_QUEEN, b_QUEEN, w_KING, b_KING


class Pawn:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y


    def draw(self, win):
        if self.color == white:
            win.blit(w_PAWN, (self.x - w_PAWN.get_width()//2, self.y - w_PAWN.get_height()//2))
        else:
            win.blit(b_PAWN, (self.x - b_PAWN.get_width()//2, self.y - b_PAWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Rook:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y

    def draw(self, win):
        if self.color == white:
            win.blit(w_ROOK, (self.x - w_ROOK.get_width()//2, self.y - w_ROOK.get_height()//2))
        if self.color == black:
            win.blit(b_ROOK, (self.x - b_ROOK.get_width()//2, self.y - b_ROOK.get_height()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y

    def draw(self, win):
        if self.color == white:
            win.blit(w_KNIGHT, (self.x - w_KNIGHT.get_width()//2, self.y - w_KNIGHT.get_height()//2))
        if self.color == black:
            win.blit(b_KNIGHT, (self.x - b_KNIGHT.get_width()//2, self.y - b_KNIGHT.get_height()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Bischop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y

    def draw(self, win):
        if self.color == white:
            win.blit(w_BISCHOP, (self.x - w_BISCHOP.get_width()//2, self.y - w_BISCHOP.get_height()//2))
        if self.color == black:
            win.blit(b_BISCHOP, (self.x - b_BISCHOP.get_width()//2, self.y - b_BISCHOP.get_height()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y

    def draw(self, win):
        if self.color == white:
            win.blit(w_QUEEN, (self.x - w_QUEEN.get_width()//2, self.y - w_QUEEN.get_height()//2))
        if self.color == black:
            win.blit(b_QUEEN, (self.x - b_QUEEN.get_width()//2, self.y - b_QUEEN.get_height()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (sq_size*self.col + sq_size//2) + board_x
        self.y = (sq_size*self.row + sq_size//2) + board_y

    def draw(self, win):
        if self.color == white:
            win.blit(w_KING, (self.x - w_KING.get_width()//2, self.y - w_KING.get_height()//2))
        if self.color == black:
            win.blit(b_KING, (self.x - b_KING.get_width()//2, self.y - b_KING.get_height()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
