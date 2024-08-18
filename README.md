# Tic-Tac-Toe AI

This is a simple Tic-Tac-Toe game with a basic AI opponent implemented using Python and Pygame. The AI uses the Minimax algorithm to make optimal moves.

## Features

- Play against the computer.
- The AI uses the Minimax algorithm to ensure it plays optimally.
- Game state is visually displayed on a 3x3 grid.
- The game supports restarting by pressing the 'R' key.
- Visual indicators for win, lose, or draw.

## Requirements

- Python 3.x
- Pygame library
- Numpy library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/tic-tac-toe-ai.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tic-tac-toe-ai
    ```

3. Install the required dependencies:

    ```bash
    pip install pygame numpy
    ```

## How to Play

1. Run the game:

    ```bash
    python tic_tac_toe_ai.py
    ```

2. The game window will open with a 3x3 grid.
3. You play as the human (represented by circles), and the computer plays as the AI (represented by crosses).
4. Click on a square to place your circle.
5. The AI will automatically make its move after yours.
6. The game ends when either player wins or the board is full.
7. Press 'R' to restart the game.

## Code Overview

- `draw_lines()`: Draws the grid lines on the screen.
- `draw_figures()`: Draws circles (player) and crosses (AI) on the board.
- `mark_square(row, col, player)`: Marks a square on the board with the current player's move.
- `available_square(row, col)`: Checks if a square is available to mark.
- `is_board_full()`: Checks if the board is full, indicating a draw.
- `check_win(player)`: Checks if a player has won the game.
- `minimax()`: The core of the AI, recursively evaluates the game state to make optimal moves.
- `best_move()`: Determines the best move for the AI.
- `restart_game()`: Resets the game board and allows the player to start over.

## Controls

- **Mouse Click**: Place a circle on the selected square.
- **R Key**: Restart the game.

## Future Improvements

- Add different difficulty levels for the AI.
- Implement a scoring system.
- Allow players to choose between playing as a circle or a cross.

## License

This project is open-source and available under the MIT License.