import math


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"factorial() argument must be an integer, not {type(n).__name__}")

    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(f"is_prime() argument must be an integer, not {type(n).__name__}")

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def fibonacci(n):
    """
    Generate the nth Fibonacci number (0-indexed).

    Args:
        n: Non-negative integer index in Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError(f"fibonacci() argument must be an integer, not {type(n).__name__}")

    if n < 0:
        raise ValueError("fibonacci() not defined for negative indices")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def gcd(a, b):
    """
    Find the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd() arguments must be integers")

    a, b = abs(a), abs(b)

    if a == 0:
        return b
    if b == 0:
        return a

    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """
    Find the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("lcm() arguments must be integers")

    if a == 0 and b == 0:
        return 0

    return abs(a * b) // gcd(a, b)
