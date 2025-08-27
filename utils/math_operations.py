"""
Mathematical utility functions module.

This module provides various mathematical operations and calculations
that are commonly used in testing and data processing scenarios.
"""


def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer to calculate the factorial for.
        
    Returns:
        int: The factorial of n (n!).
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
        
    Examples:
        >>> calculate_factorial(0)
        1
        >>> calculate_factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
        
    Raises:
        TypeError: If n is not an integer.
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
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


def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
        
    Returns:
        list: A list containing the first n Fibonacci numbers.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Number of terms cannot be negative")
    
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def greatest_common_divisor(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using Euclidean algorithm.
    
    Args:
        a (int): First integer.
        b (int): Second integer.
        
    Returns:
        int: The greatest common divisor of a and b.
        
    Raises:
        TypeError: If either a or b is not an integer.
        ValueError: If both a and b are zero.
        
    Examples:
        >>> greatest_common_divisor(48, 18)
        6
        >>> greatest_common_divisor(17, 13)
        1
        >>> greatest_common_divisor(0, 5)
        5
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined when both numbers are zero")
    
    a, b = abs(a), abs(b)
    
    while b:
        a, b = b, a % b
    
    return a


def least_common_multiple(a, b):
    """
    Calculate the least common multiple (LCM) of two integers.
    
    Args:
        a (int): First integer.
        b (int): Second integer.
        
    Returns:
        int: The least common multiple of a and b.
        
    Raises:
        TypeError: If either a or b is not an integer.
        ValueError: If either a or b is zero.
        
    Examples:
        >>> least_common_multiple(12, 18)
        36
        >>> least_common_multiple(7, 5)
        35
        >>> least_common_multiple(4, 6)
        12
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined when either number is zero")
    
    a, b = abs(a), abs(b)
    gcd = greatest_common_divisor(a, b)
    
    return (a * b) // gcd