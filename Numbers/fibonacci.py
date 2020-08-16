# Введите число, и программа сгенерирует N членов последовательности Фибоначчи.
# Enter a number and the program will generate N members a Fibonacci series.

MAX_NUMBER = 10000


def fibonacci(N):
    """
    N -> fibonacci series
    """
    series = [1]

    while len(series) < N:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):
        series[i] = str(series[i])

    return ', '.join(series)


def inputNum():
    """
    <input> -> number
    How many numbers of Fibonacci series you want to see
    Check for non negative number less than MAX_NUMBER (10000 by default)
    """
    while True:
        s = input("Enter the number of Fibonacci sequence members: ")
        try:
            number = int(s)
            if number >= MAX_NUMBER:
                print(f"Enter a number smaller than {MAX_NUMBER}")
            elif number > 0:
                return number
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Enter a positive integer.")


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    num = inputNum()
    fibSeq = fibonacci(num)
    print(fibSeq)


if __name__ == '__main__':
    main()
