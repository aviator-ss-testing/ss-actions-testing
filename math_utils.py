"""
Mathematical utility functions module.

This module provides basic mathematical operations including factorial calculation,
greatest common divisor, least common multiple, prime number checking, and
Fibonacci sequence generation.
"""


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n (n!)

    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise ValueError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    """
    Calculate the greatest common divisor using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        ValueError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("GCD inputs must be integers")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculate the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b

    Raises:
        ValueError: If inputs are not integers or if both are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("LCM inputs must be integers")

    if a == 0 and b == 0:
        raise ValueError("LCM is not defined when both numbers are zero")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        True if n is prime, False otherwise

    Raises:
        ValueError: If n is not an integer
    """
    if not isinstance(n, int):
        raise ValueError("Prime check input must be an integer")

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


def fibonacci(n):
    """
    Generate the first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate (non-negative integer)

    Returns:
        List of the first n Fibonacci numbers

    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int):
        raise ValueError("Fibonacci input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci input must be non-negative")

    if n == 0:
        return []

    if n == 1:
        return [0]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence
