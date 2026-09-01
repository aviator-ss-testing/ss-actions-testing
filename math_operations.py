"""
Math Operations Module

A comprehensive module providing basic mathematical operations with proper error handling
and input validation. Designed for integration testing scenarios.
"""


def add(a, b):
    """
    Add two numbers together.

    Args:
        a (int or float): First number to add
        b (int or float): Second number to add

    Returns:
        int or float: Sum of a and b

    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (int or float): Number to subtract from
        b (int or float): Number to subtract

    Returns:
        int or float: Difference of a and b (a - b)

    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a (int or float): First number to multiply
        b (int or float): Second number to multiply

    Returns:
        int or float: Product of a and b

    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    return a * b


def divide(a, b):
    """
    Divide first number by second number.

    Args:
        a (int or float): Dividend (number to be divided)
        b (int or float): Divisor (number to divide by)

    Returns:
        float: Quotient of a and b (a / b)

    Raises:
        TypeError: If either argument is not a number
        ZeroDivisionError: If divisor (b) is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """
    Raise base to the power of exponent.

    Args:
        base (int or float): The base number
        exponent (int or float): The exponent to raise base to

    Returns:
        int or float: Result of base raised to exponent

    Raises:
        TypeError: If either argument is not a number
        OverflowError: If the result is too large to represent
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")

    try:
        result = base ** exponent
        if isinstance(result, (int, float)) and abs(result) == float('inf'):
            raise OverflowError("Result is too large to represent")
        return result
    except OverflowError:
        raise OverflowError("Result is too large to represent")


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer to calculate factorial for

    Returns:
        int: Factorial of n (n!)

    Raises:
        TypeError: If argument is not an integer
        ValueError: If argument is negative
        OverflowError: If the result is too large to represent
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # Handle boundary conditions
    if n <= 1:
        return 1

    # Check for potential overflow for very large numbers
    if n > 1000:
        raise OverflowError("Factorial result would be too large to represent")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result