"""
Unit tests for mathematical operations module.

Tests cover basic arithmetic, advanced mathematical functions,
edge cases, and error handling.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_ops import add, subtract, multiply, divide, factorial, fibonacci, is_prime, gcd


class TestBasicArithmetic(unittest.TestCase):
    """Test cases for basic arithmetic operations."""

    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-10, -5), -15)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(add(-1.5, 0.5), -1.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_add_mixed_types(self):
        self.assertEqual(add(5, 2.5), 7.5)
        self.assertEqual(add(3.5, 2), 5.5)

    def test_subtract_integers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(subtract(1.5, 3.7), -2.2)

    def test_subtract_mixed_types(self):
        self.assertEqual(subtract(10, 2.5), 7.5)
        self.assertEqual(subtract(7.5, 2), 5.5)

    def test_multiply_integers(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-5, -3), 15)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(multiply(-1.5, 2.0), -3.0)

    def test_multiply_mixed_types(self):
        self.assertEqual(multiply(5, 2.5), 12.5)
        self.assertEqual(multiply(3.0, 4), 12.0)

    def test_divide_integers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide(1.0, 4.0), 0.25)

    def test_divide_mixed_types(self):
        self.assertEqual(divide(10.0, 4), 2.5)
        self.assertEqual(divide(9, 2.0), 4.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)


class TestAdvancedMath(unittest.TestCase):
    """Test cases for advanced mathematical functions."""

    def test_factorial_base_cases(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_numbers(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_larger_numbers(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(12), 479001600)

    def test_factorial_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_medium_numbers(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_larger_numbers(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(25), 75025)

    def test_fibonacci_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_non_integer_input(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)
        with self.assertRaises(TypeError):
            fibonacci("10")

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))

    def test_is_prime_small_primes(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_is_prime_small_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))

    def test_is_prime_larger_primes(self):
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))

    def test_is_prime_larger_composites(self):
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(121))
        self.assertFalse(is_prime(144))

    def test_is_prime_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("7")

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(7, 5), 1)
        self.assertEqual(gcd(100, 50), 50)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 123), 123)

    def test_gcd_both_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)
        self.assertEqual(gcd(-54, 24), 6)

    def test_gcd_equal_numbers(self):
        self.assertEqual(gcd(5, 5), 5)
        self.assertEqual(gcd(42, 42), 42)
        self.assertEqual(gcd(-7, -7), 7)

    def test_gcd_coprime_numbers(self):
        self.assertEqual(gcd(13, 17), 1)
        self.assertEqual(gcd(25, 36), 1)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(3918, 2142), 6)

    def test_gcd_non_integer_input(self):
        with self.assertRaises(TypeError):
            gcd(5.5, 3)
        with self.assertRaises(TypeError):
            gcd(10, 2.5)
        with self.assertRaises(TypeError):
            gcd("12", 8)


class TestMathematicalEdgeCases(unittest.TestCase):
    """Test cases for edge cases in mathematical operations."""

    def test_large_numbers_arithmetic(self):
        large_num = 10**15
        self.assertEqual(add(large_num, large_num), 2 * large_num)
        self.assertEqual(multiply(large_num, 2), 2 * large_num)

    def test_floating_point_precision(self):
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)

        result = divide(1, 3)
        self.assertAlmostEqual(result, 0.333333333333, places=10)

    def test_negative_inputs_arithmetic(self):
        self.assertEqual(add(-100, -200), -300)
        self.assertEqual(multiply(-5, -10), 50)
        self.assertEqual(divide(-10, 2), -5.0)

    def test_zero_handling(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(multiply(1000, 0), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_factorial_boundary(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_fibonacci_boundary(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)


class TestReturnTypes(unittest.TestCase):
    """Test cases to verify correct return types."""

    def test_add_return_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(2.5, 3.5), float)

    def test_subtract_return_type(self):
        self.assertIsInstance(subtract(5, 2), int)
        self.assertIsInstance(subtract(5.5, 2.5), float)

    def test_multiply_return_type(self):
        self.assertIsInstance(multiply(3, 4), int)
        self.assertIsInstance(multiply(3.0, 4.0), float)

    def test_divide_return_type(self):
        result = divide(10, 2)
        self.assertIsInstance(result, float)

    def test_factorial_return_type(self):
        self.assertIsInstance(factorial(5), int)

    def test_fibonacci_return_type(self):
        self.assertIsInstance(fibonacci(10), int)

    def test_is_prime_return_type(self):
        self.assertIsInstance(is_prime(7), bool)

    def test_gcd_return_type(self):
        self.assertIsInstance(gcd(12, 8), int)


if __name__ == '__main__':
    unittest.main()
