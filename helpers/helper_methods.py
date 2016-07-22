import re
from math import sqrt, ceil


class helper_methods(object):
    @staticmethod
    def is_prime(test_number):
        """
        Simple helper to determine if a given nubmer is prime
        :param test_number: the number to be tested
        :return: True if the given number is prime, False if it isn't
        """
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

    @staticmethod
    def generate_prime_list(in_number):
        """
        Helper method to generate a list of prime numbers
            Pulled from: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/2073279
            This implementation was one of the faster implementations, with or without JIT-compilation
            I've modified it to include more explicit execution hints, by way of parentheses, exponents,
                native functions, etc...
        :param in_number: upper limit for the list of primes (aka. all_primes[] <= in_number)
        :return: a list object populated with prime numbers from 2 through 'in_number'
        """
        sieve = [True] * in_number
        for i in range(3, ceil(sqrt(in_number)), 2):
            if sieve[i]:
                # work through the sieve with a stride of 2*i
                sieve[i ** 2::2 * i] = [False] * (((in_number - (i ** 2) - 1) // (2 * i)) + 1)
        return [2] + [i for i in range(3, in_number, 2) if sieve[i]]

    @staticmethod
    def is_pandigital(in_number, lowest_digit=1, length=9):
        """
        Helper method to determine if the provided value is a "pandigital" number
            E.g. - "987654321" is 1-9 pangital, and 876543213 is not
        :param in_number: the number you want to check for "pandigitalness"
        :param lowest_digit: the lowest digit that should be included in your pangigital set
            usually '1' is the lowest values to search for, but other digits can be used ('0' is the next most common)
        :param length: the length of the pandigital set
            usually '9' is the length of the set, but lower values could be used also
        :return: bool indicating if the provided number fit the pandigital rules and any additional constraints
        """
        if 0 < length >= 9:
            raise Exception("length parameter: {0} was incorrect.".format(length))
        re_checker = re.compile("^(?!.*([{0}-{1}]).*\\1)[{0}-{1}]{{{0}}}$".format(lowest_digit, length))
        return True if len(re_checker.findall(str(in_number))) is not 0 else False

    @staticmethod
    def get_triangle_number(in_number):
        """
        Helper method to encapsulate the formula that produces 'triangle' numbers
        :param in_number: number indicating the 'triangle number' index you'd like the value for
        :return: the 'triangle number' produced by the equation
        """
        return in_number * (in_number + 1) // 2

    @staticmethod
    def get_pentagonal_number(in_number):
        """
        Helper method to encapsulate the formula that produces 'pentagonal numbers'
        :param in_number: number indicating the 'pentagonal number' index you'd like the value for
        :return: the 'pentagonal number' produced by the equation
        """
        return (in_number * (3 * in_number - 1)) // 2

    @staticmethod
    def get_hexagonal_number(in_number):
        """
        Helper method to encapsulate the formula that produces 'hexagonal numbers'
        :param in_number: number indicating the 'hexagonal number' index you'd like the value for
        :return: the 'hexagonal number' produced by the equation
        """
        return in_number * (2 * in_number - 1)
