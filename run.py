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
                # Ship
                display_row.append("S")  
            elif (i, j) in hits:
                # Hit
                display_row.append("H")  
            elif (i, j) in misses:
                # Miss
                display_row.append("M")  
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

def check_result(guess, board, hits, misses):
"""
Function to check the result of a guess made by computer and player. 
It takes arguments: guess, board - to check against it, sets of hits and misses.
It updates sets based on the result and returns True for a hit and False for a miss.
"""
    row, column = guess
    if board[row][column] == "X":
        print("Hit")
        hits.add((row, column))
        board[row][column] = "H"
        return True
    else:
        print("Miss! ")
        misses.add((row, column))
        return False


def place_battleships(board):
"""
This funcion locates battleships on the board. 
It takes the board as an argument and returns a set of the placed ships.
"""
    ships = set()  
    for _ in range(5):
        row, column = randint(0, 9), randint(0, 9)
        while board[row][column] == "X":
            row, column = randint(0, 9), randint(0, 9)
        board[row][column] = "X"
        ships.add((row, column))
    return ships

def main():
    """
    Main function to run all functions and allow to play multiple games
    """
    while True:
        # Initialize player's ships
        player_ships = place_battleships(player_board)