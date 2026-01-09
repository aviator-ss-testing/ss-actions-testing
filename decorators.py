"""
Function decorators for common patterns including timing, retry, caching, and type validation.
"""

import time
import functools
from typing import Callable, Any, TypeVar, cast


F = TypeVar('F', bound=Callable[..., Any])


def timer(func: F) -> F:
    """
    Decorator to measure and print function execution time.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time

    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result
    return cast(F, wrapper)


def retry(max_attempts: int) -> Callable[[F], F]:
    """
    Decorator to retry a function up to max_attempts times on failure.

    Args:
        max_attempts: Maximum number of attempts (must be >= 1)

    Returns:
        Decorator function

    Raises:
        ValueError: If max_attempts < 1

    Usage:
        @retry(max_attempts=3)
        def unreliable_function():
            # Function that might fail
            pass
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        continue
            raise last_exception
        return cast(F, wrapper)
    return decorator


def memoize(func: F) -> F:
    """
    Decorator to cache function results for repeated calls with same arguments.

    Args:
        func: The function to be memoized

    Returns:
        Wrapped function with caching behavior

    Usage:
        @memoize
        def expensive_function(n):
            # Expensive computation
            return result
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()

    return cast(F, wrapper)


def validate_types(*expected_types: type) -> Callable[[F], F]:
    """
    Decorator to validate function argument types at runtime.

    Args:
        *expected_types: Expected types for each positional argument

    Returns:
        Decorator function

    Raises:
        TypeError: If argument count or types don't match

    Usage:
        @validate_types(int, str)
        def greet(count, name):
            return f"Hello {name} " * count
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) != len(expected_types):
                raise TypeError(
                    f"{func.__name__} expects {len(expected_types)} arguments, "
                    f"got {len(args)}"
                )

            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"{func.__name__} argument {i} must be {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )

            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator
