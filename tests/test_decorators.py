"""Test cases for decorator utilities."""

import sys
import os
import unittest
import time
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.decorators import timer, memoize, validate_positive


class TestTimerDecorator(unittest.TestCase):
    """Test cases for the @timer decorator."""

    def test_timer_prints_execution_time(self):
        """Test that @timer decorator prints execution time."""
        @timer
        def sample_function(n):
            time.sleep(0.01)
            return n * 2

        captured_output = StringIO()
        sys.stdout = captured_output

        result = sample_function(5)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, 10)
        self.assertIn("sample_function executed in", output)
        self.assertIn("seconds", output)

    def test_timer_preserves_function_metadata(self):
        """Test that @timer preserves original function name and docstring."""
        @timer
        def documented_function():
            """This is a test function."""
            return 42

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "This is a test function.")

    def test_timer_with_multiple_arguments(self):
        """Test that @timer works with functions that have multiple arguments."""
        @timer
        def add_numbers(a, b, c=0):
            return a + b + c

        captured_output = StringIO()
        sys.stdout = captured_output

        result = add_numbers(1, 2, c=3)

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 6)


class TestMemoizeDecorator(unittest.TestCase):
    """Test cases for the @memoize decorator."""

    def test_memoize_caches_results(self):
        """Test that @memoize caches and returns cached results."""
        call_count = {'count': 0}

        @memoize
        def expensive_function(n):
            call_count['count'] += 1
            time.sleep(0.01)
            return n * n

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(10)
        result4 = expensive_function(5)

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 25)
        self.assertEqual(result3, 100)
        self.assertEqual(result4, 25)
        self.assertEqual(call_count['count'], 2)

    def test_memoize_with_different_arguments(self):
        """Test that @memoize differentiates between different arguments."""
        @memoize
        def multiply(a, b):
            return a * b

        result1 = multiply(3, 4)
        result2 = multiply(4, 3)
        result3 = multiply(3, 4)

        self.assertEqual(result1, 12)
        self.assertEqual(result2, 12)
        self.assertEqual(result3, 12)

    def test_memoize_with_kwargs(self):
        """Test that @memoize works with keyword arguments."""
        call_count = {'count': 0}

        @memoize
        def greet(name, greeting="Hello"):
            call_count['count'] += 1
            return f"{greeting}, {name}!"

        result1 = greet("Alice", greeting="Hi")
        result2 = greet("Alice", greeting="Hi")
        result3 = greet("Bob")
        result4 = greet("Bob")

        self.assertEqual(result1, "Hi, Alice!")
        self.assertEqual(result2, "Hi, Alice!")
        self.assertEqual(result3, "Hello, Bob!")
        self.assertEqual(result4, "Hello, Bob!")
        self.assertEqual(call_count['count'], 2)

    def test_memoize_preserves_function_metadata(self):
        """Test that @memoize preserves original function name and docstring."""
        @memoize
        def cached_function():
            """This is a cached function."""
            return 100

        self.assertEqual(cached_function.__name__, "cached_function")
        self.assertEqual(cached_function.__doc__, "This is a cached function.")


class TestValidatePositiveDecorator(unittest.TestCase):
    """Test cases for the @validate_positive decorator."""

    def test_validate_positive_with_valid_inputs(self):
        """Test that @validate_positive allows positive numeric arguments."""
        @validate_positive
        def calculate_area(length, width):
            return length * width

        result1 = calculate_area(5, 10)
        result2 = calculate_area(3.5, 2.0)

        self.assertEqual(result1, 50)
        self.assertEqual(result2, 7.0)

    def test_validate_positive_rejects_negative_values(self):
        """Test that @validate_positive raises ValueError for negative values."""
        @validate_positive
        def calculate_volume(length, width, height):
            return length * width * height

        with self.assertRaises(ValueError) as context:
            calculate_volume(-5, 10, 3)

        self.assertEqual(str(context.exception), "All numeric arguments must be positive")

    def test_validate_positive_rejects_zero(self):
        """Test that @validate_positive raises ValueError for zero values."""
        @validate_positive
        def divide(a, b):
            return a / b

        with self.assertRaises(ValueError) as context:
            divide(10, 0)

        self.assertEqual(str(context.exception), "All numeric arguments must be positive")

    def test_validate_positive_with_kwargs(self):
        """Test that @validate_positive validates keyword arguments."""
        @validate_positive
        def calculate(base=1, multiplier=1):
            return base * multiplier

        result = calculate(base=5, multiplier=3)
        self.assertEqual(result, 15)

        with self.assertRaises(ValueError):
            calculate(base=5, multiplier=-3)

    def test_validate_positive_ignores_non_numeric_types(self):
        """Test that @validate_positive only validates numeric types."""
        @validate_positive
        def process_data(value, name="test"):
            return f"{name}: {value}"

        result = process_data(5, name="example")
        self.assertEqual(result, "example: 5")


class TestDecoratorChaining(unittest.TestCase):
    """Test cases for chaining multiple decorators together."""

    def test_timer_and_memoize_chaining(self):
        """Test that @timer and @memoize work together."""
        call_count = {'count': 0}

        @timer
        @memoize
        def fibonacci(n):
            call_count['count'] += 1
            if n <= 1:
                return n
            return n + n - 1

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = fibonacci(10)
        result2 = fibonacci(10)

        sys.stdout = sys.__stdout__

        self.assertEqual(result1, result2)
        self.assertEqual(call_count['count'], 1)

    def test_validate_positive_and_timer_chaining(self):
        """Test that @validate_positive and @timer work together."""
        @timer
        @validate_positive
        def multiply(a, b):
            return a * b

        captured_output = StringIO()
        sys.stdout = captured_output

        result = multiply(3, 4)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, 12)
        self.assertIn("multiply executed in", output)

        with self.assertRaises(ValueError):
            multiply(-1, 5)

    def test_all_three_decorators_chaining(self):
        """Test that all three decorators can be chained together."""
        @timer
        @memoize
        @validate_positive
        def power(base, exponent):
            return base ** exponent

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = power(2, 3)
        result2 = power(2, 3)

        sys.stdout = sys.__stdout__

        self.assertEqual(result1, 8)
        self.assertEqual(result2, 8)

        with self.assertRaises(ValueError):
            power(0, 5)


if __name__ == '__main__':
    unittest.main()
