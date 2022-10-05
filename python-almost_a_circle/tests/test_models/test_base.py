#!/usr/bin/python3
""" Tests """
import unittest
from models.base import Base, base

class BaseClass(unittest.TestCase):
    """ Base class """
    def negative_id(self):
        result = Base(-12)
        self.assertEqual(result, -12)

    def auto_assign(self):
        result = Base()
        self.assertEqual(result.id, 1)

    def one_to_auto_assign(self):
        result = Base()
        result2 = Base()
        self.assertEqual(result.id, 2)

    if __name__ == '__main__':
        unittest.main()
