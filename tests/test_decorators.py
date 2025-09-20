"""
Comprehensive unit tests for the decorators module.
Tests all decorator functions including timing, retry, cache, validation, and logging.
"""

import time
import pytest
import logging
import random
from io import StringIO
from unittest.mock import patch, Mock
from decorators import (
    timing, retry, cache, validate, validate_types,
    log_calls, simple_log
)


class TestTimingDecorator:
    """Test the timing decorator."""

    def test_timing_decorator_basic(self, capsys):
        @timing
        def test_func():
            time.sleep(0.01)
            return "result"

        result = test_func()
        assert result == "result"

        captured = capsys.readouterr()
        assert "test_func executed in" in captured.out
        assert "seconds" in captured.out

    def test_timing_decorator_with_args(self, capsys):
        @timing
        def add_numbers(a, b):
            return a + b

        result = add_numbers(5, 3)
        assert result == 8

        captured = capsys.readouterr()
        assert "add_numbers executed in" in captured.out

    def test_timing_decorator_preserves_metadata(self):
        @timing
        def documented_func():
            """This is a test function."""
            return "test"

        assert documented_func.__name__ == "documented_func"
        assert documented_func.__doc__ == "This is a test function."

    def test_timing_decorator_with_exception(self, capsys):
        @timing
        def failing_func():
            raise ValueError("Test error")

        with pytest.raises(ValueError, match="Test error"):
            failing_func()

        captured = capsys.readouterr()
        assert "failing_func executed in" in captured.out


class TestRetryDecorator:
    """Test the retry decorator."""

    def test_retry_decorator_success_first_attempt(self, capsys):
        @retry(max_attempts=3)
        def success_func():
            return "success"

        result = success_func()
        assert result == "success"

        captured = capsys.readouterr()
        assert "Attempt" not in captured.out

    def test_retry_decorator_success_after_failures(self, capsys):
        call_count = 0

        @retry(max_attempts=3, delay=0.01)
        def sometimes_fails():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("Temporary failure")
            return "success"

        result = sometimes_fails()
        assert result == "success"
        assert call_count == 3

        captured = capsys.readouterr()
        assert "Attempt 1 failed" in captured.out
        assert "Attempt 2 failed" in captured.out

    def test_retry_decorator_all_attempts_fail(self, capsys):
        @retry(max_attempts=2, delay=0.01)
        def always_fails():
            raise ValueError("Always fails")

        with pytest.raises(ValueError, match="Always fails"):
            always_fails()

        captured = capsys.readouterr()
        assert "All 2 attempts failed" in captured.out

    def test_retry_decorator_specific_exceptions(self):
        attempt_count = 0

        @retry(max_attempts=3, exceptions=(ValueError,))
        def specific_exception_func():
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count == 1:
                raise ValueError("Retry this")
            elif attempt_count == 2:
                raise TypeError("Don't retry this")
            return "success"

        with pytest.raises(TypeError, match="Don't retry this"):
            specific_exception_func()

        assert attempt_count == 2

    def test_retry_decorator_custom_delay(self):
        start_time = time.time()

        @retry(max_attempts=2, delay=0.05)
        def delay_test():
            raise ValueError("Test delay")

        with pytest.raises(ValueError):
            delay_test()

        end_time = time.time()
        assert end_time - start_time >= 0.05

    @pytest.mark.parametrize("max_attempts,expected_calls", [
        (1, 1), (2, 2), (3, 3), (5, 5)
    ])
    def test_retry_decorator_parametrized(self, max_attempts, expected_calls):
        call_count = 0

        @retry(max_attempts=max_attempts, delay=0.001)
        def counting_func():
            nonlocal call_count
            call_count += 1
            raise ValueError("Always fail")

        with pytest.raises(ValueError):
            counting_func()

        assert call_count == expected_calls


class TestCacheDecorator:
    """Test the cache decorator."""

    def test_cache_decorator_basic(self):
        call_count = 0

        @cache(maxsize=10)
        def expensive_func(n):
            nonlocal call_count
            call_count += 1
            return n * 2

        result1 = expensive_func(5)
        result2 = expensive_func(5)
        result3 = expensive_func(10)

        assert result1 == 10
        assert result2 == 10
        assert result3 == 20
        assert call_count == 2

    def test_cache_decorator_with_kwargs(self):
        call_count = 0

        @cache(maxsize=5)
        def func_with_kwargs(a, b=10):
            nonlocal call_count
            call_count += 1
            return a + b

        result1 = func_with_kwargs(5, b=10)
        result2 = func_with_kwargs(5, b=10)
        result3 = func_with_kwargs(5, b=20)

        assert result1 == 15
        assert result2 == 15
        assert result3 == 25
        assert call_count == 2

    def test_cache_decorator_maxsize_limit(self):
        call_count = 0

        @cache(maxsize=2)
        def limited_cache(n):
            nonlocal call_count
            call_count += 1
            return n * 2

        limited_cache(1)
        limited_cache(2)
        limited_cache(3)
        limited_cache(1)

        assert call_count == 4

    def test_cache_decorator_unlimited(self):
        call_count = 0

        @cache(maxsize=None)
        def unlimited_cache(n):
            nonlocal call_count
            call_count += 1
            return n * 2

        for i in range(100):
            unlimited_cache(i)

        for i in range(100):
            unlimited_cache(i)

        assert call_count == 100

    def test_cache_info_method(self):
        @cache(maxsize=5)
        def test_func(n):
            return n

        test_func(1)
        test_func(2)
        test_func(1)

        info = test_func.cache_info()
        assert 'currsize' in info
        assert 'maxsize' in info
        assert info['maxsize'] == 5

    def test_cache_clear_method(self):
        call_count = 0

        @cache(maxsize=5)
        def clearable_func(n):
            nonlocal call_count
            call_count += 1
            return n

        clearable_func(1)
        clearable_func(1)
        assert call_count == 1

        clearable_func.cache_clear()
        clearable_func(1)
        assert call_count == 2


class TestValidateDecorator:
    """Test the validate decorator."""

    def test_validate_decorator_basic(self):
        def is_positive(x):
            return x > 0

        @validate(is_positive)
        def positive_only(n):
            return n * 2

        assert positive_only(5) == 10

        with pytest.raises(ValueError, match="failed validation"):
            positive_only(-1)

    def test_validate_decorator_multiple_validators(self):
        def is_integer(x):
            return isinstance(x, int)

        def is_positive(x):
            return x > 0

        @validate(is_integer, is_positive)
        def int_positive_only(n):
            return n * 2

        assert int_positive_only(5) == 10

        with pytest.raises(ValueError):
            int_positive_only(5.5)

        with pytest.raises(ValueError):
            int_positive_only(-1)

    def test_validate_decorator_with_kwargs(self):
        def is_string(x):
            return isinstance(x, str)

        @validate(is_string)
        def string_only(name, greeting="hello"):
            return f"{greeting} {name}"

        assert string_only("world") == "hello world"
        assert string_only("test", greeting="hi") == "hi test"

        with pytest.raises(ValueError):
            string_only(123)

        with pytest.raises(ValueError):
            string_only("name", greeting=456)

    def test_validate_decorator_preserves_metadata(self):
        def dummy_validator(x):
            return True

        @validate(dummy_validator)
        def documented_func():
            """Test function."""
            return "test"

        assert documented_func.__name__ == "documented_func"
        assert documented_func.__doc__ == "Test function."


class TestValidateTypesDecorator:
    """Test the validate_types decorator."""

    def test_validate_types_basic(self):
        @validate_types(name=str, age=int)
        def create_person(name, age):
            return {"name": name, "age": age}

        result = create_person("John", 30)
        assert result == {"name": "John", "age": 30}

        with pytest.raises(TypeError, match="expected str"):
            create_person(123, 30)

        with pytest.raises(TypeError, match="expected int"):
            create_person("John", "30")

    def test_validate_types_with_defaults(self):
        @validate_types(name=str, age=int, active=bool)
        def create_user(name, age, active=True):
            return {"name": name, "age": age, "active": active}

        result = create_user("Alice", 25)
        assert result == {"name": "Alice", "age": 25, "active": True}

        result = create_user("Bob", 35, active=False)
        assert result == {"name": "Bob", "age": 35, "active": False}

    def test_validate_types_partial_validation(self):
        @validate_types(name=str)
        def partial_validation(name, value):
            return f"{name}: {value}"

        assert partial_validation("test", 123) == "test: 123"
        assert partial_validation("test", [1, 2, 3]) == "test: [1, 2, 3]"

        with pytest.raises(TypeError):
            partial_validation(456, "value")

    @pytest.mark.parametrize("name,age,should_pass", [
        ("John", 30, True),
        (123, 30, False),
        ("John", "30", False),
        ("", 0, True),
    ])
    def test_validate_types_parametrized(self, name, age, should_pass):
        @validate_types(name=str, age=int)
        def test_func(name, age):
            return f"{name} is {age}"

        if should_pass:
            result = test_func(name, age)
            assert isinstance(result, str)
        else:
            with pytest.raises(TypeError):
                test_func(name, age)


class TestLogCallsDecorator:
    """Test the log_calls decorator."""

    def test_log_calls_basic(self, caplog):
        with caplog.at_level(logging.INFO):
            @log_calls()
            def test_func(x, y):
                return x + y

            result = test_func(3, 5)
            assert result == 8

            assert "Calling test_func(3, 5)" in caplog.text
            assert "test_func returned 8" in caplog.text

    def test_log_calls_with_kwargs(self, caplog):
        with caplog.at_level(logging.INFO):
            @log_calls()
            def test_func(a, b=10):
                return a * b

            result = test_func(5, b=3)
            assert result == 15

            assert "Calling test_func(5, b=3)" in caplog.text
            assert "test_func returned 15" in caplog.text

    def test_log_calls_with_exception(self, caplog):
        with caplog.at_level(logging.ERROR):
            @log_calls()
            def failing_func():
                raise ValueError("Test error")

            with pytest.raises(ValueError):
                failing_func()

            assert "failing_func raised ValueError: Test error" in caplog.text

    def test_log_calls_custom_logger(self, caplog):
        custom_logger = logging.getLogger("test_logger")

        with caplog.at_level(logging.INFO, logger="test_logger"):
            @log_calls(logger_name="test_logger")
            def test_func():
                return "test"

            test_func()

            assert "Calling test_func()" in caplog.text

    def test_log_calls_custom_level(self, caplog):
        with caplog.at_level(logging.DEBUG):
            @log_calls(level=logging.DEBUG)
            def debug_func():
                return "debug"

            debug_func()

            assert "Calling debug_func()" in caplog.text


class TestSimpleLogDecorator:
    """Test the simple_log decorator."""

    def test_simple_log_basic(self, capsys):
        @simple_log()
        def test_func():
            return "result"

        result = test_func()
        assert result == "result"

        captured = capsys.readouterr()
        assert "Calling test_func()" in captured.out
        assert "test_func completed successfully -> 'result'" in captured.out

    def test_simple_log_with_message(self, capsys):
        @simple_log("Processing data")
        def process_func(data):
            return len(data)

        result = process_func([1, 2, 3])
        assert result == 3

        captured = capsys.readouterr()
        assert "Processing data Calling process_func([1, 2, 3])" in captured.out
        assert "Processing data process_func completed successfully -> 3" in captured.out

    def test_simple_log_with_exception(self, capsys):
        @simple_log("Error test")
        def failing_func():
            raise RuntimeError("Test error")

        with pytest.raises(RuntimeError, match="Test error"):
            failing_func()

        captured = capsys.readouterr()
        assert "Error test Calling failing_func()" in captured.out
        assert "Error test failing_func failed with RuntimeError: Test error" in captured.out

    def test_simple_log_with_args_and_kwargs(self, capsys):
        @simple_log("Math operation")
        def calculate(a, b, operation="add"):
            if operation == "add":
                return a + b
            return a - b

        result = calculate(10, 5, operation="subtract")
        assert result == 5

        captured = capsys.readouterr()
        assert "Math operation Calling calculate(10, 5, operation='subtract')" in captured.out
        assert "Math operation calculate completed successfully -> 5" in captured.out


class TestDecoratorComposition:
    """Test decorator composition and interaction."""

    def test_timing_and_cache_composition(self, capsys):
        call_count = 0

        @timing
        @cache(maxsize=5)
        def composed_func(n):
            nonlocal call_count
            call_count += 1
            time.sleep(0.01)
            return n * 2

        result1 = composed_func(5)
        result2 = composed_func(5)

        assert result1 == 10
        assert result2 == 10
        assert call_count == 1

        captured = capsys.readouterr()
        assert "composed_func executed in" in captured.out

    def test_retry_and_validate_composition(self):
        attempt_count = 0

        def is_positive(x):
            return x > 0

        @retry(max_attempts=3, delay=0.001)
        @validate(is_positive)
        def retry_validate_func(n):
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count < 2:
                raise ValueError("Temporary failure")
            return n * 2

        result = retry_validate_func(5)
        assert result == 10
        assert attempt_count == 2

        with pytest.raises(ValueError, match="failed validation"):
            retry_validate_func(-1)

    def test_multiple_decorators(self, capsys):
        @simple_log("Testing")
        @cache(maxsize=3)
        @validate_types(n=int)
        def multi_decorated_func(n):
            return n ** 2

        result1 = multi_decorated_func(4)
        result2 = multi_decorated_func(4)

        assert result1 == 16
        assert result2 == 16

        captured = capsys.readouterr()
        assert "Testing Calling" in captured.out

        with pytest.raises(TypeError):
            multi_decorated_func("not an int")


class TestDecoratorErrorHandling:
    """Test error handling in decorators."""

    def test_cache_with_unhashable_args(self):
        @cache(maxsize=5)
        def unhashable_args_func(data):
            return len(data)

        with pytest.raises(TypeError):
            unhashable_args_func([1, 2, 3])

    def test_validate_with_no_validators(self):
        @validate()
        def no_validators_func(x):
            return x

        assert no_validators_func(42) == 42

    def test_retry_with_zero_attempts(self):
        with pytest.raises(ValueError):
            @retry(max_attempts=0)
            def zero_attempts_func():
                return "test"