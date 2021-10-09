# Счётчик слов
# Count Words

class WordCounter:

    def __init__(self):
        self.words = 0
        self.data = None

    def countWords(self, string=None, file=None):
        """
        :param string: - If user wants to work with string
        :param file: -  If user wants to work with file
        :return: - Words count
        """
        if string:
            self.data = ''.join(c for c in string if (c.isalpha() or c == ' '))
        if file:
            with open(file) as f:
                self.data = ''.join(c for c in f.read() if (c.isalpha() or c == ' '))
        self.words = len(self.data.split())
        print(self.data)

    def showResult(self):
        print(f"Word number: {self.words}")


def inputString():
    """
    <input> -> string
    """
    string = input("Enter string to count words: ")
    return string


def main():
    """
    Main function
    - Get user's string
    - Reverse it
    """

    print("-- Count words --\n")

    shouldContinue = True
    wrdCnt = WordCounter()
    while shouldContinue:
        string = inputString()
        wrdCnt.countWords(string)
        wrdCnt.showResult()
        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
