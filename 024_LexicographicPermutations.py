# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
#   1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
#   The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools


big_set_len = 10

def all_permutations(inList):
    retval = []
    retval = [''.join(x) for x in itertools.permutations(inList, len(inList))]
    retval.sort()
    return retval

def make_list(in_number):
    retval = []
    for i in range(in_number):
        retval.append(str(i))
    return retval

my_list = make_list(big_set_len)
print("my_list is now: {0}".format(my_list))
my_permutations = all_permutations(my_list)
print("my_permutations is now: {0}".format(my_permutations))

print("the one millionth permutation for set [0-9] is: {0}".format(my_permutations[999999]))
