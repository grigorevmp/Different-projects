# Разложение на произведение простых чисел и их показатель
# Prime Factorization


def factorize(num):
    """
    num -> prime factors
    """

    factor = 2
    prime_factors = ""
    factors = []
    exp = []

    while num != 1:
        if num % factor == 0:
            if factors and factors[len(factors) - 1] != factor or len(factors) == 0:
                factors.append(factor)
                exp.append(1)
            else:
                exp[len(exp) - 1] += 1
            num /= factor
        else:
            factor += 1

    i = 0
    for f, e in zip(factors, exp):
        if i > 0:
            prime_factors += ", "
        i += 1
        prime_factors += str(f) + "^" + str(e)

    return prime_factors


def inputNum():
    """
    <input> -> number
    """
    s = input("Enter the number to get it's prime factors: ")
    number = int(s)
    return number


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    num = inputNum()
    factors = factorize(num)
    print(factors)


if __name__ == '__main__':
    main()
