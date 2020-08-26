import fileinput

total = 0

for line in fileinput.input():
    lst = line.split()
    numbers = map(int, lst)
    total += sum(numbers)

print(total)