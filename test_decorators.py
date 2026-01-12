"""
Comprehensive test suite for decorators module.
"""

import unittest
import time
from io import StringIO
from unittest.mock import patch
from decorators import timer, retry, memoize, validate_types


class TestDecorators(unittest.TestCase):
    """Test cases for function decorators."""

    def test_timer_measures_execution_time(self):
        """Test timer decorator measures and prints execution time."""
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
        def add(a, b):
            return a + b

        with patch('sys.stdout', new=StringIO()):
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(10, -5), 5)

    def test_timer_works_with_various_arguments(self):
        """Test timer decorator works with positional and keyword arguments."""
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}"

        with patch('sys.stdout', new=StringIO()):
            self.assertEqual(greet("Alice"), "Hello, Alice")
            self.assertEqual(greet("Bob", greeting="Hi"), "Hi, Bob")
            self.assertEqual(greet(name="Charlie", greeting="Hey"), "Hey, Charlie")

    def test_timer_preserves_metadata(self):
        """Test timer decorator preserves function metadata."""
        @timer
        def example_function():
            """Example docstring."""
            return 42

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_retry_immediate_success(self):
        """Test retry decorator with immediately successful function."""
        call_count = [0]

        @retry(max_attempts=3)
        def successful_function():
            call_count[0] += 1
            return "success"

        result = successful_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_eventual_success(self):
        """Test retry decorator retries until success."""
        call_count = [0]

        @retry(max_attempts=3)
        def eventually_successful():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Not yet")
            return "success"

        result = eventually_successful()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)

    def test_retry_complete_failure(self):
        """Test retry decorator raises exception after all attempts fail."""
        call_count = [0]

        @retry(max_attempts=3)
        def always_fails():
            call_count[0] += 1
            raise ValueError("Always fails")

        with self.assertRaises(ValueError) as context:
            always_fails()

        self.assertEqual(call_count[0], 3)
        self.assertIn("Always fails", str(context.exception))

    def test_retry_single_attempt(self):
        """Test retry decorator with single attempt."""
        call_count = [0]

        @retry(max_attempts=1)
        def single_attempt():
            call_count[0] += 1
            raise RuntimeError("Failed")

        with self.assertRaises(RuntimeError):
            single_attempt()

        self.assertEqual(call_count[0], 1)

    def test_retry_invalid_max_attempts(self):
        """Test retry decorator raises ValueError for invalid max_attempts."""
        with self.assertRaises(ValueError) as context:
            @retry(max_attempts=0)
            def dummy():
                pass

        self.assertIn("max_attempts must be at least 1", str(context.exception))

        with self.assertRaises(ValueError):
            @retry(max_attempts=-1)
            def dummy2():
                pass

    def test_retry_preserves_metadata(self):
        """Test retry decorator preserves function metadata."""
        @retry(max_attempts=2)
        def example_function():
            """Example docstring."""
            return 42

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_memoize_caches_results(self):
        """Test memoize decorator caches function results."""
        call_count = [0]

        @memoize
        def expensive_function(n):
            call_count[0] += 1
            time.sleep(0.05)
            return n * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(10)
        result4 = expensive_function(5)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(result3, 20)
        self.assertEqual(result4, 10)
        self.assertEqual(call_count[0], 2)

    def test_memoize_handles_different_arguments(self):
        """Test memoize decorator distinguishes different arguments."""
        call_count = [0]

        @memoize
        def add(a, b):
            call_count[0] += 1
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 2), 5)

        self.assertEqual(call_count[0], 2)

    def test_memoize_handles_kwargs(self):
        """Test memoize decorator works with keyword arguments."""
        call_count = [0]

        @memoize
        def greet(name, greeting="Hello"):
            call_count[0] += 1
            return f"{greeting}, {name}"

        result1 = greet("Alice", greeting="Hi")
        result2 = greet("Alice", greeting="Hi")

        self.assertEqual(result1, "Hi, Alice")
        self.assertEqual(result2, "Hi, Alice")
        self.assertEqual(call_count[0], 1)

        result3 = greet("Alice", "Hi")
        self.assertEqual(result3, "Hi, Alice")
        self.assertEqual(call_count[0], 2)

    def test_memoize_cache_clear(self):
        """Test memoize decorator cache_clear method."""
        call_count = [0]

        @memoize
        def add(a, b):
            call_count[0] += 1
            return a + b

        add(2, 3)
        add(2, 3)
        self.assertEqual(call_count[0], 1)

        add.cache_clear()
        add(2, 3)
        self.assertEqual(call_count[0], 2)

    def test_memoize_improves_performance(self):
        """Test memoize decorator improves performance on repeated calls."""
        @memoize
        def slow_function(n):
            time.sleep(0.1)
            return n * 2

        start = time.time()
        result1 = slow_function(5)
        first_call_time = time.time() - start

        start = time.time()
        result2 = slow_function(5)
        second_call_time = time.time() - start

        self.assertEqual(result1, result2)
        self.assertGreater(first_call_time, 0.09)
        self.assertLess(second_call_time, 0.01)

    def test_memoize_preserves_metadata(self):
        """Test memoize decorator preserves function metadata."""
        @memoize
        def example_function():
            """Example docstring."""
            return 42

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")

    def test_validate_types_correct_types(self):
        """Test validate_types decorator accepts correct argument types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name} " * count

        result = greet(3, "Alice")
        self.assertEqual(result, "Hello Alice Hello Alice Hello Alice ")

    def test_validate_types_wrong_type(self):
        """Test validate_types decorator raises TypeError for wrong types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name} " * count

        with self.assertRaises(TypeError) as context:
            greet("three", "Alice")

        self.assertIn("argument 0 must be int", str(context.exception))
        self.assertIn("got str", str(context.exception))

        with self.assertRaises(TypeError) as context:
            greet(3, 123)

        self.assertIn("argument 1 must be str", str(context.exception))
        self.assertIn("got int", str(context.exception))

    def test_validate_types_wrong_argument_count(self):
        """Test validate_types decorator raises TypeError for wrong argument count."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name} " * count

        with self.assertRaises(TypeError) as context:
            greet(3)

        self.assertIn("expects 2 arguments", str(context.exception))
        self.assertIn("got 1", str(context.exception))

        with self.assertRaises(TypeError) as context:
            greet(3, "Alice", "Extra")

        self.assertIn("expects 2 arguments", str(context.exception))
        self.assertIn("got 3", str(context.exception))

    def test_validate_types_multiple_type_violations(self):
        """Test validate_types decorator with multiple type violations."""
        @validate_types(int, str, float)
        def calculate(a, b, c):
            return a + len(b) + c

        with self.assertRaises(TypeError):
            calculate("wrong", "test", 3.14)

        with self.assertRaises(TypeError):
            calculate(5, 123, 3.14)

    def test_validate_types_preserves_metadata(self):
        """Test validate_types decorator preserves function metadata."""
        @validate_types(int, str)
        def example_function(num, text):
            """Example docstring."""
            return f"{text}: {num}"

        self.assertEqual(example_function.__name__, "example_function")
        self.assertEqual(example_function.__doc__, "Example docstring.")


if __name__ == '__main__':
    unittest.main()
