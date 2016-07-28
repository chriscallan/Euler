# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
import helpers.helper_methods as hm


lower_bound = 134000  # 2 * 3 * 5 * 7     # lower bound is the 4 lowest primes multiplied together, seems a good starting point
max_try = 1000000           # arbitrary upper limit, we should find our answer well before this is reached
target_factors = 4          # makes this useful for other problems of this ilk
target_consec = 4           # again, makes this useful for other problems related to this one
# simple method to create a set of primes in a data structure that is very fast at lookups
prime_set = sorted(set(hm.helper_methods.generate_prime_list(max_try)))

def count_of_prime_factors(in_number, factor_set):
    """
    Method to encapsulate the logic of finding out how many factors in_number has in the factor_set
        Adapted from here (http://www.mathblog.dk/project-euler-47-distinct-prime-factors/)
    :param in_number: the number that you'd like to determine the number of factors for
    :param factor_set: iterable object that holds the values that may be factors of in_number
    :return: the count
    """
    retval = []
    remainder = in_number

    for prime in factor_set:
        if prime ** 2 > in_number:
            retval += (prime, )
            break
        while remainder % prime == 0:
            remainder = remainder / prime
            retval += (prime, )
        if remainder == 1:
            break

    return retval

consecutive = 0
answer_list = []
# continue as long as the number of consecutive integers is less than our target
while consecutive < target_consec:
    lower_bound += 1    # lower_bound is our ever-increasing target value
    temp_return = count_of_prime_factors(lower_bound, prime_set)
    # casting to set() removes duplicates, aka counts distinct values
    if len(set(temp_return)) == target_factors:
        consecutive += 1    # found one with the desired number of distinct prime factors
        # print("found potential: {0} with consecutive: {1}".format(lower_bound, consecutive))
        answer = dict()
        answer["number"] = lower_bound
        answer["factors"] = temp_return
        answer_list.append(answer)
    else:
        consecutive = 0     # either wasn't factorable with primes or had too many/not enough
        answer_list.clear()     # make sure you don't hold onto old candidates
        # print("bypassing: {0}".format(lower_bound))

for my_answer in answer_list:
    print("answer{0} is: {1}, factors: {2}".format(answer_list.index(my_answer) + 1, my_answer["number"],
                                                   my_answer["factors"]))


