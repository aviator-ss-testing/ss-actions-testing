"""
Decorator functions for function enhancement and demonstration of advanced Python concepts.

This module provides various decorators for:
- Performance measurement (timing)
- Function call logging
- Retry mechanisms with configurable attempts and delays
- Runtime type validation
- Result caching (memoization)
"""

import time
import logging
import functools
from typing import Any, Callable, Dict, Optional, TypeVar, Union
from inspect import signature


# Set up logging for the log_calls decorator
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

F = TypeVar('F', bound=Callable[..., Any])


def timer(func: F) -> F:
    """
    Decorator to measure and print the execution time of a function.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time when called
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper


def log_calls(func: F) -> F:
    """
    Decorator to log function calls with arguments and return values.

    Args:
        func: The function to be logged

    Returns:
        Wrapped function that logs calls when invoked
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))

        logger.info(f"Calling {func.__name__}({all_args})")

        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} returned: {repr(result)}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry function execution on failure.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        delay: Delay between retries in seconds (default: 1.0)

    Returns:
        Decorator function that retries failed executions
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"{func.__name__} failed (attempt {attempt + 1}/{max_attempts}). Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"{func.__name__} failed after {max_attempts} attempts")

            # Re-raise the last exception if all attempts failed
            raise last_exception
        return wrapper
    return decorator


def validate_types(**type_hints):
    """
    Decorator to validate function argument types at runtime.

    Args:
        **type_hints: Keyword arguments mapping parameter names to expected types

    Returns:
        Decorator function that validates types before execution

    Example:
        @validate_types(x=int, y=str)
        def my_func(x, y):
            return f"{x}: {y}"
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            sig = signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate each argument
            for param_name, expected_type in type_hints.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be of type {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def memoize(func: F) -> F:
    """
    Decorator to cache function results based on arguments (memoization).

    Args:
        func: The function to be memoized

    Returns:
        Wrapped function that caches results for repeated calls with same arguments

    Note:
        Only works with functions that have hashable arguments
    """
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from arguments
        try:
            # Convert kwargs to sorted tuple for consistent hashing
            kwargs_items = tuple(sorted(kwargs.items()))
            cache_key = (args, kwargs_items)
        except TypeError:
            # Arguments are not hashable, cannot cache
            print(f"Warning: Cannot cache {func.__name__} - arguments are not hashable")
            return func(*args, **kwargs)

        # Check if result is already cached
        if cache_key in cache:
            print(f"Cache hit for {func.__name__}")
            return cache[cache_key]

        # Compute and cache the result
        print(f"Cache miss for {func.__name__} - computing result")
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    # Add cache inspection methods
    wrapper.cache_info = lambda: {"cache_size": len(cache), "cache": dict(cache)}
    wrapper.cache_clear = lambda: cache.clear()

    return wrapper
