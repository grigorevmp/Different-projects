# Напишите программу, которая симулирует подбрасывание одной монеты столько раз, сколько захочет пользователь.
# Программа должна записывать результаты и подсчитывать сколько раз выпали орел и решка.

# heads and tails

import random


def jump():
    """
    . -> result
    """
    flip = random.random()
    if flip >= .5:
        return "head"
    else:
        return "tail"


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Coin flip --\n")

    shouldContinue = True

    heads = 0
    tails = 0

    while shouldContinue:

        j = jump()

        if j == "head":
            heads += 1
        elif j == "tail":
            tails += 1

        print(j)

        should = input("\nJump again (Y/[N]): ")
        if should.upper() != 'Y':
            print()
            print(f"Heads: {heads}")
            print(f"Tails: {tails}")
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
