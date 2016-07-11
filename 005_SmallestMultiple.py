# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

min_divisor = 1
max_divisor = 20


def is_candidate(test_number):
    retval = True
    for i in range(min_divisor, max_divisor + 1):
        if test_number % i:
            retval = False
            break
    return retval

# val = is_candidate(2520)
# print("val is: {0}".format(val))
# for i in range(20, 400000000, 2):
prospect = 2520    # this is the number for 1 - 10, so our number must be larger than that one
while True:
    if is_candidate(prospect):
        print("smallest multiple is: {0}".format(prospect))
        break
    else:
        if not prospect % 12000:
            print("checking {0} now".format(prospect))
        prospect += 2  # candidate number must be even since '2' is in the list of divisors