#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -1, 0]), 5)

    def test_all_same(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_with_floats(self):
        """Test a list containing float numbers"""
        self.assertEqual(max_integer([1.2, 2.5, 0.3, 4.8]), 4.8)

    def test_mixed_ints_and_floats(self):
        """Test a list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)

    def test_large_numbers(self):
        """Test a list with large numbers"""
        self.assertEqual(max_integer([1000000000, 999999999, 1000000001]), 1000000001)

    def test_string_input(self):
        """Test a list of strings (max by lexicographical order)"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_string_mixed_case(self):
        """Test a list of strings with mixed case"""
        self.assertEqual(max_integer(["a", "A", "b", "B"]), "b")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertIsNone(max_integer(""))

    def test_invalid_input(self):
        """Test invalid input (raises TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == "__main__":
    unittest.main()