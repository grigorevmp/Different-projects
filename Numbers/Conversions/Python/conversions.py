# Перевод из двоичной системы в десятичную и обратно
# Bin To Dec and back

import math


def BinToDec(num):
    """
    num -> result
    """
    n = 1
    result = 0
    for i in str(num)[::-1]:
        if i == '1': result += n
        n <<= 1

    return result


def DecToBin(num):
    """
    num -> result
    """
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num = num // 2

    return result


def inputData():
    """
    <input> -> function, num
    """
    _function = input("Choose (Bin -> Dec), (Dec -> Bin) (0,[1]) ")
    function = 0

    try:
        function = int(_function)
    except ValueError:
        print("Enter a positive integer.")

    if function != 0:
        function = 1

    _num = input("Enter num: ")
    num = 0

    try:
        num = int(_num)
    except ValueError:
        print("Enter a positive integer.")

    return function, num


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Conversions --\n")

    shouldContinue = True

    funcs = [BinToDec, DecToBin]

    while shouldContinue:

        function, num = inputData()
        res = funcs[function](num)

        print(f"Result: {res}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
