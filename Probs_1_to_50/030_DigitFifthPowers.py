# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

stopping_point = 10000000
achievers = set()

for i in range(2, stopping_point):
    temp_str = str(i)
    temp_total = 0
    for number in temp_str:
        temp_total += int(number) ** 5
    if temp_total == i:
        achievers.add(i)

print("the list of 'achievers' below limit: {0} is: {1}".format(stopping_point, achievers))
print("and their sum is: {0}".format(sum(achievers)))