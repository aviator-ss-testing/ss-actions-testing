"""Comprehensive test suite for decorators module validating decorator behavior."""
import unittest
import time
from io import StringIO
from unittest.mock import patch
from decorators import timer, retry, memoize, validate_types

class TestDecorators(unittest.TestCase):
    """Test cases for function decorators: timer, retry, memoize, validate_types."""

    def test_timer_measures_time(self):
        """Test timer decorator prints execution time without breaking function."""
        @timer
        def slow_function():
            time.sleep(0.1)
            return 42
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = slow_function()
            output = fake_out.getvalue()
        self.assertEqual(result, 42)
        self.assertIn('slow_function executed in', output)
        self.assertIn('seconds', output)

    def test_timer_preserves_function_metadata(self):
        """Test timer decorator preserves function name and docstring."""
        @timer
        def sample_function():
            """Sample docstring."""
            return 100
        self.assertEqual(sample_function.__name__, 'sample_function')
        self.assertEqual(sample_function.__doc__, 'Sample docstring.')

    def test_timer_with_arguments(self):
        """Test timer decorator works with functions that take arguments."""
        @timer
        def add(a, b):
            return a + b
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = add(5, 3)
        self.assertEqual(result, 8)

    def test_timer_with_kwargs(self):
        """Test timer decorator works with keyword arguments."""
        @timer
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = greet("Alice", greeting="Hi")
        self.assertEqual(result, "Hi, Alice!")

    def test_retry_immediate_success(self):
        """Test retry decorator when function succeeds immediately."""
        call_count = [0]
        @retry(max_attempts=3)
        def success_function():
            call_count[0] += 1
            return "success"
        result = success_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_eventual_success(self):
        """Test retry decorator retries failing functions until success."""
        call_count = [0]
        @retry(max_attempts=3)
        def flaky_function():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Not yet")
            return "success"
        result = flaky_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)

    def test_retry_complete_failure(self):
        """Test retry decorator raises last exception after all attempts fail."""
        call_count = [0]
        @retry(max_attempts=3)
        def failing_function():
            call_count[0] += 1
            raise ValueError("Always fails")
        with self.assertRaises(ValueError) as context:
            failing_function()
        self.assertIn("Always fails", str(context.exception))
        self.assertEqual(call_count[0], 3)

    def test_retry_single_attempt(self):
        """Test retry decorator with max_attempts=1 raises error immediately."""
        call_count = [0]
        @retry(max_attempts=1)
        def failing_function():
            call_count[0] += 1
            raise RuntimeError("Fail")
        with self.assertRaises(RuntimeError):
            failing_function()
        self.assertEqual(call_count[0], 1)

    def test_retry_invalid_max_attempts(self):
        """Test retry decorator raises ValueError for invalid max_attempts."""
        with self.assertRaises(ValueError) as context:
            @retry(max_attempts=0)
            def dummy():
                pass
        self.assertIn("max_attempts must be at least 1", str(context.exception))

    def test_retry_preserves_function_metadata(self):
        """Test retry decorator preserves function name and docstring."""
        @retry(max_attempts=2)
        def sample_function():
            """Sample docstring."""
            return 50
        self.assertEqual(sample_function.__name__, 'sample_function')
        self.assertEqual(sample_function.__doc__, 'Sample docstring.')

    def test_memoize_cache_miss(self):
        """Test memoize decorator caches results on first call."""
        call_count = [0]
        @memoize
        def expensive_function(x):
            call_count[0] += 1
            time.sleep(0.1)
            return x * 2
        result = expensive_function(5)
        self.assertEqual(result, 10)
        self.assertEqual(call_count[0], 1)

    def test_memoize_cache_hit(self):
        """Test memoize decorator returns cached results on repeated calls."""
        call_count = [0]
        @memoize
        def expensive_function(x):
            call_count[0] += 1
            time.sleep(0.1)
            return x * 2
        result1 = expensive_function(5)
        result2 = expensive_function(5)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count[0], 1)

    def test_memoize_different_arguments(self):
        """Test memoize decorator creates separate cache entries for different arguments."""
        call_count = [0]
        @memoize
        def expensive_function(x):
            call_count[0] += 1
            return x * 2
        result1 = expensive_function(5)
        result2 = expensive_function(10)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 20)
        self.assertEqual(call_count[0], 2)

    def test_memoize_with_kwargs(self):
        """Test memoize decorator handles keyword arguments correctly."""
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
        """Test memoize decorator cache_clear() method clears the cache."""
        call_count = [0]
        @memoize
        def expensive_function(x):
            call_count[0] += 1
            return x * 2
        expensive_function(5)
        expensive_function.cache_clear()
        expensive_function(5)
        self.assertEqual(call_count[0], 2)

    def test_memoize_performance_improvement(self):
        """Test memoize decorator improves performance on repeated calls."""
        @memoize
        def slow_function(x):
            time.sleep(0.1)
            return x * 2
        start1 = time.time()
        slow_function(5)
        time1 = time.time() - start1
        start2 = time.time()
        slow_function(5)
        time2 = time.time() - start2
        self.assertGreater(time1, 0.09)
        self.assertLess(time2, 0.01)

    def test_validate_types_correct_types(self):
        """Test validate_types decorator allows correct argument types."""
        @validate_types(int, str)
        def process(num, text):
            return f"{text}: {num}"
        result = process(42, "Answer")
        self.assertEqual(result, "Answer: 42")

    def test_validate_types_wrong_type(self):
        """Test validate_types decorator raises TypeError for incorrect argument types."""
        @validate_types(int, str)
        def process(num, text):
            return f"{text}: {num}"
        with self.assertRaises(TypeError) as context:
            process("42", "Answer")
        self.assertIn("argument 0 must be int", str(context.exception))

    def test_validate_types_wrong_argument_count(self):
        """Test validate_types decorator raises TypeError for wrong number of arguments."""
        @validate_types(int, str)
        def process(num, text):
            return f"{text}: {num}"
        with self.assertRaises(TypeError) as context:
            process(42)
        self.assertIn("expected 2 arguments, got 1", str(context.exception))

    def test_validate_types_multiple_types(self):
        """Test validate_types decorator validates all argument types."""
        @validate_types(int, int, str)
        def add_and_format(a, b, suffix):
            return f"{a + b}{suffix}"
        result = add_and_format(10, 20, "!")
        self.assertEqual(result, "30!")
        with self.assertRaises(TypeError):
            add_and_format(10, "20", "!")

    def test_validate_types_preserves_function_metadata(self):
        """Test validate_types decorator preserves function name and docstring."""
        @validate_types(int)
        def sample_function(x):
            """Sample docstring."""
            return x * 2
        self.assertEqual(sample_function.__name__, 'sample_function')
        self.assertEqual(sample_function.__doc__, 'Sample docstring.')

if __name__ == '__main__':
    unittest.main()
