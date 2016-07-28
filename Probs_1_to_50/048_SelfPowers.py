# Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


# just loop over numbers and raise to the appropriate power
running_total = 0
for i in range(1, 1001):
    running_total += i ** i

print("running_total is now: {0}".format(running_total))
# just cast as a string and retrieve the last 10 digits
print("final ten digits are: {0}".format(str(running_total)[-10:]))
