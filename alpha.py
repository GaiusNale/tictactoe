# This is the first script and i forgot i had commented this out 
import random
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board():
    for row in board:
        print ('|'.join(row))
        print ('-' * 5)

def computer_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == ' ':
            board[row][col] = '0'
            break

def evaluate(board):
    """
    Evaluate the current state of th board,
    Return plus 10 if you win and -10 if the human wins, and 0 for a draw
    """

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return -10
            elif board[row][0] == "O":
                return +10
            
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return -10
            elif board[0][col] == 'O':
                return +10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return -10
        elif board[0][0] == 'O':
            return +10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return -10
        elif board[0][2] == 'O':
            return +10            
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return None 
    
    return 0

def minimax(board, depth, is_maximizing):
    """
    Implement the minimax algorithm to determine the best move for the computer opponent.
    """
    score = evaluate(board)

    # Base case: return the score if the game is over or if the maximum depth is reached
    if score is not None:
        return score

    # If it's the computer's turn
    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '  # Undo the move
                    best_score = max(score, best_score)
        return best_score

    # If it's the opponent's turn
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '  # Undo the move
                    best_score = min(score, best_score)
        return best_score


def player_move():
    while True:
        try: 
            move = int(input("Enter the position you want to play on (1-9): "))
            if 1 <= move <= 9:
                row = (move-1)//3
                col = (move -1) % 3 
                if board [row][col] == ' ':
                    board [row][col] = 'X'
                    return True
                else:
                    print ("that has already been used. Pick another")
            else:
                print ("That's not a position that can be played.")
        except ValueError:
            print ("That's not a number jackass.")
