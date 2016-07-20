# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
#       amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#   The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000. (31626)
from math import sqrt, ceil

def get_divisor_sum(in_number):
    retval_divisors = []
    for potential_divisors in range(1, ceil(sqrt(in_number))):
        if in_number % potential_divisors == 0:
            retval_divisors.append(potential_divisors)
            correlary_divisor = in_number / potential_divisors
            if correlary_divisor not in retval_divisors and correlary_divisor != in_number:
                retval_divisors.append(int(in_number / potential_divisors))
    return sum(retval_divisors)

amicable_pairs = []
dont_repeat = []
for searcher in range(1, 10000):
    if searcher in dont_repeat:
        continue
    working_val = get_divisor_sum(searcher)
    amicable_val = get_divisor_sum(working_val)
    if searcher == amicable_val and working_val != searcher:
        amicable_pairs.append([searcher, working_val])
        dont_repeat.append(searcher)
        dont_repeat.append(working_val)
print("amicable pairs are: {0}".format(amicable_pairs))

total = 0
for pair in amicable_pairs:
    total += pair[0] + pair[1]
print("sum of all amicable numbers are: {0}".format(total))