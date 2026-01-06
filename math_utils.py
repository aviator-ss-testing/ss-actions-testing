"""
Mathematical utility functions for common operations and statistics.
"""

from typing import List
from collections import Counter


def factorial(n: int) -> int:
    """
    Calculate the factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")
    if n < 0:
        raise ValueError("Argument must be non-negative")

    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number (0-indexed).

    Args:
        n: Non-negative integer index

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")
    if n < 0:
        raise ValueError("Argument must be non-negative")

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")

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
    Calculate the greatest common divisor of two integers using Euclid's algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If either argument is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

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
        TypeError: If either argument is not an integer
        ValueError: If both arguments are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    if a == 0 and b == 0:
        raise ValueError("LCM is undefined when both arguments are zero")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def mean(numbers: List[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The mean of the numbers

    Raises:
        TypeError: If numbers is not a list or contains non-numeric values
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of empty list")

    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError("List must contain only numeric values")


def median(numbers: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The median of the numbers

    Raises:
        TypeError: If numbers is not a list or contains non-numeric values
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate median of empty list")

    try:
        sorted_numbers = sorted(numbers)
    except TypeError:
        raise TypeError("List must contain only numeric values")

    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def mode(numbers: List[float]) -> float:
    """
    Calculate the mode (most frequent value) of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        The mode of the numbers (if multiple modes exist, returns the first one encountered)

    Raises:
        TypeError: If numbers is not a list
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mode of empty list")

    try:
        counter = Counter(numbers)
    except TypeError:
        raise TypeError("List must contain only hashable numeric values")

    return counter.most_common(1)[0][0]
