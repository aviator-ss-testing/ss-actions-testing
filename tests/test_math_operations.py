"""
Comprehensive test suite for the math_operations module.

Tests cover all mathematical functions with positive, negative, and edge case scenarios
including proper error handling validation.
"""

import unittest
import sys
import os

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from math_operations import add, subtract, multiply, divide, power, factorial


class TestMathOperations(unittest.TestCase):
    """Test cases for all math operations functions."""

    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 15), 25)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(10, -15), -5)

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(add(-1.5, 2.8), 1.3, places=7)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -5), -5)

    def test_add_type_error(self):
        """Test add function raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(2, "3")
        with self.assertRaises(TypeError):
            add(None, 5)
        with self.assertRaises(TypeError):
            add([], 5)

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 15), -5)
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-2, -3), 1)
        self.assertEqual(subtract(-10, 5), -15)
        self.assertEqual(subtract(10, -5), 15)

    def test_subtract_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(subtract(5.7, 2.3), 3.4, places=7)
        self.assertAlmostEqual(subtract(-1.5, -2.8), 1.3, places=7)

    def test_subtract_type_error(self):
        """Test subtract function raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            subtract("5", 3)
        with self.assertRaises(TypeError):
            subtract(5, "3")
        with self.assertRaises(TypeError):
            subtract(None, 5)

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(1, 10), 10)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(3, -4), -12)
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0, places=7)
        self.assertAlmostEqual(multiply(-1.5, 2.0), -3.0, places=7)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_type_error(self):
        """Test multiply function raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            multiply("3", 4)
        with self.assertRaises(TypeError):
            multiply(3, "4")
        with self.assertRaises(TypeError):
            multiply(None, 5)

    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(10, 4), 2.5)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-6, 2), -3.0)
        self.assertEqual(divide(6, -2), -3.0)
        self.assertEqual(divide(-6, -2), 3.0)

    def test_divide_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(divide(-4.5, 1.5), -3.0, places=7)

    def test_divide_by_zero_error(self):
        """Test divide function raises ZeroDivisionError for division by zero."""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    def test_divide_type_error(self):
        """Test divide function raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            divide("6", 2)
        with self.assertRaises(TypeError):
            divide(6, "2")
        with self.assertRaises(TypeError):
            divide(None, 5)

    def test_power_positive_numbers(self):
        """Test power function with positive numbers."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(1, 100), 1)

    def test_power_negative_base(self):
        """Test power function with negative base."""
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-1, 5), -1)

    def test_power_negative_exponent(self):
        """Test power function with negative exponent."""
        self.assertEqual(power(2, -3), 0.125)
        self.assertAlmostEqual(power(4, -2), 0.25, places=7)

    def test_power_floats(self):
        """Test power function with floating point numbers."""
        self.assertAlmostEqual(power(2.5, 2), 6.25, places=7)
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=7)

    def test_power_edge_cases(self):
        """Test power function edge cases."""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)  # 0^0 = 1 by convention

    def test_power_type_error(self):
        """Test power function raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            power("2", 3)
        with self.assertRaises(TypeError):
            power(2, "3")
        with self.assertRaises(TypeError):
            power(None, 5)

    def test_factorial_positive_integers(self):
        """Test factorial function with positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_edge_cases(self):
        """Test factorial function edge cases."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_large_numbers(self):
        """Test factorial function with reasonably large numbers."""
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_number_error(self):
        """Test factorial function raises ValueError for negative numbers."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_non_integer_error(self):
        """Test factorial function raises TypeError for non-integers."""
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(None)

    def test_factorial_overflow_error(self):
        """Test factorial function raises OverflowError for very large numbers."""
        with self.assertRaises(OverflowError):
            factorial(1001)  # Should exceed the limit set in the function


if __name__ == '__main__':
    unittest.main()