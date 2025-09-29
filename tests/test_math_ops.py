"""Test cases for mathematical operations module."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math_ops


class TestBasicArithmetic(unittest.TestCase):
    """Test cases for basic arithmetic operations."""

    def test_add_integers(self):
        self.assertEqual(math_ops.add(2, 3), 5)
        self.assertEqual(math_ops.add(-5, 3), -2)
        self.assertEqual(math_ops.add(0, 0), 0)
        self.assertEqual(math_ops.add(-10, -20), -30)

    def test_add_floats(self):
        self.assertAlmostEqual(math_ops.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(math_ops.add(-1.5, 1.5), 0.0)
        self.assertAlmostEqual(math_ops.add(0.1, 0.2), 0.3)

    def test_add_mixed_types(self):
        self.assertAlmostEqual(math_ops.add(5, 2.5), 7.5)
        self.assertAlmostEqual(math_ops.add(2.5, 5), 7.5)

    def test_add_large_numbers(self):
        self.assertEqual(math_ops.add(10**15, 10**15), 2 * 10**15)
        self.assertEqual(math_ops.add(999999999999, 1), 1000000000000)

    def test_subtract_integers(self):
        self.assertEqual(math_ops.subtract(5, 3), 2)
        self.assertEqual(math_ops.subtract(3, 5), -2)
        self.assertEqual(math_ops.subtract(0, 5), -5)
        self.assertEqual(math_ops.subtract(-3, -5), 2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(math_ops.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(math_ops.subtract(0.3, 0.1), 0.2)

    def test_subtract_mixed_types(self):
        self.assertAlmostEqual(math_ops.subtract(10, 3.5), 6.5)
        self.assertAlmostEqual(math_ops.subtract(7.5, 2), 5.5)

    def test_multiply_integers(self):
        self.assertEqual(math_ops.multiply(3, 4), 12)
        self.assertEqual(math_ops.multiply(-3, 4), -12)
        self.assertEqual(math_ops.multiply(-3, -4), 12)
        self.assertEqual(math_ops.multiply(0, 100), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(math_ops.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(math_ops.multiply(0.1, 0.1), 0.01)

    def test_multiply_large_numbers(self):
        self.assertEqual(math_ops.multiply(10**10, 10**10), 10**20)

    def test_divide_integers(self):
        self.assertAlmostEqual(math_ops.divide(10, 2), 5.0)
        self.assertAlmostEqual(math_ops.divide(7, 2), 3.5)
        self.assertAlmostEqual(math_ops.divide(-10, 2), -5.0)
        self.assertAlmostEqual(math_ops.divide(-10, -2), 5.0)

    def test_divide_floats(self):
        self.assertAlmostEqual(math_ops.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(math_ops.divide(1.0, 3.0), 0.333333, places=5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            math_ops.divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            math_ops.divide(0, 0)
        with self.assertRaises(ZeroDivisionError):
            math_ops.divide(-10, 0)

    def test_divide_zero_by_number(self):
        self.assertAlmostEqual(math_ops.divide(0, 5), 0.0)
        self.assertAlmostEqual(math_ops.divide(0, -5), 0.0)


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function."""

    def test_factorial_base_cases(self):
        self.assertEqual(math_ops.factorial(0), 1)
        self.assertEqual(math_ops.factorial(1), 1)

    def test_factorial_small_numbers(self):
        self.assertEqual(math_ops.factorial(2), 2)
        self.assertEqual(math_ops.factorial(3), 6)
        self.assertEqual(math_ops.factorial(4), 24)
        self.assertEqual(math_ops.factorial(5), 120)
        self.assertEqual(math_ops.factorial(10), 3628800)

    def test_factorial_large_numbers(self):
        self.assertEqual(math_ops.factorial(20), 2432902008176640000)

    def test_factorial_negative_input(self):
        with self.assertRaises(ValueError):
            math_ops.factorial(-1)
        with self.assertRaises(ValueError):
            math_ops.factorial(-10)

    def test_factorial_non_integer_input(self):
        with self.assertRaises(TypeError):
            math_ops.factorial(5.5)
        with self.assertRaises(TypeError):
            math_ops.factorial("5")
        with self.assertRaises(TypeError):
            math_ops.factorial(None)


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci function."""

    def test_fibonacci_base_cases(self):
        self.assertEqual(math_ops.fibonacci(0), 0)
        self.assertEqual(math_ops.fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(math_ops.fibonacci(2), 1)
        self.assertEqual(math_ops.fibonacci(3), 2)
        self.assertEqual(math_ops.fibonacci(4), 3)
        self.assertEqual(math_ops.fibonacci(5), 5)
        self.assertEqual(math_ops.fibonacci(6), 8)
        self.assertEqual(math_ops.fibonacci(7), 13)
        self.assertEqual(math_ops.fibonacci(10), 55)

    def test_fibonacci_large_numbers(self):
        self.assertEqual(math_ops.fibonacci(20), 6765)
        self.assertEqual(math_ops.fibonacci(30), 832040)

    def test_fibonacci_negative_input(self):
        with self.assertRaises(ValueError):
            math_ops.fibonacci(-1)
        with self.assertRaises(ValueError):
            math_ops.fibonacci(-10)

    def test_fibonacci_non_integer_input(self):
        with self.assertRaises(TypeError):
            math_ops.fibonacci(5.5)
        with self.assertRaises(TypeError):
            math_ops.fibonacci("5")
        with self.assertRaises(TypeError):
            math_ops.fibonacci(None)


class TestIsPrime(unittest.TestCase):
    """Test cases for is_prime function."""

    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in primes:
            self.assertTrue(math_ops.is_prime(prime), f"{prime} should be prime")

    def test_non_prime_numbers(self):
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
        for num in non_primes:
            self.assertFalse(math_ops.is_prime(num), f"{num} should not be prime")

    def test_edge_cases(self):
        self.assertFalse(math_ops.is_prime(0))
        self.assertFalse(math_ops.is_prime(1))
        self.assertFalse(math_ops.is_prime(-1))
        self.assertFalse(math_ops.is_prime(-5))

    def test_large_primes(self):
        self.assertTrue(math_ops.is_prime(97))
        self.assertTrue(math_ops.is_prime(101))
        self.assertTrue(math_ops.is_prime(997))

    def test_large_non_primes(self):
        self.assertFalse(math_ops.is_prime(100))
        self.assertFalse(math_ops.is_prime(1000))
        self.assertFalse(math_ops.is_prime(10000))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            math_ops.is_prime(5.5)
        with self.assertRaises(TypeError):
            math_ops.is_prime("5")
        with self.assertRaises(TypeError):
            math_ops.is_prime(None)


class TestGCD(unittest.TestCase):
    """Test cases for GCD function."""

    def test_gcd_basic(self):
        self.assertEqual(math_ops.gcd(12, 8), 4)
        self.assertEqual(math_ops.gcd(54, 24), 6)
        self.assertEqual(math_ops.gcd(48, 18), 6)

    def test_gcd_coprime(self):
        self.assertEqual(math_ops.gcd(17, 19), 1)
        self.assertEqual(math_ops.gcd(13, 7), 1)

    def test_gcd_same_numbers(self):
        self.assertEqual(math_ops.gcd(5, 5), 5)
        self.assertEqual(math_ops.gcd(100, 100), 100)

    def test_gcd_with_zero(self):
        self.assertEqual(math_ops.gcd(0, 5), 5)
        self.assertEqual(math_ops.gcd(5, 0), 5)

    def test_gcd_both_zero(self):
        with self.assertRaises(ValueError):
            math_ops.gcd(0, 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(math_ops.gcd(-12, 8), 4)
        self.assertEqual(math_ops.gcd(12, -8), 4)
        self.assertEqual(math_ops.gcd(-12, -8), 4)

    def test_gcd_large_numbers(self):
        self.assertEqual(math_ops.gcd(1071, 462), 21)
        self.assertEqual(math_ops.gcd(123456, 789012), 12)

    def test_gcd_non_integer_input(self):
        with self.assertRaises(TypeError):
            math_ops.gcd(5.5, 3)
        with self.assertRaises(TypeError):
            math_ops.gcd(5, 3.5)
        with self.assertRaises(TypeError):
            math_ops.gcd("5", 3)


class TestTypeCorrectness(unittest.TestCase):
    """Test return value types match type hints."""

    def test_add_return_types(self):
        self.assertIsInstance(math_ops.add(2, 3), int)
        self.assertIsInstance(math_ops.add(2.0, 3.0), float)
        self.assertIsInstance(math_ops.add(2, 3.0), float)

    def test_divide_return_type(self):
        self.assertIsInstance(math_ops.divide(10, 2), float)
        self.assertIsInstance(math_ops.divide(10, 3), float)

    def test_factorial_return_type(self):
        self.assertIsInstance(math_ops.factorial(5), int)

    def test_fibonacci_return_type(self):
        self.assertIsInstance(math_ops.fibonacci(10), int)

    def test_is_prime_return_type(self):
        self.assertIsInstance(math_ops.is_prime(5), bool)
        self.assertIsInstance(math_ops.is_prime(4), bool)

    def test_gcd_return_type(self):
        self.assertIsInstance(math_ops.gcd(12, 8), int)


class TestFloatingPointPrecision(unittest.TestCase):
    """Test floating point precision edge cases."""

    def test_small_float_addition(self):
        result = math_ops.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)

    def test_small_float_subtraction(self):
        result = math_ops.subtract(0.3, 0.1)
        self.assertAlmostEqual(result, 0.2, places=10)

    def test_small_float_multiplication(self):
        result = math_ops.multiply(0.1, 0.1)
        self.assertAlmostEqual(result, 0.01, places=10)

    def test_small_float_division(self):
        result = math_ops.divide(1.0, 3.0)
        self.assertAlmostEqual(result, 0.333333333333, places=10)

    def test_very_large_floats(self):
        large = 1e100
        result = math_ops.add(large, large)
        self.assertAlmostEqual(result, 2e100)

    def test_very_small_floats(self):
        small = 1e-100
        result = math_ops.multiply(small, 2)
        self.assertAlmostEqual(result, 2e-100)


if __name__ == '__main__':
    unittest.main()