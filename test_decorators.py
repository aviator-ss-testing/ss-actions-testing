"""
Comprehensive test suite for decorators module.
"""

import unittest
import time
from unittest.mock import patch
from io import StringIO
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
        """Test timer decorator preserves original function behavior."""
        @timer
        def add_numbers(a, b):
            return a + b

        with patch('sys.stdout', new=StringIO()):
            result = add_numbers(5, 3)

        self.assertEqual(result, 8)

    def test_timer_preserves_metadata(self):
        """Test timer decorator preserves function metadata."""
        @timer
        def sample_function():
            """Sample docstring."""
            pass

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")

    def test_timer_works_with_various_arguments(self):
        """Test timer decorator works with positional and keyword arguments."""
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        with patch('sys.stdout', new=StringIO()):
            result1 = greet("Alice")
            result2 = greet("Bob", greeting="Hi")

        self.assertEqual(result1, "Hello, Alice!")
        self.assertEqual(result2, "Hi, Bob!")

    def test_retry_immediate_success(self):
        """Test retry decorator with function that succeeds immediately."""
        call_count = [0]

        @retry(max_attempts=3)
        def succeed_immediately():
            call_count[0] += 1
            return "success"

        result = succeed_immediately()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_eventual_success(self):
        """Test retry decorator with function that succeeds after failures."""
        call_count = [0]

        @retry(max_attempts=3)
        def succeed_on_third_try():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Not yet")
            return "success"

        result = succeed_on_third_try()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)

    def test_retry_complete_failure(self):
        """Test retry decorator when all attempts fail."""
        call_count = [0]

        @retry(max_attempts=3)
        def always_fail():
            call_count[0] += 1
            raise ValueError("Always fails")

        with self.assertRaises(ValueError) as context:
            always_fail()

        self.assertEqual(str(context.exception), "Always fails")
        self.assertEqual(call_count[0], 3)

    def test_retry_single_attempt(self):
        """Test retry decorator with single attempt."""
        call_count = [0]

        @retry(max_attempts=1)
        def fail_once():
            call_count[0] += 1
            raise ValueError("Failed")

        with self.assertRaises(ValueError):
            fail_once()

        self.assertEqual(call_count[0], 1)

    def test_retry_invalid_max_attempts(self):
        """Test retry decorator raises error for invalid max_attempts."""
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
        def sample_function():
            """Sample docstring."""
            return "result"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")

    def test_memoize_caches_results(self):
        """Test memoize decorator caches function results."""
        call_count = [0]

        @memoize
        def expensive_function(n):
            call_count[0] += 1
            time.sleep(0.1)
            return n * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count[0], 1)

    def test_memoize_different_arguments(self):
        """Test memoize decorator with different arguments."""
        call_count = [0]

        @memoize
        def compute(x, y):
            call_count[0] += 1
            return x + y

        result1 = compute(2, 3)
        result2 = compute(4, 5)
        result3 = compute(2, 3)

        self.assertEqual(result1, 5)
        self.assertEqual(result2, 9)
        self.assertEqual(result3, 5)
        self.assertEqual(call_count[0], 2)

    def test_memoize_with_kwargs(self):
        """Test memoize decorator with keyword arguments."""
        call_count = [0]

        @memoize
        def greet(name, greeting="Hello"):
            call_count[0] += 1
            return f"{greeting}, {name}!"

        result1 = greet("Alice", greeting="Hi")
        result2 = greet("Alice", greeting="Hi")
        result3 = greet("Alice", greeting="Hey")

        self.assertEqual(result1, "Hi, Alice!")
        self.assertEqual(result2, "Hi, Alice!")
        self.assertEqual(result3, "Hey, Alice!")
        self.assertEqual(call_count[0], 2)

    def test_memoize_cache_clear(self):
        """Test memoize decorator cache_clear functionality."""
        call_count = [0]

        @memoize
        def compute(n):
            call_count[0] += 1
            return n * 2

        compute(5)
        compute(5)
        self.assertEqual(call_count[0], 1)

        compute.cache_clear()
        compute(5)
        self.assertEqual(call_count[0], 2)

    def test_memoize_performance_improvement(self):
        """Test memoize decorator improves performance."""
        @memoize
        def slow_compute(n):
            time.sleep(0.1)
            return n * 2

        start1 = time.time()
        result1 = slow_compute(5)
        time1 = time.time() - start1

        start2 = time.time()
        result2 = slow_compute(5)
        time2 = time.time() - start2

        self.assertEqual(result1, result2)
        self.assertGreater(time1, 0.09)
        self.assertLess(time2, 0.01)

    def test_memoize_preserves_metadata(self):
        """Test memoize decorator preserves function metadata."""
        @memoize
        def sample_function():
            """Sample docstring."""
            return "result"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")

    def test_validate_types_correct_types(self):
        """Test validate_types decorator with correct argument types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name}! " * count

        result = greet(3, "Alice")
        self.assertEqual(result, "Hello Alice! Hello Alice! Hello Alice! ")

    def test_validate_types_wrong_type(self):
        """Test validate_types decorator raises TypeError for wrong types."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name}! " * count

        with self.assertRaises(TypeError) as context:
            greet("3", "Alice")

        self.assertIn("argument 0 must be int", str(context.exception))
        self.assertIn("got str", str(context.exception))

    def test_validate_types_wrong_argument_count(self):
        """Test validate_types decorator raises TypeError for wrong argument count."""
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name}! " * count

        with self.assertRaises(TypeError) as context:
            greet(3)

        self.assertIn("expects 2 arguments", str(context.exception))
        self.assertIn("got 1", str(context.exception))

    def test_validate_types_multiple_wrong_types(self):
        """Test validate_types decorator with multiple type violations."""
        @validate_types(int, str, float)
        def compute(a, b, c):
            return a + len(b) + c

        with self.assertRaises(TypeError):
            compute("5", "text", 3.14)

        with self.assertRaises(TypeError):
            compute(5, 123, 3.14)

    def test_validate_types_preserves_metadata(self):
        """Test validate_types decorator preserves function metadata."""
        @validate_types(int)
        def sample_function(n):
            """Sample docstring."""
            return n * 2

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")


if __name__ == '__main__':
    unittest.main()
