"""
Comprehensive tests for mathematical utility functions.

This module tests all mathematical operations in the utils.math_operations module,
ensuring complete code coverage with normal cases, edge cases, and error conditions.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.math_operations import (
    calculate_factorial,
    is_prime,
    fibonacci_sequence,
    greatest_common_divisor,
    least_common_multiple,
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_standard_deviation,
    sum_of_divisors,
    is_perfect_number
)


class TestMathOperations(unittest.TestCase):
    """Test cases for all mathematical utility functions."""
    
    def test_calculate_factorial_normal_cases(self):
        """Test factorial calculation with normal inputs."""
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(10), 3628800)
        
    def test_calculate_factorial_error_cases(self):
        """Test factorial calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_factorial("5")
        with self.assertRaises(TypeError):
            calculate_factorial(5.0)
        with self.assertRaises(TypeError):
            calculate_factorial(None)
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial(-10)
    
    def test_is_prime_normal_cases(self):
        """Test prime checking with normal inputs."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(23))
        self.assertFalse(is_prime(25))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))
        
    def test_is_prime_large_numbers(self):
        """Test prime checking with larger numbers."""
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(103))
        self.assertFalse(is_prime(121))
        self.assertTrue(is_prime(997))
        
    def test_is_prime_error_cases(self):
        """Test prime checking with invalid inputs."""
        with self.assertRaises(TypeError):
            is_prime("5")
        with self.assertRaises(TypeError):
            is_prime(5.0)
        with self.assertRaises(TypeError):
            is_prime(None)
        with self.assertRaises(TypeError):
            is_prime([])
    
    def test_fibonacci_sequence_normal_cases(self):
        """Test Fibonacci sequence generation with normal inputs."""
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        
    def test_fibonacci_sequence_error_cases(self):
        """Test Fibonacci sequence generation with invalid inputs."""
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")
        with self.assertRaises(TypeError):
            fibonacci_sequence(5.0)
        with self.assertRaises(TypeError):
            fibonacci_sequence(None)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-10)
    
    def test_greatest_common_divisor_normal_cases(self):
        """Test GCD calculation with normal inputs."""
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(17, 13), 1)
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(12, 8), 4)
        self.assertEqual(greatest_common_divisor(24, 36), 12)
        self.assertEqual(greatest_common_divisor(7, 14), 7)
        
    def test_greatest_common_divisor_negative_numbers(self):
        """Test GCD calculation with negative numbers."""
        self.assertEqual(greatest_common_divisor(-48, 18), 6)
        self.assertEqual(greatest_common_divisor(48, -18), 6)
        self.assertEqual(greatest_common_divisor(-48, -18), 6)
        self.assertEqual(greatest_common_divisor(-12, -8), 4)
        
    def test_greatest_common_divisor_error_cases(self):
        """Test GCD calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            greatest_common_divisor("5", 3)
        with self.assertRaises(TypeError):
            greatest_common_divisor(5, "3")
        with self.assertRaises(TypeError):
            greatest_common_divisor(5.0, 3)
        with self.assertRaises(TypeError):
            greatest_common_divisor(None, 3)
        with self.assertRaises(ValueError):
            greatest_common_divisor(0, 0)
    
    def test_least_common_multiple_normal_cases(self):
        """Test LCM calculation with normal inputs."""
        self.assertEqual(least_common_multiple(12, 18), 36)
        self.assertEqual(least_common_multiple(7, 5), 35)
        self.assertEqual(least_common_multiple(4, 6), 12)
        self.assertEqual(least_common_multiple(15, 25), 75)
        self.assertEqual(least_common_multiple(3, 7), 21)
        self.assertEqual(least_common_multiple(8, 12), 24)
        
    def test_least_common_multiple_negative_numbers(self):
        """Test LCM calculation with negative numbers."""
        self.assertEqual(least_common_multiple(-12, 18), 36)
        self.assertEqual(least_common_multiple(12, -18), 36)
        self.assertEqual(least_common_multiple(-12, -18), 36)
        
    def test_least_common_multiple_error_cases(self):
        """Test LCM calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            least_common_multiple("5", 3)
        with self.assertRaises(TypeError):
            least_common_multiple(5, "3")
        with self.assertRaises(TypeError):
            least_common_multiple(5.0, 3)
        with self.assertRaises(ValueError):
            least_common_multiple(0, 5)
        with self.assertRaises(ValueError):
            least_common_multiple(5, 0)
        with self.assertRaises(ValueError):
            least_common_multiple(0, 0)
    
    def test_calculate_mean_normal_cases(self):
        """Test mean calculation with normal inputs."""
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_mean([10, 20, 30]), 20.0)
        self.assertEqual(calculate_mean([1]), 1.0)
        self.assertEqual(calculate_mean([2.5, 3.5, 4.0]), 10.0/3)
        self.assertEqual(calculate_mean([-1, 0, 1]), 0.0)
        self.assertEqual(calculate_mean([100]), 100.0)
        
    def test_calculate_mean_mixed_types(self):
        """Test mean calculation with mixed numeric types."""
        self.assertEqual(calculate_mean([1, 2.0, 3, 4.0]), 2.5)
        self.assertEqual(calculate_mean([1.5, 2.5]), 2.0)
        
    def test_calculate_mean_error_cases(self):
        """Test mean calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_mean("not_a_list")
        with self.assertRaises(TypeError):
            calculate_mean(123)
        with self.assertRaises(TypeError):
            calculate_mean(None)
        with self.assertRaises(ValueError):
            calculate_mean([])
        with self.assertRaises(ValueError):
            calculate_mean([1, 2, "three", 4])
        with self.assertRaises(ValueError):
            calculate_mean([1, 2, None, 4])
        with self.assertRaises(ValueError):
            calculate_mean([1, 2, [3], 4])
    
    def test_calculate_median_normal_cases(self):
        """Test median calculation with normal inputs."""
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(calculate_median([1]), 1.0)
        self.assertEqual(calculate_median([5, 1, 3, 2, 4]), 3.0)
        self.assertEqual(calculate_median([10, 20]), 15.0)
        self.assertEqual(calculate_median([1, 100, 2]), 2.0)
        
    def test_calculate_median_mixed_types(self):
        """Test median calculation with mixed numeric types."""
        self.assertEqual(calculate_median([1, 2.0, 3]), 2.0)
        self.assertEqual(calculate_median([1.5, 2.5, 3.5]), 2.5)
        
    def test_calculate_median_error_cases(self):
        """Test median calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_median("not_a_list")
        with self.assertRaises(TypeError):
            calculate_median(123)
        with self.assertRaises(ValueError):
            calculate_median([])
        with self.assertRaises(ValueError):
            calculate_median([1, 2, "three"])
        with self.assertRaises(ValueError):
            calculate_median([1, None, 3])
    
    def test_calculate_mode_normal_cases(self):
        """Test mode calculation with normal inputs."""
        self.assertEqual(calculate_mode([1, 2, 2, 3, 4]), [2])
        self.assertEqual(calculate_mode([1, 1, 2, 2, 3]), [1, 2])
        self.assertEqual(calculate_mode([1]), [1])
        self.assertEqual(calculate_mode([1, 1, 1]), [1])
        self.assertEqual(calculate_mode([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(calculate_mode([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 5])
        
    def test_calculate_mode_mixed_types(self):
        """Test mode calculation with mixed numeric types."""
        self.assertEqual(calculate_mode([1, 1.0, 2, 2.0]), [1, 2.0])
        self.assertEqual(calculate_mode([1.5, 1.5, 2.5]), [1.5])
        
    def test_calculate_mode_error_cases(self):
        """Test mode calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_mode("not_a_list")
        with self.assertRaises(ValueError):
            calculate_mode([])
        with self.assertRaises(ValueError):
            calculate_mode([1, 2, "three"])
        with self.assertRaises(ValueError):
            calculate_mode([1, None, 3])
    
    def test_calculate_variance_normal_cases(self):
        """Test variance calculation with normal inputs."""
        result1 = calculate_variance([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result1, 2.5, places=6)
        
        result2 = calculate_variance([10, 12, 14, 16, 18])
        self.assertAlmostEqual(result2, 10.0, places=6)
        
        result3 = calculate_variance([1, 1])
        self.assertAlmostEqual(result3, 0.0, places=6)
        
        result4 = calculate_variance([2, 4, 6])
        self.assertAlmostEqual(result4, 4.0, places=6)
        
    def test_calculate_variance_mixed_types(self):
        """Test variance calculation with mixed numeric types."""
        result = calculate_variance([1, 2.0, 3, 4.0])
        self.assertAlmostEqual(result, 5.0/3, places=6)
        
    def test_calculate_variance_error_cases(self):
        """Test variance calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_variance("not_a_list")
        with self.assertRaises(ValueError):
            calculate_variance([])
        with self.assertRaises(ValueError):
            calculate_variance([1])
        with self.assertRaises(ValueError):
            calculate_variance([1, 2, "three"])
        with self.assertRaises(ValueError):
            calculate_variance([1, None, 3])
    
    def test_calculate_standard_deviation_normal_cases(self):
        """Test standard deviation calculation with normal inputs."""
        result1 = calculate_standard_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result1, 1.5811388300841898, places=6)
        
        result2 = calculate_standard_deviation([10, 12, 14, 16, 18])
        self.assertAlmostEqual(result2, 3.1622776601683795, places=6)
        
        result3 = calculate_standard_deviation([1, 1])
        self.assertAlmostEqual(result3, 0.0, places=6)
        
        result4 = calculate_standard_deviation([2, 4, 6])
        self.assertAlmostEqual(result4, 2.0, places=6)
        
    def test_calculate_standard_deviation_error_cases(self):
        """Test standard deviation calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            calculate_standard_deviation("not_a_list")
        with self.assertRaises(ValueError):
            calculate_standard_deviation([])
        with self.assertRaises(ValueError):
            calculate_standard_deviation([1])
        with self.assertRaises(ValueError):
            calculate_standard_deviation([1, 2, "three"])
        with self.assertRaises(ValueError):
            calculate_standard_deviation([1, None, 3])
    
    def test_sum_of_divisors_normal_cases(self):
        """Test sum of divisors calculation with normal inputs."""
        self.assertEqual(sum_of_divisors(1), 0)
        self.assertEqual(sum_of_divisors(6), 6)
        self.assertEqual(sum_of_divisors(12), 16)
        self.assertEqual(sum_of_divisors(28), 28)
        self.assertEqual(sum_of_divisors(8), 7)
        self.assertEqual(sum_of_divisors(10), 8)
        self.assertEqual(sum_of_divisors(15), 9)
        
    def test_sum_of_divisors_prime_numbers(self):
        """Test sum of divisors for prime numbers (should always be 1)."""
        self.assertEqual(sum_of_divisors(2), 1)
        self.assertEqual(sum_of_divisors(3), 1)
        self.assertEqual(sum_of_divisors(5), 1)
        self.assertEqual(sum_of_divisors(7), 1)
        self.assertEqual(sum_of_divisors(11), 1)
        self.assertEqual(sum_of_divisors(13), 1)
        
    def test_sum_of_divisors_perfect_squares(self):
        """Test sum of divisors for perfect squares."""
        self.assertEqual(sum_of_divisors(4), 3)
        self.assertEqual(sum_of_divisors(9), 4)
        self.assertEqual(sum_of_divisors(16), 15)
        self.assertEqual(sum_of_divisors(25), 6)
        
    def test_sum_of_divisors_error_cases(self):
        """Test sum of divisors calculation with invalid inputs."""
        with self.assertRaises(TypeError):
            sum_of_divisors("6")
        with self.assertRaises(TypeError):
            sum_of_divisors(6.0)
        with self.assertRaises(TypeError):
            sum_of_divisors(None)
        with self.assertRaises(ValueError):
            sum_of_divisors(0)
        with self.assertRaises(ValueError):
            sum_of_divisors(-1)
        with self.assertRaises(ValueError):
            sum_of_divisors(-10)
    
    def test_is_perfect_number_normal_cases(self):
        """Test perfect number checking with normal inputs."""
        self.assertFalse(is_perfect_number(1))
        self.assertFalse(is_perfect_number(2))
        self.assertFalse(is_perfect_number(3))
        self.assertFalse(is_perfect_number(4))
        self.assertFalse(is_perfect_number(5))
        self.assertTrue(is_perfect_number(6))
        self.assertFalse(is_perfect_number(7))
        self.assertFalse(is_perfect_number(8))
        self.assertFalse(is_perfect_number(12))
        self.assertTrue(is_perfect_number(28))
        self.assertFalse(is_perfect_number(30))
        
    def test_is_perfect_number_larger_numbers(self):
        """Test perfect number checking with larger numbers."""
        self.assertTrue(is_perfect_number(496))
        self.assertFalse(is_perfect_number(500))
        self.assertFalse(is_perfect_number(1000))
        
    def test_is_perfect_number_error_cases(self):
        """Test perfect number checking with invalid inputs."""
        with self.assertRaises(TypeError):
            is_perfect_number("6")
        with self.assertRaises(TypeError):
            is_perfect_number(6.0)
        with self.assertRaises(TypeError):
            is_perfect_number(None)
        with self.assertRaises(ValueError):
            is_perfect_number(0)
        with self.assertRaises(ValueError):
            is_perfect_number(-1)
        with self.assertRaises(ValueError):
            is_perfect_number(-10)


if __name__ == '__main__':
    unittest.main()