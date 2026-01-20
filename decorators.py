"""Function decorators for timing, retrying, caching, and type validation."""
import time
import functools
from typing import Callable, Any, TypeVar, Tuple

F = TypeVar('F', bound=Callable[..., Any])

def timer(func: F) -> F:
    """Decorator to measure and print function execution time.
    Usage: @timer decorates functions to log their execution time.
    Example: @timer\n    def slow_function(): ..."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result
    return wrapper

def retry(max_attempts: int) -> Callable[[F], F]:
    """Decorator to retry a function if it raises an exception.
    Args: max_attempts - Maximum number of attempts (must be >= 1)
    Usage: @retry(max_attempts=3) decorates functions to retry on failure.
    Example: @retry(3)\n    def flaky_function(): ...
    Raises: ValueError if max_attempts < 1"""
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
            if last_exception:
                raise last_exception
        return wrapper
    return decorator

def memoize(func: F) -> F:
    """Decorator to cache function results for given arguments.
    Usage: @memoize decorates functions to cache return values.
    Example: @memoize\n    def expensive_function(x): ...
    Note: Adds cache_clear() method to clear the cache."""
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

def validate_types(*expected_types: type) -> Callable[[F], F]:
    """Decorator to validate function argument types at runtime.
    Args: *expected_types - Expected types for each positional argument
    Usage: @validate_types(int, str) validates first arg is int, second is str.
    Example: @validate_types(int, int)\n    def add(a, b): ...
    Raises: TypeError if argument count or types don't match"""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(f"{func.__name__} expected {len(expected_types)} arguments, got {len(args)}")
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"{func.__name__} argument {i} must be {expected_type.__name__}, not {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
