"""
Mathematical Operations Module

This module provides basic and advanced mathematical functions with proper error handling
and type hints for computational scenarios and testing purposes.
"""

from typing import Union, List
import math


# Basic arithmetic functions
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers and return the result."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract second number from first and return the result."""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers and return the result."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide first number by second and return the result.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient as a float

    Raises:
        ZeroDivisionError: If divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# Advanced mathematical functions
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.

    Args:
        n: A non-negative integer representing the position in the sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


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
        raise TypeError("Prime check input must be an integer")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If either input is not an integer
        ValueError: If both inputs are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD inputs must be integers")

    # Handle the case where both numbers are zero
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined when both numbers are zero")

    # Make both numbers positive for the algorithm
    a, b = abs(a), abs(b)

    # Euclidean algorithm
    while b:
        a, b = b, a % b
    return a