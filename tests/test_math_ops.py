"""
Unit tests for math_ops module.

Tests cover all mathematical utility functions including factorial, fibonacci,
greatest common divisor, and prime number checking with various edge cases.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.math_ops import factorial, fibonacci, gcd, is_prime


class TestMathOps(unittest.TestCase):
    """Test class for mathematical operations."""

    def test_factorial_normal_cases(self):
        """Test factorial with normal positive integers."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_edge_case_zero(self):
        """Test factorial of 0 returns 1."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_edge_case_one(self):
        """Test factorial of 1 returns 1."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative_input(self):
        """Test factorial raises ValueError for negative numbers."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("negative", str(context.exception).lower())

        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_invalid_type(self):
        """Test factorial raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            factorial(3.5)

        with self.assertRaises(TypeError):
            factorial("5")

        with self.assertRaises(TypeError):
            factorial(None)

    def test_fibonacci_base_cases(self):
        """Test fibonacci with base cases 0 and 1."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_normal_cases(self):
        """Test fibonacci with various positions."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_negative_input(self):
        """Test fibonacci raises ValueError for negative indices."""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertIn("negative", str(context.exception).lower())

        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_invalid_type(self):
        """Test fibonacci raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            fibonacci(5.5)

        with self.assertRaises(TypeError):
            fibonacci("10")

        with self.assertRaises(TypeError):
            fibonacci([1, 2, 3])

    def test_gcd_normal_cases(self):
        """Test gcd with various number pairs."""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(18, 48), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(54, 24), 6)

    def test_gcd_edge_case_zero(self):
        """Test gcd with zero as one of the inputs."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_edge_case_one(self):
        """Test gcd with one as an input."""
        self.assertEqual(gcd(1, 5), 1)
        self.assertEqual(gcd(5, 1), 1)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_negative_numbers(self):
        """Test gcd handles negative numbers correctly."""
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_same_numbers(self):
        """Test gcd of identical numbers."""
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(42, 42), 42)

    def test_gcd_invalid_type(self):
        """Test gcd raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            gcd(3.5, 5)

        with self.assertRaises(TypeError):
            gcd(5, "10")

        with self.assertRaises(TypeError):
            gcd(None, 5)

    def test_is_prime_prime_numbers(self):
        """Test is_prime correctly identifies prime numbers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(97))

    def test_is_prime_composite_numbers(self):
        """Test is_prime correctly identifies composite numbers."""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(100))

    def test_is_prime_edge_case_zero(self):
        """Test is_prime returns False for 0."""
        self.assertFalse(is_prime(0))

    def test_is_prime_edge_case_one(self):
        """Test is_prime returns False for 1."""
        self.assertFalse(is_prime(1))

    def test_is_prime_edge_case_two(self):
        """Test is_prime correctly identifies 2 as prime."""
        self.assertTrue(is_prime(2))

    def test_is_prime_negative_numbers(self):
        """Test is_prime returns False for negative numbers."""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-10))

    def test_is_prime_invalid_type(self):
        """Test is_prime raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            is_prime(5.5)

        with self.assertRaises(TypeError):
            is_prime("7")

        with self.assertRaises(TypeError):
            is_prime(None)


if __name__ == '__main__':
    unittest.main()
