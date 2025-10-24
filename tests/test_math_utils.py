"""Comprehensive tests for math_utils module."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.math_utils import factorial, fibonacci, is_prime, gcd, lcm, mean, median


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function."""

    def test_factorial_positive_integers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("negative", str(context.exception).lower())

        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_non_integer_raises_error(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

        with self.assertRaises(TypeError):
            factorial("5")


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci function."""

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_sequence_correctness(self):
        sequence = [fibonacci(i) for i in range(10)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(sequence, expected)

    def test_fibonacci_larger_numbers(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertIn("negative", str(context.exception).lower())

    def test_fibonacci_non_integer_raises_error(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)

        with self.assertRaises(TypeError):
            fibonacci("5")


class TestIsPrime(unittest.TestCase):
    """Test cases for is_prime function."""

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(15))

    def test_edge_case_zero(self):
        self.assertFalse(is_prime(0))

    def test_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_edge_case_negative(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-2))

    def test_large_prime(self):
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))

    def test_non_integer_raises_error(self):
        with self.assertRaises(TypeError):
            is_prime(5.5)

        with self.assertRaises(TypeError):
            is_prime("5")


class TestGcd(unittest.TestCase):
    """Test cases for gcd function."""

    def test_gcd_basic_cases(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(17, 19), 1)
        self.assertEqual(gcd(12, 8), 4)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 7), 7)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(15, 15), 15)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_with_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_commutative(self):
        self.assertEqual(gcd(48, 18), gcd(18, 48))
        self.assertEqual(gcd(100, 25), gcd(25, 100))

    def test_gcd_non_integer_raises_error(self):
        with self.assertRaises(TypeError):
            gcd(5.5, 3)

        with self.assertRaises(TypeError):
            gcd(5, "3")


class TestLcm(unittest.TestCase):
    """Test cases for lcm function."""

    def test_lcm_basic_cases(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(3, 5), 15)
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(7, 5), 35)

    def test_lcm_with_zero(self):
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 7), 0)

    def test_lcm_both_zero_raises_error(self):
        with self.assertRaises(ValueError) as context:
            lcm(0, 0)
        self.assertIn("undefined", str(context.exception).lower())

    def test_lcm_same_numbers(self):
        self.assertEqual(lcm(15, 15), 15)
        self.assertEqual(lcm(1, 1), 1)

    def test_lcm_with_one(self):
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(10, 1), 10)

    def test_lcm_with_negative_numbers(self):
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(4, -6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_correctness(self):
        result = lcm(12, 18)
        self.assertEqual(result, 36)
        self.assertEqual(result % 12, 0)
        self.assertEqual(result % 18, 0)

    def test_lcm_non_integer_raises_error(self):
        with self.assertRaises(TypeError):
            lcm(5.5, 3)

        with self.assertRaises(TypeError):
            lcm(5, "3")


class TestMean(unittest.TestCase):
    """Test cases for mean function."""

    def test_mean_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            mean([])
        self.assertIn("at least one", str(context.exception).lower())

    def test_mean_single_value(self):
        self.assertEqual(mean([5]), 5.0)
        self.assertEqual(mean([10]), 10.0)
        self.assertEqual(mean([-3]), -3.0)

    def test_mean_multiple_values(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20, 30]), 20.0)
        self.assertEqual(mean([2, 4, 6, 8]), 5.0)

    def test_mean_with_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3]), -2.0)
        self.assertEqual(mean([-5, 5]), 0.0)

    def test_mean_with_floats(self):
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5)
        self.assertAlmostEqual(mean([0.1, 0.2, 0.3]), 0.2)

    def test_mean_non_list_raises_error(self):
        with self.assertRaises(TypeError):
            mean((1, 2, 3))

        with self.assertRaises(TypeError):
            mean(5)

    def test_mean_non_numeric_values_raises_error(self):
        with self.assertRaises(TypeError):
            mean([1, 2, "3"])

        with self.assertRaises(TypeError):
            mean(["a", "b", "c"])


class TestMedian(unittest.TestCase):
    """Test cases for median function."""

    def test_median_empty_list_raises_error(self):
        with self.assertRaises(ValueError) as context:
            median([])
        self.assertIn("at least one", str(context.exception).lower())

    def test_median_single_value(self):
        self.assertEqual(median([5]), 5)
        self.assertEqual(median([10]), 10)

    def test_median_odd_length_lists(self):
        self.assertEqual(median([1, 2, 3]), 2)
        self.assertEqual(median([5, 1, 3]), 3)
        self.assertEqual(median([10, 20, 30, 40, 50]), 30)

    def test_median_even_length_lists(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_median_unsorted_list(self):
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([5, 2, 8, 1]), 3.5)

    def test_median_with_negative_numbers(self):
        self.assertEqual(median([-1, -2, -3]), -2)
        self.assertEqual(median([-5, 5, 0]), 0)

    def test_median_with_duplicates(self):
        self.assertEqual(median([1, 2, 2, 3]), 2.0)
        self.assertEqual(median([5, 5, 5]), 5)

    def test_median_correct_ordering(self):
        result = median([10, 1, 5, 3, 8])
        self.assertEqual(result, 5)

    def test_median_non_list_raises_error(self):
        with self.assertRaises(TypeError):
            median((1, 2, 3))

        with self.assertRaises(TypeError):
            median(5)

    def test_median_non_numeric_values_raises_error(self):
        with self.assertRaises(TypeError):
            median([1, 2, "3"])

        with self.assertRaises(TypeError):
            median([1, "b", 3])


if __name__ == '__main__':
    unittest.main()
