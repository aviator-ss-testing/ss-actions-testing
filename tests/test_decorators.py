"""Test cases for decorator functionality module."""

import unittest
import sys
import os
import time
import logging
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import decorators


class TestTimerDecorator(unittest.TestCase):
    """Test cases for the timer decorator."""

    def test_timer_measures_execution_time(self):
        """Test that timer decorator accurately measures execution time."""
        @decorators.timer
        def slow_function():
            time.sleep(0.1)
            return "done"

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = slow_function()
            output = fake_output.getvalue()

        self.assertEqual(result, "done")
        self.assertIn("slow_function executed in", output)
        self.assertIn("seconds", output)

    def test_timer_output_format(self):
        """Test that timer decorator outputs correct format with 6 decimal places."""
        @decorators.timer
        def fast_function():
            return 42

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = fast_function()
            output = fake_output.getvalue()

        self.assertEqual(result, 42)
        self.assertRegex(output, r'fast_function executed in \d+\.\d{6} seconds')

    def test_timer_preserves_function_metadata(self):
        """Test that timer decorator preserves original function name and docstring."""
        @decorators.timer
        def documented_function():
            """This is a docstring."""
            return None

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "This is a docstring.")

    def test_timer_with_arguments(self):
        """Test that timer decorator works with functions that take arguments."""
        @decorators.timer
        def add_numbers(a, b):
            return a + b

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = add_numbers(5, 10)
            output = fake_output.getvalue()

        self.assertEqual(result, 15)
        self.assertIn("add_numbers executed in", output)


class TestLogCallsDecorator(unittest.TestCase):
    """Test cases for the log_calls decorator."""

    def setUp(self):
        """Set up logging capture before each test."""
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.INFO)
        decorators.logger.addHandler(self.handler)

    def tearDown(self):
        """Clean up logging handlers after each test."""
        decorators.logger.removeHandler(self.handler)

    def test_log_calls_captures_function_invocation(self):
        """Test that log_calls decorator captures function calls."""
        @decorators.log_calls
        def greet(name):
            return f"Hello, {name}"

        result = greet("Alice")
        log_output = self.log_capture.getvalue()

        self.assertEqual(result, "Hello, Alice")
        self.assertIn("Calling greet('Alice')", log_output)
        self.assertIn("greet returned: 'Hello, Alice'", log_output)

    def test_log_calls_captures_parameters(self):
        """Test that log_calls decorator logs both args and kwargs."""
        @decorators.log_calls
        def calculate(x, y, operation="add"):
            if operation == "add":
                return x + y
            return x - y

        result = calculate(10, 5, operation="subtract")
        log_output = self.log_capture.getvalue()

        self.assertEqual(result, 5)
        self.assertIn("Calling calculate(10, 5, operation='subtract')", log_output)
        self.assertIn("calculate returned: 5", log_output)

    def test_log_calls_handles_exceptions(self):
        """Test that log_calls decorator logs exceptions."""
        @decorators.log_calls
        def failing_function():
            raise ValueError("Test error")

        with self.assertRaises(ValueError):
            failing_function()

        log_output = self.log_capture.getvalue()
        self.assertIn("Calling failing_function()", log_output)
        self.assertIn("failing_function raised ValueError: Test error", log_output)

    def test_log_calls_with_no_arguments(self):
        """Test that log_calls decorator works with functions that have no arguments."""
        @decorators.log_calls
        def get_constant():
            return 42

        result = get_constant()
        log_output = self.log_capture.getvalue()

        self.assertEqual(result, 42)
        self.assertIn("Calling get_constant()", log_output)
        self.assertIn("get_constant returned: 42", log_output)


class TestRetryDecorator(unittest.TestCase):
    """Test cases for the retry decorator."""

    def test_retry_succeeds_on_first_attempt(self):
        """Test that retry decorator doesn't retry when function succeeds."""
        call_count = [0]

        @decorators.retry(max_attempts=3, delay=0.01)
        def successful_function():
            call_count[0] += 1
            return "success"

        result = successful_function()

        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 1)

    def test_retry_with_failing_then_succeeding(self):
        """Test that retry decorator retries and eventually succeeds."""
        call_count = [0]

        @decorators.retry(max_attempts=3, delay=0.01)
        def sometimes_failing_function():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("Temporary failure")
            return "success"

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = sometimes_failing_function()
            output = fake_output.getvalue()

        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)
        self.assertIn("Retrying", output)

    def test_retry_exhausts_all_attempts(self):
        """Test that retry decorator fails after max attempts."""
        call_count = [0]

        @decorators.retry(max_attempts=3, delay=0.01)
        def always_failing_function():
            call_count[0] += 1
            raise RuntimeError("Permanent failure")

        with patch('sys.stdout', new=StringIO()) as fake_output:
            with self.assertRaises(RuntimeError) as context:
                always_failing_function()
            output = fake_output.getvalue()

        self.assertEqual(str(context.exception), "Permanent failure")
        self.assertEqual(call_count[0], 3)
        self.assertIn("failed after 3 attempts", output)

    def test_retry_with_custom_attempts(self):
        """Test that retry decorator respects custom max_attempts parameter."""
        call_count = [0]

        @decorators.retry(max_attempts=5, delay=0.01)
        def failing_function():
            call_count[0] += 1
            raise Exception("Failure")

        with self.assertRaises(Exception):
            failing_function()

        self.assertEqual(call_count[0], 5)

    def test_retry_delay_timing(self):
        """Test that retry decorator respects delay parameter."""
        @decorators.retry(max_attempts=2, delay=0.05)
        def failing_function():
            raise Exception("Failure")

        start_time = time.time()
        with self.assertRaises(Exception):
            failing_function()
        elapsed_time = time.time() - start_time

        self.assertGreater(elapsed_time, 0.04)


class TestValidateTypesDecorator(unittest.TestCase):
    """Test cases for the validate_types decorator."""

    def test_validate_types_with_correct_types(self):
        """Test that validate_types decorator passes with correct types."""
        @decorators.validate_types(x=int, y=str)
        def process_data(x, y):
            return f"{x}: {y}"

        result = process_data(42, "hello")
        self.assertEqual(result, "42: hello")

    def test_validate_types_raises_on_incorrect_type(self):
        """Test that validate_types decorator raises TypeError for incorrect types."""
        @decorators.validate_types(x=int, y=str)
        def process_data(x, y):
            return f"{x}: {y}"

        with self.assertRaises(TypeError) as context:
            process_data("not an int", "hello")

        self.assertIn("Argument 'x' must be of type int", str(context.exception))
        self.assertIn("got str", str(context.exception))

    def test_validate_types_with_multiple_incorrect_types(self):
        """Test that validate_types decorator catches first incorrect type."""
        @decorators.validate_types(a=int, b=float, c=str)
        def compute(a, b, c):
            return a + b

        with self.assertRaises(TypeError) as context:
            compute(10, 20, 30)

        self.assertIn("Argument 'c' must be of type str", str(context.exception))
        self.assertIn("got int", str(context.exception))

    def test_validate_types_with_kwargs(self):
        """Test that validate_types decorator works with keyword arguments."""
        @decorators.validate_types(name=str, age=int)
        def create_profile(name, age):
            return {"name": name, "age": age}

        result = create_profile(name="Alice", age=30)
        self.assertEqual(result, {"name": "Alice", "age": 30})

        with self.assertRaises(TypeError):
            create_profile(name=123, age=30)

    def test_validate_types_partial_validation(self):
        """Test that validate_types only validates specified parameters."""
        @decorators.validate_types(x=int)
        def flexible_function(x, y):
            return x + y

        result = flexible_function(5, "hello")
        self.assertEqual(result, "5hello")

        with self.assertRaises(TypeError):
            flexible_function("not int", "hello")

    def test_validate_types_preserves_function_behavior(self):
        """Test that validate_types decorator doesn't alter function behavior."""
        @decorators.validate_types(numbers=list)
        def sum_list(numbers):
            return sum(numbers)

        result = sum_list([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)


class TestMemoizeDecorator(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize_caches_results(self):
        """Test that memoize decorator caches function results."""
        call_count = [0]

        @decorators.memoize
        def expensive_function(x):
            call_count[0] += 1
            return x * x

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result1 = expensive_function(5)
            result2 = expensive_function(5)
            output = fake_output.getvalue()

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 25)
        self.assertEqual(call_count[0], 1)
        self.assertIn("Cache miss", output)
        self.assertIn("Cache hit", output)

    def test_memoize_different_arguments(self):
        """Test that memoize decorator differentiates between different arguments."""
        call_count = [0]

        @decorators.memoize
        def compute(x, y):
            call_count[0] += 1
            return x + y

        with patch('sys.stdout', new=StringIO()):
            result1 = compute(1, 2)
            result2 = compute(3, 4)
            result3 = compute(1, 2)

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 7)
        self.assertEqual(result3, 3)
        self.assertEqual(call_count[0], 2)

    def test_memoize_with_kwargs(self):
        """Test that memoize decorator works with keyword arguments."""
        call_count = [0]

        @decorators.memoize
        def format_string(text, prefix=">>"):
            call_count[0] += 1
            return f"{prefix} {text}"

        with patch('sys.stdout', new=StringIO()):
            result1 = format_string("hello", prefix=">>")
            result2 = format_string("hello", prefix=">>")
            result3 = format_string("hello", prefix="<<")

        self.assertEqual(result1, ">> hello")
        self.assertEqual(result2, ">> hello")
        self.assertEqual(result3, "<< hello")
        self.assertEqual(call_count[0], 2)

    def test_memoize_cache_info(self):
        """Test that memoize decorator provides cache info."""
        @decorators.memoize
        def simple_function(x):
            return x * 2

        with patch('sys.stdout', new=StringIO()):
            simple_function(1)
            simple_function(2)
            simple_function(1)

        cache_info = simple_function.cache_info()
        self.assertEqual(cache_info["cache_size"], 2)
        self.assertIn(((1,), ()), cache_info["cache"])
        self.assertIn(((2,), ()), cache_info["cache"])

    def test_memoize_cache_clear(self):
        """Test that memoize decorator allows cache clearing."""
        call_count = [0]

        @decorators.memoize
        def counting_function(x):
            call_count[0] += 1
            return x + 1

        with patch('sys.stdout', new=StringIO()):
            counting_function(5)
            counting_function(5)
            self.assertEqual(call_count[0], 1)

            counting_function.cache_clear()

            counting_function(5)
            self.assertEqual(call_count[0], 2)

    def test_memoize_with_unhashable_arguments(self):
        """Test that memoize decorator handles unhashable arguments gracefully."""
        call_count = [0]

        @decorators.memoize
        def process_list(items):
            call_count[0] += 1
            return len(items)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = process_list([1, 2, 3])
            output = fake_output.getvalue()

        self.assertEqual(result, 3)
        self.assertEqual(call_count[0], 1)
        self.assertIn("Cannot cache", output)
        self.assertIn("arguments are not hashable", output)

    def test_memoize_preserves_function_metadata(self):
        """Test that memoize decorator preserves original function name and docstring."""
        @decorators.memoize
        def documented_function(x):
            """Calculate something."""
            return x * 2

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "Calculate something.")


if __name__ == '__main__':
    unittest.main()