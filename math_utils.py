"""
Mathematical and statistical utility functions.

This module provides common mathematical operations and statistical calculations
with proper input validation and error handling.
"""

from typing import List
from collections import Counter


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"factorial() argument must be an integer, not {type(n).__name__}")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number (0-indexed).

    Args:
        n: A non-negative integer index

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"fibonacci() argument must be an integer, not {type(n).__name__}")
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: An integer to check

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"is_prime() argument must be an integer, not {type(n).__name__}")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"gcd() arguments must be integers, not {type(a).__name__}")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"gcd() arguments must be integers, not {type(b).__name__}")
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"lcm() arguments must be integers, not {type(a).__name__}")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"lcm() arguments must be integers, not {type(b).__name__}")
    if a == 0 and b == 0:
        raise ValueError("lcm(0, 0) is undefined")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def mean(numbers: List[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: A list of numbers

    Returns:
        The arithmetic mean

    Raises:
        TypeError: If numbers is not a list
        ValueError: If numbers is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(f"mean() argument must be a list, not {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("mean() requires at least one number")

    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        numbers: A list of numbers

    Returns:
        The median value

    Raises:
        TypeError: If numbers is not a list
        ValueError: If numbers is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(f"median() argument must be a list, not {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("median() requires at least one number")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]


def mode(numbers: List[float]) -> float:
    """
    Calculate the mode (most frequent value) of a list of numbers.

    Args:
        numbers: A list of numbers

    Returns:
        The most frequent value (if multiple values have the same frequency, returns the first one encountered)

    Raises:
        TypeError: If numbers is not a list
        ValueError: If numbers is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(f"mode() argument must be a list, not {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("mode() requires at least one number")

    counter = Counter(numbers)
    return counter.most_common(1)[0][0]
