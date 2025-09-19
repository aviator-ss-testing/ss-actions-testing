"""
Comprehensive test suite for math_ops module using unittest framework.
Tests cover normal cases, edge cases, error conditions, and performance validation.
"""

import unittest
import time
import math
from math_ops import (
    add, subtract, multiply, divide,
    factorial, fibonacci, prime_checker, gcd, lcm,
    mean, median, mode, standard_deviation,
    area_circle, area_rectangle, area_triangle, pythagorean_theorem
)


class TestMathOperations(unittest.TestCase):
    """Test case class for all mathematical operations."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sample_data = [1, 2, 3, 4, 5]
        self.empty_data = []
        self.single_item_data = [42]
        self.duplicate_data = [1, 2, 2, 3, 3, 3]
        self.float_data = [1.5, 2.5, 3.5, 4.5]
        self.mixed_data = [1, 2.5, 3, 4.5, 5]

    # Basic arithmetic function tests
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, 5), -5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(20, 10), 10)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 7), 35)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_by_one(self):
        """Test multiplication by one."""
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(1, 1), 1)

    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(10, 5), 2)
        self.assertAlmostEqual(divide(7, 3), 2.333333333333333, places=7)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-6, -2), 3)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(6, -2), -3)

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Division by zero is not allowed")

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -3), 0)

    # Advanced math function tests
    def test_factorial_positive_integers(self):
        """Test factorial with positive integers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers")

    def test_factorial_non_integer_raises_error(self):
        """Test that factorial of non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(5.5)
        self.assertEqual(str(context.exception), "Input must be an integer")

    def test_fibonacci_sequence(self):
        """Test Fibonacci sequence with parametrized cases."""
        fibonacci_cases = [
            (0, 0), (1, 1), (2, 1), (3, 2), (4, 3),
            (5, 5), (6, 8), (7, 13), (8, 21), (10, 55)
        ]
        for n, expected in fibonacci_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)

    def test_fibonacci_negative_raises_error(self):
        """Test that Fibonacci of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Fibonacci is not defined for negative numbers")

    def test_fibonacci_non_integer_raises_error(self):
        """Test that Fibonacci of non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            fibonacci(5.5)
        self.assertEqual(str(context.exception), "Input must be an integer")

    def test_prime_checker_known_primes(self):
        """Test prime checker with known prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(prime_checker(prime))

    def test_prime_checker_known_composites(self):
        """Test prime checker with known composite numbers."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]
        for composite in composites:
            with self.subTest(composite=composite):
                self.assertFalse(prime_checker(composite))

    def test_prime_checker_edge_cases(self):
        """Test prime checker with edge cases."""
        self.assertFalse(prime_checker(0))
        self.assertFalse(prime_checker(1))
        self.assertFalse(prime_checker(-5))

    def test_prime_checker_non_integer_raises_error(self):
        """Test that prime checker with non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            prime_checker(5.5)
        self.assertEqual(str(context.exception), "Input must be an integer")

    def test_gcd_positive_numbers(self):
        """Test GCD with positive numbers."""
        gcd_cases = [
            (12, 18, 6), (15, 25, 5), (17, 19, 1),
            (24, 36, 12), (100, 75, 25)
        ]
        for a, b, expected in gcd_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), expected)

    def test_gcd_negative_numbers(self):
        """Test GCD with negative numbers."""
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(12, -18), 6)
        self.assertEqual(gcd(-12, -18), 6)

    def test_gcd_with_zero(self):
        """Test GCD with zero."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_non_integer_raises_error(self):
        """Test that GCD with non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            gcd(5.5, 3)
        self.assertEqual(str(context.exception), "Both inputs must be integers")

    def test_lcm_positive_numbers(self):
        """Test LCM with positive numbers."""
        lcm_cases = [
            (4, 6, 12), (15, 25, 75), (17, 19, 323),
            (12, 18, 36), (3, 5, 15)
        ]
        for a, b, expected in lcm_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(lcm(a, b), expected)

    def test_lcm_with_zero(self):
        """Test LCM with zero."""
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_negative_numbers(self):
        """Test LCM with negative numbers."""
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(4, -6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_non_integer_raises_error(self):
        """Test that LCM with non-integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            lcm(5.5, 3)
        self.assertEqual(str(context.exception), "Both inputs must be integers")

    # Statistical function tests
    def test_mean_integers(self):
        """Test mean calculation with integers."""
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20, 30]), 20.0)

    def test_mean_floats(self):
        """Test mean calculation with floats."""
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5, places=7)

    def test_mean_mixed_numbers(self):
        """Test mean calculation with mixed integers and floats."""
        self.assertAlmostEqual(mean([1, 2.5, 3, 4.5]), 2.75, places=7)

    def test_mean_empty_list_raises_error(self):
        """Test that mean of empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            mean([])
        self.assertEqual(str(context.exception), "Cannot calculate mean of empty list")

    def test_mean_non_numbers_raises_error(self):
        """Test that mean with non-numbers raises ValueError."""
        with self.assertRaises(ValueError) as context:
            mean([1, 2, "3"])
        self.assertEqual(str(context.exception), "All elements must be numbers")

    def test_median_odd_length(self):
        """Test median with odd-length lists."""
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([10, 5, 15]), 10.0)

    def test_median_even_length(self):
        """Test median with even-length lists."""
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20, 30, 40]), 25.0)

    def test_median_single_element(self):
        """Test median with single element."""
        self.assertEqual(median([42]), 42.0)

    def test_median_unsorted_data(self):
        """Test median with unsorted data."""
        self.assertEqual(median([5, 1, 3, 2, 4]), 3.0)

    def test_median_empty_list_raises_error(self):
        """Test that median of empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            median([])
        self.assertEqual(str(context.exception), "Cannot calculate median of empty list")

    def test_mode_single_mode(self):
        """Test mode with single most frequent value."""
        self.assertEqual(mode([1, 2, 2, 3]), [2])
        self.assertEqual(mode([1, 1, 1, 2, 3]), [1])

    def test_mode_multiple_modes(self):
        """Test mode with multiple most frequent values."""
        result = mode([1, 1, 2, 2, 3])
        self.assertEqual(sorted(result), [1, 2])

    def test_mode_all_unique(self):
        """Test mode with all unique values."""
        result = mode([1, 2, 3, 4])
        self.assertEqual(sorted(result), [1, 2, 3, 4])

    def test_mode_empty_list_raises_error(self):
        """Test that mode of empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            mode([])
        self.assertEqual(str(context.exception), "Cannot calculate mode of empty list")

    def test_standard_deviation_known_values(self):
        """Test standard deviation with known values."""
        self.assertAlmostEqual(standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]), 2.0, places=7)
        self.assertEqual(standard_deviation([1]), 0.0)

    def test_standard_deviation_identical_values(self):
        """Test standard deviation with identical values."""
        self.assertEqual(standard_deviation([5, 5, 5, 5]), 0.0)

    def test_standard_deviation_empty_list_raises_error(self):
        """Test that standard deviation of empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            standard_deviation([])
        self.assertEqual(str(context.exception), "Cannot calculate standard deviation of empty list")

    # Geometric function tests
    def test_area_circle_positive_radius(self):
        """Test circle area calculation with positive radius."""
        self.assertAlmostEqual(area_circle(1), math.pi, places=7)
        self.assertAlmostEqual(area_circle(2), 4 * math.pi, places=7)
        self.assertAlmostEqual(area_circle(0.5), 0.25 * math.pi, places=7)

    def test_area_circle_zero_radius(self):
        """Test circle area calculation with zero radius."""
        self.assertEqual(area_circle(0), 0)

    def test_area_circle_negative_radius_raises_error(self):
        """Test that circle area with negative radius raises ValueError."""
        with self.assertRaises(ValueError) as context:
            area_circle(-1)
        self.assertEqual(str(context.exception), "Radius cannot be negative")

    def test_area_circle_non_number_raises_error(self):
        """Test that circle area with non-number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            area_circle("5")
        self.assertEqual(str(context.exception), "Radius must be a number")

    def test_area_rectangle_positive_dimensions(self):
        """Test rectangle area calculation with positive dimensions."""
        self.assertEqual(area_rectangle(3, 4), 12)
        self.assertEqual(area_rectangle(5.5, 2), 11)
        self.assertEqual(area_rectangle(10, 10), 100)

    def test_area_rectangle_zero_dimension(self):
        """Test rectangle area calculation with zero dimension."""
        self.assertEqual(area_rectangle(0, 5), 0)
        self.assertEqual(area_rectangle(5, 0), 0)
        self.assertEqual(area_rectangle(0, 0), 0)

    def test_area_rectangle_negative_dimension_raises_error(self):
        """Test that rectangle area with negative dimension raises ValueError."""
        with self.assertRaises(ValueError) as context:
            area_rectangle(-1, 5)
        self.assertEqual(str(context.exception), "Length and width cannot be negative")

    def test_area_triangle_positive_dimensions(self):
        """Test triangle area calculation with positive dimensions."""
        self.assertEqual(area_triangle(6, 4), 12)
        self.assertEqual(area_triangle(5, 8), 20)
        self.assertAlmostEqual(area_triangle(3.5, 2.5), 4.375, places=7)

    def test_area_triangle_zero_dimension(self):
        """Test triangle area calculation with zero dimension."""
        self.assertEqual(area_triangle(0, 5), 0)
        self.assertEqual(area_triangle(5, 0), 0)

    def test_area_triangle_negative_dimension_raises_error(self):
        """Test that triangle area with negative dimension raises ValueError."""
        with self.assertRaises(ValueError) as context:
            area_triangle(-1, 5)
        self.assertEqual(str(context.exception), "Base and height cannot be negative")

    def test_pythagorean_theorem_known_values(self):
        """Test Pythagorean theorem with known values."""
        self.assertAlmostEqual(pythagorean_theorem(3, 4), 5.0, places=7)
        self.assertAlmostEqual(pythagorean_theorem(5, 12), 13.0, places=7)
        self.assertAlmostEqual(pythagorean_theorem(8, 15), 17.0, places=7)

    def test_pythagorean_theorem_equal_sides(self):
        """Test Pythagorean theorem with equal sides."""
        self.assertAlmostEqual(pythagorean_theorem(1, 1), math.sqrt(2), places=7)
        self.assertAlmostEqual(pythagorean_theorem(5, 5), 5 * math.sqrt(2), places=7)

    def test_pythagorean_theorem_zero_side(self):
        """Test Pythagorean theorem with zero side."""
        self.assertEqual(pythagorean_theorem(0, 5), 5.0)
        self.assertEqual(pythagorean_theorem(3, 0), 3.0)

    def test_pythagorean_theorem_negative_side_raises_error(self):
        """Test that Pythagorean theorem with negative side raises ValueError."""
        with self.assertRaises(ValueError) as context:
            pythagorean_theorem(-1, 5)
        self.assertEqual(str(context.exception), "Side lengths cannot be negative")

    # Performance validation tests
    def test_factorial_performance(self):
        """Test factorial performance for reasonable computation time."""
        start_time = time.time()
        result = factorial(20)
        end_time = time.time()

        self.assertEqual(result, 2432902008176640000)
        self.assertLess(end_time - start_time, 1.0, "Factorial should compute quickly")

    def test_fibonacci_performance(self):
        """Test Fibonacci performance for reasonable computation time."""
        start_time = time.time()
        result = fibonacci(30)
        end_time = time.time()

        self.assertEqual(result, 832040)
        self.assertLess(end_time - start_time, 1.0, "Fibonacci should compute quickly")

    def test_prime_checker_performance(self):
        """Test prime checker performance for large numbers."""
        start_time = time.time()
        result = prime_checker(982451653)  # Known large prime
        end_time = time.time()

        self.assertTrue(result)
        self.assertLess(end_time - start_time, 2.0, "Prime checking should be reasonably fast")

    def test_standard_deviation_performance_large_dataset(self):
        """Test standard deviation performance with large dataset."""
        large_data = list(range(10000))

        start_time = time.time()
        result = standard_deviation(large_data)
        end_time = time.time()

        self.assertIsInstance(result, float)
        self.assertLess(end_time - start_time, 1.0, "Standard deviation should compute quickly")

    def tearDown(self):
        """Clean up after each test method."""
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)