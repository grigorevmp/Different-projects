# Проблема ближайшец пары
# Это задача вычислительной геометрии: дается n точек в метрическом пространстве,
# найти пару точек, расстояние между которыми наименьшее.

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    p1, p2 -> distance
    """
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))


def bruteForce(P, n):
    """
    P, n -> min_val
    A Brute Force method
    """
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < min_val:
                min_val = distance(P[i], P[j])
    return min_val


def stripClosest(strip, size, d):
    """
    strip, size, d -> min_val
    """
    min_val = d

    strip.sort(key=lambda point: point.y)

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = distance(strip[i], strip[j])
            j += 1

    return min_val


def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    midPoint = P[mid]

    dl = closestUtil(P[:mid], mid)
    dr = closestUtil(P[mid:], n - mid)

    d = min(dl, dr)

    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])

    return min(d, stripClosest(strip, len(strip), d))


def closest(P, n):
    P.sort(key=lambda point: point.x)

    return closestUtil(P, n)


def main():
    """
    Main function
    - Get user's number
    - Calculate result
    - Print result
    """

    print("-- Closets pair problem --\n")

    P = [Point(2, 3), Point(12, 30),
         Point(40, 50), Point(5, 1),
         Point(12, 10), Point(3, 4)]
    print("The smallest distance is",
          closest(P, len(P)))


if __name__ == '__main__':
    main()
