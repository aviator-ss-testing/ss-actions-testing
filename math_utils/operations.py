from typing import Callable, Any
from functools import wraps


class memoize:
    """Decorator for caching function results based on arguments."""

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.cache = {}

    def __call__(self, *args: Any) -> Any:
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b with zero division validation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


@memoize
def factorial(n: int) -> int:
    """Calculate factorial of n with memoization."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
