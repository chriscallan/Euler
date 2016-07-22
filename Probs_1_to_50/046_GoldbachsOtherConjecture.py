# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
#   a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
from helpers.helper_methods import *


max_limit = 100000
# generate these outside the method so that we don't have to regenerate this again and again
prime_set = sorted(set(helper_methods.generate_prime_list(max_limit)))
print("done making primes")
def is_odd_goldbach(in_number):
    retval = False
    for prime in prime_set:
        if prime > i:
            break  # no need to check when my prime is larger than the value to describe
        for j in range(1, 500):
            print("checking the answer for: {0}, with prime: {1}, and j: {2}".format(i, prime, j))
            gold_num = prime + (2 * (j ** 2))
            if gold_num == in_number:
                retval = True
                break
    return retval

answer = 0
for i in range(35, max_limit, 2):
    if helper_methods.is_prime(i):  # skip prime digits
        continue
    if not is_odd_goldbach(i):
        answer = i
        break

print("answer is: {0}".format(answer))
