import sys
import pygame as pg
import numpy as np

pg.init()

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
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH =  25

# Initiazlizing the game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic-Tac-Toe AI") 
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))


def draw_lines(color= WHITE):
    for i in range(1, BOARD_ROWS):
        pg.draw.line(screen, color, (0, SQUARE_SIZE *i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pg.draw.line(screen, color, (SQUARE_SIZE *i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range (BOARD_COLUMNS):
            if board[row][col] == 1:
                pg.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pg.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4  , row * SQUARE_SIZE + SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4))
                pg.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

def mark_square(row, col, player):
    board[row][col] = player 

def available_square(row, col):
    return board[row][col] == 0

def is_board_full(check_board=board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if check_board[row][col] == 0:
                return True
    return False

def check_win(player, check_board=board):
    for col in range (BOARD_COLUMNS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
        
    for row in range (BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
        
    if check_board[0][0] == player and check_board[1][1] and check_board[2][2] == player:
        return True
    if check_board[0][2] == player and check_board[1][1] and check_board[2][0] == player:
        return True
    
    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win (2, minimax_board):
        return float('inf')
    if check_win (1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return
    
    if is_maximizing:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score