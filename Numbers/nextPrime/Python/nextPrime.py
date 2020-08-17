# Программа находит простые числа до тех пор, пока пользователь перестанет спрашивать.
# Generate prime numbers until the user chooses to stop


def isPrime(number):
    """
    number -> [bool] is prime ?
    """

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def genPrime(currentPrime):
    """
    currentPrime -> newPrime
    """

    newPrime = currentPrime + 1

    while True:

        if not isPrime(newPrime):
            newPrime += 1
        else:
            break

    return newPrime


def inputAnswer():
    """
    <input> -> number
    """
    s = input("Would you like to see the next prime? (Y/[N])")
    return s


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Next Prime Number --\n")

    currentPrime = 2

    while True:

        answer = inputAnswer()
        if answer.lower().startswith('y'):
            print(currentPrime)
            currentPrime = genPrime(currentPrime)
        else:
            break


if __name__ == '__main__':
    main()
