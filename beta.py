import sys
import pygame as pg
import numpy as np

pygame.init()

# Color constants 
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game constants
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLUMNS = 3
SQUARE_SIZE = WIDTH // BOARD_ROWS
CIRCLE_SIZE = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH =  25

# Initiazlizing the game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic-Tac-Toe AI") 
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))


def draw_line(color= WHITE):
    for i in range(1, BOARD_COLUMNS):
        pg.draw.line(screen, color, start_pos: (0, SQUARE_SIZE * i), end_pos: (WIDTH, SQUARE_SIZE * i),) 
        pg.draw.line(screen, color, start_pos: (SQUARE_SIZE * i), 0, end_pos: ( SQUARE_SIZE * i, HEIGHT)) 

