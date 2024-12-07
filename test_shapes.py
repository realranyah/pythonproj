import unittest
from shapes import rectangle, square, triangle, circle

class testShape(unittest.TestCase):
    def testRec(self):
        self.assertEqual(rectangle(-1, 4), -4)
        self.assertEqual(rectangle(2, 5), 10)

    def testSquare(self):
        self.assertEqual(square(4), 16)

    def testTri(self):
        self.assertEqual(triangle(4, 3), 6)

    def testCir(self):
        self.assertEqual(circle(3), 28.26)