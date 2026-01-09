"""
Comprehensive test suite for decorators module.
"""

import unittest
import time
import sys
from io import StringIO
from unittest.mock import patch
from decorators import timer, retry, memoize, validate_types


class TestDecorators(unittest.TestCase):
    """Test cases for function decorators."""

    def test_timer_measures_execution_time(self):
        """Test timer decorator produces time measurements."""
        @timer
        def slow_function():
            time.sleep(0.1)
            return "done"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = slow_function()
            output = fake_out.getvalue()

        self.assertEqual(result, "done")
        self.assertIn("slow_function executed in", output)
        self.assertIn("seconds", output)

    def test_timer_preserves_function_behavior(self):
        """Test timer decorator doesn't break function behavior."""
        @timer
        def add_numbers(a, b):
            return a + b

        with patch('sys.stdout', new=StringIO()):
            result = add_numbers(5, 3)

        self.assertEqual(result, 8)

    def test_timer_preserves_metadata(self):
        """Test timer decorator preserves function metadata."""
        @timer
        def example_function():
            """Example docstring."""
            pass

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_timer_with_arguments(self):
        """Test timer decorator with various argument types."""
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        with patch('sys.stdout', new=StringIO()):
            result1 = greet("Alice")
            result2 = greet("Bob", greeting="Hi")

        self.assertEqual(result1, "Hello, Alice!")
        self.assertEqual(result2, "Hi, Bob!")

    def test_retry_succeeds_immediately(self):
        """Test retry decorator when function succeeds on first attempt."""
        call_count = [0]

        @retry(max_attempts=3)
        def always_succeeds():
            call_count[0] += 1
            return "success"

        result = always_succeeds()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_succeeds_eventually(self):
        """Test retry decorator retries until function succeeds."""
        call_count = [0]

        @retry(max_attempts=3)
        def succeeds_on_third_try():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Not yet")
            return "success"

        result = succeeds_on_third_try()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)

    def test_retry_fails_after_max_attempts(self):
        """Test retry decorator raises exception after max attempts."""
        call_count = [0]

        @retry(max_attempts=3)
        def always_fails():
            call_count[0] += 1
            raise ValueError("Always fails")

        with self.assertRaises(ValueError) as context:
            always_fails()

        self.assertEqual(str(context.exception), "Always fails")
        self.assertEqual(call_count[0], 3)

    def test_retry_with_single_attempt(self):
        """Test retry decorator with max_attempts=1."""
        call_count = [0]

        @retry(max_attempts=1)
        def fails_once():
            call_count[0] += 1
            raise RuntimeError("Failed")

        with self.assertRaises(RuntimeError):
            fails_once()

        self.assertEqual(call_count[0], 1)

    def test_retry_invalid_max_attempts(self):
        """Test retry decorator raises ValueError for invalid max_attempts."""
        with self.assertRaises(ValueError):
            @retry(max_attempts=0)
            def some_function():
                pass

        with self.assertRaises(ValueError):
            @retry(max_attempts=-1)
            def another_function():
                pass

    def test_retry_preserves_metadata(self):
        """Test retry decorator preserves function metadata."""
        @retry(max_attempts=2)
        def example_function():
            """Example docstring."""
            pass

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_memoize_caches_results(self):
        """Test memoize decorator caches function results."""
        call_count = [0]

        @memoize
        def expensive_computation(n):
            call_count[0] += 1
            time.sleep(0.05)
            return n * n

        result1 = expensive_computation(5)
        result2 = expensive_computation(5)
        result3 = expensive_computation(5)

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 25)
        self.assertEqual(result3, 25)
        self.assertEqual(call_count[0], 1)

    def test_memoize_different_arguments(self):
        """Test memoize decorator handles different arguments separately."""
        call_count = [0]

        @memoize
        def add(a, b):
            call_count[0] += 1
            return a + b

        result1 = add(2, 3)
        result2 = add(2, 3)
        result3 = add(3, 4)
        result4 = add(2, 3)

        self.assertEqual(result1, 5)
        self.assertEqual(result2, 5)
        self.assertEqual(result3, 7)
        self.assertEqual(result4, 5)
        self.assertEqual(call_count[0], 2)

    def test_memoize_with_kwargs(self):
        """Test memoize decorator handles keyword arguments."""
        call_count = [0]

        @memoize
        def greet(name, greeting="Hello"):
            call_count[0] += 1
            return f"{greeting}, {name}!"

        result1 = greet("Alice", greeting="Hi")
        result2 = greet("Alice", greeting="Hi")
        result3 = greet("Alice", greeting="Hello")

        self.assertEqual(result1, "Hi, Alice!")
        self.assertEqual(result2, "Hi, Alice!")
        self.assertEqual(result3, "Hello, Alice!")
        self.assertEqual(call_count[0], 2)

    def test_memoize_cache_clear(self):
        """Test memoize decorator cache_clear functionality."""
        call_count = [0]

        @memoize
        def compute(n):
            call_count[0] += 1
            return n * 2

        result1 = compute(10)
        result2 = compute(10)
        compute.cache_clear()
        result3 = compute(10)

        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count[0], 2)

    def test_memoize_improves_performance(self):
        """Test memoize decorator improves performance on repeated calls."""
        @memoize
        def slow_function(n):
            time.sleep(0.1)
            return n * n

        start_time = time.time()
        result1 = slow_function(5)
        first_call_time = time.time() - start_time

        start_time = time.time()
        result2 = slow_function(5)
        second_call_time = time.time() - start_time

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 25)
        self.assertGreater(first_call_time, 0.09)
        self.assertLess(second_call_time, 0.01)

    def test_memoize_preserves_metadata(self):
        """Test memoize decorator preserves function metadata."""
        @memoize
        def example_function():
            """Example docstring."""
            pass

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_validate_types_correct_types(self):
        """Test validate_types decorator accepts correct types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name} " * count

        result = greet(3, "World")
        self.assertEqual(result, "Hello World Hello World Hello World ")

    def test_validate_types_wrong_type(self):
        """Test validate_types decorator raises TypeError for wrong types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name}"

        with self.assertRaises(TypeError) as context:
            greet("3", "World")

        self.assertIn("must be int", str(context.exception))
        self.assertIn("got str", str(context.exception))

    def test_validate_types_wrong_argument_count(self):
        """Test validate_types decorator raises TypeError for wrong argument count."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name}"

        with self.assertRaises(TypeError) as context:
            greet(3)

        self.assertIn("expects 2 arguments", str(context.exception))
        self.assertIn("got 1", str(context.exception))

    def test_validate_types_multiple_wrong_types(self):
        """Test validate_types decorator checks all argument types."""
        @validate_types(int, int, str)
        def calculate(a, b, operation):
            return f"{a} {operation} {b}"

        with self.assertRaises(TypeError):
            calculate(1, "2", "plus")

        with self.assertRaises(TypeError):
            calculate("1", 2, "plus")

    def test_validate_types_with_none(self):
        """Test validate_types decorator rejects None for non-None types."""
        @validate_types(int, str)
        def process(num, text):
            return f"{text}: {num}"

        with self.assertRaises(TypeError):
            process(None, "test")

        with self.assertRaises(TypeError):
            process(42, None)

    def test_validate_types_preserves_metadata(self):
        """Test validate_types decorator preserves function metadata."""
        @validate_types(int)
        def example_function(n):
            """Example docstring."""
            pass

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")


if __name__ == '__main__':
    unittest.main()
