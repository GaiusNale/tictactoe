import sys
import pygame
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


