from random import randint

# Rules of the game
rules = """BATTLESHIPS GAME RULES: \n\nThe game is played on grids on which each player's fleet of battleships are marked.. 
\nThe grids are square 10x10, and the location of the fleets are concealed from the other player.
\nPlayers call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
\nIt's a single user game to play against the computer. """
print(rules)

grid = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}


first_board =  [[" "] * 9 for x in range(9)]

record_board = [[" "] * 9 for x in range(9)]

def create_board(b):
    print('  A B C D E F G G I J ')
    print('  +-+-+-+-+-+-+-+-+-+ ')
    number = 1
    for row in b: 
        print("%d|%s|" % (number, "|".join(row)))
        number += 1

create_board(first_board)