"""String utility functions for common string operations and text processing."""


def reverse_string(s):
    """Reverse a string.

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
    """Check if a string is a palindrome (case-insensitive).

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
    """Count the number of words in a text.

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
    """Convert a string to title case.

    Args:
        s (str): The string to convert

    Returns:
        str: The string in title case

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    return s.title()


def remove_duplicates(s):
    """Remove consecutive duplicate characters from a string.

    Args:
        s (str): The string to process

    Returns:
        str: The string with consecutive duplicates removed

    Raises:
        TypeError: If s is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    if not s:
        return s

    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(s[i])
    return ''.join(result)


def truncate(s, length, suffix='...'):
    """Truncate a string to a specified length with an optional suffix.

    Args:
        s (str): The string to truncate
        length (int): The maximum length (must be non-negative)
        suffix (str): The suffix to append to truncated strings (default: '...')

    Returns:
        str: The truncated string with suffix, or original if within length

    Raises:
        TypeError: If s or suffix is not a string, or length is not an integer
        ValueError: If length is negative
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string for s, got {type(s).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"Expected string for suffix, got {type(suffix).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"Expected int for length, got {type(length).__name__}")
    if length < 0:
        raise ValueError("Length must be non-negative")

    if len(s) <= length:
        return s
    return s[:length] + suffix
