"""Simple calculator module for testing CI rework."""


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exp: int) -> int:
    """Raise base to the power of exp."""
    # BUG: returns string but annotated as int (type error)
    return f"{base}^{exp}"
