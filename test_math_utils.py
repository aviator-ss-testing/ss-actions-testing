"""
Comprehensive test suite for math_utils module.
"""

import unittest
from math_utils import factorial, fibonacci, is_prime, gcd, lcm, mean, median, mode


class TestMathUtils(unittest.TestCase):
    """Test cases for mathematical utility functions."""

    def test_factorial_normal_cases(self):
        """Test factorial with typical positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_edge_cases(self):
        """Test factorial edge cases."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_factorial_negative_raises_error(self):
        """Test factorial raises ValueError for negative numbers."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_type_error(self):
        """Test factorial raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(None)

    def test_factorial_large_number(self):
        """Test factorial with larger number."""
        self.assertEqual(factorial(7), 5040)

    def test_fibonacci_normal_cases(self):
        """Test fibonacci with typical indices."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_edge_cases(self):
        """Test fibonacci edge cases."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_negative_raises_error(self):
        """Test fibonacci raises ValueError for negative numbers."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_type_error(self):
        """Test fibonacci raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            fibonacci(5.5)
        with self.assertRaises(TypeError):
            fibonacci("5")
        with self.assertRaises(TypeError):
            fibonacci(None)

    def test_fibonacci_sequence(self):
        """Test fibonacci sequence correctness."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_val in enumerate(expected):
            self.assertEqual(fibonacci(i), expected_val)

    def test_is_prime_true_cases(self):
        """Test is_prime with prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in primes:
            self.assertTrue(is_prime(prime), f"{prime} should be prime")

    def test_is_prime_false_cases(self):
        """Test is_prime with non-prime numbers."""
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27]
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} should not be prime")

    def test_is_prime_edge_cases(self):
        """Test is_prime edge cases."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-7))

    def test_is_prime_type_error(self):
        """Test is_prime raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("5")
        with self.assertRaises(TypeError):
            is_prime(None)

    def test_is_prime_large_number(self):
        """Test is_prime with larger numbers."""
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))

    def test_gcd_normal_cases(self):
        """Test gcd with typical integer pairs."""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(7, 13), 1)

    def test_gcd_edge_cases(self):
        """Test gcd edge cases."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_negative_numbers(self):
        """Test gcd with negative numbers."""
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_type_error(self):
        """Test gcd raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            gcd(5.5, 3)
        with self.assertRaises(TypeError):
            gcd(5, 3.3)
        with self.assertRaises(TypeError):
            gcd("5", 3)

    def test_gcd_coprime_numbers(self):
        """Test gcd with coprime numbers."""
        self.assertEqual(gcd(17, 19), 1)
        self.assertEqual(gcd(25, 36), 1)

    def test_lcm_normal_cases(self):
        """Test lcm with typical integer pairs."""
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(7, 5), 35)
        self.assertEqual(lcm(10, 15), 30)

    def test_lcm_edge_cases(self):
        """Test lcm edge cases."""
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(5, 5), 5)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)

    def test_lcm_both_zero_raises_error(self):
        """Test lcm raises ValueError when both arguments are zero."""
        with self.assertRaises(ValueError):
            lcm(0, 0)

    def test_lcm_type_error(self):
        """Test lcm raises TypeError for non-integer input."""
        with self.assertRaises(TypeError):
            lcm(5.5, 3)
        with self.assertRaises(TypeError):
            lcm(5, 3.3)
        with self.assertRaises(TypeError):
            lcm("5", 3)

    def test_lcm_negative_numbers(self):
        """Test lcm with negative numbers."""
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(4, -6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_mean_normal_cases(self):
        """Test mean with typical lists of numbers."""
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5)

    def test_mean_edge_cases(self):
        """Test mean edge cases."""
        self.assertAlmostEqual(mean([5]), 5.0)
        self.assertAlmostEqual(mean([0, 0, 0]), 0.0)
        self.assertAlmostEqual(mean([-1, 0, 1]), 0.0)

    def test_mean_negative_numbers(self):
        """Test mean with negative numbers."""
        self.assertAlmostEqual(mean([-5, -10, -15]), -10.0)
        self.assertAlmostEqual(mean([-2, 2, -4, 4]), 0.0)

    def test_mean_empty_list_raises_error(self):
        """Test mean raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            mean([])

    def test_mean_type_errors(self):
        """Test mean raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            mean("not a list")
        with self.assertRaises(TypeError):
            mean([1, 2, "three"])
        with self.assertRaises(TypeError):
            mean([1, 2, None])

    def test_median_normal_cases(self):
        """Test median with typical lists of numbers."""
        self.assertAlmostEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(median([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(median([5, 1, 3, 2, 4]), 3.0)

    def test_median_edge_cases(self):
        """Test median edge cases."""
        self.assertAlmostEqual(median([5]), 5.0)
        self.assertAlmostEqual(median([1, 2]), 1.5)
        self.assertAlmostEqual(median([0, 0, 0]), 0.0)

    def test_median_unsorted_input(self):
        """Test median correctly sorts unsorted input."""
        self.assertAlmostEqual(median([3, 1, 4, 1, 5, 9, 2, 6]), 3.5)
        self.assertAlmostEqual(median([9, 5, 1, 3, 7]), 5.0)

    def test_median_empty_list_raises_error(self):
        """Test median raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            median([])

    def test_median_type_errors(self):
        """Test median raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            median("not a list")
        with self.assertRaises(TypeError):
            median([1, 2, "three"])
        with self.assertRaises(TypeError):
            median([1, 2, None])

    def test_mode_normal_cases(self):
        """Test mode with typical lists of numbers."""
        self.assertEqual(mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(mode([5, 5, 5, 1, 2, 3]), 5)
        self.assertEqual(mode([1, 1, 2, 2, 2, 3]), 2)

    def test_mode_edge_cases(self):
        """Test mode edge cases."""
        self.assertEqual(mode([5]), 5)
        self.assertEqual(mode([1, 1, 1]), 1)
        self.assertEqual(mode([0, 0, 0, 1]), 0)

    def test_mode_all_unique(self):
        """Test mode when all values appear once."""
        result = mode([1, 2, 3, 4, 5])
        self.assertIn(result, [1, 2, 3, 4, 5])

    def test_mode_empty_list_raises_error(self):
        """Test mode raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            mode([])

    def test_mode_type_errors(self):
        """Test mode raises TypeError for invalid input."""
        with self.assertRaises(TypeError):
            mode("not a list")


if __name__ == '__main__':
    unittest.main()
