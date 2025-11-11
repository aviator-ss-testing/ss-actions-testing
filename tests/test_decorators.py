import unittest
import sys
import os
import time
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.decorators import timer, memoize, validate_types, retry


class TestDecorators(unittest.TestCase):

    def test_timer_measures_execution_time(self):
        """Test that timer decorator measures and prints execution time"""
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

    def test_timer_preserves_function_behavior(self):
        """Test that timer decorator doesn't change function return value"""
        @timer
        def add(a, b):
            return a + b

        captured_output = StringIO()
        sys.stdout = captured_output

        result = add(5, 3)

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 8)

    def test_timer_handles_exceptions(self):
        """Test that timer decorator allows exceptions to propagate"""
        @timer
        def failing_function():
            raise ValueError("Test error")

        captured_output = StringIO()
        sys.stdout = captured_output

        with self.assertRaises(ValueError) as context:
            failing_function()

        sys.stdout = sys.__stdout__

        self.assertEqual(str(context.exception), "Test error")

    def test_memoize_caches_results(self):
        """Test that memoize decorator caches function results"""
        call_count = {'count': 0}

        @memoize
        def expensive_function(x):
            call_count['count'] += 1
            return x * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(10)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count['count'], 2)

    def test_memoize_handles_multiple_arguments(self):
        """Test that memoize works with multiple arguments"""
        @memoize
        def multiply(a, b):
            return a * b

        result1 = multiply(3, 4)
        result2 = multiply(3, 4)
        result3 = multiply(4, 3)

        self.assertEqual(result1, 12)
        self.assertEqual(result2, 12)
        self.assertEqual(result3, 12)

    def test_memoize_cache_clear(self):
        """Test that memoize cache can be cleared"""
        call_count = {'count': 0}

        @memoize
        def counter(x):
            call_count['count'] += 1
            return x

        counter(5)
        self.assertEqual(call_count['count'], 1)

        counter(5)
        self.assertEqual(call_count['count'], 1)

        counter.cache_clear()

        counter(5)
        self.assertEqual(call_count['count'], 2)

    def test_memoize_with_kwargs(self):
        """Test that memoize handles keyword arguments"""
        @memoize
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}"

        result1 = greet("Alice", greeting="Hi")
        result2 = greet("Alice", greeting="Hi")

        self.assertEqual(result1, "Hi, Alice")
        self.assertEqual(result2, "Hi, Alice")

    def test_validate_types_accepts_correct_types(self):
        """Test that validate_types accepts arguments of correct type"""
        @validate_types(x=int, y=str)
        def process(x, y):
            return f"{y}: {x}"

        result = process(42, "Number")
        self.assertEqual(result, "Number: 42")

    def test_validate_types_rejects_wrong_positional_types(self):
        """Test that validate_types raises TypeError for wrong positional argument types"""
        @validate_types(x=int, y=str)
        def process(x, y):
            return f"{y}: {x}"

        with self.assertRaises(TypeError) as context:
            process("not an int", "text")

        self.assertIn("must be of type int", str(context.exception))

    def test_validate_types_rejects_wrong_keyword_types(self):
        """Test that validate_types raises TypeError for wrong keyword argument types"""
        @validate_types(x=int, y=str)
        def process(x, y):
            return f"{y}: {x}"

        with self.assertRaises(TypeError) as context:
            process(x=42, y=123)

        self.assertIn("must be of type str", str(context.exception))

    def test_validate_types_partial_validation(self):
        """Test that validate_types only validates specified parameters"""
        @validate_types(x=int)
        def process(x, y):
            return f"{x}-{y}"

        result = process(5, "hello")
        self.assertEqual(result, "5-hello")

    def test_validate_types_with_multiple_types(self):
        """Test validate_types with multiple argument type validations"""
        @validate_types(a=int, b=float, c=str)
        def calculate(a, b, c):
            return f"{c}: {a + b}"

        result = calculate(10, 5.5, "Sum")
        self.assertEqual(result, "Sum: 15.5")

    def test_retry_succeeds_on_first_attempt(self):
        """Test that retry decorator succeeds when function works on first try"""
        @retry(max_attempts=3)
        def reliable_function():
            return "success"

        result = reliable_function()
        self.assertEqual(result, "success")

    def test_retry_succeeds_after_failures(self):
        """Test that retry decorator retries and eventually succeeds"""
        attempt_count = {'count': 0}

        @retry(max_attempts=3, delay=0.01)
        def flaky_function():
            attempt_count['count'] += 1
            if attempt_count['count'] < 3:
                raise ValueError("Temporary error")
            return "success"

        result = flaky_function()
        self.assertEqual(result, "success")
        self.assertEqual(attempt_count['count'], 3)

    def test_retry_raises_after_max_attempts(self):
        """Test that retry decorator raises exception after max attempts exceeded"""
        @retry(max_attempts=3, delay=0.01)
        def always_fails():
            raise ValueError("Permanent error")

        with self.assertRaises(ValueError) as context:
            always_fails()

        self.assertEqual(str(context.exception), "Permanent error")

    def test_retry_with_specific_exceptions(self):
        """Test that retry only catches specified exception types"""
        @retry(max_attempts=3, delay=0.01, exceptions=(ValueError,))
        def specific_error():
            raise TypeError("Wrong error type")

        with self.assertRaises(TypeError) as context:
            specific_error()

        self.assertEqual(str(context.exception), "Wrong error type")

    def test_retry_respects_delay(self):
        """Test that retry decorator respects the delay parameter"""
        @retry(max_attempts=3, delay=0.05)
        def failing_function():
            raise ValueError("Test error")

        start_time = time.time()

        with self.assertRaises(ValueError):
            failing_function()

        elapsed_time = time.time() - start_time
        self.assertGreaterEqual(elapsed_time, 0.1)

    def test_retry_with_return_value(self):
        """Test that retry decorator preserves return values"""
        attempt_count = {'count': 0}

        @retry(max_attempts=2, delay=0.01)
        def eventually_returns_value():
            attempt_count['count'] += 1
            if attempt_count['count'] < 2:
                raise RuntimeError("Not yet")
            return 42

        result = eventually_returns_value()
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
