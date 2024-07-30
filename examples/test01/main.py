from shape import Shape
from circle import Circle
from rectangle import Rectangle

def main():
    circle = Circle("red", 5)
    rectangle = Rectangle("blue", 4, 6)

    shapes = [circle, rectangle]

    for shape in shapes:
        print(shape.describe())
        print(f"Area: {shape.area():.2f}")
        print()

if __name__ == "__main__":
    main()