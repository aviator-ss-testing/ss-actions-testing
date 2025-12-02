from .utils import validate_numbers


@validate_numbers
def add(a, b):
    """Add two numbers together. Returns the sum of a and b."""
    return a + b


@validate_numbers
def multiply(a, b):
    """Multiply two numbers together. Returns the product of a and b. Raises TypeError if inputs are not numeric."""
    return a * b


@validate_numbers
def power(base, exponent):
    """Raise base to the power of exponent. Returns base ** exponent. Raises TypeError if inputs are not numeric."""
    return base ** exponent


def factorial(n):
    """Calculate the factorial of n (n!). Returns the factorial for non-negative integer n. Raises TypeError if n is not an integer, ValueError if n is negative."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Factorial requires an integer argument")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
