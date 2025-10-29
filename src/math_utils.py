"""
Mathematical utility functions with input validation.

This module provides basic mathematical operations including factorial, GCD,
prime checking, and Fibonacci sequence generation.
"""

import functools


def validate_positive(func):
    """
    Decorator to ensure numeric inputs are positive.
    
    Raises ValueError if any numeric argument is negative.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Function {func.__name__} requires positive arguments, got {arg}")
        return func(*args, **kwargs)
    return wrapper


def factorial(n):
    """
    Calculate factorial of a number with input validation.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
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


def gcd(a, b):
    """
    Calculate greatest common divisor using Euclidean algorithm.
    
    Args:
        a (int): First integer
        b (int): Second integer
        
    Returns:
        int: Greatest common divisor of a and b
        
    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("GCD inputs must be integers")
    
    # Handle negative numbers by using absolute values
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Prime check input must be an integer")
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


@validate_positive
def fibonacci(n):
    """
    Generate nth Fibonacci number.
    
    Args:
        n (int): Position in Fibonacci sequence (must be positive)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is not positive (via @validate_positive decorator)
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci input must be an integer")
    
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b