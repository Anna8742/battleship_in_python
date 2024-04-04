from random import randint

"""
This code was inspired by the tutorial 
"""

# Rules of the game
rules = """BATTLESHIPS GAME RULES: \n\nThe game is played on grids on which each player's fleet of battleships are marked.. 
\nThe grids are square 10x10, and the location of the fleets are concealed from the other player.
\nPlayers call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
\nIt's a single user game to play against the computer. """
print(rules)

# Mapping of letters to grids
grid = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}

# Initialize player's primary board
player_board = [[" "] * 10 for _ in range(10)]

# Initialize computer's primary board
computer_board = [[" "] * 10 for _ in range(10)]

def create_primary_board(board, ships=None, hits=None, misses=None):
    """
    Function to create and print the primary game board. 
    As arguments it takes 'board' as an input to display primary board, 
    'ships', 'hits', and 'misses' to display them on the board. The ships are 
    represented by "S", hits by "H" and misses by "M" on the board.
    """
    print('  A B C D E F G H I J ')
    print('  +-+-+-+-+-+-+-+-+-+ ')
    number = 1
    ships = set() if ships is None else ships
    hits = set() if hits is None else hits
    misses = set() if misses is None else misses
    for i, row in enumerate(board):
        display_row = []
        for j, cell in enumerate(row):
            if (i, j) in ships:
                display_row.append("S")  # Ship
            elif (i, j) in hits:
                display_row.append("H")  # Hit
            elif (i, j) in misses:
                display_row.append("M")  # Miss
            else:
                display_row.append(cell)
        print("%2d|%s|" % (number, "|".join(display_row)))
        number += 1

def user_guess():
    """
    Function that makes player to make a guess. 
    It returns a tuple containing the row and column of the guesses.
    """
    print("Enter your guess")
    row = int(input("Enter the number from 1 to 10: ")) - 1
    while row not in range(10):
        print("Incorrect input, try again.")
        row = int(input("Enter a number from 1 to 10: ")) - 1
    column = input("Enter a letter from A to J: ").upper()
    while column not in "ABCDEFGHIJ":
        print("Incorrect input, try again.")
        column = input("Enter a letter from A to J: ").upper()
    return row, grid[column]

def AI_guess():
    """
    Function to generate a random guess for the computer's turn. 
    It returns of tuple of the computer's guess
    """
    row = randint(0, 9)
    column = randint(0, 9)
    return row, column