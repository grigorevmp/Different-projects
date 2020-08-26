# Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces. Spaces will be
# included only when more than one word is present.
#
# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    new = ""
    for s in sentence.split():
        if len(s) >= 5:
            new += s[::-1] + " "
        else:
            new += s + " "
    return new[:len(new)-1]


if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))
    print(spin_words("This is a test"))
    print(spin_words("This is another test"))
