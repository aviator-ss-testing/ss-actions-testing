"""
Mathematical operations module providing arithmetic, advanced math, statistical, and geometric functions.
"""

import math
from collections import Counter
from typing import List, Union, Tuple


# Basic arithmetic functions
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a."""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# Advanced math functions
def factorial(n: int) -> int:
    """Calculate the factorial of n. Raises ValueError if n is negative."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number. Raises ValueError if n is negative."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prime_checker(n: int) -> bool:
    """Check if n is a prime number. Returns False for negative numbers and 0, 1."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two integers using Euclidean algorithm."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate the Least Common Multiple of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# Statistical functions
def mean(data: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate mean of empty list")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")
    return sum(data) / len(data)


def median(data: List[Union[int, float]]) -> float:
    """Calculate the median of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate median of empty list")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")

    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return float(sorted_data[n // 2])


def mode(data: List[Union[int, float]]) -> List[Union[int, float]]:
    """Calculate the mode(s) of a list of numbers. Returns list of most frequent values."""
    if not data:
        raise ValueError("Cannot calculate mode of empty list")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")

    counter = Counter(data)
    max_count = max(counter.values())
    return [value for value, count in counter.items() if count == max_count]


def standard_deviation(data: List[Union[int, float]]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate standard deviation of empty list")
    if len(data) == 1:
        return 0.0
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")

    data_mean = mean(data)
    variance = sum((x - data_mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


# Geometric functions
def area_circle(radius: Union[int, float]) -> float:
    """Calculate the area of a circle given its radius."""
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def area_rectangle(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """Calculate the area of a rectangle given its length and width."""
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


def area_triangle(base: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """Calculate the area of a triangle given its base and height."""
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers")
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def pythagorean_theorem(a: Union[int, float], b: Union[int, float]) -> float:
    """Calculate the hypotenuse of a right triangle given two sides using Pythagorean theorem."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both sides must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Side lengths cannot be negative")
    return math.sqrt(a ** 2 + b ** 2)