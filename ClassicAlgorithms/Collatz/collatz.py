# Гипотеза Коллатца
# Collatz

def collatz(num):
    """
    num -> steps
    """
    steps = 0

    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        steps += 1

    return steps


def inputNum():
    """
    <input> -> number
    """
    while True:
        s = input("Enter the number: ")
        try:
            number = int(s)
            return number
        except ValueError:
            print("Enter an integer.")
            return 1


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Collatz --\n")

    shouldContinue = True

    while shouldContinue:

        num = inputNum()
        steps = collatz(num)
        print(steps)

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
