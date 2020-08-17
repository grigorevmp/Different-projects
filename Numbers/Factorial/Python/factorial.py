# Решить с помощью циклов и отдельно с помощью рекурсии.
# Solve with cycles and recursion

TOOGLE = "cycle"  # recursion


def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num - 1)


def factorial(num):
    """
    num -> result
    """
    result = 1

    if TOOGLE == "cycle":
        for i in range(num):
            result *= (i + 1)

    if TOOGLE == "recursion":
        result = recur_factorial(num)

    return result


def inputData():
    """
    <input> -> num
    """
    _num = input("Input number: ")
    num = 0

    try:
        num = int(_num)
    except ValueError:
        print("Enter a positive integer.")

    return num


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Factorial --\n")

    shouldContinue = True

    while shouldContinue:

        num = inputData()
        res = factorial(num)

        print(f"Result: {res}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
