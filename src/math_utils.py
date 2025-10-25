"""Mathematical utility functions for common operations."""

import math
from typing import List


def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"Factorial requires an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Generate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"Fibonacci requires an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: An integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(f"is_prime requires an integer, got {type(n).__name__}")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Find the greatest common divisor of two numbers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd requires two integers")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Find the least common multiple of two numbers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("lcm requires two integers")

    if a == 0 and b == 0:
        raise ValueError("lcm is not defined for both arguments being zero")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def mean(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: A list of numeric values

    Returns:
        The arithmetic mean of the numbers

    Raises:
        TypeError: If numbers is not a list
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(f"mean requires a list, got {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of an empty list")

    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """Find the median value of a list of numbers.

    Args:
        numbers: A list of numeric values

    Returns:
        The median value (middle value or average of two middle values)

    Raises:
        TypeError: If numbers is not a list
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(f"median requires a list, got {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate median of an empty list")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
