# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(in_number):
    retVal = True
    back_seeker = -1
    # print("number is now: {0}".format(in_number))
    for fwd_seeker in range(0, len(str(in_number))):
        if str(in_number)[fwd_seeker] != str(in_number)[back_seeker]:
            retVal = False
        back_seeker -= 1
    return retVal

min_num = 1
max_num = 999
candidates = []

# myval = is_palindromic(92329)
# print("myval is: {0}".format(myval))
for i in range(min_num, max_num):
    for j in range(min_num, max_num):
        # print("about to multiply: {0} and {1}".format(i, j))
        temp = i * j
        if len(str(temp)) > 1 and is_palindromic(temp) and temp not in candidates:
            print("{0} is palindromic".format(temp))
            candidates.append(temp)
            break

highest = max(candidates)
print("highest palindromic number derived from 2 3-digit numbers is: {0}".format(highest))