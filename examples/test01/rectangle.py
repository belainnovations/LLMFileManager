from shape import Shape

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"{super().describe()} Specifically, I'm a rectangle with width {self.width} and height {self.height}."