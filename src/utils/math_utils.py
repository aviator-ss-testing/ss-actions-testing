"""Mathematical utility functions for common operations."""


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: The number to check

    Returns:
        True if the number is prime, False otherwise

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
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


def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n: The number to calculate factorial for

    Returns:
        The factorial of n (n!)

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers using Euclidean algorithm.

    Args:
        a: First number
        b: Second number

    Returns:
        The greatest common divisor of a and b

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 50)
        50
        >>> gcd(17, 19)
        1
    """
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a
