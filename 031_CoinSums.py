# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import sys


coins = [1, 2, 5, 10, 20, 50, 100, 200]
my_target = 200
ways = [0] * (my_target + 1)
ways[0] = 1
for x in coins:
    for i in range(x, (my_target + 1)):
        ways[i] += ways[i-x]
print("the number of 'ways' to make 2 pounds is: {0}".format(ways[my_target]))
# combinations = {}
# # this is the seed for all the work that comes on later
# for seed in range(len(coins)):
#     combinations[seed, 0] = 1   # this sets up the combinatorial for making "1p" using our coin set
#     combinations[0, seed] = 1
#
# for x in range(len(coins)):
#     for y in range(1, len(coins)):
#         print("x: {0}, y: {1}".format(x, y))
#         try:
#             if x > coins[y]:
#                 # combinations.update({(x, y): combinations[x, y] + combinations[x, y - 1]})
#                 # combinations.update({(x, y): combinations[x, y] + combinations[x - coins[y], y]})
#                 combinations[x, y] += combinations[x, y - 1]
#                 combinations[x, y] += combinations[x - coins[y], y]
#             else:
#                 combinations[x, y] = combinations[x, y - 1]
#         except KeyError as exc:
#             print("Exception is: {0}".format(sys.exc_info()))
#         print("combinations[{0}, {1}]: {2}".format(x, y, combinations[x, y]))

# print("There are: {0} ways to make 2 pounds from coins.".format(len(combinations)))