from typing import Callable
from functools import wraps
from .operations import memoize


def validate_positive(func: Callable) -> Callable:
    """Decorator for enforcing positive integer inputs."""
    @wraps(func)
    def wrapper(n: int) -> any:
        if not isinstance(n, int):
            raise TypeError(f"Expected integer, got {type(n).__name__}")
        if n <= 0:
            raise ValueError(f"Expected positive integer, got {n}")
        return func(n)
    return wrapper


@validate_positive
def is_prime(n: int) -> bool:
    """Check if a number is prime with validation."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


@memoize
def fibonacci(n: int) -> int:
    """Generate the nth Fibonacci number with memoization."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_perfect_square(n: int) -> bool:
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    if n == 0:
        return True
    root = int(n ** 0.5)
    return root * root == n
