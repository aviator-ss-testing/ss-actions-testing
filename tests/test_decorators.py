import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.decorators import timer, memoize, validate_types, retry, log_calls


class TestTimer(unittest.TestCase):

    def test_timer_executes_function(self):
        @timer
        def simple_function():
            return 42

        result = simple_function()
        self.assertEqual(result, 42)

    def test_timer_completes_with_delay(self):
        @timer
        def delayed_function():
            time.sleep(0.01)
            return "done"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = delayed_function()
            output = mock_stdout.getvalue()

        self.assertEqual(result, "done")
        self.assertIn("delayed_function took", output)
        self.assertIn("seconds to execute", output)

    def test_timer_preserves_metadata(self):
        @timer
        def documented_function():
            """This is a test function."""
            return "test"

        self.assertEqual(documented_function.__name__, "documented_function")
        self.assertEqual(documented_function.__doc__, "This is a test function.")


class TestMemoize(unittest.TestCase):

    def test_memoize_caches_results(self):
        call_count = [0]

        @memoize
        def expensive_function(x):
            call_count[0] += 1
            return x * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)
        result3 = expensive_function(10)
        result4 = expensive_function(5)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(result3, 20)
        self.assertEqual(result4, 10)
        self.assertEqual(call_count[0], 2)

    def test_memoize_with_side_effects(self):
        side_effect_tracker = []

        @memoize
        def function_with_side_effect(x):
            side_effect_tracker.append(x)
            return x + 1

        function_with_side_effect(1)
        function_with_side_effect(1)
        function_with_side_effect(2)
        function_with_side_effect(1)

        self.assertEqual(side_effect_tracker, [1, 2])

    def test_memoize_cache_accessible(self):
        @memoize
        def cacheable_function(a, b):
            return a + b

        cacheable_function(1, 2)
        cacheable_function(3, 4)

        self.assertIn((1, 2), cacheable_function.cache)
        self.assertIn((3, 4), cacheable_function.cache)
        self.assertEqual(cacheable_function.cache[(1, 2)], 3)
        self.assertEqual(cacheable_function.cache[(3, 4)], 7)

    def test_memoize_preserves_metadata(self):
        @memoize
        def add(x, y):
            """Adds two numbers."""
            return x + y

        self.assertEqual(add.__name__, "add")
        self.assertEqual(add.__doc__, "Adds two numbers.")


class TestValidateTypes(unittest.TestCase):

    def test_validate_types_correct_types_pass(self):
        @validate_types(int, int)
        def add(a, b):
            return a + b

        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_validate_types_incorrect_type_raises_error(self):
        @validate_types(int, int)
        def add(a, b):
            return a + b

        with self.assertRaises(TypeError) as context:
            add("5", 10)

        self.assertIn("argument 0 must be int", str(context.exception))
        self.assertIn("got str", str(context.exception))

    def test_validate_types_multiple_incorrect_types(self):
        @validate_types(str, int, float)
        def process(text, count, ratio):
            return f"{text}: {count * ratio}"

        with self.assertRaises(TypeError) as context:
            process("test", "not_int", 1.5)

        self.assertIn("argument 1 must be int", str(context.exception))

    def test_validate_types_wrong_number_of_arguments(self):
        @validate_types(int, int)
        def add(a, b):
            return a + b

        with self.assertRaises(TypeError) as context:
            add(5, 10, 15)

        self.assertIn("expects 2 arguments", str(context.exception))
        self.assertIn("got 3", str(context.exception))

    def test_validate_types_preserves_metadata(self):
        @validate_types(int)
        def square(n):
            """Returns the square of n."""
            return n * n

        self.assertEqual(square.__name__, "square")
        self.assertEqual(square.__doc__, "Returns the square of n.")


class TestRetry(unittest.TestCase):

    def test_retry_succeeds_on_first_attempt(self):
        @retry(max_attempts=3)
        def successful_function():
            return "success"

        result = successful_function()
        self.assertEqual(result, "success")

    def test_retry_succeeds_after_failures(self):
        attempt_counter = [0]

        @retry(max_attempts=3)
        def flaky_function():
            attempt_counter[0] += 1
            if attempt_counter[0] < 3:
                raise ValueError("Temporary failure")
            return "success"

        result = flaky_function()
        self.assertEqual(result, "success")
        self.assertEqual(attempt_counter[0], 3)

    def test_retry_fails_after_max_attempts(self):
        @retry(max_attempts=3)
        def always_failing_function():
            raise RuntimeError("Permanent failure")

        with self.assertRaises(RuntimeError) as context:
            always_failing_function()

        self.assertEqual(str(context.exception), "Permanent failure")

    def test_retry_attempts_correct_number_of_times(self):
        attempt_counter = [0]

        @retry(max_attempts=5)
        def counting_function():
            attempt_counter[0] += 1
            raise ValueError("Always fails")

        with self.assertRaises(ValueError):
            counting_function()

        self.assertEqual(attempt_counter[0], 5)

    def test_retry_preserves_metadata(self):
        @retry(max_attempts=2)
        def api_call():
            """Makes an API call."""
            return "data"

        self.assertEqual(api_call.__name__, "api_call")
        self.assertEqual(api_call.__doc__, "Makes an API call.")


class TestLogCalls(unittest.TestCase):

    def test_log_calls_logs_function_call(self):
        @log_calls
        def greet(name):
            return f"Hello, {name}!"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = greet("Alice")
            output = mock_stdout.getvalue()

        self.assertEqual(result, "Hello, Alice!")
        self.assertIn("Calling greet('Alice')", output)
        self.assertIn("greet returned 'Hello, Alice!'", output)

    def test_log_calls_with_multiple_arguments(self):
        @log_calls
        def add(a, b):
            return a + b

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = add(5, 10)
            output = mock_stdout.getvalue()

        self.assertEqual(result, 15)
        self.assertIn("Calling add(5, 10)", output)
        self.assertIn("add returned 15", output)

    def test_log_calls_with_kwargs(self):
        @log_calls
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = greet("Bob", greeting="Hi")
            output = mock_stdout.getvalue()

        self.assertEqual(result, "Hi, Bob!")
        self.assertIn("Calling greet('Bob', greeting='Hi')", output)
        self.assertIn("greet returned 'Hi, Bob!'", output)

    def test_log_calls_with_no_arguments(self):
        @log_calls
        def get_timestamp():
            return 123456

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_timestamp()
            output = mock_stdout.getvalue()

        self.assertEqual(result, 123456)
        self.assertIn("Calling get_timestamp()", output)
        self.assertIn("get_timestamp returned 123456", output)

    def test_log_calls_preserves_metadata(self):
        @log_calls
        def calculate(x, y):
            """Calculates something."""
            return x * y

        self.assertEqual(calculate.__name__, "calculate")
        self.assertEqual(calculate.__doc__, "Calculates something.")


if __name__ == '__main__':
    unittest.main()
