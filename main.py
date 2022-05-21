from unicodedata import name
import pygame

from config import *
from computer_player import *
from draw import *
from tkinter import *

name = ''
def win(screen, winner = "Player"):
    
    if winner == "Player":
        # Label(root, text = name + win_text2  , font=text_font).pack()
        display_text(screen, win_text1 + name + win_text2  , (screen_size[0] // 2, screen_size[1] // 2))
    else:
        # Label(root, text = name + lose_text  , font=text_font).pack()
        display_text(screen, name + lose_text , (screen_size[0] // 2, screen_size[1] // 2))
    

def check_if_end_game(screen, board):
    if enemy_five_in_a_row(board, 1):
        win(screen, "Player")
        return 1
    elif enemy_five_in_a_row(board, -1):
        win(screen, "Computer")
        return 1
    return 0

def window_game():
    global name
    name = username.get()
    root.destroy()
    
    pygame.init()

    screen = draw_screen()
    

    board = new_board()

    pygame.display.update()

    game_over = False

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if game_over:
                    pygame.quit()
                pos = pygame.mouse.get_pos()
                x = pos[0] // 40
                y = pos[1] // 40
                if board[x][y] != 0:
                    continue
                drawX(screen, x, y)
                board[x][y] = 1
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev1 = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
                computer_reply(screen, board)
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev = pygame.event.get()
                    game_over = True
                    continue
                pygame.display.update()
                



root = Tk()
root.title("Caro")
root.geometry("400x400")
root.config(background= '#8ec8ed')

def myClick():
	lb = Label(root, text = "Hello world!")
	lb.grid(row = 3, column = 0)

Label(root, text = 'User Name').pack()

username =  Entry(root, font = text_font, width = 15, background= 'white')
username.pack()
username.focus()

button = Button(root, text = "Start", command = window_game).pack()

root.mainloop()
