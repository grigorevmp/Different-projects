# Калькулятор
# Calculator

import math

class Calculator():

    def __init__(self):
        self.op = 0
        self.b = 0
        self.op = ''
        self.op_list = '+-/*^'

    def run(self):
        """
        a, b, op -> result
        """

        if self.op not in '+-/*^':
            return 'Please only type one of these characters: "+, -, *, /"!'

        if self.op == '+':
            return str(self.a) + ' ' + self.op + ' ' + str(self.b) + ' = ' + str(self.a + self.b)
        if self.op == '-':
            return str(self.a) + ' ' + self.op + ' ' + str(self.b) + ' = ' + str(self.a - self.b)
        if self.op == '*':
            return str(self.a) + ' ' + self.op + ' ' + str(self.b) + ' = ' + str(self.a * self.b)
        if self.op == '/':
            return str(self.a) + ' ' + self.op + ' ' + str(self.b) + ' = ' + str(self.a / self.b)
        if self.op == '^':
            return str(self.a) + ' ' + self.op + ' ' + str(self.b) + ' = ' + str(math.pow(self.a, self.b))

    def inputData(self):
        """
        <str> -> a, op, b
        """
        try:
            data = input('Type the expression, like "12 + 4" (dont forget spaces!): ')
            data_arr = data.split()
            self.a = int(data_arr[0])
            self.op = data_arr[1]
            self.b = int(data_arr[2])

        except ValueError:
            print("Enter a positive integer.")


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Calculator --\n")

    shouldContinue = True

    calc = Calculator()

    while shouldContinue:

        calc.inputData()
        print(calc.run())

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
