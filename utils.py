"""
Utility functions module containing string manipulation, numeric operations, and list processing functions.
"""
from typing import List, Any, Union
import math


# String manipulation functions
def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string

    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        text: The string to capitalize

    Returns:
        String with each word capitalized

    Example:
        >>> capitalize_words("hello world")
        "Hello World"
    """
    return ' '.join(word.capitalize() for word in text.split())


def clean_whitespace(text: str) -> str:
    """
    Remove leading/trailing whitespace and normalize internal whitespace to single spaces.

    Args:
        text: The string to clean

    Returns:
        Cleaned string with normalized whitespace

    Example:
        >>> clean_whitespace("  hello    world  ")
        "hello world"
    """
    return ' '.join(text.split())


# Numeric utility functions
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Example:
        >>> fibonacci(5)
        5
    """
    if n < 0:
        raise ValueError("Fibonacci number position cannot be negative")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: The number to calculate factorial for

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: The number to check

    Returns:
        True if the number is prime, False otherwise

    Example:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
    """
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


# List processing functions
def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list structure.

    Args:
        nested_list: A list that may contain sublists

    Returns:
        A flattened list with all elements at the same level

    Example:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def unique_elements(items: List[Any]) -> List[Any]:
    """
    Return a list with unique elements while preserving order.

    Args:
        items: The list to remove duplicates from

    Returns:
        A list with unique elements in their first occurrence order

    Example:
        >>> unique_elements([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def filter_even(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Filter a list to return only even numbers.

    Args:
        numbers: A list of numbers

    Returns:
        A list containing only the even numbers

    Example:
        >>> filter_even([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return [num for num in numbers if isinstance(num, (int, float)) and num % 2 == 0]