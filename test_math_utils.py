import unittest
from math_utils import add, subtract, multiply, divide, power, factorial, is_prime, fibonacci


class TestBasicOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(100, 200), 300)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)

    def test_add_with_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -5), -5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(100, 50), 50)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(-5, -3), 15)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(100, 0), 0)
        self.assertEqual(multiply(0, -5), 0)


class TestDivision(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(100, 4), 25)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(10, -2), -5)

    def test_divide_with_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -10), 0)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_zero_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(0, 0)

    def test_divide_returns_float(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)


class TestPower(unittest.TestCase):

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(10, -2), 0.01)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)


class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_numbers(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_factorial_larger_numbers(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers")

        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_non_integer_raises_error(self):
        with self.assertRaises(TypeError) as context:
            factorial(5.5)
        self.assertEqual(str(context.exception), "Factorial is only defined for integers")

        with self.assertRaises(TypeError):
            factorial("5")


class TestIsPrime(unittest.TestCase):

    def test_is_prime_with_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(97))

    def test_is_prime_with_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(100))

    def test_is_prime_edge_case_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_edge_case_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_edge_case_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-10))

    def test_is_prime_non_integer_raises_error(self):
        with self.assertRaises(TypeError) as context:
            is_prime(5.5)
        self.assertEqual(str(context.exception), "Prime check is only defined for integers")

        with self.assertRaises(TypeError):
            is_prime("5")


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero_length(self):
        self.assertEqual(fibonacci(0), [])

    def test_fibonacci_one_length(self):
        self.assertEqual(fibonacci(1), [0])

    def test_fibonacci_two_length(self):
        self.assertEqual(fibonacci(2), [0, 1])

    def test_fibonacci_small_sequences(self):
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_longer_sequence(self):
        result = fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 10)

    def test_fibonacci_sequence_correctness(self):
        sequence = fibonacci(8)
        for i in range(2, len(sequence)):
            self.assertEqual(sequence[i], sequence[i-1] + sequence[i-2])

    def test_fibonacci_negative_length_raises_error(self):
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Fibonacci length must be non-negative")

        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_non_integer_raises_error(self):
        with self.assertRaises(TypeError) as context:
            fibonacci(5.5)
        self.assertEqual(str(context.exception), "Fibonacci length must be an integer")

        with self.assertRaises(TypeError):
            fibonacci("5")


if __name__ == '__main__':
    unittest.main()
