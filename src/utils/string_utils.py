"""String manipulation utilities.

This module provides common string manipulation functions including
reversing, palindrome checking, title casing, and word counting.
"""


def reverse_string(s: str) -> str:
    """Reverse a string.

    Args:
        s: The string to reverse.

    Returns:
        The reversed string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive).

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("hello")
        False
    """
    normalized = s.lower()
    return normalized == normalized[::-1]


def title_case(s: str) -> str:
    """Convert a string to title case.

    Args:
        s: The string to convert.

    Returns:
        The string in title case.

    Examples:
        >>> title_case("hello world")
        'Hello World'
        >>> title_case("the quick brown fox")
        'The Quick Brown Fox'
    """
    return s.title()


def count_words(s: str) -> int:
    """Count the number of words in a string.

    Words are defined as sequences of non-whitespace characters
    separated by whitespace.

    Args:
        s: The string to count words in.

    Returns:
        The number of words in the string.

    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("  hello   world  ")
        2
        >>> count_words("")
        0
    """
    if not s or not s.strip():
        return 0
    return len(s.split())
