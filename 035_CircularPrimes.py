# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
#   are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?


def is_prime(test_number):
    retval = True
    try:
        if test_number > 1:
            divisor = 2
            while divisor <= (test_number / 2):
                if test_number % divisor == 0:
                    retval = False
                    break
                divisor += 1
    except Exception as exc:
        print("Exception")
    return retval


def circulate_number(innumber):
    retval = [innumber]
    for i in range(len(str(innumber))):
        new_number = str(innumber)[1 + i:] + str(innumber)[:(0 + i) + 1]
        if int(new_number) not in retval:
            retval.append(int(new_number))
    return retval


def contains_even_number(innumber):
    retval = False
    evens = (2, 4, 5, 6, 8, 0, )
    for number in str(innumber):
        if int(number) in evens:
            retval = True
            break
    return retval
#
max_limit = 1000000
# primes = set()
# primes.add(2)   # this is the only even prime
# count = 0
# for i in range(1, max_limit, 2):
#     count += 1
#     if count % 1000 == 0:
#         print("working on {0}".format(i))
#     if is_prime(i):
#         primes.add(i)

final_answer = set()
final_answer.add(2)     # tack this in as it is the only even prime number
final_answer.add(5)     # this is another special-case prime

for i in range(3, max_limit, 2):    # allows us to step over even numbers, no need to check them
    if i not in final_answer and not contains_even_number(i) and is_prime(i):
        test = circulate_number(i)
        all_good = True
        # print("came up with these circulations: {0}".format(test))
        for entry in test:
            if not is_prime(int(entry)):
                all_good = False
                break
        if all_good:
            for entry in test:
                print("adding: {0}".format(entry))
                final_answer.add(int(entry))
#
# # put things back together
# # for my_entry in final_answer:
final_answer = list(final_answer)
final_answer.sort()
print("final_answer is: {0}".format(final_answer))
print("and the answer to the question is: {0}".format(len(final_answer)))

# def primes(max_n):
#     numbers = list(range(3, max_n+1, 2))
#     half = max_n // 2
#     initial = 4
#     for step in range(3, max_n+1, 2):
#         for i in range(initial, half, step):
#             numbers[i - 1] = 0
#         initial += 2 * (step + 1)
#
#         if initial > half:
#             return [2] + list(filter(None, numbers))
#
#
# def rotate(S_list):
#     S=[]
#     for i in range(len(S_list)):
#         S.append(int(S_list[i:] + S_list[:i]))
#     return set(S)
#
# def circularPrime(limit):
#     all_primes_in_limit = primes(limit)
#     circular_prime = []
#     reject_list = ['0', '2', '4', '5', '6', '8']
#     all_primes_in_limit=[i for i in all_primes_in_limit if not any(j in reject_list for j in set(str(i)))]
#     while all_primes_in_limit:
#         shuffleset = rotate(str(all_primes_in_limit[-1]))
#         primeset = set(all_primes_in_limit)
#         if not shuffleset - primeset:
#             circular_prime += list(shuffleset)
#         all_primes_in_limit = list(primeset-shuffleset)
#     circular_prime.sort()
#     return circular_prime
#
#
# #for limit value 1000000
# my_val = circularPrime(1000000)
# print("full set of answers is: {0}".format(my_val))
# print("answer to the question is: {0}".format(len(my_val)))
