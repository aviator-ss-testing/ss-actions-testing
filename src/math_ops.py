"""
Mathematical utility functions for common operations.

This module provides basic mathematical operations including factorial,
fibonacci sequence, greatest common divisor, and prime number checking.
"""

from typing import Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number (0-indexed).

    Args:
        n: A non-negative integer representing the position in the sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative indices")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
        >>> gcd(0, 5)
        5
    """
    if not isinstance(a, int):
        raise TypeError(f"First argument must be integer, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Second argument must be integer, got {type(b).__name__}")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: An integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True
