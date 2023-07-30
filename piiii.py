from math import *


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        c = self.length * self.breadth
        return c


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        c = pi * self.radius * self.radius
        return c


c1=Circle(4)
res=c1.area()
print(res)