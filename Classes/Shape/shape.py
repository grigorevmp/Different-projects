from math import pi, sqrt
from abc import ABC, abstractmethod

"""
Shapes

I use @property and @abstractmethod for the first time and it's really cool thing
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        return pi * self._radius * self._radius

    @property
    def perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @property
    def sides(self):
        return [self._side_a, self._side_b, self._side_c]

    @property
    def area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2
        return sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c
