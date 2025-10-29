"""
Test suite for math_utils module.

Tests all mathematical utility functions including factorial, GCD,
prime checking, Fibonacci sequence, and the validate_positive decorator.
"""

import unittest
import sys
import os

# Add src directory to path for importing modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from math_utils import factorial, gcd, is_prime, fibonacci, validate_positive


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function."""
    
    def test_factorial_valid_inputs(self):
        """Test factorial with valid inputs (0, 1, 5, 10)."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    
    def test_factorial_invalid_negative(self):
        """Test factorial with negative numbers."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)
    
    def test_factorial_invalid_non_integer(self):
        """Test factorial with non-integer inputs."""
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial([5])


class TestGCD(unittest.TestCase):
    """Test cases for greatest common divisor function."""
    
    def test_gcd_basic_cases(self):
        """Test GCD with various number pairs."""
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(15, 25), 5)
        self.assertEqual(gcd(17, 19), 1)  # Coprime numbers
        self.assertEqual(gcd(100, 75), 25)
    
    def test_gcd_edge_cases(self):
        """Test GCD with edge cases including zero and negative numbers."""
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(-12, 8), 4)  # Negative numbers
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)
    
    def test_gcd_same_numbers(self):
        """Test GCD with identical numbers."""
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(42, 42), 42)
    
    def test_gcd_invalid_inputs(self):
        """Test GCD with non-integer inputs."""
        with self.assertRaises(TypeError):
            gcd(3.5, 2)
        with self.assertRaises(TypeError):
            gcd(3, "2")
        with self.assertRaises(TypeError):
            gcd("3", 2)


class TestIsPrime(unittest.TestCase):
    """Test cases for prime number checking function."""
    
    def test_is_prime_edge_cases(self):
        """Test is_prime with edge cases (0, 1, 2)."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
    
    def test_is_prime_small_primes(self):
        """Test is_prime with known small prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(is_prime(prime), f"{prime} should be prime")
    
    def test_is_prime_non_primes(self):
        """Test is_prime with known non-prime numbers."""
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} should not be prime")
    
    def test_is_prime_larger_numbers(self):
        """Test is_prime with larger numbers."""
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(121))  # 11^2
    
    def test_is_prime_negative_numbers(self):
        """Test is_prime with negative numbers."""
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-11))
    
    def test_is_prime_invalid_inputs(self):
        """Test is_prime with non-integer inputs."""
        with self.assertRaises(TypeError):
            is_prime(3.5)
        with self.assertRaises(TypeError):
            is_prime("7")
        with self.assertRaises(TypeError):
            is_prime([7])


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci sequence function."""
    
    def test_fibonacci_first_10_numbers(self):
        """Test fibonacci sequence correctness for first 10 numbers."""
        # Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected_value in enumerate(expected, 1):
            self.assertEqual(fibonacci(i), expected_value, 
                           f"fibonacci({i}) should be {expected_value}")
    
    def test_fibonacci_larger_numbers(self):
        """Test fibonacci with larger position numbers."""
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_fibonacci_invalid_negative(self):
        """Test fibonacci with negative numbers (should be caught by decorator)."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)
    
    def test_fibonacci_with_zero(self):
        """Test fibonacci with zero (decorator allows non-negative numbers)."""
        # The @validate_positive decorator allows 0 (only rejects negative numbers)
        result = fibonacci(0)
        # Based on the implementation, fibonacci(0) returns 1
        self.assertEqual(result, 1)
    
    def test_fibonacci_invalid_non_integer(self):
        """Test fibonacci with non-integer inputs."""
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        with self.assertRaises(TypeError):
            fibonacci("5")


class TestValidatePositiveDecorator(unittest.TestCase):
    """Test cases for the validate_positive decorator."""
    
    def setUp(self):
        """Set up test functions decorated with validate_positive."""
        @validate_positive
        def test_func_single_arg(x):
            return x * 2
        
        @validate_positive
        def test_func_multiple_args(x, y, z=1):
            return x + y + z
        
        @validate_positive
        def test_func_mixed_args(x, text, y):
            return f"{text}: {x + y}"
        
        self.test_func_single_arg = test_func_single_arg
        self.test_func_multiple_args = test_func_multiple_args
        self.test_func_mixed_args = test_func_mixed_args
    
    def test_decorator_positive_values(self):
        """Test decorator behavior with positive values."""
        self.assertEqual(self.test_func_single_arg(5), 10)
        self.assertEqual(self.test_func_multiple_args(1, 2, 3), 6)
        self.assertEqual(self.test_func_mixed_args(5, "Result", 10), "Result: 15")
    
    def test_decorator_negative_values(self):
        """Test decorator behavior with negative values."""
        with self.assertRaises(ValueError) as context:
            self.test_func_single_arg(-5)
        self.assertIn("requires positive arguments", str(context.exception))
        
        with self.assertRaises(ValueError):
            self.test_func_multiple_args(-1, 2)
        
        with self.assertRaises(ValueError):
            self.test_func_multiple_args(1, -2)
        
        with self.assertRaises(ValueError):
            self.test_func_mixed_args(-5, "Test", 10)
        
        with self.assertRaises(ValueError):
            self.test_func_mixed_args(5, "Test", -10)
    
    def test_decorator_zero_values(self):
        """Test decorator behavior with zero values."""
        self.assertEqual(self.test_func_single_arg(0), 0)
        self.assertEqual(self.test_func_multiple_args(0, 1), 2)
        self.assertEqual(self.test_func_mixed_args(0, "Zero", 5), "Zero: 5")
    
    def test_decorator_non_numeric_values(self):
        """Test decorator behavior with non-numeric values (should pass through)."""
        self.assertEqual(self.test_func_mixed_args(5, "Test", 10), "Test: 15")
        # Non-numeric arguments should not trigger the decorator
        @validate_positive
        def test_func_string_only(text):
            return text.upper()
        
        self.assertEqual(test_func_string_only("hello"), "HELLO")
    
    def test_decorator_preserves_function_metadata(self):
        """Test that decorator preserves original function metadata."""
        # Test that fibonacci function (which uses the decorator) preserves its name and docstring
        self.assertEqual(fibonacci.__name__, 'fibonacci')
        self.assertIn('Generate nth Fibonacci number', fibonacci.__doc__)


if __name__ == '__main__':
    unittest.main()