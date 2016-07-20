# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
#   2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
#   recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

upper_limit = 1000
max_length = 0
max_n = 0
candidate_number = 2
while candidate_number < upper_limit:
    dividend = 1
    divisor = candidate_number
    quotient = "."
    divisor_list = ()
    divisor_list = divisor_list + (dividend,)
    while True:
        if 0 < dividend < divisor:
            dividend *= 10
            while dividend < divisor:
                dividend *= 10
                quotient += "0"
        if dividend not in divisor_list:
            divisor_list += (dividend,)
        else:
            break
        temp = dividend
        dividend = (dividend - int((dividend/divisor))*divisor)
        quotient += str(int(temp/divisor))
    if max_length <= len(quotient):
        max_length = len(quotient)
        max_n = candidate_number
        candidate_quotient = quotient
    candidate_number += 1
print("Max Length={0} for Decimal Expansion of 1/{1}={2}".format(max_length, max_n, candidate_quotient))



# max_num = 1000
# candidate = {}
# for i in range(2, max_num):
#     result = 1 / i
#     candidate[i] = result
#
# winning_number = 0
# win_count = 0
# winning_pair = {}
# for entry_key in candidate.keys():
#     print("entry_key is: {0}".format(entry_key))
#     div_result = str(candidate[entry_key]).split(".")[1]
#     print("div_result is: {0}".format(div_result))
#     for i in range(1, len(str(div_result))):
#         print("found: {0} has substring: {1}".format(div_result, str(div_result)[:i]))
#         if str(div_result).count(str(div_result)[:i]) > win_count:
#             winning_number = entry_key
#             win_count = i
#             winning_pair[i] = str(div_result)[:i]

#
# print("win_count is: {0} and winning_pair is: {1}".format(win_count, str(winning_pair)))
# print("number with the largest reciprocal count is: {0}".format(winning_number))
