# Problem 45
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.
from helpers.helper_methods import *


# set these two up as set() objects for quick lookup
# and creating these is very quick with the function-based generation
pent_set = set(helper_methods.get_pentagonal_number(x) for x in range(2, 500000))
hex_set = set(helper_methods.get_hexagonal_number(x) for x in range(2, 500000))
counter = 285   # provided as the first number, we are tasked with finding the "next" number
trip_switch = True

while trip_switch:
    counter += 1
    candidate = helper_methods.get_triangle_number(counter)
    if candidate in pent_set and candidate in hex_set:
        trip_switch = False
        print("answer is: {0}".format(candidate))
        break
