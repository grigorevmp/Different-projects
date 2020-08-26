# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers
# finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)

# # Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

import unittest


# Best solution
def iq_test_2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


# My solution
def iq_test(numbers):
    odd = 0
    even = 0
    curr = 0
    ro = 0
    re = 0
    n = 0
    for num in numbers.split():
        n += 1
        if int(num) % 2 == 0:
            even += 1
            curr += 1
            re = n
            if even >= 2 and odd == 1:
                if ro:
                    return ro
                else:
                    return num
            if even == 1 and odd >= 2:
                if re:
                    return re
                else:
                    return num
        else:
            odd += 1
            ro = n
            if even == 1 and odd >= 2:
                if re:
                    return re
                else:
                    return num
            if even >= 2 and odd == 1:
                if ro:
                    return ro
                else:
                    return num


class Test(unittest.TestCase):

    def test_split(self):
        # self.assertEqual(iq_test("2 4 7 8 10"), 3)
        # self.assertEqual(iq_test("1 2 2"), 1)
        self.assertEqual(iq_test("44 8 32 42 16 3"), 6)


if __name__ == '__main__':
    unittest.main()
