# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it
# should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
import re
import unittest


def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return [s[i:i + 2] for i in range(0, len(s), 2)]



class Test(unittest.TestCase):

    def test_split(self):
        self.assertEqual(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
        self.assertEqual(solution("asdfads"), ['as', 'df', 'ad', 's_'])
        self.assertEqual(solution(""), [])
        self.assertEqual(solution("x"), ["x_"])


if __name__ == '__main__':
    unittest.main()
