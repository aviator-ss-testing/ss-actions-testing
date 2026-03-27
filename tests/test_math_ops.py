import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.math_ops import factorial, is_prime, fibonacci, gcd, lcm


class TestMathOps(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive_small(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_positive_large(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial([5])
        with self.assertRaises(TypeError):
            factorial(None)

    def test_is_prime_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_is_prime_large_primes(self):
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(541))
        self.assertTrue(is_prime(7919))

    def test_is_prime_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(1000))

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))

    def test_is_prime_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            is_prime(5.5)
        with self.assertRaises(TypeError):
            is_prime("5")
        with self.assertRaises(TypeError):
            is_prime(None)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_large_numbers(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_negative_raises_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)
        with self.assertRaises(TypeError):
            fibonacci("5")
        with self.assertRaises(TypeError):
            fibonacci(None)

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 50), 50)

    def test_gcd_coprime_numbers(self):
        self.assertEqual(gcd(17, 19), 1)
        self.assertEqual(gcd(7, 11), 1)
        self.assertEqual(gcd(25, 49), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(123456, 789012), 12)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(42, 42), 42)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            gcd(5.5, 3)
        with self.assertRaises(TypeError):
            gcd(5, 3.5)
        with self.assertRaises(TypeError):
            gcd("5", 3)
        with self.assertRaises(TypeError):
            gcd(None, 5)

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(21, 6), 42)

    def test_lcm_coprime_numbers(self):
        self.assertEqual(lcm(7, 11), 77)
        self.assertEqual(lcm(5, 9), 45)

    def test_lcm_with_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-12, 8), 24)
        self.assertEqual(lcm(12, -8), 24)
        self.assertEqual(lcm(-12, -8), 24)

    def test_lcm_large_numbers(self):
        self.assertEqual(lcm(123456, 789012), 8117355456)

    def test_lcm_same_numbers(self):
        self.assertEqual(lcm(42, 42), 42)
        self.assertEqual(lcm(1, 1), 1)

    def test_lcm_with_one(self):
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(10, 1), 10)

    def test_lcm_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            lcm(5.5, 3)
        with self.assertRaises(TypeError):
            lcm(5, 3.5)
        with self.assertRaises(TypeError):
            lcm("5", 3)
        with self.assertRaises(TypeError):
            lcm(None, 5)


if __name__ == '__main__':
    unittest.main()
