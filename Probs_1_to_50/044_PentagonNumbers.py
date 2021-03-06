# Problem 44
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj|
#   is minimised; what is the value of D?
from math import sqrt,fabs


max_limit = 5000   # keep this minimal since larger numbers will increase their "pentagonal distance"
difference = 1     # set a default value that will be replaced later (aka. "our answer is definitely bigger than this")

def get_pent_number(in_number):
    """
    simple helper method to return the pentagonal number, given the index to calculate for
    :param in_number: the index of the pentagonal number you'd like the pentagonal number for
    :return: integer that is the pentagonal number located at the provided index
    """
    return (in_number * (3 * in_number - 1)) // 2

def is_pentagonal(in_number):
    """
    Utility method to hold the inverse of the pentagonal number function
    :param in_number: the number to check for pentagonal'ness
    :return: bool indicating if it passed the check, or not
    """
    return (sqrt(1 + 24 * in_number) + 1 / 6).is_integer()

# solution is adapted from the solution found here:
#       https://alphacentauri32.wordpress.com/2011/05/05/project-euler-problem-44-solved-with-python/
pent_set = set(get_pent_number(n) for n in range(2, max_limit))     # sets provide lightning quick lookups
for outer_pent in pent_set:
    for inner_pent in pent_set:
        if (outer_pent + inner_pent) in pent_set and (inner_pent - outer_pent) in pent_set:
            difference = fabs(outer_pent - inner_pent)
        else:
            continue

print("answer is: {0}".format(difference))
