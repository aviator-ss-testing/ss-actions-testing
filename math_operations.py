"""
Mathematical utility functions for testing purposes.

This module provides common mathematical operations including basic arithmetic,
statistical calculations, and number utilities with comprehensive error handling.
"""

from typing import List, Union, Tuple
import math


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Raises:
        TypeError: If inputs are not numbers
        OverflowError: If result exceeds system limits

    Examples:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers, got {type(a).__name__} and {type(b).__name__}")

    if math.isinf(a) or math.isinf(b):
        raise OverflowError("Cannot add infinite values")

    if math.isnan(a) or math.isnan(b):
        return float('nan')

    result = a + b

    if math.isinf(result):
        raise OverflowError("Addition result exceeds system limits")

    return result


def multiply_list(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Multiply all numbers in a list together.

    Args:
        numbers: List of numbers to multiply

    Returns:
        Product of all numbers in the list

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty

    Examples:
        >>> multiply_list([2, 3, 4])
        24
        >>> multiply_list([1.5, 2])
        3.0
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")

    if not numbers:
        raise ValueError("Cannot multiply empty list")

    result = 1
    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, found {type(num).__name__} at index {i}")

        if math.isnan(num):
            return float('nan')

        if math.isinf(num):
            if result == 0:
                return float('nan')
            elif result > 0:
                return float('inf') if num > 0 else float('-inf')
            else:
                return float('-inf') if num > 0 else float('inf')

        result *= num

        if math.isinf(result):
            return result

    return result


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        Arithmetic mean as a float

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty

    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([2.5, 3.5])
        3.0
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")

    if not numbers:
        raise ValueError("Cannot calculate average of empty list")

    total = 0
    valid_count = 0

    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numbers, found {type(num).__name__} at index {i}")

        if math.isnan(num):
            continue

        if math.isinf(num):
            return float('inf') if num > 0 else float('-inf')

        total += num
        valid_count += 1

    if valid_count == 0:
        return float('nan')

    return total / valid_count


def find_prime_factors(n: int) -> List[int]:
    """
    Find all prime factors of a positive integer.

    Args:
        n: Positive integer to factorize

    Returns:
        List of prime factors in ascending order

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is not positive

    Examples:
        >>> find_prime_factors(12)
        [2, 2, 3]
        >>> find_prime_factors(17)
        [17]
        >>> find_prime_factors(1)
        []
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return []

    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers in the Fibonacci sequence.

    Args:
        n: Number of Fibonacci numbers to generate (non-negative)

    Returns:
        List containing the first n Fibonacci numbers

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative

    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return []

    if n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        next_fib = sequence[i-1] + sequence[i-2]
        sequence.append(next_fib)

    return sequence