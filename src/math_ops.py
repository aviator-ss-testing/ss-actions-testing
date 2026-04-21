def add(a, b):
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """Subtract b from a.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """Divide a by b.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Quotient of a divided by b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        Result of base raised to exponent
    """
    return base ** exponent


def factorial(n):
    """Calculate the factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int):
        raise ValueError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    """Calculate the greatest common divisor using Euclid's algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b
    """
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a
