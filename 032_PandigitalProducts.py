# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
#   the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
#   1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
#   1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import re

pandigitals = set()
# pre-compiled to help with performance
re_checker = re.compile("^(?!.*([1-9]).*\\1)[1-9]{9}$")

for x in range(10000):
    for y in range(10000):
        product = x * y
        str_version = "{0}{1}{2}".format(str(product), str(x), str(y))
        if len(str_version) > 9:
            break
        if re_checker.match(str_version) is not None:
            print("multiplicand: {0}, multiplier: {1}, product: {2}".format(x, y, product))
            pandigitals.add(product)

print("sum of all: {0}".format(sum(pandigitals)))
