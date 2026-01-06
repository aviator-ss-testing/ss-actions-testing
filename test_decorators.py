"""Tests for decorator functions."""

import unittest
import time
from io import StringIO
from unittest.mock import patch
from decorators import timer, retry, memoize, validate_types


class TestDecorators(unittest.TestCase):
    """Test cases for function decorators."""

    def test_timer_preserves_function_behavior(self):
        """Test that timer decorator doesn't break function behavior."""
        @timer
        def add(a, b):
            return a + b

        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_timer_preserves_function_metadata(self):
        """Test that timer preserves original function name and docstring."""
        @timer
        def my_function():
            """Test docstring."""
            pass

        self.assertEqual(my_function.__name__, 'my_function')
        self.assertEqual(my_function.__doc__, 'Test docstring.')

    def test_timer_produces_output(self):
        """Test that timer prints execution time."""
        @timer
        def slow_function():
            time.sleep(0.01)
            return "done"

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = slow_function()
            output = fake_output.getvalue()

        self.assertEqual(result, "done")
        self.assertIn("slow_function took", output)
        self.assertIn("seconds", output)

    def test_timer_with_arguments(self):
        """Test timer decorator with function that takes arguments."""
        @timer
        def multiply(x, y, z=1):
            return x * y * z

        result = multiply(2, 3, z=4)
        self.assertEqual(result, 24)

    def test_retry_succeeds_on_first_attempt(self):
        """Test retry decorator when function succeeds immediately."""
        call_count = []

        @retry(max_attempts=3)
        def succeeds_immediately():
            call_count.append(1)
            return "success"

        result = succeeds_immediately()
        self.assertEqual(result, "success")
        self.assertEqual(len(call_count), 1)

    def test_retry_succeeds_after_failures(self):
        """Test retry decorator retries until function succeeds."""
        call_count = []

        @retry(max_attempts=3)
        def fails_twice():
            call_count.append(1)
            if len(call_count) < 3:
                raise ValueError("Not ready yet")
            return "success"

        result = fails_twice()
        self.assertEqual(result, "success")
        self.assertEqual(len(call_count), 3)

    def test_retry_fails_after_max_attempts(self):
        """Test retry decorator raises exception after exhausting attempts."""
        call_count = []

        @retry(max_attempts=3)
        def always_fails():
            call_count.append(1)
            raise RuntimeError("Always fails")

        with self.assertRaises(RuntimeError) as context:
            always_fails()

        self.assertEqual(str(context.exception), "Always fails")
        self.assertEqual(len(call_count), 3)

    def test_retry_with_one_attempt(self):
        """Test retry decorator with max_attempts=1."""
        call_count = []

        @retry(max_attempts=1)
        def fails_once():
            call_count.append(1)
            raise ValueError("Failed")

        with self.assertRaises(ValueError):
            fails_once()

        self.assertEqual(len(call_count), 1)

    def test_retry_invalid_max_attempts(self):
        """Test retry decorator raises ValueError for invalid max_attempts."""
        with self.assertRaises(ValueError) as context:
            @retry(max_attempts=0)
            def some_function():
                pass

        self.assertIn("must be at least 1", str(context.exception))

    def test_retry_preserves_function_metadata(self):
        """Test that retry preserves original function name and docstring."""
        @retry(max_attempts=2)
        def my_function():
            """Test docstring."""
            return True

        self.assertEqual(my_function.__name__, 'my_function')
        self.assertEqual(my_function.__doc__, 'Test docstring.')

    def test_memoize_caches_results(self):
        """Test memoize decorator caches function results."""
        call_count = []

        @memoize
        def expensive_function(n):
            call_count.append(1)
            return n * n

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(5)

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 25)
        self.assertEqual(result3, 25)
        self.assertEqual(len(call_count), 1)

    def test_memoize_different_arguments(self):
        """Test memoize caches separately for different arguments."""
        call_count = []

        @memoize
        def square(n):
            call_count.append(1)
            return n * n

        result1 = square(3)
        result2 = square(4)
        result3 = square(3)

        self.assertEqual(result1, 9)
        self.assertEqual(result2, 16)
        self.assertEqual(result3, 9)
        self.assertEqual(len(call_count), 2)

    def test_memoize_with_kwargs(self):
        """Test memoize works with keyword arguments."""
        call_count = []

        @memoize
        def add(a, b=0):
            call_count.append(1)
            return a + b

        result1 = add(5, b=3)
        result2 = add(5, b=3)
        result3 = add(5, b=4)

        self.assertEqual(result1, 8)
        self.assertEqual(result2, 8)
        self.assertEqual(result3, 9)
        self.assertEqual(len(call_count), 2)

    def test_memoize_cache_attribute(self):
        """Test memoize exposes cache attribute."""
        @memoize
        def double(n):
            return n * 2

        double(5)
        double(10)

        self.assertIsInstance(double.cache, dict)
        self.assertEqual(len(double.cache), 2)

    def test_memoize_cache_clear(self):
        """Test memoize cache_clear method."""
        call_count = []

        @memoize
        def triple(n):
            call_count.append(1)
            return n * 3

        triple(5)
        self.assertEqual(len(call_count), 1)

        triple.cache_clear()
        triple(5)
        self.assertEqual(len(call_count), 2)

    def test_memoize_improves_performance(self):
        """Test memoize actually improves performance on repeated calls."""
        @memoize
        def slow_computation(n):
            time.sleep(0.01)
            return n * n

        start1 = time.time()
        result1 = slow_computation(10)
        duration1 = time.time() - start1

        start2 = time.time()
        result2 = slow_computation(10)
        duration2 = time.time() - start2

        self.assertEqual(result1, result2)
        self.assertLess(duration2, duration1 / 2)

    def test_validate_types_correct_types(self):
        """Test validate_types accepts correct argument types."""
        @validate_types(int, str, float)
        def process_data(id, name, score):
            return f"{name} (#{id}): {score}"

        result = process_data(42, "Alice", 95.5)
        self.assertEqual(result, "Alice (#42): 95.5")

    def test_validate_types_wrong_type(self):
        """Test validate_types raises TypeError for wrong argument type."""
        @validate_types(int, str)
        def greet(age, name):
            return f"{name} is {age}"

        with self.assertRaises(TypeError) as context:
            greet("thirty", "Bob")

        error_msg = str(context.exception)
        self.assertIn("argument 0", error_msg)
        self.assertIn("int", error_msg)
        self.assertIn("str", error_msg)

    def test_validate_types_wrong_argument_count_too_few(self):
        """Test validate_types raises TypeError when too few arguments."""
        @validate_types(int, str, float)
        def process_data(id, name, score):
            return f"{name}: {score}"

        with self.assertRaises(TypeError) as context:
            process_data(1, "Test")

        error_msg = str(context.exception)
        self.assertIn("expected 3 arguments", error_msg)
        self.assertIn("got 2", error_msg)

    def test_validate_types_wrong_argument_count_too_many(self):
        """Test validate_types raises TypeError when too many arguments."""
        @validate_types(int, str)
        def simple_func(a, b):
            return a + len(b)

        with self.assertRaises(TypeError) as context:
            simple_func(1, "test", "extra")

        error_msg = str(context.exception)
        self.assertIn("expected 2 arguments", error_msg)
        self.assertIn("got 3", error_msg)

    def test_validate_types_multiple_wrong_types(self):
        """Test validate_types reports first type mismatch."""
        @validate_types(int, int, int)
        def sum_three(a, b, c):
            return a + b + c

        with self.assertRaises(TypeError) as context:
            sum_three(1, "wrong", "also wrong")

        error_msg = str(context.exception)
        self.assertIn("argument 1", error_msg)

    def test_validate_types_preserves_function_metadata(self):
        """Test that validate_types preserves function name and docstring."""
        @validate_types(int)
        def my_function(x):
            """Test docstring."""
            return x * 2

        self.assertEqual(my_function.__name__, 'my_function')
        self.assertEqual(my_function.__doc__, 'Test docstring.')

    def test_validate_types_with_bool_and_int(self):
        """Test validate_types with bool (which is subclass of int)."""
        @validate_types(int)
        def double(x):
            return x * 2

        result = double(True)
        self.assertEqual(result, 2)

    def test_validate_types_with_none_type(self):
        """Test validate_types can validate None type."""
        @validate_types(type(None))
        def accepts_none(x):
            return "got none"

        result = accepts_none(None)
        self.assertEqual(result, "got none")

        with self.assertRaises(TypeError):
            accepts_none(42)


if __name__ == '__main__':
    unittest.main()
