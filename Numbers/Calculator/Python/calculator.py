# Калькулятор
# Calculator

import math


def calc(a, b, op):
    """
    a, b, op -> result
    """

    if op not in '+-/*^':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    if op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    if op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    if op == '/':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    if op == '^':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(math.pow(a, b))


def inputData():
    """
    <input> -> a, b, op
    """

    a = 0
    b = 0
    op = '-'

    try:
        a = int(input('Type the first number: '))
        b = int(input('Type the second number: '))
        op = input(
            'What kind of operation would you like to do?\
            \nChoose between +, -, *, /, ^ : ')
    except ValueError:
        print("Enter a positive integer.")

    return a, b, op


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Calculator --\n")

    shouldContinue = True

    while shouldContinue:

        a, b, op = inputData()
        print(calc(a, b, op))

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
