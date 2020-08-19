from itertools import cycle

alp = 'abcdefghijklmnopqrstuvwxyz'


def encode(text, key):
    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 26) % 26]
    return ''.join(map(f, zip(text, cycle(key))))


def decode(coded_text, key):
    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 26]
    return ''.join(map(f, zip(coded_text, cycle(key))))


def inputString():
    """
    <input> -> string
    """
    try:
        mode = input("Input mode (encrypt, [decrypt]): ")
        string = input("Enter string to encrypt: ")
        key = input("Enter key to encrypt: ")
        return mode, string, key
    except ValueError:
        print("Wrong data")


def main():
    """
    Main function
    - Get user's string
    - encode it
    - decode it
    """

    print("-- Vernam cipher --\n")

    shouldContinue = True

    while shouldContinue:

        mode, string, key = inputString()
        if mode == "encoding":
            encrypted = encode(string, key)
            print(f"Encrypted: {encrypted}")
        else:
            encrypted = decode(string, key)
            print(f"Encrypted: {encrypted}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
