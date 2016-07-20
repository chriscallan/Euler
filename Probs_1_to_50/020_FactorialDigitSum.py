# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

from math import factorial

my_val = str(factorial(100))
running_total = 0
for i in my_val:
    running_total += int(i)

print("the final value is: {0}".format(running_total))
