import pygame
from .constants import bgc, white, black, light_sq, dark_sq, b_width, b_height, rows, cols, board_x, board_y, sq_size
from .pieces import Pawn, Rook, Knight, Bischop, Queen, King

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.inCheck = False
        self.w_king_pos = (7, 4)
        self.b_king_pos = (0, 4)
        self.move_log = []
        self.create_board()
        

    def draw_squares(self, win):
        win.fill(bgc)
        pygame.draw.rect(win, black, (board_x-5, board_y-5, b_width+10, b_height+10))
        pygame.draw.rect(win, dark_sq, (board_x, board_y, b_width, b_height))
        for row in range(rows):
            for col in range(row%2, rows, 2):
                pygame.draw.rect(win, light_sq, ((row*sq_size)+board_x, (col*sq_size)+board_y, sq_size, sq_size))

    def move(self, piece, row, col):
        self.move_log.append([piece, (piece.row, piece.col), (row, col), self.board[row][col]])
        if isinstance(piece, King):
            if piece.color == black:
                self.b_king_pos = (row, col)
            else:
                self.w_king_pos = (row, col)
        if self.board[row][col]!=0:
            self.remove(self.board[row][col])
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if isinstance(piece, Pawn) and piece.color==white and row==0:
            #pawn can be promoted
            pass

    def pawn_promotion(self, piece):
        pass

    def undo_move(self):
        last_move = self.move_log.pop()
        piece_moved = last_move[0]
        starting_pos = last_move[1]
        ending_pos = last_move[2]
        cap_piece = last_move[3]
        self.board[starting_pos[0]][starting_pos[1]] = piece_moved
        if isinstance(piece_moved, King):
            if piece_moved.color==white:
                self.w_king_pos = (starting_pos[0], starting_pos[1])
            else: self.b_king_pos = (starting_pos[0], starting_pos[1])
        piece_moved.move(starting_pos[0], starting_pos[1])
        self.board[ending_pos[0]][ending_pos[1]] = cap_piece
        

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if row==0:
                    if col==0 or col==7:
                        self.board[row].append(Rook(row, col, black))
                    elif col==1 or col==6:
                        self.board[row].append(Knight(row, col, black))
                    elif col==2 or col==5:
                        self.board[row].append(Bischop(row, col, black))
                    elif col==3:
                        self.board[row].append(Queen(row, col, black))
                    else:
                        self.board[row].append(King(row, col, black))
                elif row==1:
                    self.board[row].append(Pawn(row, col, black))
                elif row==6:
                    self.board[row].append(Pawn(row, col, white))
                elif row==7:
                    if col==0 or col==7:
                        self.board[row].append(Rook(row, col, white))
                    elif col==1 or col==6:
                        self.board[row].append(Knight(row, col, white))
                    elif col==2 or col==5:
                        self.board[row].append(Bischop(row, col, white))
                    elif col==3:
                        self.board[row].append(Queen(row, col, white))
                    else:
                        self.board[row].append(King(row, col, white))
                else:
                    self.board[row].append(0)
        

    def draw(self, win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0
                

    def get_valid_moves(self, piece):
        moves = []

        if isinstance(piece, Bischop) or isinstance(piece, Queen):
            r = piece.row
            c = piece.col
            while r > 0 and c > 0: #up left diagonal
                if self.board[r-1][c-1]!=0 and self.board[r-1][c-1].color!=piece.color:
                    moves.append( (r-1, c-1) )
                    break
                elif self.board[r-1][c-1]!=0 and self.board[r-1][c-1].color==piece.color:
                    break
                else: moves.append( (r-1, c-1) )
                r -= 1
                c -= 1
            r = piece.row
            c = piece.col
            while r > 0 and c < 7: #up right diagonal
                if self.board[r-1][c+1]!=0 and self.board[r-1][c+1].color!=piece.color:
                    moves.append( (r-1, c+1) )
                    break
                elif self.board[r-1][c+1]!=0 and self.board[r-1][c+1].color==piece.color:
                    break
                else: moves.append( (r-1, c+1) )
                r -= 1
                c += 1
            r = piece.row
            c = piece.col
            while r < 7 and c > 0: #bottom left diagonal
                if self.board[r+1][c-1]!=0 and self.board[r+1][c-1].color!=piece.color:
                    moves.append( (r+1, c-1) )
                    break
                elif self.board[r+1][c-1]!=0 and self.board[r+1][c-1].color==piece.color:
                    break
                else: moves.append( (r+1, c-1) )
                r += 1
                c -= 1
            r = piece.row
            c = piece.col
            while r < 7 and c < 7: # bottom right diagonal
                if self.board[r+1][c+1]!=0 and self.board[r+1][c+1].color!=piece.color:
                    moves.append( (r+1, c+1) )
                    break
                elif self.board[r+1][c+1]!=0 and self.board[r+1][c+1].color==piece.color:
                    break
                else: moves.append( (r+1, c+1) )
                r += 1
                c += 1
            
        if isinstance(piece, Rook) or isinstance(piece, Queen):
            for row in range(piece.row-1, -1, -1): #upward
                if self.board[row][piece.col]!=0 and self.board[row][piece.col].color!=piece.color:
                    moves.append( (row, piece.col) )
                    break
                elif self.board[row][piece.col]!=0 and self.board[row][piece.col].color==piece.color:
                    break
                else: moves.append( (row, piece.col) )

            for row in range(piece.row+1, 8, 1): #downward
                if self.board[row][piece.col]!=0 and self.board[row][piece.col].color!=piece.color:
                    moves.append( (row, piece.col) )
                    break
                elif self.board[row][piece.col]!=0 and self.board[row][piece.col].color==piece.color:
                    break
                else: moves.append( (row, piece.col) )

            for col in range(piece.col-1, -1, -1): #leftward
                if self.board[piece.row][col]!=0 and self.board[piece.row][col].color!=piece.color:
                    moves.append( (piece.row, col) )
                    break
                elif self.board[piece.row][col]!=0 and self.board[piece.row][col].color==piece.color:
                    break
                else: moves.append( (piece.row, col) )

            for col in range(piece.col+1, 8, 1): #rightward
                if self.board[piece.row][col]!=0 and self.board[piece.row][col].color!=piece.color:
                    moves.append( (piece.row, col) )
                    break 
                elif self.board[piece.row][col]!=0 and self.board[piece.row][col].color==piece.color:
                    break
                else: moves.append( (piece.row, col) )



                             
        elif isinstance(piece, Pawn):
            if piece.color == white:
                if piece.row == 6 and self.board[piece.row-1][piece.col]==0 and self.board[piece.row-2][piece.col]==0:
                    moves.append( (piece.row - 2, piece.col) )
                if piece.row > 0:
                    if self.board[piece.row - 1][piece.col] == 0:
                        moves.append( (piece.row - 1, piece.col) )
                    if piece.col > 0 and self.board[piece.row-1][piece.col-1]!=0 and self.board[piece.row-1][piece.col-1].color==black:
                        moves.append( (piece.row-1, piece.col-1) )
                    if piece.col < 7 and self.board[piece.row-1][piece.col+1]!=0 and self.board[piece.row-1][piece.col+1].color==black:
                        moves.append( (piece.row-1, piece.col+1) )
            else: #color = black
                if piece.row == 1 and self.board[piece.row+1][piece.col]==0 and self.board[piece.row+2][piece.col]==0:
                    moves.append( (piece.row + 2, piece.col) )
                if piece.row < 7:
                    if self.board[piece.row + 1][piece.col] == 0:
                        moves.append( (piece.row + 1, piece.col) )
                    if piece.col > 0 and self.board[piece.row+1][piece.col-1]!=0 and self.board[piece.row+1][piece.col-1].color==white:
                        moves.append( (piece.row+1, piece.col-1) )
                    if piece.col < 7 and self.board[piece.row+1][piece.col+1]!=0 and self.board[piece.row+1][piece.col+1].color==white:
                        moves.append( (piece.row+1, piece.col+1) )

                    
        elif isinstance(piece, Knight):
            if piece.row>1 and piece.col>0 and (self.board[piece.row-2][piece.col-1]==0 or (self.board[piece.row-2][piece.col-1]!=0 and self.board[piece.row-2][piece.col-1].color!=piece.color)):
                moves.append( (piece.row-2, piece.col-1) )
            if piece.row>1 and piece.col<7 and (self.board[piece.row-2][piece.col+1]==0 or (self.board[piece.row-2][piece.col+1]!=0 and self.board[piece.row-2][piece.col+1].color!=piece.color)):
                moves.append( (piece.row-2, piece.col+1) )
            if piece.row>0 and piece.col>1 and (self.board[piece.row-1][piece.col-2]==0 or (self.board[piece.row-1][piece.col-2]!=0 and self.board[piece.row-1][piece.col-2].color!=piece.color)):
                moves.append( (piece.row-1, piece.col-2) )
            if piece.row>0 and piece.col<6 and (self.board[piece.row-1][piece.col+2]==0 or (self.board[piece.row-1][piece.col+2]!=0 and self.board[piece.row-1][piece.col+2].color!=piece.color)):
                moves.append( (piece.row-1, piece.col+2) )
            if piece.row<6 and piece.col>0 and (self.board[piece.row+2][piece.col-1]==0 or (self.board[piece.row+2][piece.col-1]!=0 and self.board[piece.row+2][piece.col-1].color!=piece.color)):
                moves.append( (piece.row+2, piece.col-1) )
            if piece.row<6 and piece.col<7 and (self.board[piece.row+2][piece.col+1]==0 or (self.board[piece.row+2][piece.col+1]!=0 and self.board[piece.row+2][piece.col+1].color!=piece.color)):
                moves.append( (piece.row+2, piece.col+1) )
            if piece.row<7 and piece.col>1 and (self.board[piece.row+1][piece.col-2]==0 or (self.board[piece.row+1][piece.col-2]!=0 and self.board[piece.row+1][piece.col-2].color!=piece.color)):
                moves.append( (piece.row+1, piece.col-2) )
            if piece.row<7 and piece.col<6 and (self.board[piece.row+1][piece.col+2]==0 or (self.board[piece.row+1][piece.col+2]!=0 and self.board[piece.row+1][piece.col+2].color!=piece.color)):
                moves.append( (piece.row+1, piece.col+2) )


        elif isinstance(piece, King): # piece = king
            if piece.row > 0:
                if self.board[piece.row-1][piece.col]==0 or (self.board[piece.row-1][piece.col]!=0 and self.board[piece.row-1][piece.col].color!=piece.color):
                    moves.append( (piece.row-1, piece.col) ) #top
                if piece.col>0 and (self.board[piece.row-1][piece.col-1]==0 or (self.board[piece.row-1][piece.col-1]!=0 and self.board[piece.row-1][piece.col-1].color!=piece.color)):
                    moves.append( (piece.row-1, piece.col-1) ) #top left
                if piece.col<7 and (self.board[piece.row-1][piece.col+1]==0 or (self.board[piece.row-1][piece.col+1]!=0 and self.board[piece.row-1][piece.col+1].color!=piece.color)):
                    moves.append( (piece.row-1, piece.col+1) ) #top right
            if piece.col>0 and (self.board[piece.row][piece.col-1]==0 or (self.board[piece.row][piece.col-1]!=0 and self.board[piece.row][piece.col-1].color!=piece.color)):
                moves.append( (piece.row, piece.col-1) ) #left
            if piece.col<7 and (self.board[piece.row][piece.col+1]==0 or (self.board[piece.row][piece.col+1]!=0 and self.board[piece.row][piece.col+1].color!=piece.color)):
                moves.append( (piece.row, piece.col+1) ) #right
            if piece.row < 7:
                if self.board[piece.row+1][piece.col]==0 or (self.board[piece.row+1][piece.col]!=0 and self.board[piece.row+1][piece.col].color!=piece.color):
                    moves.append( (piece.row+1, piece.col) ) #bottom
                if piece.col>0 and (self.board[piece.row+1][piece.col-1]==0 or (self.board[piece.row+1][piece.col-1]!=0 and self.board[piece.row+1][piece.col-1].color!=piece.color)):
                    moves.append( (piece.row+1, piece.col-1) ) #bottom left
                if piece.col<7 and (self.board[piece.row+1][piece.col+1]==0 or (self.board[piece.row+1][piece.col+1]!=0 and self.board[piece.row+1][piece.col+1].color!=piece.color)):
                    moves.append( (piece.row+1, piece.col+1) ) #bottom right
        
        return moves


    def king_under_attack(self, king_pos):
        king_row, king_col = king_pos
        king_color = self.board[king_row][king_col].color
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0 and piece.color != king_color:
                    if king_pos in self.get_valid_moves(piece):
                        return True
        return False


    def valid_moves_king_not_attacked(self, piece):
        moves = self.get_valid_moves(piece)
        for i in range(len(moves)-1, -1, -1):
            row, col = moves[i][0], moves[i][1]
            self.move(piece, row, col)
            if piece.color == white:
                king_pos = self.w_king_pos
            else:
                king_pos = self.b_king_pos

            if self.king_under_attack(king_pos):
                moves.remove(moves[i])
            self.undo_move()
        return moves

    def all_valid_moves(self):
        all_valid_moves = {}
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col]!=0:
                    all_valid_moves[self.board[row][col]] = self.valid_moves_king_not_attacked(self.board[row][col])
        return all_valid_moves



    
                    
    
                
    
    
        
