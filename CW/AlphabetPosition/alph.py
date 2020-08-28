# Alphabet Position

# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
  al = 'abcdefghijklmnopqrstuvwxyz'
  return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))