import unittest
from math import pi
from shape import Shape
from circle import Circle
from rectangle import Rectangle

class TestShapes(unittest.TestCase):
    def test_shape_abstract(self):
        with self.assertRaises(NotImplementedError):
            Shape("red").area()

    def test_circle(self):
        circle = Circle("blue", 5)
        self.assertEqual(circle.color, "blue")
        self.assertEqual(circle.radius, 5)
        self.assertAlmostEqual(circle.area(), pi * 25, places=2)
        self.assertIn("blue shape", circle.describe())
        self.assertIn("circle with radius 5", circle.describe())

    def test_rectangle(self):
        rectangle = Rectangle("green", 4, 6)
        self.assertEqual(rectangle.color, "green")
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.area(), 24)
        self.assertIn("green shape", rectangle.describe())
        self.assertIn("rectangle with width 4 and height 6", rectangle.describe())

if __name__ == '__main__':
    unittest.main()