# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
#   For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
from helpers.helper_methods import *
import re



# pulled on information about divisibility of numbers from here:
#       http://blog.dreamshire.com/project-euler-41-solution/
# basically, that if a numbers constituent digits are divisible by 3, then so is the number
# this allows manually eliminating whole classes of numbers based on the idealized pandigital number
top_num = 7654321      # largest number will be under 10 digits long (at least in base10)

max_length = 7          # found this from a little manual proofs
min_pan = 1
while not (helper_methods.is_pandigital(top_num, min_pan, max_length) and helper_methods.is_prime(top_num)):
    top_num -= 2

print("answer is: {0}".format(top_num))
