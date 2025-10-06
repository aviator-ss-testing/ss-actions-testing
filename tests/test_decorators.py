"""
Unit tests for decorator functions module.

Tests cover timing, logging, retry, validation, and caching decorators,
including decorator stacking and metadata preservation.
"""

import unittest
import time
import logging
import sys
from io import StringIO
from unittest.mock import patch, MagicMock
from decorators import timer, log_calls, retry, validate_types, memoize


class TestTimerDecorator(unittest.TestCase):
    """Test suite for the timer decorator."""

    def test_timer_measures_execution_time(self):
        """Test that timer decorator measures execution time accurately."""
        @timer
        def slow_function():
            time.sleep(0.1)
            return "done"

        captured_output = StringIO()
        sys.stdout = captured_output

        result = slow_function()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, "done")
        self.assertIn("slow_function executed in", output)
        self.assertIn("seconds", output)

    def test_timer_output_format(self):
        """Test that timer output format is correct with reasonable timing values."""
        @timer
        def quick_function():
            return 42

        captured_output = StringIO()
        sys.stdout = captured_output

        result = quick_function()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, 42)
        self.assertRegex(output, r"quick_function executed in \d+\.\d{6} seconds")

    def test_timer_preserves_function_metadata(self):
        """Test that timer preserves original function name and docstring."""
        @timer
        def documented_function():
            """This is a test function."""
            pass

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "This is a test function.")

    def test_timer_with_arguments(self):
        """Test timer decorator with functions that take arguments."""
        @timer
        def add_numbers(a, b):
            return a + b

        captured_output = StringIO()
        sys.stdout = captured_output

        result = add_numbers(5, 3)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, 8)
        self.assertIn("add_numbers executed in", output)

    def test_timer_with_exception(self):
        """Test that timer works correctly when function raises an exception."""
        @timer
        def failing_function():
            raise ValueError("Test error")

        captured_output = StringIO()
        sys.stdout = captured_output

        with self.assertRaises(ValueError):
            failing_function()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("failing_function executed in", output)


class TestLogCallsDecorator(unittest.TestCase):
    """Test suite for the log_calls decorator."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
        self.handler.setFormatter(formatter)

        logger = logging.getLogger('decorators')
        logger.addHandler(self.handler)
        logger.setLevel(logging.INFO)

    def tearDown(self):
        """Clean up after each test method."""
        logger = logging.getLogger('decorators')
        logger.removeHandler(self.handler)

    def test_log_calls_captures_function_calls(self):
        """Test that log_calls captures function calls with correct format."""
        @log_calls
        def test_function(x, y):
            return x + y

        result = test_function(3, 5)

        self.assertEqual(result, 8)
        log_output = self.log_capture.getvalue()
        self.assertIn("Calling test_function(3, 5)", log_output)
        self.assertIn("test_function returned: 8", log_output)

    def test_log_calls_captures_kwargs(self):
        """Test that log_calls captures keyword arguments correctly."""
        @log_calls
        def test_function(x, y=10):
            return x * y

        result = test_function(5, y=7)

        self.assertEqual(result, 35)
        log_output = self.log_capture.getvalue()
        self.assertIn("Calling test_function(5, y=7)", log_output)
        self.assertIn("test_function returned: 35", log_output)

    def test_log_calls_captures_exception(self):
        """Test that log_calls logs exceptions correctly."""
        @log_calls
        def failing_function():
            raise RuntimeError("Test exception")

        with self.assertRaises(RuntimeError):
            failing_function()

        log_output = self.log_capture.getvalue()
        self.assertIn("Calling failing_function()", log_output)
        self.assertIn("failing_function raised RuntimeError: Test exception", log_output)

    def test_log_calls_preserves_metadata(self):
        """Test that log_calls preserves function metadata."""
        @log_calls
        def documented_function():
            """Function documentation."""
            return True

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Function documentation.")

    def test_log_calls_with_no_arguments(self):
        """Test log_calls with a function that takes no arguments."""
        @log_calls
        def no_args_function():
            return "result"

        result = no_args_function()

        self.assertEqual(result, "result")
        log_output = self.log_capture.getvalue()
        self.assertIn("Calling no_args_function()", log_output)


class TestRetryDecorator(unittest.TestCase):
    """Test suite for the retry decorator."""

    def test_retry_successful_on_first_attempt(self):
        """Test retry decorator when function succeeds on first attempt."""
        call_count = [0]

        @retry(max_attempts=3, delay=0.01)
        def successful_function():
            call_count[0] += 1
            return "success"

        result = successful_function()

        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_successful_after_failures(self):
        """Test retry decorator when function succeeds after initial failures."""
        call_count = [0]

        @retry(max_attempts=3, delay=0.01)
        def eventually_successful():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Not yet")
            return "success"

        captured_output = StringIO()
        sys.stdout = captured_output

        result = eventually_successful()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)
        self.assertIn("eventually_successful failed (attempt 1/3)", output)
        self.assertIn("eventually_successful failed (attempt 2/3)", output)

    def test_retry_fails_after_max_attempts(self):
        """Test retry decorator when function fails after all attempts."""
        call_count = [0]

        @retry(max_attempts=3, delay=0.01)
        def always_failing():
            call_count[0] += 1
            raise ValueError("Always fails")

        captured_output = StringIO()
        sys.stdout = captured_output

        with self.assertRaises(ValueError) as context:
            always_failing()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(str(context.exception), "Always fails")
        self.assertEqual(call_count[0], 3)
        self.assertIn("always_failing failed after 3 attempts", output)

    def test_retry_configurable_attempts(self):
        """Test retry decorator with different max_attempts values."""
        call_count = [0]

        @retry(max_attempts=5, delay=0.01)
        def failing_function():
            call_count[0] += 1
            raise RuntimeError("Error")

        with self.assertRaises(RuntimeError):
            failing_function()

        self.assertEqual(call_count[0], 5)

    def test_retry_preserves_metadata(self):
        """Test that retry preserves function metadata."""
        @retry(max_attempts=2, delay=0.01)
        def documented_function():
            """Retry test function."""
            return True

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Retry test function.")


class TestValidateTypesDecorator(unittest.TestCase):
    """Test suite for the validate_types decorator."""

    def test_validate_types_with_correct_types(self):
        """Test validate_types with correct parameter types."""
        @validate_types(x=int, y=str)
        def test_function(x, y):
            return f"{x}: {y}"

        result = test_function(42, "hello")
        self.assertEqual(result, "42: hello")

    def test_validate_types_with_incorrect_types(self):
        """Test validate_types raises TypeError for incorrect parameter types."""
        @validate_types(x=int, y=str)
        def test_function(x, y):
            return f"{x}: {y}"

        with self.assertRaises(TypeError) as context:
            test_function("wrong", "hello")

        self.assertIn("Argument 'x' must be of type int", str(context.exception))
        self.assertIn("got str", str(context.exception))

    def test_validate_types_multiple_violations(self):
        """Test validate_types with multiple type violations."""
        @validate_types(x=int, y=str, z=float)
        def test_function(x, y, z):
            return x, y, z

        with self.assertRaises(TypeError):
            test_function("wrong", 123, "also_wrong")

    def test_validate_types_with_kwargs(self):
        """Test validate_types with keyword arguments."""
        @validate_types(x=int, y=str)
        def test_function(x, y="default"):
            return f"{x}: {y}"

        result = test_function(x=10, y="test")
        self.assertEqual(result, "10: test")

        with self.assertRaises(TypeError):
            test_function(x="wrong", y="test")

    def test_validate_types_partial_validation(self):
        """Test validate_types validates only specified parameters."""
        @validate_types(x=int)
        def test_function(x, y):
            return x + len(y)

        result = test_function(5, "hello")
        self.assertEqual(result, 10)

        with self.assertRaises(TypeError):
            test_function("wrong", "hello")

    def test_validate_types_preserves_metadata(self):
        """Test that validate_types preserves function metadata."""
        @validate_types(x=int)
        def documented_function(x):
            """Validation test function."""
            return x

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Validation test function.")


class TestMemoizeDecorator(unittest.TestCase):
    """Test suite for the memoize decorator."""

    def test_memoize_caches_results(self):
        """Test that memoize caches function results correctly."""
        call_count = [0]

        @memoize
        def expensive_function(x):
            call_count[0] += 1
            return x * 2

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(10)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count[0], 2)
        self.assertIn("Cache miss", output)
        self.assertIn("Cache hit", output)

    def test_memoize_cache_hits_and_misses(self):
        """Test memoize reports cache hits and misses correctly."""
        @memoize
        def test_function(x, y):
            return x + y

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = test_function(1, 2)
        result2 = test_function(1, 2)
        result3 = test_function(2, 3)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 3)
        self.assertEqual(result3, 5)

        self.assertEqual(output.count("Cache miss"), 2)
        self.assertEqual(output.count("Cache hit"), 1)

    def test_memoize_with_kwargs(self):
        """Test memoize works correctly with keyword arguments."""
        call_count = [0]

        @memoize
        def test_function(x, y=10):
            call_count[0] += 1
            return x * y

        result1 = test_function(5, y=3)
        result2 = test_function(5, y=3)
        result3 = test_function(x=5, y=3)

        self.assertEqual(result1, 15)
        self.assertEqual(result2, 15)
        self.assertEqual(result3, 15)
        self.assertEqual(call_count[0], 1)

    def test_memoize_cache_info(self):
        """Test memoize cache_info method returns correct information."""
        @memoize
        def test_function(x):
            return x * 2

        captured_output = StringIO()
        sys.stdout = captured_output

        test_function(5)
        test_function(10)
        test_function(5)

        sys.stdout = sys.__stdout__

        cache_info = test_function.cache_info()
        self.assertEqual(cache_info["cache_size"], 2)
        self.assertIn((5,), [key[0] for key in cache_info["cache"].keys()])
        self.assertIn((10,), [key[0] for key in cache_info["cache"].keys()])

    def test_memoize_cache_clear(self):
        """Test memoize cache_clear method clears the cache."""
        call_count = [0]

        @memoize
        def test_function(x):
            call_count[0] += 1
            return x * 2

        captured_output = StringIO()
        sys.stdout = captured_output

        test_function(5)
        test_function(5)

        test_function.cache_clear()

        test_function(5)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(call_count[0], 2)
        self.assertEqual(output.count("Cache miss"), 2)
        self.assertEqual(output.count("Cache hit"), 1)

    def test_memoize_with_unhashable_args(self):
        """Test memoize handles unhashable arguments gracefully."""
        call_count = [0]

        @memoize
        def test_function(x):
            call_count[0] += 1
            return len(x)

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = test_function([1, 2, 3])
        result2 = test_function([1, 2, 3])

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 3)
        self.assertEqual(call_count[0], 2)
        self.assertIn("Cannot cache", output)

    def test_memoize_preserves_metadata(self):
        """Test that memoize preserves function metadata."""
        @memoize
        def documented_function(x):
            """Memoization test function."""
            return x

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Memoization test function.")


class TestDecoratorStacking(unittest.TestCase):
    """Test suite for stacking multiple decorators together."""

    def test_timer_and_memoize_stacking(self):
        """Test that timer and memoize decorators work together."""
        call_count = [0]

        @timer
        @memoize
        def test_function(x):
            call_count[0] += 1
            time.sleep(0.05)
            return x * 2

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = test_function(5)
        result2 = test_function(5)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count[0], 1)
        self.assertIn("executed in", output)
        self.assertIn("Cache hit", output)

    def test_log_calls_and_retry_stacking(self):
        """Test that log_calls and retry decorators work together."""
        call_count = [0]

        handler = logging.StreamHandler(StringIO())
        handler.setLevel(logging.INFO)
        logger = logging.getLogger('decorators')
        logger.addHandler(handler)

        @log_calls
        @retry(max_attempts=3, delay=0.01)
        def test_function():
            call_count[0] += 1
            if call_count[0] < 2:
                raise ValueError("Retry needed")
            return "success"

        result = test_function()

        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 2)

        logger.removeHandler(handler)

    def test_validate_types_and_memoize_stacking(self):
        """Test that validate_types and memoize decorators work together."""
        call_count = [0]

        @validate_types(x=int)
        @memoize
        def test_function(x):
            call_count[0] += 1
            return x * 3

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = test_function(5)
        result2 = test_function(5)

        sys.stdout = sys.__stdout__

        self.assertEqual(result1, 15)
        self.assertEqual(result2, 15)
        self.assertEqual(call_count[0], 1)

        with self.assertRaises(TypeError):
            test_function("wrong")

    def test_triple_decorator_stacking(self):
        """Test stacking three decorators together."""
        call_count = [0]

        @timer
        @validate_types(x=int)
        @memoize
        def test_function(x):
            call_count[0] += 1
            return x ** 2

        captured_output = StringIO()
        sys.stdout = captured_output

        result1 = test_function(4)
        result2 = test_function(4)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertEqual(result1, 16)
        self.assertEqual(result2, 16)
        self.assertEqual(call_count[0], 1)
        self.assertIn("executed in", output)

    def test_stacked_decorators_preserve_metadata(self):
        """Test that stacked decorators preserve function metadata."""
        @timer
        @log_calls
        @memoize
        def documented_function(x):
            """Stacking test function."""
            return x

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Stacking test function.")


if __name__ == '__main__':
    unittest.main()
