# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
#   left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
#       3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from Euler.helpers.helper_methods import *


max_limit = 1000000


def truncate_left(in_number):
    retval = []
    worker = in_number
    # while len(worker) > 1:  # go down to length '1' so as to avoid adding empty entries
    #     retval.append(worker[1:])
    #     worker = worker[1:]

    try:
        while worker > 10:
            temp_worker = worker - (int(worker / (10 ** (len(str(worker)) - 1))) * (10 ** (len(str(worker)) - 1)))
            retval.append(temp_worker)
            worker = temp_worker
    except Exception as exc:
        pass
    return retval


def truncate_right(in_number):
    retval = []
    worker = in_number
    # while len(worker) > 1:
    #     retval.append(worker[:-1])
    #     worker = worker[:-1]
    while int(worker / 10) > 0:
        temp_worker = int(worker / 10)
        retval.append(temp_worker)
        worker = temp_worker
    return retval


def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1) // 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) // 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


print("figuring out the primes")
primes = primes(max_limit)
# for i in range(1, max_limit, 2):  # no need to even look at even numbers, beyond '2' that is
#     if i % 3333 == 0:
#         print("working on {0}".format(i))
#     if helper_methods.is_prime(i):
#         primes.append(i)
print("found: {0}".format(len(primes)))

final_answer = set()
for prime in primes:
    all_good = True
    for bad_digit in ['0', '2', '4', '5', '6', '8']:
        if bad_digit in str(prime) or '1' in str(prime):
            if '1' in str(prime):
                if str(prime).index('1') == 0 or str(prime).rindex('1') == (len(str(prime)) - 1):
                    all_good = False
                    break
            if (bad_digit == 2 or bad_digit == 5) and (str(prime).index('2') > 0 or str(prime).index('5') > 0):
                all_good = False
                break
    if all_good:
        # print("investigating {0}".format(prime))
        # left = set(truncate_left(prime))
        # right = set(truncate_right(prime))
        # if left.issubset(primes) and right.issubset(primes):
        #     final_answer.add(prime)
        for left in truncate_left(prime):
            if not helper_methods.is_prime(int(left)):
                all_good = False
                continue
        for right in truncate_right(prime):
            if not helper_methods.is_prime(int(right)):
                all_good = False
                continue
        if all_good:
            print("Found prime: {0} is left/right truncatable".format(prime))
            final_answer.add(prime)
# these are considered non-truncatable
if 2 in final_answer:
    final_answer.remove(2)
if 3 in final_answer:
    final_answer.remove(3)
if 5 in final_answer:
    final_answer.remove(5)
if 7 in final_answer:
    final_answer.remove(7)
list(final_answer)
presentable = list(final_answer)
presentable.sort()
print("All values I found are: {0}".format(presentable))
print("length of the answer is: {0}, and sum is: {1}".format(len(presentable), sum(presentable)))
print("which is {0}".format("correct" if len(final_answer) == 11 else "incorrect"))


