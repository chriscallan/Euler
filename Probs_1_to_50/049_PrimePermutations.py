# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#   (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there
#   is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
from helpers.helper_methods import helper_methods as hm
from itertools import permutations
import timeit



def method1():
    """
    Initial swing at solving this issue, a rather slow implementation though
    :return: n/a
    """
    lower_bound = 1000
    upper_bound = 10000
    target_digit_len = 4
    for i in range(1000, 10000):    # define the range for 4-digit numbers
        distance = 0
        if hm.is_prime(i):      # don't need further processing if the starting number isn't prime
            perm_set = sorted(set([int(''.join(x)) for x in permutations(str(i), 4)]))
            for perm in perm_set:
                # strips off the leading '0', if any, and makes sure we're not repeating our seed value
                if len(str(int(perm))) < target_digit_len or perm == i:
                    continue
                # derive the distance value from the first two numbers that we're working with
                distance = i - int(perm) if (i - int(perm)) > 0 else int(perm) - i
                if distance + i in perm_set and hm.is_prime(distance + i):
                    second_number = distance + i
                    if second_number in perm_set:
                        if second_number + distance in perm_set and hm.is_prime(distance + second_number):
                            third_number = second_number + distance
                            print("method1")
                            print("I think I found one: {0}, {1}, {2}".format(i, second_number, third_number))
    return True

def method2():
    """
    A more elegant and performant solution to the problem statement, about 6x faster than method1()
    :return: n/a
    """
    prime_set = sorted(set(hm.generate_prime_list(10000)))
    for prime in prime_set:
        if len(str(prime)) < 4:
            continue
        perms = sorted(set([int(''.join(x)) for x in permutations(str(prime), 4)]))
        dist = 0
        for variation in perms:
            if variation in prime_set:
                dist = prime - variation if prime - variation > 0 else variation - prime
                final_var = dist + variation
                if final_var in prime_set and variation != prime and final_var != prime and final_var in perms:
                    print("methdd2")
                    print("got me another: {0}, {1}, {2}".format(prime, variation, dist + variation))
    return True

# run both methods through the old timer facilities to see who comes out on top
print(timeit.timeit(stmt=method1, number=3))
print(timeit.timeit(stmt=method2, number=3))


