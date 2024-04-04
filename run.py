from random import randint

# Rules of the game
rules = """BATTLESHIPS GAME RULES: \n\nThe game is played on grids on which each player's fleet of battleships are marked. 
\nThe grids are square 10x10, and the location of the fleets are concealed from the other player.
\nPlayers call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
\nIt's a single user game to play against the computer. """
print(rules)

# Constants
BOARD_SIZE = 10
NUMBER_OF_SHIPS = 5



# Mapping of letters to grids
grid = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

# Initialize player's primary board
player_board = [[" "] * 10 for _ in range(10)]

# Initialize computer's primary board
computer_board = [[" "] * 10 for _ in range(10)]


def create_primary_board(board, ships=None, hits=None, misses=None, user_guess=None):
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
    user_guess = set() if user_guess is None else user_guess
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
            elif (i, j) in user_guess:
                # User Guess
                display_row.append("X")
            else:
                display_row.append(cell)
        print("%2d|%s|" % (number, "|".join(display_row)))
        number += 1


def user_guess():
    """
    Function that makes player to make a guess.
    It returns a tuple containing the row and column of the guesses.
    """
    while True:
        try:
            print("Enter your guess")
            row = int(input("Enter the number from 1 to 10: ")) - 1
            if row not in range(10):
                raise ValueError("Row must be between 1 and 10.")
            column = input("Enter a letter from A to J: ").upper()
            if column not in "ABCDEFGHIJ":
                raise ValueError("Column must be a letter from A to J.")
            return row, grid[column]
        except ValueError as e:
            print("Incorrect input:", e)


def AI_guess():
    """
    Function to generate a random guess for the computer's turn.
    It returns of tuple of the computer's guess
    """
    row = randint(0, 9)
    column = randint(0, 9)
    return row, column


def check_result(guess, board, hits, misses, user_guess):
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
        user_guess.add((row, column))
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
        try:
            # Initialize player's ships
            player_ships = place_battleships(player_board)

            # Initialize hits and misses sets for both player and computer
            player_hits = set()
            player_misses = set()
            computer_hits = set()
            computer_misses = set()
            player_guesses = set()

            # Game loop
            while len(player_hits) < 5 and len(computer_hits) < 5 and len(player_misses) < 10:
                # Player's turn
                print("\nPlayer's Turn:")
                print("\nPlayer's guesses on computer's board: ")
                create_primary_board(computer_board, hits=player_hits, misses=player_misses, user_guess=player_guesses)
                user_guess_coord = user_guess()
                if check_result(user_guess_coord, computer_board, computer_hits, computer_misses, player_guesses):
                    print("\nPlayer's Primary Board: ")
                    create_primary_board(player_board, ships=player_ships, hits=computer_hits, misses=computer_misses)
                else:
                    print("\nPlayer's Primary Board: ")
                    create_primary_board(player_board, ships=player_ships, hits=computer_hits, misses=computer_misses)

                if len(computer_hits) == 5:
                    print("\nCongratulations! You sank all the computer's battleships!")
                    break

                # Computer's turn
                print("\nComputer's Turn:")
                computer_guess_coord = AI_guess()
                print("Computer guesses:", computer_guess_coord)
                if check_result(computer_guess_coord, player_board, player_hits, player_misses, player_guesses):
                    print("\nPlayer's Primary Board and computer's guesses: ")
                    create_primary_board(player_board, ships=player_ships, hits=player_hits, misses=player_misses,
                                         user_guess=player_guesses)
                else:
                    print("\nPlayer's Primary Board and computer's guesses: ")
                    create_primary_board(player_board, ships=player_ships, hits=player_hits, misses=player_misses,
                                         user_guess=player_guesses)

                if len(player_hits) == 5:
                    print("\nOops! All your battleships have been sunk by the computer!")
                    break

            # Play again
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thank you for playing! Goodbye!")
                break
        except Exception as e:
            print("Error:", e)
            print("An error occurred. Restarting the game.")


if __name__ == "__main__":
    main()
