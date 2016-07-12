# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
#       resolutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?



def find_pyth_set(in_perimeter):
    retval = []
    # found the mathematical proof here
    #   codereview.stackexchange.com/questions/49413/project-euler-39-integer-right-triangles
    for a in range(3, (in_perimeter // 2) - 1):
        c = ((a ** 2) + ((in_perimeter - a) ** 2)) // (2 * (in_perimeter - a))
        b = ((c ** 2) - (a ** 2)) ** 0.5
        # make sure the square root is an integer/whole number
        if b.is_integer() and (a + b + c) == in_perimeter:
            retval.append((a, int(b), c, ))
    return retval
# this holds the potential candidate values to answer the question
final_answer = {'perimeter': 0, 'count': 0, 'set': []}
for perimeter in range(1000):
    working_set = find_pyth_set(perimeter)
    if len(working_set) > final_answer['count']:
        final_answer['perimeter'] = perimeter
        final_answer['count'] = len(working_set)
        final_answer['set'] = working_set

print("final_answer: {0} count is: {1} and the set is: {2}".format(str(final_answer['perimeter']),
                                                                   str(final_answer['count']), final_answer['set']))

