import pygame
from config import *
from positions import *

def drawX(screen , x = 0, y = 0):
    points = ((x * square_size + from_border, y * square_size + from_border), 
             ((x + 1) * square_size - from_border, (y + 1) * square_size - from_border), 
             ((x + 1) * square_size - from_border, y * square_size + from_border), 
             (x * square_size + from_border, (y + 1) * square_size - from_border))
    pygame.draw.line(screen, X_color, points[0], points[1], tic_tac_thickness)
    pygame.draw.line(screen, X_color, points[2], points[3], tic_tac_thickness)

def drawO(screen, x = 0, y = 0):
    pygame.draw.circle(screen, O_color, ((x + 0.5) * square_size, (y + 0.5) * square_size), square_size // 3, tic_tac_thickness)

def draw_screen():
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    i = 0
    while i < 1000:
        pygame.draw.line(screen, (0,0,0), (i, 0), (i, 1000), border_thickness)
        pygame.draw.line(screen, (0,0,0), (0, i), (1000, i), border_thickness)
        i += square_size
    return screen

def new_board():
    board = [[0 for x in range(screen_size[0] // square_size)] for y in range(screen_size[1] // square_size)]
    return board

def display_text(screen, text, coordinate):
    font = pygame.font.Font(text_font, text_size)
    screen_text = font.render(text, True, text_color)
    textRect = screen_text.get_rect()
    textRect.center = (coordinate[0], coordinate[1])
    screen.blit(screen_text, textRect)

def win(screen, winner = "Player"):
    if winner == "Player":
        display_text(screen, win_text , (screen_size[0] // 2, screen_size[1] // 2))
    else:
        display_text(screen, lose_text, (screen_size[0] // 2, screen_size[1] // 2))

def check_if_end_game(screen, board):
    if enemy_five_in_a_row(board, 1):
        win(screen, "Player")
        return 1
    elif enemy_five_in_a_row(board, -1):
        win(screen, "Computer")
        return 1
    return 0
    