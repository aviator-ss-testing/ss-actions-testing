def add(a: int, b: int) -> int:
    """
    Return the sum of two integers.

    Args:
        a: The first integer
        b: The second integer

    Returns:
        int: The sum of a and b
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    Return the product of two integers.

    Args:
        a: The first integer
        b: The second integer

    Returns:
        int: The product of a and b
    """
    return a * b


def is_even(n: int) -> bool:
    """
    Check if a number is even.

    Args:
        n: The integer to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return n % 2 == 0
