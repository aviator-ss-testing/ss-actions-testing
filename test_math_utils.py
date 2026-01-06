"""
Comprehensive test suite for math_utils module.
"""

import unittest
from math_utils import factorial, fibonacci, is_prime, gcd, lcm, mean, median, mode


class TestMathUtils(unittest.TestCase):
    """Test cases for mathematical utility functions."""

    def test_factorial_normal_cases(self):
        """Test factorial with normal positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_edge_cases(self):
        """Test factorial with edge cases."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_invalid_type(self):
        """Test factorial raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(None)

    def test_factorial_negative_input(self):
        """Test factorial raises ValueError for negative inputs."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_fibonacci_normal_cases(self):
        """Test fibonacci with normal positive integers."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_edge_cases(self):
        """Test fibonacci with edge cases."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_invalid_type(self):
        """Test fibonacci raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            fibonacci(5.5)
        with self.assertRaises(TypeError):
            fibonacci("5")
        with self.assertRaises(TypeError):
            fibonacci(None)

    def test_fibonacci_negative_input(self):
        """Test fibonacci raises ValueError for negative inputs."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_is_prime_normal_cases(self):
        """Test is_prime with normal integers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))

    def test_is_prime_composite_numbers(self):
        """Test is_prime correctly identifies composite numbers."""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(1000))

    def test_is_prime_edge_cases(self):
        """Test is_prime with edge cases."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-10))

    def test_is_prime_invalid_type(self):
        """Test is_prime raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("5")
        with self.assertRaises(TypeError):
            is_prime(None)

    def test_gcd_normal_cases(self):
        """Test gcd with normal positive integers."""
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(17, 19), 1)
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_edge_cases(self):
        """Test gcd with edge cases including zero and one."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(1, 5), 1)
        self.assertEqual(gcd(5, 1), 1)

    def test_gcd_negative_numbers(self):
        """Test gcd with negative integers."""
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)

    def test_gcd_invalid_type(self):
        """Test gcd raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            gcd(5.5, 3)
        with self.assertRaises(TypeError):
            gcd(5, 3.3)
        with self.assertRaises(TypeError):
            gcd("5", 3)
        with self.assertRaises(TypeError):
            gcd(None, 5)

    def test_lcm_normal_cases(self):
        """Test lcm with normal positive integers."""
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(15, 20), 60)
        self.assertEqual(lcm(21, 6), 42)

    def test_lcm_edge_cases(self):
        """Test lcm with edge cases including zero and one."""
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(5, 1), 5)

    def test_lcm_both_zero(self):
        """Test lcm raises ValueError when both arguments are zero."""
        with self.assertRaises(ValueError):
            lcm(0, 0)

    def test_lcm_negative_numbers(self):
        """Test lcm with negative integers."""
        self.assertEqual(lcm(-12, 8), 24)
        self.assertEqual(lcm(12, -8), 24)
        self.assertEqual(lcm(-12, -8), 24)

    def test_lcm_invalid_type(self):
        """Test lcm raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            lcm(5.5, 3)
        with self.assertRaises(TypeError):
            lcm(5, 3.3)
        with self.assertRaises(TypeError):
            lcm("5", 3)
        with self.assertRaises(TypeError):
            lcm(None, 5)

    def test_mean_normal_cases(self):
        """Test mean with normal numeric lists."""
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(mean([5.5, 4.5, 6.0]), 5.333333, places=5)
        self.assertAlmostEqual(mean([100]), 100.0)

    def test_mean_edge_cases(self):
        """Test mean with edge cases including zero and negative numbers."""
        self.assertAlmostEqual(mean([0, 0, 0]), 0.0)
        self.assertAlmostEqual(mean([-5, -10, -15]), -10.0)
        self.assertAlmostEqual(mean([-5, 5]), 0.0)
        self.assertAlmostEqual(mean([1]), 1.0)

    def test_mean_empty_list(self):
        """Test mean raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            mean([])

    def test_mean_invalid_type(self):
        """Test mean raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            mean("not a list")
        with self.assertRaises(TypeError):
            mean(123)
        with self.assertRaises(TypeError):
            mean(None)

    def test_mean_non_numeric_values(self):
        """Test mean raises TypeError for lists with non-numeric values."""
        with self.assertRaises(TypeError):
            mean([1, 2, "3"])
        with self.assertRaises(TypeError):
            mean([1, None, 3])

    def test_median_normal_cases(self):
        """Test median with normal numeric lists."""
        self.assertAlmostEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(median([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(median([5, 1, 3, 2, 4]), 3.0)
        self.assertAlmostEqual(median([10]), 10.0)

    def test_median_edge_cases(self):
        """Test median with edge cases including zero and negative numbers."""
        self.assertAlmostEqual(median([0, 0, 0]), 0.0)
        self.assertAlmostEqual(median([-5, -10, -15]), -10.0)
        self.assertAlmostEqual(median([-5, 5]), 0.0)
        self.assertAlmostEqual(median([1]), 1.0)

    def test_median_unsorted_input(self):
        """Test median correctly handles unsorted lists."""
        self.assertAlmostEqual(median([3, 1, 4, 1, 5]), 3.0)
        self.assertAlmostEqual(median([10, 5, 20, 15]), 12.5)

    def test_median_empty_list(self):
        """Test median raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            median([])

    def test_median_invalid_type(self):
        """Test median raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            median("not a list")
        with self.assertRaises(TypeError):
            median(123)
        with self.assertRaises(TypeError):
            median(None)

    def test_median_non_numeric_values(self):
        """Test median raises TypeError for lists with non-numeric values."""
        with self.assertRaises(TypeError):
            median([1, 2, "3"])
        with self.assertRaises(TypeError):
            median([1, None, 3])

    def test_mode_normal_cases(self):
        """Test mode with normal numeric lists."""
        self.assertEqual(mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(mode([5, 5, 5, 1, 2]), 5)
        self.assertEqual(mode([1, 1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(mode([10]), 10)

    def test_mode_edge_cases(self):
        """Test mode with edge cases."""
        self.assertEqual(mode([0, 0, 1, 2]), 0)
        self.assertEqual(mode([-5, -5, -10]), -5)
        self.assertEqual(mode([1]), 1)

    def test_mode_all_same_frequency(self):
        """Test mode when all values have same frequency."""
        result = mode([1, 2, 3])
        self.assertIn(result, [1, 2, 3])

    def test_mode_empty_list(self):
        """Test mode raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            mode([])

    def test_mode_invalid_type(self):
        """Test mode raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            mode("not a list")
        with self.assertRaises(TypeError):
            mode(123)
        with self.assertRaises(TypeError):
            mode(None)


if __name__ == '__main__':
    unittest.main()
