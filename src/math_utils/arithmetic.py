"""
Arithmetic utilities module providing basic mathematical operations.

This module contains functions for fundamental arithmetic operations including
addition, subtraction, multiplication, and division with proper error handling.
"""

from typing import Union


Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a divided by b

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
