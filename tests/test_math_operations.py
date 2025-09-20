"""
Comprehensive test suite for math_operations module.

Tests all mathematical functions including edge cases, error conditions,
and boundary conditions.
"""

import unittest
import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from math_operations import (
    add_numbers, multiply_list, calculate_average,
    find_prime_factors, fibonacci_sequence
)


class TestAddNumbers(unittest.TestCase):
    """Test cases for add_numbers function."""

    def test_positive_integers(self):
        """Test addition with positive integers."""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(10, 0), 10)

    def test_negative_integers(self):
        """Test addition with negative integers."""
        self.assertEqual(add_numbers(-5, -3), -8)
        self.assertEqual(add_numbers(-5, 3), -2)
        self.assertEqual(add_numbers(5, -3), 2)

    def test_floating_point(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add_numbers(2.5, 1.5), 4.0)
        self.assertAlmostEqual(add_numbers(-2.5, 1.5), -1.0)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=10)

    def test_zero_operations(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(0.0, 0.0), 0.0)

    def test_large_numbers(self):
        """Test addition with large numbers."""
        large_int = 10**15
        self.assertEqual(add_numbers(large_int, large_int), 2 * large_int)

    def test_nan_handling(self):
        """Test handling of NaN values."""
        result = add_numbers(float('nan'), 5)
        self.assertTrue(math.isnan(result))
        result = add_numbers(5, float('nan'))
        self.assertTrue(math.isnan(result))

    def test_infinity_error(self):
        """Test error handling for infinite values."""
        with self.assertRaises(OverflowError):
            add_numbers(float('inf'), 5)
        with self.assertRaises(OverflowError):
            add_numbers(5, float('-inf'))

    def test_type_error(self):
        """Test type error for non-numeric inputs."""
        with self.assertRaises(TypeError):
            add_numbers("5", 3)
        with self.assertRaises(TypeError):
            add_numbers(5, "3")
        with self.assertRaises(TypeError):
            add_numbers(None, 5)


class TestMultiplyList(unittest.TestCase):
    """Test cases for multiply_list function."""

    def test_positive_integers(self):
        """Test multiplication with positive integers."""
        self.assertEqual(multiply_list([2, 3, 4]), 24)
        self.assertEqual(multiply_list([1, 5, 2]), 10)
        self.assertEqual(multiply_list([1]), 1)

    def test_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply_list([2, 0, 4]), 0)
        self.assertEqual(multiply_list([0]), 0)

    def test_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply_list([-2, 3]), -6)
        self.assertEqual(multiply_list([-2, -3]), 6)
        self.assertEqual(multiply_list([-1, -1, -1]), -1)

    def test_floating_point(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(multiply_list([1.5, 2.0]), 3.0)
        self.assertAlmostEqual(multiply_list([0.5, 0.5]), 0.25)

    def test_empty_list_error(self):
        """Test error for empty list."""
        with self.assertRaises(ValueError):
            multiply_list([])

    def test_non_list_input_error(self):
        """Test error for non-list input."""
        with self.assertRaises(TypeError):
            multiply_list("123")
        with self.assertRaises(TypeError):
            multiply_list(123)

    def test_non_numeric_elements_error(self):
        """Test error for non-numeric elements."""
        with self.assertRaises(TypeError):
            multiply_list([1, 2, "3"])
        with self.assertRaises(TypeError):
            multiply_list([1, None, 3])

    def test_nan_handling(self):
        """Test handling of NaN values."""
        result = multiply_list([1, 2, float('nan')])
        self.assertTrue(math.isnan(result))

    def test_infinity_handling(self):
        """Test handling of infinite values."""
        result = multiply_list([2, float('inf')])
        self.assertTrue(math.isinf(result) and result > 0)
        result = multiply_list([2, float('-inf')])
        self.assertTrue(math.isinf(result) and result < 0)


class TestCalculateAverage(unittest.TestCase):
    """Test cases for calculate_average function."""

    def test_positive_numbers(self):
        """Test average with positive numbers."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10, 20]), 15.0)
        self.assertEqual(calculate_average([5]), 5.0)

    def test_negative_numbers(self):
        """Test average with negative numbers."""
        self.assertEqual(calculate_average([-1, -2, -3]), -2.0)
        self.assertEqual(calculate_average([-5, 5]), 0.0)

    def test_floating_point(self):
        """Test average with floating point numbers."""
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.0]), 2.333333333333333)
        self.assertEqual(calculate_average([2.0, 4.0]), 3.0)

    def test_with_zero(self):
        """Test average including zero."""
        self.assertEqual(calculate_average([0, 5, 10]), 5.0)
        self.assertEqual(calculate_average([0]), 0.0)

    def test_empty_list_error(self):
        """Test error for empty list."""
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_non_list_input_error(self):
        """Test error for non-list input."""
        with self.assertRaises(TypeError):
            calculate_average("123")

    def test_non_numeric_elements_error(self):
        """Test error for non-numeric elements."""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "3"])

    def test_nan_handling(self):
        """Test handling of NaN values (should be ignored)."""
        result = calculate_average([1, 2, float('nan'), 3])
        self.assertEqual(result, 2.0)
        result = calculate_average([float('nan')])
        self.assertTrue(math.isnan(result))

    def test_infinity_handling(self):
        """Test handling of infinite values."""
        result = calculate_average([1, 2, float('inf')])
        self.assertTrue(math.isinf(result) and result > 0)
        result = calculate_average([1, 2, float('-inf')])
        self.assertTrue(math.isinf(result) and result < 0)


class TestFindPrimeFactors(unittest.TestCase):
    """Test cases for find_prime_factors function."""

    def test_small_numbers(self):
        """Test prime factorization of small numbers."""
        self.assertEqual(find_prime_factors(1), [])
        self.assertEqual(find_prime_factors(2), [2])
        self.assertEqual(find_prime_factors(3), [3])
        self.assertEqual(find_prime_factors(4), [2, 2])

    def test_composite_numbers(self):
        """Test prime factorization of composite numbers."""
        self.assertEqual(find_prime_factors(12), [2, 2, 3])
        self.assertEqual(find_prime_factors(15), [3, 5])
        self.assertEqual(find_prime_factors(30), [2, 3, 5])
        self.assertEqual(find_prime_factors(100), [2, 2, 5, 5])

    def test_prime_numbers(self):
        """Test prime factorization of prime numbers."""
        self.assertEqual(find_prime_factors(7), [7])
        self.assertEqual(find_prime_factors(13), [13])
        self.assertEqual(find_prime_factors(17), [17])

    def test_larger_numbers(self):
        """Test prime factorization of larger numbers."""
        self.assertEqual(find_prime_factors(60), [2, 2, 3, 5])
        self.assertEqual(find_prime_factors(72), [2, 2, 2, 3, 3])

    def test_perfect_squares(self):
        """Test prime factorization of perfect squares."""
        self.assertEqual(find_prime_factors(9), [3, 3])
        self.assertEqual(find_prime_factors(16), [2, 2, 2, 2])
        self.assertEqual(find_prime_factors(25), [5, 5])

    def test_non_integer_error(self):
        """Test error for non-integer input."""
        with self.assertRaises(TypeError):
            find_prime_factors(12.5)
        with self.assertRaises(TypeError):
            find_prime_factors("12")

    def test_non_positive_error(self):
        """Test error for non-positive integers."""
        with self.assertRaises(ValueError):
            find_prime_factors(0)
        with self.assertRaises(ValueError):
            find_prime_factors(-5)


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for fibonacci_sequence function."""

    def test_zero_and_one(self):
        """Test Fibonacci sequence for n=0 and n=1."""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_small_sequences(self):
        """Test small Fibonacci sequences."""
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])
        self.assertEqual(fibonacci_sequence(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_medium_sequence(self):
        """Test medium-sized Fibonacci sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected)

    def test_sequence_properties(self):
        """Test mathematical properties of Fibonacci sequence."""
        fib_10 = fibonacci_sequence(10)
        self.assertEqual(len(fib_10), 10)
        for i in range(2, len(fib_10)):
            self.assertEqual(fib_10[i], fib_10[i-1] + fib_10[i-2])

    def test_larger_sequence(self):
        """Test that larger sequences work and have correct length."""
        fib_20 = fibonacci_sequence(20)
        self.assertEqual(len(fib_20), 20)
        self.assertEqual(fib_20[0], 0)
        self.assertEqual(fib_20[1], 1)
        self.assertEqual(fib_20[-1], 4181)  # 20th Fibonacci number

    def test_non_integer_error(self):
        """Test error for non-integer input."""
        with self.assertRaises(TypeError):
            fibonacci_sequence(5.5)
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")

    def test_negative_error(self):
        """Test error for negative input."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-10)


if __name__ == '__main__':
    unittest.main(verbosity=2)