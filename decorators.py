import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator that prints the execution time of the wrapped function.

    Args:
        func: The function to be timed

    Returns:
        The wrapped function that prints execution time

    Examples:
        >>> @timer
        ... def slow_function():
        ...     time.sleep(1)
        ...     return "done"
        >>> slow_function()
        Function 'slow_function' took 1.0001 seconds
        'done'
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    Decorator that caches function results based on arguments.
    Uses a simple dictionary-based cache to store results.

    Args:
        func: The function whose results should be cached

    Returns:
        The wrapped function with caching capability

    Examples:
        >>> @memoize
        ... def expensive_function(n):
        ...     time.sleep(1)
        ...     return n * 2
        >>> expensive_function(5)  # Takes 1 second
        10
        >>> expensive_function(5)  # Returns instantly from cache
        10
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache:
            return cache[cache_key]

        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return wrapper


def repeat(n: int) -> Callable:
    """
    Decorator that executes a function n times and returns a list of results.

    Args:
        n: The number of times to execute the function

    Returns:
        A decorator that wraps the function to execute it n times

    Examples:
        >>> @repeat(3)
        ... def get_random():
        ...     return 42
        >>> get_random()
        [42, 42, 42]

        >>> @repeat(0)
        ... def get_value():
        ...     return "test"
        >>> get_value()
        []
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator
