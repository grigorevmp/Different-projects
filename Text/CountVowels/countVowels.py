# Счётчик гласных
# Count Vowels


class VowelCounter:

    def __init__(self):
        self.vowels = "aeiou"
        self.count = {char: 0 for char in self.vowels}
        self.string = ''

    def countVowels(self, str=None):
        """
        :param string: - String to work with
        :return: - Vowels count
        """
        self.string = str
        for char in self.string:
            if char in self.vowels:
                self.count[char] += 1

    def getCount(self):
        return self.count

    def getString(self):
        return self.string

    def clearData(self):
        self.count = {char: 0 for char in self.vowels}
        self.string = ''


def inputString():
    """
    <input> -> string
    """
    string = input("Enter string to count vowels: ")
    return string


def main():
    """
    Main function
    - Get user's string
    - Count vowels in it
    """

    print("-- Count Vowels --\n")

    shouldContinue = True
    vowCnt = VowelCounter()
    while shouldContinue:

        string = inputString()
        vowCnt.countVowels(string)
        print(f"Vowels number in \"{vowCnt.getString()}\": {vowCnt.getCount()}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
