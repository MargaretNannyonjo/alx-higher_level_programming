#!/usr/bin/python3


import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_regular_list(self):
        # Test with regular list
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_unordered_list(self):
        # Test with an unordered list
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_max_integer_empty_list(self):
        # Test with an empty list
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_negative_values(self):
        # Test with negative values
        result = max_integer([-1, -5, -3, -2])
        self.assertEqual(result, -1)

    def test_max_integer_duplicates(self):
        # Test with duplicates
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
