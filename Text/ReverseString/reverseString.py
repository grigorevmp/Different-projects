# Разворот строки
# Reverse string

def reverse(string):
    """
    :param string: - orginal string
    :return: - reversed string
    """
    return string[::-1]


def inputString():
    """
    <input> -> string
    """
    string = input("Enter string to reverse: ")
    return string


def main():
    """
    Main function
    - Get user's string
    - Reverse it
    """

    print("-- Reverse string --\n")

    shouldContinue = True

    while shouldContinue:

        string = inputString()
        reversedString = reverse(string)
        print(f"Reversed: {reversedString}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
