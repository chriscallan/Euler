# Problem 10
# Published on Friday, 8th February 2002, 06:00 pm; Solved by 211840; Difficulty rating: 5%
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from math import sqrt


def is_prime(test_number):
    retval = True
    if test_number > 2:
        divisor = 2
        while divisor <= sqrt(test_number):
            if test_number % divisor == 0:
                retval = False
                break
            if divisor % 2 == 0:
                divisor += 1
            else:
                divisor += 2
    return retval

running_total = 0   # can start wtih '1' & '2' already in there

for i in range(2, 2000000):
    if is_prime(i):
        running_total += i
    else:
        if i % 3001 == 0:
            print("now working on: {0}".format(i))

print("sum of all primes below 2 million is: {0}".format(running_total))