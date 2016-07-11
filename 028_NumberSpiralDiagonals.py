# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
from math import floor
from enum import Enum

# constants for this problem
grid_rows = 1001      # 1001, for the final problem
grid_cols = grid_rows       # make column/row distinction later on easier
max_idx = grid_rows - 1     #just to make life easier later
grid_print = True           # use this to print the grid after setting it up, later on

#first setup the grid
my_grid = [[0 for x in range(grid_rows)] for y in range(grid_cols)]
# find the starting point
starting_point = int(grid_rows / 2)    # subtract 1 to account for zero-based indexing

# these are "grid maintenance" types of things
grid_filled = False
fill_directions = Enum('direction', 'right down left up')
current_direction = fill_directions.right
grid_value = 1      # start off at zero so that the outside 'while' loop works for all iterations

# start the offsets off with a minimal value
row_offset = 0
col_offset = 0

# working variables, these will be used to keep track of the current positione
candidate_col = starting_point
candidate_row = starting_point

my_grid[candidate_row][candidate_col] = grid_value
grid_value += 1     # this seeds the center of our spiral

while not grid_filled:
    try:
        if current_direction == fill_directions.right and my_grid[candidate_row][candidate_col + 1] == 0:
            candidate_col += 1   # offset by one column
            if my_grid[candidate_row + 1][candidate_col] == 0:
                current_direction = fill_directions.down
        elif current_direction == fill_directions.down and my_grid[candidate_row + 1][candidate_col] == 0:
            candidate_row += 1
            if my_grid[candidate_row][candidate_col - 1] == 0:
                current_direction = fill_directions.left
        elif current_direction == fill_directions.left and my_grid[candidate_row][candidate_col - 1] == 0:
            candidate_col -= 1
            if my_grid[candidate_row - 1][candidate_col] == 0:
                current_direction = fill_directions.up
        elif current_direction == fill_directions.up and my_grid[candidate_row - 1][candidate_col] == 0:
            candidate_row -= 1
            if my_grid[candidate_row][candidate_col + 1] == 0:
                current_direction = fill_directions.right
        else:
            raise Exception("current_direction wasn't in the enum of possible directions: {0}".format(current_direction))
    except IndexError as idxExc:
        break

    if candidate_row == grid_cols and candidate_row == grid_rows:
        grid_filled = True
    else:
        my_grid[candidate_row][candidate_col] = grid_value
        grid_value += 1

if grid_print:
    for x in range(grid_rows):
        row_val = ""
        for y in range(grid_cols):
            row_val += "{0}\t".format(my_grid[x][y])
        print("row {0}: {1}".format(x, row_val))

current_row = 0
running_total = 0
for i in range(grid_cols):
    running_total += my_grid[current_row][i]
    running_total += my_grid[current_row][(-i - 1) if i > 0 else -1] if my_grid[current_row][i] != 1 else 0
    current_row += 1

print("running_total is: {0}".format(running_total))