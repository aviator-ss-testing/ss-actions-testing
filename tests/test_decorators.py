"""
Tests for decorator functionality to ensure they properly enhance base functions.

This module contains comprehensive tests for all decorator types, verifying that:
- Decorators preserve original function behavior while adding new features
- Timing decorators return reasonable execution times
- Caching decorators actually cache results and improve performance on repeated calls
- Validation decorators properly check inputs
- Rate limiting and retry decorators work as expected
"""

import pytest
import time
import warnings
import logging
import io
import sys
from unittest.mock import patch, MagicMock

from src.decorators import (
    timer, validate_types, validate_range, validate, retry, log_calls,
    memoize, rate_limit, deprecated, type_check
)


class TestTimerDecorator:
    """Test the timer decorator functionality."""

    def test_timer_preserves_function_behavior(self, capsys):
        """Test that timer decorator preserves original function behavior."""
        @timer
        def add(x, y):
            return x + y

        result = add(3, 5)
        assert result == 8

        # Check that timing output was printed
        captured = capsys.readouterr()
        assert "add executed in" in captured.out
        assert "seconds" in captured.out

    def test_timer_preserves_function_metadata(self):
        """Test that timer decorator preserves function metadata."""
        @timer
        def test_func():
            """Test function docstring."""
            return 42

        assert test_func.__name__ == "test_func"
        assert test_func.__doc__ == "Test function docstring."

    def test_timer_measures_reasonable_execution_time(self, capsys):
        """Test that timer reports reasonable execution times."""
        @timer
        def slow_function():
            time.sleep(0.01)  # Sleep for 10ms
            return "done"

        result = slow_function()
        assert result == "done"

        captured = capsys.readouterr()
        # Extract the execution time from the output
        output_lines = captured.out.strip().split('\n')
        timing_line = [line for line in output_lines if "executed in" in line][0]

        # Parse execution time (format: "slow_function executed in X.XXXXXX seconds")
        time_str = timing_line.split("executed in ")[1].split(" seconds")[0]
        execution_time = float(time_str)

        # Should be at least 0.01 seconds (10ms) but less than 1 second
        assert 0.009 <= execution_time <= 1.0

    def test_timer_with_exception(self, capsys):
        """Test that timer works correctly when function raises exception."""
        @timer
        def failing_function():
            raise ValueError("Test error")

        with pytest.raises(ValueError, match="Test error"):
            failing_function()

        # Timer should still measure execution time even if function fails
        captured = capsys.readouterr()
        assert "failing_function executed in" in captured.out


class TestValidationDecorators:
    """Test validation decorators (types, ranges, combined)."""

    def test_validate_types_success(self):
        """Test type validation with correct types."""
        @validate_types(x=int, y=float)
        def add(x, y):
            return x + y

        result = add(5, 2.5)
        assert result == 7.5

    def test_validate_types_failure(self):
        """Test type validation with incorrect types."""
        @validate_types(x=int, y=float)
        def add(x, y):
            return x + y

        with pytest.raises(TypeError, match="Parameter 'x' must be of type int, got str"):
            add("5", 2.5)

        with pytest.raises(TypeError, match="Parameter 'y' must be of type float, got int"):
            add(5, 2)

    def test_validate_range_success(self):
        """Test range validation with values in range."""
        @validate_range(x=(0, 10), y=(-5, 5))
        def process(x, y):
            return x * y

        result = process(5, 3)
        assert result == 15

    def test_validate_range_failure(self):
        """Test range validation with values out of range."""
        @validate_range(x=(0, 10), y=(-5, 5))
        def process(x, y):
            return x * y

        with pytest.raises(ValueError, match="Parameter 'x' must be between 0 and 10, got 15"):
            process(15, 3)

        with pytest.raises(ValueError, match="Parameter 'y' must be between -5 and 5, got 10"):
            process(5, 10)

    def test_validate_combined_success(self):
        """Test combined type and range validation."""
        @validate(
            types={'x': int, 'y': float},
            ranges={'x': (0, 100), 'y': (0.0, 1.0)}
        )
        def calculate(x, y):
            return x * y

        result = calculate(50, 0.5)
        assert result == 25.0

    def test_validate_combined_type_failure(self):
        """Test combined validation with type error."""
        @validate(
            types={'x': int, 'y': float},
            ranges={'x': (0, 100), 'y': (0.0, 1.0)}
        )
        def calculate(x, y):
            return x * y

        with pytest.raises(TypeError, match="Parameter 'x' must be of type int, got str"):
            calculate("50", 0.5)

    def test_validate_combined_range_failure(self):
        """Test combined validation with range error."""
        @validate(
            types={'x': int, 'y': float},
            ranges={'x': (0, 100), 'y': (0.0, 1.0)}
        )
        def calculate(x, y):
            return x * y

        with pytest.raises(ValueError, match="Parameter 'x' must be between 0 and 100, got 150"):
            calculate(150, 0.5)

    def test_validation_preserves_function_behavior(self):
        """Test that validation decorators preserve original function behavior."""
        original_func = lambda x, y: x + y

        @validate_types(x=int, y=int)
        def decorated_func(x, y):
            return x + y

        # Test same inputs produce same outputs
        assert original_func(3, 5) == decorated_func(3, 5)
        assert decorated_func.__name__ == "decorated_func"


class TestRetryDecorator:
    """Test retry decorator functionality."""

    def test_retry_success_first_attempt(self):
        """Test retry decorator when function succeeds on first attempt."""
        call_count = 0

        @retry(max_attempts=3, delay=0.01)
        def stable_function():
            nonlocal call_count
            call_count += 1
            return "success"

        result = stable_function()
        assert result == "success"
        assert call_count == 1

    def test_retry_success_after_failures(self, capsys):
        """Test retry decorator when function succeeds after some failures."""
        call_count = 0

        @retry(max_attempts=3, delay=0.01)
        def unstable_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError(f"Attempt {call_count} failed")
            return "success"

        result = unstable_function()
        assert result == "success"
        assert call_count == 3

        # Check retry messages were printed
        captured = capsys.readouterr()
        assert "Attempt 1 failed" in captured.out
        assert "Attempt 2 failed" in captured.out
        assert "Retrying in 0.01 seconds" in captured.out

    def test_retry_all_attempts_fail(self, capsys):
        """Test retry decorator when all attempts fail."""
        call_count = 0

        @retry(max_attempts=3, delay=0.01)
        def always_failing():
            nonlocal call_count
            call_count += 1
            raise ValueError(f"Attempt {call_count} failed")

        with pytest.raises(ValueError, match="Attempt 3 failed"):
            always_failing()

        assert call_count == 3

        captured = capsys.readouterr()
        assert "All 3 attempts failed" in captured.out

    def test_retry_specific_exceptions(self):
        """Test retry decorator with specific exception types."""
        call_count = 0

        @retry(max_attempts=3, delay=0.01, exceptions=(ValueError,))
        def selective_retry():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise ValueError("This should be retried")
            elif call_count == 2:
                raise TypeError("This should not be retried")
            return "success"

        with pytest.raises(TypeError, match="This should not be retried"):
            selective_retry()

        assert call_count == 2  # Only one retry due to TypeError not being caught


class TestLogCallsDecorator:
    """Test log_calls decorator functionality."""

    def test_log_calls_default_behavior(self, caplog):
        """Test log_calls decorator with default settings."""
        with caplog.at_level(logging.INFO):
            @log_calls()
            def multiply(x, y):
                return x * y

            result = multiply(3, 4)
            assert result == 12

        # Check logging output
        log_messages = [record.message for record in caplog.records]
        assert any("Calling multiply(3, 4)" in msg for msg in log_messages)
        assert any("multiply returned: 12" in msg for msg in log_messages)

    def test_log_calls_no_args(self, caplog):
        """Test log_calls decorator without logging arguments."""
        with caplog.at_level(logging.INFO):
            @log_calls(include_args=False, include_result=True)
            def divide(x, y):
                return x / y

            result = divide(10, 2)
            assert result == 5.0

        log_messages = [record.message for record in caplog.records]
        assert any("Calling divide" == msg for msg in log_messages)
        assert any("divide returned: 5.0" in msg for msg in log_messages)

    def test_log_calls_with_exception(self, caplog):
        """Test log_calls decorator when function raises exception."""
        with caplog.at_level(logging.INFO):
            @log_calls()
            def failing_divide(x, y):
                return x / y

            with pytest.raises(ZeroDivisionError):
                failing_divide(10, 0)

        log_messages = [record.message for record in caplog.records]
        assert any("Calling failing_divide(10, 0)" in msg for msg in log_messages)
        assert any("failing_divide raised ZeroDivisionError" in msg for msg in log_messages)


class TestMemoizeDecorator:
    """Test memoization decorator functionality."""

    def test_memoize_caches_results(self):
        """Test that memoize decorator caches function results."""
        call_count = 0

        @memoize
        def expensive_calculation(n):
            nonlocal call_count
            call_count += 1
            time.sleep(0.001)  # Simulate expensive operation
            return n * n

        # First call should execute the function
        result1 = expensive_calculation(5)
        assert result1 == 25
        assert call_count == 1

        # Second call with same arguments should use cache
        result2 = expensive_calculation(5)
        assert result2 == 25
        assert call_count == 1  # Function not called again

        # Call with different arguments should execute function
        result3 = expensive_calculation(10)
        assert result3 == 100
        assert call_count == 2

    def test_memoize_performance_improvement(self):
        """Test that memoization improves performance on repeated calls."""
        @memoize
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        # Time the first calculation
        start_time = time.time()
        result1 = fibonacci(20)
        first_duration = time.time() - start_time

        # Time the second calculation (should be much faster due to caching)
        start_time = time.time()
        result2 = fibonacci(20)
        second_duration = time.time() - start_time

        assert result1 == result2 == 6765
        assert second_duration < first_duration * 0.1  # Should be at least 10x faster

    def test_memoize_cache_methods(self):
        """Test memoize decorator cache inspection methods."""
        @memoize
        def square(x):
            return x * x

        # Initially empty cache
        assert len(square.cache) == 0

        # Add some cached values
        square(5)
        square(10)
        assert len(square.cache) == 2

        # Test cache info
        cache_info = square.cache_info()
        assert cache_info['hits'] == 2

        # Test cache clear
        square.cache_clear()
        assert len(square.cache) == 0

    def test_memoize_with_kwargs(self):
        """Test memoization with keyword arguments."""
        call_count = 0

        @memoize
        def power(base, exponent=2):
            nonlocal call_count
            call_count += 1
            return base ** exponent

        # Test with different calling styles
        result1 = power(3, 4)
        result2 = power(3, exponent=4)
        result3 = power(base=3, exponent=4)

        assert result1 == result2 == result3 == 81
        assert call_count == 1  # All should use the same cache entry

    def test_memoize_with_unhashable_args(self):
        """Test memoization behavior with unhashable arguments."""
        call_count = 0

        @memoize
        def process_list(items):
            nonlocal call_count
            call_count += 1
            return sum(items)

        # Lists are not hashable, so memoization should be skipped
        result1 = process_list([1, 2, 3])
        result2 = process_list([1, 2, 3])

        assert result1 == result2 == 6
        assert call_count == 2  # Function called both times due to unhashable args


class TestRateLimitDecorator:
    """Test rate limiting decorator functionality."""

    def test_rate_limit_enforces_delay(self, capsys):
        """Test that rate limiting enforces minimum delay between calls."""
        @rate_limit(calls_per_second=10.0)  # Allow 10 calls per second (0.1s interval)
        def fast_function():
            return "result"

        start_time = time.time()

        # Make two rapid calls
        result1 = fast_function()
        result2 = fast_function()

        end_time = time.time()
        total_time = end_time - start_time

        assert result1 == result2 == "result"
        # Should take at least 0.1 seconds due to rate limiting
        assert total_time >= 0.09  # Allow for small timing variations

        captured = capsys.readouterr()
        assert "Rate limiting fast_function" in captured.out

    def test_rate_limit_no_delay_when_slow(self):
        """Test that rate limiting doesn't add delay when calls are naturally slow."""
        @rate_limit(calls_per_second=10.0)  # 0.1s minimum interval
        def slow_function():
            time.sleep(0.15)  # Naturally slower than rate limit
            return "result"

        start_time = time.time()
        result1 = slow_function()
        result2 = slow_function()
        end_time = time.time()

        total_time = end_time - start_time
        assert result1 == result2 == "result"
        # Should take about 0.3s (2 * 0.15s) without additional rate limiting delay
        assert 0.25 <= total_time <= 0.4

    def test_rate_limit_per_instance(self):
        """Test rate limiting with per-instance configuration."""
        @rate_limit(calls_per_second=5.0, per_instance=True)
        def parameterized_function(x):
            return x * 2

        start_time = time.time()

        # Different arguments should not interfere with each other's rate limiting
        result1 = parameterized_function(1)  # First call with arg 1
        result2 = parameterized_function(2)  # First call with arg 2 (should be immediate)
        result3 = parameterized_function(1)  # Second call with arg 1 (should be delayed)

        end_time = time.time()
        total_time = end_time - start_time

        assert result1 == 2
        assert result2 == 4
        assert result3 == 2

        # Should take at least 0.2s due to rate limiting on the repeated arg
        assert total_time >= 0.19


class TestDeprecatedDecorator:
    """Test deprecated decorator functionality."""

    def test_deprecated_basic_warning(self):
        """Test basic deprecation warning."""
        @deprecated()
        def old_function():
            return "legacy"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = old_function()

            assert result == "legacy"
            assert len(w) == 1
            assert issubclass(w[0].category, DeprecationWarning)
            assert "Call to deprecated function 'old_function'" in str(w[0].message)

    def test_deprecated_with_details(self):
        """Test deprecation warning with detailed information."""
        @deprecated(
            reason="Function is no longer maintained",
            version="2.0",
            alternative="new_function()"
        )
        def old_function():
            return "legacy"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = old_function()

            assert result == "legacy"
            assert len(w) == 1
            warning_msg = str(w[0].message)
            assert "deprecated since version 2.0" in warning_msg
            assert "Function is no longer maintained" in warning_msg
            assert "Use new_function() instead" in warning_msg

    def test_deprecated_preserves_functionality(self):
        """Test that deprecated decorator preserves original function behavior."""
        @deprecated()
        def calculate(x, y):
            return x + y

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = calculate(5, 3)
            assert result == 8


class TestTypeCheckDecorator:
    """Test type checking decorator functionality."""

    def test_type_check_success(self):
        """Test type checking with correct types."""
        @type_check()
        def add_numbers(x: int, y: int) -> int:
            return x + y

        result = add_numbers(3, 5)
        assert result == 8

    def test_type_check_input_failure(self):
        """Test type checking with incorrect input types."""
        @type_check(strict=True)
        def add_numbers(x: int, y: int) -> int:
            return x + y

        with pytest.raises(TypeError, match="Type mismatch for parameter 'x'"):
            add_numbers("3", 5)

    def test_type_check_return_failure(self):
        """Test type checking with incorrect return type."""
        @type_check(strict=True, check_return=True)
        def get_number() -> int:
            return "not a number"  # Wrong return type

        with pytest.raises(TypeError, match="Return type mismatch"):
            get_number()

    def test_type_check_non_strict_mode(self):
        """Test type checking in non-strict mode (warnings instead of errors)."""
        @type_check(strict=False)
        def add_numbers(x: int, y: int) -> int:
            return str(x + y)  # Wrong return type

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = add_numbers(3, 5)

            assert result == "8"  # Function still executes
            assert len(w) == 1
            assert "Return type mismatch" in str(w[0].message)

    def test_type_check_no_hints(self):
        """Test type checking when function has no type hints."""
        @type_check(strict=False)
        def no_hints_function(x, y):
            return x + y

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = no_hints_function(3, 5)

            assert result == 8
            assert len(w) == 1
            assert "No type hints found" in str(w[0].message)


class TestDecoratorCombinations:
    """Test combinations of decorators working together."""

    def test_timer_with_memoize(self, capsys):
        """Test timer and memoize decorators working together."""
        @timer
        @memoize
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        # First call should be timed and cached
        result1 = fibonacci(10)

        # Second call should be much faster due to caching
        result2 = fibonacci(10)

        assert result1 == result2 == 55

        captured = capsys.readouterr()
        # Should see timing output for both calls
        timing_lines = [line for line in captured.out.split('\n') if 'executed in' in line]
        assert len(timing_lines) >= 2

    def test_validation_with_retry(self):
        """Test validation and retry decorators working together."""
        call_count = 0

        @retry(max_attempts=3, delay=0.01)
        @validate_types(x=int, y=int)
        def unstable_add(x, y):
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise ValueError("Temporary failure")
            return x + y

        # Should succeed after retry with valid types
        result = unstable_add(3, 5)
        assert result == 8
        assert call_count == 2

        # Should fail immediately with invalid types (before retry logic)
        call_count = 0
        with pytest.raises(TypeError, match="Parameter 'x' must be of type int"):
            unstable_add("3", 5)

        assert call_count == 0  # Validation happens before function execution

    def test_multiple_decorators_preserve_metadata(self):
        """Test that multiple decorators preserve function metadata."""
        @timer
        @memoize
        @validate_types(x=int)
        def documented_function(x):
            """This function has documentation."""
            return x * 2

        assert documented_function.__name__ == "documented_function"
        assert "This function has documentation" in documented_function.__doc__


# Integration tests with actual math functions
class TestDecoratorsWithMathFunctions:
    """Test decorators integrated with actual math functions."""

    def test_timer_with_factorial(self, capsys):
        """Test timer decorator with factorial calculation."""
        from src.basic_math import factorial

        timed_factorial = timer(factorial)
        result = timed_factorial(10)

        assert result == 3628800

        captured = capsys.readouterr()
        assert "factorial executed in" in captured.out

    def test_memoize_with_fibonacci_performance(self):
        """Test memoization significantly improves fibonacci performance."""
        # Create a fibonacci function similar to what might be in basic_math
        def fibonacci_slow(n):
            if n < 2:
                return n
            return fibonacci_slow(n-1) + fibonacci_slow(n-2)

        @memoize
        def fibonacci_fast(n):
            if n < 2:
                return n
            return fibonacci_fast(n-1) + fibonacci_fast(n-2)

        # Test that memoized version is significantly faster
        start_time = time.time()
        result_fast = fibonacci_fast(25)
        fast_time = time.time() - start_time

        start_time = time.time()
        result_slow = fibonacci_slow(25)
        slow_time = time.time() - start_time

        assert result_fast == result_slow == 75025
        assert fast_time < slow_time * 0.1  # Should be at least 10x faster

    def test_validation_with_divide(self):
        """Test validation decorator with divide function."""
        from src.basic_math import divide

        @validate_types(a=(int, float), b=(int, float))
        @validate_range(b=(0.001, float('inf')))  # Prevent division by values too close to zero
        def safe_divide(a, b):
            return divide(a, b)

        # Should work with valid inputs
        result = safe_divide(10.0, 2.0)
        assert result == 5.0

        # Should fail with invalid types
        with pytest.raises(TypeError):
            safe_divide("10", 2.0)

        # Should fail with zero division
        with pytest.raises(ValueError, match="Parameter 'b' must be between 0.001"):
            safe_divide(10.0, 0.0)