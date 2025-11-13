import unittest
from math_utils.operations import add, subtract, multiply, divide, power, factorial, memoize


class TestBasicOperations(unittest.TestCase):
    """Test cases for basic arithmetic operations."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10.5, 2.3), 12.8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)

    def test_add_with_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5.5, 2.3), 3.2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(-5, -3), 15)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)


class TestDivision(unittest.TestCase):
    """Test cases for division operation."""

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_with_decimal_result(self):
        self.assertEqual(divide(10, 4), 2.5)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)


class TestPower(unittest.TestCase):
    """Test cases for power operation."""

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(10, -1), 0.1)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(100, 0), 1)

    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)

    def test_power_fractional_exponent(self):
        self.assertEqual(power(4, 0.5), 2.0)
        self.assertEqual(power(27, 1/3), 3.0)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)


class TestFactorial(unittest.TestCase):
    """Test cases for factorial operation."""

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(3), 6)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers")

    def test_factorial_negative_large_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-10)


class TestMemoization(unittest.TestCase):
    """Test cases for memoization decorator."""

    def test_memoize_caches_results(self):
        call_count = 0

        @memoize
        def expensive_function(n):
            nonlocal call_count
            call_count += 1
            return n * 2

        result1 = expensive_function(5)
        self.assertEqual(result1, 10)
        self.assertEqual(call_count, 1)

        result2 = expensive_function(5)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count, 1)

        result3 = expensive_function(10)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count, 2)

    def test_memoize_with_multiple_arguments(self):
        @memoize
        def multi_arg_function(a, b):
            return a + b

        result1 = multi_arg_function(3, 4)
        self.assertEqual(result1, 7)

        result2 = multi_arg_function(3, 4)
        self.assertEqual(result2, 7)

        result3 = multi_arg_function(4, 3)
        self.assertEqual(result3, 7)

    def test_factorial_uses_memoization(self):
        factorial(5)
        factorial(6)

        memoized_factorial = factorial
        cache_size = len(memoized_factorial.cache)
        self.assertGreater(cache_size, 0)


if __name__ == '__main__':
    unittest.main()
