"""
Arithmetic utility functions for basic mathematical operations.

This module provides fundamental arithmetic operations including:
- Addition and multiplication with variable arguments
- Power operations with validation
- Factorial calculations
- Greatest common divisor (GCD) and least common multiple (LCM)
"""


def add(*args):
    """
    Sum multiple numbers.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        Sum of all arguments, or 0 if no arguments provided

    Examples:
        >>> add(1, 2, 3)
        6
        >>> add(5)
        5
        >>> add()
        0
    """
    return sum(args)


def multiply(*args):
    """
    Multiply multiple numbers.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        Product of all arguments, or 1 if no arguments provided

    Examples:
        >>> multiply(2, 3, 4)
        24
        >>> multiply(5)
        5
        >>> multiply()
        1
    """
    if not args:
        return 1

    result = args[0]
    for num in args[1:]:
        result *= num
    return result


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base ** exponent

    Raises:
        ValueError: If base is negative and exponent is fractional

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(2, -1)
        0.5
    """
    if base < 0 and isinstance(exponent, float) and not exponent.is_integer():
        raise ValueError("Cannot raise negative base to fractional exponent")

    return base ** exponent


def factorial(n):
    """
    Calculate factorial of n (n!).

    Args:
        n: Non-negative integer

    Returns:
        n! = n * (n-1) * (n-2) * ... * 1

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    if not isinstance(n, int):
        raise ValueError("Factorial requires an integer argument")

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
    Calculate greatest common divisor using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 50)
        50
        >>> gcd(17, 13)
        1
    """
    a, b = abs(int(a)), abs(int(b))

    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """
    Calculate least common multiple.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b

    Raises:
        ValueError: If either a or b is zero

    Examples:
        >>> lcm(12, 18)
        36
        >>> lcm(5, 7)
        35
        >>> lcm(10, 15)
        30
    """
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero")

    return abs(int(a) * int(b)) // gcd(a, b)
