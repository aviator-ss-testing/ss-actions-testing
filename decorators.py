"""Function decorators for timing, retry logic, memoization, and type validation."""

import time
import functools
from typing import Any, Callable, TypeVar


F = TypeVar('F', bound=Callable[..., Any])


def timer(func: F) -> F:
    """Decorator to measure and print function execution time.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time

    Example:
        @timer
        def slow_function():
            time.sleep(1)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper


def retry(max_attempts: int = 3):
    """Decorator to retry a function if it raises an exception.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)

    Returns:
        Decorator function

    Raises:
        ValueError: If max_attempts is less than 1
        Exception: Re-raises the last exception if all attempts fail

    Example:
        @retry(max_attempts=5)
        def flaky_api_call():
            response = requests.get(url)
            return response.json()
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

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
                        continue
            raise last_exception
        return wrapper
    return decorator


def memoize(func: F) -> F:
    """Decorator to cache function results based on arguments.

    Caches the return value of a function for each unique set of arguments.
    Only works with hashable arguments.

    Args:
        func: The function whose results should be cached

    Returns:
        Wrapped function with caching behavior

    Example:
        @memoize
        def expensive_computation(n):
            return sum(i**2 for i in range(n))
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper


def validate_types(*expected_types):
    """Decorator to validate function argument types at runtime.

    Checks that the function arguments match the expected types in order.
    Raises TypeError if any argument doesn't match its expected type.

    Args:
        *expected_types: Expected types for each positional argument

    Returns:
        Decorator function

    Raises:
        TypeError: If argument count or types don't match expectations

    Example:
        @validate_types(int, str, float)
        def process_data(id, name, score):
            return f"{name} (#{id}): {score}"
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"{func.__name__} expected {len(expected_types)} arguments, "
                    f"got {len(args)}"
                )

            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"{func.__name__} argument {i} expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )

            return func(*args, **kwargs)
        return wrapper
    return decorator
