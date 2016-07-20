# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
#   order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
from itertools import permutations


max_idx = 10
prime_divisors = [2, 3, 5, 7, 11, 13, 17]
all_permutations = permutations(range(max_idx), max_idx)

divi_list = []
for perm in all_permutations:
    # do some quick checks first so that entries that can be disqualified with simple tests are caught
    if perm[0] != 0:        # don't worry about permutations that start with '0'
        if int(perm[3]) in [0, 2, 4, 6, 8]:  # make sure the first candidate is cursorily divisible by '2'
            if (int((perm[2] + perm[3] + perm[4])) / 3).is_integer():    # simple check to see if the division was 'simple'
                if int(perm[5]) in [0, 5]:
                    # now that the simple cases are eliminated, go ahead and run the full tests on the candidates
                    for i in range(1, max_idx - 2):     # be aware that we need to stop at len() - 3 becuase of our substring size
                        temp_val = int("".join(map(str, perm[i:i+3])))
                        prime = prime_divisors[i - 1]
                        if (temp_val // prime) * prime == temp_val:
                            if i == len(prime_divisors):
                                print("adding: {0} to the answer list".format(perm))
                                divi_list.append(perm)
                        else:
                            break
# now turn the list objects filtered from the original permutations object into integer values
num_list = []
for num in divi_list:
    num_list.append(int("".join(map(str, num))))

# and finally some friendly output to present the answer that the script found
print("num_list is: {0}".format(num_list))
print("sum of all substring divisibles is: {0}".format(str(sum(num_list))))
