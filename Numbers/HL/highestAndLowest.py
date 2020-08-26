# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

import unittest


def high_and_low(numbers):
    return f"{sorted(list(map(int, numbers.split(' '))))[-1]} {sorted(list(map(int, numbers.split(' '))))[0]}"


class Test(unittest.TestCase):

    def test_split(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")


if __name__ == '__main__':
    unittest.main()
