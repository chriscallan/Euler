# Problem 15
# Published on Friday, 19th April 2002, 06:00 pm; Solved by 123393; Difficulty rating: 5%
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?


rows = 21
cols = 21
my_grid = [[0 for i in range(cols)] for j in range(rows)]
# print("my_grid is now: {0}".format(my_grid))
for i in range(rows):
    for j in range(cols):
        # edge rows have only one possible method to get there
        if i == 0:
            my_grid[i][j] = 1
        if j == 0:
            my_grid[i][0] = 1
        else:
            my_grid[i][j] = my_grid[i - 1][j] + my_grid[i][j - 1]

print("value in the final cell of 20x20 grid is: {0}".format(my_grid[rows-1][cols-1]))