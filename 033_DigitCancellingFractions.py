# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
#   incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
#   digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import sys


result_set = []
for i in range(10, 100):
    for j in range(10, 100):
        if (i % 10 == 0 and j % 10 == 0) or i >= j:     # skip the trivial examples
            continue
        result = i / j
        for i_num in str(i):
            if str(j).__contains__(i_num):
                try:
                    if int(str(i).replace(i_num, "", 1)) == 0 or int(str(j).replace(i_num, "", 1)) == 0:
                        continue
                    second_result = int(str(i).replace(i_num, "", 1)) / int(str(j).replace(i_num, "", 1))
                except Exception as exc:
                    print("Exception: {0}".format(sys.exc_info()))
                if result == second_result:
                    print("Found that: {0} / {1} fits the criteria".format(i, j))
                    result_set += [(i, j)]
print("result_set is: {0}".format(result_set))
final_result = 1    # so as not to create an only-zero final_result
final_top = 1
final_bottom = 1
for top, bottom in result_set:
    # final_result *= result
    final_top *= top
    final_bottom *= bottom
print("final_top is: {0}, final_bottom is: {1}".format(final_top, final_bottom))
print("final_result is: {0}".format(final_result))

