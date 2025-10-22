"""Reusable decorators for function enhancement.

This module provides decorators for timing function execution, caching results,
and validating function arguments.
"""

import functools
import time


def timer(func):
    """Decorator that measures and prints function execution time.

    This decorator wraps a function and prints the time it took to execute.
    Useful for performance profiling and optimization.

    Args:
        func: The function to be timed.

    Returns:
        The wrapped function that measures execution time.

    Example:
        >>> @timer
        ... def slow_function(n):
        ...     return sum(range(n))
        >>> result = slow_function(1000000)
        slow_function executed in 0.0234 seconds
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def memoize(func):
    """Decorator implementing simple caching for expensive function calls.

    This decorator caches the results of function calls based on their arguments.
    Subsequent calls with the same arguments return the cached result instantly
    without re-executing the function. Works with hashable arguments only.

    Args:
        func: The function whose results should be cached.

    Returns:
        The wrapped function with caching capability.

    Example:
        >>> @memoize
        ... def expensive_calculation(n):
        ...     return sum(i**2 for i in range(n))
        >>> result1 = expensive_calculation(1000000)  # Takes time
        >>> result2 = expensive_calculation(1000000)  # Returns instantly from cache

    Note:
        This decorator is best suited for pure functions (functions that always
        return the same output for the same input and have no side effects).
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from args and kwargs
        # Convert kwargs to a sorted tuple of items for hashability
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache:
            return cache[cache_key]

        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return wrapper


def validate_positive(func):
    """Decorator ensuring all numeric arguments are positive.

    This decorator validates that all numeric arguments (int or float) passed
    to the function are positive (greater than zero). Raises ValueError if any
    numeric argument is zero or negative.

    Args:
        func: The function whose numeric arguments should be validated.

    Returns:
        The wrapped function with argument validation.

    Raises:
        ValueError: If any numeric argument is not positive (i.e., <= 0).

    Example:
        >>> @validate_positive
        ... def calculate_area(length, width):
        ...     return length * width
        >>> calculate_area(5, 10)
        50
        >>> calculate_area(-5, 10)
        ValueError: All numeric arguments must be positive
        >>> calculate_area(0, 10)
        ValueError: All numeric arguments must be positive

    Note:
        This decorator only validates int and float types. Other types are passed
        through without validation.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("All numeric arguments must be positive")

        # Check all keyword arguments
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError("All numeric arguments must be positive")

        return func(*args, **kwargs)

    return wrapper
