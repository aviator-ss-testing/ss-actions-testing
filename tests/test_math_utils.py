import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from math_utils import factorial, gcd, is_prime, fibonacci, validate_positive


class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_negative_one_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_factorial_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial("5")


class TestGCD(unittest.TestCase):

    def test_gcd_basic(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_coprime(self):
        self.assertEqual(gcd(17, 13), 1)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(42, 42), 42)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_gcd_both_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(1071, 462), 21)

    def test_gcd_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            gcd(5.5, 3)

    def test_gcd_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            gcd("10", 5)


class TestIsPrime(unittest.TestCase):

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_small_primes(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_is_prime_larger_primes(self):
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))

    def test_is_prime_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(100))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            is_prime(-7)

    def test_is_prime_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            is_prime(7.0)

    def test_is_prime_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            is_prime("7")


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_sequence_first_ten(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_value in enumerate(expected):
            with self.subTest(i=i):
                self.assertEqual(fibonacci(i), expected_value)

    def test_fibonacci_larger_number(self):
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)

    def test_fibonacci_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci("5")


class TestValidatePositiveDecorator(unittest.TestCase):

    def test_decorator_preserves_function_name(self):
        self.assertEqual(factorial.__name__, 'factorial')

    def test_decorator_allows_zero(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(fibonacci(0), 0)
        self.assertFalse(is_prime(0))

    def test_decorator_allows_positive_integers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(fibonacci(10), 55)
        self.assertTrue(is_prime(7))

    def test_decorator_rejects_negative_integers(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)
        with self.assertRaises(ValueError):
            is_prime(-7)

    def test_decorator_rejects_negative_floats(self):
        @validate_positive
        def test_func(x):
            return x * 2

        with self.assertRaises(ValueError):
            test_func(-3.5)

    def test_decorator_allows_positive_floats(self):
        @validate_positive
        def test_func(x):
            return x * 2

        self.assertEqual(test_func(3.5), 7.0)


if __name__ == '__main__':
    unittest.main()
