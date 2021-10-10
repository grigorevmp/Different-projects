# Напишите программу, которая симулирует подбрасывание одной монеты столько раз, сколько захочет пользователь.
# Программа должна записывать результаты и подсчитывать сколько раз выпали орел и решка.

# heads and tails

import random


class Coin:

    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.current = None

    def flip(self):
        """
        . -> result
        """
        if random.random() >= .5:
            self.current = "head"
            self.heads += 1
        else:
            self.current = "tail"
            self.tails += 1
        return self.current

    def get_stats(self):
        return self.heads, self.tails, self.current


def main():
        """
        Main function
        - Get user's number
        - Calculate result
        - Print result
        """

        print("-- Coin flip --\n")

        shouldContinue = True
        coin = Coin()
        heads = 0
        tails = 0

        while shouldContinue:

            print(coin.flip())

            should = input("\nJump again (Y/[N]): ")
            if should.upper() != 'Y':
                heads, tails, current = coin.get_stats()
                print()
                print(f"Heads: {heads}")
                print(f"Tails: {tails}")
                shouldContinue = False
            else:
                shouldContinue = True


if __name__ == '__main__':
    main()
