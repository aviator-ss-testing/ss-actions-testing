"""
Decorator utilities for function enhancement.

This module provides decorators for caching, validation, and performance monitoring.
"""

import functools
import time


def memoize(func):
    """
    Cache function results based on arguments to avoid redundant calculations.

    This decorator stores previously computed results in a dictionary, using the
    function arguments as the cache key. Subsequent calls with the same arguments
    return the cached result instead of recomputing.

    Args:
        func: The function to be memoized

    Returns:
        The wrapped function with memoization capabilities

    Examples:
        >>> @memoize
        ... def expensive_calculation(n):
        ...     return n ** 2
        >>> expensive_calculation(5)
        25
        >>> expensive_calculation(5)  # Returns cached result
        25
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)

        return cache[cache_key]

    return wrapper


def validate_positive(func):
    """
    Ensure all numeric arguments are positive.

    This decorator validates that all arguments passed to the decorated function
    are positive numbers (greater than 0). Raises ValueError if any argument is
    not positive.

    Args:
        func: The function to be validated

    Returns:
        The wrapped function with positive validation

    Raises:
        ValueError: If any argument is not positive

    Examples:
        >>> @validate_positive
        ... def area(length, width):
        ...     return length * width
        >>> area(5, 3)
        15
        >>> area(-5, 3)  # Raises ValueError
        Traceback (most recent call last):
        ...
        ValueError: All arguments must be positive numbers
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())

        for arg in all_args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("All arguments must be positive numbers")

        return func(*args, **kwargs)

    return wrapper


def validate_numeric(func):
    """
    Ensure all arguments are numeric (int or float).

    This decorator validates that all arguments passed to the decorated function
    are either integers or floats. Raises ValueError if any argument is not numeric.

    Args:
        func: The function to be validated

    Returns:
        The wrapped function with numeric validation

    Raises:
        ValueError: If any argument is not numeric

    Examples:
        >>> @validate_numeric
        ... def calculate(a, b):
        ...     return a + b
        >>> calculate(5, 3)
        8
        >>> calculate("5", 3)  # Raises ValueError
        Traceback (most recent call last):
        ...
        ValueError: All arguments must be numeric (int or float)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())

        for arg in all_args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numeric (int or float)")

        return func(*args, **kwargs)

    return wrapper


def timer(func):
    """
    Measure and print function execution time.

    This decorator measures how long a function takes to execute and prints
    the execution time in seconds. Useful for performance profiling and optimization.

    Args:
        func: The function to be timed

    Returns:
        The wrapped function with timing capabilities

    Examples:
        >>> @timer
        ... def slow_function():
        ...     return sum(range(1000000))
        >>> result = slow_function()  # Prints: Function 'slow_function' executed in 0.0234 seconds
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")

        return result

    return wrapper
