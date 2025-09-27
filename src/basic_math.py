"""
Basic mathematical operations module.

This module provides fundamental mathematical functions with proper input validation
and error handling for common edge cases.
"""

import math
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b (int if both inputs are int, float otherwise)

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.

    Args:
        a: Number to subtract from (int or float)
        b: Number to subtract (int or float)

    Returns:
        Difference of a and b (int if both inputs are int, float otherwise)

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Product of a and b (int if both inputs are int, float otherwise)

    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Divide first number by second number.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Quotient of a and b as float

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If divisor is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


def power(base: Number, exponent: Number) -> Number:
    """
    Raise base to the power of exponent.

    Args:
        base: Base number (int or float)
        exponent: Exponent (int or float)

    Returns:
        Result of base^exponent (int if both inputs are int and result is whole, float otherwise)

    Raises:
        TypeError: If inputs are not numbers
        ValueError: For invalid operations like negative base with fractional exponent
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    try:
        result = base ** exponent
        # Return int if both inputs are int and result is a whole number
        if isinstance(base, int) and isinstance(exponent, int) and isinstance(result, (int, float)) and result.is_integer():
            return int(result)
        return result
    except (ValueError, OverflowError) as e:
        raise ValueError(f"Invalid power operation: {e}")


def factorial(n: int) -> int:
    """
    Calculate factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n (n!)

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(n, int):
        raise TypeError("Factorial input must be an integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    return math.factorial(n)