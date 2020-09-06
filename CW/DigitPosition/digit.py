# The position of a digital string in a infinite digital string
# https://www.codewars.com/kata/582c1092306063791c000c00/train/python

#  findPosition("454") = ?
#  Oh, no! There is no "454" in "123456789101112131415",
#  so we should return -1?
#  No, I said, this is a string of infinite length.
#  We need to increase the length of the string to find "454"
#
#  findPosition("454") == 79
#  because "123456789101112131415...44454647".indexOf("454")=79
#   findPosition("456") == 3
#  ("...3456...")
#        ^^^
#  findPosition("454") == 79
#  ("...444546...")
#         ^^^
#  findPosition("455") == 98
#  ("...545556...")
#        ^^^
#  findPosition("910") == 8
#  ("...7891011...")
#         ^^^

### Execution Timed Out
def findPosition(num):
    i = 1
    iter = 0
    res = ""
    while True:
        for sym in str(i):
            res += sym
            iter += 1
            if len(num) <= len(res) and res[len(res) - len(num):len(res)] == num:
                return iter - len(num)
        i += 1



if __name__ == '__main__':
    print(findPosition("456"))
    print(findPosition("454"))
    print(findPosition("455"))
    print(findPosition("910"))
    print(findPosition("9100"))
    print(findPosition("99100"))
    print(findPosition("00101"))
    print(findPosition("001"))
    print(findPosition("00"))
    print(findPosition("123456789"))
    print(findPosition("1234567891"))
    print(findPosition("123456798"))
    print(findPosition("10"))
    print(findPosition("53635"))
    print(findPosition("040"))
    print(findPosition("11"))
    print(findPosition("99"))
    print(findPosition("667"))
    print(findPosition("0404"))
    print(findPosition("949225100"))
    print(findPosition("58257860625"))
    print(findPosition("3999589058124"))
    print(findPosition("555899959741198"))
    print(findPosition("01"))
    print(findPosition("091"))
    print(findPosition("0910"))
    print(findPosition("0991"))
    print(findPosition("09910"))
    print(findPosition("09991"))