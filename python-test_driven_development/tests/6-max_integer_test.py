#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_messy_list(self):
        result = max_integer([10, 8, 23, 18, 5])
        self.assertEqual(result, 23)

    def test_sorted_list(self):
        result = max_integer([9, 11, 23, 45, 62])
        self.assertEqual(result, 62)

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_letter_list(self):
        result = max_integer(["hola", "chau"])
        self.assertEqual(result, "hola")

    def test_one_elem_list(self):
        result = max_integer([3])
        self.assertEqual(result, 3)

    if __name__ == '__main__':
        unittest.main()
