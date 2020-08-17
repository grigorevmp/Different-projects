# Пользователь вводит стоимость и количество денег.
# Программа рассчитывает сдачу и количество мелких монет, необходимых для сдачи
# The user enters a cost and then the amount of money given. The program will
# figure out the change and the number of quarters, dimes, nickels, pennies
# needed for the change.

import math


def moneyChange(diff):

    hundreds = math.floor(diff / 100)
    leftover = diff - hundreds * 100
    fifties = math.floor(leftover / 50)
    leftover -= fifties * 50
    twenties = math.floor(leftover / 20)
    leftover -= twenties * 20
    tens = math.floor(leftover / 10)
    leftover -= tens * 10
    fives = math.floor(leftover / 5)
    leftover -= fives * 5
    ones = math.floor(leftover)
    leftover -= ones

    leftover *= 100
    quarters = math.floor(leftover / 25)
    leftover -= quarters * 25
    dimes = math.floor(leftover / 10)
    leftover -= dimes * 10
    nickels = math.floor(leftover / 5)
    leftover -= nickels * 5
    pennies = math.floor(leftover + 0.5)

    print("Change due:")
    if hundreds > 0:
        print("$100 bills:", hundreds)

    if fifties > 0:
        print("$50 bills: ", fifties)

    if twenties > 0:
        print("$20 bills: ", twenties)

    if tens > 0:
        print("$10 bills: ", tens)

    if fives > 0:
        print("$5 bills:  ", fives)

    if ones > 0:
        print("$1 bills:  ", ones)

    if quarters > 0:
        print("Quarters:  ", quarters)

    if dimes > 0:
        print("Dimes:     ", dimes)

    if nickels > 0:
        print("Nickels:   ", nickels)

    if pennies > 0:
        print("Pennies:   ", pennies)


def inputNum():
    """
    <input> -> cost, amount
    """
    _cost = input("Enter cost: ")
    cost = 0

    try:
        cost = int(_cost)
    except ValueError:
        print("Enter a positive integer.")

    _amount = input("Enter amount: ")
    amount = 0

    try:
        amount = int(_amount)
    except ValueError:
        print("Enter a positive integer.")

    return cost, amount


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Money changing --\n")

    shouldContinue = True

    while shouldContinue:

        cost, amount = inputNum()
        diff = amount - cost

        if cost > amount:
            print("Not enough money =(")
        else:
            moneyChange(diff)

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
