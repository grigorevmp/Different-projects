# Сфера эратосфена
# Sieve of Eratosthenes

def sieve(num):
    """
    num -> steps
    """

    is_prime = [False] * 2 + [True] * (num - 1)
    for i in range(int(num ** 0.5 + 1.5)):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


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

    print("-- Fibonacci series --\n")

    shouldContinue = True

    while shouldContinue:

        num = inputNum()
        nums = sieve(num)
        print(nums)

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
