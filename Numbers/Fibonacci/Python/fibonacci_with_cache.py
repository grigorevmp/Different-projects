# Введите число, и программа сгенерирует N членов последовательности Фибоначчи.
# Enter a number and the program will generate N members a Fibonacci series.

MAX_NUMBER = 10000

import collections.abc
import functools


def memoize(function):
    cache = {}

    @functools.wraps(function)
    def wrap(*args, **kwargs):
        if not isinstance(args, collections.abc.Hashable):
            return function(*args, **kwargs)
        if args in cache:
            return cache[args]
        value = function(*args, **kwargs)
        cache[args] = value
        return value

    return wrap


@memoize
def fibonacci(n):
    """
    Returns the n'th Fibonacci number where n is an integer >= 0
    :param n: integer >= 0
    :return: n'th Fibonacci number
    """
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def inputNum():
    """
    <input> -> number
    How many numbers of Fibonacci series you want to see
    Check for non negative number less than MAX_NUMBER (10000 by default)
    """
    while True:
        s = input("Enter the number of Fibonacci number: ")
        try:
            number = int(s)
            if number >= MAX_NUMBER:
                print(f"Enter a number smaller than {MAX_NUMBER}")
            elif number > 0:
                return number
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Enter a positive integer.")


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Fibonacci series --\n")

    shouldContinue = True

    while shouldContinue:

        num = inputNum()
        fibSeq = fibonacci(num)
        print(fibSeq)

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
