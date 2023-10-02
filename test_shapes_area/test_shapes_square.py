import math
import unittest

from shapes_area.shapes_area import Circle, Triangle, calculate_area


class TestShape(unittest.TestCase):
    def test_circle_area(self):
        radius = float(input("Enter circle radius: "))
        circle = Circle(radius=radius)
        s = math.pi * radius ** 2
        self.assertEqual(circle.get_area(), s)

    def test_triangle_area(self):
        a, b, c = map(float, input("Enter triangle sides: ").split())
        triangle = Triangle(a=a, b=b, c=c)
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        self.assertEqual(triangle.get_area(), s)

    def test_triangle_rectangular(self):
        a, b, c = 3, 4, 5
        triangle = Triangle(a=a, b=b, c=c)
        self.assertTrue(triangle.is_rectangular())

        triangle.a = 5
        self.assertFalse(triangle.is_rectangular())

    def test_calculate_area(self):
        radius = 8
        circle = Circle(radius=radius)
        self.assertEqual(calculate_area(shape=circle), math.pi * 64)

        a, b, c = 3, 4, 5
        triangle = Triangle(a=a, b=b, c=c)
        self.assertEqual(calculate_area(shape=triangle), 6)

        triangle.a = 5
        self.assertFalse(triangle.is_rectangular())


if __name__ == "__main__":
    unittest.main()
