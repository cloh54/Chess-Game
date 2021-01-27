import pygame

WIDTH, HEIGHT = 1200, 800
b_width, b_height = 640, 640
rows, cols = 8, 8
board_x = (WIDTH - b_width)//2
board_y = ((HEIGHT - b_height)//2)
sq_size = b_width//cols



#rgb
white = (255, 255, 255)
black = (0, 0, 0)
dark_sq = (122, 102, 119)
light_sq = (204, 183, 174)
sq_border = (230, 230, 250)
bgc = (219, 112, 147)


#pieces
b_PAWN = pygame.transform.scale(pygame.image.load('chess_pieces/b_pawn.png'), (sq_size, sq_size))
w_PAWN = pygame.transform.scale(pygame.image.load('chess_pieces/w_pawn.png'), (sq_size, sq_size))
b_KNIGHT = pygame.transform.scale(pygame.image.load('chess_pieces/b_knight.png'), (sq_size, sq_size))
w_KNIGHT = pygame.transform.scale(pygame.image.load('chess_pieces/w_knight.png'), (sq_size, sq_size))
b_ROOK = pygame.transform.scale(pygame.image.load('chess_pieces/b_rook.png'), (sq_size, sq_size))
w_ROOK = pygame.transform.scale(pygame.image.load('chess_pieces/w_rook.png'), (sq_size, sq_size))
b_BISCHOP = pygame.transform.scale(pygame.image.load('chess_pieces/b_bischop.png'), (sq_size, sq_size))
w_BISCHOP = pygame.transform.scale(pygame.image.load('chess_pieces/w_bischop.png'), (sq_size, sq_size))
b_QUEEN = pygame.transform.scale(pygame.image.load('chess_pieces/b_queen.png'), (sq_size, sq_size))
w_QUEEN = pygame.transform.scale(pygame.image.load('chess_pieces/w_queen.png'), (sq_size, sq_size))
b_KING = pygame.transform.scale(pygame.image.load('chess_pieces/b_king.png'), (sq_size, sq_size))
w_KING = pygame.transform.scale(pygame.image.load('chess_pieces/w_king.png'), (sq_size, sq_size))


