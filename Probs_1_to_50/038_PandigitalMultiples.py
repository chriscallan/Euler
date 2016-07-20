# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
#   product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital,
#   918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
#   with (1,2, ... , n) where n > 1?
import itertools
from helpers.helper_methods import *

max_len = 9
min_pan = 1
my_range = range(1, max_len + 1)    # add 1 to make sure we get the digit '9'
high_numbers = []
final_answer = []
for variation in itertools.permutations(my_range, len(my_range)):
    # print("variation is: {0}".format(str(variation)))
    high_numbers.append(variation)

achiever = 0
for i in range(9000, 10000):
    temp_worker = str(i) + str(i * 2)
    if helper_methods.is_pandigital(temp_worker, min_pan, max_len):
        print("found pandigital: {0}".format(temp_worker))
        if '0' not in temp_worker:
            if len(str(temp_worker)) == 9:
                if int(temp_worker) > achiever:
                    achiever = int(temp_worker)

print("answer is: {0}".format(achiever))
