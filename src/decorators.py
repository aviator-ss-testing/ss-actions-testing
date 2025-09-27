"""
Decorator utilities for enhancing function behavior.

This module provides decorators for timing, validation, retry logic, and logging
to enhance existing functions without modifying their core logic.
"""

import time
import functools
import logging
from typing import Any, Callable, Dict, List, Union

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