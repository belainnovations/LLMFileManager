from shape import Shape
from circle import Circle
from rectangle import Rectangle

def print_shape_info(shape: Shape):
    print(shape.describe())
    print(f"Area: {shape.area():.2f}")
    print()

def main():
    # Create instances of Circle and Rectangle
    small_circle = Circle("blue", 3)
    large_circle = Circle("yellow", 7)
    square = Rectangle("green", 5, 5)
    rectangle = Rectangle("blue", 4, 6)

    # Store shapes in a list to demonstrate polymorphism
    shapes = [small_circle, large_circle, square, rectangle]

    # Print information for each shape
    for shape in shapes:
        print_shape_info(shape)

    # Demonstrate that we can still access specific attributes of subclasses
    print(f"The small circle has a radius of {small_circle.radius}")
    print(f"The rectangle has a width of {rectangle.width} and a height of {rectangle.height}")

if __name__ == "__main__":
    main()