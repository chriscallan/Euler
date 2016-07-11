

def prime_factors(in_number):
    retVal = []
    if in_number < 2:
        raise  ValueError("There are no factors for that which you can't figure out on your own.")
    divisor = 2
    print("divisor is: {0}".format(divisor))
    while in_number > 1:
        if not in_number % divisor:
            print("inside the if-not")
            if divisor not in retVal:
                retVal.append(divisor)
            in_number /= divisor
            print("in_number is now: {0}".format(in_number))
            divisor -= 1
            print("divisor was decremented to: {0}".format(divisor))
        divisor += 1
        print("divisor was incremented to: {0}".format(divisor))
    print("about to return: {0}".format(retVal))
    return retVal
    # retVal = []
    # potential = 2
    # while in_number > 1:
    #     while in_number % potential == 0:
    #         retVal.append(potential)
    #         in_number /= potential
    #     potential += 1
    #     if potential ** 2 > in_number:
    #         if in_number > 1:
    #             retVal.append(in_number)
    #         break
    # return  retVal

# def gen_prime_numbers(max=300000000000)
#     retVal = []
#     for

primes = prime_factors(600851475143)
print("primes are: {0}".format(primes))
