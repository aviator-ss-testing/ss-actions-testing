"""
Decorator utilities for enhancing function behavior.

This module provides decorators for timing, validation, retry logic, logging,
caching, rate limiting, deprecation warnings, and type checking to enhance
existing functions without modifying their core logic.
"""

import time
import functools
import logging
import warnings
import threading
from typing import Any, Callable, Dict, List, Union, get_type_hints

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer(func: Callable) -> Callable:
    """
    Decorator that measures and prints the execution time of a function.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper


def validate_types(**type_checks: type) -> Callable:
    """
    Decorator that validates input parameter types and ranges.

    Args:
        **type_checks: Keyword arguments mapping parameter names to expected types

    Returns:
        Decorator function that validates inputs

    Example:
        @validate_types(x=int, y=float)
        def add(x, y):
            return x + y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature for parameter names
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate types
            for param_name, expected_type in type_checks.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Parameter '{param_name}' must be of type {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_range(**range_checks: Dict[str, tuple]) -> Callable:
    """
    Decorator that validates input parameter ranges.

    Args:
        **range_checks: Keyword arguments mapping parameter names to (min, max) tuples

    Returns:
        Decorator function that validates ranges

    Example:
        @validate_range(x=(0, 100), y=(-10, 10))
        def process(x, y):
            return x + y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature for parameter names
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate ranges
            for param_name, (min_val, max_val) in range_checks.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, (int, float)):
                        continue  # Skip non-numeric values
                    if not (min_val <= value <= max_val):
                        raise ValueError(
                            f"Parameter '{param_name}' must be between {min_val} and {max_val}, "
                            f"got {value}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)) -> Callable:
    """
    Decorator that retries function calls on failure with configurable attempts.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        delay: Delay in seconds between retries (default: 1.0)
        exceptions: Tuple of exceptions to catch and retry on (default: (Exception,))

    Returns:
        Decorator function that implements retry logic

    Example:
        @retry(max_attempts=5, delay=0.5, exceptions=(ValueError, TypeError))
        def unstable_function():
            # Function that might fail
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed for {func.__name__}: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed for {func.__name__}")

            # If we get here, all attempts failed
            raise last_exception
        return wrapper
    return decorator


def log_calls(include_args: bool = True, include_result: bool = True) -> Callable:
    """
    Decorator that logs function calls and results for debugging.

    Args:
        include_args: Whether to include function arguments in the log (default: True)
        include_result: Whether to include function result in the log (default: True)

    Returns:
        Decorator function that logs function calls

    Example:
        @log_calls(include_args=True, include_result=False)
        def calculate(x, y):
            return x * y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log function call
            if include_args:
                args_str = ", ".join(repr(arg) for arg in args)
                kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
                all_args = ", ".join(filter(None, [args_str, kwargs_str]))
                logger.info(f"Calling {func.__name__}({all_args})")
            else:
                logger.info(f"Calling {func.__name__}")

            # Execute function
            try:
                result = func(*args, **kwargs)

                # Log result
                if include_result:
                    logger.info(f"{func.__name__} returned: {repr(result)}")
                else:
                    logger.info(f"{func.__name__} completed successfully")

                return result

            except Exception as e:
                logger.error(f"{func.__name__} raised {type(e).__name__}: {e}")
                raise

        return wrapper
    return decorator


# Convenience decorator that combines validation decorators
def validate(types: Dict[str, type] = None, ranges: Dict[str, tuple] = None) -> Callable:
    """
    Convenience decorator that combines type and range validation.

    Args:
        types: Dictionary mapping parameter names to expected types
        ranges: Dictionary mapping parameter names to (min, max) tuples

    Returns:
        Decorator function that validates both types and ranges

    Example:
        @validate(types={'x': int, 'y': float}, ranges={'x': (0, 100)})
        def process(x, y):
            return x * y
    """
    def decorator(func: Callable) -> Callable:
        # Apply type validation if specified
        if types:
            func = validate_types(**types)(func)

        # Apply range validation if specified
        if ranges:
            func = validate_range(**ranges)(func)

        return func
    return decorator


def memoize(func: Callable) -> Callable:
    """
    Simple memoization decorator for caching function results.

    Caches function results based on arguments to avoid repeated computations.
    Works with functions that have hashable arguments.

    Args:
        func: The function to memoize

    Returns:
        Wrapped function that caches results

    Example:
        @memoize
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        try:
            # Convert kwargs to sorted tuple for consistent hashing
            kwargs_tuple = tuple(sorted(kwargs.items()))
            cache_key = (args, kwargs_tuple)
        except TypeError:
            # If arguments are not hashable, don't cache
            return func(*args, **kwargs)

        # Return cached result if available
        if cache_key in cache:
            return cache[cache_key]

        # Compute and cache result
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: {'hits': len(cache), 'cached_results': list(cache.keys())}

    return wrapper


def rate_limit(calls_per_second: float = 1.0, per_instance: bool = False) -> Callable:
    """
    Rate limiting decorator that prevents too frequent function calls.

    Limits the frequency of function calls by introducing delays when necessary.

    Args:
        calls_per_second: Maximum number of calls allowed per second (default: 1.0)
        per_instance: If True, rate limit per function instance, otherwise globally (default: False)

    Returns:
        Decorator function that implements rate limiting

    Example:
        @rate_limit(calls_per_second=2.0)
        def api_call():
            return "API response"
    """
    min_interval = 1.0 / calls_per_second

    def decorator(func: Callable) -> Callable:
        last_called = {}
        lock = threading.Lock()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                # Determine key for tracking calls
                if per_instance:
                    # Use function + args as key for per-instance limiting
                    try:
                        key = (func.__name__, args, tuple(sorted(kwargs.items())))
                    except TypeError:
                        key = func.__name__  # Fallback if args not hashable
                else:
                    # Global limiting for this function
                    key = func.__name__

                current_time = time.time()

                # Check if we need to wait
                if key in last_called:
                    time_since_last = current_time - last_called[key]
                    if time_since_last < min_interval:
                        sleep_time = min_interval - time_since_last
                        print(f"Rate limiting {func.__name__}: sleeping {sleep_time:.3f}s")
                        time.sleep(sleep_time)
                        current_time = time.time()

                last_called[key] = current_time

            return func(*args, **kwargs)

        return wrapper
    return decorator


def deprecated(reason: str = "", version: str = "", alternative: str = "") -> Callable:
    """
    Decorator that warns when deprecated functions are called.

    Issues a DeprecationWarning when the decorated function is called,
    providing information about deprecation reason and alternatives.

    Args:
        reason: Reason for deprecation (default: "")
        version: Version when function was deprecated (default: "")
        alternative: Suggested alternative function or approach (default: "")

    Returns:
        Decorator function that issues deprecation warnings

    Example:
        @deprecated(reason="Use new_function instead", version="2.0", alternative="new_function()")
        def old_function():
            return "legacy behavior"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Build warning message
            warning_msg = f"Call to deprecated function '{func.__name__}'"

            if version:
                warning_msg += f" (deprecated since version {version})"

            if reason:
                warning_msg += f": {reason}"

            if alternative:
                warning_msg += f". Use {alternative} instead"

            # Issue deprecation warning
            warnings.warn(
                warning_msg,
                category=DeprecationWarning,
                stacklevel=2
            )

            return func(*args, **kwargs)

        return wrapper
    return decorator


def type_check(strict: bool = True, check_return: bool = True) -> Callable:
    """
    Type checking decorator that validates input and output types based on type hints.

    Validates function arguments and return values against their type annotations.

    Args:
        strict: If True, raises TypeError on mismatch; if False, issues warning (default: True)
        check_return: Whether to validate return type (default: True)

    Returns:
        Decorator function that validates types

    Example:
        @type_check()
        def add_numbers(x: int, y: int) -> int:
            return x + y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get type hints
            try:
                type_hints = get_type_hints(func)
            except (NameError, AttributeError):
                # No type hints available, skip validation
                if not strict:
                    warnings.warn(f"No type hints found for function '{func.__name__}'")
                return func(*args, **kwargs)

            # Get function signature for parameter names
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate input types
            for param_name, value in bound_args.arguments.items():
                if param_name in type_hints and param_name != 'return':
                    expected_type = type_hints[param_name]

                    # Handle Union types and other special typing constructs
                    if hasattr(expected_type, '__origin__'):
                        # Skip complex generic types for now
                        continue

                    if not isinstance(value, expected_type):
                        error_msg = (
                            f"Type mismatch for parameter '{param_name}' in function '{func.__name__}': "
                            f"expected {expected_type.__name__}, got {type(value).__name__}"
                        )

                        if strict:
                            raise TypeError(error_msg)
                        else:
                            warnings.warn(error_msg)

            # Execute function
            result = func(*args, **kwargs)

            # Validate return type if requested
            if check_return and 'return' in type_hints:
                expected_return_type = type_hints['return']

                # Skip complex generic types
                if not hasattr(expected_return_type, '__origin__'):
                    if not isinstance(result, expected_return_type):
                        error_msg = (
                            f"Return type mismatch in function '{func.__name__}': "
                            f"expected {expected_return_type.__name__}, got {type(result).__name__}"
                        )

                        if strict:
                            raise TypeError(error_msg)
                        else:
                            warnings.warn(error_msg)

            return result

        return wrapper
    return decorator