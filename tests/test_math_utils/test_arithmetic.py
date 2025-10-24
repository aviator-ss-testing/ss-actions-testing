"""
Comprehensive test suite for arithmetic operations module.

This module tests all arithmetic functions including positive cases,
edge cases, and error handling scenarios.
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.math_utils.arithmetic import add, subtract, multiply, divide


class TestArithmetic(unittest.TestCase):
    """Test suite for arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(100, 250), 350)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, -20), -30)

    def test_add_mixed_signs(self):
        """Test addition with mixed positive and negative numbers."""
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(10, -10), 0)

    def test_add_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)

    def test_add_with_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(add(3.14159, 2.71828), 5.85987)

    def test_add_large_numbers(self):
        """Test addition with very large numbers."""
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(10**15, 10**15), 2 * 10**15)

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(20, 10), 10)
        self.assertEqual(subtract(100, 25), 75)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, -20), 10)

    def test_subtract_mixed_signs(self):
        """Test subtraction with mixed positive and negative numbers."""
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_resulting_in_zero(self):
        """Test subtraction resulting in zero."""
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(100, 100), 0)

    def test_subtract_with_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2, places=10)
        self.assertAlmostEqual(subtract(10.0, 3.5), 6.5)

    def test_subtract_large_numbers(self):
        """Test subtraction with very large numbers."""
        self.assertEqual(subtract(3000000, 1000000), 2000000)
        self.assertEqual(subtract(10**15, 10**14), 9 * 10**14)

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 7), 35)
        self.assertEqual(multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(-5, -5), 25)

    def test_multiply_mixed_signs(self):
        """Test multiplication with mixed positive and negative numbers."""
        self.assertEqual(multiply(5, -3), -15)
        self.assertEqual(multiply(-5, 3), -15)

    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(100, 0), 0)

    def test_multiply_with_one(self):
        """Test multiplication with one (identity property)."""
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(-7, 1), -7)

    def test_multiply_with_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(multiply(2.5, 3.0), 7.5)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)
        self.assertAlmostEqual(multiply(3.14, 2.0), 6.28)

    def test_multiply_large_numbers(self):
        """Test multiplication with very large numbers."""
        self.assertEqual(multiply(1000, 1000), 1000000)
        self.assertEqual(multiply(10**6, 10**6), 10**12)

    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(20, 4), 5.0)
        self.assertEqual(divide(100, 10), 10.0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-6, -3), 2.0)
        self.assertEqual(divide(-20, -4), 5.0)

    def test_divide_mixed_signs(self):
        """Test division with mixed positive and negative numbers."""
        self.assertEqual(divide(6, -3), -2.0)
        self.assertEqual(divide(-6, 3), -2.0)

    def test_divide_resulting_in_float(self):
        """Test division resulting in floating point numbers."""
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(10, 3), 3.333333, places=5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

    def test_divide_with_zero_numerator(self):
        """Test division with zero as numerator."""
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, 100), 0.0)
        self.assertEqual(divide(0, -5), 0.0)

    def test_divide_with_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide(10.0, 4.0), 2.5)

    def test_divide_large_numbers(self):
        """Test division with very large numbers."""
        self.assertEqual(divide(1000000, 1000), 1000.0)
        self.assertEqual(divide(10**12, 10**6), 10**6)

    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_by_zero_with_zero_numerator(self):
        """Test that division by zero raises exception even with zero numerator."""
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    def test_divide_by_zero_with_negative_numerator(self):
        """Test that division by zero raises exception with negative numerator."""
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)


if __name__ == '__main__':
    unittest.main()
