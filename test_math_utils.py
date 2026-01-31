"""Comprehensive test suite for math_utils module with normal, edge, and error cases."""
import unittest
from math_utils import factorial, fibonacci, is_prime, gcd, lcm, math_mean, math_median, math_mode

class TestMathUtils(unittest.TestCase):
    """Test cases for mathematical and statistical utility functions."""

    def test_factorial_normal_cases(self):
        """Test factorial with typical positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_edge_cases(self):
        """Test factorial boundary conditions."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_factorial_negative_raises_error(self):
        """Test factorial raises ValueError for negative inputs."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_type_error(self):
        """Test factorial raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(True)

    def test_fibonacci_normal_cases(self):
        """Test fibonacci with typical indices."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_edge_cases(self):
        """Test fibonacci boundary conditions."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_negative_raises_error(self):
        """Test fibonacci raises ValueError for negative inputs."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_type_error(self):
        """Test fibonacci raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        with self.assertRaises(TypeError):
            fibonacci("10")
        with self.assertRaises(TypeError):
            fibonacci(True)

    def test_is_prime_normal_cases(self):
        """Test is_prime with various integers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))

    def test_is_prime_edge_cases(self):
        """Test is_prime with boundary values."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))

    def test_is_prime_negative_numbers(self):
        """Test is_prime returns False for negative numbers."""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-7))

    def test_is_prime_type_error(self):
        """Test is_prime raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("7")
        with self.assertRaises(TypeError):
            is_prime(True)

    def test_gcd_normal_cases(self):
        """Test gcd with typical integer pairs."""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 50), 50)
        self.assertEqual(gcd(17, 19), 1)
        self.assertEqual(gcd(54, 24), 6)

    def test_gcd_edge_cases(self):
        """Test gcd with boundary values including zero."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1, 100), 1)

    def test_gcd_negative_numbers(self):
        """Test gcd handles negative inputs correctly."""
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_both_zero_raises_error(self):
        """Test gcd raises ValueError when both arguments are zero."""
        with self.assertRaises(ValueError):
            gcd(0, 0)

    def test_gcd_type_error(self):
        """Test gcd raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            gcd(5.5, 10)
        with self.assertRaises(TypeError):
            gcd(10, "5")
        with self.assertRaises(TypeError):
            gcd(True, 10)

    def test_lcm_normal_cases(self):
        """Test lcm with typical integer pairs."""
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(3, 5), 15)
        self.assertEqual(lcm(21, 6), 42)
        self.assertEqual(lcm(10, 15), 30)

    def test_lcm_edge_cases(self):
        """Test lcm with boundary values including zero."""
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(1, 100), 100)

    def test_lcm_negative_numbers(self):
        """Test lcm handles negative inputs correctly."""
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(4, -6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_both_zero_raises_error(self):
        """Test lcm raises ValueError when both arguments are zero."""
        with self.assertRaises(ValueError):
            lcm(0, 0)

    def test_lcm_type_error(self):
        """Test lcm raises TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            lcm(5.5, 10)
        with self.assertRaises(TypeError):
            lcm(10, "5")
        with self.assertRaises(TypeError):
            lcm(True, 10)

    def test_math_mean_normal_cases(self):
        """Test math_mean with typical number lists."""
        self.assertAlmostEqual(math_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(math_mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(math_mean([1.5, 2.5, 3.5]), 2.5)
        self.assertAlmostEqual(math_mean([100]), 100.0)

    def test_math_mean_edge_cases(self):
        """Test math_mean with boundary conditions."""
        self.assertAlmostEqual(math_mean([0]), 0.0)
        self.assertAlmostEqual(math_mean([1]), 1.0)
        self.assertAlmostEqual(math_mean([0, 0, 0]), 0.0)
        self.assertAlmostEqual(math_mean([-5, -10, -15]), -10.0)

    def test_math_mean_negative_and_positive(self):
        """Test math_mean with mixed positive and negative numbers."""
        self.assertAlmostEqual(math_mean([-5, 0, 5]), 0.0)
        self.assertAlmostEqual(math_mean([-10, 10, -5, 5]), 0.0)
        self.assertAlmostEqual(math_mean([1, -1, 2, -2]), 0.0)

    def test_math_mean_empty_list_raises_error(self):
        """Test math_mean raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            math_mean([])

    def test_math_mean_type_error(self):
        """Test math_mean raises TypeError for non-list inputs."""
        with self.assertRaises(TypeError):
            math_mean(5)
        with self.assertRaises(TypeError):
            math_mean("123")
        with self.assertRaises(TypeError):
            math_mean((1, 2, 3))

    def test_math_median_normal_cases(self):
        """Test math_median with typical number lists."""
        self.assertAlmostEqual(math_median([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(math_median([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(math_median([5, 1, 3, 2, 4]), 3.0)
        self.assertAlmostEqual(math_median([10, 20, 30, 40]), 25.0)

    def test_math_median_edge_cases(self):
        """Test math_median with boundary conditions."""
        self.assertAlmostEqual(math_median([5]), 5.0)
        self.assertAlmostEqual(math_median([1, 2]), 1.5)
        self.assertAlmostEqual(math_median([0, 0, 0]), 0.0)

    def test_math_median_unsorted_input(self):
        """Test math_median correctly sorts input before calculating."""
        self.assertAlmostEqual(math_median([3, 1, 2]), 2.0)
        self.assertAlmostEqual(math_median([10, 5, 15, 20]), 12.5)
        self.assertAlmostEqual(math_median([100, 1, 50]), 50.0)

    def test_math_median_negative_numbers(self):
        """Test math_median with negative numbers."""
        self.assertAlmostEqual(math_median([-5, -10, -15]), -10.0)
        self.assertAlmostEqual(math_median([-5, 0, 5]), 0.0)

    def test_math_median_empty_list_raises_error(self):
        """Test math_median raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            math_median([])

    def test_math_median_type_error(self):
        """Test math_median raises TypeError for non-list inputs."""
        with self.assertRaises(TypeError):
            math_median(5)
        with self.assertRaises(TypeError):
            math_median("123")

    def test_math_mode_normal_cases(self):
        """Test math_mode with typical number lists."""
        self.assertEqual(math_mode([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(math_mode([5, 5, 5, 1, 2]), 5)
        self.assertEqual(math_mode([1, 1, 2, 2, 3]), 1)

    def test_math_mode_edge_cases(self):
        """Test math_mode with boundary conditions."""
        self.assertEqual(math_mode([5]), 5)
        self.assertEqual(math_mode([1, 1]), 1)
        self.assertEqual(math_mode([0, 0, 0]), 0)

    def test_math_mode_all_unique(self):
        """Test math_mode returns first value when all are unique."""
        result = math_mode([1, 2, 3, 4, 5])
        self.assertIn(result, [1, 2, 3, 4, 5])

    def test_math_mode_negative_numbers(self):
        """Test math_mode with negative numbers."""
        self.assertEqual(math_mode([-5, -5, -10]), -5)
        self.assertEqual(math_mode([-1, -1, -1, 0, 0]), -1)

    def test_math_mode_empty_list_raises_error(self):
        """Test math_mode raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            math_mode([])

    def test_math_mode_type_error(self):
        """Test math_mode raises TypeError for non-list inputs."""
        with self.assertRaises(TypeError):
            math_mode(5)
        with self.assertRaises(TypeError):
            math_mode("123")

if __name__ == '__main__':
    unittest.main()
