"""
Arithmetic utilities module.

This module provides basic arithmetic operations including addition, subtraction,
multiplication, and division with proper type hints and error handling.
"""

from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Add two numbers.

    Args: x: First number
          y: Second number
    Returns: Sum of x and y
    """
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Subtract second number from first number.

    Args: x: Number to subtract from
          y: Number to subtract
    Returns: Difference of x and y
    """
    return x - y


def multiply(x: Number, y: Number) -> Number:
    """Multiply two numbers.

    Args: x: First number
          y: Second number
    Returns: Product of x and y
    """
    return x * y


def divide(x: Number, y: Number) -> float:
    """Divide first number by second number.

    Args: x: Dividend
          y: Divisor
    Returns: Quotient of x divided by y
    Raises: ZeroDivisionError: If y is zero
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y