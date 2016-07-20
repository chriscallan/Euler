# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?



def get_my_fib(in_number, _cache={}):
    if in_number in _cache:
        return _cache[in_number]
    elif in_number > 1:
        return _cache.setdefault(in_number, get_my_fib(in_number - 1) + get_my_fib(in_number - 2))
    return in_number

# this is just a unit test to make sure I get the solution that I expect when using known values
# my_solution = get_my_fib(12)
# print("my_solution is: {0}".format(my_solution))

semaphore = True
fib_candidate = 1
while semaphore:
    if fib_candidate % 15 == 0:
        print("currently checking: {0}".format(fib_candidate))
    if (len(str(get_my_fib(fib_candidate)))) == 1000:
        semaphore = False
    else:
        fib_candidate += 1

print("found: {0} as the fibonacci number with 1000 digits.".format(fib_candidate))