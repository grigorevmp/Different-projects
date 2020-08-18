# Поросячья латынь
# Pig latin

def pigLatin(string):
    """
    Pig Latin – Pig Latin is a game of alterations played on the English language game.
    To create the Pig Latin form of an English word the initial consonant sound is transposed
    to the end of the word and an ay is affixed
    (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
    """
    words = []
    vowels = 'aeiou'
    for word in string.split():
        if len(word) > 2 and word[0] not in vowels:
            words.append(word[1:] + '-' + word[0] + 'ay')
        else:
            words.append(word + '-ay')
    return ' '.join(words)


def inputString():
    """
    <input> -> string
    """
    string = input("Enter string to cypher: ")
    return string


def main():
    """
    Main function
    - Get user's string
    - Reverse it
    """

    print("-- Pig latin --\n")

    shouldContinue = True

    while shouldContinue:

        string = inputString()
        nums = pigLatin(string)
        print(f"Cyphered word: {nums}")

        should = input("\nContinue (Y/[N]): ")
        if should.upper() != 'Y':
            shouldContinue = False
        else:
            shouldContinue = True


if __name__ == '__main__':
    main()
