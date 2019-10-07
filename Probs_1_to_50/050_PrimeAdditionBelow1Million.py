#!/usr/bin/env python


# layout all the helper methods that will make things easier
def sieve_of_eratosthenes(prospect_value):
    """
    Creates a list of all prime numbers below the input
        - utilizies the Sieve of Erasthosthenes for max performance
    :return a list containing all prime numbers below 'prospect_value', and zeros for all non-prime values
    """
    primes = list(range(prospect_value))    # create the empty list
    # seed the 'matrix' with known non-primes
    primes[0] = 0
    primes[1] = 0
    seed = 2
    
    while seed * seed <= prospect_value:    # Only need to go from 2 to int(sqrt(x))
        # already crossed out, continue
        if primes[seed] == 0:
            seed += 1
            continue
        j = 2 * seed      # now get the multiples of 'seed'
        while j < prospect_value:
            primes[j] = 0   # Cross out this as it is composite
            j += seed       # cover all multiples of i
        seed += 1
    return primes


def get_primes_below_target(in_target):
    """
    Helper method to encapsulate the filtering of the return value of the non-primes
    :param in_target: max value that you want primes to be less than
    :return: list of prime numbers in ascending order
    """
    ret_val = sieve_of_eratosthenes(target_val)    # first get all primes < target_val
    ret_val = [x for x in ret_val if x != 0]  # filter out all the non-prime values
    return ret_val


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def add_up_sieve_values_to_prime(in_list, start_idx, max_value):
    ret_val = 0
    ret_list = []
    for i in range(len(in_list[start_idx:])):
        if ret_val + in_list[i + start_idx] <= max_value:
            ret_list.append(in_list[i + start_idx])
            ret_val += in_list[i + start_idx]
            # print("adding: {}, index: {}, totalling: {}".format(tmp_val, in_list.index(tmp_val), ret_val))
        else:
            break
    if isPrime(ret_val):
        return ret_val, ret_list
    else:
        return 0, []
    

#   Start the actual program execution here
print("check for primes")
target_val = 1000000

local_primes = get_primes_below_target(target_val)
largest_value = 0
largest_items = []
for i in range(len(local_primes)):
    the_answer, the_answer_list = add_up_sieve_values_to_prime(local_primes, i, target_val)
    # print("the_answer: {},\ntha_answer_list: {}".format(the_answer, the_answer_list))
    if the_answer > largest_value and len(the_answer_list) > len(largest_items):
        largest_value = the_answer
        largest_items = the_answer_list.copy()
        print("largest_value: {}\nmade of: {}".format(largest_value, the_answer_list))

