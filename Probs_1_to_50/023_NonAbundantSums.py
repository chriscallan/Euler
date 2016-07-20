# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less
# than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from math import sqrt, ceil
from itertools import combinations_with_replacement


max_num = 28123     # provided as the mathematical limit for this particular problem
def find_divisors(in_number):
    retval = []    # all numbers are divisible by '1', so we'll just add it here
    retval.append(1)
    for i in range(2, in_number):
        if in_number % i == 0 and i <= ceil(sqrt(in_number)):
            if i not in retval:
                retval.append(i)
            if int(in_number / i ) not in retval:
                retval.append(int(in_number / i))
    retval.sort()
    return retval

def find_all_abundant_numbers(in_max):
    retval = []
    for i in range(1, in_max):      # start at '1' so that 0 isn't tested for "abundantness"
        if sum(find_divisors(i)) > i:
            retval.append(i)
    return retval



abundant_numbers = []
abundant_numbers = find_all_abundant_numbers(max_num)  # initialization step
abundant_numbers.sort()
# working_abundant_numbers = combinations(abundant_numbers, 2)
abundant_sums = {x+y for x, y in combinations_with_replacement(abundant_numbers, 2) if x+y < max_num}
# abundant_numbers = set(abundant_numbers)
print("found the abundant numbers: {0}".format(abundant_sums))

inexpressible = []
for i in range(1, max_num):
    if i in abundant_sums:
        print("i: {0} was in the abundant_sums set".format(i))
    else:
        print("i: {0} was not found in abundant_sums set".format(i))
        inexpressible.append(i)
    # semaphore = False
    # for first in abundant_numbers:
    #     for second in abundant_numbers:
    #         if first + second == i:
    #             print("{0} was expressible as: {1} + {2}".format(i, first, second))
    #             semaphore = True
    #             break       # is expressible so move on to the next candidate number
    #         elif ((list(abundant_numbers).index(second) == (len(abundant_numbers) - 1)) and
    #                 (list(abundant_numbers).index(first) == (len(abundant_numbers) - 1))):
    #             print("{0} is being added to the inexpressible array".format(i))
    #             if i not in inexpressible:
    #                 inexpressible.append(i)
    #             break
    #         else:
    #             continue
    #     if semaphore:
    #         break

print("inexpressable is: {0}".format(inexpressible))
print("answer is: {0}".format(sum(inexpressible)))
