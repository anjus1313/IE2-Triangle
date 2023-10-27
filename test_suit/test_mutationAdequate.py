import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(6, 5, 10)
        expected = Triangle.Type.SCALENE
        #self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(6, 6, 10)
        expected = Triangle.Type.ISOSCELES
        #self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(6, 10, 10)
        expected = Triangle.Type.ISOSCELES
        #self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(6, 4, 10)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(0, 5, 5)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(5, 0, 5)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(5, 9, 5)
        expected = Triangle.Type.ISOSCELES
        #self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(5, 10, 5)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(13, 7, 6)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(6, 13, 7)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

    def test13(self):
        actual = Triangle.classify(5, 5, 0)
        expected = Triangle.Type.INVALID
        #self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()