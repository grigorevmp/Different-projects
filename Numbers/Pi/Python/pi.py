# Найти число пи до n-й цифры после запятой
# Find Pi up to the Nth digit
import math

MAX_NUMBER = 10000


def sqrt(n, limit):
    """
    n, limit -> x
    Calculate square of number (n) with limit
    """
    precision = 10 ** 16
    n_float = float((n * precision) // limit) / precision
    x = (int(precision * math.sqrt(n_float)) * limit) // precision
    n_limit = n * limit
    while True:
        x_old = x
        x = (x + n_limit // x) // 2
        if x == x_old:
            break
    return x


def Pi(limit):
    """
    limit -> pi
    Calculate PI up to the Nth digit using a Chudnovksy's series.
    """
    k = 1
    a_k = limit
    a_tot = limit
    b_tot = 0
    C = 640320
    C3_OVER_24 = C ** 3 // 24
    while True:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k ** 3 * C3_OVER_24
        a_tot += a_k
        b_tot += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409 * a_tot + 545140134 * b_tot
    pi = (426880 * sqrt(10005 * limit, limit) * limit) // total
    return pi


def inputLimit():
    """
    <input> -> digit
    Get user's limit for PI
    Check for non negative number less than MAX_NUMBER (10000 by default)
    """
    while True:
        s = input("Enter the number of decimals to calculate to: ")
        try:
            digit = int(s)
            if digit >= MAX_NUMBER:
                print(f"Enter a number smaller than {MAX_NUMBER}")
            elif digit > 0:
                return digit
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Enter a positive integer.")


def main():
    """
    Main function
    - Get user's limit
    - Calculate result
    - Print result
    """

    print("-- Find Pi up to the Nth digit --\n")

    shouldContinue = True

    while shouldContinue:

        limit = inputLimit()
        pi = str(Pi(10 ** (limit * 10)))[:limit]
        pi = pi[0] + '.' + pi[1:]

        # show 40 digits by one line

        i = 0
        for digit in pi:
            print(digit, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
