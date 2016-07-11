# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?


working_value = 2 ** 1000
running_total = 0

for i in range(len(str(working_value))):
    running_total += int(str(working_value)[i])

print("running_total is: {0}".format(running_total))
