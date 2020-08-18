# Счётчик слов
# Count Words

def countWords(string=None, file=None):
    """
    :param string: - If user wants to work with string
    :param file: -  If user wants to work with file
    :return: - Words count
    """
    word_count = 0
    if string:
        word_count = len(string.split())
    if file:
        with open(file) as f:
            word_count = len(f.read().split())
    return word_count


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

    while shouldContinue:

        string = inputString()
        nums = countWords(string)
        print(f"Word number: {nums}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
