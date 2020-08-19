"""
Реализуйте шифр Цезаря, как шифрование, так и дешифрование. Ключом является целое число от 1 до 25.
Этот ключ сдвигает буквы алфавита (от A до Z). При шифровании каждая буква алфавита заменяется буквой,
находящейся на выбранное количество позиций дальше (алфавит закольцовывается).
Таким образом, при использовании ключа 2 “HI” становится “JK”, а при использовании ключа 20 “HI”
превращается в “BC”. Это простое моноалфавитное шифрование легко взламывается, поскольку злоумышленник, у которого на
руках есть зашифрованное послание, может использовать частотный анализ, или просто попробовать все 25 ключей.
"""

"""
Implement a Caesar cipher, both encoding and decoding. The key is an integer
from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
encoding replaces each letter with the 1st to 25th next letter in the alphabet
(wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
"BC". This simple "monoalphabetic substitution cipher" provides almost no
security, because an attacker who has the encoded message can either use
frequency analysis to guess the key, or just try all 25 keys.
"""


class Caesar:

    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 0
        self.message = ''
        self.translated = ''

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.letters:
                num = self.letters.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.letters):
                    num = num - len(self.letters)
                elif num < 0:
                    num = num + len(self.letters)

                self.translated = self.translated + self.letters[num]
            else:
                self.translated = self.translated + symbol

        return self.translated

    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')


def inputString():
    """
    <input> -> string
    """
    try:
        mode = input("Input mode (encrypt, [decrypt]): ")
        string = input("Enter string to encrypt: ")
        key = int(input("Enter key to encrypt: "))
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

    print("-- Caesar cipher --\n")

    shouldContinue = True
    cr = Caesar()

    while shouldContinue:

        mode, string, key = inputString()
        if mode == "encoding":
            encrypted = cr.encrypt(string, key)
            print(f"Encrypted: {encrypted}")
        else:
            encrypted = cr.decrypt(string, key)
            print(f"Encrypted: {encrypted}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
