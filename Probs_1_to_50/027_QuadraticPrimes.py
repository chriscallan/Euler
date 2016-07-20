# Problem 27
# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However,
#   when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41
#       is clearly divisible by 41.
#
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values
#       n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
#   primes for consecutive values of n, starting with n = 0.
from math import sqrt

prime_list = []
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

def prime_factors(in_number):
    retVal = []
    if in_number < 2:
        raise ValueError("There are no factors for that which you can't figure out on your own.")
    divisor = 2
    # print("divisor is: {0}".format(divisor))
    while in_number > 1:
        if not in_number % divisor:
            # print("inside the if-not")
            if divisor not in retVal:
                retVal.append(divisor)
            in_number /= divisor
            # print("in_number is now: {0}".format(in_number))
            divisor -= 1
            # print("divisor was decremented to: {0}".format(divisor))
        divisor += 1
        # print("divisor was incremented to: {0}".format(divisor))
    # print("about to return: {0}".format(retVal))
    return retVal

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False]*(int((n - i * i - 1)/(2 * i)) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

prime_list = primes(19970010)
print("prime_list is now: {0} long".format(len(prime_list)))
# for temp in range(1, 1997001):
#     if is_prime(temp):
#         prime_list.append(temp)

max_limit = 1000
prime_list = set(prime_list)
max_consecutive = 0
a_b_winner = ()

for a in range(-999, max_limit, 2):
    is_consecutive = True
    # print("back at a: {0}".format(a))
    for b in range(-1000, max_limit):
        n = 0
        while abs(((n*n)+(a*n)+b)) in prime_list:
            n += 1
        # for n in range(max_limit):
        #     test_value = (n * n) + (a * n) + b
        #     if test_value not in prime_list and n > max_consecutive:
        #         is_consecutive = False      # need this for the semaphore on the parent loop here
        #         max_consecutive = n - 1
        #         a_b_winner += (a - 1, b - 1,)
        #         break
            if n > max_consecutive:
                max_consecutive = n
                a_b_winner = (a, b,)
            # if not test_value % 2 == 0:     # don't test even numbers
            #     factors = prime_factors(test_value)
            # if len(factors) == 1:   # only primes are divisible by 1 and themselves
            #     print("n: {0}, a: {1}, b: {2}".format(n, a, b))
            #     break

print("max_consecutive was: {0}".format(max_consecutive))
print("a: {0}, b: {1}, product of the two: {2}".format(a_b_winner[0], a_b_winner[1], (a_b_winner[0] * a_b_winner[1])))

