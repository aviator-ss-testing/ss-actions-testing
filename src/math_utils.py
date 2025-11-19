from functools import wraps


def validate_numbers(func):
    """
    Decorator that validates inputs are numeric types (int or float).
    Raises TypeError if any argument is not numeric.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"All arguments must be numeric. Got {type(arg).__name__}")
        for value in kwargs.values():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"All arguments must be numeric. Got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper


@validate_numbers
def add(a, b):
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b

    Raises:
        TypeError: If inputs are not numeric
    """
    return a + b


@validate_numbers
def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The product of a and b

    Raises:
        TypeError: If inputs are not numeric
    """
    return a * b


@validate_numbers
def power(base, exponent):
    """
    Raise base to the power of exponent.

    Args:
        base: The base number (int or float)
        exponent: The exponent (int or float)

    Returns:
        base raised to the power of exponent

    Raises:
        TypeError: If inputs are not numeric
    """
    return base ** exponent


def factorial(n):
    """
    Calculate the factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
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
