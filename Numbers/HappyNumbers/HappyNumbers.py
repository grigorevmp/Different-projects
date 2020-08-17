# Счастливое число определено следующим процессом. Начиная с некоторого положительного целого числа,
# замените число суммой квадратов его цифр и повторяйте процесс до тех пор, пока число не будет равным
# одному(на чем все и остановится) или оно будет циклиться бесконечно. Если цикл конечен,
# то изначальное число называется счастливым. Найдите первые 8 счастливых чисел.

# In number theory, a happy number is a number which eventually reaches 1 when replaced by the sum of the square of
# each digit

def isHappy(num):
    """
    num -> is happy
    """

    allPrev = []

    while True:
        newNum = 0
        
        while num > 0:
            newNum += (num % 10) ** 2
            num //= 10
            
        if newNum == 1:
            return True
        if allPrev and newNum in allPrev:
            return False

        allPrev.append(newNum)
        num = newNum


def findEightHappy():
    num = 1
    count = 0
    while count < 8:
        if isHappy(num):
            print(count + 1, ": ", num)
            count += 1
        num += 1


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Happy numbers --\n")

    findEightHappy()


if __name__ == '__main__':
    main()
