"""Mathematical utility functions for common operations."""

import math


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n (n!)

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("factorial() argument must be an integer")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """
    Generate the nth Fibonacci number (0-indexed).

    The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Args:
        n (int): A non-negative integer representing the position in the sequence

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("fibonacci() argument must be an integer")
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
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
    Check if a number is prime.

    Args:
        n (int): The number to check

    Returns:
        bool: True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("is_prime() argument must be an integer")
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


def gcd(a, b):
    """
    Find the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The greatest common divisor of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd() arguments must be integers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Find the least common multiple of two integers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The least common multiple of a and b

    Raises:
        TypeError: If a or b is not an integer
        ValueError: If both a and b are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("lcm() arguments must be integers")
    if a == 0 and b == 0:
        raise ValueError("lcm(0, 0) is undefined")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def mean(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        numbers (list): A list of numeric values

    Returns:
        float: The arithmetic mean of the numbers

    Raises:
        ValueError: If the list is empty
        TypeError: If numbers is not a list or contains non-numeric values
    """
    if not isinstance(numbers, list):
        raise TypeError("mean() argument must be a list")
    if len(numbers) == 0:
        raise ValueError("mean() requires at least one number")
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError("mean() requires all elements to be numeric")


def median(numbers):
    """
    Find the median value of a list of numbers.

    Args:
        numbers (list): A list of numeric values

    Returns:
        float: The median value (middle value for odd-length lists,
               average of two middle values for even-length lists)

    Raises:
        ValueError: If the list is empty
        TypeError: If numbers is not a list or contains non-numeric values
    """
    if not isinstance(numbers, list):
        raise TypeError("median() argument must be a list")
    if len(numbers) == 0:
        raise ValueError("median() requires at least one number")
    try:
        sorted_numbers = sorted(numbers)
    except TypeError:
        raise TypeError("median() requires all elements to be numeric")

    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
