## Tic-Tac-Toe 

This is a Python script that implements a game of Tic Tac Toe. The code contains a few functions that are used to print the game board, accept user inputs, and check for a winning condition.

The code imports three libraries: `termtables`, `datetime`, and `emoji`. The termtables library is used to draw the grid for the game, the datetime library is used to calculate the time taken for the game to complete, and the emoji library is used to print emojis.

The `print_grid` function takes three parameters, which represent the rows of the game board, and prints the board to the console using the termtables library.

The `input_values` function accepts user inputs for row and column positions and updates the game board. It returns `True` if the inputs are valid and `False` otherwise.

The `winning_case` function checks if the move made by a player is a winning move, and returns the player number (1 or 2) if it is. If there is no winner, the function returns `0`.

Overall, this is a relatively simple implementation of the game of Tic-Tac-Toe in Python, and could be improved by adding more features such as AI opponents or more sophisticated game logic.
