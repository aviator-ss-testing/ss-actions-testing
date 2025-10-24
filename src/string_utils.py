"""
String Utilities Module

This module provides common string manipulation and text processing functions.
"""


def reverse_string(s):
    """
    Reverse a string.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome (case-insensitive).

    Args:
        s (str): The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    normalized = s.lower()
    return normalized == normalized[::-1]


def word_count(text):
    """
    Count the number of words in text.

    Args:
        text (str): The text to count words in

    Returns:
        int: The number of words in the text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")
    if not text or text.isspace():
        return 0
    return len(text.split())


def title_case(s):
    """
    Convert string to title case.

    Args:
        s (str): The string to convert

    Returns:
        str: The string converted to title case

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s.title()


def remove_duplicates(s):
    """
    Remove consecutive duplicate characters from a string.

    Args:
        s (str): The string to process

    Returns:
        str: The string with consecutive duplicate characters removed

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    if not s:
        return s

    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result.append(s[i])

    return ''.join(result)


def truncate(s, length, suffix='...'):
    """
    Truncate string with ellipsis if it exceeds the specified length.

    Args:
        s (str): The string to truncate
        length (int): The maximum length before truncation
        suffix (str): The suffix to append when truncating (default: '...')

    Returns:
        str: The truncated string with suffix, or original string if within length

    Raises:
        TypeError: If s or suffix is not a string, or length is not an integer
        ValueError: If length is negative
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string for s, got {type(s).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"Expected int for length, got {type(length).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"Expected string for suffix, got {type(suffix).__name__}")
    if length < 0:
        raise ValueError("Length must be non-negative")

    if len(s) <= length:
        return s

    return s[:length] + suffix
