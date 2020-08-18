# Счётчик гласных
# Count Vowels

def countVowels(string=None):
    """
    :param string: - String to work with
    :return: - Vowels count
    """
    vowels = "aeiou"
    count = {char: 0 for char in vowels}
    for char in string:
        if char in vowels:
            count[char] += 1
    return count


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
    - Reverse it
    """

    print("-- Count Vowels --\n")

    shouldContinue = True

    while shouldContinue:

        string = inputString()
        nums = countVowels(string)
        print(f"Vowels number: {nums}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
