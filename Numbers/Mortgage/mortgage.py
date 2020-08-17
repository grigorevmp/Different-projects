# Вычислить месячные выплаты фиксированного срока в течение заданных N сроков с заданной процентной ставкой.
# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.

import math


def monthlyPayments(p, apr, y):
    """
    num -> prime factors
    """

    # get month number
    n = math.ceil(y * 12)
    # monthly payments
    monthly = apr / 12
    monthlyPay = p * (monthly / 100 * math.pow(1 + monthly/100, n)) / (math.pow(1 + monthly/100, n) - 1)

    return monthlyPay


def inputData():
    """
    <input> -> p, apr, y
    """
    _p = input("Enter the principal owed ($): ")
    p = 0

    try:
        p = int(_p)
    except ValueError:
        print("Enter a positive integer.")

    _apr = input("Enter the mortgage rate or APR (%): ")
    apr = 0

    try:
        apr = int(_apr)
    except ValueError:
        print("Enter a positive integer.")

    _y = input("Enter the length of the mortgage (years): ")
    y = 0

    try:
        y = int(_y)
    except ValueError:
        print("Enter a positive integer.")

    return p, apr, y


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Mortgage calculator --\n")

    shouldContinue = True

    while shouldContinue:

        p, apr, y = inputData()
        monthlyPayment = monthlyPayments(p, apr, y)

        print(f"Monthly mortgage payment for {p}")
        print(f"at an APR of {apr} over {y} years:")
        print(f"{monthlyPayment}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
