import pygame
from .constants import bgc, white, black, sq_size, board_x, board_y, sq_border, b_height
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = white
        self.valid_moves = []

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_checkmate(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece!=0 and piece.color == self.turn:
            self.selected = piece
            all_valid_moves = self.board.all_valid_moves()
            self.valid_moves = all_valid_moves[piece]
            return True

        return False

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = []
        if self.turn == white:
            self.turn = black
        else:
            self.turn = white

    def draw_valid_moves(self, moves):
        padding = 5
        for move in moves:
            row = move[0]
            col = move[1]
            pygame.draw.rect(self.win, sq_border, (board_x+(col*sq_size)+(padding//2), board_y+(row*sq_size)+(padding//2), sq_size-padding, sq_size-padding), padding)
        
    def checkmate(self):
        all_valid_moves = self.board.all_valid_moves()
        if self.turn == white:
            for key in all_valid_moves:
                if key.color == white and all_valid_moves[key]!=[]:
                    return False
        else: #black's turn
            for key in all_valid_moves:
                if key.color == black and all_valid_moves[key]!=[]:
                    return False
        return True

    def draw_checkmate(self, win):
        font = pygame.font.SysFont(None, sq_size)
        font_border = pygame.font.SysFont(None, sq_size+1)
        w_win = font.render('Checkmate! White Wins', True, white)
        w_border = font_border.render('Checkmate! White Wins', True, black)
        b_win = font.render('Checkmate! Black Wins', True, black)
        b_border = font_border.render('Checkmate! Black Wins', True, white)
        if self.checkmate():
            if self.turn==white:
                win.blit(b_border, (board_x-9, (board_y+b_height-5)//2))
                win.blit(b_win, (board_x-8, ((board_y+b_height-5)//2)-1))
            else:
                win.blit(w_border, (board_x-9, (board_y+b_height-5)//2))
                win.blit(w_win, (board_x-8, ((board_y+b_height-5)//2)-1))

