
from random import randint

rules = '''RULES: \nThe game is played on four grids, two for each player. 
\nThe grids are square 10x10, and the individual squares in the grid are identified by letter and number.
\nOne one grid the player arranges ships and records the shots by the opponent. on the other, hidden grid, the player records their own shots.
\n Before play begins, the ships are secretly arranged on the primary grid. The types of numbers of ships are allowed are the same for each player.'''
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





