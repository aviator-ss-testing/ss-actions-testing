"""
Unit tests for mathematical operations module.

Tests cover basic arithmetic, advanced mathematical functions,
edge cases, and error handling scenarios.
"""

import unittest
import sys
import math
sys.path.insert(0, '..')
from math_ops import add, subtract, multiply, divide, factorial, fibonacci, is_prime, gcd


class TestBasicArithmetic(unittest.TestCase):
    """Test suite for basic arithmetic operations."""

    def test_add_integers(self):
        """Test addition with integer inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_add_floats(self):
        """Test addition with float inputs."""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=10)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0, places=10)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)

    def test_add_mixed_types(self):
        """Test addition with mixed int and float inputs."""
        self.assertEqual(add(5, 2.5), 7.5)
        self.assertEqual(add(2.5, 5), 7.5)

    def test_subtract_integers(self):
        """Test subtraction with integer inputs."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(100, 50), 50)

    def test_subtract_floats(self):
        """Test subtraction with float inputs."""
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2, places=10)
        self.assertAlmostEqual(subtract(-1.5, 2.5), -4.0, places=10)

    def test_subtract_mixed_types(self):
        """Test subtraction with mixed int and float inputs."""
        self.assertEqual(subtract(10, 2.5), 7.5)
        self.assertEqual(subtract(7.5, 2), 5.5)

    def test_multiply_integers(self):
        """Test multiplication with integer inputs."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(7, 8), 56)

    def test_multiply_floats(self):
        """Test multiplication with float inputs."""
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0, places=10)
        self.assertAlmostEqual(multiply(-2.5, 3.0), -7.5, places=10)
        self.assertAlmostEqual(multiply(0.1, 0.1), 0.01, places=10)

    def test_multiply_mixed_types(self):
        """Test multiplication with mixed int and float inputs."""
        self.assertEqual(multiply(5, 2.5), 12.5)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_divide_integers(self):
        """Test division with integer inputs."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

    def test_divide_floats(self):
        """Test division with float inputs."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0, places=10)
        self.assertAlmostEqual(divide(10.0, 3.0), 3.333333333, places=9)

    def test_divide_mixed_types(self):
        """Test division with mixed int and float inputs."""
        self.assertEqual(divide(10, 2.5), 4.0)
        self.assertEqual(divide(7.5, 3), 2.5)

    def test_divide_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, -3), 0.0)


class TestFactorial(unittest.TestCase):
    """Test suite for factorial function."""

    def test_factorial_zero(self):
        """Test factorial of 0 (boundary case)."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """Test factorial of 1 (boundary case)."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_numbers(self):
        """Test factorial of small positive integers."""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_larger_numbers(self):
        """Test factorial of larger numbers."""
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(15), 1307674368000)

    def test_factorial_negative_input(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("Factorial is not defined for negative numbers", str(context.exception))

        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_non_integer_input(self):
        """Test that non-integer input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            factorial(3.5)
        self.assertIn("Factorial input must be an integer", str(context.exception))

        with self.assertRaises(TypeError):
            factorial("5")


class TestFibonacci(unittest.TestCase):
    """Test suite for Fibonacci function."""

    def test_fibonacci_zero(self):
        """Test Fibonacci of 0 (boundary case)."""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        """Test Fibonacci of 1 (boundary case)."""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test Fibonacci of small positive integers."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)

    def test_fibonacci_larger_numbers(self):
        """Test Fibonacci of larger numbers."""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_negative_input(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertIn("Fibonacci is not defined for negative numbers", str(context.exception))

        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_non_integer_input(self):
        """Test that non-integer input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            fibonacci(5.5)
        self.assertIn("Fibonacci input must be an integer", str(context.exception))

        with self.assertRaises(TypeError):
            fibonacci("10")


class TestIsPrime(unittest.TestCase):
    """Test suite for is_prime function."""

    def test_prime_numbers(self):
        """Test known prime numbers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(97))

    def test_non_prime_numbers(self):
        """Test known non-prime numbers."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(100))

    def test_negative_numbers(self):
        """Test that negative numbers are not prime."""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-7))

    def test_large_primes(self):
        """Test larger prime numbers."""
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(997))
        self.assertTrue(is_prime(7919))

    def test_large_composites(self):
        """Test larger composite numbers."""
        self.assertFalse(is_prime(1000))
        self.assertFalse(is_prime(9999))

    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            is_prime(7.5)
        self.assertIn("Prime check input must be an integer", str(context.exception))

        with self.assertRaises(TypeError):
            is_prime("7")


class TestGCD(unittest.TestCase):
    """Test suite for GCD function."""

    def test_gcd_positive_integers(self):
        """Test GCD with positive integers."""
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(7, 13), 1)

    def test_gcd_with_one(self):
        """Test GCD with one as an input."""
        self.assertEqual(gcd(1, 5), 1)
        self.assertEqual(gcd(17, 1), 1)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_with_zero(self):
        """Test GCD with zero (one zero)."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(7, 0), 7)

    def test_gcd_both_zero(self):
        """Test that GCD of two zeros raises ValueError."""
        with self.assertRaises(ValueError) as context:
            gcd(0, 0)
        self.assertIn("GCD is undefined when both numbers are zero", str(context.exception))

    def test_gcd_negative_numbers(self):
        """Test GCD with negative numbers (should return positive GCD)."""
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)
        self.assertEqual(gcd(-54, 24), 6)

    def test_gcd_same_numbers(self):
        """Test GCD when both numbers are the same."""
        self.assertEqual(gcd(5, 5), 5)
        self.assertEqual(gcd(100, 100), 100)

    def test_gcd_coprime(self):
        """Test GCD of coprime numbers (GCD = 1)."""
        self.assertEqual(gcd(13, 17), 1)
        self.assertEqual(gcd(21, 22), 1)
        self.assertEqual(gcd(35, 64), 1)

    def test_gcd_large_numbers(self):
        """Test GCD with large numbers."""
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(123456, 789012), 12)

    def test_gcd_non_integer_input(self):
        """Test that non-integer input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            gcd(12.5, 8)
        self.assertIn("GCD inputs must be integers", str(context.exception))

        with self.assertRaises(TypeError):
            gcd(12, 8.5)

        with self.assertRaises(TypeError):
            gcd("12", 8)


class TestFloatingPointPrecision(unittest.TestCase):
    """Test suite for floating point precision edge cases."""

    def test_add_floating_point_precision(self):
        """Test addition with floating point precision issues."""
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)

    def test_multiply_small_floats(self):
        """Test multiplication of very small floats."""
        result = multiply(0.0001, 0.0001)
        self.assertAlmostEqual(result, 0.00000001, places=15)

    def test_divide_floating_point_precision(self):
        """Test division with floating point precision."""
        result = divide(1, 3)
        self.assertAlmostEqual(result, 0.333333333333, places=10)

        result = divide(2, 3)
        self.assertAlmostEqual(result, 0.666666666667, places=10)

    def test_large_number_operations(self):
        """Test operations with large numbers."""
        large1 = 10**15
        large2 = 10**15
        self.assertEqual(add(large1, large2), 2 * 10**15)
        self.assertEqual(multiply(10**6, 10**6), 10**12)


class TestReturnTypes(unittest.TestCase):
    """Test suite to verify return types match type hints."""

    def test_add_return_type(self):
        """Test that add returns correct type."""
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(2.5, 3.5), float)
        self.assertIsInstance(add(2, 3.5), float)

    def test_subtract_return_type(self):
        """Test that subtract returns correct type."""
        self.assertIsInstance(subtract(5, 3), int)
        self.assertIsInstance(subtract(5.5, 2.5), float)

    def test_multiply_return_type(self):
        """Test that multiply returns correct type."""
        self.assertIsInstance(multiply(3, 4), int)
        self.assertIsInstance(multiply(3.0, 4.0), float)

    def test_divide_return_type(self):
        """Test that divide always returns float."""
        self.assertIsInstance(divide(10, 2), float)
        self.assertIsInstance(divide(10.0, 2.0), float)

    def test_factorial_return_type(self):
        """Test that factorial returns int."""
        self.assertIsInstance(factorial(5), int)
        self.assertIsInstance(factorial(0), int)

    def test_fibonacci_return_type(self):
        """Test that fibonacci returns int."""
        self.assertIsInstance(fibonacci(10), int)
        self.assertIsInstance(fibonacci(0), int)

    def test_is_prime_return_type(self):
        """Test that is_prime returns bool."""
        self.assertIsInstance(is_prime(7), bool)
        self.assertIsInstance(is_prime(4), bool)

    def test_gcd_return_type(self):
        """Test that gcd returns int."""
        self.assertIsInstance(gcd(12, 8), int)
        self.assertIsInstance(gcd(0, 5), int)


if __name__ == '__main__':
    unittest.main()
