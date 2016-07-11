# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
#   proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.



starting_value = 13
max_value = 999999
winner = {"number": 0, "count": 0, "trail": []}

def halfer(x):
    return int(x / 2)

def triple_plus_one(x):
    return (3 * x) + 1

for i in range(max_value, starting_value, -1):
    breadcrumb_trail = []
    temp_value = 0
    first_run = True
    temp_value = i
    while temp_value > 1 or first_run:
        first_run = False
        if not temp_value % 2:
            temp_value = halfer(temp_value)
        else:
            temp_value = triple_plus_one(temp_value)
        breadcrumb_trail.append(temp_value)
        if temp_value == 1:
            if len(breadcrumb_trail) > winner.get("count"):
                winner.__setitem__("number", i)
                winner.__setitem__("count", len(breadcrumb_trail))
                winner.__setitem__("trail", breadcrumb_trail)
                print("start val: {0}, length: {1}, sequence: {2}".format(i, len(breadcrumb_trail), breadcrumb_trail))
            break

print("winner is: {0}".format(winner))