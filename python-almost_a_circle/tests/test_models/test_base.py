#!/usr/bin/python3
""" Tests """
import unittest
from models.base import Base, base

class BaseClass(unittest.TestCase):
    """ Base class """
    def negative_id(self):
        result = Base(-12)
        self.assertEqual(result, -12)

    if __name__ == '__main__':
        unittest.main()
