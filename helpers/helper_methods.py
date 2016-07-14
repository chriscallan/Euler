import re


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
    def is_pandigital(in_number, length=9):
        re_checker = re.compile("^(?!.*([1-{0}]).*\\1)[1-{0}]{{{0}}}$".format(length))
        return True if len(re_checker.findall(str(in_number))) is not 0 else False


