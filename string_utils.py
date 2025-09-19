"""
String Utilities Module

A comprehensive module providing string manipulation functions with proper error handling
and input validation. Designed for integration testing scenarios with support for edge cases,
Unicode characters, and case-insensitive operations.
"""


def reverse_string(s):
    """
    Reverse a string.

    Args:
        s (str or None): String to reverse

    Returns:
        str: Reversed string

    Raises:
        TypeError: If argument is not a string or None
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        raise TypeError("Argument must be a string or None")
    return s[::-1]


def count_vowels(s):
    """
    Count the number of vowels in a string (case-insensitive).

    Args:
        s (str or None): String to count vowels in

    Returns:
        int: Number of vowels found

    Raises:
        TypeError: If argument is not a string or None
    """
    if s is None:
        return 0
    if not isinstance(s, str):
        raise TypeError("Argument must be a string or None")

    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)


def is_palindrome(s):
    """
    Check if a string is a palindrome (case-insensitive, ignoring spaces and punctuation).

    Args:
        s (str or None): String to check

    Returns:
        bool: True if string is a palindrome, False otherwise

    Raises:
        TypeError: If argument is not a string or None
    """
    if s is None:
        return True  # Empty string is considered a palindrome
    if not isinstance(s, str):
        raise TypeError("Argument must be a string or None")

    # Convert to lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Empty string after cleaning is considered a palindrome
    if not cleaned:
        return True

    return cleaned == cleaned[::-1]


def capitalize_words(s):
    """
    Capitalize the first letter of each word in a string.

    Args:
        s (str or None): String to capitalize

    Returns:
        str: String with each word's first letter capitalized

    Raises:
        TypeError: If argument is not a string or None
    """
    if s is None:
        return ""
    if not isinstance(s, str):
        raise TypeError("Argument must be a string or None")

    # Handle empty string
    if not s:
        return ""

    # Split into words, capitalize each, and rejoin
    # This handles multiple spaces and preserves word boundaries
    words = s.split()
    if not words:
        return s  # Return original if only whitespace

    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)