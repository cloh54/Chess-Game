import pygame
from pygame import font
from chess.constants import white, black, WIDTH, HEIGHT, sq_size, b_width, b_height, board_x, board_y
from chess.board import Board
from chess.game import Game

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHESS')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y-board_y)//sq_size
    col = (x-board_x)//sq_size
    return row, col

def search_font(name):
    found_font = font.match_font(name)
    return found_font

def message_display(used_font, size, color, xy, message):
    font_object = pygame.font.Font(used_font, size)
    rendered_text = font_object.render(message, True, (color))
    WIN.blit(rendered_text, (xy))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)
        
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if x<(board_x+b_width) and x>board_x and y<(board_y+b_height) and y>board_y:
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        
        game.update()
    
    pygame.quit()


main()
