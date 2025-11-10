import unittest
import time
from io import StringIO
import sys
from decorators import timer, retry, validate_types, memoize


class TestTimerDecorator(unittest.TestCase):
    def test_timer_captures_execution_time(self):
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

    def test_timer_preserves_function_name(self):
        @timer
        def my_function():
            return 42

        self.assertEqual(my_function.__name__, "my_function")

    def test_timer_with_arguments(self):
        @timer
        def add_numbers(a, b):
            return a + b

        captured_output = StringIO()
        sys.stdout = captured_output

        result = add_numbers(5, 3)

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 8)


class TestRetryDecorator(unittest.TestCase):
    def test_retry_succeeds_on_first_attempt(self):
        @retry(attempts=3, delay=0.01)
        def successful_function():
            return "success"

        result = successful_function()
        self.assertEqual(result, "success")

    def test_retry_succeeds_after_failures(self):
        call_count = {"count": 0}

        @retry(attempts=3, delay=0.01)
        def eventually_succeeds():
            call_count["count"] += 1
            if call_count["count"] < 3:
                raise ValueError("Not yet")
            return "success"

        result = eventually_succeeds()
        self.assertEqual(result, "success")
        self.assertEqual(call_count["count"], 3)

    def test_retry_exhausts_attempts(self):
        call_count = {"count": 0}

        @retry(attempts=3, delay=0.01)
        def always_fails():
            call_count["count"] += 1
            raise ValueError("Always fails")

        with self.assertRaises(ValueError) as cm:
            always_fails()

        self.assertEqual(str(cm.exception), "Always fails")
        self.assertEqual(call_count["count"], 3)

    def test_retry_invalid_attempts(self):
        with self.assertRaises(ValueError) as cm:
            @retry(attempts=0, delay=0.01)
            def func():
                pass

        self.assertIn("positive integer", str(cm.exception))

    def test_retry_invalid_delay(self):
        with self.assertRaises(ValueError) as cm:
            @retry(attempts=3, delay=-1)
            def func():
                pass

        self.assertIn("non-negative", str(cm.exception))

    def test_retry_with_different_exceptions(self):
        call_count = {"count": 0}

        @retry(attempts=2, delay=0.01)
        def raises_different_exceptions():
            call_count["count"] += 1
            if call_count["count"] == 1:
                raise ValueError("First error")
            raise TypeError("Second error")

        with self.assertRaises(TypeError) as cm:
            raises_different_exceptions()

        self.assertEqual(str(cm.exception), "Second error")
        self.assertEqual(call_count["count"], 2)


class TestValidateTypesDecorator(unittest.TestCase):
    def test_validate_types_correct_types(self):
        @validate_types
        def add(a: int, b: int) -> int:
            return a + b

        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_validate_types_incorrect_positional_arg(self):
        @validate_types
        def add(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError) as cm:
            add(5, "3")

        self.assertIn("'b'", str(cm.exception))
        self.assertIn("int", str(cm.exception))
        self.assertIn("str", str(cm.exception))

    def test_validate_types_incorrect_first_arg(self):
        @validate_types
        def multiply(x: int, y: int) -> int:
            return x * y

        with self.assertRaises(TypeError) as cm:
            multiply("5", 3)

        self.assertIn("'x'", str(cm.exception))
        self.assertIn("int", str(cm.exception))
        self.assertIn("str", str(cm.exception))

    def test_validate_types_with_kwargs(self):
        @validate_types
        def greet(name: str, age: int):
            return f"{name} is {age}"

        result = greet(name="Alice", age=30)
        self.assertEqual(result, "Alice is 30")

    def test_validate_types_incorrect_kwarg(self):
        @validate_types
        def greet(name: str, age: int):
            return f"{name} is {age}"

        with self.assertRaises(TypeError) as cm:
            greet(name="Alice", age="30")

        self.assertIn("'age'", str(cm.exception))
        self.assertIn("int", str(cm.exception))
        self.assertIn("str", str(cm.exception))

    def test_validate_types_mixed_args_kwargs(self):
        @validate_types
        def process(value: int, multiplier: int):
            return value * multiplier

        result = process(10, multiplier=5)
        self.assertEqual(result, 50)

    def test_validate_types_no_annotations(self):
        @validate_types
        def no_types(a, b):
            return a + b

        result = no_types(1, 2)
        self.assertEqual(result, 3)

        result = no_types("hello", "world")
        self.assertEqual(result, "helloworld")

    def test_validate_types_string_parameter(self):
        @validate_types
        def repeat(text: str, times: int) -> str:
            return text * times

        result = repeat("ha", 3)
        self.assertEqual(result, "hahaha")

        with self.assertRaises(TypeError):
            repeat(123, 3)


class TestMemoizeDecorator(unittest.TestCase):
    def test_memoize_caches_results(self):
        call_count = {"count": 0}

        @memoize
        def expensive_function(n):
            call_count["count"] += 1
            return n * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count["count"], 1)

    def test_memoize_different_arguments(self):
        call_count = {"count": 0}

        @memoize
        def add(a, b):
            call_count["count"] += 1
            return a + b

        result1 = add(2, 3)
        result2 = add(4, 5)
        result3 = add(2, 3)

        self.assertEqual(result1, 5)
        self.assertEqual(result2, 9)
        self.assertEqual(result3, 5)
        self.assertEqual(call_count["count"], 2)

    def test_memoize_with_kwargs(self):
        call_count = {"count": 0}

        @memoize
        def calculate(x, y):
            call_count["count"] += 1
            return x * y

        result1 = calculate(x=3, y=4)
        result2 = calculate(x=3, y=4)

        self.assertEqual(result1, 12)
        self.assertEqual(result2, 12)
        self.assertEqual(call_count["count"], 1)

    def test_memoize_cache_clear(self):
        call_count = {"count": 0}

        @memoize
        def square(n):
            call_count["count"] += 1
            return n * n

        result1 = square(5)
        self.assertEqual(call_count["count"], 1)

        square.cache_clear()

        result2 = square(5)
        self.assertEqual(result2, 25)
        self.assertEqual(call_count["count"], 2)

    def test_memoize_cache_attribute(self):
        @memoize
        def add(a, b):
            return a + b

        add(2, 3)
        add(4, 5)

        self.assertEqual(len(add.cache), 2)
        self.assertIn(((2, 3), ()), add.cache)
        self.assertIn(((4, 5), ()), add.cache)

    def test_memoize_with_zero_arguments(self):
        call_count = {"count": 0}

        @memoize
        def get_constant():
            call_count["count"] += 1
            return 42

        result1 = get_constant()
        result2 = get_constant()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        self.assertEqual(call_count["count"], 1)

    def test_memoize_preserves_function_name(self):
        @memoize
        def my_function():
            return "test"

        self.assertEqual(my_function.__name__, "my_function")


if __name__ == "__main__":
    unittest.main()
