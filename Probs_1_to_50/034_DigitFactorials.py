# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math

final_set = set()

high_mark = 1000000
for i in range(high_mark):
    str_version = str(i)
    fac_total = 0
    for num in str_version:
        fac_total += math.factorial(int(num))
    if fac_total == i and i != 1 and i != 2:
        final_set.add(i)

print("final_set sum is: {0}".format(sum(final_set)))
print("final_set includes: {0}".format(final_set))
