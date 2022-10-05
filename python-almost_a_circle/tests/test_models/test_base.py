#!/usr/bin/python3
""" base tests """
import unittest
from models.base import Base

class BaseClass(unittest.TestCase):
    """ Base class """
    def test_negative_id(self):
        result = Base(-12)
        self.assertEqual(result.id, -12)

    def test_auto_assign(self):
        result = Base()
        self.assertEqual(result.id, 1)

    def test_one_to_auto_assign(self):
        result = Base()
        result2 = Base()
        self.assertEqual(result.id, 2)

    if __name__ == '__main__':
        unittest.main()
