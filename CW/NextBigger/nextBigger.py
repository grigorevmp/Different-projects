# Next bigger number with the same digits

# Create a function that takes a positive integer and returns the next bigger number that can be formed by
# rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071

def next_bigger(n):
    if int("".join(sorted(str(n), reverse=True))) == n:
        return -1
    num = list(str(n))
    for i in range(len(num)-1, 0, -1):
        if num[i] > num[i-1]:
            head=num[:i]
            tail=num[i:]
            break
    minB = sorted(list(tail))
    while minB[0] <= head[-1]:
        del minB[0]
    tail[tail.index(min(minB))], head[-1] = head[-1], tail[tail.index(min(minB))]
    return int(''.join(map(str, head + sorted(tail))))