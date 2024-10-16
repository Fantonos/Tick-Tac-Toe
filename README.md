# Tic Tac Toe 

This is a simple command-line Tic Tac Toe game implemented in Python. The game supports two modes: Player vs Player and Player vs Bot.

## Features

- Two game modes: Player vs Player and Player vs Bot
- Interactive command-line interface
- Randomized bot moves
- Help section for game instructions
- Win condition checking

## How to Play

1. Run the script using Python:

2. Choose the game mode:
- Enter `1` for Player vs Player
- Enter `2` for Player vs Bot

3. Players take turns entering their moves using the coordinate system:
```         
        (1)  (2)  (3)
    A) | A1 | A2 | A3 |
    B) | B1 | B2 | B3 |
    C) | C1 | C2 | C3 |
```

4. Enter the coordinates (e.g., A1, B2, C3) to place your symbol on the board.

5. The game continues until a player wins or the game ends in a tie.

## Help

You can access the help section at any time by typing `HELP`, `H`, `HE`, or `HEL` when prompted for input.

## Game Logic

- The game board is represented by a dictionary `tic_tac_dic`.
- Players use symbols 'X' and 'O'.
- The `check_if_won` function checks for winning conditions after each move.
- In Player vs Bot mode, the bot makes random moves using the `bots_move` function.

## Functions

- `get_player_input`: Handles player input and updates the game board
- `display_game_board`: Prints the current state of the game board
- `bots_move`: Generates a random move for the bot
- `help_section`: Displays game instructions
- `check_if_won`: Checks if the current player has won
- `main`: Main game loop
- `start`: Initiates the game and handles game mode selection

## Requirements

- Python 3.x

## License

This project is open-source and available under the MIT License.
[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
