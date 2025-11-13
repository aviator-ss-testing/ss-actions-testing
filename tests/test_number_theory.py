import unittest
from math_utils.number_theory import is_prime, gcd, lcm, fibonacci, is_perfect_square, validate_positive


class TestIsPrime(unittest.TestCase):
    """Test cases for is_prime function."""

    def test_is_prime_with_known_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(97))

    def test_is_prime_with_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(100))

    def test_is_prime_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_edge_case_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_large_prime(self):
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(1009))

    def test_is_prime_large_composite(self):
        self.assertFalse(is_prime(1000))
        self.assertFalse(is_prime(1024))


class TestGCD(unittest.TestCase):
    """Test cases for gcd function."""

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_coprime_numbers(self):
        self.assertEqual(gcd(13, 7), 1)
        self.assertEqual(gcd(25, 16), 1)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(5, 5), 5)
        self.assertEqual(gcd(100, 100), 100)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_with_one(self):
        self.assertEqual(gcd(1, 5), 1)
        self.assertEqual(gcd(100, 1), 1)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        self.assertEqual(gcd(-12, -8), 4)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(270, 192), 6)


class TestLCM(unittest.TestCase):
    """Test cases for lcm function."""

    def test_lcm_positive_numbers(self):
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(21, 6), 42)

    def test_lcm_coprime_numbers(self):
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(13, 17), 221)

    def test_lcm_same_numbers(self):
        self.assertEqual(lcm(5, 5), 5)
        self.assertEqual(lcm(100, 100), 100)

    def test_lcm_with_zero(self):
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_with_one(self):
        self.assertEqual(lcm(1, 5), 5)
        self.assertEqual(lcm(100, 1), 100)

    def test_lcm_negative_numbers(self):
        self.assertEqual(lcm(-12, 8), 24)
        self.assertEqual(lcm(12, -8), 24)
        self.assertEqual(lcm(-12, -8), 24)

    def test_lcm_large_numbers(self):
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(lcm(270, 192), 8640)


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci function."""

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_larger_numbers(self):
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Fibonacci is not defined for negative numbers")

    def test_fibonacci_negative_large_raises_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_uses_memoization(self):
        fibonacci(10)
        fibonacci(12)

        cache_size = len(fibonacci.cache)
        self.assertGreater(cache_size, 0)


class TestIsPerfectSquare(unittest.TestCase):
    """Test cases for is_perfect_square function."""

    def test_is_perfect_square_true(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(25))
        self.assertTrue(is_perfect_square(36))
        self.assertTrue(is_perfect_square(49))
        self.assertTrue(is_perfect_square(64))
        self.assertTrue(is_perfect_square(81))
        self.assertTrue(is_perfect_square(100))

    def test_is_perfect_square_false(self):
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(7))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(15))
        self.assertFalse(is_perfect_square(99))

    def test_is_perfect_square_large_perfect(self):
        self.assertTrue(is_perfect_square(144))
        self.assertTrue(is_perfect_square(225))
        self.assertTrue(is_perfect_square(10000))

    def test_is_perfect_square_large_non_perfect(self):
        self.assertFalse(is_perfect_square(1000))
        self.assertFalse(is_perfect_square(9999))

    def test_is_perfect_square_negative(self):
        self.assertFalse(is_perfect_square(-1))
        self.assertFalse(is_perfect_square(-4))
        self.assertFalse(is_perfect_square(-100))


class TestValidatePositive(unittest.TestCase):
    """Test cases for validate_positive decorator."""

    def test_validate_positive_with_negative_input(self):
        with self.assertRaises(ValueError) as context:
            is_prime(-5)
        self.assertEqual(str(context.exception), "Expected positive integer, got -5")

    def test_validate_positive_with_zero(self):
        with self.assertRaises(ValueError) as context:
            is_prime(0)
        self.assertEqual(str(context.exception), "Expected positive integer, got 0")

    def test_validate_positive_with_non_integer(self):
        with self.assertRaises(TypeError) as context:
            is_prime(5.5)
        self.assertEqual(str(context.exception), "Expected integer, got float")

    def test_validate_positive_with_string(self):
        with self.assertRaises(TypeError) as context:
            is_prime("5")
        self.assertEqual(str(context.exception), "Expected integer, got str")

    def test_validate_positive_with_valid_input(self):
        result = is_prime(5)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
