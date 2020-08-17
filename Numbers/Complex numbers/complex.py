# Показать:
# - Сумму
# - Умножение
# - Сопряжение
# - Отрицание
# - Разность
# - Деление
# (могут быть сделаны путем использования нескольких уже написанных функций)

import math


class Complex:

    # i = math.sqrt(-1)

    def __int__(self, _z):
        """
        :param _z:  - other complex value
        :return: - new complex value
        """
        self.a = _z.a
        self.b = _z.b

    def __init__(self, a, b):
        """
        :param a: - imagine
        :param b: - real
        """
        self.a = a
        self.b = b

    def __str__(self):
        """
        :return: Returns complex number as a string
        """
        return "a: " + str(self.a) + " b: " + str(self.b)

    def __add__(self, other):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        return Complex(self.a - other.a, self.b - other.b)

    def __abs__(self):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        a = self.a
        b = self.b
        return math.sqrt(a ** 2 + b ** 2)

    def __neg__(self):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        return Complex(self.a, - self.b)

    def __mul__(self, other):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return Complex((a * c - b * d), (a * d + b * c))

    def __truediv__ (self, other):
        """
        :param other: - other complex value
        :return: - sum of two complex values
        """
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return Complex((a * c + b * d) / (c ** 2 + b ** 2), (b * c - a * d) / (c ** 2 + b ** 2), )


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """
    z1 = Complex(1, 2)
    z2 = Complex(2, 3)
    z = z1 / z2

    print(str(z))


if __name__ == '__main__':
    main()
