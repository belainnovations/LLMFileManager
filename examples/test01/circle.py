from math import pi
from shape import Shape

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def describe(self):
        return f"{super().describe()} Specifically, I'm a circle with radius {self.radius}."