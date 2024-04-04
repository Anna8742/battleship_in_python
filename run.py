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
player_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Initialize computer's primary board
computer_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def print_board(board):
    """
    Function to print the game board.
    """
    print('  A B C D E F G H I J ')
    print('  +-+-+-+-+-+-+-+-+-+ ')
    for i, row in enumerate(board):
        print("%2d|%s|" % (i + 1, "|".join(row)))
    print('  +-+-+-+-+-+-+-+-+-+ ')


def user_guess():
    """
    Function that makes player to make a guess.
    It returns a tuple containing the row and column of the guesses.
    """
    while True:
        try:
            print("Enter your guess")
            row = int(input("Enter the number from 1 to 10: ")) - 1
            if row not in range(BOARD_SIZE):
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
    It returns a tuple of the computer's guess.
    """
    return randint(0, BOARD_SIZE - 1), randint(0, BOARD_SIZE - 1)


def check_result(guess, board, hits, misses):
    """
    Function to check the result of a guess made by computer and player.
    It takes arguments: guess, board - to check against it, sets of hits and misses.
    It updates sets based on the result and returns True for a hit and False for a miss.
    """
    row, column = guess
    if board[row][column] == "S":
        print("Hit")
        hits.add((row, column))
        board[row][column] = "X"
        return True
    else:
        print("Miss! ")
        misses.add((row, column))
        board[row][column] = "M"
        return False


def place_battleships(board):
    """
    This function locates battleships on the board.
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

            # Game loop
            while len(player_hits) < NUMBER_OF_SHIPS and len(computer_hits) < NUMBER_OF_SHIPS and len(player_misses) < BOARD_SIZE:
                # Player's turn
                print("\nYour Turn:")
                print_board(computer_board)
                user_guess_coord = user_guess()
                if check_result(user_guess_coord, computer_board, player_hits, player_misses):
                    print("Your guess:")
                    print_board(computer_board)
                else:
                    print("Your guess:")
                    print_board(computer_board)

                if len(computer_hits) == NUMBER_OF_SHIPS:
                    print("Congratulations! You sank all of the computer's battleships!")
                    break

                # Computer's turn
                print("\nComputer's Turn:")
                computer_guess_coord = AI_guess()
                print("Computer's guess:", chr(computer_guess_coord[1] + 65) + str(computer_guess_coord[0] + 1))
                if check_result(computer_guess_coord, player_board, computer_hits, computer_misses):
                    print("Computer's guess:")
                    print_board(player_board)
                else:
                    print("Computer's guess:")
                    print_board(player_board)

                if len(player_hits) == NUMBER_OF_SHIPS:
                    print("Oops! All of your battleships have been sunk by the computer!")
                    break

            # Play again
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thank you for playing! Goodbye!")
                break
        except Exception as e:
            print("An error occurred. Restarting the game.")


if __name__ == "__main__":
    main()
