# Палиндром
# Palindrome

def palindrome(string):
    """
    :param string: - original string
    :return: - reversed string
    """
    return string == string[::-1]


def inputString():
    """
    <input> -> string
    """
    string = input("Enter string to check for palindrome: ")
    return string


def main():
    """
    Main function
    - Get user's string
    - Reverse it
    """

    print("-- Palindrome --\n")

    shouldContinue = True

    while shouldContinue:

        string = inputString()
        reversedString = palindrome(string)
        print(f"Palindrome: {reversedString}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
