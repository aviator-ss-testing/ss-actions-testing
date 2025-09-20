"""
Comprehensive test suite for math_operations module.

Tests all mathematical functions including edge cases, error conditions,
and boundary conditions.
"""

import unittest
import math
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from math_operations import (
    add_numbers, multiply_list, calculate_average,
    find_prime_factors, fibonacci_sequence
)


class TestAddNumbers(unittest.TestCase):
    """Test cases for add_numbers function."""

    def test_positive_integers(self):
        """Test addition with positive integers."""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(10, 0), 10)

    def test_negative_integers(self):
        """Test addition with negative integers."""
        self.assertEqual(add_numbers(-5, -3), -8)
        self.assertEqual(add_numbers(-5, 3), -2)
        self.assertEqual(add_numbers(5, -3), 2)

    def test_floating_point(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(add_numbers(2.5, 1.5), 4.0)
        self.assertAlmostEqual(add_numbers(-2.5, 1.5), -1.0)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=10)

    def test_zero_operations(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(0.0, 0.0), 0.0)

    def test_large_numbers(self):
        """Test addition with large numbers."""
        large_int = 10**15
        self.assertEqual(add_numbers(large_int, large_int), 2 * large_int)

    def test_nan_handling(self):
        """Test handling of NaN values."""
        result = add_numbers(float('nan'), 5)
        self.assertTrue(math.isnan(result))
        result = add_numbers(5, float('nan'))
        self.assertTrue(math.isnan(result))

    def test_infinity_error(self):
        """Test error handling for infinite values."""
        with self.assertRaises(OverflowError):
            add_numbers(float('inf'), 5)
        with self.assertRaises(OverflowError):
            add_numbers(5, float('-inf'))

    def test_type_error(self):
        """Test type error for non-numeric inputs."""
        with self.assertRaises(TypeError):
            add_numbers("5", 3)
        with self.assertRaises(TypeError):
            add_numbers(5, "3")
        with self.assertRaises(TypeError):
            add_numbers(None, 5)
        with self.assertRaises(TypeError):
            add_numbers([], 5)
        with self.assertRaises(TypeError):
            add_numbers({}, 5)

    def test_very_large_numbers(self):
        """Test addition with very large numbers."""
        large_num = 10**100
        self.assertEqual(add_numbers(large_num, 1), large_num + 1)
        self.assertEqual(add_numbers(-large_num, large_num), 0)

    def test_very_small_numbers(self):
        """Test addition with very small numbers."""
        tiny_num = 1e-100
        self.assertAlmostEqual(add_numbers(tiny_num, tiny_num), 2 * tiny_num)
        self.assertAlmostEqual(add_numbers(tiny_num, -tiny_num), 0, places=10)

    def test_mixed_int_float_types(self):
        """Test addition with mixed integer and float types."""
        self.assertEqual(add_numbers(5, 2.0), 7.0)
        self.assertEqual(add_numbers(2.5, 3), 5.5)
        self.assertIsInstance(add_numbers(5, 2.0), float)
        self.assertIsInstance(add_numbers(2.5, 3), float)


class TestMultiplyList(unittest.TestCase):
    """Test cases for multiply_list function."""

    def test_positive_integers(self):
        """Test multiplication with positive integers."""
        self.assertEqual(multiply_list([2, 3, 4]), 24)
        self.assertEqual(multiply_list([1, 5, 2]), 10)
        self.assertEqual(multiply_list([1]), 1)

    def test_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply_list([2, 0, 4]), 0)
        self.assertEqual(multiply_list([0]), 0)

    def test_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply_list([-2, 3]), -6)
        self.assertEqual(multiply_list([-2, -3]), 6)
        self.assertEqual(multiply_list([-1, -1, -1]), -1)

    def test_floating_point(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(multiply_list([1.5, 2.0]), 3.0)
        self.assertAlmostEqual(multiply_list([0.5, 0.5]), 0.25)

    def test_empty_list_error(self):
        """Test error for empty list."""
        with self.assertRaises(ValueError):
            multiply_list([])

    def test_non_list_input_error(self):
        """Test error for non-list input."""
        with self.assertRaises(TypeError):
            multiply_list("123")
        with self.assertRaises(TypeError):
            multiply_list(123)

    def test_non_numeric_elements_error(self):
        """Test error for non-numeric elements."""
        with self.assertRaises(TypeError):
            multiply_list([1, 2, "3"])
        with self.assertRaises(TypeError):
            multiply_list([1, None, 3])

    def test_nan_handling(self):
        """Test handling of NaN values."""
        result = multiply_list([1, 2, float('nan')])
        self.assertTrue(math.isnan(result))

    def test_infinity_handling(self):
        """Test handling of infinite values."""
        result = multiply_list([2, float('inf')])
        self.assertTrue(math.isinf(result) and result > 0)
        result = multiply_list([2, float('-inf')])
        self.assertTrue(math.isinf(result) and result < 0)

    def test_very_large_list(self):
        """Test multiplication with very large lists."""
        large_list = [1.1] * 1000
        result = multiply_list(large_list)
        self.assertTrue(math.isinf(result))

    def test_mixed_data_types(self):
        """Test multiplication with mixed integer and float types."""
        self.assertEqual(multiply_list([2, 3.0]), 6.0)
        self.assertEqual(multiply_list([1.5, 4]), 6.0)
        self.assertIsInstance(multiply_list([2, 3.0]), float)

    def test_very_small_numbers(self):
        """Test multiplication with very small numbers."""
        tiny_nums = [1e-50, 1e-50]
        result = multiply_list(tiny_nums)
        self.assertEqual(result, 1e-100)

    def test_single_element_edge_cases(self):
        """Test single element edge cases."""
        self.assertEqual(multiply_list([float('inf')]), float('inf'))
        self.assertEqual(multiply_list([float('-inf')]), float('-inf'))
        result = multiply_list([float('nan')])
        self.assertTrue(math.isnan(result))


class TestCalculateAverage(unittest.TestCase):
    """Test cases for calculate_average function."""

    def test_positive_numbers(self):
        """Test average with positive numbers."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10, 20]), 15.0)
        self.assertEqual(calculate_average([5]), 5.0)

    def test_negative_numbers(self):
        """Test average with negative numbers."""
        self.assertEqual(calculate_average([-1, -2, -3]), -2.0)
        self.assertEqual(calculate_average([-5, 5]), 0.0)

    def test_floating_point(self):
        """Test average with floating point numbers."""
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.0]), 2.333333333333333)
        self.assertEqual(calculate_average([2.0, 4.0]), 3.0)

    def test_with_zero(self):
        """Test average including zero."""
        self.assertEqual(calculate_average([0, 5, 10]), 5.0)
        self.assertEqual(calculate_average([0]), 0.0)

    def test_empty_list_error(self):
        """Test error for empty list."""
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_non_list_input_error(self):
        """Test error for non-list input."""
        with self.assertRaises(TypeError):
            calculate_average("123")

    def test_non_numeric_elements_error(self):
        """Test error for non-numeric elements."""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "3"])

    def test_nan_handling(self):
        """Test handling of NaN values (should be ignored)."""
        result = calculate_average([1, 2, float('nan'), 3])
        self.assertEqual(result, 2.0)
        result = calculate_average([float('nan')])
        self.assertTrue(math.isnan(result))

    def test_infinity_handling(self):
        """Test handling of infinite values."""
        result = calculate_average([1, 2, float('inf')])
        self.assertTrue(math.isinf(result) and result > 0)
        result = calculate_average([1, 2, float('-inf')])
        self.assertTrue(math.isinf(result) and result < 0)

    def test_very_large_numbers(self):
        """Test average with very large numbers."""
        large_nums = [10**100, 10**100, 10**100]
        result = calculate_average(large_nums)
        self.assertEqual(result, 10**100)

    def test_very_small_numbers(self):
        """Test average with very small numbers."""
        tiny_nums = [1e-100, 2e-100, 3e-100]
        result = calculate_average(tiny_nums)
        self.assertAlmostEqual(result, 2e-100, places=110)

    def test_precision_edge_cases(self):
        """Test precision with floating point edge cases."""
        nums = [0.1, 0.2, 0.3]
        result = calculate_average(nums)
        self.assertAlmostEqual(result, 0.2, places=10)

    def test_large_list_performance(self):
        """Test performance with large list."""
        large_list = list(range(10000))
        result = calculate_average(large_list)
        expected = sum(large_list) / len(large_list)
        self.assertEqual(result, expected)

    def test_mixed_positive_negative_zeros(self):
        """Test average with mixed positive, negative, and zero values."""
        mixed_list = [-100, 0, 100, -50, 50]
        result = calculate_average(mixed_list)
        self.assertEqual(result, 0.0)


class TestFindPrimeFactors(unittest.TestCase):
    """Test cases for find_prime_factors function."""

    def test_small_numbers(self):
        """Test prime factorization of small numbers."""
        self.assertEqual(find_prime_factors(1), [])
        self.assertEqual(find_prime_factors(2), [2])
        self.assertEqual(find_prime_factors(3), [3])
        self.assertEqual(find_prime_factors(4), [2, 2])

    def test_composite_numbers(self):
        """Test prime factorization of composite numbers."""
        self.assertEqual(find_prime_factors(12), [2, 2, 3])
        self.assertEqual(find_prime_factors(15), [3, 5])
        self.assertEqual(find_prime_factors(30), [2, 3, 5])
        self.assertEqual(find_prime_factors(100), [2, 2, 5, 5])

    def test_prime_numbers(self):
        """Test prime factorization of prime numbers."""
        self.assertEqual(find_prime_factors(7), [7])
        self.assertEqual(find_prime_factors(13), [13])
        self.assertEqual(find_prime_factors(17), [17])

    def test_larger_numbers(self):
        """Test prime factorization of larger numbers."""
        self.assertEqual(find_prime_factors(60), [2, 2, 3, 5])
        self.assertEqual(find_prime_factors(72), [2, 2, 2, 3, 3])

    def test_perfect_squares(self):
        """Test prime factorization of perfect squares."""
        self.assertEqual(find_prime_factors(9), [3, 3])
        self.assertEqual(find_prime_factors(16), [2, 2, 2, 2])
        self.assertEqual(find_prime_factors(25), [5, 5])

    def test_non_integer_error(self):
        """Test error for non-integer input."""
        with self.assertRaises(TypeError):
            find_prime_factors(12.5)
        with self.assertRaises(TypeError):
            find_prime_factors("12")

    def test_non_positive_error(self):
        """Test error for non-positive integers."""
        with self.assertRaises(ValueError):
            find_prime_factors(0)
        with self.assertRaises(ValueError):
            find_prime_factors(-5)

    def test_very_large_prime(self):
        """Test factorization of large prime numbers."""
        large_prime = 1009  # A reasonably large prime
        result = find_prime_factors(large_prime)
        self.assertEqual(result, [large_prime])

    def test_large_composite_number(self):
        """Test factorization of large composite numbers."""
        large_composite = 1024  # 2^10
        result = find_prime_factors(large_composite)
        self.assertEqual(result, [2] * 10)

    def test_numbers_with_many_factors(self):
        """Test numbers with many prime factors."""
        # 2 * 3 * 5 * 7 * 11 = 2310
        result = find_prime_factors(2310)
        self.assertEqual(result, [2, 3, 5, 7, 11])

    def test_powers_of_primes(self):
        """Test powers of prime numbers."""
        self.assertEqual(find_prime_factors(8), [2, 2, 2])  # 2^3
        self.assertEqual(find_prime_factors(27), [3, 3, 3])  # 3^3
        self.assertEqual(find_prime_factors(125), [5, 5, 5])  # 5^3

    def test_additional_type_errors(self):
        """Test additional invalid input types."""
        with self.assertRaises(TypeError):
            find_prime_factors([12])
        with self.assertRaises(TypeError):
            find_prime_factors(None)
        with self.assertRaises(TypeError):
            find_prime_factors({})

    def test_performance_large_number(self):
        """Test performance with reasonably large numbers."""
        start_time = time.time()
        result = find_prime_factors(997)  # Large prime
        end_time = time.time()

        self.assertEqual(result, [997])
        self.assertLess(end_time - start_time, 1.0)  # Should complete within 1 second


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for fibonacci_sequence function."""

    def test_zero_and_one(self):
        """Test Fibonacci sequence for n=0 and n=1."""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_small_sequences(self):
        """Test small Fibonacci sequences."""
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])
        self.assertEqual(fibonacci_sequence(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_medium_sequence(self):
        """Test medium-sized Fibonacci sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected)

    def test_sequence_properties(self):
        """Test mathematical properties of Fibonacci sequence."""
        fib_10 = fibonacci_sequence(10)
        self.assertEqual(len(fib_10), 10)
        for i in range(2, len(fib_10)):
            self.assertEqual(fib_10[i], fib_10[i-1] + fib_10[i-2])

    def test_larger_sequence(self):
        """Test that larger sequences work and have correct length."""
        fib_20 = fibonacci_sequence(20)
        self.assertEqual(len(fib_20), 20)
        self.assertEqual(fib_20[0], 0)
        self.assertEqual(fib_20[1], 1)
        self.assertEqual(fib_20[-1], 4181)  # 20th Fibonacci number

    def test_non_integer_error(self):
        """Test error for non-integer input."""
        with self.assertRaises(TypeError):
            fibonacci_sequence(5.5)
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")

    def test_negative_error(self):
        """Test error for negative input."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-10)

    def test_very_large_fibonacci_sequence(self):
        """Test performance and correctness of large Fibonacci sequences."""
        n = 100
        start_time = time.time()
        fib_seq = fibonacci_sequence(n)
        end_time = time.time()

        self.assertEqual(len(fib_seq), n)
        self.assertEqual(fib_seq[0], 0)
        self.assertEqual(fib_seq[1], 1)
        # Verify last few numbers are correct
        self.assertEqual(fib_seq[-1], 218922995834555169026)
        self.assertLess(end_time - start_time, 1.0)  # Should complete within 1 second

    def test_fibonacci_growth_properties(self):
        """Test mathematical properties of Fibonacci sequence growth."""
        fib_15 = fibonacci_sequence(15)
        self.assertEqual(len(fib_15), 15)

        # Test that each number is sum of previous two (except first two)
        for i in range(2, len(fib_15)):
            self.assertEqual(fib_15[i], fib_15[i-1] + fib_15[i-2])

        # Test that sequence is strictly increasing after first two
        for i in range(2, len(fib_15)):
            self.assertGreater(fib_15[i], fib_15[i-1])

    def test_fibonacci_performance_scaling(self):
        """Test that fibonacci generation scales linearly."""
        # Test small sequence timing
        start_time = time.time()
        fibonacci_sequence(50)
        small_time = time.time() - start_time

        # Test larger sequence timing
        start_time = time.time()
        fibonacci_sequence(200)
        large_time = time.time() - start_time

        # Large sequence should not be dramatically slower (allow for 10x difference)
        self.assertLess(large_time, small_time * 10)

    def test_additional_type_errors(self):
        """Test additional invalid input types for fibonacci."""
        with self.assertRaises(TypeError):
            fibonacci_sequence([5])
        with self.assertRaises(TypeError):
            fibonacci_sequence(None)
        with self.assertRaises(TypeError):
            fibonacci_sequence({})
        with self.assertRaises(TypeError):
            fibonacci_sequence(True)  # Boolean is technically an int subclass but not intended

    def test_edge_case_boundary_values(self):
        """Test boundary values for Fibonacci sequence."""
        # Test that n=2 works correctly (minimum for full pattern)
        fib_2 = fibonacci_sequence(2)
        self.assertEqual(fib_2, [0, 1])

        # Test medium size for comprehensive verification
        fib_7 = fibonacci_sequence(7)
        expected_7 = [0, 1, 1, 2, 3, 5, 8]
        self.assertEqual(fib_7, expected_7)


class TestPerformance(unittest.TestCase):
    """Performance tests for math operations functions."""

    def test_add_numbers_performance(self):
        """Test add_numbers performance with repeated operations."""
        start_time = time.time()
        for _ in range(10000):
            add_numbers(12345, 67890)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)

    def test_multiply_list_large_input_performance(self):
        """Test multiply_list performance with large input."""
        large_list = [1.001] * 5000
        start_time = time.time()
        multiply_list(large_list)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)

    def test_calculate_average_large_dataset(self):
        """Test calculate_average performance with large dataset."""
        large_dataset = list(range(50000))
        start_time = time.time()
        calculate_average(large_dataset)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)

    def test_find_prime_factors_worst_case(self):
        """Test find_prime_factors performance with large prime."""
        large_prime = 7919  # Large prime number
        start_time = time.time()
        result = find_prime_factors(large_prime)
        end_time = time.time()

        self.assertEqual(result, [large_prime])
        self.assertLess(end_time - start_time, 2.0)  # Allow more time for prime factorization

    def test_fibonacci_sequence_scaling(self):
        """Test fibonacci_sequence performance scaling."""
        # Test different sizes to verify linear scaling
        sizes = [100, 500, 1000]
        times = []

        for size in sizes:
            start_time = time.time()
            fibonacci_sequence(size)
            end_time = time.time()
            times.append(end_time - start_time)

        # Each should complete within reasonable time
        for i, time_taken in enumerate(times):
            self.assertLess(time_taken, 2.0, f"Size {sizes[i]} took too long: {time_taken}s")

    def test_memory_efficiency_fibonacci(self):
        """Test that fibonacci_sequence doesn't use excessive memory."""
        import sys

        # Get baseline memory usage
        baseline = sys.getsizeof([])

        # Generate large fibonacci sequence
        fib_1000 = fibonacci_sequence(1000)
        list_size = sys.getsizeof(fib_1000)

        # Memory should scale reasonably with size
        # Allow generous margin for Python object overhead
        expected_max = baseline + (1000 * 8 * 10)  # Rough estimate with overhead
        self.assertLess(list_size, expected_max)


if __name__ == '__main__':
    unittest.main(verbosity=2)