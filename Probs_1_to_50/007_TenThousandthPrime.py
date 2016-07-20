# Problem 7
# Published on Friday, 28th December 2001, 06:00 pm; Solved by 268132; Difficulty rating: 5%
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime(test_number):
    retval = True
    if test_number > 1:
        divisor = 2
        while divisor <= (test_number / 2):
            if test_number % divisor == 0:
                retval = False
                break
            divisor += 1
    return retval

prime_holder = []
i = 1
while True:  # can step by 2 since even numbers are all divisible by 2
    myprime = is_prime(i)
    if myprime:
        prime_holder.append(i)
        print("myprime is: {0}, for {1}".format(myprime, i))
        print("length of prime_holder is: {0}".format(str(len(prime_holder))))
    if len(prime_holder) == 10001 and myprime:
        print("10,001st prime number is: {0}".format(i))
        break
    i += 2