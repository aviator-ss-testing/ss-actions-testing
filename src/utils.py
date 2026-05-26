"""
Utility functions and decorators for common operations.

This module provides decorators for timing, memoization, and validation,
as well as utility functions for clamping values and chunking lists.
"""

import time
import functools
from typing import Any, Callable, List, TypeVar, Union

T = TypeVar('T')


def timer(func: Callable) -> Callable:
    """
    Decorator to measure and print the execution time of a function.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time

    Examples:
        >>> @timer
        ... def slow_function():
        ...     time.sleep(1)
        >>> slow_function()  # doctest: +SKIP
        Function 'slow_function' took 1.0012 seconds
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed:.4f} seconds")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    Decorator to cache function results for repeated calls with same arguments.

    Args:
        func: The function whose results should be cached

    Returns:
        Wrapped function with memoization

    Examples:
        >>> @memoize
        ... def expensive_calculation(n):
        ...     return n * n
        >>> expensive_calculation(5)
        25
        >>> expensive_calculation(5)  # Returns cached result
        25
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


def validate_positive(func: Callable) -> Callable:
    """
    Decorator to ensure all integer arguments are positive.

    Args:
        func: The function whose arguments should be validated

    Returns:
        Wrapped function with input validation

    Raises:
        ValueError: If any integer argument is not positive

    Examples:
        >>> @validate_positive
        ... def process_positive(n):
        ...     return n * 2
        >>> process_positive(5)
        10
        >>> process_positive(-5)  # doctest: +SKIP
        Traceback (most recent call last):
        ValueError: All integer arguments must be positive
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if isinstance(arg, int) and arg <= 0:
                raise ValueError("All integer arguments must be positive")
        for value in kwargs.values():
            if isinstance(value, int) and value <= 0:
                raise ValueError("All integer arguments must be positive")
        return func(*args, **kwargs)
    return wrapper


def clamp(value: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """
    Clamp a value between minimum and maximum bounds.

    Args:
        value: The value to clamp
        min_val: The minimum allowed value
        max_val: The maximum allowed value

    Returns:
        The clamped value

    Raises:
        TypeError: If arguments are not numeric types
        ValueError: If min_val is greater than max_val

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be numeric, got {type(value).__name__}")
    if not isinstance(min_val, (int, float)):
        raise TypeError(f"Minimum value must be numeric, got {type(min_val).__name__}")
    if not isinstance(max_val, (int, float)):
        raise TypeError(f"Maximum value must be numeric, got {type(max_val).__name__}")

    if min_val > max_val:
        raise ValueError(f"Minimum value ({min_val}) cannot be greater than maximum value ({max_val})")

    return max(min_val, min(value, max_val))


def chunk_list(lst: List[T], size: int) -> List[List[T]]:
    """
    Split a list into chunks of specified size.

    Args:
        lst: The list to split into chunks
        size: The size of each chunk

    Returns:
        A list of chunks (sublists)

    Raises:
        TypeError: If lst is not a list or size is not an integer
        ValueError: If size is less than 1

    Examples:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk_list(['a', 'b', 'c'], 1)
        [['a'], ['b'], ['c']]
        >>> chunk_list([1, 2, 3, 4], 4)
        [[1, 2, 3, 4]]
    """
    if not isinstance(lst, list):
        raise TypeError(f"First argument must be a list, got {type(lst).__name__}")
    if not isinstance(size, int):
        raise TypeError(f"Chunk size must be an integer, got {type(size).__name__}")
    if size < 1:
        raise ValueError("Chunk size must be at least 1")

    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])
    return chunks
