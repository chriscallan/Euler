# Problem 36
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def is_palindromic(in_number):
    retVal = True
    back_seeker = -1
    # print("number is now: {0}".format(in_number))
    for fwd_seeker in range(0, len(str(in_number).strip('0'))):
        if str(in_number)[fwd_seeker] != str(in_number)[back_seeker]:
            retVal = False
        back_seeker -= 1
    return retVal


final_answer = set()
max_limit = 1000000
for i in range(max_limit):
    if is_palindromic(i):
        bin_repr = bin(i)[2:]
        if is_palindromic(bin_repr):
            print("found one: {0}".format(i))
            final_answer.add(i)

print("final_answer is: {0}".format(final_answer))
print("answer to the question is: {0}".format(sum(final_answer)))
