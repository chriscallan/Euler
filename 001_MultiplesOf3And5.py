# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

divisors = (3, 5)
runningtotal = 0
lowerlimit = 1
upperlimit = 1000

for i in range(lowerlimit, upperlimit):
    for j in divisors:
        if i % j == 0:
            runningtotal += i
            break

print("total count is: {0}".format(runningtotal))