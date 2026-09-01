"""
Mathematical operations module providing basic and intermediate math functions.
"""

import math


def factorial(n):
    """
    Compute the factorial of n.

    Parameters:
        n (int): Non-negative integer to compute factorial for

    Returns:
        int: The factorial of n (n!)

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """
    Return the nth Fibonacci number.

    Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """
    Check if n is a prime number using efficient algorithm.

    Parameters:
        n (int): Number to check for primality

    Returns:
        bool: True if n is prime, False otherwise
    """
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        return False

    if n != int(n):
        return False

    n = int(n)

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using Euclidean algorithm.

    Parameters:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD inputs must be integers")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Compute the least common multiple of a and b.

    Parameters:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("LCM inputs must be integers")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def power(base, exp):
    """
    Compute base raised to the power of exp with special case handling.

    Parameters:
        base (int/float): The base number
        exp (int/float): The exponent

    Returns:
        int/float: base raised to the power of exp

    Special cases:
        - Any number to the power of 0 is 1 (except 0^0 which returns 1)
        - 0 to any positive power is 0
        - Negative exponents return fractional results
    """
    # Handle special case: 0^0
    if base == 0 and exp == 0:
        return 1

    # Handle base of 0
    if base == 0:
        if exp < 0:
            raise ValueError("Cannot raise 0 to a negative power")
        return 0

    # Handle exponent of 0
    if exp == 0:
        return 1

    # Handle negative exponents
    if exp < 0:
        return 1 / power(base, -exp)

    # Handle integer exponents efficiently
    if isinstance(exp, int):
        result = 1
        current_base = base
        current_exp = exp

        # Exponentiation by squaring
        while current_exp > 0:
            if current_exp % 2 == 1:
                result *= current_base
            current_base *= current_base
            current_exp //= 2

        return result

    # For non-integer exponents, use built-in power
    return base ** exp
