# #
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000



final_string = ""       # use this to store the working number
max_size = 200000       # we can stop here because out string will be the right size after this many loops
string_size = 1000000
digit_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
for i in range(max_size + 1):
    final_string += str(i)
    if len(final_string) >= string_size + 1:        # need to account for zero-indexing
        print("full string is: {0}".format(final_string))
        print("found {0} to be our string".format(final_string))
        break

final_answer = 1        # can't initialize with '0' or out product is always zero
for digit in digit_list:
    final_answer *= int(final_string[digit])

print("final product is: {0}".format(final_answer))

