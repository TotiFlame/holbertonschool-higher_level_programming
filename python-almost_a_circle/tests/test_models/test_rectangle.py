#!/usr/bin/python3
""" rectangle tests """
import unittest
from models.rectangle import Rectangle


class RectangleClass(unittest.TestCase):
    """ rectangle class """
    def test_rectangle(self):
        result = Rectangle(3, 5)
        self.assertEqual(result.__str__(), '[Rectangle] (4) 0/0 - 3/5')

    def test_three_rectangle(self):
        result = Rectangle(3, 5, 2)
        self.assertEqual(result.__str__(), '[Rectangle] (5) 2/0 - 3/5')

    def test_three_rectangle(self):
        result = Rectangle(3, 5, 2, 3)
        self.assertEqual(result.__str__(), '[Rectangle] (5) 2/3 - 3/5')

if __name__ == '__main__':
    unittest.main()
