class Converter:
    _dists = {'mtml': lambda metre: metre * 0.00062,
             'mlmt': lambda mile: mile * 1601,
             'mti': lambda metre: metre * 39.37,
             'imt': lambda inch: inch * 0.0254,
             'iy': lambda inch: inch * 0.0278,
             'yi': lambda yard: yard * 36,
             'mty': lambda metre: metre * 1.09361,
             'ymt': lambda yard: yard * 0.9144,
             'mly': lambda mile: mile * 1760,
             'yml': lambda yard: yard * 0.000568182,
             'mli': lambda mile: mile * 63360,
             'iml': lambda inch: inch * 1.57828e-5,
             'mtf': lambda metre: metre * 3.28084,
             'mlf': lambda mile: mile * 5280,
             'if': lambda inch: inch * 0.0833333,
             'yf': lambda yard: yard * 3,
             'fmt': lambda feet: feet * 0.3048,
             'fml': lambda feet: feet * 0.000189394,
             'fi': lambda feet: feet * 12,
             'fy': lambda feet: feet * 0.333333
             }

    _temps = {'cf': lambda c: c * (9 / 5) + 32,
              'fc': lambda f: (f - 32) * (5 / 9),
              'ck': lambda c: c + 273.15,
              'kc': lambda k: k - 273.15,
              'fk': lambda f: (f + 459.67) * 5 / 9,
              'kf': lambda k: k * (9 / 5) - 459.67
              }

    _weights = {'pkg': lambda p: p * 0.453592,
                'kgp': lambda kg: kg * 2.20462,
              }

    def baseConverterDialog(self):
        try:
            _num = int(input("Input number: "))
            _to = int(input("Convert to: "))
            _from = int(input("Convert from: "))
            print("Result: ", self.baseConvert(_num, _to, _from))
        except ValueError:
            print("Wrong data")

    def baseConvert(self, num, toBase=10, fromBase=10):

        if isinstance(num, str):
            n = int(num, fromBase)
        else:
            n = int(num)

        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < toBase:
            return alphabet[n]
        else:
            return self.baseConvert(n // toBase, toBase) + alphabet[n % toBase]

    def tempConverterDialog(self):
        try:
            print("Please use: 'f' for fahrenheit, 'k' for kelvin, 'c' for celsius")
            _temp = int(input("Input temperature: "))
            _to = input("Convert to: ")
            _from = input("Convert from: ")
            print(f"Result: {self.tempConverter(_from.lower()[0], _to.lower()[0], _temp)}{_to}")
        except ValueError:
            print("Wrong data")

    def tempConverter(self, msr_from, msr_to, temp):
        try:
            return self._temps[msr_from[0] + msr_to[0]](temp)
        except KeyError:
            return f"Cannot convert from {msr_from} to {msr_to}"

    def distanceConverterDialog(self):
        try:
            print("Please use: 'mt' for metre, 'ml' for miles, 'i' for inches, 'y' for yards, 'f' for feet")
            _temp = int(input("Input distance: "))
            _to = input("Convert to: ")
            _from = input("Convert from: ")
            print(f"Result: {self.distanceConverter(_from.lower()[0], _to.lower()[0], _temp)}{_to}")
        except ValueError:
            print("Wrong data")

    def distanceConverter(self, msr_from, msr_to, temp):
        try:
            return self._dists[msr_from[0] + msr_to[0]](temp)
        except KeyError:
            return f"Cannot convert from {msr_from} to {msr_to}"

    def weightConverterDialog(self):
        try:
            print("Please use: 'p' for pounds, 'kg' for kilograms")
            _temp = int(input("Input weight: "))
            _to = input("Convert to: ")
            _from = input("Convert from: ")
            print(f"Result: {self.weightConverter(_from.lower()[0], _to.lower()[0], _temp)}{_to}")
        except ValueError:
            print("Wrong data")

    def weightConverter(self, msr_from, msr_to, temp):
        try:
            return self._weights[msr_from[0] + msr_to[0]](temp)
        except KeyError:
            return f"Cannot convert from {msr_from} to {msr_to}"


def showMenu():
    print()
    print("Menu:")
    print("\t1. Numeric base converter")
    print("\t2. Temperature converter")
    print("\t3. Distance converter")
    print("\t4. Weight converter")
    print("\t0. Exit")


def menu():
    """
    Menu
    - Print menu
    - User chooses menu item
    - User inputs data to convert
    - User sees an answer
    """

    print("-- Conversions -- ")

    converter = Converter()

    while True:
        showMenu()
        try:
            userItem = int(input("Your choose: "))
            if userItem == 0:
                break
            elif userItem == 1:
                converter.baseConverterDialog()
            elif userItem == 2:
                converter.tempConverterDialog()
            elif userItem == 3:
                converter.distanceConverterDialog()
            elif userItem == 4:
                converter.weightConverterDialog()
            else:
                break
        except ValueError:
            print("Wrong data")


if __name__ == '__main__':
    menu()
