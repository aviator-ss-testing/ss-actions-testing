"""
Test suite for mathematical operations module.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.mathops.operations import factorial, fibonacci, is_prime, gcd, lcm, power


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
            factorial(-1)

    def test_factorial_negative_five_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_factorial_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial("5")


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_fifteen(self):
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_two(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_seven(self):
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci(3.14)


class TestIsPrime(unittest.TestCase):

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_three(self):
        self.assertTrue(is_prime(3))

    def test_is_prime_seven(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_thirteen(self):
        self.assertTrue(is_prime(13))

    def test_is_prime_large_prime(self):
        self.assertTrue(is_prime(97))

    def test_is_prime_four(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_nine(self):
        self.assertFalse(is_prime(9))

    def test_is_prime_fifteen(self):
        self.assertFalse(is_prime(15))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-5))

    def test_is_prime_negative_prime_value(self):
        self.assertFalse(is_prime(-7))


class TestGCD(unittest.TestCase):

    def test_gcd_coprime_pair(self):
        self.assertEqual(gcd(17, 13), 1)

    def test_gcd_coprime_pair_larger(self):
        self.assertEqual(gcd(25, 36), 1)

    def test_gcd_common_factor(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_common_factor_larger(self):
        self.assertEqual(gcd(100, 50), 50)

    def test_gcd_zero_first_arg(self):
        self.assertEqual(gcd(0, 5), 5)

    def test_gcd_zero_second_arg(self):
        self.assertEqual(gcd(12, 0), 12)

    def test_gcd_both_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_equal_numbers(self):
        self.assertEqual(gcd(42, 42), 42)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-12, 8), 4)

    def test_gcd_both_negative(self):
        self.assertEqual(gcd(-15, -25), 5)

    def test_gcd_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError):
            gcd(5.5, 3)

    def test_gcd_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            gcd(10, "5")


class TestLCM(unittest.TestCase):

    def test_lcm_coprime_numbers(self):
        self.assertEqual(lcm(3, 5), 15)

    def test_lcm_with_common_factor(self):
        self.assertEqual(lcm(12, 18), 36)

    def test_lcm_one_divides_other(self):
        self.assertEqual(lcm(4, 12), 12)

    def test_lcm_equal_numbers(self):
        self.assertEqual(lcm(7, 7), 7)

    def test_lcm_with_one(self):
        self.assertEqual(lcm(1, 15), 15)

    def test_lcm_zero_first_arg(self):
        self.assertEqual(lcm(0, 5), 0)

    def test_lcm_zero_second_arg(self):
        self.assertEqual(lcm(8, 0), 0)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-4, 6), 12)

    def test_lcm_both_negative(self):
        self.assertEqual(lcm(-3, -5), 15)

    def test_lcm_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError):
            lcm(4.5, 3)


class TestPower(unittest.TestCase):

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_positive_exponent_larger(self):
        self.assertEqual(power(5, 4), 625)

    def test_power_zero_exponent(self):
        self.assertEqual(power(10, 0), 1)

    def test_power_zero_exponent_negative_base(self):
        self.assertEqual(power(-5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)

    def test_power_negative_exponent_larger(self):
        self.assertAlmostEqual(power(5, -2), 0.04)

    def test_power_base_zero_positive_exponent(self):
        self.assertEqual(power(0, 5), 0)

    def test_power_base_zero_zero_exponent(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_base_zero_negative_exponent_raises_value_error(self):
        with self.assertRaises(ValueError):
            power(0, -1)

    def test_power_negative_base_positive_exponent(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_negative_base_even_exponent(self):
        self.assertEqual(power(-3, 2), 9)

    def test_power_one_to_any_power(self):
        self.assertEqual(power(1, 100), 1)

    def test_power_float_base(self):
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_power_float_exponent(self):
        result = power(4, 0.5)
        self.assertAlmostEqual(result, 2.0)


if __name__ == '__main__':
    unittest.main()
